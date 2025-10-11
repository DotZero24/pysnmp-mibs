# SNMP MIB module (SUPERMICRO-RADIUS-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-RADIUS-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:19 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

futureRADIUSEXTMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30)
)
if mibBuilder.loadTexts:
    futureRADIUSEXTMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsRadExtClient_ObjectIdentity = ObjectIdentity
fsRadExtClient = _FsRadExtClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1)
)
_FsRadExtServer_ObjectIdentity = ObjectIdentity
fsRadExtServer = _FsRadExtServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 1)
)
_FsRadExtDebugMask_Type = Integer32
_FsRadExtDebugMask_Object = MibScalar
fsRadExtDebugMask = _FsRadExtDebugMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 1, 1),
    _FsRadExtDebugMask_Type()
)
fsRadExtDebugMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRadExtDebugMask.setStatus("current")


class _FsRadExtMaxNoOfUserEntries_Type(Integer32):
    """Custom type fsRadExtMaxNoOfUserEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsRadExtMaxNoOfUserEntries_Type.__name__ = "Integer32"
_FsRadExtMaxNoOfUserEntries_Object = MibScalar
fsRadExtMaxNoOfUserEntries = _FsRadExtMaxNoOfUserEntries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 1, 2),
    _FsRadExtMaxNoOfUserEntries_Type()
)
fsRadExtMaxNoOfUserEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRadExtMaxNoOfUserEntries.setStatus("current")
_FsRadExtPrimaryServerAddressType_Type = InetAddressType
_FsRadExtPrimaryServerAddressType_Object = MibScalar
fsRadExtPrimaryServerAddressType = _FsRadExtPrimaryServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 1, 3),
    _FsRadExtPrimaryServerAddressType_Type()
)
fsRadExtPrimaryServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRadExtPrimaryServerAddressType.setStatus("current")


class _FsRadExtPrimaryServer_Type(InetAddress):
    """Custom type fsRadExtPrimaryServer based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsRadExtPrimaryServer_Type.__name__ = "InetAddress"
_FsRadExtPrimaryServer_Object = MibScalar
fsRadExtPrimaryServer = _FsRadExtPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 1, 4),
    _FsRadExtPrimaryServer_Type()
)
fsRadExtPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRadExtPrimaryServer.setStatus("current")
_FsRadExtServerTable_Object = MibTable
fsRadExtServerTable = _FsRadExtServerTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 1, 5)
)
if mibBuilder.loadTexts:
    fsRadExtServerTable.setStatus("current")
_FsRadExtServerEntry_Object = MibTableRow
fsRadExtServerEntry = _FsRadExtServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 1, 5, 1)
)
fsRadExtServerEntry.setIndexNames(
    (0, "SUPERMICRO-RADIUS-EXT-MIB", "fsRadExtServerIndex"),
)
if mibBuilder.loadTexts:
    fsRadExtServerEntry.setStatus("current")


class _FsRadExtServerIndex_Type(Integer32):
    """Custom type fsRadExtServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_FsRadExtServerIndex_Type.__name__ = "Integer32"
_FsRadExtServerIndex_Object = MibTableColumn
fsRadExtServerIndex = _FsRadExtServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 1, 5, 1, 1),
    _FsRadExtServerIndex_Type()
)
fsRadExtServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRadExtServerIndex.setStatus("current")
_FsRadExtServerAddrType_Type = InetAddressType
_FsRadExtServerAddrType_Object = MibTableColumn
fsRadExtServerAddrType = _FsRadExtServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 1, 5, 1, 2),
    _FsRadExtServerAddrType_Type()
)
fsRadExtServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRadExtServerAddrType.setStatus("current")
_FsRadExtServerAddress_Type = InetAddress
_FsRadExtServerAddress_Object = MibTableColumn
fsRadExtServerAddress = _FsRadExtServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 1, 5, 1, 3),
    _FsRadExtServerAddress_Type()
)
fsRadExtServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRadExtServerAddress.setStatus("current")


class _FsRadExtServerType_Type(Integer32):
    """Custom type fsRadExtServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auth", 1),
          ("acct", 2),
          ("both", 3))
    )


