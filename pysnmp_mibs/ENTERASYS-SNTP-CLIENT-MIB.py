# SNMP MIB module (ENTERASYS-SNTP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-SNTP-CLIENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:18 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

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


# MODULE-IDENTITY

etsysSntpClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38)
)
if mibBuilder.loadTexts:
    etsysSntpClientMIB.setRevisions(
        ("2011-03-09 15:56",
         "2003-06-13 18:09")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SntpClientOperModes(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("disabled", 0),
          ("unicast", 1),
          ("multicast", 2),
          ("broadcast", 3),
          ("anycast", 4))
    )


class SntpClientUpdateStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("success", 2),
          ("requestTimedOut", 3),
          ("badDateEncoded", 4),
          ("versionNotSupported", 5),
          ("serverUnsychronized", 6))
    )



# MIB Managed Objects in the order of their OIDs

_EtsysSntpClientObjects_ObjectIdentity = ObjectIdentity
etsysSntpClientObjects = _EtsysSntpClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1)
)
_EtsysSntpClientDevice_ObjectIdentity = ObjectIdentity
etsysSntpClientDevice = _EtsysSntpClientDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 1)
)


class _EtsysSntpClientVersion_Type(Integer32):
    """Custom type etsysSntpClientVersion based on Integer32"""
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


_EtsysSntpClientVersion_Type.__name__ = "Integer32"
_EtsysSntpClientVersion_Object = MibScalar
etsysSntpClientVersion = _EtsysSntpClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 1, 1),
    _EtsysSntpClientVersion_Type()
)
etsysSntpClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientVersion.setStatus("current")
_EtsysSntpClientSupportedMode_Type = SntpClientOperModes
_EtsysSntpClientSupportedMode_Object = MibScalar
etsysSntpClientSupportedMode = _EtsysSntpClientSupportedMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 1, 2),
    _EtsysSntpClientSupportedMode_Type()
)
etsysSntpClientSupportedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientSupportedMode.setStatus("current")


class _EtsysSntpClientMode_Type(SntpClientOperModes):
    """Custom type etsysSntpClientMode based on SntpClientOperModes"""
    defaultBinValue = "1"


_EtsysSntpClientMode_Type.__name__ = "SntpClientOperModes"
_EtsysSntpClientMode_Object = MibScalar
etsysSntpClientMode = _EtsysSntpClientMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 1, 3),
    _EtsysSntpClientMode_Type()
)
etsysSntpClientMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSntpClientMode.setStatus("current")


class _EtsysSntpClientLastUpdateTime_Type(DateAndTime):
    """Custom type etsysSntpClientLastUpdateTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_EtsysSntpClientLastUpdateTime_Type.__name__ = "DateAndTime"
_EtsysSntpClientLastUpdateTime_Object = MibScalar
etsysSntpClientLastUpdateTime = _EtsysSntpClientLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 1, 4),
    _EtsysSntpClientLastUpdateTime_Type()
)
etsysSntpClientLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientLastUpdateTime.setStatus("current")


class _EtsysSntpClientLastAttemptTime_Type(DateAndTime):
    """Custom type etsysSntpClientLastAttemptTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_EtsysSntpClientLastAttemptTime_Type.__name__ = "DateAndTime"
_EtsysSntpClientLastAttemptTime_Object = MibScalar
etsysSntpClientLastAttemptTime = _EtsysSntpClientLastAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 1, 5),
    _EtsysSntpClientLastAttemptTime_Type()
)
etsysSntpClientLastAttemptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientLastAttemptTime.setStatus("current")


class _EtsysSntpClientLastAttemptStatus_Type(SntpClientUpdateStatus):
    """Custom type etsysSntpClientLastAttemptStatus based on SntpClientUpdateStatus"""
    defaultValue = 1


_EtsysSntpClientLastAttemptStatus_Type.__name__ = "SntpClientUpdateStatus"
_EtsysSntpClientLastAttemptStatus_Object = MibScalar
etsysSntpClientLastAttemptStatus = _EtsysSntpClientLastAttemptStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 1, 6),
    _EtsysSntpClientLastAttemptStatus_Type()
)
etsysSntpClientLastAttemptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientLastAttemptStatus.setStatus("current")


