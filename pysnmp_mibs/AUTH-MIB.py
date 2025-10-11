# SNMP MIB module (AUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/AUTH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:51:51 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(PaeControlledPortStatus,
 dot1xPaePortNumber) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "PaeControlledPortStatus",
    "dot1xPaePortNumber")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

swAuthCtrl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(TextualConvention, OctetString):
    status = "current"


class VlanId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_SwAuthenCtrl_ObjectIdentity = ObjectIdentity
swAuthenCtrl = _SwAuthenCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 1)
)


class _AuthProtocol_Type(Integer32):
    """Custom type authProtocol based on Integer32"""
    defaultValue = 4

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
        *(("authProtocolNone", 1),
          ("authProtocolLocal", 2),
          ("authProtocolRadius", 3),
          ("authProtocolRadiusEap", 4),
          ("authProtocolRadiusChap", 5),
          ("authProtocolTacacs", 6))
    )


_AuthProtocol_Type.__name__ = "Integer32"
_AuthProtocol_Object = MibScalar
authProtocol = _AuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 1, 1),
    _AuthProtocol_Type()
)
authProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authProtocol.setStatus("current")


class _SwAuthMode_Type(Integer32):
    """Custom type swAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portBase", 1),
          ("macBase", 2))
    )


_SwAuthMode_Type.__name__ = "Integer32"
_SwAuthMode_Object = MibScalar
swAuthMode = _SwAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 1, 2),
    _SwAuthMode_Type()
)
swAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthMode.setStatus("current")


class _SwAuthorizationState_Type(Integer32):
    """Custom type swAuthorizationState based on Integer32"""
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


_SwAuthorizationState_Type.__name__ = "Integer32"
_SwAuthorizationState_Object = MibScalar
swAuthorizationState = _SwAuthorizationState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 1, 3),
    _SwAuthorizationState_Type()
)
swAuthorizationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthorizationState.setStatus("current")


class _SwAuthFailOver_Type(Integer32):
    """Custom type swAuthFailOver based on Integer32"""
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


_SwAuthFailOver_Type.__name__ = "Integer32"
_SwAuthFailOver_Object = MibScalar
swAuthFailOver = _SwAuthFailOver_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 1, 4),
    _SwAuthFailOver_Type()
)
swAuthFailOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthFailOver.setStatus("current")
_SwRadiusCtrl_ObjectIdentity = ObjectIdentity
swRadiusCtrl = _SwRadiusCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2)
)


class _SwRadiusDeadTime_Type(Unsigned32):
    """Custom type swRadiusDeadTime based on Unsigned32"""
    defaultValue = 1


_SwRadiusDeadTime_Type.__name__ = "Unsigned32"
_SwRadiusDeadTime_Object = MibScalar
swRadiusDeadTime = _SwRadiusDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 1),
    _SwRadiusDeadTime_Type()
)
swRadiusDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusDeadTime.setStatus("current")


class _SwRadiusTimeout_Type(Unsigned32):
    """Custom type swRadiusTimeout based on Unsigned32"""
    defaultValue = 10


_SwRadiusTimeout_Type.__name__ = "Unsigned32"
_SwRadiusTimeout_Object = MibScalar
swRadiusTimeout = _SwRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 2),
    _SwRadiusTimeout_Type()
)
swRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusTimeout.setStatus("current")


class _SwRadiusRetransmitAttempts_Type(Unsigned32):
    """Custom type swRadiusRetransmitAttempts based on Unsigned32"""
    defaultValue = 2


_SwRadiusRetransmitAttempts_Type.__name__ = "Unsigned32"
_SwRadiusRetransmitAttempts_Object = MibScalar
swRadiusRetransmitAttempts = _SwRadiusRetransmitAttempts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 3),
    _SwRadiusRetransmitAttempts_Type()
)
swRadiusRetransmitAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusRetransmitAttempts.setStatus("current")
_SwRadiusServerTable_Object = MibTable
swRadiusServerTable = _SwRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4)
)
if mibBuilder.loadTexts:
    swRadiusServerTable.setStatus("current")
_SwRadiusServerEntry_Object = MibTableRow
swRadiusServerEntry = _SwRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1)
)
swRadiusServerEntry.setIndexNames(
    (0, "AUTH-MIB", "swRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    swRadiusServerEntry.setStatus("current")


class _SwRadiusServerIndex_Type(Integer32):
    """Custom type swRadiusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("swRadiusServerIndex-first", 1),
          ("swRadiusServerIndex-second", 2),
          ("swRadiusServerIndex-third", 3))
    )


_SwRadiusServerIndex_Type.__name__ = "Integer32"
_SwRadiusServerIndex_Object = MibTableColumn
swRadiusServerIndex = _SwRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 1),
    _SwRadiusServerIndex_Type()
)
swRadiusServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusServerIndex.setStatus("current")
_SwRadiusServerIpAddr_Type = IpAddress
_SwRadiusServerIpAddr_Object = MibTableColumn
swRadiusServerIpAddr = _SwRadiusServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 2),
    _SwRadiusServerIpAddr_Type()
)
swRadiusServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusServerIpAddr.setStatus("obsolete")


class _SwRadiusServerKey_Type(OctetString):
    """Custom type swRadiusServerKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwRadiusServerKey_Type.__name__ = "OctetString"
_SwRadiusServerKey_Object = MibTableColumn
swRadiusServerKey = _SwRadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 3),
    _SwRadiusServerKey_Type()
)
swRadiusServerKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swRadiusServerKey.setStatus("current")


class _SwRadiusAuthPortNumber_Type(Unsigned32):
    """Custom type swRadiusAuthPortNumber based on Unsigned32"""
    defaultValue = 1812


_SwRadiusAuthPortNumber_Type.__name__ = "Unsigned32"
_SwRadiusAuthPortNumber_Object = MibTableColumn
swRadiusAuthPortNumber = _SwRadiusAuthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 4),
    _SwRadiusAuthPortNumber_Type()
)
swRadiusAuthPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthPortNumber.setStatus("current")


class _SwRadiusAcctPortNumber_Type(Unsigned32):
    """Custom type swRadiusAcctPortNumber based on Unsigned32"""
    defaultValue = 1813


_SwRadiusAcctPortNumber_Type.__name__ = "Unsigned32"
_SwRadiusAcctPortNumber_Object = MibTableColumn
swRadiusAcctPortNumber = _SwRadiusAcctPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 5),
    _SwRadiusAcctPortNumber_Type()
)
swRadiusAcctPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAcctPortNumber.setStatus("current")
_SwRadiusServerStatus_Type = RowStatus
_SwRadiusServerStatus_Object = MibTableColumn
swRadiusServerStatus = _SwRadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 6),
    _SwRadiusServerStatus_Type()
)
swRadiusServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusServerStatus.setStatus("current")


class _SwRadiusServerTimeout_Type(Unsigned32):
    """Custom type swRadiusServerTimeout based on Unsigned32"""
    defaultValue = 5


_SwRadiusServerTimeout_Type.__name__ = "Unsigned32"
_SwRadiusServerTimeout_Object = MibTableColumn
swRadiusServerTimeout = _SwRadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 7),
    _SwRadiusServerTimeout_Type()
)
swRadiusServerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusServerTimeout.setStatus("current")


class _SwRadiusServerRetransmit_Type(Unsigned32):
    """Custom type swRadiusServerRetransmit based on Unsigned32"""
    defaultValue = 2


_SwRadiusServerRetransmit_Type.__name__ = "Unsigned32"
_SwRadiusServerRetransmit_Object = MibTableColumn
swRadiusServerRetransmit = _SwRadiusServerRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 8),
    _SwRadiusServerRetransmit_Type()
)
swRadiusServerRetransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusServerRetransmit.setStatus("current")


class _SwRadiusServerAddrType_Type(InetAddressType):
    """Custom type swRadiusServerAddrType based on InetAddressType"""
    defaultValue = 1


_SwRadiusServerAddrType_Type.__name__ = "InetAddressType"
_SwRadiusServerAddrType_Object = MibTableColumn
swRadiusServerAddrType = _SwRadiusServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 9),
    _SwRadiusServerAddrType_Type()
)
swRadiusServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusServerAddrType.setStatus("current")
_SwRadiusServerAddr_Type = InetAddress
_SwRadiusServerAddr_Object = MibTableColumn
swRadiusServerAddr = _SwRadiusServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 4, 1, 10),
    _SwRadiusServerAddr_Type()
)
swRadiusServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusServerAddr.setStatus("current")


class _SwRadiusVrfName_Type(DisplayString):
    """Custom type swRadiusVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SwRadiusVrfName_Type.__name__ = "DisplayString"
_SwRadiusVrfName_Object = MibScalar
swRadiusVrfName = _SwRadiusVrfName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 2, 5),
    _SwRadiusVrfName_Type()
)
swRadiusVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusVrfName.setStatus("current")
_SwRadiusAuthInfo_ObjectIdentity = ObjectIdentity
swRadiusAuthInfo = _SwRadiusAuthInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3)
)