_FsRadExtServerType_Type.__name__ = "Integer32"
_FsRadExtServerType_Object = MibTableColumn
fsRadExtServerType = _FsRadExtServerType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 1, 5, 1, 4),
    _FsRadExtServerType_Type()
)
fsRadExtServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRadExtServerType.setStatus("current")
_FsRadExtServerSharedSecret_Type = DisplayString
_FsRadExtServerSharedSecret_Object = MibTableColumn
fsRadExtServerSharedSecret = _FsRadExtServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 1, 5, 1, 5),
    _FsRadExtServerSharedSecret_Type()
)
fsRadExtServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRadExtServerSharedSecret.setStatus("current")


class _FsRadExtServerEnabled_Type(Integer32):
    """Custom type fsRadExtServerEnabled based on Integer32"""
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
        *(("enabled", 1),
          ("disabled", 2),
          ("destroy", 3))
    )


_FsRadExtServerEnabled_Type.__name__ = "Integer32"
_FsRadExtServerEnabled_Object = MibTableColumn
fsRadExtServerEnabled = _FsRadExtServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 1, 5, 1, 6),
    _FsRadExtServerEnabled_Type()
)
fsRadExtServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRadExtServerEnabled.setStatus("current")


class _FsRadExtServerResponseTime_Type(Integer32):
    """Custom type fsRadExtServerResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_FsRadExtServerResponseTime_Type.__name__ = "Integer32"
_FsRadExtServerResponseTime_Object = MibTableColumn
fsRadExtServerResponseTime = _FsRadExtServerResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 1, 5, 1, 7),
    _FsRadExtServerResponseTime_Type()
)
fsRadExtServerResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRadExtServerResponseTime.setStatus("current")


class _FsRadExtServerMaximumRetransmission_Type(Integer32):
    """Custom type fsRadExtServerMaximumRetransmission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_FsRadExtServerMaximumRetransmission_Type.__name__ = "Integer32"
_FsRadExtServerMaximumRetransmission_Object = MibTableColumn
fsRadExtServerMaximumRetransmission = _FsRadExtServerMaximumRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 1, 5, 1, 8),
    _FsRadExtServerMaximumRetransmission_Type()
)
fsRadExtServerMaximumRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRadExtServerMaximumRetransmission.setStatus("current")
_FsRadExtServerEntryStatus_Type = RowStatus
_FsRadExtServerEntryStatus_Object = MibTableColumn
fsRadExtServerEntryStatus = _FsRadExtServerEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 1, 5, 1, 9),
    _FsRadExtServerEntryStatus_Type()
)
fsRadExtServerEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRadExtServerEntryStatus.setStatus("current")
_FsRadAuthClient_ObjectIdentity = ObjectIdentity
fsRadAuthClient = _FsRadAuthClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2)
)
_FsRadExtAuthClientInvalidServerAddresses_Type = Counter32
_FsRadExtAuthClientInvalidServerAddresses_Object = MibScalar
fsRadExtAuthClientInvalidServerAddresses = _FsRadExtAuthClientInvalidServerAddresses_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 1),
    _FsRadExtAuthClientInvalidServerAddresses_Type()
)
fsRadExtAuthClientInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAuthClientInvalidServerAddresses.setStatus("current")
_FsRadExtAuthClientIdentifier_Type = SnmpAdminString
_FsRadExtAuthClientIdentifier_Object = MibScalar
fsRadExtAuthClientIdentifier = _FsRadExtAuthClientIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 2),
    _FsRadExtAuthClientIdentifier_Type()
)
fsRadExtAuthClientIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAuthClientIdentifier.setStatus("current")
_FsRadExtAuthServerTable_Object = MibTable
fsRadExtAuthServerTable = _FsRadExtAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fsRadExtAuthServerTable.setStatus("current")
_FsRadExtAuthServerEntry_Object = MibTableRow
fsRadExtAuthServerEntry = _FsRadExtAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 3, 1)
)
fsRadExtAuthServerEntry.setIndexNames(
    (0, "SUPERMICRO-RADIUS-EXT-MIB", "fsRadExtAuthServerIndex"),
)
if mibBuilder.loadTexts:
    fsRadExtAuthServerEntry.setStatus("current")