class _EtsysSntpClientAuthenticationEnable_Type(TruthValue):
    """Custom type etsysSntpClientAuthenticationEnable based on TruthValue"""
    defaultValue = 2


_EtsysSntpClientAuthenticationEnable_Type.__name__ = "TruthValue"
_EtsysSntpClientAuthenticationEnable_Object = MibScalar
etsysSntpClientAuthenticationEnable = _EtsysSntpClientAuthenticationEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 1, 7),
    _EtsysSntpClientAuthenticationEnable_Type()
)
etsysSntpClientAuthenticationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSntpClientAuthenticationEnable.setStatus("current")
_EtsysSntpClientMaxAuthenticationKeys_Type = Unsigned32
_EtsysSntpClientMaxAuthenticationKeys_Object = MibScalar
etsysSntpClientMaxAuthenticationKeys = _EtsysSntpClientMaxAuthenticationKeys_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 1, 8),
    _EtsysSntpClientMaxAuthenticationKeys_Type()
)
etsysSntpClientMaxAuthenticationKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientMaxAuthenticationKeys.setStatus("current")
_EtsysSntpClientUnicast_ObjectIdentity = ObjectIdentity
etsysSntpClientUnicast = _EtsysSntpClientUnicast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2)
)


class _EtsysSntpClientUnicastPollInterval_Type(Unsigned32):
    """Custom type etsysSntpClientUnicastPollInterval based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16284),
    )


_EtsysSntpClientUnicastPollInterval_Type.__name__ = "Unsigned32"
_EtsysSntpClientUnicastPollInterval_Object = MibScalar
etsysSntpClientUnicastPollInterval = _EtsysSntpClientUnicastPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 1),
    _EtsysSntpClientUnicastPollInterval_Type()
)
etsysSntpClientUnicastPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSntpClientUnicastPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    etsysSntpClientUnicastPollInterval.setUnits("seconds")


class _EtsysSntpClientUnicastPollTimeout_Type(Unsigned32):
    """Custom type etsysSntpClientUnicastPollTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_EtsysSntpClientUnicastPollTimeout_Type.__name__ = "Unsigned32"
_EtsysSntpClientUnicastPollTimeout_Object = MibScalar
etsysSntpClientUnicastPollTimeout = _EtsysSntpClientUnicastPollTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 2),
    _EtsysSntpClientUnicastPollTimeout_Type()
)
etsysSntpClientUnicastPollTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSntpClientUnicastPollTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysSntpClientUnicastPollTimeout.setUnits("seconds")


class _EtsysSntpClientUnicastPollRetry_Type(Unsigned32):
    """Custom type etsysSntpClientUnicastPollRetry based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EtsysSntpClientUnicastPollRetry_Type.__name__ = "Unsigned32"
_EtsysSntpClientUnicastPollRetry_Object = MibScalar
etsysSntpClientUnicastPollRetry = _EtsysSntpClientUnicastPollRetry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 3),
    _EtsysSntpClientUnicastPollRetry_Type()
)
etsysSntpClientUnicastPollRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSntpClientUnicastPollRetry.setStatus("current")


class _EtsysSntpClientUServerMaxEntries_Type(Unsigned32):
    """Custom type etsysSntpClientUServerMaxEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EtsysSntpClientUServerMaxEntries_Type.__name__ = "Unsigned32"
_EtsysSntpClientUServerMaxEntries_Object = MibScalar
etsysSntpClientUServerMaxEntries = _EtsysSntpClientUServerMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 4),
    _EtsysSntpClientUServerMaxEntries_Type()
)
etsysSntpClientUServerMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientUServerMaxEntries.setStatus("current")


