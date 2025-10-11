# SNMP MIB module (ARICENT-TACACS-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-TACACS-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:48 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

futureTacacsClientExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29)
)
if mibBuilder.loadTexts:
    futureTacacsClientExtMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FutureTacacsClientExtScalarGroup_ObjectIdentity = ObjectIdentity
futureTacacsClientExtScalarGroup = _FutureTacacsClientExtScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1)
)
_FsTacClntExtActiveServerAddressType_Type = InetAddressType
_FsTacClntExtActiveServerAddressType_Object = MibScalar
fsTacClntExtActiveServerAddressType = _FsTacClntExtActiveServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 1),
    _FsTacClntExtActiveServerAddressType_Type()
)
fsTacClntExtActiveServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTacClntExtActiveServerAddressType.setStatus("current")
_FsTacClntExtActiveServer_Type = InetAddress
_FsTacClntExtActiveServer_Object = MibScalar
fsTacClntExtActiveServer = _FsTacClntExtActiveServer_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 2),
    _FsTacClntExtActiveServer_Type()
)
fsTacClntExtActiveServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTacClntExtActiveServer.setStatus("current")
_FsTacClntExtTraceLevel_Type = Unsigned32
_FsTacClntExtTraceLevel_Object = MibScalar
fsTacClntExtTraceLevel = _FsTacClntExtTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 3),
    _FsTacClntExtTraceLevel_Type()
)
fsTacClntExtTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTacClntExtTraceLevel.setStatus("current")