class _SwRadiusAuthClientIdentifier_Type(OctetString):
    """Custom type swRadiusAuthClientIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SwRadiusAuthClientIdentifier_Type.__name__ = "OctetString"
_SwRadiusAuthClientIdentifier_Object = MibScalar
swRadiusAuthClientIdentifier = _SwRadiusAuthClientIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 1),
    _SwRadiusAuthClientIdentifier_Type()
)
swRadiusAuthClientIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientIdentifier.setStatus("obsolete")
_SwRadiusAuthClientInvalidServerAddresses_Type = Counter32
_SwRadiusAuthClientInvalidServerAddresses_Object = MibScalar
swRadiusAuthClientInvalidServerAddresses = _SwRadiusAuthClientInvalidServerAddresses_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 2),
    _SwRadiusAuthClientInvalidServerAddresses_Type()
)
swRadiusAuthClientInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientInvalidServerAddresses.setStatus("obsolete")
_SwRadiusAuthServerTable_Object = MibTable
swRadiusAuthServerTable = _SwRadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3)
)
if mibBuilder.loadTexts:
    swRadiusAuthServerTable.setStatus("current")
_SwRadiusAuthServerEntry_Object = MibTableRow
swRadiusAuthServerEntry = _SwRadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1)
)
swRadiusAuthServerEntry.setIndexNames(
    (0, "AUTH-MIB", "swRadiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    swRadiusAuthServerEntry.setStatus("obsolete")
_SwRadiusAuthServerIndex_Type = Integer32
_SwRadiusAuthServerIndex_Object = MibTableColumn
swRadiusAuthServerIndex = _SwRadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 1),
    _SwRadiusAuthServerIndex_Type()
)
swRadiusAuthServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthServerIndex.setStatus("obsolete")
_SwRadiusAuthServerAddress_Type = IpAddress
_SwRadiusAuthServerAddress_Object = MibTableColumn
swRadiusAuthServerAddress = _SwRadiusAuthServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 2),
    _SwRadiusAuthServerAddress_Type()
)
swRadiusAuthServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthServerAddress.setStatus("obsolete")


class _SwRadiusAuthClientServerPortNumber_Type(Unsigned32):
    """Custom type swRadiusAuthClientServerPortNumber based on Unsigned32"""
    defaultValue = 1812


_SwRadiusAuthClientServerPortNumber_Type.__name__ = "Unsigned32"
_SwRadiusAuthClientServerPortNumber_Object = MibTableColumn
swRadiusAuthClientServerPortNumber = _SwRadiusAuthClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 3),
    _SwRadiusAuthClientServerPortNumber_Type()
)
swRadiusAuthClientServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientServerPortNumber.setStatus("obsolete")
_SwRadiusAuthClientRoundTripTime_Type = Counter32
_SwRadiusAuthClientRoundTripTime_Object = MibTableColumn
swRadiusAuthClientRoundTripTime = _SwRadiusAuthClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 4),
    _SwRadiusAuthClientRoundTripTime_Type()
)
swRadiusAuthClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientRoundTripTime.setStatus("obsolete")
_SwRadiusAuthClientAccessRequests_Type = Counter32
_SwRadiusAuthClientAccessRequests_Object = MibTableColumn
swRadiusAuthClientAccessRequests = _SwRadiusAuthClientAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 5),
    _SwRadiusAuthClientAccessRequests_Type()
)
swRadiusAuthClientAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientAccessRequests.setStatus("obsolete")
_SwRadiusAuthClientAccessRetransmissions_Type = Counter32
_SwRadiusAuthClientAccessRetransmissions_Object = MibTableColumn
swRadiusAuthClientAccessRetransmissions = _SwRadiusAuthClientAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 6),
    _SwRadiusAuthClientAccessRetransmissions_Type()
)
swRadiusAuthClientAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientAccessRetransmissions.setStatus("obsolete")
_SwRadiusAuthClientAccessAccepts_Type = Counter32
_SwRadiusAuthClientAccessAccepts_Object = MibTableColumn
swRadiusAuthClientAccessAccepts = _SwRadiusAuthClientAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 7),
    _SwRadiusAuthClientAccessAccepts_Type()
)
swRadiusAuthClientAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientAccessAccepts.setStatus("obsolete")
_SwRadiusAuthClientAccessRejects_Type = Counter32
_SwRadiusAuthClientAccessRejects_Object = MibTableColumn
swRadiusAuthClientAccessRejects = _SwRadiusAuthClientAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 8),
    _SwRadiusAuthClientAccessRejects_Type()
)
swRadiusAuthClientAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientAccessRejects.setStatus("obsolete")
_SwRadiusAuthClientAccessChallenges_Type = Counter32
_SwRadiusAuthClientAccessChallenges_Object = MibTableColumn
swRadiusAuthClientAccessChallenges = _SwRadiusAuthClientAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 9),
    _SwRadiusAuthClientAccessChallenges_Type()
)
swRadiusAuthClientAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientAccessChallenges.setStatus("obsolete")
_SwRadiusAuthClientMalformedAccessResponses_Type = Counter32
_SwRadiusAuthClientMalformedAccessResponses_Object = MibTableColumn
swRadiusAuthClientMalformedAccessResponses = _SwRadiusAuthClientMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 10),
    _SwRadiusAuthClientMalformedAccessResponses_Type()
)
swRadiusAuthClientMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientMalformedAccessResponses.setStatus("obsolete")
_SwRadiusAuthClientBadAuthenticators_Type = Counter32
_SwRadiusAuthClientBadAuthenticators_Object = MibTableColumn
swRadiusAuthClientBadAuthenticators = _SwRadiusAuthClientBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 11),
    _SwRadiusAuthClientBadAuthenticators_Type()
)
swRadiusAuthClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientBadAuthenticators.setStatus("obsolete")
_SwRadiusAuthClientPendingRequests_Type = Counter32
_SwRadiusAuthClientPendingRequests_Object = MibTableColumn
swRadiusAuthClientPendingRequests = _SwRadiusAuthClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 12),
    _SwRadiusAuthClientPendingRequests_Type()
)
swRadiusAuthClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientPendingRequests.setStatus("obsolete")
_SwRadiusAuthClientTimeouts_Type = Counter32
_SwRadiusAuthClientTimeouts_Object = MibTableColumn
swRadiusAuthClientTimeouts = _SwRadiusAuthClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 13),
    _SwRadiusAuthClientTimeouts_Type()
)
swRadiusAuthClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientTimeouts.setStatus("obsolete")
_SwRadiusAuthClientUnknownTypes_Type = Counter32
_SwRadiusAuthClientUnknownTypes_Object = MibTableColumn
swRadiusAuthClientUnknownTypes = _SwRadiusAuthClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 14),
    _SwRadiusAuthClientUnknownTypes_Type()
)
swRadiusAuthClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientUnknownTypes.setStatus("obsolete")
_SwRadiusAuthClientPacketsDropped_Type = Counter32
_SwRadiusAuthClientPacketsDropped_Object = MibTableColumn
swRadiusAuthClientPacketsDropped = _SwRadiusAuthClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 3, 3, 1, 15),
    _SwRadiusAuthClientPacketsDropped_Type()
)
swRadiusAuthClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAuthClientPacketsDropped.setStatus("obsolete")
_SwRadiusAccountingCtrl_ObjectIdentity = ObjectIdentity
swRadiusAccountingCtrl = _SwRadiusAccountingCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 4)
)
_SwRadiusAcctUpdateInterval_Type = Unsigned32
_SwRadiusAcctUpdateInterval_Object = MibScalar
swRadiusAcctUpdateInterval = _SwRadiusAcctUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 1),
    _SwRadiusAcctUpdateInterval_Type()
)
swRadiusAcctUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusAcctUpdateInterval.setStatus("current")
_SwRadiusAcctSuppressNullUserName_Type = TruthValue
_SwRadiusAcctSuppressNullUserName_Object = MibScalar
swRadiusAcctSuppressNullUserName = _SwRadiusAcctSuppressNullUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 2),
    _SwRadiusAcctSuppressNullUserName_Type()
)
swRadiusAcctSuppressNullUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusAcctSuppressNullUserName.setStatus("current")
_SwRadiusAcctServiceTable_Object = MibTable
swRadiusAcctServiceTable = _SwRadiusAcctServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 3)
)
if mibBuilder.loadTexts:
    swRadiusAcctServiceTable.setStatus("current")
_SwRadiusAcctServiceEntry_Object = MibTableRow
swRadiusAcctServiceEntry = _SwRadiusAcctServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 3, 1)
)
swRadiusAcctServiceEntry.setIndexNames(
    (0, "AUTH-MIB", "swRadiusAcctServiceIndex"),
)
if mibBuilder.loadTexts:
    swRadiusAcctServiceEntry.setStatus("current")


class _SwRadiusAcctServiceIndex_Type(Integer32):
    """Custom type swRadiusAcctServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acctServiceIndex-network", 1),
          ("acctServiceIndex-exec", 2),
          ("acctServiceIndex-system", 3))
    )


_SwRadiusAcctServiceIndex_Type.__name__ = "Integer32"
_SwRadiusAcctServiceIndex_Object = MibTableColumn
swRadiusAcctServiceIndex = _SwRadiusAcctServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 3, 1, 1),
    _SwRadiusAcctServiceIndex_Type()
)
swRadiusAcctServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRadiusAcctServiceIndex.setStatus("current")


class _SwRadiusAcctServiceMethod_Type(Integer32):
    """Custom type swRadiusAcctServiceMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("swRadiusAcctServiceMethodNone", 1),
          ("swRadiusAcctServiceMethodRadius", 2))
    )


_SwRadiusAcctServiceMethod_Type.__name__ = "Integer32"
_SwRadiusAcctServiceMethod_Object = MibTableColumn
swRadiusAcctServiceMethod = _SwRadiusAcctServiceMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 3, 1, 2),
    _SwRadiusAcctServiceMethod_Type()
)
swRadiusAcctServiceMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusAcctServiceMethod.setStatus("current")


class _SwRadiusAcctServiceMode_Type(Integer32):
    """Custom type swRadiusAcctServiceMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("radiusAcctServiceModeNone", 1),
          ("radiusAcctServiceModeStartStop", 2),
          ("radiusAcctServiceModeStopOnly", 3))
    )


_SwRadiusAcctServiceMode_Type.__name__ = "Integer32"
_SwRadiusAcctServiceMode_Object = MibTableColumn
swRadiusAcctServiceMode = _SwRadiusAcctServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 4, 3, 1, 3),
    _SwRadiusAcctServiceMode_Type()
)
swRadiusAcctServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusAcctServiceMode.setStatus("current")
_SwRadiusAccountingInfo_ObjectIdentity = ObjectIdentity
swRadiusAccountingInfo = _SwRadiusAccountingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 5)
)
_SwMacAuthBaseStatsInfo_ObjectIdentity = ObjectIdentity
swMacAuthBaseStatsInfo = _SwMacAuthBaseStatsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6)
)
_SwMacAuthStateTable_Object = MibTable
swMacAuthStateTable = _SwMacAuthStateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1)
)
if mibBuilder.loadTexts:
    swMacAuthStateTable.setStatus("obsolete")
_SwMacAuthStateEntry_Object = MibTableRow
swMacAuthStateEntry = _SwMacAuthStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1, 1)
)
swMacAuthStateEntry.setIndexNames(
    (0, "AUTH-MIB", "swPaeMacAddr"),
    (0, "AUTH-MIB", "swPaePortNumber"),
)
if mibBuilder.loadTexts:
    swMacAuthStateEntry.setStatus("obsolete")
_SwPaeMacAddr_Type = MacAddress
_SwPaeMacAddr_Object = MibTableColumn
swPaeMacAddr = _SwPaeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1, 1, 1),
    _SwPaeMacAddr_Type()
)
swPaeMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPaeMacAddr.setStatus("obsolete")
_SwPaePortNumber_Type = InterfaceIndex
_SwPaePortNumber_Object = MibTableColumn
swPaePortNumber = _SwPaePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1, 1, 2),
    _SwPaePortNumber_Type()
)
swPaePortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swPaePortNumber.setStatus("obsolete")


class _SwAuthPaeState_Type(Integer32):
    """Custom type swAuthPaeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("initialize", 1),
          ("disconnected", 2),
          ("connecting", 3),
          ("authenticating", 4),
          ("authenticated", 5),
          ("aborting", 6),
          ("held", 7),
          ("forceAuth", 8),
          ("forceUnauth", 9))
    )


_SwAuthPaeState_Type.__name__ = "Integer32"
_SwAuthPaeState_Object = MibTableColumn
swAuthPaeState = _SwAuthPaeState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1, 1, 3),
    _SwAuthPaeState_Type()
)
swAuthPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthPaeState.setStatus("obsolete")


class _SwAuthBackendAuthState_Type(Integer32):
    """Custom type swAuthBackendAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("request", 1),
          ("response", 2),
          ("success", 3),
          ("fail", 4),
          ("timeout", 5),
          ("idle", 6),
          ("initialize", 7))
    )


_SwAuthBackendAuthState_Type.__name__ = "Integer32"
_SwAuthBackendAuthState_Object = MibTableColumn
swAuthBackendAuthState = _SwAuthBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1, 1, 4),
    _SwAuthBackendAuthState_Type()
)
swAuthBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthBackendAuthState.setStatus("obsolete")
_SwAuthAuthControlledPortStatus_Type = PaeControlledPortStatus
_SwAuthAuthControlledPortStatus_Object = MibTableColumn
swAuthAuthControlledPortStatus = _SwAuthAuthControlledPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 1, 1, 5),
    _SwAuthAuthControlledPortStatus_Type()
)
swAuthAuthControlledPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthControlledPortStatus.setStatus("obsolete")
_SwMacAuthStatsTable_Object = MibTable
swMacAuthStatsTable = _SwMacAuthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2)
)
if mibBuilder.loadTexts:
    swMacAuthStatsTable.setStatus("current")
_SwMacAuthStatsEntry_Object = MibTableRow
swMacAuthStatsEntry = _SwMacAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1)
)
swMacAuthStatsEntry.setIndexNames(
    (0, "AUTH-MIB", "swPaeMacAddr"),
    (0, "AUTH-MIB", "swPaePortNumber"),
)
if mibBuilder.loadTexts:
    swMacAuthStatsEntry.setStatus("current")
_SwAuthEapolFramesRx_Type = Counter32
_SwAuthEapolFramesRx_Object = MibTableColumn
swAuthEapolFramesRx = _SwAuthEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 1),
    _SwAuthEapolFramesRx_Type()
)
swAuthEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapolFramesRx.setStatus("current")
_SwAuthEapolFramesTx_Type = Counter32
_SwAuthEapolFramesTx_Object = MibTableColumn
swAuthEapolFramesTx = _SwAuthEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 2),
    _SwAuthEapolFramesTx_Type()
)
swAuthEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapolFramesTx.setStatus("current")
_SwAuthEapolStartFramesRx_Type = Counter32
_SwAuthEapolStartFramesRx_Object = MibTableColumn
swAuthEapolStartFramesRx = _SwAuthEapolStartFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 3),
    _SwAuthEapolStartFramesRx_Type()
)
swAuthEapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapolStartFramesRx.setStatus("current")
_SwAuthEapolLogoffFramesRx_Type = Counter32
_SwAuthEapolLogoffFramesRx_Object = MibTableColumn
swAuthEapolLogoffFramesRx = _SwAuthEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 4),
    _SwAuthEapolLogoffFramesRx_Type()
)
swAuthEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapolLogoffFramesRx.setStatus("current")
_SwAuthEapolRespIdFramesRx_Type = Counter32
_SwAuthEapolRespIdFramesRx_Object = MibTableColumn
swAuthEapolRespIdFramesRx = _SwAuthEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 5),
    _SwAuthEapolRespIdFramesRx_Type()
)
swAuthEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapolRespIdFramesRx.setStatus("current")
_SwAuthEapolRespFramesRx_Type = Counter32
_SwAuthEapolRespFramesRx_Object = MibTableColumn
swAuthEapolRespFramesRx = _SwAuthEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 6),
    _SwAuthEapolRespFramesRx_Type()
)
swAuthEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapolRespFramesRx.setStatus("current")
_SwAuthEapolReqIdFramesTx_Type = Counter32
_SwAuthEapolReqIdFramesTx_Object = MibTableColumn
swAuthEapolReqIdFramesTx = _SwAuthEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 7),
    _SwAuthEapolReqIdFramesTx_Type()
)
swAuthEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapolReqIdFramesTx.setStatus("current")
_SwAuthEapolReqFramesTx_Type = Counter32
_SwAuthEapolReqFramesTx_Object = MibTableColumn
swAuthEapolReqFramesTx = _SwAuthEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 8),
    _SwAuthEapolReqFramesTx_Type()
)
swAuthEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapolReqFramesTx.setStatus("current")
_SwAuthInvalidEapolFramesRx_Type = Counter32
_SwAuthInvalidEapolFramesRx_Object = MibTableColumn
swAuthInvalidEapolFramesRx = _SwAuthInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 9),
    _SwAuthInvalidEapolFramesRx_Type()
)
swAuthInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthInvalidEapolFramesRx.setStatus("current")
_SwAuthEapLengthErrorFramesRx_Type = Counter32
_SwAuthEapLengthErrorFramesRx_Object = MibTableColumn
swAuthEapLengthErrorFramesRx = _SwAuthEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 10),
    _SwAuthEapLengthErrorFramesRx_Type()
)
swAuthEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapLengthErrorFramesRx.setStatus("current")
_SwAuthLastEapolFrameVersion_Type = Unsigned32
_SwAuthLastEapolFrameVersion_Object = MibTableColumn
swAuthLastEapolFrameVersion = _SwAuthLastEapolFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 11),
    _SwAuthLastEapolFrameVersion_Type()
)
swAuthLastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthLastEapolFrameVersion.setStatus("current")
_SwAuthLastEapolFrameSource_Type = MacAddress
_SwAuthLastEapolFrameSource_Object = MibTableColumn
swAuthLastEapolFrameSource = _SwAuthLastEapolFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 2, 1, 12),
    _SwAuthLastEapolFrameSource_Type()
)
swAuthLastEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthLastEapolFrameSource.setStatus("current")
_SwMacAuthDiagTable_Object = MibTable
swMacAuthDiagTable = _SwMacAuthDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3)
)
if mibBuilder.loadTexts:
    swMacAuthDiagTable.setStatus("current")
