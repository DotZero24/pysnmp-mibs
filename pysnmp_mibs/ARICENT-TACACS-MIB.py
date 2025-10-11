# SNMP MIB module (ARICENT-TACACS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-TACACS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:52 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

futureTacacsClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 77)
)
if mibBuilder.loadTexts:
    futureTacacsClientMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FutureTacacsClientScalarGroup_ObjectIdentity = ObjectIdentity
futureTacacsClientScalarGroup = _FutureTacacsClientScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1)
)
_FsTacClntActiveServer_Type = IpAddress
_FsTacClntActiveServer_Object = MibScalar
fsTacClntActiveServer = _FsTacClntActiveServer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 1),
    _FsTacClntActiveServer_Type()
)
fsTacClntActiveServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTacClntActiveServer.setStatus("current")
_FsTacClntTraceLevel_Type = Unsigned32
_FsTacClntTraceLevel_Object = MibScalar
fsTacClntTraceLevel = _FsTacClntTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 2),
    _FsTacClntTraceLevel_Type()
)
fsTacClntTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTacClntTraceLevel.setStatus("current")


class _FsTacClntRetransmit_Type(Integer32):
    """Custom type fsTacClntRetransmit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsTacClntRetransmit_Type.__name__ = "Integer32"
_FsTacClntRetransmit_Object = MibScalar
fsTacClntRetransmit = _FsTacClntRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 3),
    _FsTacClntRetransmit_Type()
)
fsTacClntRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTacClntRetransmit.setStatus("current")
_FsTacClntStatisticsGroup_ObjectIdentity = ObjectIdentity
fsTacClntStatisticsGroup = _FsTacClntStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4)
)
_FsTacClntAuthenStartRequests_Type = Counter32
_FsTacClntAuthenStartRequests_Object = MibScalar
fsTacClntAuthenStartRequests = _FsTacClntAuthenStartRequests_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 1),
    _FsTacClntAuthenStartRequests_Type()
)
fsTacClntAuthenStartRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthenStartRequests.setStatus("current")
_FsTacClntAuthenContinueRequests_Type = Counter32
_FsTacClntAuthenContinueRequests_Object = MibScalar
fsTacClntAuthenContinueRequests = _FsTacClntAuthenContinueRequests_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 2),
    _FsTacClntAuthenContinueRequests_Type()
)
fsTacClntAuthenContinueRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthenContinueRequests.setStatus("current")
_FsTacClntAuthenEnableRequests_Type = Counter32
_FsTacClntAuthenEnableRequests_Object = MibScalar
fsTacClntAuthenEnableRequests = _FsTacClntAuthenEnableRequests_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 3),
    _FsTacClntAuthenEnableRequests_Type()
)
fsTacClntAuthenEnableRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthenEnableRequests.setStatus("current")
_FsTacClntAuthenAbortRequests_Type = Counter32
_FsTacClntAuthenAbortRequests_Object = MibScalar
fsTacClntAuthenAbortRequests = _FsTacClntAuthenAbortRequests_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 4),
    _FsTacClntAuthenAbortRequests_Type()
)
fsTacClntAuthenAbortRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthenAbortRequests.setStatus("current")
_FsTacClntAuthenPassReceived_Type = Counter32
_FsTacClntAuthenPassReceived_Object = MibScalar
fsTacClntAuthenPassReceived = _FsTacClntAuthenPassReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 5),
    _FsTacClntAuthenPassReceived_Type()
)
fsTacClntAuthenPassReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthenPassReceived.setStatus("current")
_FsTacClntAuthenFailReceived_Type = Counter32
_FsTacClntAuthenFailReceived_Object = MibScalar
fsTacClntAuthenFailReceived = _FsTacClntAuthenFailReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 6),
    _FsTacClntAuthenFailReceived_Type()
)
fsTacClntAuthenFailReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthenFailReceived.setStatus("current")
_FsTacClntAuthenGetUserReceived_Type = Counter32
_FsTacClntAuthenGetUserReceived_Object = MibScalar
fsTacClntAuthenGetUserReceived = _FsTacClntAuthenGetUserReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 7),
    _FsTacClntAuthenGetUserReceived_Type()
)
fsTacClntAuthenGetUserReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthenGetUserReceived.setStatus("current")
_FsTacClntAuthenGetPassReceived_Type = Counter32
_FsTacClntAuthenGetPassReceived_Object = MibScalar
fsTacClntAuthenGetPassReceived = _FsTacClntAuthenGetPassReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 8),
    _FsTacClntAuthenGetPassReceived_Type()
)
fsTacClntAuthenGetPassReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthenGetPassReceived.setStatus("current")
_FsTacClntAuthenGetDataReceived_Type = Counter32
_FsTacClntAuthenGetDataReceived_Object = MibScalar
fsTacClntAuthenGetDataReceived = _FsTacClntAuthenGetDataReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 9),
    _FsTacClntAuthenGetDataReceived_Type()
)
fsTacClntAuthenGetDataReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthenGetDataReceived.setStatus("current")
_FsTacClntAuthenErrorReceived_Type = Counter32
_FsTacClntAuthenErrorReceived_Object = MibScalar
fsTacClntAuthenErrorReceived = _FsTacClntAuthenErrorReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 10),
    _FsTacClntAuthenErrorReceived_Type()
)
fsTacClntAuthenErrorReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthenErrorReceived.setStatus("current")
_FsTacClntAuthenFollowReceived_Type = Counter32
_FsTacClntAuthenFollowReceived_Object = MibScalar
fsTacClntAuthenFollowReceived = _FsTacClntAuthenFollowReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 11),
    _FsTacClntAuthenFollowReceived_Type()
)
fsTacClntAuthenFollowReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthenFollowReceived.setStatus("current")
_FsTacClntAuthenRestartReceived_Type = Counter32
_FsTacClntAuthenRestartReceived_Object = MibScalar
fsTacClntAuthenRestartReceived = _FsTacClntAuthenRestartReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 12),
    _FsTacClntAuthenRestartReceived_Type()
)
fsTacClntAuthenRestartReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthenRestartReceived.setStatus("current")
_FsTacClntAuthenSessionTimouts_Type = Counter32
_FsTacClntAuthenSessionTimouts_Object = MibScalar
fsTacClntAuthenSessionTimouts = _FsTacClntAuthenSessionTimouts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 13),
    _FsTacClntAuthenSessionTimouts_Type()
)
fsTacClntAuthenSessionTimouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthenSessionTimouts.setStatus("current")
_FsTacClntAuthorRequests_Type = Counter32
_FsTacClntAuthorRequests_Object = MibScalar
fsTacClntAuthorRequests = _FsTacClntAuthorRequests_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 14),
    _FsTacClntAuthorRequests_Type()
)
fsTacClntAuthorRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthorRequests.setStatus("current")
_FsTacClntAuthorPassAddReceived_Type = Counter32
_FsTacClntAuthorPassAddReceived_Object = MibScalar
fsTacClntAuthorPassAddReceived = _FsTacClntAuthorPassAddReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 15),
    _FsTacClntAuthorPassAddReceived_Type()
)
fsTacClntAuthorPassAddReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthorPassAddReceived.setStatus("current")
_FsTacClntAuthorPassReplReceived_Type = Counter32
_FsTacClntAuthorPassReplReceived_Object = MibScalar
fsTacClntAuthorPassReplReceived = _FsTacClntAuthorPassReplReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 16),
    _FsTacClntAuthorPassReplReceived_Type()
)
fsTacClntAuthorPassReplReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthorPassReplReceived.setStatus("current")
_FsTacClntAuthorFailReceived_Type = Counter32
_FsTacClntAuthorFailReceived_Object = MibScalar
fsTacClntAuthorFailReceived = _FsTacClntAuthorFailReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 17),
    _FsTacClntAuthorFailReceived_Type()
)
fsTacClntAuthorFailReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthorFailReceived.setStatus("current")
_FsTacClntAuthorErrorReceived_Type = Counter32
_FsTacClntAuthorErrorReceived_Object = MibScalar
fsTacClntAuthorErrorReceived = _FsTacClntAuthorErrorReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 18),
    _FsTacClntAuthorErrorReceived_Type()
)
fsTacClntAuthorErrorReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthorErrorReceived.setStatus("current")
_FsTacClntAuthorFollowReceived_Type = Counter32
_FsTacClntAuthorFollowReceived_Object = MibScalar
fsTacClntAuthorFollowReceived = _FsTacClntAuthorFollowReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 19),
    _FsTacClntAuthorFollowReceived_Type()
)
fsTacClntAuthorFollowReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthorFollowReceived.setStatus("current")
_FsTacClntAuthorSessionTimeouts_Type = Counter32
_FsTacClntAuthorSessionTimeouts_Object = MibScalar
fsTacClntAuthorSessionTimeouts = _FsTacClntAuthorSessionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 20),
    _FsTacClntAuthorSessionTimeouts_Type()
)
fsTacClntAuthorSessionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAuthorSessionTimeouts.setStatus("current")
_FsTacClntAcctStartRequests_Type = Counter32
_FsTacClntAcctStartRequests_Object = MibScalar
fsTacClntAcctStartRequests = _FsTacClntAcctStartRequests_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 21),
    _FsTacClntAcctStartRequests_Type()
)
fsTacClntAcctStartRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAcctStartRequests.setStatus("current")
_FsTacClntAcctWdRequests_Type = Counter32
_FsTacClntAcctWdRequests_Object = MibScalar
fsTacClntAcctWdRequests = _FsTacClntAcctWdRequests_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 22),
    _FsTacClntAcctWdRequests_Type()
)
fsTacClntAcctWdRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAcctWdRequests.setStatus("current")
_FsTacClntAcctStopRequests_Type = Counter32
_FsTacClntAcctStopRequests_Object = MibScalar
fsTacClntAcctStopRequests = _FsTacClntAcctStopRequests_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 23),
    _FsTacClntAcctStopRequests_Type()
)
fsTacClntAcctStopRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAcctStopRequests.setStatus("current")
_FsTacClntAcctSuccessReceived_Type = Counter32
_FsTacClntAcctSuccessReceived_Object = MibScalar
fsTacClntAcctSuccessReceived = _FsTacClntAcctSuccessReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 24),
    _FsTacClntAcctSuccessReceived_Type()
)
fsTacClntAcctSuccessReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAcctSuccessReceived.setStatus("current")
_FsTacClntAcctErrorReceived_Type = Counter32
_FsTacClntAcctErrorReceived_Object = MibScalar
fsTacClntAcctErrorReceived = _FsTacClntAcctErrorReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 25),
    _FsTacClntAcctErrorReceived_Type()
)
fsTacClntAcctErrorReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAcctErrorReceived.setStatus("current")
_FsTacClntAcctFollowReceived_Type = Counter32
_FsTacClntAcctFollowReceived_Object = MibScalar
fsTacClntAcctFollowReceived = _FsTacClntAcctFollowReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 26),
    _FsTacClntAcctFollowReceived_Type()
)
fsTacClntAcctFollowReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAcctFollowReceived.setStatus("current")
_FsTacClntAcctSessionTimeouts_Type = Counter32
_FsTacClntAcctSessionTimeouts_Object = MibScalar
fsTacClntAcctSessionTimeouts = _FsTacClntAcctSessionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 27),
    _FsTacClntAcctSessionTimeouts_Type()
)
fsTacClntAcctSessionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntAcctSessionTimeouts.setStatus("current")
_FsTacClntMalformedPktsReceived_Type = Counter32
_FsTacClntMalformedPktsReceived_Object = MibScalar
fsTacClntMalformedPktsReceived = _FsTacClntMalformedPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 28),
    _FsTacClntMalformedPktsReceived_Type()
)
fsTacClntMalformedPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntMalformedPktsReceived.setStatus("current")
_FsTacClntSocketFailures_Type = Counter32
_FsTacClntSocketFailures_Object = MibScalar
fsTacClntSocketFailures = _FsTacClntSocketFailures_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 29),
    _FsTacClntSocketFailures_Type()
)
fsTacClntSocketFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntSocketFailures.setStatus("current")
_FsTacClntConnectionFailures_Type = Counter32
_FsTacClntConnectionFailures_Object = MibScalar
fsTacClntConnectionFailures = _FsTacClntConnectionFailures_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 1, 4, 30),
    _FsTacClntConnectionFailures_Type()
)
fsTacClntConnectionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntConnectionFailures.setStatus("current")
_FutureTacacsClientTableGroup_ObjectIdentity = ObjectIdentity
futureTacacsClientTableGroup = _FutureTacacsClientTableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 77, 2)
)
_FsTacClntServerTable_Object = MibTable
fsTacClntServerTable = _FsTacClntServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 2, 1)
)
if mibBuilder.loadTexts:
    fsTacClntServerTable.setStatus("current")
_FsTacClntServerEntry_Object = MibTableRow
fsTacClntServerEntry = _FsTacClntServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 2, 1, 1)
)
fsTacClntServerEntry.setIndexNames(
    (0, "ARICENT-TACACS-MIB", "fsTacClntServerAddress"),
)
if mibBuilder.loadTexts:
    fsTacClntServerEntry.setStatus("current")
_FsTacClntServerAddress_Type = IpAddress
_FsTacClntServerAddress_Object = MibTableColumn
fsTacClntServerAddress = _FsTacClntServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 2, 1, 1, 1),
    _FsTacClntServerAddress_Type()
)
fsTacClntServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTacClntServerAddress.setStatus("current")
_FsTacClntServerStatus_Type = RowStatus
_FsTacClntServerStatus_Object = MibTableColumn
fsTacClntServerStatus = _FsTacClntServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 2, 1, 1, 2),
    _FsTacClntServerStatus_Type()
)
fsTacClntServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTacClntServerStatus.setStatus("current")


class _FsTacClntServerSingleConnect_Type(Integer32):
    """Custom type fsTacClntServerSingleConnect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_FsTacClntServerSingleConnect_Type.__name__ = "Integer32"