class _FsRadExtAuthServerIndex_Type(Integer32):
    """Custom type fsRadExtAuthServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsRadExtAuthServerIndex_Type.__name__ = "Integer32"
_FsRadExtAuthServerIndex_Object = MibTableColumn
fsRadExtAuthServerIndex = _FsRadExtAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 3, 1, 1),
    _FsRadExtAuthServerIndex_Type()
)
fsRadExtAuthServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRadExtAuthServerIndex.setStatus("current")
_FsRadExtAuthServerAddressType_Type = InetAddressType
_FsRadExtAuthServerAddressType_Object = MibTableColumn
fsRadExtAuthServerAddressType = _FsRadExtAuthServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 3, 1, 2),
    _FsRadExtAuthServerAddressType_Type()
)
fsRadExtAuthServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAuthServerAddressType.setStatus("current")
_FsRadExtAuthServerAddress_Type = InetAddress
_FsRadExtAuthServerAddress_Object = MibTableColumn
fsRadExtAuthServerAddress = _FsRadExtAuthServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 3, 1, 3),
    _FsRadExtAuthServerAddress_Type()
)
fsRadExtAuthServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAuthServerAddress.setStatus("current")


class _FsRadExtAuthClientServerPortNumber_Type(Integer32):
    """Custom type fsRadExtAuthClientServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsRadExtAuthClientServerPortNumber_Type.__name__ = "Integer32"