_SwMacAuthDiagEntry_Object = MibTableRow
swMacAuthDiagEntry = _SwMacAuthDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1)
)
swMacAuthDiagEntry.setIndexNames(
    (0, "AUTH-MIB", "swPaeMacAddr"),
    (0, "AUTH-MIB", "swPaePortNumber"),
)
if mibBuilder.loadTexts:
    swMacAuthDiagEntry.setStatus("current")
_SwAuthEntersConnecting_Type = Counter32
_SwAuthEntersConnecting_Object = MibTableColumn
swAuthEntersConnecting = _SwAuthEntersConnecting_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 1),
    _SwAuthEntersConnecting_Type()
)
swAuthEntersConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEntersConnecting.setStatus("current")
_SwAuthEapLogoffsWhileConnecting_Type = Counter32
_SwAuthEapLogoffsWhileConnecting_Object = MibTableColumn
swAuthEapLogoffsWhileConnecting = _SwAuthEapLogoffsWhileConnecting_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 2),
    _SwAuthEapLogoffsWhileConnecting_Type()
)
swAuthEapLogoffsWhileConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEapLogoffsWhileConnecting.setStatus("current")
_SwAuthEntersAuthenticating_Type = Counter32
_SwAuthEntersAuthenticating_Object = MibTableColumn
swAuthEntersAuthenticating = _SwAuthEntersAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 3),
    _SwAuthEntersAuthenticating_Type()
)
swAuthEntersAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthEntersAuthenticating.setStatus("current")
_SwAuthAuthSuccessWhileAuthenticating_Type = Counter32
_SwAuthAuthSuccessWhileAuthenticating_Object = MibTableColumn
swAuthAuthSuccessWhileAuthenticating = _SwAuthAuthSuccessWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 4),
    _SwAuthAuthSuccessWhileAuthenticating_Type()
)
swAuthAuthSuccessWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthSuccessWhileAuthenticating.setStatus("current")
_SwAuthAuthTimeoutsWhileAuthenticating_Type = Counter32
_SwAuthAuthTimeoutsWhileAuthenticating_Object = MibTableColumn
swAuthAuthTimeoutsWhileAuthenticating = _SwAuthAuthTimeoutsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 5),
    _SwAuthAuthTimeoutsWhileAuthenticating_Type()
)
swAuthAuthTimeoutsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthTimeoutsWhileAuthenticating.setStatus("current")
_SwAuthAuthFailWhileAuthenticating_Type = Counter32
_SwAuthAuthFailWhileAuthenticating_Object = MibTableColumn
swAuthAuthFailWhileAuthenticating = _SwAuthAuthFailWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 6),
    _SwAuthAuthFailWhileAuthenticating_Type()
)
swAuthAuthFailWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthFailWhileAuthenticating.setStatus("current")
_SwAuthAuthReauthsWhileAuthenticating_Type = Counter32
_SwAuthAuthReauthsWhileAuthenticating_Object = MibTableColumn
swAuthAuthReauthsWhileAuthenticating = _SwAuthAuthReauthsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 7),
    _SwAuthAuthReauthsWhileAuthenticating_Type()
)
swAuthAuthReauthsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthReauthsWhileAuthenticating.setStatus("current")
_SwAuthAuthEapStartsWhileAuthenticating_Type = Counter32
_SwAuthAuthEapStartsWhileAuthenticating_Object = MibTableColumn
swAuthAuthEapStartsWhileAuthenticating = _SwAuthAuthEapStartsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 8),
    _SwAuthAuthEapStartsWhileAuthenticating_Type()
)
swAuthAuthEapStartsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthEapStartsWhileAuthenticating.setStatus("current")
_SwAuthAuthEapLogoffWhileAuthenticating_Type = Counter32
_SwAuthAuthEapLogoffWhileAuthenticating_Object = MibTableColumn
swAuthAuthEapLogoffWhileAuthenticating = _SwAuthAuthEapLogoffWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 9),
    _SwAuthAuthEapLogoffWhileAuthenticating_Type()
)
swAuthAuthEapLogoffWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthEapLogoffWhileAuthenticating.setStatus("current")
_SwAuthAuthReauthsWhileAuthenticated_Type = Counter32
_SwAuthAuthReauthsWhileAuthenticated_Object = MibTableColumn
swAuthAuthReauthsWhileAuthenticated = _SwAuthAuthReauthsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 10),
    _SwAuthAuthReauthsWhileAuthenticated_Type()
)
swAuthAuthReauthsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthReauthsWhileAuthenticated.setStatus("current")
_SwAuthAuthEapStartsWhileAuthenticated_Type = Counter32
_SwAuthAuthEapStartsWhileAuthenticated_Object = MibTableColumn
swAuthAuthEapStartsWhileAuthenticated = _SwAuthAuthEapStartsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 11),
    _SwAuthAuthEapStartsWhileAuthenticated_Type()
)
swAuthAuthEapStartsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthEapStartsWhileAuthenticated.setStatus("current")
_SwAuthAuthEapLogoffWhileAuthenticated_Type = Counter32
_SwAuthAuthEapLogoffWhileAuthenticated_Object = MibTableColumn
swAuthAuthEapLogoffWhileAuthenticated = _SwAuthAuthEapLogoffWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 12),
    _SwAuthAuthEapLogoffWhileAuthenticated_Type()
)
swAuthAuthEapLogoffWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthEapLogoffWhileAuthenticated.setStatus("current")
_SwAuthBackendResponses_Type = Counter32
_SwAuthBackendResponses_Object = MibTableColumn
swAuthBackendResponses = _SwAuthBackendResponses_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 13),
    _SwAuthBackendResponses_Type()
)
swAuthBackendResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthBackendResponses.setStatus("current")
_SwAuthBackendAccessChallenges_Type = Counter32
_SwAuthBackendAccessChallenges_Object = MibTableColumn
swAuthBackendAccessChallenges = _SwAuthBackendAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 14),
    _SwAuthBackendAccessChallenges_Type()
)
swAuthBackendAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthBackendAccessChallenges.setStatus("current")
_SwAuthBackendOtherRequestsToSupplicant_Type = Counter32
_SwAuthBackendOtherRequestsToSupplicant_Object = MibTableColumn
swAuthBackendOtherRequestsToSupplicant = _SwAuthBackendOtherRequestsToSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 15),
    _SwAuthBackendOtherRequestsToSupplicant_Type()
)
swAuthBackendOtherRequestsToSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthBackendOtherRequestsToSupplicant.setStatus("current")
_SwAuthBackendNonNakResponsesFromSupplicant_Type = Counter32
_SwAuthBackendNonNakResponsesFromSupplicant_Object = MibTableColumn
swAuthBackendNonNakResponsesFromSupplicant = _SwAuthBackendNonNakResponsesFromSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 16),
    _SwAuthBackendNonNakResponsesFromSupplicant_Type()
)
swAuthBackendNonNakResponsesFromSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthBackendNonNakResponsesFromSupplicant.setStatus("current")
_SwAuthBackendAuthSuccesses_Type = Counter32
_SwAuthBackendAuthSuccesses_Object = MibTableColumn
swAuthBackendAuthSuccesses = _SwAuthBackendAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 17),
    _SwAuthBackendAuthSuccesses_Type()
)
swAuthBackendAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthBackendAuthSuccesses.setStatus("current")
_SwAuthBackendAuthFails_Type = Counter32
_SwAuthBackendAuthFails_Object = MibTableColumn
swAuthBackendAuthFails = _SwAuthBackendAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 3, 1, 18),
    _SwAuthBackendAuthFails_Type()
)
swAuthBackendAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthBackendAuthFails.setStatus("current")
_SwMacAuthSessionStatsTable_Object = MibTable
swMacAuthSessionStatsTable = _SwMacAuthSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4)
)
if mibBuilder.loadTexts:
    swMacAuthSessionStatsTable.setStatus("current")
_SwMacAuthSessionStatsEntry_Object = MibTableRow
swMacAuthSessionStatsEntry = _SwMacAuthSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1)
)
swMacAuthSessionStatsEntry.setIndexNames(
    (0, "AUTH-MIB", "swPaeMacAddr"),
    (0, "AUTH-MIB", "swPaePortNumber"),
)
if mibBuilder.loadTexts:
    swMacAuthSessionStatsEntry.setStatus("current")
_SwAuthSessionOctetsRx_Type = Counter64
_SwAuthSessionOctetsRx_Object = MibTableColumn
swAuthSessionOctetsRx = _SwAuthSessionOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 1),
    _SwAuthSessionOctetsRx_Type()
)
swAuthSessionOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthSessionOctetsRx.setStatus("current")
_SwAuthSessionOctetsTx_Type = Counter64
_SwAuthSessionOctetsTx_Object = MibTableColumn
swAuthSessionOctetsTx = _SwAuthSessionOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 2),
    _SwAuthSessionOctetsTx_Type()
)
swAuthSessionOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthSessionOctetsTx.setStatus("current")
_SwAuthSessionFramesRx_Type = Counter32
_SwAuthSessionFramesRx_Object = MibTableColumn
swAuthSessionFramesRx = _SwAuthSessionFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 3),
    _SwAuthSessionFramesRx_Type()
)
swAuthSessionFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthSessionFramesRx.setStatus("current")
_SwAuthSessionFramesTx_Type = Counter32
_SwAuthSessionFramesTx_Object = MibTableColumn
swAuthSessionFramesTx = _SwAuthSessionFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 4),
    _SwAuthSessionFramesTx_Type()
)
swAuthSessionFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthSessionFramesTx.setStatus("current")
_SwAuthSessionId_Type = SnmpAdminString
_SwAuthSessionId_Object = MibTableColumn
swAuthSessionId = _SwAuthSessionId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 5),
    _SwAuthSessionId_Type()
)
swAuthSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthSessionId.setStatus("current")


class _SwAuthSessionAuthenticMethod_Type(Integer32):
    """Custom type swAuthSessionAuthenticMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remoteAuthServer", 1),
          ("localAuthServer", 2))
    )


_SwAuthSessionAuthenticMethod_Type.__name__ = "Integer32"
_SwAuthSessionAuthenticMethod_Object = MibTableColumn
swAuthSessionAuthenticMethod = _SwAuthSessionAuthenticMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 6),
    _SwAuthSessionAuthenticMethod_Type()
)
swAuthSessionAuthenticMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthSessionAuthenticMethod.setStatus("current")
_SwAuthSessionTime_Type = TimeTicks
_SwAuthSessionTime_Object = MibTableColumn
swAuthSessionTime = _SwAuthSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 7),
    _SwAuthSessionTime_Type()
)
swAuthSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthSessionTime.setStatus("current")


class _SwAuthSessionTerminateCause_Type(Integer32):
    """Custom type swAuthSessionTerminateCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              999)
        )
    )
    namedValues = NamedValues(
        *(("supplicantLogoff", 1),
          ("portFailure", 2),
          ("supplicantRestart", 3),
          ("reauthFailed", 4),
          ("authControlForceUnauth", 5),
          ("portReInit", 6),
          ("portAdminDisabled", 7),
          ("notTerminatedYet", 999))
    )