class _EtsysSntpClientUServerCurrEntries_Type(Gauge32):
    """Custom type etsysSntpClientUServerCurrEntries based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EtsysSntpClientUServerCurrEntries_Type.__name__ = "Gauge32"
_EtsysSntpClientUServerCurrEntries_Object = MibScalar
etsysSntpClientUServerCurrEntries = _EtsysSntpClientUServerCurrEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 5),
    _EtsysSntpClientUServerCurrEntries_Type()
)
etsysSntpClientUServerCurrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientUServerCurrEntries.setStatus("current")
_EtsysSntpClientUServerTable_Object = MibTable
etsysSntpClientUServerTable = _EtsysSntpClientUServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 6)
)
if mibBuilder.loadTexts:
    etsysSntpClientUServerTable.setStatus("current")
_EtsysSntpClientUServerEntry_Object = MibTableRow
etsysSntpClientUServerEntry = _EtsysSntpClientUServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 6, 1)
)
etsysSntpClientUServerEntry.setIndexNames(
    (0, "ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUServerAddrType"),
    (0, "ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUServerAddr"),
)
if mibBuilder.loadTexts:
    etsysSntpClientUServerEntry.setStatus("current")
_EtsysSntpClientUServerAddrType_Type = InetAddressType
_EtsysSntpClientUServerAddrType_Object = MibTableColumn
etsysSntpClientUServerAddrType = _EtsysSntpClientUServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 6, 1, 1),
    _EtsysSntpClientUServerAddrType_Type()
)
etsysSntpClientUServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysSntpClientUServerAddrType.setStatus("current")


class _EtsysSntpClientUServerAddr_Type(InetAddress):
    """Custom type etsysSntpClientUServerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EtsysSntpClientUServerAddr_Type.__name__ = "InetAddress"
_EtsysSntpClientUServerAddr_Object = MibTableColumn
etsysSntpClientUServerAddr = _EtsysSntpClientUServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 6, 1, 2),
    _EtsysSntpClientUServerAddr_Type()
)
etsysSntpClientUServerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysSntpClientUServerAddr.setStatus("current")


class _EtsysSntpClientUServerPrecedence_Type(Unsigned32):
    """Custom type etsysSntpClientUServerPrecedence based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EtsysSntpClientUServerPrecedence_Type.__name__ = "Unsigned32"
_EtsysSntpClientUServerPrecedence_Object = MibTableColumn
etsysSntpClientUServerPrecedence = _EtsysSntpClientUServerPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 6, 1, 3),
    _EtsysSntpClientUServerPrecedence_Type()
)
etsysSntpClientUServerPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSntpClientUServerPrecedence.setStatus("current")


class _EtsysSntpClientUServerLastUpdateTime_Type(DateAndTime):
    """Custom type etsysSntpClientUServerLastUpdateTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_EtsysSntpClientUServerLastUpdateTime_Type.__name__ = "DateAndTime"
_EtsysSntpClientUServerLastUpdateTime_Object = MibTableColumn
etsysSntpClientUServerLastUpdateTime = _EtsysSntpClientUServerLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 6, 1, 4),
    _EtsysSntpClientUServerLastUpdateTime_Type()
)
etsysSntpClientUServerLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientUServerLastUpdateTime.setStatus("current")