_FsRadExtAuthClientServerPortNumber_Object = MibTableColumn
fsRadExtAuthClientServerPortNumber = _FsRadExtAuthClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 3, 1, 4),
    _FsRadExtAuthClientServerPortNumber_Type()
)
fsRadExtAuthClientServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRadExtAuthClientServerPortNumber.setStatus("current")
_FsRadExtAuthClientRoundTripTime_Type = TimeTicks
_FsRadExtAuthClientRoundTripTime_Object = MibTableColumn
fsRadExtAuthClientRoundTripTime = _FsRadExtAuthClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 3, 1, 5),
    _FsRadExtAuthClientRoundTripTime_Type()
)
fsRadExtAuthClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAuthClientRoundTripTime.setStatus("current")
_FsRadExtAuthClientAccessRequests_Type = Counter32
_FsRadExtAuthClientAccessRequests_Object = MibTableColumn
fsRadExtAuthClientAccessRequests = _FsRadExtAuthClientAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 3, 1, 6),
    _FsRadExtAuthClientAccessRequests_Type()
)
fsRadExtAuthClientAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAuthClientAccessRequests.setStatus("current")
_FsRadExtAuthClientAccessRetransmissions_Type = Counter32
_FsRadExtAuthClientAccessRetransmissions_Object = MibTableColumn
fsRadExtAuthClientAccessRetransmissions = _FsRadExtAuthClientAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 3, 1, 7),
    _FsRadExtAuthClientAccessRetransmissions_Type()
)
fsRadExtAuthClientAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAuthClientAccessRetransmissions.setStatus("current")
_FsRadExtAuthClientAccessAccepts_Type = Counter32
_FsRadExtAuthClientAccessAccepts_Object = MibTableColumn
fsRadExtAuthClientAccessAccepts = _FsRadExtAuthClientAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 3, 1, 8),
    _FsRadExtAuthClientAccessAccepts_Type()
)
fsRadExtAuthClientAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAuthClientAccessAccepts.setStatus("current")
_FsRadExtAuthClientAccessRejects_Type = Counter32
_FsRadExtAuthClientAccessRejects_Object = MibTableColumn
fsRadExtAuthClientAccessRejects = _FsRadExtAuthClientAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 3, 1, 9),
    _FsRadExtAuthClientAccessRejects_Type()
)
fsRadExtAuthClientAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAuthClientAccessRejects.setStatus("current")
_FsRadExtAuthClientAccessChallenges_Type = Counter32
_FsRadExtAuthClientAccessChallenges_Object = MibTableColumn
fsRadExtAuthClientAccessChallenges = _FsRadExtAuthClientAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 3, 1, 10),
    _FsRadExtAuthClientAccessChallenges_Type()
)
fsRadExtAuthClientAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAuthClientAccessChallenges.setStatus("current")
_FsRadExtAuthClientMalformedAccessResponses_Type = Counter32
_FsRadExtAuthClientMalformedAccessResponses_Object = MibTableColumn
fsRadExtAuthClientMalformedAccessResponses = _FsRadExtAuthClientMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 3, 1, 11),
    _FsRadExtAuthClientMalformedAccessResponses_Type()
)
fsRadExtAuthClientMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAuthClientMalformedAccessResponses.setStatus("current")
_FsRadExtAuthClientBadAuthenticators_Type = Counter32
_FsRadExtAuthClientBadAuthenticators_Object = MibTableColumn
fsRadExtAuthClientBadAuthenticators = _FsRadExtAuthClientBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 3, 1, 12),
    _FsRadExtAuthClientBadAuthenticators_Type()
)
fsRadExtAuthClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAuthClientBadAuthenticators.setStatus("current")
_FsRadExtAuthClientPendingRequests_Type = Gauge32
_FsRadExtAuthClientPendingRequests_Object = MibTableColumn
fsRadExtAuthClientPendingRequests = _FsRadExtAuthClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 3, 1, 13),
    _FsRadExtAuthClientPendingRequests_Type()
)
fsRadExtAuthClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAuthClientPendingRequests.setStatus("current")
_FsRadExtAuthClientTimeouts_Type = Counter32
_FsRadExtAuthClientTimeouts_Object = MibTableColumn
fsRadExtAuthClientTimeouts = _FsRadExtAuthClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 3, 1, 14),
    _FsRadExtAuthClientTimeouts_Type()
)
fsRadExtAuthClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAuthClientTimeouts.setStatus("current")
_FsRadExtAuthClientUnknownTypes_Type = Counter32
_FsRadExtAuthClientUnknownTypes_Object = MibTableColumn
fsRadExtAuthClientUnknownTypes = _FsRadExtAuthClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 3, 1, 15),
    _FsRadExtAuthClientUnknownTypes_Type()
)
fsRadExtAuthClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAuthClientUnknownTypes.setStatus("current")
_FsRadExtAuthClientPacketsDropped_Type = Counter32
_FsRadExtAuthClientPacketsDropped_Object = MibTableColumn
fsRadExtAuthClientPacketsDropped = _FsRadExtAuthClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 2, 3, 1, 16),
    _FsRadExtAuthClientPacketsDropped_Type()
)
fsRadExtAuthClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAuthClientPacketsDropped.setStatus("current")
_FsRadAccClient_ObjectIdentity = ObjectIdentity
fsRadAccClient = _FsRadAccClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3)
)
_FsRadExtAccClientInvalidServerAddresses_Type = Counter32
_FsRadExtAccClientInvalidServerAddresses_Object = MibScalar
fsRadExtAccClientInvalidServerAddresses = _FsRadExtAccClientInvalidServerAddresses_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3, 1),
    _FsRadExtAccClientInvalidServerAddresses_Type()
)
fsRadExtAccClientInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAccClientInvalidServerAddresses.setStatus("current")
_FsRadExtAccClientIdentifier_Type = SnmpAdminString
_FsRadExtAccClientIdentifier_Object = MibScalar
fsRadExtAccClientIdentifier = _FsRadExtAccClientIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3, 2),
    _FsRadExtAccClientIdentifier_Type()
)
fsRadExtAccClientIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAccClientIdentifier.setStatus("current")
_FsRadExtAccServerTable_Object = MibTable
fsRadExtAccServerTable = _FsRadExtAccServerTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3, 3)
)
if mibBuilder.loadTexts:
    fsRadExtAccServerTable.setStatus("current")