_FsTacClntServerSingleConnect_Object = MibTableColumn
fsTacClntServerSingleConnect = _FsTacClntServerSingleConnect_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 2, 1, 1, 3),
    _FsTacClntServerSingleConnect_Type()
)
fsTacClntServerSingleConnect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTacClntServerSingleConnect.setStatus("current")


class _FsTacClntServerPort_Type(Integer32):
    """Custom type fsTacClntServerPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsTacClntServerPort_Type.__name__ = "Integer32"
_FsTacClntServerPort_Object = MibTableColumn
fsTacClntServerPort = _FsTacClntServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 2, 1, 1, 4),
    _FsTacClntServerPort_Type()
)
fsTacClntServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTacClntServerPort.setStatus("current")


class _FsTacClntServerTimeout_Type(Integer32):
    """Custom type fsTacClntServerTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsTacClntServerTimeout_Type.__name__ = "Integer32"
_FsTacClntServerTimeout_Object = MibTableColumn
fsTacClntServerTimeout = _FsTacClntServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 2, 1, 1, 5),
    _FsTacClntServerTimeout_Type()
)
fsTacClntServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTacClntServerTimeout.setStatus("current")
_FsTacClntServerKey_Type = DisplayString
_FsTacClntServerKey_Object = MibTableColumn
fsTacClntServerKey = _FsTacClntServerKey_Object(
    (1, 3, 6, 1, 4, 1, 2076, 77, 2, 1, 1, 6),
    _FsTacClntServerKey_Type()
)
fsTacClntServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTacClntServerKey.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-TACACS-MIB",
    **{"futureTacacsClientMIB": futureTacacsClientMIB,
       "futureTacacsClientScalarGroup": futureTacacsClientScalarGroup,
       "fsTacClntActiveServer": fsTacClntActiveServer,
       "fsTacClntTraceLevel": fsTacClntTraceLevel,
       "fsTacClntRetransmit": fsTacClntRetransmit,
       "fsTacClntStatisticsGroup": fsTacClntStatisticsGroup,
       "fsTacClntAuthenStartRequests": fsTacClntAuthenStartRequests,
       "fsTacClntAuthenContinueRequests": fsTacClntAuthenContinueRequests,
       "fsTacClntAuthenEnableRequests": fsTacClntAuthenEnableRequests,
       "fsTacClntAuthenAbortRequests": fsTacClntAuthenAbortRequests,
       "fsTacClntAuthenPassReceived": fsTacClntAuthenPassReceived,
       "fsTacClntAuthenFailReceived": fsTacClntAuthenFailReceived,
       "fsTacClntAuthenGetUserReceived": fsTacClntAuthenGetUserReceived,
       "fsTacClntAuthenGetPassReceived": fsTacClntAuthenGetPassReceived,
       "fsTacClntAuthenGetDataReceived": fsTacClntAuthenGetDataReceived,
       "fsTacClntAuthenErrorReceived": fsTacClntAuthenErrorReceived,
       "fsTacClntAuthenFollowReceived": fsTacClntAuthenFollowReceived,
       "fsTacClntAuthenRestartReceived": fsTacClntAuthenRestartReceived,
       "fsTacClntAuthenSessionTimouts": fsTacClntAuthenSessionTimouts,
       "fsTacClntAuthorRequests": fsTacClntAuthorRequests,
       "fsTacClntAuthorPassAddReceived": fsTacClntAuthorPassAddReceived,
       "fsTacClntAuthorPassReplReceived": fsTacClntAuthorPassReplReceived,
       "fsTacClntAuthorFailReceived": fsTacClntAuthorFailReceived,
       "fsTacClntAuthorErrorReceived": fsTacClntAuthorErrorReceived,
       "fsTacClntAuthorFollowReceived": fsTacClntAuthorFollowReceived,
       "fsTacClntAuthorSessionTimeouts": fsTacClntAuthorSessionTimeouts,
       "fsTacClntAcctStartRequests": fsTacClntAcctStartRequests,
       "fsTacClntAcctWdRequests": fsTacClntAcctWdRequests,
       "fsTacClntAcctStopRequests": fsTacClntAcctStopRequests,
       "fsTacClntAcctSuccessReceived": fsTacClntAcctSuccessReceived,
       "fsTacClntAcctErrorReceived": fsTacClntAcctErrorReceived,
       "fsTacClntAcctFollowReceived": fsTacClntAcctFollowReceived,
       "fsTacClntAcctSessionTimeouts": fsTacClntAcctSessionTimeouts,
       "fsTacClntMalformedPktsReceived": fsTacClntMalformedPktsReceived,
       "fsTacClntSocketFailures": fsTacClntSocketFailures,
       "fsTacClntConnectionFailures": fsTacClntConnectionFailures,
       "futureTacacsClientTableGroup": futureTacacsClientTableGroup,
       "fsTacClntServerTable": fsTacClntServerTable,
       "fsTacClntServerEntry": fsTacClntServerEntry,
       "fsTacClntServerAddress": fsTacClntServerAddress,
       "fsTacClntServerStatus": fsTacClntServerStatus,
       "fsTacClntServerSingleConnect": fsTacClntServerSingleConnect,
       "fsTacClntServerPort": fsTacClntServerPort,
       "fsTacClntServerTimeout": fsTacClntServerTimeout,
       "fsTacClntServerKey": fsTacClntServerKey}
)