class _EtsysSntpClientUServerLastAttemptTime_Type(DateAndTime):
    """Custom type etsysSntpClientUServerLastAttemptTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_EtsysSntpClientUServerLastAttemptTime_Type.__name__ = "DateAndTime"
_EtsysSntpClientUServerLastAttemptTime_Object = MibTableColumn
etsysSntpClientUServerLastAttemptTime = _EtsysSntpClientUServerLastAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 6, 1, 5),
    _EtsysSntpClientUServerLastAttemptTime_Type()
)
etsysSntpClientUServerLastAttemptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientUServerLastAttemptTime.setStatus("current")


class _EtsysSntpClientUServerLastAttemptStatus_Type(SntpClientUpdateStatus):
    """Custom type etsysSntpClientUServerLastAttemptStatus based on SntpClientUpdateStatus"""
    defaultValue = 1


_EtsysSntpClientUServerLastAttemptStatus_Type.__name__ = "SntpClientUpdateStatus"
_EtsysSntpClientUServerLastAttemptStatus_Object = MibTableColumn
etsysSntpClientUServerLastAttemptStatus = _EtsysSntpClientUServerLastAttemptStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 6, 1, 6),
    _EtsysSntpClientUServerLastAttemptStatus_Type()
)
etsysSntpClientUServerLastAttemptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientUServerLastAttemptStatus.setStatus("current")
_EtsysSntpClientUServerNumRequests_Type = Counter32
_EtsysSntpClientUServerNumRequests_Object = MibTableColumn
etsysSntpClientUServerNumRequests = _EtsysSntpClientUServerNumRequests_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 6, 1, 7),
    _EtsysSntpClientUServerNumRequests_Type()
)
etsysSntpClientUServerNumRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientUServerNumRequests.setStatus("current")
_EtsysSntpClientUServerNumFailedRequests_Type = Counter32
_EtsysSntpClientUServerNumFailedRequests_Object = MibTableColumn
etsysSntpClientUServerNumFailedRequests = _EtsysSntpClientUServerNumFailedRequests_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 6, 1, 8),
    _EtsysSntpClientUServerNumFailedRequests_Type()
)
etsysSntpClientUServerNumFailedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientUServerNumFailedRequests.setStatus("current")
_EtsysSntpClientUServerStatus_Type = RowStatus
_EtsysSntpClientUServerStatus_Object = MibTableColumn
etsysSntpClientUServerStatus = _EtsysSntpClientUServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 6, 1, 9),
    _EtsysSntpClientUServerStatus_Type()
)
etsysSntpClientUServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSntpClientUServerStatus.setStatus("current")


class _EtsysSntpClientUServerAuthKey_Type(Unsigned32):
    """Custom type etsysSntpClientUServerAuthKey based on Unsigned32"""
    defaultValue = 0


_EtsysSntpClientUServerAuthKey_Type.__name__ = "Unsigned32"
_EtsysSntpClientUServerAuthKey_Object = MibTableColumn
etsysSntpClientUServerAuthKey = _EtsysSntpClientUServerAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 6, 1, 10),
    _EtsysSntpClientUServerAuthKey_Type()
)
etsysSntpClientUServerAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSntpClientUServerAuthKey.setStatus("current")
_EtsysSntpClientUAuthKeyTable_Object = MibTable
etsysSntpClientUAuthKeyTable = _EtsysSntpClientUAuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 7)
)
if mibBuilder.loadTexts:
    etsysSntpClientUAuthKeyTable.setStatus("current")
_EtsysSntpClientUAuthKeyEntry_Object = MibTableRow
etsysSntpClientUAuthKeyEntry = _EtsysSntpClientUAuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 7, 1)
)
etsysSntpClientUAuthKeyEntry.setIndexNames(
    (0, "ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUAuthKey"),
)
if mibBuilder.loadTexts:
    etsysSntpClientUAuthKeyEntry.setStatus("current")
_EtsysSntpClientUAuthKey_Type = Unsigned32
_EtsysSntpClientUAuthKey_Object = MibTableColumn
etsysSntpClientUAuthKey = _EtsysSntpClientUAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 7, 1, 1),
    _EtsysSntpClientUAuthKey_Type()
)
etsysSntpClientUAuthKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysSntpClientUAuthKey.setStatus("current")


class _EtsysSntpClientUAuthType_Type(Integer32):
    """Custom type etsysSntpClientUAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha-1", 2))
    )


_EtsysSntpClientUAuthType_Type.__name__ = "Integer32"
_EtsysSntpClientUAuthType_Object = MibTableColumn
etsysSntpClientUAuthType = _EtsysSntpClientUAuthType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 7, 1, 2),
    _EtsysSntpClientUAuthType_Type()
)
etsysSntpClientUAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSntpClientUAuthType.setStatus("current")