_SwAuthSessionTerminateCause_Type.__name__ = "Integer32"
_SwAuthSessionTerminateCause_Object = MibTableColumn
swAuthSessionTerminateCause = _SwAuthSessionTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 8),
    _SwAuthSessionTerminateCause_Type()
)
swAuthSessionTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthSessionTerminateCause.setStatus("current")
_SwAuthSessionUserName_Type = SnmpAdminString
_SwAuthSessionUserName_Object = MibTableColumn
swAuthSessionUserName = _SwAuthSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 4, 1, 9),
    _SwAuthSessionUserName_Type()
)
swAuthSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthSessionUserName.setStatus("current")
_SwDot1xAuthStateTable_Object = MibTable
swDot1xAuthStateTable = _SwDot1xAuthStateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 5)
)
if mibBuilder.loadTexts:
    swDot1xAuthStateTable.setStatus("current")
_SwDot1xAuthStateEntry_Object = MibTableRow
swDot1xAuthStateEntry = _SwDot1xAuthStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 5, 1)
)
swDot1xAuthStateEntry.setIndexNames(
    (0, "AUTH-MIB", "swDot1xAuthPortNumber"),
    (0, "AUTH-MIB", "swDot1xAuthVID"),
    (0, "AUTH-MIB", "swDot1xAuthMACAddress"),
)
if mibBuilder.loadTexts:
    swDot1xAuthStateEntry.setStatus("current")
_SwDot1xAuthPortNumber_Type = InterfaceIndex
_SwDot1xAuthPortNumber_Object = MibTableColumn
swDot1xAuthPortNumber = _SwDot1xAuthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 5, 1, 1),
    _SwDot1xAuthPortNumber_Type()
)
swDot1xAuthPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDot1xAuthPortNumber.setStatus("current")
_SwDot1xAuthVID_Type = Integer32
_SwDot1xAuthVID_Object = MibTableColumn
swDot1xAuthVID = _SwDot1xAuthVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 5, 1, 2),
    _SwDot1xAuthVID_Type()
)
swDot1xAuthVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDot1xAuthVID.setStatus("current")
_SwDot1xAuthMACAddress_Type = MacAddress
_SwDot1xAuthMACAddress_Object = MibTableColumn
swDot1xAuthMACAddress = _SwDot1xAuthMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 5, 1, 3),
    _SwDot1xAuthMACAddress_Type()
)
swDot1xAuthMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDot1xAuthMACAddress.setStatus("current")


class _SwDot1xAuthenticatorPAEState_Type(Integer32):
    """Custom type swDot1xAuthenticatorPAEState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("initialize", 1),
          ("disconnected", 2),
          ("connecting", 3),
          ("authenticating", 4),
          ("authenticated", 5),
          ("aborting", 6),
          ("held", 7),
          ("forceAuth", 8),
          ("forceUnauth", 9))
    )


_SwDot1xAuthenticatorPAEState_Type.__name__ = "Integer32"
_SwDot1xAuthenticatorPAEState_Object = MibTableColumn
swDot1xAuthenticatorPAEState = _SwDot1xAuthenticatorPAEState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 5, 1, 4),
    _SwDot1xAuthenticatorPAEState_Type()
)
swDot1xAuthenticatorPAEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthenticatorPAEState.setStatus("current")


class _SwDot1xAuthBackendAuthState_Type(Integer32):
    """Custom type swDot1xAuthBackendAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("request", 1),
          ("response", 2),
          ("success", 3),
          ("fail", 4),
          ("timeout", 5),
          ("idle", 6),
          ("initialize", 7))
    )


_SwDot1xAuthBackendAuthState_Type.__name__ = "Integer32"
_SwDot1xAuthBackendAuthState_Object = MibTableColumn
swDot1xAuthBackendAuthState = _SwDot1xAuthBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 5, 1, 5),
    _SwDot1xAuthBackendAuthState_Type()
)
swDot1xAuthBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthBackendAuthState.setStatus("current")