class _FsTacClntExtRetransmit_Type(Integer32):
    """Custom type fsTacClntExtRetransmit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsTacClntExtRetransmit_Type.__name__ = "Integer32"
_FsTacClntExtRetransmit_Object = MibScalar
fsTacClntExtRetransmit = _FsTacClntExtRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 4),
    _FsTacClntExtRetransmit_Type()
)
fsTacClntExtRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTacClntExtRetransmit.setStatus("current")
_FsTacClntExtStatisticsGroup_ObjectIdentity = ObjectIdentity
fsTacClntExtStatisticsGroup = _FsTacClntExtStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5)
)
_FsTacClntExtAuthenStartRequests_Type = Counter32
_FsTacClntExtAuthenStartRequests_Object = MibScalar
fsTacClntExtAuthenStartRequests = _FsTacClntExtAuthenStartRequests_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 1),
    _FsTacClntExtAuthenStartRequests_Type()
)
fsTacClntExtAuthenStartRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthenStartRequests.setStatus("current")
_FsTacClntExtAuthenContinueRequests_Type = Counter32
_FsTacClntExtAuthenContinueRequests_Object = MibScalar
fsTacClntExtAuthenContinueRequests = _FsTacClntExtAuthenContinueRequests_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 2),
    _FsTacClntExtAuthenContinueRequests_Type()
)
fsTacClntExtAuthenContinueRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthenContinueRequests.setStatus("current")
_FsTacClntExtAuthenEnableRequests_Type = Counter32
_FsTacClntExtAuthenEnableRequests_Object = MibScalar
fsTacClntExtAuthenEnableRequests = _FsTacClntExtAuthenEnableRequests_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 3),
    _FsTacClntExtAuthenEnableRequests_Type()
)
fsTacClntExtAuthenEnableRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthenEnableRequests.setStatus("current")
_FsTacClntExtAuthenAbortRequests_Type = Counter32
_FsTacClntExtAuthenAbortRequests_Object = MibScalar
fsTacClntExtAuthenAbortRequests = _FsTacClntExtAuthenAbortRequests_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 4),
    _FsTacClntExtAuthenAbortRequests_Type()
)
fsTacClntExtAuthenAbortRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthenAbortRequests.setStatus("current")
_FsTacClntExtAuthenPassReceived_Type = Counter32
_FsTacClntExtAuthenPassReceived_Object = MibScalar
fsTacClntExtAuthenPassReceived = _FsTacClntExtAuthenPassReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 5),
    _FsTacClntExtAuthenPassReceived_Type()
)
fsTacClntExtAuthenPassReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthenPassReceived.setStatus("current")
_FsTacClntExtAuthenFailReceived_Type = Counter32
_FsTacClntExtAuthenFailReceived_Object = MibScalar
fsTacClntExtAuthenFailReceived = _FsTacClntExtAuthenFailReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 6),
    _FsTacClntExtAuthenFailReceived_Type()
)
fsTacClntExtAuthenFailReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthenFailReceived.setStatus("current")
_FsTacClntExtAuthenGetUserReceived_Type = Counter32
_FsTacClntExtAuthenGetUserReceived_Object = MibScalar
fsTacClntExtAuthenGetUserReceived = _FsTacClntExtAuthenGetUserReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 7),
    _FsTacClntExtAuthenGetUserReceived_Type()
)
fsTacClntExtAuthenGetUserReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthenGetUserReceived.setStatus("current")
_FsTacClntExtAuthenGetPassReceived_Type = Counter32
_FsTacClntExtAuthenGetPassReceived_Object = MibScalar
fsTacClntExtAuthenGetPassReceived = _FsTacClntExtAuthenGetPassReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 8),
    _FsTacClntExtAuthenGetPassReceived_Type()
)
fsTacClntExtAuthenGetPassReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthenGetPassReceived.setStatus("current")
_FsTacClntExtAuthenGetDataReceived_Type = Counter32
_FsTacClntExtAuthenGetDataReceived_Object = MibScalar
fsTacClntExtAuthenGetDataReceived = _FsTacClntExtAuthenGetDataReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 9),
    _FsTacClntExtAuthenGetDataReceived_Type()
)
fsTacClntExtAuthenGetDataReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthenGetDataReceived.setStatus("current")
_FsTacClntExtAuthenErrorReceived_Type = Counter32
_FsTacClntExtAuthenErrorReceived_Object = MibScalar
fsTacClntExtAuthenErrorReceived = _FsTacClntExtAuthenErrorReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 10),
    _FsTacClntExtAuthenErrorReceived_Type()
)
fsTacClntExtAuthenErrorReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthenErrorReceived.setStatus("current")
_FsTacClntExtAuthenFollowReceived_Type = Counter32
_FsTacClntExtAuthenFollowReceived_Object = MibScalar
fsTacClntExtAuthenFollowReceived = _FsTacClntExtAuthenFollowReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 11),
    _FsTacClntExtAuthenFollowReceived_Type()
)
fsTacClntExtAuthenFollowReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthenFollowReceived.setStatus("current")
_FsTacClntExtAuthenRestartReceived_Type = Counter32
_FsTacClntExtAuthenRestartReceived_Object = MibScalar
fsTacClntExtAuthenRestartReceived = _FsTacClntExtAuthenRestartReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 12),
    _FsTacClntExtAuthenRestartReceived_Type()
)
fsTacClntExtAuthenRestartReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthenRestartReceived.setStatus("current")
_FsTacClntExtAuthenSessionTimouts_Type = Counter32
_FsTacClntExtAuthenSessionTimouts_Object = MibScalar
fsTacClntExtAuthenSessionTimouts = _FsTacClntExtAuthenSessionTimouts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 13),
    _FsTacClntExtAuthenSessionTimouts_Type()
)
fsTacClntExtAuthenSessionTimouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthenSessionTimouts.setStatus("current")
_FsTacClntExtAuthorRequests_Type = Counter32
_FsTacClntExtAuthorRequests_Object = MibScalar
fsTacClntExtAuthorRequests = _FsTacClntExtAuthorRequests_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 14),
    _FsTacClntExtAuthorRequests_Type()
)
fsTacClntExtAuthorRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthorRequests.setStatus("current")
_FsTacClntExtAuthorPassAddReceived_Type = Counter32
_FsTacClntExtAuthorPassAddReceived_Object = MibScalar
fsTacClntExtAuthorPassAddReceived = _FsTacClntExtAuthorPassAddReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 15),
    _FsTacClntExtAuthorPassAddReceived_Type()
)
fsTacClntExtAuthorPassAddReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthorPassAddReceived.setStatus("current")
_FsTacClntExtAuthorPassReplReceived_Type = Counter32
_FsTacClntExtAuthorPassReplReceived_Object = MibScalar
fsTacClntExtAuthorPassReplReceived = _FsTacClntExtAuthorPassReplReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 16),
    _FsTacClntExtAuthorPassReplReceived_Type()
)
fsTacClntExtAuthorPassReplReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthorPassReplReceived.setStatus("current")
_FsTacClntExtAuthorFailReceived_Type = Counter32
_FsTacClntExtAuthorFailReceived_Object = MibScalar
fsTacClntExtAuthorFailReceived = _FsTacClntExtAuthorFailReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 17),
    _FsTacClntExtAuthorFailReceived_Type()
)
fsTacClntExtAuthorFailReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthorFailReceived.setStatus("current")
_FsTacClntExtAuthorErrorReceived_Type = Counter32
_FsTacClntExtAuthorErrorReceived_Object = MibScalar
fsTacClntExtAuthorErrorReceived = _FsTacClntExtAuthorErrorReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 18),
    _FsTacClntExtAuthorErrorReceived_Type()
)
fsTacClntExtAuthorErrorReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthorErrorReceived.setStatus("current")
_FsTacClntExtAuthorFollowReceived_Type = Counter32
_FsTacClntExtAuthorFollowReceived_Object = MibScalar
fsTacClntExtAuthorFollowReceived = _FsTacClntExtAuthorFollowReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 19),
    _FsTacClntExtAuthorFollowReceived_Type()
)
fsTacClntExtAuthorFollowReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthorFollowReceived.setStatus("current")
_FsTacClntExtAuthorSessionTimeouts_Type = Counter32
_FsTacClntExtAuthorSessionTimeouts_Object = MibScalar
fsTacClntExtAuthorSessionTimeouts = _FsTacClntExtAuthorSessionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 20),
    _FsTacClntExtAuthorSessionTimeouts_Type()
)
fsTacClntExtAuthorSessionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAuthorSessionTimeouts.setStatus("current")
_FsTacClntExtAcctStartRequests_Type = Counter32
_FsTacClntExtAcctStartRequests_Object = MibScalar
fsTacClntExtAcctStartRequests = _FsTacClntExtAcctStartRequests_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 21),
    _FsTacClntExtAcctStartRequests_Type()
)
fsTacClntExtAcctStartRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAcctStartRequests.setStatus("current")
_FsTacClntExtAcctWdRequests_Type = Counter32
_FsTacClntExtAcctWdRequests_Object = MibScalar
fsTacClntExtAcctWdRequests = _FsTacClntExtAcctWdRequests_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 22),
    _FsTacClntExtAcctWdRequests_Type()
)
fsTacClntExtAcctWdRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAcctWdRequests.setStatus("current")
_FsTacClntExtAcctStopRequests_Type = Counter32
_FsTacClntExtAcctStopRequests_Object = MibScalar
fsTacClntExtAcctStopRequests = _FsTacClntExtAcctStopRequests_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 23),
    _FsTacClntExtAcctStopRequests_Type()
)
fsTacClntExtAcctStopRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAcctStopRequests.setStatus("current")
_FsTacClntExtAcctSuccessReceived_Type = Counter32
_FsTacClntExtAcctSuccessReceived_Object = MibScalar
fsTacClntExtAcctSuccessReceived = _FsTacClntExtAcctSuccessReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 24),
    _FsTacClntExtAcctSuccessReceived_Type()
)
fsTacClntExtAcctSuccessReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAcctSuccessReceived.setStatus("current")
_FsTacClntExtAcctErrorReceived_Type = Counter32
_FsTacClntExtAcctErrorReceived_Object = MibScalar
fsTacClntExtAcctErrorReceived = _FsTacClntExtAcctErrorReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 25),
    _FsTacClntExtAcctErrorReceived_Type()
)
fsTacClntExtAcctErrorReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAcctErrorReceived.setStatus("current")
_FsTacClntExtAcctFollowReceived_Type = Counter32
_FsTacClntExtAcctFollowReceived_Object = MibScalar
fsTacClntExtAcctFollowReceived = _FsTacClntExtAcctFollowReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 26),
    _FsTacClntExtAcctFollowReceived_Type()
)
fsTacClntExtAcctFollowReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAcctFollowReceived.setStatus("current")
_FsTacClntExtAcctSessionTimeouts_Type = Counter32
_FsTacClntExtAcctSessionTimeouts_Object = MibScalar
fsTacClntExtAcctSessionTimeouts = _FsTacClntExtAcctSessionTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 27),
    _FsTacClntExtAcctSessionTimeouts_Type()
)
fsTacClntExtAcctSessionTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtAcctSessionTimeouts.setStatus("current")
_FsTacClntExtMalformedPktsReceived_Type = Counter32
_FsTacClntExtMalformedPktsReceived_Object = MibScalar
fsTacClntExtMalformedPktsReceived = _FsTacClntExtMalformedPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 28),
    _FsTacClntExtMalformedPktsReceived_Type()
)
fsTacClntExtMalformedPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtMalformedPktsReceived.setStatus("current")
_FsTacClntExtSocketFailures_Type = Counter32
_FsTacClntExtSocketFailures_Object = MibScalar
fsTacClntExtSocketFailures = _FsTacClntExtSocketFailures_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 29),
    _FsTacClntExtSocketFailures_Type()
)
fsTacClntExtSocketFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtSocketFailures.setStatus("current")
_FsTacClntExtConnectionFailures_Type = Counter32
_FsTacClntExtConnectionFailures_Object = MibScalar
fsTacClntExtConnectionFailures = _FsTacClntExtConnectionFailures_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 1, 5, 30),
    _FsTacClntExtConnectionFailures_Type()
)
fsTacClntExtConnectionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacClntExtConnectionFailures.setStatus("current")
_FutureTacacsClientExtTableGroup_ObjectIdentity = ObjectIdentity
futureTacacsClientExtTableGroup = _FutureTacacsClientExtTableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 2)
)
_FsTacClntExtServerTable_Object = MibTable
fsTacClntExtServerTable = _FsTacClntExtServerTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 2, 1)
)
if mibBuilder.loadTexts:
    fsTacClntExtServerTable.setStatus("current")
_FsTacClntExtServerEntry_Object = MibTableRow
fsTacClntExtServerEntry = _FsTacClntExtServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 2, 1, 1)
)
fsTacClntExtServerEntry.setIndexNames(
    (0, "ARICENT-TACACS-EXT-MIB", "fsTacClntExtServerAddressType"),
    (0, "ARICENT-TACACS-EXT-MIB", "fsTacClntExtServerAddress"),
)
if mibBuilder.loadTexts:
    fsTacClntExtServerEntry.setStatus("current")
_FsTacClntExtServerAddressType_Type = InetAddressType
_FsTacClntExtServerAddressType_Object = MibTableColumn
fsTacClntExtServerAddressType = _FsTacClntExtServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 2, 1, 1, 1),
    _FsTacClntExtServerAddressType_Type()
)
fsTacClntExtServerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTacClntExtServerAddressType.setStatus("current")
_FsTacClntExtServerAddress_Type = InetAddress
_FsTacClntExtServerAddress_Object = MibTableColumn
fsTacClntExtServerAddress = _FsTacClntExtServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 2, 1, 1, 2),
    _FsTacClntExtServerAddress_Type()
)
fsTacClntExtServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTacClntExtServerAddress.setStatus("current")
_FsTacClntExtServerStatus_Type = RowStatus
_FsTacClntExtServerStatus_Object = MibTableColumn
fsTacClntExtServerStatus = _FsTacClntExtServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 2, 1, 1, 3),
    _FsTacClntExtServerStatus_Type()
)
fsTacClntExtServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTacClntExtServerStatus.setStatus("current")


class _FsTacClntExtServerSingleConnect_Type(Integer32):
    """Custom type fsTacClntExtServerSingleConnect based on Integer32"""
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


_FsTacClntExtServerSingleConnect_Type.__name__ = "Integer32"
_FsTacClntExtServerSingleConnect_Object = MibTableColumn
fsTacClntExtServerSingleConnect = _FsTacClntExtServerSingleConnect_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 2, 1, 1, 4),
    _FsTacClntExtServerSingleConnect_Type()
)
fsTacClntExtServerSingleConnect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTacClntExtServerSingleConnect.setStatus("current")


class _FsTacClntExtServerPort_Type(Integer32):
    """Custom type fsTacClntExtServerPort based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsTacClntExtServerPort_Type.__name__ = "Integer32"