class _EtsysSntpClientUAuthValue_Type(OctetString):
    """Custom type etsysSntpClientUAuthValue based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EtsysSntpClientUAuthValue_Type.__name__ = "OctetString"
_EtsysSntpClientUAuthValue_Object = MibTableColumn
etsysSntpClientUAuthValue = _EtsysSntpClientUAuthValue_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 7, 1, 3),
    _EtsysSntpClientUAuthValue_Type()
)
etsysSntpClientUAuthValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSntpClientUAuthValue.setStatus("current")


class _EtsysSntpClientUKeyTrusted_Type(TruthValue):
    """Custom type etsysSntpClientUKeyTrusted based on TruthValue"""
    defaultValue = 2


_EtsysSntpClientUKeyTrusted_Type.__name__ = "TruthValue"
_EtsysSntpClientUKeyTrusted_Object = MibTableColumn
etsysSntpClientUKeyTrusted = _EtsysSntpClientUKeyTrusted_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 7, 1, 4),
    _EtsysSntpClientUKeyTrusted_Type()
)
etsysSntpClientUKeyTrusted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSntpClientUKeyTrusted.setStatus("current")


class _EtsysSntpClientUAuthKeyStatus_Type(RowStatus):
    """Custom type etsysSntpClientUAuthKeyStatus based on RowStatus"""
    defaultValue = 4


_EtsysSntpClientUAuthKeyStatus_Type.__name__ = "RowStatus"
_EtsysSntpClientUAuthKeyStatus_Object = MibTableColumn
etsysSntpClientUAuthKeyStatus = _EtsysSntpClientUAuthKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 2, 7, 1, 5),
    _EtsysSntpClientUAuthKeyStatus_Type()
)
etsysSntpClientUAuthKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysSntpClientUAuthKeyStatus.setStatus("current")
_EtsysSntpClientMulticast_ObjectIdentity = ObjectIdentity
etsysSntpClientMulticast = _EtsysSntpClientMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 3)
)


class _EtsysSntpClientMulticastDelay_Type(Unsigned32):
    """Custom type etsysSntpClientMulticastDelay based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_EtsysSntpClientMulticastDelay_Type.__name__ = "Unsigned32"
_EtsysSntpClientMulticastDelay_Object = MibScalar
etsysSntpClientMulticastDelay = _EtsysSntpClientMulticastDelay_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 3, 1),
    _EtsysSntpClientMulticastDelay_Type()
)
etsysSntpClientMulticastDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSntpClientMulticastDelay.setStatus("current")
if mibBuilder.loadTexts:
    etsysSntpClientMulticastDelay.setUnits("microseconds")
_EtsysSntpClientMulticastCount_Type = Counter32
_EtsysSntpClientMulticastCount_Object = MibScalar
etsysSntpClientMulticastCount = _EtsysSntpClientMulticastCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 3, 2),
    _EtsysSntpClientMulticastCount_Type()
)
etsysSntpClientMulticastCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientMulticastCount.setStatus("current")
_EtsysSntpClientBroadcast_ObjectIdentity = ObjectIdentity
etsysSntpClientBroadcast = _EtsysSntpClientBroadcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 4)
)


class _EtsysSntpClientBroadcastDelay_Type(Unsigned32):
    """Custom type etsysSntpClientBroadcastDelay based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_EtsysSntpClientBroadcastDelay_Type.__name__ = "Unsigned32"
_EtsysSntpClientBroadcastDelay_Object = MibScalar
etsysSntpClientBroadcastDelay = _EtsysSntpClientBroadcastDelay_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 4, 1),
    _EtsysSntpClientBroadcastDelay_Type()
)
etsysSntpClientBroadcastDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSntpClientBroadcastDelay.setStatus("current")
if mibBuilder.loadTexts:
    etsysSntpClientBroadcastDelay.setUnits("microseconds")
_EtsysSntpClientBroadcastCount_Type = Counter32
_EtsysSntpClientBroadcastCount_Object = MibScalar
etsysSntpClientBroadcastCount = _EtsysSntpClientBroadcastCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 4, 2),
    _EtsysSntpClientBroadcastCount_Type()
)
etsysSntpClientBroadcastCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientBroadcastCount.setStatus("current")
_EtsysSntpClientAnycast_ObjectIdentity = ObjectIdentity
etsysSntpClientAnycast = _EtsysSntpClientAnycast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 5)
)


class _EtsysSntpClientAnycastBindRequestInterval_Type(Unsigned32):
    """Custom type etsysSntpClientAnycastBindRequestInterval based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16284),
    )


_EtsysSntpClientAnycastBindRequestInterval_Type.__name__ = "Unsigned32"
_EtsysSntpClientAnycastBindRequestInterval_Object = MibScalar
etsysSntpClientAnycastBindRequestInterval = _EtsysSntpClientAnycastBindRequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 5, 1),
    _EtsysSntpClientAnycastBindRequestInterval_Type()
)
etsysSntpClientAnycastBindRequestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSntpClientAnycastBindRequestInterval.setStatus("current")
if mibBuilder.loadTexts:
    etsysSntpClientAnycastBindRequestInterval.setUnits("seconds")