class _SwDot1xAuthAuthControlledStatus_Type(Integer32):
    """Custom type swDot1xAuthAuthControlledStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authenticating", 1),
          ("authorized", 2),
          ("unauthorized", 3))
    )


_SwDot1xAuthAuthControlledStatus_Type.__name__ = "Integer32"
_SwDot1xAuthAuthControlledStatus_Object = MibTableColumn
swDot1xAuthAuthControlledStatus = _SwDot1xAuthAuthControlledStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 5, 1, 6),
    _SwDot1xAuthAuthControlledStatus_Type()
)
swDot1xAuthAuthControlledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthAuthControlledStatus.setStatus("current")
_SwDot1xAuthAssignVID_Type = Integer32
_SwDot1xAuthAssignVID_Object = MibTableColumn
swDot1xAuthAssignVID = _SwDot1xAuthAssignVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 5, 1, 7),
    _SwDot1xAuthAssignVID_Type()
)
swDot1xAuthAssignVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthAssignVID.setStatus("current")
_SwDot1xAuthAssignPriority_Type = Integer32
_SwDot1xAuthAssignPriority_Object = MibTableColumn
swDot1xAuthAssignPriority = _SwDot1xAuthAssignPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 5, 1, 8),
    _SwDot1xAuthAssignPriority_Type()
)
swDot1xAuthAssignPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthAssignPriority.setStatus("current")
_SwDot1xAuthStatsTable_Object = MibTable
swDot1xAuthStatsTable = _SwDot1xAuthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 6)
)
if mibBuilder.loadTexts:
    swDot1xAuthStatsTable.setStatus("current")
_SwDot1xAuthStatsEntry_Object = MibTableRow
swDot1xAuthStatsEntry = _SwDot1xAuthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 6, 1)
)
swDot1xAuthStatsEntry.setIndexNames(
    (0, "AUTH-MIB", "swDot1xAuthPortNumber"),
    (0, "AUTH-MIB", "swDot1xAuthVID"),
    (0, "AUTH-MIB", "swDot1xAuthMACAddress"),
)
if mibBuilder.loadTexts:
    swDot1xAuthStatsEntry.setStatus("current")
_SwDot1xAuthEapolFramesRx_Type = Counter32
_SwDot1xAuthEapolFramesRx_Object = MibTableColumn
swDot1xAuthEapolFramesRx = _SwDot1xAuthEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 6, 1, 1),
    _SwDot1xAuthEapolFramesRx_Type()
)
swDot1xAuthEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthEapolFramesRx.setStatus("current")
_SwDot1xAuthEapolFramesTx_Type = Counter32
_SwDot1xAuthEapolFramesTx_Object = MibTableColumn
swDot1xAuthEapolFramesTx = _SwDot1xAuthEapolFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 6, 1, 2),
    _SwDot1xAuthEapolFramesTx_Type()
)
swDot1xAuthEapolFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthEapolFramesTx.setStatus("current")
_SwDot1xAuthEapolStartFramesRx_Type = Counter32
_SwDot1xAuthEapolStartFramesRx_Object = MibTableColumn
swDot1xAuthEapolStartFramesRx = _SwDot1xAuthEapolStartFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 6, 1, 3),
    _SwDot1xAuthEapolStartFramesRx_Type()
)
swDot1xAuthEapolStartFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthEapolStartFramesRx.setStatus("current")
_SwDot1xAuthEapolLogoffFramesRx_Type = Counter32
_SwDot1xAuthEapolLogoffFramesRx_Object = MibTableColumn
swDot1xAuthEapolLogoffFramesRx = _SwDot1xAuthEapolLogoffFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 6, 1, 4),
    _SwDot1xAuthEapolLogoffFramesRx_Type()
)
swDot1xAuthEapolLogoffFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthEapolLogoffFramesRx.setStatus("current")
_SwDot1xAuthEapolRespIdFramesRx_Type = Counter32
_SwDot1xAuthEapolRespIdFramesRx_Object = MibTableColumn
swDot1xAuthEapolRespIdFramesRx = _SwDot1xAuthEapolRespIdFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 6, 1, 5),
    _SwDot1xAuthEapolRespIdFramesRx_Type()
)
swDot1xAuthEapolRespIdFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthEapolRespIdFramesRx.setStatus("current")
_SwDot1xAuthEapolRespFramesRx_Type = Counter32
_SwDot1xAuthEapolRespFramesRx_Object = MibTableColumn
swDot1xAuthEapolRespFramesRx = _SwDot1xAuthEapolRespFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 6, 1, 6),
    _SwDot1xAuthEapolRespFramesRx_Type()
)
swDot1xAuthEapolRespFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthEapolRespFramesRx.setStatus("current")
_SwDot1xAuthEapolReqIdFramesTx_Type = Counter32
_SwDot1xAuthEapolReqIdFramesTx_Object = MibTableColumn
swDot1xAuthEapolReqIdFramesTx = _SwDot1xAuthEapolReqIdFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 6, 1, 7),
    _SwDot1xAuthEapolReqIdFramesTx_Type()
)
swDot1xAuthEapolReqIdFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthEapolReqIdFramesTx.setStatus("current")
_SwDot1xAuthEapolReqFramesTx_Type = Counter32
_SwDot1xAuthEapolReqFramesTx_Object = MibTableColumn
swDot1xAuthEapolReqFramesTx = _SwDot1xAuthEapolReqFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 6, 1, 8),
    _SwDot1xAuthEapolReqFramesTx_Type()
)
swDot1xAuthEapolReqFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthEapolReqFramesTx.setStatus("current")
_SwDot1xAuthInvalidEapolFramesRx_Type = Counter32
_SwDot1xAuthInvalidEapolFramesRx_Object = MibTableColumn
swDot1xAuthInvalidEapolFramesRx = _SwDot1xAuthInvalidEapolFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 6, 1, 9),
    _SwDot1xAuthInvalidEapolFramesRx_Type()
)
swDot1xAuthInvalidEapolFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthInvalidEapolFramesRx.setStatus("current")
_SwDot1xAuthEapLengthErrorFramesRx_Type = Counter32
_SwDot1xAuthEapLengthErrorFramesRx_Object = MibTableColumn
swDot1xAuthEapLengthErrorFramesRx = _SwDot1xAuthEapLengthErrorFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 6, 1, 10),
    _SwDot1xAuthEapLengthErrorFramesRx_Type()
)
swDot1xAuthEapLengthErrorFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthEapLengthErrorFramesRx.setStatus("current")
_SwDot1xAuthLastEapolFrameVersion_Type = Unsigned32
_SwDot1xAuthLastEapolFrameVersion_Object = MibTableColumn
swDot1xAuthLastEapolFrameVersion = _SwDot1xAuthLastEapolFrameVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 6, 1, 11),
    _SwDot1xAuthLastEapolFrameVersion_Type()
)
swDot1xAuthLastEapolFrameVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthLastEapolFrameVersion.setStatus("current")
_SwDot1xAuthLastEapolFrameSource_Type = MacAddress
_SwDot1xAuthLastEapolFrameSource_Object = MibTableColumn
swDot1xAuthLastEapolFrameSource = _SwDot1xAuthLastEapolFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 6, 1, 12),
    _SwDot1xAuthLastEapolFrameSource_Type()
)
swDot1xAuthLastEapolFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthLastEapolFrameSource.setStatus("current")
_SwDot1xAuthDiagTable_Object = MibTable
swDot1xAuthDiagTable = _SwDot1xAuthDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7)
)
if mibBuilder.loadTexts:
    swDot1xAuthDiagTable.setStatus("current")
_SwDot1xAuthDiagEntry_Object = MibTableRow
swDot1xAuthDiagEntry = _SwDot1xAuthDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1)
)
swDot1xAuthDiagEntry.setIndexNames(
    (0, "AUTH-MIB", "swDot1xAuthPortNumber"),
    (0, "AUTH-MIB", "swDot1xAuthVID"),
    (0, "AUTH-MIB", "swDot1xAuthMACAddress"),
)
if mibBuilder.loadTexts:
    swDot1xAuthDiagEntry.setStatus("current")
_SwDot1xAuthEntersConnecting_Type = Counter32
_SwDot1xAuthEntersConnecting_Object = MibTableColumn
swDot1xAuthEntersConnecting = _SwDot1xAuthEntersConnecting_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1, 1),
    _SwDot1xAuthEntersConnecting_Type()
)
swDot1xAuthEntersConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthEntersConnecting.setStatus("current")
_SwDot1xAuthEapLogoffsWhileConnecting_Type = Counter32
_SwDot1xAuthEapLogoffsWhileConnecting_Object = MibTableColumn
swDot1xAuthEapLogoffsWhileConnecting = _SwDot1xAuthEapLogoffsWhileConnecting_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1, 2),
    _SwDot1xAuthEapLogoffsWhileConnecting_Type()
)
swDot1xAuthEapLogoffsWhileConnecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthEapLogoffsWhileConnecting.setStatus("current")
_SwDot1xAuthEntersAuthenticating_Type = Counter32
_SwDot1xAuthEntersAuthenticating_Object = MibTableColumn
swDot1xAuthEntersAuthenticating = _SwDot1xAuthEntersAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1, 3),
    _SwDot1xAuthEntersAuthenticating_Type()
)
swDot1xAuthEntersAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthEntersAuthenticating.setStatus("current")
_SwDot1xAuthAuthSuccessWhileAuthenticating_Type = Counter32
_SwDot1xAuthAuthSuccessWhileAuthenticating_Object = MibTableColumn
swDot1xAuthAuthSuccessWhileAuthenticating = _SwDot1xAuthAuthSuccessWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1, 4),
    _SwDot1xAuthAuthSuccessWhileAuthenticating_Type()
)
swDot1xAuthAuthSuccessWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthAuthSuccessWhileAuthenticating.setStatus("current")
_SwDot1xAuthAuthTimeoutsWhileAuthenticating_Type = Counter32
_SwDot1xAuthAuthTimeoutsWhileAuthenticating_Object = MibTableColumn
swDot1xAuthAuthTimeoutsWhileAuthenticating = _SwDot1xAuthAuthTimeoutsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1, 5),
    _SwDot1xAuthAuthTimeoutsWhileAuthenticating_Type()
)
swDot1xAuthAuthTimeoutsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthAuthTimeoutsWhileAuthenticating.setStatus("current")
_SwDot1xAuthAuthFailWhileAuthenticating_Type = Counter32
_SwDot1xAuthAuthFailWhileAuthenticating_Object = MibTableColumn
swDot1xAuthAuthFailWhileAuthenticating = _SwDot1xAuthAuthFailWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1, 6),
    _SwDot1xAuthAuthFailWhileAuthenticating_Type()
)
swDot1xAuthAuthFailWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthAuthFailWhileAuthenticating.setStatus("current")
_SwDot1xAuthAuthReauthsWhileAuthenticating_Type = Counter32
_SwDot1xAuthAuthReauthsWhileAuthenticating_Object = MibTableColumn
swDot1xAuthAuthReauthsWhileAuthenticating = _SwDot1xAuthAuthReauthsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1, 7),
    _SwDot1xAuthAuthReauthsWhileAuthenticating_Type()
)
swDot1xAuthAuthReauthsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthAuthReauthsWhileAuthenticating.setStatus("current")
_SwDot1xAuthAuthEapStartsWhileAuthenticating_Type = Counter32
_SwDot1xAuthAuthEapStartsWhileAuthenticating_Object = MibTableColumn
swDot1xAuthAuthEapStartsWhileAuthenticating = _SwDot1xAuthAuthEapStartsWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1, 8),
    _SwDot1xAuthAuthEapStartsWhileAuthenticating_Type()
)
swDot1xAuthAuthEapStartsWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthAuthEapStartsWhileAuthenticating.setStatus("current")
_SwDot1xAuthAuthEapLogoffWhileAuthenticating_Type = Counter32
_SwDot1xAuthAuthEapLogoffWhileAuthenticating_Object = MibTableColumn
swDot1xAuthAuthEapLogoffWhileAuthenticating = _SwDot1xAuthAuthEapLogoffWhileAuthenticating_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1, 9),
    _SwDot1xAuthAuthEapLogoffWhileAuthenticating_Type()
)
swDot1xAuthAuthEapLogoffWhileAuthenticating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthAuthEapLogoffWhileAuthenticating.setStatus("current")
_SwDot1xAuthAuthReauthsWhileAuthenticated_Type = Counter32
_SwDot1xAuthAuthReauthsWhileAuthenticated_Object = MibTableColumn
swDot1xAuthAuthReauthsWhileAuthenticated = _SwDot1xAuthAuthReauthsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1, 10),
    _SwDot1xAuthAuthReauthsWhileAuthenticated_Type()
)
swDot1xAuthAuthReauthsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthAuthReauthsWhileAuthenticated.setStatus("current")
_SwDot1xAuthAuthEapStartsWhileAuthenticated_Type = Counter32
_SwDot1xAuthAuthEapStartsWhileAuthenticated_Object = MibTableColumn
swDot1xAuthAuthEapStartsWhileAuthenticated = _SwDot1xAuthAuthEapStartsWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1, 11),
    _SwDot1xAuthAuthEapStartsWhileAuthenticated_Type()
)
swDot1xAuthAuthEapStartsWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthAuthEapStartsWhileAuthenticated.setStatus("current")
_SwDot1xAuthAuthEapLogoffWhileAuthenticated_Type = Counter32
_SwDot1xAuthAuthEapLogoffWhileAuthenticated_Object = MibTableColumn
swDot1xAuthAuthEapLogoffWhileAuthenticated = _SwDot1xAuthAuthEapLogoffWhileAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1, 12),
    _SwDot1xAuthAuthEapLogoffWhileAuthenticated_Type()
)
swDot1xAuthAuthEapLogoffWhileAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthAuthEapLogoffWhileAuthenticated.setStatus("current")
_SwDot1xAuthBackendResponses_Type = Counter32
_SwDot1xAuthBackendResponses_Object = MibTableColumn
swDot1xAuthBackendResponses = _SwDot1xAuthBackendResponses_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1, 13),
    _SwDot1xAuthBackendResponses_Type()
)
swDot1xAuthBackendResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthBackendResponses.setStatus("current")
_SwDot1xAuthBackendAccessChallenges_Type = Counter32
_SwDot1xAuthBackendAccessChallenges_Object = MibTableColumn
swDot1xAuthBackendAccessChallenges = _SwDot1xAuthBackendAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1, 14),
    _SwDot1xAuthBackendAccessChallenges_Type()
)
swDot1xAuthBackendAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthBackendAccessChallenges.setStatus("current")
_SwDot1xAuthBackendOtherRequestsToSupplicant_Type = Counter32
_SwDot1xAuthBackendOtherRequestsToSupplicant_Object = MibTableColumn
swDot1xAuthBackendOtherRequestsToSupplicant = _SwDot1xAuthBackendOtherRequestsToSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1, 15),
    _SwDot1xAuthBackendOtherRequestsToSupplicant_Type()
)
swDot1xAuthBackendOtherRequestsToSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthBackendOtherRequestsToSupplicant.setStatus("current")
_SwDot1xAuthBackendNonNakResponsesFromSupplicant_Type = Counter32
_SwDot1xAuthBackendNonNakResponsesFromSupplicant_Object = MibTableColumn
swDot1xAuthBackendNonNakResponsesFromSupplicant = _SwDot1xAuthBackendNonNakResponsesFromSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1, 16),
    _SwDot1xAuthBackendNonNakResponsesFromSupplicant_Type()
)
swDot1xAuthBackendNonNakResponsesFromSupplicant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthBackendNonNakResponsesFromSupplicant.setStatus("current")
_SwDot1xAuthBackendAuthSuccesses_Type = Counter32
_SwDot1xAuthBackendAuthSuccesses_Object = MibTableColumn
swDot1xAuthBackendAuthSuccesses = _SwDot1xAuthBackendAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1, 17),
    _SwDot1xAuthBackendAuthSuccesses_Type()
)
swDot1xAuthBackendAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthBackendAuthSuccesses.setStatus("current")
_SwDot1xAuthBackendAuthFails_Type = Counter32
_SwDot1xAuthBackendAuthFails_Object = MibTableColumn
swDot1xAuthBackendAuthFails = _SwDot1xAuthBackendAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 7, 1, 18),
    _SwDot1xAuthBackendAuthFails_Type()
)
swDot1xAuthBackendAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthBackendAuthFails.setStatus("current")
_SwDot1xAuthSessionStatsTable_Object = MibTable
swDot1xAuthSessionStatsTable = _SwDot1xAuthSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 8)
)
if mibBuilder.loadTexts:
    swDot1xAuthSessionStatsTable.setStatus("current")
_SwDot1xAuthSessionStatsEntry_Object = MibTableRow
swDot1xAuthSessionStatsEntry = _SwDot1xAuthSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 8, 1)
)
swDot1xAuthSessionStatsEntry.setIndexNames(
    (0, "AUTH-MIB", "swDot1xAuthPortNumber"),
    (0, "AUTH-MIB", "swDot1xAuthVID"),
    (0, "AUTH-MIB", "swDot1xAuthMACAddress"),
)
if mibBuilder.loadTexts:
    swDot1xAuthSessionStatsEntry.setStatus("current")
_SwDot1xAuthSessionOctetsRx_Type = Counter64
_SwDot1xAuthSessionOctetsRx_Object = MibTableColumn
swDot1xAuthSessionOctetsRx = _SwDot1xAuthSessionOctetsRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 8, 1, 1),
    _SwDot1xAuthSessionOctetsRx_Type()
)
swDot1xAuthSessionOctetsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthSessionOctetsRx.setStatus("current")
_SwDot1xAuthSessionOctetsTx_Type = Counter64
_SwDot1xAuthSessionOctetsTx_Object = MibTableColumn
swDot1xAuthSessionOctetsTx = _SwDot1xAuthSessionOctetsTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 8, 1, 2),
    _SwDot1xAuthSessionOctetsTx_Type()
)
swDot1xAuthSessionOctetsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthSessionOctetsTx.setStatus("current")
_SwDot1xAuthSessionFramesRx_Type = Counter32
_SwDot1xAuthSessionFramesRx_Object = MibTableColumn
swDot1xAuthSessionFramesRx = _SwDot1xAuthSessionFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 8, 1, 3),
    _SwDot1xAuthSessionFramesRx_Type()
)
swDot1xAuthSessionFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthSessionFramesRx.setStatus("current")
_SwDot1xAuthSessionFramesTx_Type = Counter32
_SwDot1xAuthSessionFramesTx_Object = MibTableColumn
swDot1xAuthSessionFramesTx = _SwDot1xAuthSessionFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 8, 1, 4),
    _SwDot1xAuthSessionFramesTx_Type()
)
swDot1xAuthSessionFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthSessionFramesTx.setStatus("current")
_SwDot1xAuthSessionId_Type = SnmpAdminString
_SwDot1xAuthSessionId_Object = MibTableColumn
swDot1xAuthSessionId = _SwDot1xAuthSessionId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 8, 1, 5),
    _SwDot1xAuthSessionId_Type()
)
swDot1xAuthSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthSessionId.setStatus("current")


class _SwDot1xAuthSessionAuthenticMethod_Type(Integer32):
    """Custom type swDot1xAuthSessionAuthenticMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remoteAuthServer", 1),
          ("localAuthServer", 2))
    )


_SwDot1xAuthSessionAuthenticMethod_Type.__name__ = "Integer32"
_SwDot1xAuthSessionAuthenticMethod_Object = MibTableColumn
swDot1xAuthSessionAuthenticMethod = _SwDot1xAuthSessionAuthenticMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 8, 1, 6),
    _SwDot1xAuthSessionAuthenticMethod_Type()
)
swDot1xAuthSessionAuthenticMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthSessionAuthenticMethod.setStatus("current")
_SwDot1xAuthSessionTime_Type = TimeTicks
_SwDot1xAuthSessionTime_Object = MibTableColumn
swDot1xAuthSessionTime = _SwDot1xAuthSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 8, 1, 7),
    _SwDot1xAuthSessionTime_Type()
)
swDot1xAuthSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthSessionTime.setStatus("current")