_FsRadExtAccServerEntry_Object = MibTableRow
fsRadExtAccServerEntry = _FsRadExtAccServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3, 3, 1)
)
fsRadExtAccServerEntry.setIndexNames(
    (0, "SUPERMICRO-RADIUS-EXT-MIB", "fsRadExtAccServerIndex"),
)
if mibBuilder.loadTexts:
    fsRadExtAccServerEntry.setStatus("current")


class _FsRadExtAccServerIndex_Type(Integer32):
    """Custom type fsRadExtAccServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsRadExtAccServerIndex_Type.__name__ = "Integer32"
_FsRadExtAccServerIndex_Object = MibTableColumn
fsRadExtAccServerIndex = _FsRadExtAccServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3, 3, 1, 1),
    _FsRadExtAccServerIndex_Type()
)
fsRadExtAccServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRadExtAccServerIndex.setStatus("current")
_FsRadExtAccServerAddressType_Type = InetAddressType
_FsRadExtAccServerAddressType_Object = MibTableColumn
fsRadExtAccServerAddressType = _FsRadExtAccServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3, 3, 1, 2),
    _FsRadExtAccServerAddressType_Type()
)
fsRadExtAccServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAccServerAddressType.setStatus("current")
_FsRadExtAccServerAddress_Type = InetAddress
_FsRadExtAccServerAddress_Object = MibTableColumn
fsRadExtAccServerAddress = _FsRadExtAccServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3, 3, 1, 3),
    _FsRadExtAccServerAddress_Type()
)
fsRadExtAccServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAccServerAddress.setStatus("current")


class _FsRadExtAccClientServerPortNumber_Type(Integer32):
    """Custom type fsRadExtAccClientServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsRadExtAccClientServerPortNumber_Type.__name__ = "Integer32"