_FsTacClntExtServerPort_Object = MibTableColumn
fsTacClntExtServerPort = _FsTacClntExtServerPort_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 2, 1, 1, 5),
    _FsTacClntExtServerPort_Type()
)
fsTacClntExtServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTacClntExtServerPort.setStatus("current")


class _FsTacClntExtServerTimeout_Type(Integer32):
    """Custom type fsTacClntExtServerTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsTacClntExtServerTimeout_Type.__name__ = "Integer32"
_FsTacClntExtServerTimeout_Object = MibTableColumn
fsTacClntExtServerTimeout = _FsTacClntExtServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 2, 1, 1, 6),
    _FsTacClntExtServerTimeout_Type()
)
fsTacClntExtServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTacClntExtServerTimeout.setStatus("current")
_FsTacClntExtServerKey_Type = DisplayString
_FsTacClntExtServerKey_Object = MibTableColumn
fsTacClntExtServerKey = _FsTacClntExtServerKey_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 29, 2, 1, 1, 7),
    _FsTacClntExtServerKey_Type()
)
fsTacClntExtServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTacClntExtServerKey.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-TACACS-EXT-MIB",
    **{"futureTacacsClientExtMIB": futureTacacsClientExtMIB,
       "futureTacacsClientExtScalarGroup": futureTacacsClientExtScalarGroup,
       "fsTacClntExtActiveServerAddressType": fsTacClntExtActiveServerAddressType,
       "fsTacClntExtActiveServer": fsTacClntExtActiveServer,
       "fsTacClntExtTraceLevel": fsTacClntExtTraceLevel,
       "fsTacClntExtRetransmit": fsTacClntExtRetransmit,
       "fsTacClntExtStatisticsGroup": fsTacClntExtStatisticsGroup,
       "fsTacClntExtAuthenStartRequests": fsTacClntExtAuthenStartRequests,
       "fsTacClntExtAuthenContinueRequests": fsTacClntExtAuthenContinueRequests,
       "fsTacClntExtAuthenEnableRequests": fsTacClntExtAuthenEnableRequests,
       "fsTacClntExtAuthenAbortRequests": fsTacClntExtAuthenAbortRequests,
       "fsTacClntExtAuthenPassReceived": fsTacClntExtAuthenPassReceived,
       "fsTacClntExtAuthenFailReceived": fsTacClntExtAuthenFailReceived,
       "fsTacClntExtAuthenGetUserReceived": fsTacClntExtAuthenGetUserReceived,
       "fsTacClntExtAuthenGetPassReceived": fsTacClntExtAuthenGetPassReceived,
       "fsTacClntExtAuthenGetDataReceived": fsTacClntExtAuthenGetDataReceived,
       "fsTacClntExtAuthenErrorReceived": fsTacClntExtAuthenErrorReceived,
       "fsTacClntExtAuthenFollowReceived": fsTacClntExtAuthenFollowReceived,
       "fsTacClntExtAuthenRestartReceived": fsTacClntExtAuthenRestartReceived,
       "fsTacClntExtAuthenSessionTimouts": fsTacClntExtAuthenSessionTimouts,
       "fsTacClntExtAuthorRequests": fsTacClntExtAuthorRequests,
       "fsTacClntExtAuthorPassAddReceived": fsTacClntExtAuthorPassAddReceived,
       "fsTacClntExtAuthorPassReplReceived": fsTacClntExtAuthorPassReplReceived,
       "fsTacClntExtAuthorFailReceived": fsTacClntExtAuthorFailReceived,
       "fsTacClntExtAuthorErrorReceived": fsTacClntExtAuthorErrorReceived,
       "fsTacClntExtAuthorFollowReceived": fsTacClntExtAuthorFollowReceived,
       "fsTacClntExtAuthorSessionTimeouts": fsTacClntExtAuthorSessionTimeouts,
       "fsTacClntExtAcctStartRequests": fsTacClntExtAcctStartRequests,
       "fsTacClntExtAcctWdRequests": fsTacClntExtAcctWdRequests,
       "fsTacClntExtAcctStopRequests": fsTacClntExtAcctStopRequests,
       "fsTacClntExtAcctSuccessReceived": fsTacClntExtAcctSuccessReceived,
       "fsTacClntExtAcctErrorReceived": fsTacClntExtAcctErrorReceived,
       "fsTacClntExtAcctFollowReceived": fsTacClntExtAcctFollowReceived,
       "fsTacClntExtAcctSessionTimeouts": fsTacClntExtAcctSessionTimeouts,
       "fsTacClntExtMalformedPktsReceived": fsTacClntExtMalformedPktsReceived,
       "fsTacClntExtSocketFailures": fsTacClntExtSocketFailures,
       "fsTacClntExtConnectionFailures": fsTacClntExtConnectionFailures,
       "futureTacacsClientExtTableGroup": futureTacacsClientExtTableGroup,
       "fsTacClntExtServerTable": fsTacClntExtServerTable,
       "fsTacClntExtServerEntry": fsTacClntExtServerEntry,
       "fsTacClntExtServerAddressType": fsTacClntExtServerAddressType,
       "fsTacClntExtServerAddress": fsTacClntExtServerAddress,
       "fsTacClntExtServerStatus": fsTacClntExtServerStatus,
       "fsTacClntExtServerSingleConnect": fsTacClntExtServerSingleConnect,
       "fsTacClntExtServerPort": fsTacClntExtServerPort,
       "fsTacClntExtServerTimeout": fsTacClntExtServerTimeout,
       "fsTacClntExtServerKey": fsTacClntExtServerKey}
)