class _SwDot1xAuthSessionTerminateCause_Type(Integer32):
    """Custom type swDot1xAuthSessionTerminateCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              999)
        )
    )
    namedValues = NamedValues(
        *(("supplicantLogoff", 1),
          ("portFailure", 2),
          ("supplicantRestart", 3),
          ("reauthFailed", 4),
          ("authControlForceUnauth", 5),
          ("portReInit", 6),
          ("portAdminDisabled", 7),
          ("notTerminatedYet", 999))
    )


_SwDot1xAuthSessionTerminateCause_Type.__name__ = "Integer32"
_SwDot1xAuthSessionTerminateCause_Object = MibTableColumn
swDot1xAuthSessionTerminateCause = _SwDot1xAuthSessionTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 8, 1, 8),
    _SwDot1xAuthSessionTerminateCause_Type()
)
swDot1xAuthSessionTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthSessionTerminateCause.setStatus("current")
_SwDot1xAuthSessionUserName_Type = SnmpAdminString
_SwDot1xAuthSessionUserName_Object = MibTableColumn
swDot1xAuthSessionUserName = _SwDot1xAuthSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 6, 8, 1, 9),
    _SwDot1xAuthSessionUserName_Type()
)
swDot1xAuthSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDot1xAuthSessionUserName.setStatus("current")
_SwRadiusCommand_ObjectIdentity = ObjectIdentity
swRadiusCommand = _SwRadiusCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 7)
)
_SwRadiusForceDownPortNumber_Type = Unsigned32
_SwRadiusForceDownPortNumber_Object = MibScalar
swRadiusForceDownPortNumber = _SwRadiusForceDownPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 7, 1),
    _SwRadiusForceDownPortNumber_Type()
)
swRadiusForceDownPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusForceDownPortNumber.setStatus("current")
_SwRadiusForceDownMacAddr_Type = MacAddress
_SwRadiusForceDownMacAddr_Object = MibScalar
swRadiusForceDownMacAddr = _SwRadiusForceDownMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 7, 2),
    _SwRadiusForceDownMacAddr_Type()
)
swRadiusForceDownMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRadiusForceDownMacAddr.setStatus("current")
_SwAuthenticatedPortInfo_ObjectIdentity = ObjectIdentity
swAuthenticatedPortInfo = _SwAuthenticatedPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 8)
)
_SwAuthenticatedPortCtrlTable_Object = MibTable
swAuthenticatedPortCtrlTable = _SwAuthenticatedPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 8, 1)
)
if mibBuilder.loadTexts:
    swAuthenticatedPortCtrlTable.setStatus("current")
_SwAuthenticatedPortCtrlEntry_Object = MibTableRow
swAuthenticatedPortCtrlEntry = _SwAuthenticatedPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 8, 1, 1)
)
swAuthenticatedPortCtrlEntry.setIndexNames(
    (0, "AUTH-MIB", "swAuthenticatedPortNumber"),
)
if mibBuilder.loadTexts:
    swAuthenticatedPortCtrlEntry.setStatus("current")
_SwAuthenticatedPortNumber_Type = Integer32
_SwAuthenticatedPortNumber_Object = MibTableColumn
swAuthenticatedPortNumber = _SwAuthenticatedPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 8, 1, 1, 1),
    _SwAuthenticatedPortNumber_Type()
)
swAuthenticatedPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swAuthenticatedPortNumber.setStatus("current")


class _SwAuthenticatedPortCapabilities_Type(Integer32):
    """Custom type swAuthenticatedPortCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("authenticator", 2))
    )


_SwAuthenticatedPortCapabilities_Type.__name__ = "Integer32"
_SwAuthenticatedPortCapabilities_Object = MibTableColumn
swAuthenticatedPortCapabilities = _SwAuthenticatedPortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 8, 1, 1, 2),
    _SwAuthenticatedPortCapabilities_Type()
)
swAuthenticatedPortCapabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthenticatedPortCapabilities.setStatus("current")
_SwMacBasedPaePortInfo_ObjectIdentity = ObjectIdentity
swMacBasedPaePortInfo = _SwMacBasedPaePortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 9)
)
_SwMacBasedPaePortTable_Object = MibTable
swMacBasedPaePortTable = _SwMacBasedPaePortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 9, 1)
)
if mibBuilder.loadTexts:
    swMacBasedPaePortTable.setStatus("current")
_SwMacBasedPaePortEntry_Object = MibTableRow
swMacBasedPaePortEntry = _SwMacBasedPaePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 9, 1, 1)
)
swMacBasedPaePortEntry.setIndexNames(
    (0, "AUTH-MIB", "swMacBasedPaePortNumber"),
)
if mibBuilder.loadTexts:
    swMacBasedPaePortEntry.setStatus("current")
_SwMacBasedPaePortNumber_Type = InterfaceIndex
_SwMacBasedPaePortNumber_Object = MibTableColumn
swMacBasedPaePortNumber = _SwMacBasedPaePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 9, 1, 1, 1),
    _SwMacBasedPaePortNumber_Type()
)
swMacBasedPaePortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swMacBasedPaePortNumber.setStatus("current")
_SwMacBasedPaeMacAddress_Type = MacAddress
_SwMacBasedPaeMacAddress_Object = MibTableColumn
swMacBasedPaeMacAddress = _SwMacBasedPaeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 9, 1, 1, 2),
    _SwMacBasedPaeMacAddress_Type()
)
swMacBasedPaeMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedPaeMacAddress.setStatus("current")


class _SwMacBasedPaePortInitializeOrReauthStatus_Type(Integer32):
    """Custom type swMacBasedPaePortInitializeOrReauthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("initialize", 2),
          ("reauthenticate", 3))
    )


_SwMacBasedPaePortInitializeOrReauthStatus_Type.__name__ = "Integer32"
_SwMacBasedPaePortInitializeOrReauthStatus_Object = MibTableColumn
swMacBasedPaePortInitializeOrReauthStatus = _SwMacBasedPaePortInitializeOrReauthStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 9, 1, 1, 3),
    _SwMacBasedPaePortInitializeOrReauthStatus_Type()
)
swMacBasedPaePortInitializeOrReauthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedPaePortInitializeOrReauthStatus.setStatus("current")
_SwMacBasedPaeTable_Object = MibTable
swMacBasedPaeTable = _SwMacBasedPaeTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 9, 2)
)
if mibBuilder.loadTexts:
    swMacBasedPaeTable.setStatus("current")
_SwMacBasedPaeEntry_Object = MibTableRow
swMacBasedPaeEntry = _SwMacBasedPaeEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 9, 2, 1)
)
swMacBasedPaeEntry.setIndexNames(
    (0, "AUTH-MIB", "swMacBasedPaePort"),
    (0, "AUTH-MIB", "swMacBasedPaeMac"),
)
if mibBuilder.loadTexts:
    swMacBasedPaeEntry.setStatus("current")
_SwMacBasedPaePort_Type = InterfaceIndex
_SwMacBasedPaePort_Object = MibTableColumn
swMacBasedPaePort = _SwMacBasedPaePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 9, 2, 1, 1),
    _SwMacBasedPaePort_Type()
)
swMacBasedPaePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swMacBasedPaePort.setStatus("current")
_SwMacBasedPaeMac_Type = MacAddress
_SwMacBasedPaeMac_Object = MibTableColumn
swMacBasedPaeMac = _SwMacBasedPaeMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 9, 2, 1, 2),
    _SwMacBasedPaeMac_Type()
)
swMacBasedPaeMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swMacBasedPaeMac.setStatus("current")


class _SwMacBasedPaeInitOrReauthStatus_Type(Integer32):
    """Custom type swMacBasedPaeInitOrReauthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("initialize", 2),
          ("reauthenticate", 3))
    )


_SwMacBasedPaeInitOrReauthStatus_Type.__name__ = "Integer32"
_SwMacBasedPaeInitOrReauthStatus_Object = MibTableColumn
swMacBasedPaeInitOrReauthStatus = _SwMacBasedPaeInitOrReauthStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 9, 2, 1, 3),
    _SwMacBasedPaeInitOrReauthStatus_Type()
)
swMacBasedPaeInitOrReauthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedPaeInitOrReauthStatus.setStatus("current")
_SwPaeAuthenticator_ObjectIdentity = ObjectIdentity
swPaeAuthenticator = _SwPaeAuthenticator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 10)
)


class _SwPaeAuthSysFwdPdu_Type(Integer32):
    """Custom type swPaeAuthSysFwdPdu based on Integer32"""
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


_SwPaeAuthSysFwdPdu_Type.__name__ = "Integer32"
_SwPaeAuthSysFwdPdu_Object = MibScalar
swPaeAuthSysFwdPdu = _SwPaeAuthSysFwdPdu_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 10, 1),
    _SwPaeAuthSysFwdPdu_Type()
)
swPaeAuthSysFwdPdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPaeAuthSysFwdPdu.setStatus("current")
_SwPaeAuthSysMaxUser_Type = Integer32
_SwPaeAuthSysMaxUser_Object = MibScalar
swPaeAuthSysMaxUser = _SwPaeAuthSysMaxUser_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 10, 2),
    _SwPaeAuthSysMaxUser_Type()
)
swPaeAuthSysMaxUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPaeAuthSysMaxUser.setStatus("current")
_SwPaeAuthConfigTable_Object = MibTable
swPaeAuthConfigTable = _SwPaeAuthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 10, 3)
)
if mibBuilder.loadTexts:
    swPaeAuthConfigTable.setStatus("current")
_SwPaeAuthConfigEntry_Object = MibTableRow
swPaeAuthConfigEntry = _SwPaeAuthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 10, 3, 1)
)
swPaeAuthConfigEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    swPaeAuthConfigEntry.setStatus("current")


class _SwPaeAuthFwdPdu_Type(Integer32):
    """Custom type swPaeAuthFwdPdu based on Integer32"""
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


_SwPaeAuthFwdPdu_Type.__name__ = "Integer32"
_SwPaeAuthFwdPdu_Object = MibTableColumn
swPaeAuthFwdPdu = _SwPaeAuthFwdPdu_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 10, 3, 1, 1),
    _SwPaeAuthFwdPdu_Type()
)
swPaeAuthFwdPdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPaeAuthFwdPdu.setStatus("current")
_SwPaeAuthMaxUser_Type = Integer32
_SwPaeAuthMaxUser_Object = MibTableColumn
swPaeAuthMaxUser = _SwPaeAuthMaxUser_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 10, 3, 1, 2),
    _SwPaeAuthMaxUser_Type()
)
swPaeAuthMaxUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPaeAuthMaxUser.setStatus("current")
_SwAuthStateTable_Object = MibTable
swAuthStateTable = _SwAuthStateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 10, 4)
)
if mibBuilder.loadTexts:
    swAuthStateTable.setStatus("current")
_SwAuthStateEntry_Object = MibTableRow
swAuthStateEntry = _SwAuthStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 10, 4, 1)
)
swAuthStateEntry.setIndexNames(
    (0, "AUTH-MIB", "swAuthPortNumber"),
    (0, "AUTH-MIB", "swAuthMacAddress"),
)
if mibBuilder.loadTexts:
    swAuthStateEntry.setStatus("current")
_SwAuthPortNumber_Type = InterfaceIndex
_SwAuthPortNumber_Object = MibTableColumn
swAuthPortNumber = _SwAuthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 10, 4, 1, 1),
    _SwAuthPortNumber_Type()
)
swAuthPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swAuthPortNumber.setStatus("current")
_SwAuthMacAddress_Type = MacAddress
_SwAuthMacAddress_Object = MibTableColumn
swAuthMacAddress = _SwAuthMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 10, 4, 1, 2),
    _SwAuthMacAddress_Type()
)
swAuthMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swAuthMacAddress.setStatus("current")


class _SwAuthAuthControlledStatus_Type(Integer32):
    """Custom type swAuthAuthControlledStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authenticating", 1),
          ("authorized", 2),
          ("unauthorized", 3))
    )


_SwAuthAuthControlledStatus_Type.__name__ = "Integer32"
_SwAuthAuthControlledStatus_Object = MibTableColumn
swAuthAuthControlledStatus = _SwAuthAuthControlledStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 10, 4, 1, 3),
    _SwAuthAuthControlledStatus_Type()
)
swAuthAuthControlledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAuthControlledStatus.setStatus("current")
_SwAuthAssignVid_Type = Integer32
_SwAuthAssignVid_Object = MibTableColumn
swAuthAssignVid = _SwAuthAssignVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 10, 4, 1, 4),
    _SwAuthAssignVid_Type()
)
swAuthAssignVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAssignVid.setStatus("current")
_SwAuthAssignPriority_Type = Integer32
_SwAuthAssignPriority_Object = MibTableColumn
swAuthAssignPriority = _SwAuthAssignPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 10, 4, 1, 5),
    _SwAuthAssignPriority_Type()
)
swAuthAssignPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthAssignPriority.setStatus("current")


class _SwAuthenticatorPAEState_Type(Integer32):
    """Custom type swAuthenticatorPAEState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("initialize", 1),
          ("disconnected", 2),
          ("connecting", 3),
          ("authenticating", 4),
          ("authenticated", 5),
          ("aborting", 6),
          ("held", 7),
          ("forceAuth", 8),
          ("forceUnauth", 9))
    )


_SwAuthenticatorPAEState_Type.__name__ = "Integer32"
_SwAuthenticatorPAEState_Object = MibTableColumn
swAuthenticatorPAEState = _SwAuthenticatorPAEState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 10, 4, 1, 6),
    _SwAuthenticatorPAEState_Type()
)
swAuthenticatorPAEState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthenticatorPAEState.setStatus("current")