_FsRadExtAccClientServerPortNumber_Object = MibTableColumn
fsRadExtAccClientServerPortNumber = _FsRadExtAccClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3, 3, 1, 4),
    _FsRadExtAccClientServerPortNumber_Type()
)
fsRadExtAccClientServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRadExtAccClientServerPortNumber.setStatus("current")
_FsRadExtAccClientRoundTripTime_Type = TimeTicks
_FsRadExtAccClientRoundTripTime_Object = MibTableColumn
fsRadExtAccClientRoundTripTime = _FsRadExtAccClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3, 3, 1, 5),
    _FsRadExtAccClientRoundTripTime_Type()
)
fsRadExtAccClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAccClientRoundTripTime.setStatus("current")
_FsRadExtAccClientRequests_Type = Counter32
_FsRadExtAccClientRequests_Object = MibTableColumn
fsRadExtAccClientRequests = _FsRadExtAccClientRequests_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3, 3, 1, 6),
    _FsRadExtAccClientRequests_Type()
)
fsRadExtAccClientRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAccClientRequests.setStatus("current")
_FsRadExtAccClientRetransmissions_Type = Counter32
_FsRadExtAccClientRetransmissions_Object = MibTableColumn
fsRadExtAccClientRetransmissions = _FsRadExtAccClientRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3, 3, 1, 7),
    _FsRadExtAccClientRetransmissions_Type()
)
fsRadExtAccClientRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAccClientRetransmissions.setStatus("current")
_FsRadExtAccClientResponses_Type = Counter32
_FsRadExtAccClientResponses_Object = MibTableColumn
fsRadExtAccClientResponses = _FsRadExtAccClientResponses_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3, 3, 1, 8),
    _FsRadExtAccClientResponses_Type()
)
fsRadExtAccClientResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAccClientResponses.setStatus("current")
_FsRadExtAccClientMalformedResponses_Type = Counter32
_FsRadExtAccClientMalformedResponses_Object = MibTableColumn
fsRadExtAccClientMalformedResponses = _FsRadExtAccClientMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3, 3, 1, 9),
    _FsRadExtAccClientMalformedResponses_Type()
)
fsRadExtAccClientMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAccClientMalformedResponses.setStatus("current")
_FsRadExtAccClientBadAuthenticators_Type = Counter32
_FsRadExtAccClientBadAuthenticators_Object = MibTableColumn
fsRadExtAccClientBadAuthenticators = _FsRadExtAccClientBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3, 3, 1, 10),
    _FsRadExtAccClientBadAuthenticators_Type()
)
fsRadExtAccClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAccClientBadAuthenticators.setStatus("current")
_FsRadExtAccClientPendingRequests_Type = Gauge32
_FsRadExtAccClientPendingRequests_Object = MibTableColumn
fsRadExtAccClientPendingRequests = _FsRadExtAccClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3, 3, 1, 11),
    _FsRadExtAccClientPendingRequests_Type()
)
fsRadExtAccClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAccClientPendingRequests.setStatus("current")
_FsRadExtAccClientTimeouts_Type = Counter32
_FsRadExtAccClientTimeouts_Object = MibTableColumn
fsRadExtAccClientTimeouts = _FsRadExtAccClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3, 3, 1, 12),
    _FsRadExtAccClientTimeouts_Type()
)
fsRadExtAccClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAccClientTimeouts.setStatus("current")
_FsRadExtAccClientUnknownTypes_Type = Counter32
_FsRadExtAccClientUnknownTypes_Object = MibTableColumn
fsRadExtAccClientUnknownTypes = _FsRadExtAccClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3, 3, 1, 13),
    _FsRadExtAccClientUnknownTypes_Type()
)
fsRadExtAccClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAccClientUnknownTypes.setStatus("current")
_FsRadExtAccClientPacketsDropped_Type = Counter32
_FsRadExtAccClientPacketsDropped_Object = MibTableColumn
fsRadExtAccClientPacketsDropped = _FsRadExtAccClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 30, 1, 3, 3, 1, 14),
    _FsRadExtAccClientPacketsDropped_Type()
)
fsRadExtAccClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRadExtAccClientPacketsDropped.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-RADIUS-EXT-MIB",
    **{"futureRADIUSEXTMIB": futureRADIUSEXTMIB,
       "fsRadExtClient": fsRadExtClient,
       "fsRadExtServer": fsRadExtServer,
       "fsRadExtDebugMask": fsRadExtDebugMask,
       "fsRadExtMaxNoOfUserEntries": fsRadExtMaxNoOfUserEntries,
       "fsRadExtPrimaryServerAddressType": fsRadExtPrimaryServerAddressType,
       "fsRadExtPrimaryServer": fsRadExtPrimaryServer,
       "fsRadExtServerTable": fsRadExtServerTable,
       "fsRadExtServerEntry": fsRadExtServerEntry,
       "fsRadExtServerIndex": fsRadExtServerIndex,
       "fsRadExtServerAddrType": fsRadExtServerAddrType,
       "fsRadExtServerAddress": fsRadExtServerAddress,
       "fsRadExtServerType": fsRadExtServerType,
       "fsRadExtServerSharedSecret": fsRadExtServerSharedSecret,
       "fsRadExtServerEnabled": fsRadExtServerEnabled,
       "fsRadExtServerResponseTime": fsRadExtServerResponseTime,
       "fsRadExtServerMaximumRetransmission": fsRadExtServerMaximumRetransmission,
       "fsRadExtServerEntryStatus": fsRadExtServerEntryStatus,
       "fsRadAuthClient": fsRadAuthClient,
       "fsRadExtAuthClientInvalidServerAddresses": fsRadExtAuthClientInvalidServerAddresses,
       "fsRadExtAuthClientIdentifier": fsRadExtAuthClientIdentifier,
       "fsRadExtAuthServerTable": fsRadExtAuthServerTable,
       "fsRadExtAuthServerEntry": fsRadExtAuthServerEntry,
       "fsRadExtAuthServerIndex": fsRadExtAuthServerIndex,
       "fsRadExtAuthServerAddressType": fsRadExtAuthServerAddressType,
       "fsRadExtAuthServerAddress": fsRadExtAuthServerAddress,
       "fsRadExtAuthClientServerPortNumber": fsRadExtAuthClientServerPortNumber,
       "fsRadExtAuthClientRoundTripTime": fsRadExtAuthClientRoundTripTime,
       "fsRadExtAuthClientAccessRequests": fsRadExtAuthClientAccessRequests,
       "fsRadExtAuthClientAccessRetransmissions": fsRadExtAuthClientAccessRetransmissions,
       "fsRadExtAuthClientAccessAccepts": fsRadExtAuthClientAccessAccepts,
       "fsRadExtAuthClientAccessRejects": fsRadExtAuthClientAccessRejects,
       "fsRadExtAuthClientAccessChallenges": fsRadExtAuthClientAccessChallenges,
       "fsRadExtAuthClientMalformedAccessResponses": fsRadExtAuthClientMalformedAccessResponses,
       "fsRadExtAuthClientBadAuthenticators": fsRadExtAuthClientBadAuthenticators,
       "fsRadExtAuthClientPendingRequests": fsRadExtAuthClientPendingRequests,
       "fsRadExtAuthClientTimeouts": fsRadExtAuthClientTimeouts,
       "fsRadExtAuthClientUnknownTypes": fsRadExtAuthClientUnknownTypes,
       "fsRadExtAuthClientPacketsDropped": fsRadExtAuthClientPacketsDropped,
       "fsRadAccClient": fsRadAccClient,
       "fsRadExtAccClientInvalidServerAddresses": fsRadExtAccClientInvalidServerAddresses,
       "fsRadExtAccClientIdentifier": fsRadExtAccClientIdentifier,
       "fsRadExtAccServerTable": fsRadExtAccServerTable,
       "fsRadExtAccServerEntry": fsRadExtAccServerEntry,
       "fsRadExtAccServerIndex": fsRadExtAccServerIndex,
       "fsRadExtAccServerAddressType": fsRadExtAccServerAddressType,
       "fsRadExtAccServerAddress": fsRadExtAccServerAddress,
       "fsRadExtAccClientServerPortNumber": fsRadExtAccClientServerPortNumber,
       "fsRadExtAccClientRoundTripTime": fsRadExtAccClientRoundTripTime,
       "fsRadExtAccClientRequests": fsRadExtAccClientRequests,
       "fsRadExtAccClientRetransmissions": fsRadExtAccClientRetransmissions,
       "fsRadExtAccClientResponses": fsRadExtAccClientResponses,
       "fsRadExtAccClientMalformedResponses": fsRadExtAccClientMalformedResponses,
       "fsRadExtAccClientBadAuthenticators": fsRadExtAccClientBadAuthenticators,
       "fsRadExtAccClientPendingRequests": fsRadExtAccClientPendingRequests,
       "fsRadExtAccClientTimeouts": fsRadExtAccClientTimeouts,
       "fsRadExtAccClientUnknownTypes": fsRadExtAccClientUnknownTypes,
       "fsRadExtAccClientPacketsDropped": fsRadExtAccClientPacketsDropped}
)