class _EtsysSntpClientAnycastPollInterval_Type(Unsigned32):
    """Custom type etsysSntpClientAnycastPollInterval based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16284),
    )


_EtsysSntpClientAnycastPollInterval_Type.__name__ = "Unsigned32"
_EtsysSntpClientAnycastPollInterval_Object = MibScalar
etsysSntpClientAnycastPollInterval = _EtsysSntpClientAnycastPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 5, 2),
    _EtsysSntpClientAnycastPollInterval_Type()
)
etsysSntpClientAnycastPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSntpClientAnycastPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    etsysSntpClientAnycastPollInterval.setUnits("seconds")


class _EtsysSntpClientAnycastPollTimeout_Type(Unsigned32):
    """Custom type etsysSntpClientAnycastPollTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_EtsysSntpClientAnycastPollTimeout_Type.__name__ = "Unsigned32"
_EtsysSntpClientAnycastPollTimeout_Object = MibScalar
etsysSntpClientAnycastPollTimeout = _EtsysSntpClientAnycastPollTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 5, 3),
    _EtsysSntpClientAnycastPollTimeout_Type()
)
etsysSntpClientAnycastPollTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSntpClientAnycastPollTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysSntpClientAnycastPollTimeout.setUnits("seconds")


class _EtsysSntpClientAnycastPollRetry_Type(Unsigned32):
    """Custom type etsysSntpClientAnycastPollRetry based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EtsysSntpClientAnycastPollRetry_Type.__name__ = "Unsigned32"
_EtsysSntpClientAnycastPollRetry_Object = MibScalar
etsysSntpClientAnycastPollRetry = _EtsysSntpClientAnycastPollRetry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 5, 4),
    _EtsysSntpClientAnycastPollRetry_Type()
)
etsysSntpClientAnycastPollRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysSntpClientAnycastPollRetry.setStatus("current")
_EtsysSntpClientAnycastServerAddrType_Type = InetAddressType
_EtsysSntpClientAnycastServerAddrType_Object = MibScalar
etsysSntpClientAnycastServerAddrType = _EtsysSntpClientAnycastServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 5, 5),
    _EtsysSntpClientAnycastServerAddrType_Type()
)
etsysSntpClientAnycastServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientAnycastServerAddrType.setStatus("current")


class _EtsysSntpClientAnycastServerAddr_Type(InetAddress):
    """Custom type etsysSntpClientAnycastServerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EtsysSntpClientAnycastServerAddr_Type.__name__ = "InetAddress"
_EtsysSntpClientAnycastServerAddr_Object = MibScalar
etsysSntpClientAnycastServerAddr = _EtsysSntpClientAnycastServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 5, 6),
    _EtsysSntpClientAnycastServerAddr_Type()
)
etsysSntpClientAnycastServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientAnycastServerAddr.setStatus("current")
_EtsysSntpClientAnycastNumRequests_Type = Counter32
_EtsysSntpClientAnycastNumRequests_Object = MibScalar
etsysSntpClientAnycastNumRequests = _EtsysSntpClientAnycastNumRequests_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 5, 7),
    _EtsysSntpClientAnycastNumRequests_Type()
)
etsysSntpClientAnycastNumRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientAnycastNumRequests.setStatus("current")
_EtsysSntpClientAnycastNumPollRequests_Type = Counter32
_EtsysSntpClientAnycastNumPollRequests_Object = MibScalar
etsysSntpClientAnycastNumPollRequests = _EtsysSntpClientAnycastNumPollRequests_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 1, 5, 8),
    _EtsysSntpClientAnycastNumPollRequests_Type()
)
etsysSntpClientAnycastNumPollRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysSntpClientAnycastNumPollRequests.setStatus("current")
_EtsysSntpClientConformance_ObjectIdentity = ObjectIdentity
etsysSntpClientConformance = _EtsysSntpClientConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 2)
)
_EtsysSntpClientGroups_ObjectIdentity = ObjectIdentity
etsysSntpClientGroups = _EtsysSntpClientGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 2, 1)
)
_EtsysSntpClientCompliances_ObjectIdentity = ObjectIdentity
etsysSntpClientCompliances = _EtsysSntpClientCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 2, 2)
)

# Managed Objects groups

etsysSntpClientDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 2, 1, 1)
)
etsysSntpClientDeviceGroup.setObjects(
      *(("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientVersion"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientSupportedMode"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientMode"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientLastUpdateTime"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientLastAttemptTime"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientLastAttemptStatus"))
)
if mibBuilder.loadTexts:
    etsysSntpClientDeviceGroup.setStatus("current")

etsysSntpClientUnicastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 2, 1, 2)
)
etsysSntpClientUnicastGroup.setObjects(
      *(("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUnicastPollInterval"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUnicastPollTimeout"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUnicastPollRetry"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUServerMaxEntries"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUServerCurrEntries"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUServerPrecedence"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUServerLastUpdateTime"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUServerLastAttemptTime"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUServerLastAttemptStatus"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUServerNumRequests"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUServerNumFailedRequests"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUServerStatus"))
)
if mibBuilder.loadTexts:
    etsysSntpClientUnicastGroup.setStatus("current")

etsysSntpClientMulticastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 2, 1, 3)
)
etsysSntpClientMulticastGroup.setObjects(
      *(("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientMulticastDelay"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientMulticastCount"))
)
if mibBuilder.loadTexts:
    etsysSntpClientMulticastGroup.setStatus("current")

etsysSntpClientBroadcastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 2, 1, 4)
)
etsysSntpClientBroadcastGroup.setObjects(
      *(("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientBroadcastDelay"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientBroadcastCount"))
)
if mibBuilder.loadTexts:
    etsysSntpClientBroadcastGroup.setStatus("current")

etsysSntpClientAnycastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 2, 1, 5)
)
etsysSntpClientAnycastGroup.setObjects(
      *(("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientAnycastBindRequestInterval"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientAnycastPollInterval"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientAnycastPollTimeout"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientAnycastPollRetry"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientAnycastServerAddrType"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientAnycastServerAddr"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientAnycastNumRequests"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientAnycastNumPollRequests"))
)
if mibBuilder.loadTexts:
    etsysSntpClientAnycastGroup.setStatus("current")

etsysSntpClientUnicastAuthenticationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 2, 1, 6)
)
etsysSntpClientUnicastAuthenticationGroup.setObjects(
      *(("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientAuthenticationEnable"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientMaxAuthenticationKeys"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUServerAuthKey"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUAuthKey"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUAuthType"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUAuthValue"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUKeyTrusted"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUAuthKeyStatus"))
)
if mibBuilder.loadTexts:
    etsysSntpClientUnicastAuthenticationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysSntpClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 38, 2, 2, 1)
)
etsysSntpClientCompliance.setObjects(
      *(("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientDeviceGroup"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUnicastGroup"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientMulticastGroup"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientBroadcastGroup"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientAnycastGroup"),
        ("ENTERASYS-SNTP-CLIENT-MIB", "etsysSntpClientUnicastAuthenticationGroup"))
)
if mibBuilder.loadTexts:
    etsysSntpClientCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-SNTP-CLIENT-MIB",
    **{"SntpClientOperModes": SntpClientOperModes,
       "SntpClientUpdateStatus": SntpClientUpdateStatus,
       "etsysSntpClientMIB": etsysSntpClientMIB,
       "etsysSntpClientObjects": etsysSntpClientObjects,
       "etsysSntpClientDevice": etsysSntpClientDevice,
       "etsysSntpClientVersion": etsysSntpClientVersion,
       "etsysSntpClientSupportedMode": etsysSntpClientSupportedMode,
       "etsysSntpClientMode": etsysSntpClientMode,
       "etsysSntpClientLastUpdateTime": etsysSntpClientLastUpdateTime,
       "etsysSntpClientLastAttemptTime": etsysSntpClientLastAttemptTime,
       "etsysSntpClientLastAttemptStatus": etsysSntpClientLastAttemptStatus,
       "etsysSntpClientAuthenticationEnable": etsysSntpClientAuthenticationEnable,
       "etsysSntpClientMaxAuthenticationKeys": etsysSntpClientMaxAuthenticationKeys,
       "etsysSntpClientUnicast": etsysSntpClientUnicast,
       "etsysSntpClientUnicastPollInterval": etsysSntpClientUnicastPollInterval,
       "etsysSntpClientUnicastPollTimeout": etsysSntpClientUnicastPollTimeout,
       "etsysSntpClientUnicastPollRetry": etsysSntpClientUnicastPollRetry,
       "etsysSntpClientUServerMaxEntries": etsysSntpClientUServerMaxEntries,
       "etsysSntpClientUServerCurrEntries": etsysSntpClientUServerCurrEntries,
       "etsysSntpClientUServerTable": etsysSntpClientUServerTable,
       "etsysSntpClientUServerEntry": etsysSntpClientUServerEntry,
       "etsysSntpClientUServerAddrType": etsysSntpClientUServerAddrType,
       "etsysSntpClientUServerAddr": etsysSntpClientUServerAddr,
       "etsysSntpClientUServerPrecedence": etsysSntpClientUServerPrecedence,
       "etsysSntpClientUServerLastUpdateTime": etsysSntpClientUServerLastUpdateTime,
       "etsysSntpClientUServerLastAttemptTime": etsysSntpClientUServerLastAttemptTime,
       "etsysSntpClientUServerLastAttemptStatus": etsysSntpClientUServerLastAttemptStatus,
       "etsysSntpClientUServerNumRequests": etsysSntpClientUServerNumRequests,
       "etsysSntpClientUServerNumFailedRequests": etsysSntpClientUServerNumFailedRequests,
       "etsysSntpClientUServerStatus": etsysSntpClientUServerStatus,
       "etsysSntpClientUServerAuthKey": etsysSntpClientUServerAuthKey,
       "etsysSntpClientUAuthKeyTable": etsysSntpClientUAuthKeyTable,
       "etsysSntpClientUAuthKeyEntry": etsysSntpClientUAuthKeyEntry,
       "etsysSntpClientUAuthKey": etsysSntpClientUAuthKey,
       "etsysSntpClientUAuthType": etsysSntpClientUAuthType,
       "etsysSntpClientUAuthValue": etsysSntpClientUAuthValue,
       "etsysSntpClientUKeyTrusted": etsysSntpClientUKeyTrusted,
       "etsysSntpClientUAuthKeyStatus": etsysSntpClientUAuthKeyStatus,
       "etsysSntpClientMulticast": etsysSntpClientMulticast,
       "etsysSntpClientMulticastDelay": etsysSntpClientMulticastDelay,
       "etsysSntpClientMulticastCount": etsysSntpClientMulticastCount,
       "etsysSntpClientBroadcast": etsysSntpClientBroadcast,
       "etsysSntpClientBroadcastDelay": etsysSntpClientBroadcastDelay,
       "etsysSntpClientBroadcastCount": etsysSntpClientBroadcastCount,
       "etsysSntpClientAnycast": etsysSntpClientAnycast,
       "etsysSntpClientAnycastBindRequestInterval": etsysSntpClientAnycastBindRequestInterval,
       "etsysSntpClientAnycastPollInterval": etsysSntpClientAnycastPollInterval,
       "etsysSntpClientAnycastPollTimeout": etsysSntpClientAnycastPollTimeout,
       "etsysSntpClientAnycastPollRetry": etsysSntpClientAnycastPollRetry,
       "etsysSntpClientAnycastServerAddrType": etsysSntpClientAnycastServerAddrType,
       "etsysSntpClientAnycastServerAddr": etsysSntpClientAnycastServerAddr,
       "etsysSntpClientAnycastNumRequests": etsysSntpClientAnycastNumRequests,
       "etsysSntpClientAnycastNumPollRequests": etsysSntpClientAnycastNumPollRequests,
       "etsysSntpClientConformance": etsysSntpClientConformance,
       "etsysSntpClientGroups": etsysSntpClientGroups,
       "etsysSntpClientDeviceGroup": etsysSntpClientDeviceGroup,
       "etsysSntpClientUnicastGroup": etsysSntpClientUnicastGroup,
       "etsysSntpClientMulticastGroup": etsysSntpClientMulticastGroup,
       "etsysSntpClientBroadcastGroup": etsysSntpClientBroadcastGroup,
       "etsysSntpClientAnycastGroup": etsysSntpClientAnycastGroup,
       "etsysSntpClientUnicastAuthenticationGroup": etsysSntpClientUnicastAuthenticationGroup,
       "etsysSntpClientCompliances": etsysSntpClientCompliances,
       "etsysSntpClientCompliance": etsysSntpClientCompliance}
)