class _SwAuthBKdAuthState_Type(Integer32):
    """Custom type swAuthBKdAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("request", 1),
          ("response", 2),
          ("success", 3),
          ("fail", 4),
          ("timeout", 5),
          ("idle", 6),
          ("initialize", 7))
    )


_SwAuthBKdAuthState_Type.__name__ = "Integer32"
_SwAuthBKdAuthState_Object = MibTableColumn
swAuthBKdAuthState = _SwAuthBKdAuthState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 10, 4, 1, 7),
    _SwAuthBKdAuthState_Type()
)
swAuthBKdAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swAuthBKdAuthState.setStatus("current")
_SwCompoundAuthMgmt_ObjectIdentity = ObjectIdentity
swCompoundAuthMgmt = _SwCompoundAuthMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 11)
)
_SwCompoundAuthPortTable_Object = MibTable
swCompoundAuthPortTable = _SwCompoundAuthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 11, 1)
)
if mibBuilder.loadTexts:
    swCompoundAuthPortTable.setStatus("current")
_SwCompoundAuthPortEntry_Object = MibTableRow
swCompoundAuthPortEntry = _SwCompoundAuthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 11, 1, 1)
)
swCompoundAuthPortEntry.setIndexNames(
    (0, "AUTH-MIB", "swCompoundAuthPortIndex"),
)
if mibBuilder.loadTexts:
    swCompoundAuthPortEntry.setStatus("current")


class _SwCompoundAuthPortIndex_Type(Integer32):
    """Custom type swCompoundAuthPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwCompoundAuthPortIndex_Type.__name__ = "Integer32"
_SwCompoundAuthPortIndex_Object = MibTableColumn
swCompoundAuthPortIndex = _SwCompoundAuthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 11, 1, 1, 1),
    _SwCompoundAuthPortIndex_Type()
)
swCompoundAuthPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCompoundAuthPortIndex.setStatus("current")


class _SwCompoundAuthPortAuthMode_Type(Integer32):
    """Custom type swCompoundAuthPortAuthMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hostbased", 1),
          ("portbased", 2))
    )


_SwCompoundAuthPortAuthMode_Type.__name__ = "Integer32"
_SwCompoundAuthPortAuthMode_Object = MibTableColumn
swCompoundAuthPortAuthMode = _SwCompoundAuthPortAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 11, 1, 1, 2),
    _SwCompoundAuthPortAuthMode_Type()
)
swCompoundAuthPortAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCompoundAuthPortAuthMode.setStatus("current")


class _SwCompoundAuthPortMethod_Type(Integer32):
    """Custom type swCompoundAuthPortMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("any", 2),
          ("dot1xImpb", 3),
          ("impbJwac", 4),
          ("impbWac", 5),
          ("macImpb", 6),
          ("macJwac", 7))
    )


_SwCompoundAuthPortMethod_Type.__name__ = "Integer32"
_SwCompoundAuthPortMethod_Object = MibTableColumn
swCompoundAuthPortMethod = _SwCompoundAuthPortMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 11, 1, 1, 3),
    _SwCompoundAuthPortMethod_Type()
)
swCompoundAuthPortMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCompoundAuthPortMethod.setStatus("current")
_SwCompoundAuthPortAuthVLANs_Type = DisplayString
_SwCompoundAuthPortAuthVLANs_Object = MibTableColumn
swCompoundAuthPortAuthVLANs = _SwCompoundAuthPortAuthVLANs_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 11, 1, 1, 4),
    _SwCompoundAuthPortAuthVLANs_Type()
)
swCompoundAuthPortAuthVLANs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCompoundAuthPortAuthVLANs.setStatus("current")
_SwGuestVlanTable_Object = MibTable
swGuestVlanTable = _SwGuestVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 11, 2)
)
if mibBuilder.loadTexts:
    swGuestVlanTable.setStatus("current")
_SwGuestVlanEntry_Object = MibTableRow
swGuestVlanEntry = _SwGuestVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 11, 2, 1)
)
swGuestVlanEntry.setIndexNames(
    (0, "AUTH-MIB", "swGuestVlanId"),
)
if mibBuilder.loadTexts:
    swGuestVlanEntry.setStatus("current")
_SwGuestVlanId_Type = VlanId
_SwGuestVlanId_Object = MibTableColumn
swGuestVlanId = _SwGuestVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 11, 2, 1, 1),
    _SwGuestVlanId_Type()
)
swGuestVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swGuestVlanId.setStatus("current")
_SwGuestVlanPorts_Type = PortList
_SwGuestVlanPorts_Object = MibTableColumn
swGuestVlanPorts = _SwGuestVlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 11, 2, 1, 2),
    _SwGuestVlanPorts_Type()
)
swGuestVlanPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swGuestVlanPorts.setStatus("current")
_SwGuestVlanRowStatus_Type = RowStatus
_SwGuestVlanRowStatus_Object = MibTableColumn
swGuestVlanRowStatus = _SwGuestVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 11, 2, 1, 3),
    _SwGuestVlanRowStatus_Type()
)
swGuestVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swGuestVlanRowStatus.setStatus("current")


class _SwAuthorizationAttributes_Type(Integer32):
    """Custom type swAuthorizationAttributes based on Integer32"""
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


_SwAuthorizationAttributes_Type.__name__ = "Integer32"
_SwAuthorizationAttributes_Object = MibScalar
swAuthorizationAttributes = _SwAuthorizationAttributes_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 11, 3),
    _SwAuthorizationAttributes_Type()
)
swAuthorizationAttributes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthorizationAttributes.setStatus("current")


class _SwAuthServerFailoverState_Type(Integer32):
    """Custom type swAuthServerFailoverState based on Integer32"""
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
        *(("block", 1),
          ("local", 2),
          ("permit", 3))
    )


_SwAuthServerFailoverState_Type.__name__ = "Integer32"
_SwAuthServerFailoverState_Object = MibScalar
swAuthServerFailoverState = _SwAuthServerFailoverState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 11, 4),
    _SwAuthServerFailoverState_Type()
)
swAuthServerFailoverState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthServerFailoverState.setStatus("current")


class _SwAuthMACFormatCase_Type(Integer32):
    """Custom type swAuthMACFormatCase based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uppercase", 1),
          ("lowercase", 2))
    )


_SwAuthMACFormatCase_Type.__name__ = "Integer32"
_SwAuthMACFormatCase_Object = MibScalar
swAuthMACFormatCase = _SwAuthMACFormatCase_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 11, 5),
    _SwAuthMACFormatCase_Type()
)
swAuthMACFormatCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthMACFormatCase.setStatus("current")


class _SwAuthMACFormatDelimiter_Type(Integer32):
    """Custom type swAuthMACFormatDelimiter based on Integer32"""
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
        *(("none", 1),
          ("hyphen", 2),
          ("colon", 3),
          ("dot", 4))
    )


_SwAuthMACFormatDelimiter_Type.__name__ = "Integer32"
_SwAuthMACFormatDelimiter_Object = MibScalar
swAuthMACFormatDelimiter = _SwAuthMACFormatDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 11, 6),
    _SwAuthMACFormatDelimiter_Type()
)
swAuthMACFormatDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthMACFormatDelimiter.setStatus("current")


class _SwAuthMACFormatDelimiterNumber_Type(Integer32):
    """Custom type swAuthMACFormatDelimiterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delimiter-number-1", 1),
          ("delimiter-number-2", 2),
          ("delimiter-number-5", 3))
    )


_SwAuthMACFormatDelimiterNumber_Type.__name__ = "Integer32"
_SwAuthMACFormatDelimiterNumber_Object = MibScalar
swAuthMACFormatDelimiterNumber = _SwAuthMACFormatDelimiterNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 3, 11, 7),
    _SwAuthMACFormatDelimiterNumber_Type()
)
swAuthMACFormatDelimiterNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAuthMACFormatDelimiterNumber.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AUTH-MIB",
    **{"PortList": PortList,
       "VlanId": VlanId,
       "swAuthCtrl": swAuthCtrl,
       "swAuthenCtrl": swAuthenCtrl,
       "authProtocol": authProtocol,
       "swAuthMode": swAuthMode,
       "swAuthorizationState": swAuthorizationState,
       "swAuthFailOver": swAuthFailOver,
       "swRadiusCtrl": swRadiusCtrl,
       "swRadiusDeadTime": swRadiusDeadTime,
       "swRadiusTimeout": swRadiusTimeout,
       "swRadiusRetransmitAttempts": swRadiusRetransmitAttempts,
       "swRadiusServerTable": swRadiusServerTable,
       "swRadiusServerEntry": swRadiusServerEntry,
       "swRadiusServerIndex": swRadiusServerIndex,
       "swRadiusServerIpAddr": swRadiusServerIpAddr,
       "swRadiusServerKey": swRadiusServerKey,
       "swRadiusAuthPortNumber": swRadiusAuthPortNumber,
       "swRadiusAcctPortNumber": swRadiusAcctPortNumber,
       "swRadiusServerStatus": swRadiusServerStatus,
       "swRadiusServerTimeout": swRadiusServerTimeout,
       "swRadiusServerRetransmit": swRadiusServerRetransmit,
       "swRadiusServerAddrType": swRadiusServerAddrType,
       "swRadiusServerAddr": swRadiusServerAddr,
       "swRadiusVrfName": swRadiusVrfName,
       "swRadiusAuthInfo": swRadiusAuthInfo,
       "swRadiusAuthClientIdentifier": swRadiusAuthClientIdentifier,
       "swRadiusAuthClientInvalidServerAddresses": swRadiusAuthClientInvalidServerAddresses,
       "swRadiusAuthServerTable": swRadiusAuthServerTable,
       "swRadiusAuthServerEntry": swRadiusAuthServerEntry,
       "swRadiusAuthServerIndex": swRadiusAuthServerIndex,
       "swRadiusAuthServerAddress": swRadiusAuthServerAddress,
       "swRadiusAuthClientServerPortNumber": swRadiusAuthClientServerPortNumber,
       "swRadiusAuthClientRoundTripTime": swRadiusAuthClientRoundTripTime,
       "swRadiusAuthClientAccessRequests": swRadiusAuthClientAccessRequests,
       "swRadiusAuthClientAccessRetransmissions": swRadiusAuthClientAccessRetransmissions,
       "swRadiusAuthClientAccessAccepts": swRadiusAuthClientAccessAccepts,
       "swRadiusAuthClientAccessRejects": swRadiusAuthClientAccessRejects,
       "swRadiusAuthClientAccessChallenges": swRadiusAuthClientAccessChallenges,
       "swRadiusAuthClientMalformedAccessResponses": swRadiusAuthClientMalformedAccessResponses,
       "swRadiusAuthClientBadAuthenticators": swRadiusAuthClientBadAuthenticators,
       "swRadiusAuthClientPendingRequests": swRadiusAuthClientPendingRequests,
       "swRadiusAuthClientTimeouts": swRadiusAuthClientTimeouts,
       "swRadiusAuthClientUnknownTypes": swRadiusAuthClientUnknownTypes,
       "swRadiusAuthClientPacketsDropped": swRadiusAuthClientPacketsDropped,
       "swRadiusAccountingCtrl": swRadiusAccountingCtrl,
       "swRadiusAcctUpdateInterval": swRadiusAcctUpdateInterval,
       "swRadiusAcctSuppressNullUserName": swRadiusAcctSuppressNullUserName,
       "swRadiusAcctServiceTable": swRadiusAcctServiceTable,
       "swRadiusAcctServiceEntry": swRadiusAcctServiceEntry,
       "swRadiusAcctServiceIndex": swRadiusAcctServiceIndex,
       "swRadiusAcctServiceMethod": swRadiusAcctServiceMethod,
       "swRadiusAcctServiceMode": swRadiusAcctServiceMode,
       "swRadiusAccountingInfo": swRadiusAccountingInfo,
       "swMacAuthBaseStatsInfo": swMacAuthBaseStatsInfo,
       "swMacAuthStateTable": swMacAuthStateTable,
       "swMacAuthStateEntry": swMacAuthStateEntry,
       "swPaeMacAddr": swPaeMacAddr,
       "swPaePortNumber": swPaePortNumber,
       "swAuthPaeState": swAuthPaeState,
       "swAuthBackendAuthState": swAuthBackendAuthState,
       "swAuthAuthControlledPortStatus": swAuthAuthControlledPortStatus,
       "swMacAuthStatsTable": swMacAuthStatsTable,
       "swMacAuthStatsEntry": swMacAuthStatsEntry,
       "swAuthEapolFramesRx": swAuthEapolFramesRx,
       "swAuthEapolFramesTx": swAuthEapolFramesTx,
       "swAuthEapolStartFramesRx": swAuthEapolStartFramesRx,
       "swAuthEapolLogoffFramesRx": swAuthEapolLogoffFramesRx,
       "swAuthEapolRespIdFramesRx": swAuthEapolRespIdFramesRx,
       "swAuthEapolRespFramesRx": swAuthEapolRespFramesRx,
       "swAuthEapolReqIdFramesTx": swAuthEapolReqIdFramesTx,
       "swAuthEapolReqFramesTx": swAuthEapolReqFramesTx,
       "swAuthInvalidEapolFramesRx": swAuthInvalidEapolFramesRx,
       "swAuthEapLengthErrorFramesRx": swAuthEapLengthErrorFramesRx,
       "swAuthLastEapolFrameVersion": swAuthLastEapolFrameVersion,
       "swAuthLastEapolFrameSource": swAuthLastEapolFrameSource,
       "swMacAuthDiagTable": swMacAuthDiagTable,
       "swMacAuthDiagEntry": swMacAuthDiagEntry,
       "swAuthEntersConnecting": swAuthEntersConnecting,
       "swAuthEapLogoffsWhileConnecting": swAuthEapLogoffsWhileConnecting,
       "swAuthEntersAuthenticating": swAuthEntersAuthenticating,
       "swAuthAuthSuccessWhileAuthenticating": swAuthAuthSuccessWhileAuthenticating,
       "swAuthAuthTimeoutsWhileAuthenticating": swAuthAuthTimeoutsWhileAuthenticating,
       "swAuthAuthFailWhileAuthenticating": swAuthAuthFailWhileAuthenticating,
       "swAuthAuthReauthsWhileAuthenticating": swAuthAuthReauthsWhileAuthenticating,
       "swAuthAuthEapStartsWhileAuthenticating": swAuthAuthEapStartsWhileAuthenticating,
       "swAuthAuthEapLogoffWhileAuthenticating": swAuthAuthEapLogoffWhileAuthenticating,
       "swAuthAuthReauthsWhileAuthenticated": swAuthAuthReauthsWhileAuthenticated,
       "swAuthAuthEapStartsWhileAuthenticated": swAuthAuthEapStartsWhileAuthenticated,
       "swAuthAuthEapLogoffWhileAuthenticated": swAuthAuthEapLogoffWhileAuthenticated,
       "swAuthBackendResponses": swAuthBackendResponses,
       "swAuthBackendAccessChallenges": swAuthBackendAccessChallenges,
       "swAuthBackendOtherRequestsToSupplicant": swAuthBackendOtherRequestsToSupplicant,
       "swAuthBackendNonNakResponsesFromSupplicant": swAuthBackendNonNakResponsesFromSupplicant,
       "swAuthBackendAuthSuccesses": swAuthBackendAuthSuccesses,
       "swAuthBackendAuthFails": swAuthBackendAuthFails,
       "swMacAuthSessionStatsTable": swMacAuthSessionStatsTable,
       "swMacAuthSessionStatsEntry": swMacAuthSessionStatsEntry,
       "swAuthSessionOctetsRx": swAuthSessionOctetsRx,
       "swAuthSessionOctetsTx": swAuthSessionOctetsTx,
       "swAuthSessionFramesRx": swAuthSessionFramesRx,
       "swAuthSessionFramesTx": swAuthSessionFramesTx,
       "swAuthSessionId": swAuthSessionId,
       "swAuthSessionAuthenticMethod": swAuthSessionAuthenticMethod,
       "swAuthSessionTime": swAuthSessionTime,
       "swAuthSessionTerminateCause": swAuthSessionTerminateCause,
       "swAuthSessionUserName": swAuthSessionUserName,
       "swDot1xAuthStateTable": swDot1xAuthStateTable,
       "swDot1xAuthStateEntry": swDot1xAuthStateEntry,
       "swDot1xAuthPortNumber": swDot1xAuthPortNumber,
       "swDot1xAuthVID": swDot1xAuthVID,
       "swDot1xAuthMACAddress": swDot1xAuthMACAddress,
       "swDot1xAuthenticatorPAEState": swDot1xAuthenticatorPAEState,
       "swDot1xAuthBackendAuthState": swDot1xAuthBackendAuthState,
       "swDot1xAuthAuthControlledStatus": swDot1xAuthAuthControlledStatus,
       "swDot1xAuthAssignVID": swDot1xAuthAssignVID,
       "swDot1xAuthAssignPriority": swDot1xAuthAssignPriority,
       "swDot1xAuthStatsTable": swDot1xAuthStatsTable,
       "swDot1xAuthStatsEntry": swDot1xAuthStatsEntry,
       "swDot1xAuthEapolFramesRx": swDot1xAuthEapolFramesRx,
       "swDot1xAuthEapolFramesTx": swDot1xAuthEapolFramesTx,
       "swDot1xAuthEapolStartFramesRx": swDot1xAuthEapolStartFramesRx,
       "swDot1xAuthEapolLogoffFramesRx": swDot1xAuthEapolLogoffFramesRx,
       "swDot1xAuthEapolRespIdFramesRx": swDot1xAuthEapolRespIdFramesRx,
       "swDot1xAuthEapolRespFramesRx": swDot1xAuthEapolRespFramesRx,
       "swDot1xAuthEapolReqIdFramesTx": swDot1xAuthEapolReqIdFramesTx,
       "swDot1xAuthEapolReqFramesTx": swDot1xAuthEapolReqFramesTx,
       "swDot1xAuthInvalidEapolFramesRx": swDot1xAuthInvalidEapolFramesRx,
       "swDot1xAuthEapLengthErrorFramesRx": swDot1xAuthEapLengthErrorFramesRx,
       "swDot1xAuthLastEapolFrameVersion": swDot1xAuthLastEapolFrameVersion,
       "swDot1xAuthLastEapolFrameSource": swDot1xAuthLastEapolFrameSource,
       "swDot1xAuthDiagTable": swDot1xAuthDiagTable,
       "swDot1xAuthDiagEntry": swDot1xAuthDiagEntry,
       "swDot1xAuthEntersConnecting": swDot1xAuthEntersConnecting,
       "swDot1xAuthEapLogoffsWhileConnecting": swDot1xAuthEapLogoffsWhileConnecting,
       "swDot1xAuthEntersAuthenticating": swDot1xAuthEntersAuthenticating,
       "swDot1xAuthAuthSuccessWhileAuthenticating": swDot1xAuthAuthSuccessWhileAuthenticating,
       "swDot1xAuthAuthTimeoutsWhileAuthenticating": swDot1xAuthAuthTimeoutsWhileAuthenticating,
       "swDot1xAuthAuthFailWhileAuthenticating": swDot1xAuthAuthFailWhileAuthenticating,
       "swDot1xAuthAuthReauthsWhileAuthenticating": swDot1xAuthAuthReauthsWhileAuthenticating,
       "swDot1xAuthAuthEapStartsWhileAuthenticating": swDot1xAuthAuthEapStartsWhileAuthenticating,
       "swDot1xAuthAuthEapLogoffWhileAuthenticating": swDot1xAuthAuthEapLogoffWhileAuthenticating,
       "swDot1xAuthAuthReauthsWhileAuthenticated": swDot1xAuthAuthReauthsWhileAuthenticated,
       "swDot1xAuthAuthEapStartsWhileAuthenticated": swDot1xAuthAuthEapStartsWhileAuthenticated,
       "swDot1xAuthAuthEapLogoffWhileAuthenticated": swDot1xAuthAuthEapLogoffWhileAuthenticated,
       "swDot1xAuthBackendResponses": swDot1xAuthBackendResponses,
       "swDot1xAuthBackendAccessChallenges": swDot1xAuthBackendAccessChallenges,
       "swDot1xAuthBackendOtherRequestsToSupplicant": swDot1xAuthBackendOtherRequestsToSupplicant,
       "swDot1xAuthBackendNonNakResponsesFromSupplicant": swDot1xAuthBackendNonNakResponsesFromSupplicant,
       "swDot1xAuthBackendAuthSuccesses": swDot1xAuthBackendAuthSuccesses,
       "swDot1xAuthBackendAuthFails": swDot1xAuthBackendAuthFails,
       "swDot1xAuthSessionStatsTable": swDot1xAuthSessionStatsTable,
       "swDot1xAuthSessionStatsEntry": swDot1xAuthSessionStatsEntry,
       "swDot1xAuthSessionOctetsRx": swDot1xAuthSessionOctetsRx,
       "swDot1xAuthSessionOctetsTx": swDot1xAuthSessionOctetsTx,
       "swDot1xAuthSessionFramesRx": swDot1xAuthSessionFramesRx,
       "swDot1xAuthSessionFramesTx": swDot1xAuthSessionFramesTx,
       "swDot1xAuthSessionId": swDot1xAuthSessionId,
       "swDot1xAuthSessionAuthenticMethod": swDot1xAuthSessionAuthenticMethod,
       "swDot1xAuthSessionTime": swDot1xAuthSessionTime,
       "swDot1xAuthSessionTerminateCause": swDot1xAuthSessionTerminateCause,
       "swDot1xAuthSessionUserName": swDot1xAuthSessionUserName,
       "swRadiusCommand": swRadiusCommand,
       "swRadiusForceDownPortNumber": swRadiusForceDownPortNumber,
       "swRadiusForceDownMacAddr": swRadiusForceDownMacAddr,
       "swAuthenticatedPortInfo": swAuthenticatedPortInfo,
       "swAuthenticatedPortCtrlTable": swAuthenticatedPortCtrlTable,
       "swAuthenticatedPortCtrlEntry": swAuthenticatedPortCtrlEntry,
       "swAuthenticatedPortNumber": swAuthenticatedPortNumber,
       "swAuthenticatedPortCapabilities": swAuthenticatedPortCapabilities,
       "swMacBasedPaePortInfo": swMacBasedPaePortInfo,
       "swMacBasedPaePortTable": swMacBasedPaePortTable,
       "swMacBasedPaePortEntry": swMacBasedPaePortEntry,
       "swMacBasedPaePortNumber": swMacBasedPaePortNumber,
       "swMacBasedPaeMacAddress": swMacBasedPaeMacAddress,
       "swMacBasedPaePortInitializeOrReauthStatus": swMacBasedPaePortInitializeOrReauthStatus,
       "swMacBasedPaeTable": swMacBasedPaeTable,
       "swMacBasedPaeEntry": swMacBasedPaeEntry,
       "swMacBasedPaePort": swMacBasedPaePort,
       "swMacBasedPaeMac": swMacBasedPaeMac,
       "swMacBasedPaeInitOrReauthStatus": swMacBasedPaeInitOrReauthStatus,
       "swPaeAuthenticator": swPaeAuthenticator,
       "swPaeAuthSysFwdPdu": swPaeAuthSysFwdPdu,
       "swPaeAuthSysMaxUser": swPaeAuthSysMaxUser,
       "swPaeAuthConfigTable": swPaeAuthConfigTable,
       "swPaeAuthConfigEntry": swPaeAuthConfigEntry,
       "swPaeAuthFwdPdu": swPaeAuthFwdPdu,
       "swPaeAuthMaxUser": swPaeAuthMaxUser,
       "swAuthStateTable": swAuthStateTable,
       "swAuthStateEntry": swAuthStateEntry,
       "swAuthPortNumber": swAuthPortNumber,
       "swAuthMacAddress": swAuthMacAddress,
       "swAuthAuthControlledStatus": swAuthAuthControlledStatus,
       "swAuthAssignVid": swAuthAssignVid,
       "swAuthAssignPriority": swAuthAssignPriority,
       "swAuthenticatorPAEState": swAuthenticatorPAEState,
       "swAuthBKdAuthState": swAuthBKdAuthState,
       "swCompoundAuthMgmt": swCompoundAuthMgmt,
       "swCompoundAuthPortTable": swCompoundAuthPortTable,
       "swCompoundAuthPortEntry": swCompoundAuthPortEntry,
       "swCompoundAuthPortIndex": swCompoundAuthPortIndex,
       "swCompoundAuthPortAuthMode": swCompoundAuthPortAuthMode,
       "swCompoundAuthPortMethod": swCompoundAuthPortMethod,
       "swCompoundAuthPortAuthVLANs": swCompoundAuthPortAuthVLANs,
       "swGuestVlanTable": swGuestVlanTable,
       "swGuestVlanEntry": swGuestVlanEntry,
       "swGuestVlanId": swGuestVlanId,
       "swGuestVlanPorts": swGuestVlanPorts,
       "swGuestVlanRowStatus": swGuestVlanRowStatus,
       "swAuthorizationAttributes": swAuthorizationAttributes,
       "swAuthServerFailoverState": swAuthServerFailoverState,
       "swAuthMACFormatCase": swAuthMACFormatCase,
       "swAuthMACFormatDelimiter": swAuthMACFormatDelimiter,
       "swAuthMACFormatDelimiterNumber": swAuthMACFormatDelimiterNumber}
)
