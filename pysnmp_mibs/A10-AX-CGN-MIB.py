# SNMP MIB module (A10-AX-CGN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/a10/A10-AX-CGN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:00:02 2025
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

(axDDoS,
 axFixedNatStats,
 axIpNatDsliteStats,
 axIpNatLoggingStats,
 axIpNatLsnStats,
 axIpNatNat64Stats,
 axIpNatStatsDynamicMappingAclName,
 axNetworkingStats) = mibBuilder.importSymbols(
    "A10-AX-MIB",
    "axDDoS",
    "axFixedNatStats",
    "axIpNatDsliteStats",
    "axIpNatLoggingStats",
    "axIpNatLsnStats",
    "axIpNatNat64Stats",
    "axIpNatStatsDynamicMappingAclName",
    "axNetworkingStats")

(a10Mgmt,) = mibBuilder.importSymbols(
    "A10-COMMON-MIB",
    "a10Mgmt")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AxIpNatLsnGlobalStats_ObjectIdentity = ObjectIdentity
axIpNatLsnGlobalStats = _AxIpNatLsnGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1)
)


class _AxIpNatLsnTotalUserQuotaSessions_Type(Integer32):
    """Custom type axIpNatLsnTotalUserQuotaSessions based on Integer32"""
    defaultValue = 0


_AxIpNatLsnTotalUserQuotaSessions_Type.__name__ = "Integer32"
_AxIpNatLsnTotalUserQuotaSessions_Object = MibScalar
axIpNatLsnTotalUserQuotaSessions = _AxIpNatLsnTotalUserQuotaSessions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 1),
    _AxIpNatLsnTotalUserQuotaSessions_Type()
)
axIpNatLsnTotalUserQuotaSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTotalUserQuotaSessions.setStatus("current")


class _AxIpNatLsnTotalIpAddrTranslated_Type(Integer32):
    """Custom type axIpNatLsnTotalIpAddrTranslated based on Integer32"""
    defaultValue = 0


_AxIpNatLsnTotalIpAddrTranslated_Type.__name__ = "Integer32"
_AxIpNatLsnTotalIpAddrTranslated_Object = MibScalar
axIpNatLsnTotalIpAddrTranslated = _AxIpNatLsnTotalIpAddrTranslated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 2),
    _AxIpNatLsnTotalIpAddrTranslated_Type()
)
axIpNatLsnTotalIpAddrTranslated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTotalIpAddrTranslated.setStatus("current")


class _AxIpNatLsnTotalFullConeSessions_Type(Integer32):
    """Custom type axIpNatLsnTotalFullConeSessions based on Integer32"""
    defaultValue = 0


_AxIpNatLsnTotalFullConeSessions_Type.__name__ = "Integer32"
_AxIpNatLsnTotalFullConeSessions_Object = MibScalar
axIpNatLsnTotalFullConeSessions = _AxIpNatLsnTotalFullConeSessions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 3),
    _AxIpNatLsnTotalFullConeSessions_Type()
)
axIpNatLsnTotalFullConeSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTotalFullConeSessions.setStatus("current")
_AxIpNatLsnTrafficStats_ObjectIdentity = ObjectIdentity
axIpNatLsnTrafficStats = _AxIpNatLsnTrafficStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4)
)
_AxIpNatLsnTrafficFullConeSessionCreated_Type = Integer32
_AxIpNatLsnTrafficFullConeSessionCreated_Object = MibScalar
axIpNatLsnTrafficFullConeSessionCreated = _AxIpNatLsnTrafficFullConeSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 1),
    _AxIpNatLsnTrafficFullConeSessionCreated_Type()
)
axIpNatLsnTrafficFullConeSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficFullConeSessionCreated.setStatus("current")
_AxIpNatLsnTrafficFullConeSessionFreed_Type = Integer32
_AxIpNatLsnTrafficFullConeSessionFreed_Object = MibScalar
axIpNatLsnTrafficFullConeSessionFreed = _AxIpNatLsnTrafficFullConeSessionFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 2),
    _AxIpNatLsnTrafficFullConeSessionFreed_Type()
)
axIpNatLsnTrafficFullConeSessionFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficFullConeSessionFreed.setStatus("current")
_AxIpNatLsnTrafficFailsInFullConeSessionCreation_Type = Integer32
_AxIpNatLsnTrafficFailsInFullConeSessionCreation_Object = MibScalar
axIpNatLsnTrafficFailsInFullConeSessionCreation = _AxIpNatLsnTrafficFailsInFullConeSessionCreation_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 3),
    _AxIpNatLsnTrafficFailsInFullConeSessionCreation_Type()
)
axIpNatLsnTrafficFailsInFullConeSessionCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficFailsInFullConeSessionCreation.setStatus("current")
_AxIpNatLsnTrafficHairpinSessionCreated_Type = Integer32
_AxIpNatLsnTrafficHairpinSessionCreated_Object = MibScalar
axIpNatLsnTrafficHairpinSessionCreated = _AxIpNatLsnTrafficHairpinSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 4),
    _AxIpNatLsnTrafficHairpinSessionCreated_Type()
)
axIpNatLsnTrafficHairpinSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficHairpinSessionCreated.setStatus("current")
_AxIpNatLsnTrafficEndpointIndepMapMatch_Type = Integer32
_AxIpNatLsnTrafficEndpointIndepMapMatch_Object = MibScalar
axIpNatLsnTrafficEndpointIndepMapMatch = _AxIpNatLsnTrafficEndpointIndepMapMatch_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 5),
    _AxIpNatLsnTrafficEndpointIndepMapMatch_Type()
)
axIpNatLsnTrafficEndpointIndepMapMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficEndpointIndepMapMatch.setStatus("current")
_AxIpNatLsnTrafficEndpointIndepFilterMatch_Type = Integer32
_AxIpNatLsnTrafficEndpointIndepFilterMatch_Object = MibScalar
axIpNatLsnTrafficEndpointIndepFilterMatch = _AxIpNatLsnTrafficEndpointIndepFilterMatch_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 6),
    _AxIpNatLsnTrafficEndpointIndepFilterMatch_Type()
)
axIpNatLsnTrafficEndpointIndepFilterMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficEndpointIndepFilterMatch.setStatus("current")
_AxIpNatLsnTrafficUserQuotasCreated_Type = Integer32
_AxIpNatLsnTrafficUserQuotasCreated_Object = MibScalar
axIpNatLsnTrafficUserQuotasCreated = _AxIpNatLsnTrafficUserQuotasCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 7),
    _AxIpNatLsnTrafficUserQuotasCreated_Type()
)
axIpNatLsnTrafficUserQuotasCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficUserQuotasCreated.setStatus("current")
_AxIpNatLsnTrafficUserQuotasFreed_Type = Integer32
_AxIpNatLsnTrafficUserQuotasFreed_Object = MibScalar
axIpNatLsnTrafficUserQuotasFreed = _AxIpNatLsnTrafficUserQuotasFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 8),
    _AxIpNatLsnTrafficUserQuotasFreed_Type()
)
axIpNatLsnTrafficUserQuotasFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficUserQuotasFreed.setStatus("current")
_AxIpNatLsnTrafficFailsInUserQuotasCreation_Type = Integer32
_AxIpNatLsnTrafficFailsInUserQuotasCreation_Object = MibScalar
axIpNatLsnTrafficFailsInUserQuotasCreation = _AxIpNatLsnTrafficFailsInUserQuotasCreation_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 9),
    _AxIpNatLsnTrafficFailsInUserQuotasCreation_Type()
)
axIpNatLsnTrafficFailsInUserQuotasCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficFailsInUserQuotasCreation.setStatus("current")
_AxIpNatLsnTrafficIcmpUserQuotasExceeded_Type = Integer32
_AxIpNatLsnTrafficIcmpUserQuotasExceeded_Object = MibScalar
axIpNatLsnTrafficIcmpUserQuotasExceeded = _AxIpNatLsnTrafficIcmpUserQuotasExceeded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 10),
    _AxIpNatLsnTrafficIcmpUserQuotasExceeded_Type()
)
axIpNatLsnTrafficIcmpUserQuotasExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficIcmpUserQuotasExceeded.setStatus("current")
_AxIpNatLsnTrafficUdpUserQuotasExceeded_Type = Integer32
_AxIpNatLsnTrafficUdpUserQuotasExceeded_Object = MibScalar
axIpNatLsnTrafficUdpUserQuotasExceeded = _AxIpNatLsnTrafficUdpUserQuotasExceeded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 11),
    _AxIpNatLsnTrafficUdpUserQuotasExceeded_Type()
)
axIpNatLsnTrafficUdpUserQuotasExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficUdpUserQuotasExceeded.setStatus("current")
_AxIpNatLsnTrafficTcpUserQuotasExceeded_Type = Integer32
_AxIpNatLsnTrafficTcpUserQuotasExceeded_Object = MibScalar
axIpNatLsnTrafficTcpUserQuotasExceeded = _AxIpNatLsnTrafficTcpUserQuotasExceeded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 12),
    _AxIpNatLsnTrafficTcpUserQuotasExceeded_Type()
)
axIpNatLsnTrafficTcpUserQuotasExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficTcpUserQuotasExceeded.setStatus("current")
_AxIpNatLsnTrafficExtendedUserQuotasMatch_Type = Integer32
_AxIpNatLsnTrafficExtendedUserQuotasMatch_Object = MibScalar
axIpNatLsnTrafficExtendedUserQuotasMatch = _AxIpNatLsnTrafficExtendedUserQuotasMatch_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 13),
    _AxIpNatLsnTrafficExtendedUserQuotasMatch_Type()
)
axIpNatLsnTrafficExtendedUserQuotasMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficExtendedUserQuotasMatch.setStatus("current")
_AxIpNatLsnTrafficExtendedUserQuotasExceeded_Type = Integer32
_AxIpNatLsnTrafficExtendedUserQuotasExceeded_Object = MibScalar
axIpNatLsnTrafficExtendedUserQuotasExceeded = _AxIpNatLsnTrafficExtendedUserQuotasExceeded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 14),
    _AxIpNatLsnTrafficExtendedUserQuotasExceeded_Type()
)
axIpNatLsnTrafficExtendedUserQuotasExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficExtendedUserQuotasExceeded.setStatus("current")
_AxIpNatLsnTrafficNatPortUnavailable_Type = Integer32
_AxIpNatLsnTrafficNatPortUnavailable_Object = MibScalar
axIpNatLsnTrafficNatPortUnavailable = _AxIpNatLsnTrafficNatPortUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 15),
    _AxIpNatLsnTrafficNatPortUnavailable_Type()
)
axIpNatLsnTrafficNatPortUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficNatPortUnavailable.setStatus("current")
_AxIpNatLsnTrafficNewUserResourceUnavailable_Type = Integer32
_AxIpNatLsnTrafficNewUserResourceUnavailable_Object = MibScalar
axIpNatLsnTrafficNewUserResourceUnavailable = _AxIpNatLsnTrafficNewUserResourceUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 4, 16),
    _AxIpNatLsnTrafficNewUserResourceUnavailable_Type()
)
axIpNatLsnTrafficNewUserResourceUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTrafficNewUserResourceUnavailable.setStatus("current")
_AxIpNatLsnSessionStats_ObjectIdentity = ObjectIdentity
axIpNatLsnSessionStats = _AxIpNatLsnSessionStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 5)
)
_AxIpNatLsnSessionDataSessionsUsed_Type = CounterBasedGauge64
_AxIpNatLsnSessionDataSessionsUsed_Object = MibScalar
axIpNatLsnSessionDataSessionsUsed = _AxIpNatLsnSessionDataSessionsUsed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 5, 1),
    _AxIpNatLsnSessionDataSessionsUsed_Type()
)
axIpNatLsnSessionDataSessionsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnSessionDataSessionsUsed.setStatus("current")
_AxIpNatLsnSessionDataSessionsFree_Type = CounterBasedGauge64
_AxIpNatLsnSessionDataSessionsFree_Object = MibScalar
axIpNatLsnSessionDataSessionsFree = _AxIpNatLsnSessionDataSessionsFree_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 5, 2),
    _AxIpNatLsnSessionDataSessionsFree_Type()
)
axIpNatLsnSessionDataSessionsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnSessionDataSessionsFree.setStatus("current")
_AxIpNatLsnSessionSmpSessionsUsed_Type = CounterBasedGauge64
_AxIpNatLsnSessionSmpSessionsUsed_Object = MibScalar
axIpNatLsnSessionSmpSessionsUsed = _AxIpNatLsnSessionSmpSessionsUsed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 5, 3),
    _AxIpNatLsnSessionSmpSessionsUsed_Type()
)
axIpNatLsnSessionSmpSessionsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnSessionSmpSessionsUsed.setStatus("current")
_AxIpNatLsnSessionSmpSessionsFree_Type = CounterBasedGauge64
_AxIpNatLsnSessionSmpSessionsFree_Object = MibScalar
axIpNatLsnSessionSmpSessionsFree = _AxIpNatLsnSessionSmpSessionsFree_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 5, 4),
    _AxIpNatLsnSessionSmpSessionsFree_Type()
)
axIpNatLsnSessionSmpSessionsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnSessionSmpSessionsFree.setStatus("current")
_AxIpNatLsnNatPortUsageStats_ObjectIdentity = ObjectIdentity
axIpNatLsnNatPortUsageStats = _AxIpNatLsnNatPortUsageStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 6)
)
_AxIpNatLsnNatPortTcpNatPortUsed_Type = Counter64
_AxIpNatLsnNatPortTcpNatPortUsed_Object = MibScalar
axIpNatLsnNatPortTcpNatPortUsed = _AxIpNatLsnNatPortTcpNatPortUsed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 6, 1),
    _AxIpNatLsnNatPortTcpNatPortUsed_Type()
)
axIpNatLsnNatPortTcpNatPortUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnNatPortTcpNatPortUsed.setStatus("current")
_AxIpNatLsnNatPortTcpNatPortFree_Type = Counter64
_AxIpNatLsnNatPortTcpNatPortFree_Object = MibScalar
axIpNatLsnNatPortTcpNatPortFree = _AxIpNatLsnNatPortTcpNatPortFree_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 6, 2),
    _AxIpNatLsnNatPortTcpNatPortFree_Type()
)
axIpNatLsnNatPortTcpNatPortFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnNatPortTcpNatPortFree.setStatus("current")
_AxIpNatLsnNatPortUdpNatPortUsed_Type = Counter64
_AxIpNatLsnNatPortUdpNatPortUsed_Object = MibScalar
axIpNatLsnNatPortUdpNatPortUsed = _AxIpNatLsnNatPortUdpNatPortUsed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 6, 3),
    _AxIpNatLsnNatPortUdpNatPortUsed_Type()
)
axIpNatLsnNatPortUdpNatPortUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnNatPortUdpNatPortUsed.setStatus("current")
_AxIpNatLsnNatPortUdpNatPortFree_Type = Counter64
_AxIpNatLsnNatPortUdpNatPortFree_Object = MibScalar
axIpNatLsnNatPortUdpNatPortFree = _AxIpNatLsnNatPortUdpNatPortFree_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 1, 6, 4),
    _AxIpNatLsnNatPortUdpNatPortFree_Type()
)
axIpNatLsnNatPortUdpNatPortFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnNatPortUdpNatPortFree.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotSessions_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5PrivateIpAddrTotSessions = _AxIpNatLsnTop5PrivateIpAddrTotSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 2)
)
_AxIpNatLsnTop5PrivateIpAddrTotSessionTable_Object = MibTable
axIpNatLsnTop5PrivateIpAddrTotSessionTable = _AxIpNatLsnTop5PrivateIpAddrTotSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 2, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotSessionTable.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotSessionEntry_Object = MibTableRow
axIpNatLsnTop5PrivateIpAddrTotSessionEntry = _AxIpNatLsnTop5PrivateIpAddrTotSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 2, 1, 1)
)
axIpNatLsnTop5PrivateIpAddrTotSessionEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axIpNatLsnTop5PrivateIpAddr"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotSessionEntry.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddr_Type = DisplayString
_AxIpNatLsnTop5PrivateIpAddr_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddr = _AxIpNatLsnTop5PrivateIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 2, 1, 1, 1),
    _AxIpNatLsnTop5PrivateIpAddr_Type()
)
axIpNatLsnTop5PrivateIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddr.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotNumSessions_Type = Integer32
_AxIpNatLsnTop5PrivateIpAddrTotNumSessions_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrTotNumSessions = _AxIpNatLsnTop5PrivateIpAddrTotNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 2, 1, 1, 2),
    _AxIpNatLsnTop5PrivateIpAddrTotNumSessions_Type()
)
axIpNatLsnTop5PrivateIpAddrTotNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotNumSessions.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrGlobalIpAddr_Type = DisplayString
_AxIpNatLsnTop5PrivateIpAddrGlobalIpAddr_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrGlobalIpAddr = _AxIpNatLsnTop5PrivateIpAddrGlobalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 2, 1, 1, 3),
    _AxIpNatLsnTop5PrivateIpAddrGlobalIpAddr_Type()
)
axIpNatLsnTop5PrivateIpAddrGlobalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrGlobalIpAddr.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotTcpPorts_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5PrivateIpAddrTotTcpPorts = _AxIpNatLsnTop5PrivateIpAddrTotTcpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 3)
)
_AxIpNatLsnTop5PrivateIpAddrTotTcpPortTable_Object = MibTable
axIpNatLsnTop5PrivateIpAddrTotTcpPortTable = _AxIpNatLsnTop5PrivateIpAddrTotTcpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 3, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotTcpPortTable.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotTcpPortEntry_Object = MibTableRow
axIpNatLsnTop5PrivateIpAddrTotTcpPortEntry = _AxIpNatLsnTop5PrivateIpAddrTotTcpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 3, 1, 1)
)
axIpNatLsnTop5PrivateIpAddrTotTcpPortEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axIpNatLsnTop5PrivateIpAddrInTcpPort"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotTcpPortEntry.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrInTcpPort_Type = DisplayString
_AxIpNatLsnTop5PrivateIpAddrInTcpPort_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrInTcpPort = _AxIpNatLsnTop5PrivateIpAddrInTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 3, 1, 1, 1),
    _AxIpNatLsnTop5PrivateIpAddrInTcpPort_Type()
)
axIpNatLsnTop5PrivateIpAddrInTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrInTcpPort.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotNumTcpPorts_Type = Integer32
_AxIpNatLsnTop5PrivateIpAddrTotNumTcpPorts_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrTotNumTcpPorts = _AxIpNatLsnTop5PrivateIpAddrTotNumTcpPorts_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 3, 1, 1, 2),
    _AxIpNatLsnTop5PrivateIpAddrTotNumTcpPorts_Type()
)
axIpNatLsnTop5PrivateIpAddrTotNumTcpPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotNumTcpPorts.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInTcpPort_Type = DisplayString
_AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInTcpPort_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInTcpPort = _AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 3, 1, 1, 3),
    _AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInTcpPort_Type()
)
axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInTcpPort.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotUdpPorts_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5PrivateIpAddrTotUdpPorts = _AxIpNatLsnTop5PrivateIpAddrTotUdpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 4)
)
_AxIpNatLsnTop5PrivateIpAddrTotUdpPortTable_Object = MibTable
axIpNatLsnTop5PrivateIpAddrTotUdpPortTable = _AxIpNatLsnTop5PrivateIpAddrTotUdpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 4, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotUdpPortTable.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotUdpPortEntry_Object = MibTableRow
axIpNatLsnTop5PrivateIpAddrTotUdpPortEntry = _AxIpNatLsnTop5PrivateIpAddrTotUdpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 4, 1, 1)
)
axIpNatLsnTop5PrivateIpAddrTotUdpPortEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axIpNatLsnTop5PrivateIpAddrInUdpPort"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotUdpPortEntry.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrInUdpPort_Type = DisplayString
_AxIpNatLsnTop5PrivateIpAddrInUdpPort_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrInUdpPort = _AxIpNatLsnTop5PrivateIpAddrInUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 4, 1, 1, 1),
    _AxIpNatLsnTop5PrivateIpAddrInUdpPort_Type()
)
axIpNatLsnTop5PrivateIpAddrInUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrInUdpPort.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotNumUdpPorts_Type = Integer32
_AxIpNatLsnTop5PrivateIpAddrTotNumUdpPorts_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrTotNumUdpPorts = _AxIpNatLsnTop5PrivateIpAddrTotNumUdpPorts_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 4, 1, 1, 2),
    _AxIpNatLsnTop5PrivateIpAddrTotNumUdpPorts_Type()
)
axIpNatLsnTop5PrivateIpAddrTotNumUdpPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotNumUdpPorts.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInUdpPort_Type = DisplayString
_AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInUdpPort_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInUdpPort = _AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 4, 1, 1, 3),
    _AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInUdpPort_Type()
)
axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInUdpPort.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotIcmpPorts_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5PrivateIpAddrTotIcmpPorts = _AxIpNatLsnTop5PrivateIpAddrTotIcmpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 5)
)
_AxIpNatLsnTop5PrivateIpAddrTotIcmpPortTable_Object = MibTable
axIpNatLsnTop5PrivateIpAddrTotIcmpPortTable = _AxIpNatLsnTop5PrivateIpAddrTotIcmpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 5, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotIcmpPortTable.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotIcmpPortEntry_Object = MibTableRow
axIpNatLsnTop5PrivateIpAddrTotIcmpPortEntry = _AxIpNatLsnTop5PrivateIpAddrTotIcmpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 5, 1, 1)
)
axIpNatLsnTop5PrivateIpAddrTotIcmpPortEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axIpNatLsnTop5PrivateIpAddrInIcmpPort"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotIcmpPortEntry.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrInIcmpPort_Type = DisplayString
_AxIpNatLsnTop5PrivateIpAddrInIcmpPort_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrInIcmpPort = _AxIpNatLsnTop5PrivateIpAddrInIcmpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 5, 1, 1, 1),
    _AxIpNatLsnTop5PrivateIpAddrInIcmpPort_Type()
)
axIpNatLsnTop5PrivateIpAddrInIcmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrInIcmpPort.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrTotNumIcmpPorts_Type = Integer32
_AxIpNatLsnTop5PrivateIpAddrTotNumIcmpPorts_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrTotNumIcmpPorts = _AxIpNatLsnTop5PrivateIpAddrTotNumIcmpPorts_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 5, 1, 1, 2),
    _AxIpNatLsnTop5PrivateIpAddrTotNumIcmpPorts_Type()
)
axIpNatLsnTop5PrivateIpAddrTotNumIcmpPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrTotNumIcmpPorts.setStatus("current")
_AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInIcmpPort_Type = DisplayString
_AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInIcmpPort_Object = MibTableColumn
axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInIcmpPort = _AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInIcmpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 5, 1, 1, 3),
    _AxIpNatLsnTop5PrivateIpAddrGlobalIpAddrInIcmpPort_Type()
)
axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInIcmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInIcmpPort.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotSessions_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5UserPrivateIpAddrTotSessions = _AxIpNatLsnTop5UserPrivateIpAddrTotSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 6)
)
_AxIpNatLsnTop5UserPrivateIpAddrTotSessionTable_Object = MibTable
axIpNatLsnTop5UserPrivateIpAddrTotSessionTable = _AxIpNatLsnTop5UserPrivateIpAddrTotSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 6, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotSessionTable.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotSessionEntry_Object = MibTableRow
axIpNatLsnTop5UserPrivateIpAddrTotSessionEntry = _AxIpNatLsnTop5UserPrivateIpAddrTotSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 6, 1, 1)
)
axIpNatLsnTop5UserPrivateIpAddrTotSessionEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axIpNatLsnTop5UserPrivateIpAddr"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotSessionEntry.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddr_Type = DisplayString
_AxIpNatLsnTop5UserPrivateIpAddr_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddr = _AxIpNatLsnTop5UserPrivateIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 6, 1, 1, 1),
    _AxIpNatLsnTop5UserPrivateIpAddr_Type()
)
axIpNatLsnTop5UserPrivateIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddr.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotNumSessions_Type = Integer32
_AxIpNatLsnTop5UserPrivateIpAddrTotNumSessions_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrTotNumSessions = _AxIpNatLsnTop5UserPrivateIpAddrTotNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 6, 1, 1, 2),
    _AxIpNatLsnTop5UserPrivateIpAddrTotNumSessions_Type()
)
axIpNatLsnTop5UserPrivateIpAddrTotNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotNumSessions.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddr_Type = DisplayString
_AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddr_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddr = _AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 6, 1, 1, 3),
    _AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddr_Type()
)
axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddr.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotTcpSessions_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5UserPrivateIpAddrTotTcpSessions = _AxIpNatLsnTop5UserPrivateIpAddrTotTcpSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 7)
)
_AxIpNatLsnTop5UserPrivateIpAddrTotTcpSessionTable_Object = MibTable
axIpNatLsnTop5UserPrivateIpAddrTotTcpSessionTable = _AxIpNatLsnTop5UserPrivateIpAddrTotTcpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 7, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotTcpSessionTable.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotTcpSessionEntry_Object = MibTableRow
axIpNatLsnTop5UserPrivateIpAddrTotTcpSessionEntry = _AxIpNatLsnTop5UserPrivateIpAddrTotTcpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 7, 1, 1)
)
axIpNatLsnTop5UserPrivateIpAddrTotTcpSessionEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axIpNatLsnTop5UserPrivateIpAddrInTcp"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotTcpSessionEntry.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrInTcp_Type = DisplayString
_AxIpNatLsnTop5UserPrivateIpAddrInTcp_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrInTcp = _AxIpNatLsnTop5UserPrivateIpAddrInTcp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 7, 1, 1, 1),
    _AxIpNatLsnTop5UserPrivateIpAddrInTcp_Type()
)
axIpNatLsnTop5UserPrivateIpAddrInTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrInTcp.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotNumTcpSessions_Type = Integer32
_AxIpNatLsnTop5UserPrivateIpAddrTotNumTcpSessions_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrTotNumTcpSessions = _AxIpNatLsnTop5UserPrivateIpAddrTotNumTcpSessions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 7, 1, 1, 2),
    _AxIpNatLsnTop5UserPrivateIpAddrTotNumTcpSessions_Type()
)
axIpNatLsnTop5UserPrivateIpAddrTotNumTcpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotNumTcpSessions.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInTcp_Type = DisplayString
_AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInTcp_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInTcp = _AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInTcp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 7, 1, 1, 3),
    _AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInTcp_Type()
)
axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInTcp.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotUdpSessions_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5UserPrivateIpAddrTotUdpSessions = _AxIpNatLsnTop5UserPrivateIpAddrTotUdpSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 8)
)
_AxIpNatLsnTop5UserPrivateIpAddrTotUdpSessionTable_Object = MibTable
axIpNatLsnTop5UserPrivateIpAddrTotUdpSessionTable = _AxIpNatLsnTop5UserPrivateIpAddrTotUdpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 8, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotUdpSessionTable.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotUdpSessionEntry_Object = MibTableRow
axIpNatLsnTop5UserPrivateIpAddrTotUdpSessionEntry = _AxIpNatLsnTop5UserPrivateIpAddrTotUdpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 8, 1, 1)
)
axIpNatLsnTop5UserPrivateIpAddrTotUdpSessionEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axIpNatLsnTop5UserPrivateIpAddrInUdp"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotUdpSessionEntry.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrInUdp_Type = DisplayString
_AxIpNatLsnTop5UserPrivateIpAddrInUdp_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrInUdp = _AxIpNatLsnTop5UserPrivateIpAddrInUdp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 8, 1, 1, 1),
    _AxIpNatLsnTop5UserPrivateIpAddrInUdp_Type()
)
axIpNatLsnTop5UserPrivateIpAddrInUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrInUdp.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotNumUdpSessions_Type = Integer32
_AxIpNatLsnTop5UserPrivateIpAddrTotNumUdpSessions_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrTotNumUdpSessions = _AxIpNatLsnTop5UserPrivateIpAddrTotNumUdpSessions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 8, 1, 1, 2),
    _AxIpNatLsnTop5UserPrivateIpAddrTotNumUdpSessions_Type()
)
axIpNatLsnTop5UserPrivateIpAddrTotNumUdpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotNumUdpSessions.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInUdp_Type = DisplayString
_AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInUdp_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInUdp = _AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInUdp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 8, 1, 1, 3),
    _AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInUdp_Type()
)
axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInUdp.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotIcmpSessions_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessions = _AxIpNatLsnTop5UserPrivateIpAddrTotIcmpSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 9)
)
_AxIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionTable_Object = MibTable
axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionTable = _AxIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 9, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionTable.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionEntry_Object = MibTableRow
axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionEntry = _AxIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 9, 1, 1)
)
axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axIpNatLsnTop5UserPrivateIpAddrInIcmp"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionEntry.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrInIcmp_Type = DisplayString
_AxIpNatLsnTop5UserPrivateIpAddrInIcmp_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrInIcmp = _AxIpNatLsnTop5UserPrivateIpAddrInIcmp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 9, 1, 1, 1),
    _AxIpNatLsnTop5UserPrivateIpAddrInIcmp_Type()
)
axIpNatLsnTop5UserPrivateIpAddrInIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrInIcmp.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrTotNumIcmpSessions_Type = Integer32
_AxIpNatLsnTop5UserPrivateIpAddrTotNumIcmpSessions_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrTotNumIcmpSessions = _AxIpNatLsnTop5UserPrivateIpAddrTotNumIcmpSessions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 9, 1, 1, 2),
    _AxIpNatLsnTop5UserPrivateIpAddrTotNumIcmpSessions_Type()
)
axIpNatLsnTop5UserPrivateIpAddrTotNumIcmpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrTotNumIcmpSessions.setStatus("current")
_AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInIcmp_Type = DisplayString
_AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInIcmp_Object = MibTableColumn
axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInIcmp = _AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInIcmp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 9, 1, 1, 3),
    _AxIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInIcmp_Type()
)
axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInIcmp.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrTotUsers_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5GlobalPoolIpAddrTotUsers = _AxIpNatLsnTop5GlobalPoolIpAddrTotUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 10)
)
_AxIpNatLsnTop5GlobalPoolIpAddrTotUserTable_Object = MibTable
axIpNatLsnTop5GlobalPoolIpAddrTotUserTable = _AxIpNatLsnTop5GlobalPoolIpAddrTotUserTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 10, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrTotUserTable.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrTotUserEntry_Object = MibTableRow
axIpNatLsnTop5GlobalPoolIpAddrTotUserEntry = _AxIpNatLsnTop5GlobalPoolIpAddrTotUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 10, 1, 1)
)
axIpNatLsnTop5GlobalPoolIpAddrTotUserEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axIpNatLsnTop5GlobalPoolIpAddr"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrTotUserEntry.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddr_Type = DisplayString
_AxIpNatLsnTop5GlobalPoolIpAddr_Object = MibTableColumn
axIpNatLsnTop5GlobalPoolIpAddr = _AxIpNatLsnTop5GlobalPoolIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 10, 1, 1, 1),
    _AxIpNatLsnTop5GlobalPoolIpAddr_Type()
)
axIpNatLsnTop5GlobalPoolIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddr.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrTotNumUsers_Type = Integer32
_AxIpNatLsnTop5GlobalPoolIpAddrTotNumUsers_Object = MibTableColumn
axIpNatLsnTop5GlobalPoolIpAddrTotNumUsers = _AxIpNatLsnTop5GlobalPoolIpAddrTotNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 10, 1, 1, 2),
    _AxIpNatLsnTop5GlobalPoolIpAddrTotNumUsers_Type()
)
axIpNatLsnTop5GlobalPoolIpAddrTotNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrTotNumUsers.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrTotTcpPorts_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5GlobalPoolIpAddrTotTcpPorts = _AxIpNatLsnTop5GlobalPoolIpAddrTotTcpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 11)
)
_AxIpNatLsnTop5GlobalPoolIpAddrTotTcpPortTable_Object = MibTable
axIpNatLsnTop5GlobalPoolIpAddrTotTcpPortTable = _AxIpNatLsnTop5GlobalPoolIpAddrTotTcpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 11, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrTotTcpPortTable.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrTotTcpPortEntry_Object = MibTableRow
axIpNatLsnTop5GlobalPoolIpAddrTotTcpPortEntry = _AxIpNatLsnTop5GlobalPoolIpAddrTotTcpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 11, 1, 1)
)
axIpNatLsnTop5GlobalPoolIpAddrTotTcpPortEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axIpNatLsnTop5GlobalPoolIpAddrInTcp"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrTotTcpPortEntry.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrInTcp_Type = DisplayString
_AxIpNatLsnTop5GlobalPoolIpAddrInTcp_Object = MibTableColumn
axIpNatLsnTop5GlobalPoolIpAddrInTcp = _AxIpNatLsnTop5GlobalPoolIpAddrInTcp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 11, 1, 1, 1),
    _AxIpNatLsnTop5GlobalPoolIpAddrInTcp_Type()
)
axIpNatLsnTop5GlobalPoolIpAddrInTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrInTcp.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrTotNumTcpPorts_Type = Integer32
_AxIpNatLsnTop5GlobalPoolIpAddrTotNumTcpPorts_Object = MibTableColumn
axIpNatLsnTop5GlobalPoolIpAddrTotNumTcpPorts = _AxIpNatLsnTop5GlobalPoolIpAddrTotNumTcpPorts_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 11, 1, 1, 2),
    _AxIpNatLsnTop5GlobalPoolIpAddrTotNumTcpPorts_Type()
)
axIpNatLsnTop5GlobalPoolIpAddrTotNumTcpPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrTotNumTcpPorts.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrTotUdpPorts_ObjectIdentity = ObjectIdentity
axIpNatLsnTop5GlobalPoolIpAddrTotUdpPorts = _AxIpNatLsnTop5GlobalPoolIpAddrTotUdpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 12)
)
_AxIpNatLsnTop5GlobalPoolIpAddrTotUdpPortTable_Object = MibTable
axIpNatLsnTop5GlobalPoolIpAddrTotUdpPortTable = _AxIpNatLsnTop5GlobalPoolIpAddrTotUdpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 12, 1)
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrTotUdpPortTable.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrTotUdpPortEntry_Object = MibTableRow
axIpNatLsnTop5GlobalPoolIpAddrTotUdpPortEntry = _AxIpNatLsnTop5GlobalPoolIpAddrTotUdpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 12, 1, 1)
)
axIpNatLsnTop5GlobalPoolIpAddrTotUdpPortEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axIpNatLsnTop5GlobalPoolIpAddrInUdp"),
)
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrTotUdpPortEntry.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrInUdp_Type = DisplayString
_AxIpNatLsnTop5GlobalPoolIpAddrInUdp_Object = MibTableColumn
axIpNatLsnTop5GlobalPoolIpAddrInUdp = _AxIpNatLsnTop5GlobalPoolIpAddrInUdp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 12, 1, 1, 1),
    _AxIpNatLsnTop5GlobalPoolIpAddrInUdp_Type()
)
axIpNatLsnTop5GlobalPoolIpAddrInUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrInUdp.setStatus("current")
_AxIpNatLsnTop5GlobalPoolIpAddrTotNumUdpPorts_Type = Integer32
_AxIpNatLsnTop5GlobalPoolIpAddrTotNumUdpPorts_Object = MibTableColumn
axIpNatLsnTop5GlobalPoolIpAddrTotNumUdpPorts = _AxIpNatLsnTop5GlobalPoolIpAddrTotNumUdpPorts_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 12, 1, 1, 2),
    _AxIpNatLsnTop5GlobalPoolIpAddrTotNumUdpPorts_Type()
)
axIpNatLsnTop5GlobalPoolIpAddrTotNumUdpPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTop5GlobalPoolIpAddrTotNumUdpPorts.setStatus("current")
_AxIpNatLsnAlgSipStats_ObjectIdentity = ObjectIdentity
axIpNatLsnAlgSipStats = _AxIpNatLsnAlgSipStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 13)
)
_AxIpNatLsnAlgSipStatMethodRegister_Type = Counter64
_AxIpNatLsnAlgSipStatMethodRegister_Object = MibScalar
axIpNatLsnAlgSipStatMethodRegister = _AxIpNatLsnAlgSipStatMethodRegister_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 13, 1),
    _AxIpNatLsnAlgSipStatMethodRegister_Type()
)
axIpNatLsnAlgSipStatMethodRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnAlgSipStatMethodRegister.setStatus("current")
_AxIpNatLsnAlgSipStatMethodInvite_Type = Counter64
_AxIpNatLsnAlgSipStatMethodInvite_Object = MibScalar
axIpNatLsnAlgSipStatMethodInvite = _AxIpNatLsnAlgSipStatMethodInvite_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 13, 2),
    _AxIpNatLsnAlgSipStatMethodInvite_Type()
)
axIpNatLsnAlgSipStatMethodInvite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnAlgSipStatMethodInvite.setStatus("current")
_AxIpNatLsnAlgSipStatMethodAck_Type = Counter64
_AxIpNatLsnAlgSipStatMethodAck_Object = MibScalar
axIpNatLsnAlgSipStatMethodAck = _AxIpNatLsnAlgSipStatMethodAck_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 13, 3),
    _AxIpNatLsnAlgSipStatMethodAck_Type()
)
axIpNatLsnAlgSipStatMethodAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnAlgSipStatMethodAck.setStatus("current")
_AxIpNatLsnAlgSipStatMethodCancel_Type = Counter64
_AxIpNatLsnAlgSipStatMethodCancel_Object = MibScalar
axIpNatLsnAlgSipStatMethodCancel = _AxIpNatLsnAlgSipStatMethodCancel_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 13, 4),
    _AxIpNatLsnAlgSipStatMethodCancel_Type()
)
axIpNatLsnAlgSipStatMethodCancel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnAlgSipStatMethodCancel.setStatus("current")
_AxIpNatLsnAlgSipStatMethodBye_Type = Counter64
_AxIpNatLsnAlgSipStatMethodBye_Object = MibScalar
axIpNatLsnAlgSipStatMethodBye = _AxIpNatLsnAlgSipStatMethodBye_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 13, 5),
    _AxIpNatLsnAlgSipStatMethodBye_Type()
)
axIpNatLsnAlgSipStatMethodBye.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnAlgSipStatMethodBye.setStatus("current")
_AxIpNatLsnAlgSipStatMethodOptions_Type = Counter64
_AxIpNatLsnAlgSipStatMethodOptions_Object = MibScalar
axIpNatLsnAlgSipStatMethodOptions = _AxIpNatLsnAlgSipStatMethodOptions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 13, 6),
    _AxIpNatLsnAlgSipStatMethodOptions_Type()
)
axIpNatLsnAlgSipStatMethodOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnAlgSipStatMethodOptions.setStatus("current")
_AxIpNatLsnAlgSipStatMethodPrack_Type = Counter64
_AxIpNatLsnAlgSipStatMethodPrack_Object = MibScalar
axIpNatLsnAlgSipStatMethodPrack = _AxIpNatLsnAlgSipStatMethodPrack_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 13, 7),
    _AxIpNatLsnAlgSipStatMethodPrack_Type()
)
axIpNatLsnAlgSipStatMethodPrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnAlgSipStatMethodPrack.setStatus("current")
_AxIpNatLsnAlgSipStatMethodSubscribe_Type = Counter64
_AxIpNatLsnAlgSipStatMethodSubscribe_Object = MibScalar
axIpNatLsnAlgSipStatMethodSubscribe = _AxIpNatLsnAlgSipStatMethodSubscribe_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 13, 8),
    _AxIpNatLsnAlgSipStatMethodSubscribe_Type()
)
axIpNatLsnAlgSipStatMethodSubscribe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnAlgSipStatMethodSubscribe.setStatus("current")
_AxIpNatLsnAlgSipStatMethodNotify_Type = Counter64
_AxIpNatLsnAlgSipStatMethodNotify_Object = MibScalar
axIpNatLsnAlgSipStatMethodNotify = _AxIpNatLsnAlgSipStatMethodNotify_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 13, 9),
    _AxIpNatLsnAlgSipStatMethodNotify_Type()
)
axIpNatLsnAlgSipStatMethodNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnAlgSipStatMethodNotify.setStatus("current")
_AxIpNatLsnAlgSipStatMethodPublish_Type = Counter64
_AxIpNatLsnAlgSipStatMethodPublish_Object = MibScalar
axIpNatLsnAlgSipStatMethodPublish = _AxIpNatLsnAlgSipStatMethodPublish_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 13, 10),
    _AxIpNatLsnAlgSipStatMethodPublish_Type()
)
axIpNatLsnAlgSipStatMethodPublish.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnAlgSipStatMethodPublish.setStatus("current")
_AxIpNatLsnAlgSipStatMethodInfo_Type = Counter64
_AxIpNatLsnAlgSipStatMethodInfo_Object = MibScalar
axIpNatLsnAlgSipStatMethodInfo = _AxIpNatLsnAlgSipStatMethodInfo_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 13, 11),
    _AxIpNatLsnAlgSipStatMethodInfo_Type()
)
axIpNatLsnAlgSipStatMethodInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnAlgSipStatMethodInfo.setStatus("current")
_AxIpNatLsnAlgSipStatMethodRefer_Type = Counter64
_AxIpNatLsnAlgSipStatMethodRefer_Object = MibScalar
axIpNatLsnAlgSipStatMethodRefer = _AxIpNatLsnAlgSipStatMethodRefer_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 13, 12),
    _AxIpNatLsnAlgSipStatMethodRefer_Type()
)
axIpNatLsnAlgSipStatMethodRefer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnAlgSipStatMethodRefer.setStatus("current")
_AxIpNatLsnAlgSipStatMethodMessage_Type = Counter64
_AxIpNatLsnAlgSipStatMethodMessage_Object = MibScalar
axIpNatLsnAlgSipStatMethodMessage = _AxIpNatLsnAlgSipStatMethodMessage_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 13, 13),
    _AxIpNatLsnAlgSipStatMethodMessage_Type()
)
axIpNatLsnAlgSipStatMethodMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnAlgSipStatMethodMessage.setStatus("current")
_AxIpNatLsnAlgSipStatMethodUpdate_Type = Counter64
_AxIpNatLsnAlgSipStatMethodUpdate_Object = MibScalar
axIpNatLsnAlgSipStatMethodUpdate = _AxIpNatLsnAlgSipStatMethodUpdate_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 13, 14),
    _AxIpNatLsnAlgSipStatMethodUpdate_Type()
)
axIpNatLsnAlgSipStatMethodUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnAlgSipStatMethodUpdate.setStatus("current")
_AxIpNatLsnAlgSipStatMethodUnknown_Type = Counter64
_AxIpNatLsnAlgSipStatMethodUnknown_Object = MibScalar
axIpNatLsnAlgSipStatMethodUnknown = _AxIpNatLsnAlgSipStatMethodUnknown_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 13, 15),
    _AxIpNatLsnAlgSipStatMethodUnknown_Type()
)
axIpNatLsnAlgSipStatMethodUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnAlgSipStatMethodUnknown.setStatus("current")
_AxIpNatLsnPoolStats_ObjectIdentity = ObjectIdentity
axIpNatLsnPoolStats = _AxIpNatLsnPoolStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14)
)
_AxIpNatLsnDataSessionUsed_Type = CounterBasedGauge64
_AxIpNatLsnDataSessionUsed_Object = MibScalar
axIpNatLsnDataSessionUsed = _AxIpNatLsnDataSessionUsed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 1),
    _AxIpNatLsnDataSessionUsed_Type()
)
axIpNatLsnDataSessionUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnDataSessionUsed.setStatus("deprecated")
_AxIpNatLsnDataSessionFreed_Type = CounterBasedGauge64
_AxIpNatLsnDataSessionFreed_Object = MibScalar
axIpNatLsnDataSessionFreed = _AxIpNatLsnDataSessionFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 2),
    _AxIpNatLsnDataSessionFreed_Type()
)
axIpNatLsnDataSessionFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnDataSessionFreed.setStatus("deprecated")
_AxIpNatLsnTCPNatPortUsed_Type = CounterBasedGauge64
_AxIpNatLsnTCPNatPortUsed_Object = MibScalar
axIpNatLsnTCPNatPortUsed = _AxIpNatLsnTCPNatPortUsed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 3),
    _AxIpNatLsnTCPNatPortUsed_Type()
)
axIpNatLsnTCPNatPortUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTCPNatPortUsed.setStatus("deprecated")
_AxIpNatLsnTCPNatPortFree_Type = CounterBasedGauge64
_AxIpNatLsnTCPNatPortFree_Object = MibScalar
axIpNatLsnTCPNatPortFree = _AxIpNatLsnTCPNatPortFree_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 4),
    _AxIpNatLsnTCPNatPortFree_Type()
)
axIpNatLsnTCPNatPortFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnTCPNatPortFree.setStatus("deprecated")
_AxIpNatLsnUDPNatPortUsed_Type = CounterBasedGauge64
_AxIpNatLsnUDPNatPortUsed_Object = MibScalar
axIpNatLsnUDPNatPortUsed = _AxIpNatLsnUDPNatPortUsed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 5),
    _AxIpNatLsnUDPNatPortUsed_Type()
)
axIpNatLsnUDPNatPortUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnUDPNatPortUsed.setStatus("deprecated")
_AxIpNatLsnUDPNatPortFree_Type = CounterBasedGauge64
_AxIpNatLsnUDPNatPortFree_Object = MibScalar
axIpNatLsnUDPNatPortFree = _AxIpNatLsnUDPNatPortFree_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 6),
    _AxIpNatLsnUDPNatPortFree_Type()
)
axIpNatLsnUDPNatPortFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnUDPNatPortFree.setStatus("deprecated")
_AxIpNatLsnPoolStatTable_Object = MibTable
axIpNatLsnPoolStatTable = _AxIpNatLsnPoolStatTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11)
)
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatTable.setStatus("deprecated")
_AxIpNatLsnPoolStatEntry_Object = MibTableRow
axIpNatLsnPoolStatEntry = _AxIpNatLsnPoolStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1)
)
axIpNatLsnPoolStatEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axIpNatLsnPoolStatPoolName"),
    (0, "A10-AX-CGN-MIB", "axIpNatLsnPoolStatAddress"),
)
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatEntry.setStatus("current")
_AxIpNatLsnPoolStatPoolName_Type = DisplayString
_AxIpNatLsnPoolStatPoolName_Object = MibTableColumn
axIpNatLsnPoolStatPoolName = _AxIpNatLsnPoolStatPoolName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 1),
    _AxIpNatLsnPoolStatPoolName_Type()
)
axIpNatLsnPoolStatPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatPoolName.setStatus("current")
_AxIpNatLsnPoolStatAddress_Type = DisplayString
_AxIpNatLsnPoolStatAddress_Object = MibTableColumn
axIpNatLsnPoolStatAddress = _AxIpNatLsnPoolStatAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 2),
    _AxIpNatLsnPoolStatAddress_Type()
)
axIpNatLsnPoolStatAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatAddress.setStatus("current")
_AxIpNatLsnPoolStatUsers_Type = CounterBasedGauge64
_AxIpNatLsnPoolStatUsers_Object = MibTableColumn
axIpNatLsnPoolStatUsers = _AxIpNatLsnPoolStatUsers_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 3),
    _AxIpNatLsnPoolStatUsers_Type()
)
axIpNatLsnPoolStatUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatUsers.setStatus("current")
_AxIpNatLsnPoolStatIcmpUsed_Type = CounterBasedGauge64
_AxIpNatLsnPoolStatIcmpUsed_Object = MibTableColumn
axIpNatLsnPoolStatIcmpUsed = _AxIpNatLsnPoolStatIcmpUsed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 4),
    _AxIpNatLsnPoolStatIcmpUsed_Type()
)
axIpNatLsnPoolStatIcmpUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatIcmpUsed.setStatus("current")
_AxIpNatLsnPoolStatIcmpFreed_Type = CounterBasedGauge64
_AxIpNatLsnPoolStatIcmpFreed_Object = MibTableColumn
axIpNatLsnPoolStatIcmpFreed = _AxIpNatLsnPoolStatIcmpFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 5),
    _AxIpNatLsnPoolStatIcmpFreed_Type()
)
axIpNatLsnPoolStatIcmpFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatIcmpFreed.setStatus("current")
_AxIpNatLsnPoolStatIcmpTotal_Type = CounterBasedGauge64
_AxIpNatLsnPoolStatIcmpTotal_Object = MibTableColumn
axIpNatLsnPoolStatIcmpTotal = _AxIpNatLsnPoolStatIcmpTotal_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 6),
    _AxIpNatLsnPoolStatIcmpTotal_Type()
)
axIpNatLsnPoolStatIcmpTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatIcmpTotal.setStatus("current")
_AxIpNatLsnPoolStatIcmpReserved_Type = CounterBasedGauge64
_AxIpNatLsnPoolStatIcmpReserved_Object = MibTableColumn
axIpNatLsnPoolStatIcmpReserved = _AxIpNatLsnPoolStatIcmpReserved_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 7),
    _AxIpNatLsnPoolStatIcmpReserved_Type()
)
axIpNatLsnPoolStatIcmpReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatIcmpReserved.setStatus("current")
_AxIpNatLsnPoolStatIcmpPeak_Type = Counter64
_AxIpNatLsnPoolStatIcmpPeak_Object = MibTableColumn
axIpNatLsnPoolStatIcmpPeak = _AxIpNatLsnPoolStatIcmpPeak_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 8),
    _AxIpNatLsnPoolStatIcmpPeak_Type()
)
axIpNatLsnPoolStatIcmpPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatIcmpPeak.setStatus("current")
_AxIpNatLsnPoolStatIcmpHitFull_Type = CounterBasedGauge64
_AxIpNatLsnPoolStatIcmpHitFull_Object = MibTableColumn
axIpNatLsnPoolStatIcmpHitFull = _AxIpNatLsnPoolStatIcmpHitFull_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 9),
    _AxIpNatLsnPoolStatIcmpHitFull_Type()
)
axIpNatLsnPoolStatIcmpHitFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatIcmpHitFull.setStatus("current")
_AxIpNatLsnPoolStatTcpUsed_Type = CounterBasedGauge64
_AxIpNatLsnPoolStatTcpUsed_Object = MibTableColumn
axIpNatLsnPoolStatTcpUsed = _AxIpNatLsnPoolStatTcpUsed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 10),
    _AxIpNatLsnPoolStatTcpUsed_Type()
)
axIpNatLsnPoolStatTcpUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatTcpUsed.setStatus("current")
_AxIpNatLsnPoolStatTcpFreed_Type = CounterBasedGauge64
_AxIpNatLsnPoolStatTcpFreed_Object = MibTableColumn
axIpNatLsnPoolStatTcpFreed = _AxIpNatLsnPoolStatTcpFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 11),
    _AxIpNatLsnPoolStatTcpFreed_Type()
)
axIpNatLsnPoolStatTcpFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatTcpFreed.setStatus("current")
_AxIpNatLsnPoolStatTcpTotal_Type = CounterBasedGauge64
_AxIpNatLsnPoolStatTcpTotal_Object = MibTableColumn
axIpNatLsnPoolStatTcpTotal = _AxIpNatLsnPoolStatTcpTotal_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 12),
    _AxIpNatLsnPoolStatTcpTotal_Type()
)
axIpNatLsnPoolStatTcpTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatTcpTotal.setStatus("current")
_AxIpNatLsnPoolStatTcpReserved_Type = CounterBasedGauge64
_AxIpNatLsnPoolStatTcpReserved_Object = MibTableColumn
axIpNatLsnPoolStatTcpReserved = _AxIpNatLsnPoolStatTcpReserved_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 13),
    _AxIpNatLsnPoolStatTcpReserved_Type()
)
axIpNatLsnPoolStatTcpReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatTcpReserved.setStatus("current")
_AxIpNatLsnPoolStatTcpPeak_Type = Counter64
_AxIpNatLsnPoolStatTcpPeak_Object = MibTableColumn
axIpNatLsnPoolStatTcpPeak = _AxIpNatLsnPoolStatTcpPeak_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 14),
    _AxIpNatLsnPoolStatTcpPeak_Type()
)
axIpNatLsnPoolStatTcpPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatTcpPeak.setStatus("current")
_AxIpNatLsnPoolStatTcpHitFull_Type = CounterBasedGauge64
_AxIpNatLsnPoolStatTcpHitFull_Object = MibTableColumn
axIpNatLsnPoolStatTcpHitFull = _AxIpNatLsnPoolStatTcpHitFull_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 15),
    _AxIpNatLsnPoolStatTcpHitFull_Type()
)
axIpNatLsnPoolStatTcpHitFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatTcpHitFull.setStatus("current")
_AxIpNatLsnPoolStatUdpUsed_Type = CounterBasedGauge64
_AxIpNatLsnPoolStatUdpUsed_Object = MibTableColumn
axIpNatLsnPoolStatUdpUsed = _AxIpNatLsnPoolStatUdpUsed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 16),
    _AxIpNatLsnPoolStatUdpUsed_Type()
)
axIpNatLsnPoolStatUdpUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatUdpUsed.setStatus("current")
_AxIpNatLsnPoolStatUdpFreed_Type = CounterBasedGauge64
_AxIpNatLsnPoolStatUdpFreed_Object = MibTableColumn
axIpNatLsnPoolStatUdpFreed = _AxIpNatLsnPoolStatUdpFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 17),
    _AxIpNatLsnPoolStatUdpFreed_Type()
)
axIpNatLsnPoolStatUdpFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatUdpFreed.setStatus("current")
_AxIpNatLsnPoolStatUdpTotal_Type = CounterBasedGauge64
_AxIpNatLsnPoolStatUdpTotal_Object = MibTableColumn
axIpNatLsnPoolStatUdpTotal = _AxIpNatLsnPoolStatUdpTotal_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 18),
    _AxIpNatLsnPoolStatUdpTotal_Type()
)
axIpNatLsnPoolStatUdpTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatUdpTotal.setStatus("current")
_AxIpNatLsnPoolStatUdpReserved_Type = CounterBasedGauge64
_AxIpNatLsnPoolStatUdpReserved_Object = MibTableColumn
axIpNatLsnPoolStatUdpReserved = _AxIpNatLsnPoolStatUdpReserved_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 19),
    _AxIpNatLsnPoolStatUdpReserved_Type()
)
axIpNatLsnPoolStatUdpReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatUdpReserved.setStatus("current")
_AxIpNatLsnPoolStatUdpPeak_Type = Counter64
_AxIpNatLsnPoolStatUdpPeak_Object = MibTableColumn
axIpNatLsnPoolStatUdpPeak = _AxIpNatLsnPoolStatUdpPeak_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 20),
    _AxIpNatLsnPoolStatUdpPeak_Type()
)
axIpNatLsnPoolStatUdpPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatUdpPeak.setStatus("current")
_AxIpNatLsnPoolStatUdpHitFull_Type = CounterBasedGauge64
_AxIpNatLsnPoolStatUdpHitFull_Object = MibTableColumn
axIpNatLsnPoolStatUdpHitFull = _AxIpNatLsnPoolStatUdpHitFull_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 11, 1, 21),
    _AxIpNatLsnPoolStatUdpHitFull_Type()
)
axIpNatLsnPoolStatUdpHitFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolStatUdpHitFull.setStatus("current")
_AxIpNatLsnPoolNameStatTable_Object = MibTable
axIpNatLsnPoolNameStatTable = _AxIpNatLsnPoolNameStatTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12)
)
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatTable.setStatus("current")
_AxIpNatLsnPoolNameStatEntry_Object = MibTableRow
axIpNatLsnPoolNameStatEntry = _AxIpNatLsnPoolNameStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1)
)
axIpNatLsnPoolNameStatEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axIpNatLsnPoolNameStatPoolName"),
)
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatEntry.setStatus("current")
_AxIpNatLsnPoolNameStatPoolName_Type = DisplayString
_AxIpNatLsnPoolNameStatPoolName_Object = MibTableColumn
axIpNatLsnPoolNameStatPoolName = _AxIpNatLsnPoolNameStatPoolName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 1),
    _AxIpNatLsnPoolNameStatPoolName_Type()
)
axIpNatLsnPoolNameStatPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatPoolName.setStatus("current")
_AxIpNatLsnPoolNameStatAddress_Type = DisplayString
_AxIpNatLsnPoolNameStatAddress_Object = MibTableColumn
axIpNatLsnPoolNameStatAddress = _AxIpNatLsnPoolNameStatAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 2),
    _AxIpNatLsnPoolNameStatAddress_Type()
)
axIpNatLsnPoolNameStatAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatAddress.setStatus("current")
_AxIpNatLsnPoolNameEndAddress_Type = DisplayString
_AxIpNatLsnPoolNameEndAddress_Object = MibTableColumn
axIpNatLsnPoolNameEndAddress = _AxIpNatLsnPoolNameEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 3),
    _AxIpNatLsnPoolNameEndAddress_Type()
)
axIpNatLsnPoolNameEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameEndAddress.setStatus("current")
_AxIpNatLsnPoolNameStatUsers_Type = CounterBasedGauge64
_AxIpNatLsnPoolNameStatUsers_Object = MibTableColumn
axIpNatLsnPoolNameStatUsers = _AxIpNatLsnPoolNameStatUsers_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 4),
    _AxIpNatLsnPoolNameStatUsers_Type()
)
axIpNatLsnPoolNameStatUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatUsers.setStatus("current")
_AxIpNatLsnPoolNameStatIcmpUsed_Type = CounterBasedGauge64
_AxIpNatLsnPoolNameStatIcmpUsed_Object = MibTableColumn
axIpNatLsnPoolNameStatIcmpUsed = _AxIpNatLsnPoolNameStatIcmpUsed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 5),
    _AxIpNatLsnPoolNameStatIcmpUsed_Type()
)
axIpNatLsnPoolNameStatIcmpUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatIcmpUsed.setStatus("current")
_AxIpNatLsnPoolNameStatIcmpFreed_Type = CounterBasedGauge64
_AxIpNatLsnPoolNameStatIcmpFreed_Object = MibTableColumn
axIpNatLsnPoolNameStatIcmpFreed = _AxIpNatLsnPoolNameStatIcmpFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 6),
    _AxIpNatLsnPoolNameStatIcmpFreed_Type()
)
axIpNatLsnPoolNameStatIcmpFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatIcmpFreed.setStatus("current")
_AxIpNatLsnPoolNameStatIcmpTotal_Type = CounterBasedGauge64
_AxIpNatLsnPoolNameStatIcmpTotal_Object = MibTableColumn
axIpNatLsnPoolNameStatIcmpTotal = _AxIpNatLsnPoolNameStatIcmpTotal_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 7),
    _AxIpNatLsnPoolNameStatIcmpTotal_Type()
)
axIpNatLsnPoolNameStatIcmpTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatIcmpTotal.setStatus("current")
_AxIpNatLsnPoolNameStatIcmpReserved_Type = CounterBasedGauge64
_AxIpNatLsnPoolNameStatIcmpReserved_Object = MibTableColumn
axIpNatLsnPoolNameStatIcmpReserved = _AxIpNatLsnPoolNameStatIcmpReserved_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 8),
    _AxIpNatLsnPoolNameStatIcmpReserved_Type()
)
axIpNatLsnPoolNameStatIcmpReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatIcmpReserved.setStatus("current")
_AxIpNatLsnPoolNameStatIcmpPeak_Type = Counter64
_AxIpNatLsnPoolNameStatIcmpPeak_Object = MibTableColumn
axIpNatLsnPoolNameStatIcmpPeak = _AxIpNatLsnPoolNameStatIcmpPeak_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 9),
    _AxIpNatLsnPoolNameStatIcmpPeak_Type()
)
axIpNatLsnPoolNameStatIcmpPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatIcmpPeak.setStatus("current")
_AxIpNatLsnPoolNameStatIcmpHitFull_Type = CounterBasedGauge64
_AxIpNatLsnPoolNameStatIcmpHitFull_Object = MibTableColumn
axIpNatLsnPoolNameStatIcmpHitFull = _AxIpNatLsnPoolNameStatIcmpHitFull_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 10),
    _AxIpNatLsnPoolNameStatIcmpHitFull_Type()
)
axIpNatLsnPoolNameStatIcmpHitFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatIcmpHitFull.setStatus("current")
_AxIpNatLsnPoolNameStatTcpUsed_Type = CounterBasedGauge64
_AxIpNatLsnPoolNameStatTcpUsed_Object = MibTableColumn
axIpNatLsnPoolNameStatTcpUsed = _AxIpNatLsnPoolNameStatTcpUsed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 11),
    _AxIpNatLsnPoolNameStatTcpUsed_Type()
)
axIpNatLsnPoolNameStatTcpUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatTcpUsed.setStatus("current")
_AxIpNatLsnPoolNameStatTcpFreed_Type = CounterBasedGauge64
_AxIpNatLsnPoolNameStatTcpFreed_Object = MibTableColumn
axIpNatLsnPoolNameStatTcpFreed = _AxIpNatLsnPoolNameStatTcpFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 12),
    _AxIpNatLsnPoolNameStatTcpFreed_Type()
)
axIpNatLsnPoolNameStatTcpFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatTcpFreed.setStatus("current")
_AxIpNatLsnPoolNameStatTcpTotal_Type = CounterBasedGauge64
_AxIpNatLsnPoolNameStatTcpTotal_Object = MibTableColumn
axIpNatLsnPoolNameStatTcpTotal = _AxIpNatLsnPoolNameStatTcpTotal_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 13),
    _AxIpNatLsnPoolNameStatTcpTotal_Type()
)
axIpNatLsnPoolNameStatTcpTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatTcpTotal.setStatus("current")
_AxIpNatLsnPoolNameStatTcpReserved_Type = CounterBasedGauge64
_AxIpNatLsnPoolNameStatTcpReserved_Object = MibTableColumn
axIpNatLsnPoolNameStatTcpReserved = _AxIpNatLsnPoolNameStatTcpReserved_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 14),
    _AxIpNatLsnPoolNameStatTcpReserved_Type()
)
axIpNatLsnPoolNameStatTcpReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatTcpReserved.setStatus("current")
_AxIpNatLsnPoolNameStatTcpPeak_Type = Counter64
_AxIpNatLsnPoolNameStatTcpPeak_Object = MibTableColumn
axIpNatLsnPoolNameStatTcpPeak = _AxIpNatLsnPoolNameStatTcpPeak_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 15),
    _AxIpNatLsnPoolNameStatTcpPeak_Type()
)
axIpNatLsnPoolNameStatTcpPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatTcpPeak.setStatus("current")
_AxIpNatLsnPoolNameStatTcpHitFull_Type = CounterBasedGauge64
_AxIpNatLsnPoolNameStatTcpHitFull_Object = MibTableColumn
axIpNatLsnPoolNameStatTcpHitFull = _AxIpNatLsnPoolNameStatTcpHitFull_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 16),
    _AxIpNatLsnPoolNameStatTcpHitFull_Type()
)
axIpNatLsnPoolNameStatTcpHitFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatTcpHitFull.setStatus("current")
_AxIpNatLsnPoolNameStatUdpUsed_Type = CounterBasedGauge64
_AxIpNatLsnPoolNameStatUdpUsed_Object = MibTableColumn
axIpNatLsnPoolNameStatUdpUsed = _AxIpNatLsnPoolNameStatUdpUsed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 17),
    _AxIpNatLsnPoolNameStatUdpUsed_Type()
)
axIpNatLsnPoolNameStatUdpUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatUdpUsed.setStatus("current")
_AxIpNatLsnPoolNameStatUdpFreed_Type = CounterBasedGauge64
_AxIpNatLsnPoolNameStatUdpFreed_Object = MibTableColumn
axIpNatLsnPoolNameStatUdpFreed = _AxIpNatLsnPoolNameStatUdpFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 18),
    _AxIpNatLsnPoolNameStatUdpFreed_Type()
)
axIpNatLsnPoolNameStatUdpFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatUdpFreed.setStatus("current")
_AxIpNatLsnPoolNameStatUdpTotal_Type = CounterBasedGauge64
_AxIpNatLsnPoolNameStatUdpTotal_Object = MibTableColumn
axIpNatLsnPoolNameStatUdpTotal = _AxIpNatLsnPoolNameStatUdpTotal_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 19),
    _AxIpNatLsnPoolNameStatUdpTotal_Type()
)
axIpNatLsnPoolNameStatUdpTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatUdpTotal.setStatus("current")
_AxIpNatLsnPoolNameStatUdpReserved_Type = CounterBasedGauge64
_AxIpNatLsnPoolNameStatUdpReserved_Object = MibTableColumn
axIpNatLsnPoolNameStatUdpReserved = _AxIpNatLsnPoolNameStatUdpReserved_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 20),
    _AxIpNatLsnPoolNameStatUdpReserved_Type()
)
axIpNatLsnPoolNameStatUdpReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatUdpReserved.setStatus("current")
_AxIpNatLsnPoolNameStatUdpPeak_Type = Counter64
_AxIpNatLsnPoolNameStatUdpPeak_Object = MibTableColumn
axIpNatLsnPoolNameStatUdpPeak = _AxIpNatLsnPoolNameStatUdpPeak_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 21),
    _AxIpNatLsnPoolNameStatUdpPeak_Type()
)
axIpNatLsnPoolNameStatUdpPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatUdpPeak.setStatus("current")
_AxIpNatLsnPoolNameStatUdpHitFull_Type = CounterBasedGauge64
_AxIpNatLsnPoolNameStatUdpHitFull_Object = MibTableColumn
axIpNatLsnPoolNameStatUdpHitFull = _AxIpNatLsnPoolNameStatUdpHitFull_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 12, 1, 22),
    _AxIpNatLsnPoolNameStatUdpHitFull_Type()
)
axIpNatLsnPoolNameStatUdpHitFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolNameStatUdpHitFull.setStatus("current")
_AxIpNatLsnPoolGroup_ObjectIdentity = ObjectIdentity
axIpNatLsnPoolGroup = _AxIpNatLsnPoolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13)
)
_AxIpNatLsnPoolGroupCount_Type = Integer32
_AxIpNatLsnPoolGroupCount_Object = MibScalar
axIpNatLsnPoolGroupCount = _AxIpNatLsnPoolGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 1),
    _AxIpNatLsnPoolGroupCount_Type()
)
axIpNatLsnPoolGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupCount.setStatus("current")
_AxIpNatLsnPoolGroupTable_Object = MibTable
axIpNatLsnPoolGroupTable = _AxIpNatLsnPoolGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2)
)
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupTable.setStatus("current")
_AxIpNatLsnPoolGroupEntry_Object = MibTableRow
axIpNatLsnPoolGroupEntry = _AxIpNatLsnPoolGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1)
)
axIpNatLsnPoolGroupEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axIpNatLsnPoolGroupName"),
)
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupEntry.setStatus("current")
_AxIpNatLsnPoolGroupName_Type = DisplayString
_AxIpNatLsnPoolGroupName_Object = MibTableColumn
axIpNatLsnPoolGroupName = _AxIpNatLsnPoolGroupName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 1),
    _AxIpNatLsnPoolGroupName_Type()
)
axIpNatLsnPoolGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupName.setStatus("current")
_AxIpNatLsnPoolGroupUsers_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupUsers_Object = MibTableColumn
axIpNatLsnPoolGroupUsers = _AxIpNatLsnPoolGroupUsers_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 2),
    _AxIpNatLsnPoolGroupUsers_Type()
)
axIpNatLsnPoolGroupUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupUsers.setStatus("current")
_AxIpNatLsnPoolGroupIcmpUsed_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupIcmpUsed_Object = MibTableColumn
axIpNatLsnPoolGroupIcmpUsed = _AxIpNatLsnPoolGroupIcmpUsed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 3),
    _AxIpNatLsnPoolGroupIcmpUsed_Type()
)
axIpNatLsnPoolGroupIcmpUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupIcmpUsed.setStatus("current")
_AxIpNatLsnPoolGroupIcmpFreed_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupIcmpFreed_Object = MibTableColumn
axIpNatLsnPoolGroupIcmpFreed = _AxIpNatLsnPoolGroupIcmpFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 4),
    _AxIpNatLsnPoolGroupIcmpFreed_Type()
)
axIpNatLsnPoolGroupIcmpFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupIcmpFreed.setStatus("current")
_AxIpNatLsnPoolGroupIcmpTotal_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupIcmpTotal_Object = MibTableColumn
axIpNatLsnPoolGroupIcmpTotal = _AxIpNatLsnPoolGroupIcmpTotal_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 5),
    _AxIpNatLsnPoolGroupIcmpTotal_Type()
)
axIpNatLsnPoolGroupIcmpTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupIcmpTotal.setStatus("current")
_AxIpNatLsnPoolGroupIcmpReserved_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupIcmpReserved_Object = MibTableColumn
axIpNatLsnPoolGroupIcmpReserved = _AxIpNatLsnPoolGroupIcmpReserved_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 6),
    _AxIpNatLsnPoolGroupIcmpReserved_Type()
)
axIpNatLsnPoolGroupIcmpReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupIcmpReserved.setStatus("current")
_AxIpNatLsnPoolGroupIcmpPeak_Type = Counter64
_AxIpNatLsnPoolGroupIcmpPeak_Object = MibTableColumn
axIpNatLsnPoolGroupIcmpPeak = _AxIpNatLsnPoolGroupIcmpPeak_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 7),
    _AxIpNatLsnPoolGroupIcmpPeak_Type()
)
axIpNatLsnPoolGroupIcmpPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupIcmpPeak.setStatus("current")
_AxIpNatLsnPoolGroupIcmpHitFull_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupIcmpHitFull_Object = MibTableColumn
axIpNatLsnPoolGroupIcmpHitFull = _AxIpNatLsnPoolGroupIcmpHitFull_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 8),
    _AxIpNatLsnPoolGroupIcmpHitFull_Type()
)
axIpNatLsnPoolGroupIcmpHitFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupIcmpHitFull.setStatus("current")
_AxIpNatLsnPoolGroupTcpUsed_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupTcpUsed_Object = MibTableColumn
axIpNatLsnPoolGroupTcpUsed = _AxIpNatLsnPoolGroupTcpUsed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 9),
    _AxIpNatLsnPoolGroupTcpUsed_Type()
)
axIpNatLsnPoolGroupTcpUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupTcpUsed.setStatus("current")
_AxIpNatLsnPoolGroupTcpFreed_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupTcpFreed_Object = MibTableColumn
axIpNatLsnPoolGroupTcpFreed = _AxIpNatLsnPoolGroupTcpFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 10),
    _AxIpNatLsnPoolGroupTcpFreed_Type()
)
axIpNatLsnPoolGroupTcpFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupTcpFreed.setStatus("current")
_AxIpNatLsnPoolGroupTcpTotal_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupTcpTotal_Object = MibTableColumn
axIpNatLsnPoolGroupTcpTotal = _AxIpNatLsnPoolGroupTcpTotal_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 11),
    _AxIpNatLsnPoolGroupTcpTotal_Type()
)
axIpNatLsnPoolGroupTcpTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupTcpTotal.setStatus("current")
_AxIpNatLsnPoolGroupTcpReserved_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupTcpReserved_Object = MibTableColumn
axIpNatLsnPoolGroupTcpReserved = _AxIpNatLsnPoolGroupTcpReserved_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 12),
    _AxIpNatLsnPoolGroupTcpReserved_Type()
)
axIpNatLsnPoolGroupTcpReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupTcpReserved.setStatus("current")
_AxIpNatLsnPoolGroupTcpPeak_Type = Counter64
_AxIpNatLsnPoolGroupTcpPeak_Object = MibTableColumn
axIpNatLsnPoolGroupTcpPeak = _AxIpNatLsnPoolGroupTcpPeak_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 13),
    _AxIpNatLsnPoolGroupTcpPeak_Type()
)
axIpNatLsnPoolGroupTcpPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupTcpPeak.setStatus("current")
_AxIpNatLsnPoolGroupTcpHitFull_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupTcpHitFull_Object = MibTableColumn
axIpNatLsnPoolGroupTcpHitFull = _AxIpNatLsnPoolGroupTcpHitFull_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 14),
    _AxIpNatLsnPoolGroupTcpHitFull_Type()
)
axIpNatLsnPoolGroupTcpHitFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupTcpHitFull.setStatus("current")
_AxIpNatLsnPoolGroupUdpUsed_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupUdpUsed_Object = MibTableColumn
axIpNatLsnPoolGroupUdpUsed = _AxIpNatLsnPoolGroupUdpUsed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 15),
    _AxIpNatLsnPoolGroupUdpUsed_Type()
)
axIpNatLsnPoolGroupUdpUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupUdpUsed.setStatus("current")
_AxIpNatLsnPoolGroupUdpFreed_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupUdpFreed_Object = MibTableColumn
axIpNatLsnPoolGroupUdpFreed = _AxIpNatLsnPoolGroupUdpFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 16),
    _AxIpNatLsnPoolGroupUdpFreed_Type()
)
axIpNatLsnPoolGroupUdpFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupUdpFreed.setStatus("current")
_AxIpNatLsnPoolGroupUdpTotal_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupUdpTotal_Object = MibTableColumn
axIpNatLsnPoolGroupUdpTotal = _AxIpNatLsnPoolGroupUdpTotal_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 17),
    _AxIpNatLsnPoolGroupUdpTotal_Type()
)
axIpNatLsnPoolGroupUdpTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupUdpTotal.setStatus("current")
_AxIpNatLsnPoolGroupUdpReserved_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupUdpReserved_Object = MibTableColumn
axIpNatLsnPoolGroupUdpReserved = _AxIpNatLsnPoolGroupUdpReserved_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 18),
    _AxIpNatLsnPoolGroupUdpReserved_Type()
)
axIpNatLsnPoolGroupUdpReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupUdpReserved.setStatus("current")
_AxIpNatLsnPoolGroupUdpPeak_Type = Counter64
_AxIpNatLsnPoolGroupUdpPeak_Object = MibTableColumn
axIpNatLsnPoolGroupUdpPeak = _AxIpNatLsnPoolGroupUdpPeak_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 19),
    _AxIpNatLsnPoolGroupUdpPeak_Type()
)
axIpNatLsnPoolGroupUdpPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupUdpPeak.setStatus("current")
_AxIpNatLsnPoolGroupUdpHitFull_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupUdpHitFull_Object = MibTableColumn
axIpNatLsnPoolGroupUdpHitFull = _AxIpNatLsnPoolGroupUdpHitFull_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 20),
    _AxIpNatLsnPoolGroupUdpHitFull_Type()
)
axIpNatLsnPoolGroupUdpHitFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupUdpHitFull.setStatus("current")
_AxIpNatLsnPoolGroupTotalIp_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupTotalIp_Object = MibTableColumn
axIpNatLsnPoolGroupTotalIp = _AxIpNatLsnPoolGroupTotalIp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 21),
    _AxIpNatLsnPoolGroupTotalIp_Type()
)
axIpNatLsnPoolGroupTotalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupTotalIp.setStatus("current")
_AxIpNatLsnPoolGroupUsedIp_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupUsedIp_Object = MibTableColumn
axIpNatLsnPoolGroupUsedIp = _AxIpNatLsnPoolGroupUsedIp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 22),
    _AxIpNatLsnPoolGroupUsedIp_Type()
)
axIpNatLsnPoolGroupUsedIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupUsedIp.setStatus("current")
_AxIpNatLsnPoolGroupFreedIp_Type = CounterBasedGauge64
_AxIpNatLsnPoolGroupFreedIp_Object = MibTableColumn
axIpNatLsnPoolGroupFreedIp = _AxIpNatLsnPoolGroupFreedIp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 14, 13, 2, 1, 23),
    _AxIpNatLsnPoolGroupFreedIp_Type()
)
axIpNatLsnPoolGroupFreedIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnPoolGroupFreedIp.setStatus("current")
_AxIpNatLsnRadiusStats_ObjectIdentity = ObjectIdentity
axIpNatLsnRadiusStats = _AxIpNatLsnRadiusStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 15)
)
_AxIpNatLsnMSISDNReceived_Type = CounterBasedGauge64
_AxIpNatLsnMSISDNReceived_Object = MibScalar
axIpNatLsnMSISDNReceived = _AxIpNatLsnMSISDNReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 15, 1),
    _AxIpNatLsnMSISDNReceived_Type()
)
axIpNatLsnMSISDNReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnMSISDNReceived.setStatus("current")
_AxIpNatLsnRadiusIMEIReceived_Type = CounterBasedGauge64
_AxIpNatLsnRadiusIMEIReceived_Object = MibScalar
axIpNatLsnRadiusIMEIReceived = _AxIpNatLsnRadiusIMEIReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 15, 2),
    _AxIpNatLsnRadiusIMEIReceived_Type()
)
axIpNatLsnRadiusIMEIReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnRadiusIMEIReceived.setStatus("current")
_AxIpNatLsnRadiusIMSIReceived_Type = CounterBasedGauge64
_AxIpNatLsnRadiusIMSIReceived_Object = MibScalar
axIpNatLsnRadiusIMSIReceived = _AxIpNatLsnRadiusIMSIReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 15, 3),
    _AxIpNatLsnRadiusIMSIReceived_Type()
)
axIpNatLsnRadiusIMSIReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnRadiusIMSIReceived.setStatus("current")
_AxIpNatLsnCustAttrReceived_Type = CounterBasedGauge64
_AxIpNatLsnCustAttrReceived_Object = MibScalar
axIpNatLsnCustAttrReceived = _AxIpNatLsnCustAttrReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 15, 4),
    _AxIpNatLsnCustAttrReceived_Type()
)
axIpNatLsnCustAttrReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnCustAttrReceived.setStatus("current")
_AxIpNatLsnRadiusRequestReceived_Type = CounterBasedGauge64
_AxIpNatLsnRadiusRequestReceived_Object = MibScalar
axIpNatLsnRadiusRequestReceived = _AxIpNatLsnRadiusRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 15, 5),
    _AxIpNatLsnRadiusRequestReceived_Type()
)
axIpNatLsnRadiusRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnRadiusRequestReceived.setStatus("current")
_AxIpNatLsnRadiusRequestBadSecretDropped_Type = CounterBasedGauge64
_AxIpNatLsnRadiusRequestBadSecretDropped_Object = MibScalar
axIpNatLsnRadiusRequestBadSecretDropped = _AxIpNatLsnRadiusRequestBadSecretDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 15, 6),
    _AxIpNatLsnRadiusRequestBadSecretDropped_Type()
)
axIpNatLsnRadiusRequestBadSecretDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnRadiusRequestBadSecretDropped.setStatus("current")
_AxIpNatLsnRadiusRequestNoKeyAttrDropped_Type = CounterBasedGauge64
_AxIpNatLsnRadiusRequestNoKeyAttrDropped_Object = MibScalar
axIpNatLsnRadiusRequestNoKeyAttrDropped = _AxIpNatLsnRadiusRequestNoKeyAttrDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 15, 7),
    _AxIpNatLsnRadiusRequestNoKeyAttrDropped_Type()
)
axIpNatLsnRadiusRequestNoKeyAttrDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnRadiusRequestNoKeyAttrDropped.setStatus("current")
_AxIpNatLsnRadiusRequestMalFormedDropped_Type = CounterBasedGauge64
_AxIpNatLsnRadiusRequestMalFormedDropped_Object = MibScalar
axIpNatLsnRadiusRequestMalFormedDropped = _AxIpNatLsnRadiusRequestMalFormedDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 15, 8),
    _AxIpNatLsnRadiusRequestMalFormedDropped_Type()
)
axIpNatLsnRadiusRequestMalFormedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnRadiusRequestMalFormedDropped.setStatus("current")
_AxIpNatLsnRadiusRequestIgnored_Type = CounterBasedGauge64
_AxIpNatLsnRadiusRequestIgnored_Object = MibScalar
axIpNatLsnRadiusRequestIgnored = _AxIpNatLsnRadiusRequestIgnored_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 15, 9),
    _AxIpNatLsnRadiusRequestIgnored_Type()
)
axIpNatLsnRadiusRequestIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnRadiusRequestIgnored.setStatus("current")
_AxIpNatLsnRadiusRequestTableFullDropped_Type = CounterBasedGauge64
_AxIpNatLsnRadiusRequestTableFullDropped_Object = MibScalar
axIpNatLsnRadiusRequestTableFullDropped = _AxIpNatLsnRadiusRequestTableFullDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 15, 10),
    _AxIpNatLsnRadiusRequestTableFullDropped_Type()
)
axIpNatLsnRadiusRequestTableFullDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnRadiusRequestTableFullDropped.setStatus("current")
_AxIpNatLsnHAStandbyDropped_Type = CounterBasedGauge64
_AxIpNatLsnHAStandbyDropped_Object = MibScalar
axIpNatLsnHAStandbyDropped = _AxIpNatLsnHAStandbyDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 15, 11),
    _AxIpNatLsnHAStandbyDropped_Type()
)
axIpNatLsnHAStandbyDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnHAStandbyDropped.setStatus("current")
_AxIpNatLsnRadiusSecretNotConfigDropped_Type = CounterBasedGauge64
_AxIpNatLsnRadiusSecretNotConfigDropped_Object = MibScalar
axIpNatLsnRadiusSecretNotConfigDropped = _AxIpNatLsnRadiusSecretNotConfigDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 4, 15, 12),
    _AxIpNatLsnRadiusSecretNotConfigDropped_Type()
)
axIpNatLsnRadiusSecretNotConfigDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLsnRadiusSecretNotConfigDropped.setStatus("current")
_AxIpNatNat64StatsGlobal_ObjectIdentity = ObjectIdentity
axIpNatNat64StatsGlobal = _AxIpNatNat64StatsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1)
)
_AxIpNatNat64StatTotalTcpPortAlloc_Type = Counter64
_AxIpNatNat64StatTotalTcpPortAlloc_Object = MibScalar
axIpNatNat64StatTotalTcpPortAlloc = _AxIpNatNat64StatTotalTcpPortAlloc_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 1),
    _AxIpNatNat64StatTotalTcpPortAlloc_Type()
)
axIpNatNat64StatTotalTcpPortAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatTotalTcpPortAlloc.setStatus("current")
_AxIpNatNat64StatTotalTcpPortFreed_Type = Counter64
_AxIpNatNat64StatTotalTcpPortFreed_Object = MibScalar
axIpNatNat64StatTotalTcpPortFreed = _AxIpNatNat64StatTotalTcpPortFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 2),
    _AxIpNatNat64StatTotalTcpPortFreed_Type()
)
axIpNatNat64StatTotalTcpPortFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatTotalTcpPortFreed.setStatus("current")
_AxIpNatNat64StatTotalUdpPortAlloc_Type = Counter64
_AxIpNatNat64StatTotalUdpPortAlloc_Object = MibScalar
axIpNatNat64StatTotalUdpPortAlloc = _AxIpNatNat64StatTotalUdpPortAlloc_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 3),
    _AxIpNatNat64StatTotalUdpPortAlloc_Type()
)
axIpNatNat64StatTotalUdpPortAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatTotalUdpPortAlloc.setStatus("current")
_AxIpNatNat64StatTotalUdpPortFreed_Type = Counter64
_AxIpNatNat64StatTotalUdpPortFreed_Object = MibScalar
axIpNatNat64StatTotalUdpPortFreed = _AxIpNatNat64StatTotalUdpPortFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 4),
    _AxIpNatNat64StatTotalUdpPortFreed_Type()
)
axIpNatNat64StatTotalUdpPortFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatTotalUdpPortFreed.setStatus("current")
_AxIpNatNat64StatTotalIcmpPortAlloc_Type = Counter64
_AxIpNatNat64StatTotalIcmpPortAlloc_Object = MibScalar
axIpNatNat64StatTotalIcmpPortAlloc = _AxIpNatNat64StatTotalIcmpPortAlloc_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 5),
    _AxIpNatNat64StatTotalIcmpPortAlloc_Type()
)
axIpNatNat64StatTotalIcmpPortAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatTotalIcmpPortAlloc.setStatus("current")
_AxIpNatNat64StatTotalIcmpPortFreed_Type = Counter64
_AxIpNatNat64StatTotalIcmpPortFreed_Object = MibScalar
axIpNatNat64StatTotalIcmpPortFreed = _AxIpNatNat64StatTotalIcmpPortFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 6),
    _AxIpNatNat64StatTotalIcmpPortFreed_Type()
)
axIpNatNat64StatTotalIcmpPortFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatTotalIcmpPortFreed.setStatus("current")
_AxIpNatNat64StatDataSessionCreated_Type = Counter64
_AxIpNatNat64StatDataSessionCreated_Object = MibScalar
axIpNatNat64StatDataSessionCreated = _AxIpNatNat64StatDataSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 7),
    _AxIpNatNat64StatDataSessionCreated_Type()
)
axIpNatNat64StatDataSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatDataSessionCreated.setStatus("current")
_AxIpNatNat64StatDataSessionFreed_Type = Counter64
_AxIpNatNat64StatDataSessionFreed_Object = MibScalar
axIpNatNat64StatDataSessionFreed = _AxIpNatNat64StatDataSessionFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 8),
    _AxIpNatNat64StatDataSessionFreed_Type()
)
axIpNatNat64StatDataSessionFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatDataSessionFreed.setStatus("current")
_AxIpNatNat64UserQuotaCreated_Type = Counter64
_AxIpNatNat64UserQuotaCreated_Object = MibScalar
axIpNatNat64UserQuotaCreated = _AxIpNatNat64UserQuotaCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 9),
    _AxIpNatNat64UserQuotaCreated_Type()
)
axIpNatNat64UserQuotaCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64UserQuotaCreated.setStatus("current")
_AxIpNatNat64UserQuotaFreed_Type = Counter64
_AxIpNatNat64UserQuotaFreed_Object = MibScalar
axIpNatNat64UserQuotaFreed = _AxIpNatNat64UserQuotaFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 10),
    _AxIpNatNat64UserQuotaFreed_Type()
)
axIpNatNat64UserQuotaFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64UserQuotaFreed.setStatus("current")
_AxIpNatNat64UserQuotaCreateFailed_Type = Counter64
_AxIpNatNat64UserQuotaCreateFailed_Object = MibScalar
axIpNatNat64UserQuotaCreateFailed = _AxIpNatNat64UserQuotaCreateFailed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 11),
    _AxIpNatNat64UserQuotaCreateFailed_Type()
)
axIpNatNat64UserQuotaCreateFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64UserQuotaCreateFailed.setStatus("current")
_AxIpNatNat64StatTcpNatPortUnAvail_Type = Counter64
_AxIpNatNat64StatTcpNatPortUnAvail_Object = MibScalar
axIpNatNat64StatTcpNatPortUnAvail = _AxIpNatNat64StatTcpNatPortUnAvail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 12),
    _AxIpNatNat64StatTcpNatPortUnAvail_Type()
)
axIpNatNat64StatTcpNatPortUnAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatTcpNatPortUnAvail.setStatus("current")
_AxIpNatNat64StatUdpNatPortUnAvail_Type = Counter64
_AxIpNatNat64StatUdpNatPortUnAvail_Object = MibScalar
axIpNatNat64StatUdpNatPortUnAvail = _AxIpNatNat64StatUdpNatPortUnAvail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 13),
    _AxIpNatNat64StatUdpNatPortUnAvail_Type()
)
axIpNatNat64StatUdpNatPortUnAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatUdpNatPortUnAvail.setStatus("current")
_AxIpNatNat64StatIcmpNatPortUnavail_Type = Counter64
_AxIpNatNat64StatIcmpNatPortUnavail_Object = MibScalar
axIpNatNat64StatIcmpNatPortUnavail = _AxIpNatNat64StatIcmpNatPortUnavail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 14),
    _AxIpNatNat64StatIcmpNatPortUnavail_Type()
)
axIpNatNat64StatIcmpNatPortUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatIcmpNatPortUnavail.setStatus("current")
_AxIpNatNat64StatNewUserResourceUnAvail_Type = Counter64
_AxIpNatNat64StatNewUserResourceUnAvail_Object = MibScalar
axIpNatNat64StatNewUserResourceUnAvail = _AxIpNatNat64StatNewUserResourceUnAvail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 15),
    _AxIpNatNat64StatNewUserResourceUnAvail_Type()
)
axIpNatNat64StatNewUserResourceUnAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatNewUserResourceUnAvail.setStatus("current")
_AxIpNatNat64StatTcpUserQuotaExceed_Type = Counter64
_AxIpNatNat64StatTcpUserQuotaExceed_Object = MibScalar
axIpNatNat64StatTcpUserQuotaExceed = _AxIpNatNat64StatTcpUserQuotaExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 16),
    _AxIpNatNat64StatTcpUserQuotaExceed_Type()
)
axIpNatNat64StatTcpUserQuotaExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatTcpUserQuotaExceed.setStatus("current")
_AxIpNatNat64StatUdpUserQuotaExceed_Type = Counter64
_AxIpNatNat64StatUdpUserQuotaExceed_Object = MibScalar
axIpNatNat64StatUdpUserQuotaExceed = _AxIpNatNat64StatUdpUserQuotaExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 17),
    _AxIpNatNat64StatUdpUserQuotaExceed_Type()
)
axIpNatNat64StatUdpUserQuotaExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatUdpUserQuotaExceed.setStatus("current")
_AxIpNatNat64StatIcmpUserQuotaExceed_Type = Counter64
_AxIpNatNat64StatIcmpUserQuotaExceed_Object = MibScalar
axIpNatNat64StatIcmpUserQuotaExceed = _AxIpNatNat64StatIcmpUserQuotaExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 18),
    _AxIpNatNat64StatIcmpUserQuotaExceed_Type()
)
axIpNatNat64StatIcmpUserQuotaExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatIcmpUserQuotaExceed.setStatus("current")
_AxIpNatNat64StatExtendedUserQuotaMatched_Type = Counter64
_AxIpNatNat64StatExtendedUserQuotaMatched_Object = MibScalar
axIpNatNat64StatExtendedUserQuotaMatched = _AxIpNatNat64StatExtendedUserQuotaMatched_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 19),
    _AxIpNatNat64StatExtendedUserQuotaMatched_Type()
)
axIpNatNat64StatExtendedUserQuotaMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatExtendedUserQuotaMatched.setStatus("current")
_AxIpNatNat64StatExtendedUserQuotaExceeded_Type = Counter64
_AxIpNatNat64StatExtendedUserQuotaExceeded_Object = MibScalar
axIpNatNat64StatExtendedUserQuotaExceeded = _AxIpNatNat64StatExtendedUserQuotaExceeded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 20),
    _AxIpNatNat64StatExtendedUserQuotaExceeded_Type()
)
axIpNatNat64StatExtendedUserQuotaExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatExtendedUserQuotaExceeded.setStatus("current")
_AxIpNatNat64StatTcpFullConeSessionCreated_Type = Counter64
_AxIpNatNat64StatTcpFullConeSessionCreated_Object = MibScalar
axIpNatNat64StatTcpFullConeSessionCreated = _AxIpNatNat64StatTcpFullConeSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 21),
    _AxIpNatNat64StatTcpFullConeSessionCreated_Type()
)
axIpNatNat64StatTcpFullConeSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatTcpFullConeSessionCreated.setStatus("current")
_AxIpNatNat64StatTcpFullConeSessionFreed_Type = Counter64
_AxIpNatNat64StatTcpFullConeSessionFreed_Object = MibScalar
axIpNatNat64StatTcpFullConeSessionFreed = _AxIpNatNat64StatTcpFullConeSessionFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 22),
    _AxIpNatNat64StatTcpFullConeSessionFreed_Type()
)
axIpNatNat64StatTcpFullConeSessionFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatTcpFullConeSessionFreed.setStatus("current")
_AxIpNatNat64StatUdpFullConeSessionCreated_Type = Counter64
_AxIpNatNat64StatUdpFullConeSessionCreated_Object = MibScalar
axIpNatNat64StatUdpFullConeSessionCreated = _AxIpNatNat64StatUdpFullConeSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 23),
    _AxIpNatNat64StatUdpFullConeSessionCreated_Type()
)
axIpNatNat64StatUdpFullConeSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatUdpFullConeSessionCreated.setStatus("current")
_AxIpNatNat64StatUdpFullConeSessionFreed_Type = Counter64
_AxIpNatNat64StatUdpFullConeSessionFreed_Object = MibScalar
axIpNatNat64StatUdpFullConeSessionFreed = _AxIpNatNat64StatUdpFullConeSessionFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 24),
    _AxIpNatNat64StatUdpFullConeSessionFreed_Type()
)
axIpNatNat64StatUdpFullConeSessionFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatUdpFullConeSessionFreed.setStatus("current")
_AxIpNatNat64StatFullConeSessionFailed_Type = Counter64
_AxIpNatNat64StatFullConeSessionFailed_Object = MibScalar
axIpNatNat64StatFullConeSessionFailed = _AxIpNatNat64StatFullConeSessionFailed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 25),
    _AxIpNatNat64StatFullConeSessionFailed_Type()
)
axIpNatNat64StatFullConeSessionFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatFullConeSessionFailed.setStatus("current")
_AxIpNatNat64StatHairpinSessionCreated_Type = Counter64
_AxIpNatNat64StatHairpinSessionCreated_Object = MibScalar
axIpNatNat64StatHairpinSessionCreated = _AxIpNatNat64StatHairpinSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 26),
    _AxIpNatNat64StatHairpinSessionCreated_Type()
)
axIpNatNat64StatHairpinSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatHairpinSessionCreated.setStatus("current")
_AxIpNatNat64StatSelfHairpinDrop_Type = Counter64
_AxIpNatNat64StatSelfHairpinDrop_Object = MibScalar
axIpNatNat64StatSelfHairpinDrop = _AxIpNatNat64StatSelfHairpinDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 27),
    _AxIpNatNat64StatSelfHairpinDrop_Type()
)
axIpNatNat64StatSelfHairpinDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatSelfHairpinDrop.setStatus("current")
_AxIpNatNat64StatEndpointIndependentMapMatched_Type = Counter64
_AxIpNatNat64StatEndpointIndependentMapMatched_Object = MibScalar
axIpNatNat64StatEndpointIndependentMapMatched = _AxIpNatNat64StatEndpointIndependentMapMatched_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 28),
    _AxIpNatNat64StatEndpointIndependentMapMatched_Type()
)
axIpNatNat64StatEndpointIndependentMapMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatEndpointIndependentMapMatched.setStatus("current")
_AxIpNatNat64StatEndpointIndependentFilterMatched_Type = Counter64
_AxIpNatNat64StatEndpointIndependentFilterMatched_Object = MibScalar
axIpNatNat64StatEndpointIndependentFilterMatched = _AxIpNatNat64StatEndpointIndependentFilterMatched_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 29),
    _AxIpNatNat64StatEndpointIndependentFilterMatched_Type()
)
axIpNatNat64StatEndpointIndependentFilterMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatEndpointIndependentFilterMatched.setStatus("current")
_AxIpNatNat64StatEndpointDependentFilterDrop_Type = Counter64
_AxIpNatNat64StatEndpointDependentFilterDrop_Object = MibScalar
axIpNatNat64StatEndpointDependentFilterDrop = _AxIpNatNat64StatEndpointDependentFilterDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 30),
    _AxIpNatNat64StatEndpointDependentFilterDrop_Type()
)
axIpNatNat64StatEndpointDependentFilterDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatEndpointDependentFilterDrop.setStatus("current")
_AxIpNatNat64StatLayer3ForwardPackets_Type = Counter64
_AxIpNatNat64StatLayer3ForwardPackets_Object = MibScalar
axIpNatNat64StatLayer3ForwardPackets = _AxIpNatNat64StatLayer3ForwardPackets_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 31),
    _AxIpNatNat64StatLayer3ForwardPackets_Type()
)
axIpNatNat64StatLayer3ForwardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatLayer3ForwardPackets.setStatus("current")
_AxIpNatNat64StatSourceAddrPrefixMatchDrop_Type = Counter64
_AxIpNatNat64StatSourceAddrPrefixMatchDrop_Object = MibScalar
axIpNatNat64StatSourceAddrPrefixMatchDrop = _AxIpNatNat64StatSourceAddrPrefixMatchDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 32),
    _AxIpNatNat64StatSourceAddrPrefixMatchDrop_Type()
)
axIpNatNat64StatSourceAddrPrefixMatchDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatSourceAddrPrefixMatchDrop.setStatus("current")
_AxIpNatNat64StatLsnLidDrop_Type = Counter64
_AxIpNatNat64StatLsnLidDrop_Object = MibScalar
axIpNatNat64StatLsnLidDrop = _AxIpNatNat64StatLsnLidDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 33),
    _AxIpNatNat64StatLsnLidDrop_Type()
)
axIpNatNat64StatLsnLidDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatLsnLidDrop.setStatus("current")
_AxIpNatNat64StatLsnLidPassThrough_Type = Counter64
_AxIpNatNat64StatLsnLidPassThrough_Object = MibScalar
axIpNatNat64StatLsnLidPassThrough = _AxIpNatNat64StatLsnLidPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 34),
    _AxIpNatNat64StatLsnLidPassThrough_Type()
)
axIpNatNat64StatLsnLidPassThrough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatLsnLidPassThrough.setStatus("current")
_AxIpNatNat64StatNoClassListMatch_Type = Counter64
_AxIpNatNat64StatNoClassListMatch_Object = MibScalar
axIpNatNat64StatNoClassListMatch = _AxIpNatNat64StatNoClassListMatch_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 35),
    _AxIpNatNat64StatNoClassListMatch_Type()
)
axIpNatNat64StatNoClassListMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatNoClassListMatch.setStatus("current")
_AxIpNatNat64StatNatPoolMismatchDrop_Type = Counter64
_AxIpNatNat64StatNatPoolMismatchDrop_Object = MibScalar
axIpNatNat64StatNatPoolMismatchDrop = _AxIpNatNat64StatNatPoolMismatchDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 36),
    _AxIpNatNat64StatNatPoolMismatchDrop_Type()
)
axIpNatNat64StatNatPoolMismatchDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatNatPoolMismatchDrop.setStatus("current")
_AxIpNatNat64StatDataSessionUserQuotaExceeded_Type = Counter64
_AxIpNatNat64StatDataSessionUserQuotaExceeded_Object = MibScalar
axIpNatNat64StatDataSessionUserQuotaExceeded = _AxIpNatNat64StatDataSessionUserQuotaExceeded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 37),
    _AxIpNatNat64StatDataSessionUserQuotaExceeded_Type()
)
axIpNatNat64StatDataSessionUserQuotaExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatDataSessionUserQuotaExceeded.setStatus("current")
_AxIpNatNat64StatConnRateUserQuotaExceeded_Type = Counter64
_AxIpNatNat64StatConnRateUserQuotaExceeded_Object = MibScalar
axIpNatNat64StatConnRateUserQuotaExceeded = _AxIpNatNat64StatConnRateUserQuotaExceeded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 38),
    _AxIpNatNat64StatConnRateUserQuotaExceeded_Type()
)
axIpNatNat64StatConnRateUserQuotaExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatConnRateUserQuotaExceeded.setStatus("current")
_AxIpNatNat64StatEndPointIndependentFilteringInboundLimitExceeded_Type = Counter64
_AxIpNatNat64StatEndPointIndependentFilteringInboundLimitExceeded_Object = MibScalar
axIpNatNat64StatEndPointIndependentFilteringInboundLimitExceeded = _AxIpNatNat64StatEndPointIndependentFilteringInboundLimitExceeded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 39),
    _AxIpNatNat64StatEndPointIndependentFilteringInboundLimitExceeded_Type()
)
axIpNatNat64StatEndPointIndependentFilteringInboundLimitExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatEndPointIndependentFilteringInboundLimitExceeded.setStatus("current")
_AxIpNatNat64StatTcpPortOverloaded_Type = Counter64
_AxIpNatNat64StatTcpPortOverloaded_Object = MibScalar
axIpNatNat64StatTcpPortOverloaded = _AxIpNatNat64StatTcpPortOverloaded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 40),
    _AxIpNatNat64StatTcpPortOverloaded_Type()
)
axIpNatNat64StatTcpPortOverloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatTcpPortOverloaded.setStatus("current")
_AxIpNatNat64StatUdpPortOverloaded_Type = Counter64
_AxIpNatNat64StatUdpPortOverloaded_Object = MibScalar
axIpNatNat64StatUdpPortOverloaded = _AxIpNatNat64StatUdpPortOverloaded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 41),
    _AxIpNatNat64StatUdpPortOverloaded_Type()
)
axIpNatNat64StatUdpPortOverloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatUdpPortOverloaded.setStatus("current")
_AxIpNatNat64StatTcpPortOverloadingSessionCreated_Type = Counter64
_AxIpNatNat64StatTcpPortOverloadingSessionCreated_Object = MibScalar
axIpNatNat64StatTcpPortOverloadingSessionCreated = _AxIpNatNat64StatTcpPortOverloadingSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 42),
    _AxIpNatNat64StatTcpPortOverloadingSessionCreated_Type()
)
axIpNatNat64StatTcpPortOverloadingSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatTcpPortOverloadingSessionCreated.setStatus("current")
_AxIpNatNat64StatUdpPortOverloadingSessionCreated_Type = Counter64
_AxIpNatNat64StatUdpPortOverloadingSessionCreated_Object = MibScalar
axIpNatNat64StatUdpPortOverloadingSessionCreated = _AxIpNatNat64StatUdpPortOverloadingSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 43),
    _AxIpNatNat64StatUdpPortOverloadingSessionCreated_Type()
)
axIpNatNat64StatUdpPortOverloadingSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatUdpPortOverloadingSessionCreated.setStatus("current")
_AxIpNatNat64StatTcpPortOverloadingSessionFreed_Type = Counter64
_AxIpNatNat64StatTcpPortOverloadingSessionFreed_Object = MibScalar
axIpNatNat64StatTcpPortOverloadingSessionFreed = _AxIpNatNat64StatTcpPortOverloadingSessionFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 44),
    _AxIpNatNat64StatTcpPortOverloadingSessionFreed_Type()
)
axIpNatNat64StatTcpPortOverloadingSessionFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatTcpPortOverloadingSessionFreed.setStatus("current")
_AxIpNatNat64StatUdpPortOverloadingSessionFreed_Type = Counter64
_AxIpNatNat64StatUdpPortOverloadingSessionFreed_Object = MibScalar
axIpNatNat64StatUdpPortOverloadingSessionFreed = _AxIpNatNat64StatUdpPortOverloadingSessionFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 45),
    _AxIpNatNat64StatUdpPortOverloadingSessionFreed_Type()
)
axIpNatNat64StatUdpPortOverloadingSessionFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatUdpPortOverloadingSessionFreed.setStatus("current")
_AxIpNatNat64StatNatPoolUnusable_Type = Counter64
_AxIpNatNat64StatNatPoolUnusable_Object = MibScalar
axIpNatNat64StatNatPoolUnusable = _AxIpNatNat64StatNatPoolUnusable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 46),
    _AxIpNatNat64StatNatPoolUnusable_Type()
)
axIpNatNat64StatNatPoolUnusable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatNatPoolUnusable.setStatus("current")
_AxIpNatNat64StatHANatPoolUnusable_Type = Counter64
_AxIpNatNat64StatHANatPoolUnusable_Object = MibScalar
axIpNatNat64StatHANatPoolUnusable = _AxIpNatNat64StatHANatPoolUnusable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 47),
    _AxIpNatNat64StatHANatPoolUnusable_Type()
)
axIpNatNat64StatHANatPoolUnusable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatHANatPoolUnusable.setStatus("current")
_AxIpNatNat64StatNoRadiusProfileMatch_Type = Counter64
_AxIpNatNat64StatNoRadiusProfileMatch_Object = MibScalar
axIpNatNat64StatNoRadiusProfileMatch = _AxIpNatNat64StatNoRadiusProfileMatch_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 5, 1, 48),
    _AxIpNatNat64StatNoRadiusProfileMatch_Type()
)
axIpNatNat64StatNoRadiusProfileMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatNat64StatNoRadiusProfileMatch.setStatus("current")
_AxIpNatDsliteStatsGlobal_ObjectIdentity = ObjectIdentity
axIpNatDsliteStatsGlobal = _AxIpNatDsliteStatsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1)
)
_AxIpNatDsliteStatTotalTcpPortAlloc_Type = Counter64
_AxIpNatDsliteStatTotalTcpPortAlloc_Object = MibScalar
axIpNatDsliteStatTotalTcpPortAlloc = _AxIpNatDsliteStatTotalTcpPortAlloc_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 1),
    _AxIpNatDsliteStatTotalTcpPortAlloc_Type()
)
axIpNatDsliteStatTotalTcpPortAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatTotalTcpPortAlloc.setStatus("current")
_AxIpNatDsliteStatTotalTcpPortFreed_Type = Counter64
_AxIpNatDsliteStatTotalTcpPortFreed_Object = MibScalar
axIpNatDsliteStatTotalTcpPortFreed = _AxIpNatDsliteStatTotalTcpPortFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 2),
    _AxIpNatDsliteStatTotalTcpPortFreed_Type()
)
axIpNatDsliteStatTotalTcpPortFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatTotalTcpPortFreed.setStatus("current")
_AxIpNatDsliteStatTotalUdpPortAlloc_Type = Counter64
_AxIpNatDsliteStatTotalUdpPortAlloc_Object = MibScalar
axIpNatDsliteStatTotalUdpPortAlloc = _AxIpNatDsliteStatTotalUdpPortAlloc_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 3),
    _AxIpNatDsliteStatTotalUdpPortAlloc_Type()
)
axIpNatDsliteStatTotalUdpPortAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatTotalUdpPortAlloc.setStatus("current")
_AxIpNatDsliteStatTotalUdpPortFreed_Type = Counter64
_AxIpNatDsliteStatTotalUdpPortFreed_Object = MibScalar
axIpNatDsliteStatTotalUdpPortFreed = _AxIpNatDsliteStatTotalUdpPortFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 4),
    _AxIpNatDsliteStatTotalUdpPortFreed_Type()
)
axIpNatDsliteStatTotalUdpPortFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatTotalUdpPortFreed.setStatus("current")
_AxIpNatDsliteStatTotalIcmpPortAlloc_Type = Counter64
_AxIpNatDsliteStatTotalIcmpPortAlloc_Object = MibScalar
axIpNatDsliteStatTotalIcmpPortAlloc = _AxIpNatDsliteStatTotalIcmpPortAlloc_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 5),
    _AxIpNatDsliteStatTotalIcmpPortAlloc_Type()
)
axIpNatDsliteStatTotalIcmpPortAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatTotalIcmpPortAlloc.setStatus("current")
_AxIpNatDsliteStatTotalIcmpPortFreed_Type = Counter64
_AxIpNatDsliteStatTotalIcmpPortFreed_Object = MibScalar
axIpNatDsliteStatTotalIcmpPortFreed = _AxIpNatDsliteStatTotalIcmpPortFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 6),
    _AxIpNatDsliteStatTotalIcmpPortFreed_Type()
)
axIpNatDsliteStatTotalIcmpPortFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatTotalIcmpPortFreed.setStatus("current")
_AxIpNatDsliteStatDataSessionCreated_Type = Counter64
_AxIpNatDsliteStatDataSessionCreated_Object = MibScalar
axIpNatDsliteStatDataSessionCreated = _AxIpNatDsliteStatDataSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 7),
    _AxIpNatDsliteStatDataSessionCreated_Type()
)
axIpNatDsliteStatDataSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatDataSessionCreated.setStatus("current")
_AxIpNatDsliteStatDataSessionFreed_Type = Counter64
_AxIpNatDsliteStatDataSessionFreed_Object = MibScalar
axIpNatDsliteStatDataSessionFreed = _AxIpNatDsliteStatDataSessionFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 8),
    _AxIpNatDsliteStatDataSessionFreed_Type()
)
axIpNatDsliteStatDataSessionFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatDataSessionFreed.setStatus("current")
_AxIpNatDsliteUserQuotaCreated_Type = Counter64
_AxIpNatDsliteUserQuotaCreated_Object = MibScalar
axIpNatDsliteUserQuotaCreated = _AxIpNatDsliteUserQuotaCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 9),
    _AxIpNatDsliteUserQuotaCreated_Type()
)
axIpNatDsliteUserQuotaCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteUserQuotaCreated.setStatus("current")
_AxIpNatDsliteUserQuotaFreed_Type = Counter64
_AxIpNatDsliteUserQuotaFreed_Object = MibScalar
axIpNatDsliteUserQuotaFreed = _AxIpNatDsliteUserQuotaFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 10),
    _AxIpNatDsliteUserQuotaFreed_Type()
)
axIpNatDsliteUserQuotaFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteUserQuotaFreed.setStatus("current")
_AxIpNatDsliteUserQuotaCreateFailed_Type = Counter64
_AxIpNatDsliteUserQuotaCreateFailed_Object = MibScalar
axIpNatDsliteUserQuotaCreateFailed = _AxIpNatDsliteUserQuotaCreateFailed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 11),
    _AxIpNatDsliteUserQuotaCreateFailed_Type()
)
axIpNatDsliteUserQuotaCreateFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteUserQuotaCreateFailed.setStatus("current")
_AxIpNatDsliteStatTcpNatPortUnAvail_Type = Counter64
_AxIpNatDsliteStatTcpNatPortUnAvail_Object = MibScalar
axIpNatDsliteStatTcpNatPortUnAvail = _AxIpNatDsliteStatTcpNatPortUnAvail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 12),
    _AxIpNatDsliteStatTcpNatPortUnAvail_Type()
)
axIpNatDsliteStatTcpNatPortUnAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatTcpNatPortUnAvail.setStatus("current")
_AxIpNatDsliteStatUdpNatPortUnAvail_Type = Counter64
_AxIpNatDsliteStatUdpNatPortUnAvail_Object = MibScalar
axIpNatDsliteStatUdpNatPortUnAvail = _AxIpNatDsliteStatUdpNatPortUnAvail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 13),
    _AxIpNatDsliteStatUdpNatPortUnAvail_Type()
)
axIpNatDsliteStatUdpNatPortUnAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatUdpNatPortUnAvail.setStatus("current")
_AxIpNatDsliteStatIcmpNatPortUnavail_Type = Counter64
_AxIpNatDsliteStatIcmpNatPortUnavail_Object = MibScalar
axIpNatDsliteStatIcmpNatPortUnavail = _AxIpNatDsliteStatIcmpNatPortUnavail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 14),
    _AxIpNatDsliteStatIcmpNatPortUnavail_Type()
)
axIpNatDsliteStatIcmpNatPortUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatIcmpNatPortUnavail.setStatus("current")
_AxIpNatDsliteStatNewUserResourceUnAvail_Type = Counter64
_AxIpNatDsliteStatNewUserResourceUnAvail_Object = MibScalar
axIpNatDsliteStatNewUserResourceUnAvail = _AxIpNatDsliteStatNewUserResourceUnAvail_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 15),
    _AxIpNatDsliteStatNewUserResourceUnAvail_Type()
)
axIpNatDsliteStatNewUserResourceUnAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatNewUserResourceUnAvail.setStatus("current")
_AxIpNatDsliteStatTcpUserQuotaExceed_Type = Counter64
_AxIpNatDsliteStatTcpUserQuotaExceed_Object = MibScalar
axIpNatDsliteStatTcpUserQuotaExceed = _AxIpNatDsliteStatTcpUserQuotaExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 16),
    _AxIpNatDsliteStatTcpUserQuotaExceed_Type()
)
axIpNatDsliteStatTcpUserQuotaExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatTcpUserQuotaExceed.setStatus("current")
_AxIpNatDsliteStatUdpUserQuotaExceed_Type = Counter64
_AxIpNatDsliteStatUdpUserQuotaExceed_Object = MibScalar
axIpNatDsliteStatUdpUserQuotaExceed = _AxIpNatDsliteStatUdpUserQuotaExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 17),
    _AxIpNatDsliteStatUdpUserQuotaExceed_Type()
)
axIpNatDsliteStatUdpUserQuotaExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatUdpUserQuotaExceed.setStatus("current")
_AxIpNatDsliteStatIcmpUserQuotaExceed_Type = Counter64
_AxIpNatDsliteStatIcmpUserQuotaExceed_Object = MibScalar
axIpNatDsliteStatIcmpUserQuotaExceed = _AxIpNatDsliteStatIcmpUserQuotaExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 18),
    _AxIpNatDsliteStatIcmpUserQuotaExceed_Type()
)
axIpNatDsliteStatIcmpUserQuotaExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatIcmpUserQuotaExceed.setStatus("current")
_AxIpNatDsliteStatExtendedUserQuotaMatched_Type = Counter64
_AxIpNatDsliteStatExtendedUserQuotaMatched_Object = MibScalar
axIpNatDsliteStatExtendedUserQuotaMatched = _AxIpNatDsliteStatExtendedUserQuotaMatched_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 19),
    _AxIpNatDsliteStatExtendedUserQuotaMatched_Type()
)
axIpNatDsliteStatExtendedUserQuotaMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatExtendedUserQuotaMatched.setStatus("current")
_AxIpNatDsliteStatExtendedUserQuotaExceeded_Type = Counter64
_AxIpNatDsliteStatExtendedUserQuotaExceeded_Object = MibScalar
axIpNatDsliteStatExtendedUserQuotaExceeded = _AxIpNatDsliteStatExtendedUserQuotaExceeded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 20),
    _AxIpNatDsliteStatExtendedUserQuotaExceeded_Type()
)
axIpNatDsliteStatExtendedUserQuotaExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatExtendedUserQuotaExceeded.setStatus("current")
_AxIpNatDsliteStatTcpFullConeSessionCreated_Type = Counter64
_AxIpNatDsliteStatTcpFullConeSessionCreated_Object = MibScalar
axIpNatDsliteStatTcpFullConeSessionCreated = _AxIpNatDsliteStatTcpFullConeSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 21),
    _AxIpNatDsliteStatTcpFullConeSessionCreated_Type()
)
axIpNatDsliteStatTcpFullConeSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatTcpFullConeSessionCreated.setStatus("current")
_AxIpNatDsliteStatTcpFullConeSessionFreed_Type = Counter64
_AxIpNatDsliteStatTcpFullConeSessionFreed_Object = MibScalar
axIpNatDsliteStatTcpFullConeSessionFreed = _AxIpNatDsliteStatTcpFullConeSessionFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 22),
    _AxIpNatDsliteStatTcpFullConeSessionFreed_Type()
)
axIpNatDsliteStatTcpFullConeSessionFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatTcpFullConeSessionFreed.setStatus("current")
_AxIpNatDsliteStatUdpFullConeSessionCreated_Type = Counter64
_AxIpNatDsliteStatUdpFullConeSessionCreated_Object = MibScalar
axIpNatDsliteStatUdpFullConeSessionCreated = _AxIpNatDsliteStatUdpFullConeSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 23),
    _AxIpNatDsliteStatUdpFullConeSessionCreated_Type()
)
axIpNatDsliteStatUdpFullConeSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatUdpFullConeSessionCreated.setStatus("current")
_AxIpNatDsLiteStatUdpFullConeSessionFreed_Type = Counter64
_AxIpNatDsLiteStatUdpFullConeSessionFreed_Object = MibScalar
axIpNatDsLiteStatUdpFullConeSessionFreed = _AxIpNatDsLiteStatUdpFullConeSessionFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 24),
    _AxIpNatDsLiteStatUdpFullConeSessionFreed_Type()
)
axIpNatDsLiteStatUdpFullConeSessionFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsLiteStatUdpFullConeSessionFreed.setStatus("current")
_AxIpNatDsLiteStatFullConeSessionFailed_Type = Counter64
_AxIpNatDsLiteStatFullConeSessionFailed_Object = MibScalar
axIpNatDsLiteStatFullConeSessionFailed = _AxIpNatDsLiteStatFullConeSessionFailed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 25),
    _AxIpNatDsLiteStatFullConeSessionFailed_Type()
)
axIpNatDsLiteStatFullConeSessionFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsLiteStatFullConeSessionFailed.setStatus("current")
_AxIpNatDsliteStatHairpinSessionCreated_Type = Counter64
_AxIpNatDsliteStatHairpinSessionCreated_Object = MibScalar
axIpNatDsliteStatHairpinSessionCreated = _AxIpNatDsliteStatHairpinSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 26),
    _AxIpNatDsliteStatHairpinSessionCreated_Type()
)
axIpNatDsliteStatHairpinSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatHairpinSessionCreated.setStatus("current")
_AxIpNatDsliteStatSelfHairpinDrop_Type = Counter64
_AxIpNatDsliteStatSelfHairpinDrop_Object = MibScalar
axIpNatDsliteStatSelfHairpinDrop = _AxIpNatDsliteStatSelfHairpinDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 27),
    _AxIpNatDsliteStatSelfHairpinDrop_Type()
)
axIpNatDsliteStatSelfHairpinDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatSelfHairpinDrop.setStatus("current")
_AxIpNatDsliteStatEndpointIndependentMapMatched_Type = Counter64
_AxIpNatDsliteStatEndpointIndependentMapMatched_Object = MibScalar
axIpNatDsliteStatEndpointIndependentMapMatched = _AxIpNatDsliteStatEndpointIndependentMapMatched_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 28),
    _AxIpNatDsliteStatEndpointIndependentMapMatched_Type()
)
axIpNatDsliteStatEndpointIndependentMapMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatEndpointIndependentMapMatched.setStatus("current")
_AxIpNatDsliteStatEndpointIndependentFilterMatched_Type = Counter64
_AxIpNatDsliteStatEndpointIndependentFilterMatched_Object = MibScalar
axIpNatDsliteStatEndpointIndependentFilterMatched = _AxIpNatDsliteStatEndpointIndependentFilterMatched_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 29),
    _AxIpNatDsliteStatEndpointIndependentFilterMatched_Type()
)
axIpNatDsliteStatEndpointIndependentFilterMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatEndpointIndependentFilterMatched.setStatus("current")
_AxIpNatDsliteStatEndpointDependentFilterDrop_Type = Counter64
_AxIpNatDsliteStatEndpointDependentFilterDrop_Object = MibScalar
axIpNatDsliteStatEndpointDependentFilterDrop = _AxIpNatDsliteStatEndpointDependentFilterDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 30),
    _AxIpNatDsliteStatEndpointDependentFilterDrop_Type()
)
axIpNatDsliteStatEndpointDependentFilterDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatEndpointDependentFilterDrop.setStatus("current")
_AxIpNatDsliteStatTruncatedPacket_Type = Counter64
_AxIpNatDsliteStatTruncatedPacket_Object = MibScalar
axIpNatDsliteStatTruncatedPacket = _AxIpNatDsliteStatTruncatedPacket_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 31),
    _AxIpNatDsliteStatTruncatedPacket_Type()
)
axIpNatDsliteStatTruncatedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatTruncatedPacket.setStatus("current")
_AxIpNatDsliteStatLsnLidDrop_Type = Counter64
_AxIpNatDsliteStatLsnLidDrop_Object = MibScalar
axIpNatDsliteStatLsnLidDrop = _AxIpNatDsliteStatLsnLidDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 32),
    _AxIpNatDsliteStatLsnLidDrop_Type()
)
axIpNatDsliteStatLsnLidDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatLsnLidDrop.setStatus("current")
_AxIpNatDsliteStatLsnLidPassThrough_Type = Counter64
_AxIpNatDsliteStatLsnLidPassThrough_Object = MibScalar
axIpNatDsliteStatLsnLidPassThrough = _AxIpNatDsliteStatLsnLidPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 33),
    _AxIpNatDsliteStatLsnLidPassThrough_Type()
)
axIpNatDsliteStatLsnLidPassThrough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatLsnLidPassThrough.setStatus("current")
_AxIpNatDsliteStatNoClassListMatch_Type = Counter64
_AxIpNatDsliteStatNoClassListMatch_Object = MibScalar
axIpNatDsliteStatNoClassListMatch = _AxIpNatDsliteStatNoClassListMatch_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 34),
    _AxIpNatDsliteStatNoClassListMatch_Type()
)
axIpNatDsliteStatNoClassListMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatNoClassListMatch.setStatus("current")
_AxIpNatDsliteStatPermitClassListDrop_Type = Counter64
_AxIpNatDsliteStatPermitClassListDrop_Object = MibScalar
axIpNatDsliteStatPermitClassListDrop = _AxIpNatDsliteStatPermitClassListDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 35),
    _AxIpNatDsliteStatPermitClassListDrop_Type()
)
axIpNatDsliteStatPermitClassListDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatPermitClassListDrop.setStatus("current")
_AxIpNatDsliteStatDataSessionUserQuotaExceeded_Type = Counter64
_AxIpNatDsliteStatDataSessionUserQuotaExceeded_Object = MibScalar
axIpNatDsliteStatDataSessionUserQuotaExceeded = _AxIpNatDsliteStatDataSessionUserQuotaExceeded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 36),
    _AxIpNatDsliteStatDataSessionUserQuotaExceeded_Type()
)
axIpNatDsliteStatDataSessionUserQuotaExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatDataSessionUserQuotaExceeded.setStatus("current")
_AxIpNatDsliteStatConnRateUserQuotaExceeded_Type = Counter64
_AxIpNatDsliteStatConnRateUserQuotaExceeded_Object = MibScalar
axIpNatDsliteStatConnRateUserQuotaExceeded = _AxIpNatDsliteStatConnRateUserQuotaExceeded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 37),
    _AxIpNatDsliteStatConnRateUserQuotaExceeded_Type()
)
axIpNatDsliteStatConnRateUserQuotaExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatConnRateUserQuotaExceeded.setStatus("current")
_AxIpNatDsliteStatEndpointIndependentFilterInboundLimitExceeded_Type = Counter64
_AxIpNatDsliteStatEndpointIndependentFilterInboundLimitExceeded_Object = MibScalar
axIpNatDsliteStatEndpointIndependentFilterInboundLimitExceeded = _AxIpNatDsliteStatEndpointIndependentFilterInboundLimitExceeded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 38),
    _AxIpNatDsliteStatEndpointIndependentFilterInboundLimitExceeded_Type()
)
axIpNatDsliteStatEndpointIndependentFilterInboundLimitExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatEndpointIndependentFilterInboundLimitExceeded.setStatus("current")
_AxIpNatDsliteStatNatPoolMismatchDrop_Type = Counter64
_AxIpNatDsliteStatNatPoolMismatchDrop_Object = MibScalar
axIpNatDsliteStatNatPoolMismatchDrop = _AxIpNatDsliteStatNatPoolMismatchDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 39),
    _AxIpNatDsliteStatNatPoolMismatchDrop_Type()
)
axIpNatDsliteStatNatPoolMismatchDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatNatPoolMismatchDrop.setStatus("current")
_AxIpNatDsliteStatTcpPortOverloaded_Type = Counter64
_AxIpNatDsliteStatTcpPortOverloaded_Object = MibScalar
axIpNatDsliteStatTcpPortOverloaded = _AxIpNatDsliteStatTcpPortOverloaded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 40),
    _AxIpNatDsliteStatTcpPortOverloaded_Type()
)
axIpNatDsliteStatTcpPortOverloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatTcpPortOverloaded.setStatus("current")
_AxIpNatDsliteStatUdpPortOverloaded_Type = Counter64
_AxIpNatDsliteStatUdpPortOverloaded_Object = MibScalar
axIpNatDsliteStatUdpPortOverloaded = _AxIpNatDsliteStatUdpPortOverloaded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 41),
    _AxIpNatDsliteStatUdpPortOverloaded_Type()
)
axIpNatDsliteStatUdpPortOverloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatUdpPortOverloaded.setStatus("current")
_AxIpNatDsliteStatTcpPortOverloadingSessionCreated_Type = Counter64
_AxIpNatDsliteStatTcpPortOverloadingSessionCreated_Object = MibScalar
axIpNatDsliteStatTcpPortOverloadingSessionCreated = _AxIpNatDsliteStatTcpPortOverloadingSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 42),
    _AxIpNatDsliteStatTcpPortOverloadingSessionCreated_Type()
)
axIpNatDsliteStatTcpPortOverloadingSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatTcpPortOverloadingSessionCreated.setStatus("current")
_AxIpNatDsliteStatUdpPortOverloadingSessionCreated_Type = Counter64
_AxIpNatDsliteStatUdpPortOverloadingSessionCreated_Object = MibScalar
axIpNatDsliteStatUdpPortOverloadingSessionCreated = _AxIpNatDsliteStatUdpPortOverloadingSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 43),
    _AxIpNatDsliteStatUdpPortOverloadingSessionCreated_Type()
)
axIpNatDsliteStatUdpPortOverloadingSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatUdpPortOverloadingSessionCreated.setStatus("current")
_AxIpNatDsliteStatTcpPortOverloadingSessionFreed_Type = Counter64
_AxIpNatDsliteStatTcpPortOverloadingSessionFreed_Object = MibScalar
axIpNatDsliteStatTcpPortOverloadingSessionFreed = _AxIpNatDsliteStatTcpPortOverloadingSessionFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 44),
    _AxIpNatDsliteStatTcpPortOverloadingSessionFreed_Type()
)
axIpNatDsliteStatTcpPortOverloadingSessionFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatTcpPortOverloadingSessionFreed.setStatus("current")
_AxIpNatDsliteStatUdpPortOverloadingSessionFreed_Type = Counter64
_AxIpNatDsliteStatUdpPortOverloadingSessionFreed_Object = MibScalar
axIpNatDsliteStatUdpPortOverloadingSessionFreed = _AxIpNatDsliteStatUdpPortOverloadingSessionFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 45),
    _AxIpNatDsliteStatUdpPortOverloadingSessionFreed_Type()
)
axIpNatDsliteStatUdpPortOverloadingSessionFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatUdpPortOverloadingSessionFreed.setStatus("current")
_AxIpNatDsliteStatNatPoolUnusable_Type = Counter64
_AxIpNatDsliteStatNatPoolUnusable_Object = MibScalar
axIpNatDsliteStatNatPoolUnusable = _AxIpNatDsliteStatNatPoolUnusable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 46),
    _AxIpNatDsliteStatNatPoolUnusable_Type()
)
axIpNatDsliteStatNatPoolUnusable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatNatPoolUnusable.setStatus("current")
_AxIpNatDsliteStatNatHANatPoolUnusable_Type = Counter64
_AxIpNatDsliteStatNatHANatPoolUnusable_Object = MibScalar
axIpNatDsliteStatNatHANatPoolUnusable = _AxIpNatDsliteStatNatHANatPoolUnusable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 47),
    _AxIpNatDsliteStatNatHANatPoolUnusable_Type()
)
axIpNatDsliteStatNatHANatPoolUnusable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatNatHANatPoolUnusable.setStatus("current")
_AxIpNatDsliteStatNoRadiusProfileMatch_Type = Counter64
_AxIpNatDsliteStatNoRadiusProfileMatch_Object = MibScalar
axIpNatDsliteStatNoRadiusProfileMatch = _AxIpNatDsliteStatNoRadiusProfileMatch_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 6, 1, 48),
    _AxIpNatDsliteStatNoRadiusProfileMatch_Type()
)
axIpNatDsliteStatNoRadiusProfileMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatDsliteStatNoRadiusProfileMatch.setStatus("current")
_AxIpNatStatsDynamicMappingAclNameTable_Object = MibTable
axIpNatStatsDynamicMappingAclNameTable = _AxIpNatStatsDynamicMappingAclNameTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 19, 1)
)
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingAclNameTable.setStatus("current")
_AxIpNatStatsDynamicMappingAclNameEntry_Object = MibTableRow
axIpNatStatsDynamicMappingAclNameEntry = _AxIpNatStatsDynamicMappingAclNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 19, 1, 1)
)
axIpNatStatsDynamicMappingAclNameEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axIpNatStatsDynamicMappingAclNameAccessListName"),
)
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingAclNameEntry.setStatus("deprecated")
_AxIpNatStatsDynamicMappingAclNameAccessListName_Type = DisplayString
_AxIpNatStatsDynamicMappingAclNameAccessListName_Object = MibTableColumn
axIpNatStatsDynamicMappingAclNameAccessListName = _AxIpNatStatsDynamicMappingAclNameAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 19, 1, 1, 1),
    _AxIpNatStatsDynamicMappingAclNameAccessListName_Type()
)
axIpNatStatsDynamicMappingAclNameAccessListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingAclNameAccessListName.setStatus("current")
_AxIpNatStatsDynamicMappingAclNameAccessListID_Type = Integer32
_AxIpNatStatsDynamicMappingAclNameAccessListID_Object = MibTableColumn
axIpNatStatsDynamicMappingAclNameAccessListID = _AxIpNatStatsDynamicMappingAclNameAccessListID_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 19, 1, 1, 2),
    _AxIpNatStatsDynamicMappingAclNameAccessListID_Type()
)
axIpNatStatsDynamicMappingAclNameAccessListID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingAclNameAccessListID.setStatus("current")
_AxIpNatStatsDynamicMappingAclNamePoolName_Type = DisplayString
_AxIpNatStatsDynamicMappingAclNamePoolName_Object = MibTableColumn
axIpNatStatsDynamicMappingAclNamePoolName = _AxIpNatStatsDynamicMappingAclNamePoolName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 19, 1, 1, 3),
    _AxIpNatStatsDynamicMappingAclNamePoolName_Type()
)
axIpNatStatsDynamicMappingAclNamePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingAclNamePoolName.setStatus("current")
_AxIpNatStatsDynamicMappingAclNameStartAddress_Type = DisplayString
_AxIpNatStatsDynamicMappingAclNameStartAddress_Object = MibTableColumn
axIpNatStatsDynamicMappingAclNameStartAddress = _AxIpNatStatsDynamicMappingAclNameStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 19, 1, 1, 4),
    _AxIpNatStatsDynamicMappingAclNameStartAddress_Type()
)
axIpNatStatsDynamicMappingAclNameStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingAclNameStartAddress.setStatus("current")
_AxIpNatStatsDynamicMappingAclNameEndAddress_Type = DisplayString
_AxIpNatStatsDynamicMappingAclNameEndAddress_Object = MibTableColumn
axIpNatStatsDynamicMappingAclNameEndAddress = _AxIpNatStatsDynamicMappingAclNameEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 19, 1, 1, 5),
    _AxIpNatStatsDynamicMappingAclNameEndAddress_Type()
)
axIpNatStatsDynamicMappingAclNameEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingAclNameEndAddress.setStatus("current")
_AxIpNatStatsDynamicMappingAclNameTotalAddresses_Type = Integer32
_AxIpNatStatsDynamicMappingAclNameTotalAddresses_Object = MibTableColumn
axIpNatStatsDynamicMappingAclNameTotalAddresses = _AxIpNatStatsDynamicMappingAclNameTotalAddresses_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 19, 1, 1, 6),
    _AxIpNatStatsDynamicMappingAclNameTotalAddresses_Type()
)
axIpNatStatsDynamicMappingAclNameTotalAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingAclNameTotalAddresses.setStatus("current")
_AxIpNatStatsDynamicMappingAclNameAllocAddresses_Type = Integer32
_AxIpNatStatsDynamicMappingAclNameAllocAddresses_Object = MibTableColumn
axIpNatStatsDynamicMappingAclNameAllocAddresses = _AxIpNatStatsDynamicMappingAclNameAllocAddresses_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 19, 1, 1, 7),
    _AxIpNatStatsDynamicMappingAclNameAllocAddresses_Type()
)
axIpNatStatsDynamicMappingAclNameAllocAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingAclNameAllocAddresses.setStatus("current")
_AxIpNatStatsDynamicMappingAclNameMissAddresses_Type = Integer32
_AxIpNatStatsDynamicMappingAclNameMissAddresses_Object = MibTableColumn
axIpNatStatsDynamicMappingAclNameMissAddresses = _AxIpNatStatsDynamicMappingAclNameMissAddresses_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 19, 1, 1, 8),
    _AxIpNatStatsDynamicMappingAclNameMissAddresses_Type()
)
axIpNatStatsDynamicMappingAclNameMissAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingAclNameMissAddresses.setStatus("current")
_AxIpNatStatsDynamicMappingAclNameStartAddressType_Type = InetAddressType
_AxIpNatStatsDynamicMappingAclNameStartAddressType_Object = MibTableColumn
axIpNatStatsDynamicMappingAclNameStartAddressType = _AxIpNatStatsDynamicMappingAclNameStartAddressType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 19, 1, 1, 9),
    _AxIpNatStatsDynamicMappingAclNameStartAddressType_Type()
)
axIpNatStatsDynamicMappingAclNameStartAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingAclNameStartAddressType.setStatus("current")
_AxIpNatStatsDynamicMappingAclNameEndAddressType_Type = InetAddressType
_AxIpNatStatsDynamicMappingAclNameEndAddressType_Object = MibTableColumn
axIpNatStatsDynamicMappingAclNameEndAddressType = _AxIpNatStatsDynamicMappingAclNameEndAddressType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 19, 1, 1, 10),
    _AxIpNatStatsDynamicMappingAclNameEndAddressType_Type()
)
axIpNatStatsDynamicMappingAclNameEndAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatStatsDynamicMappingAclNameEndAddressType.setStatus("current")
_AxIpNatLoggingGlobalStats_ObjectIdentity = ObjectIdentity
axIpNatLoggingGlobalStats = _AxIpNatLoggingGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1)
)
_AxIpNatLoggingLogPktSent_Type = Counter64
_AxIpNatLoggingLogPktSent_Object = MibScalar
axIpNatLoggingLogPktSent = _AxIpNatLoggingLogPktSent_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 1),
    _AxIpNatLoggingLogPktSent_Type()
)
axIpNatLoggingLogPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingLogPktSent.setStatus("current")
_AxIpNatLoggingTcpSessCreated_Type = Counter64
_AxIpNatLoggingTcpSessCreated_Object = MibScalar
axIpNatLoggingTcpSessCreated = _AxIpNatLoggingTcpSessCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 2),
    _AxIpNatLoggingTcpSessCreated_Type()
)
axIpNatLoggingTcpSessCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingTcpSessCreated.setStatus("current")
_AxIpNatLoggingTcpSessDeleted_Type = Counter64
_AxIpNatLoggingTcpSessDeleted_Object = MibScalar
axIpNatLoggingTcpSessDeleted = _AxIpNatLoggingTcpSessDeleted_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 3),
    _AxIpNatLoggingTcpSessDeleted_Type()
)
axIpNatLoggingTcpSessDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingTcpSessDeleted.setStatus("current")
_AxIpNatLoggingTcpPortAllocated_Type = Counter64
_AxIpNatLoggingTcpPortAllocated_Object = MibScalar
axIpNatLoggingTcpPortAllocated = _AxIpNatLoggingTcpPortAllocated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 4),
    _AxIpNatLoggingTcpPortAllocated_Type()
)
axIpNatLoggingTcpPortAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingTcpPortAllocated.setStatus("current")
_AxIpNatLoggingTcpPortFreed_Type = Counter64
_AxIpNatLoggingTcpPortFreed_Object = MibScalar
axIpNatLoggingTcpPortFreed = _AxIpNatLoggingTcpPortFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 5),
    _AxIpNatLoggingTcpPortFreed_Type()
)
axIpNatLoggingTcpPortFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingTcpPortFreed.setStatus("current")
_AxIpNatLoggingTcpPortBatchAllocated_Type = Counter64
_AxIpNatLoggingTcpPortBatchAllocated_Object = MibScalar
axIpNatLoggingTcpPortBatchAllocated = _AxIpNatLoggingTcpPortBatchAllocated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 6),
    _AxIpNatLoggingTcpPortBatchAllocated_Type()
)
axIpNatLoggingTcpPortBatchAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingTcpPortBatchAllocated.setStatus("current")
_AxIpNatLoggingTcpPortBatchFreed_Type = Counter64
_AxIpNatLoggingTcpPortBatchFreed_Object = MibScalar
axIpNatLoggingTcpPortBatchFreed = _AxIpNatLoggingTcpPortBatchFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 7),
    _AxIpNatLoggingTcpPortBatchFreed_Type()
)
axIpNatLoggingTcpPortBatchFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingTcpPortBatchFreed.setStatus("current")
_AxIpNatLoggingUdpSessCreated_Type = Counter64
_AxIpNatLoggingUdpSessCreated_Object = MibScalar
axIpNatLoggingUdpSessCreated = _AxIpNatLoggingUdpSessCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 8),
    _AxIpNatLoggingUdpSessCreated_Type()
)
axIpNatLoggingUdpSessCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingUdpSessCreated.setStatus("current")
_AxIpNatLoggingUdpSessDeleted_Type = Counter64
_AxIpNatLoggingUdpSessDeleted_Object = MibScalar
axIpNatLoggingUdpSessDeleted = _AxIpNatLoggingUdpSessDeleted_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 9),
    _AxIpNatLoggingUdpSessDeleted_Type()
)
axIpNatLoggingUdpSessDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingUdpSessDeleted.setStatus("current")
_AxIpNatLoggingUdpPortAllocated_Type = Counter64
_AxIpNatLoggingUdpPortAllocated_Object = MibScalar
axIpNatLoggingUdpPortAllocated = _AxIpNatLoggingUdpPortAllocated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 10),
    _AxIpNatLoggingUdpPortAllocated_Type()
)
axIpNatLoggingUdpPortAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingUdpPortAllocated.setStatus("current")
_AxIpNatLoggingUdpPortFreed_Type = Counter64
_AxIpNatLoggingUdpPortFreed_Object = MibScalar
axIpNatLoggingUdpPortFreed = _AxIpNatLoggingUdpPortFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 11),
    _AxIpNatLoggingUdpPortFreed_Type()
)
axIpNatLoggingUdpPortFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingUdpPortFreed.setStatus("current")
_AxIpNatLoggingUdpPortBatchAllocated_Type = Counter64
_AxIpNatLoggingUdpPortBatchAllocated_Object = MibScalar
axIpNatLoggingUdpPortBatchAllocated = _AxIpNatLoggingUdpPortBatchAllocated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 12),
    _AxIpNatLoggingUdpPortBatchAllocated_Type()
)
axIpNatLoggingUdpPortBatchAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingUdpPortBatchAllocated.setStatus("current")
_AxIpNatLoggingUdpPortBatchFreed_Type = Counter64
_AxIpNatLoggingUdpPortBatchFreed_Object = MibScalar
axIpNatLoggingUdpPortBatchFreed = _AxIpNatLoggingUdpPortBatchFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 13),
    _AxIpNatLoggingUdpPortBatchFreed_Type()
)
axIpNatLoggingUdpPortBatchFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingUdpPortBatchFreed.setStatus("current")
_AxIpNatLoggingIcmpSessCreated_Type = Counter64
_AxIpNatLoggingIcmpSessCreated_Object = MibScalar
axIpNatLoggingIcmpSessCreated = _AxIpNatLoggingIcmpSessCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 14),
    _AxIpNatLoggingIcmpSessCreated_Type()
)
axIpNatLoggingIcmpSessCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingIcmpSessCreated.setStatus("current")
_AxIpNatLoggingIcmpSessDeleted_Type = Counter64
_AxIpNatLoggingIcmpSessDeleted_Object = MibScalar
axIpNatLoggingIcmpSessDeleted = _AxIpNatLoggingIcmpSessDeleted_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 15),
    _AxIpNatLoggingIcmpSessDeleted_Type()
)
axIpNatLoggingIcmpSessDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingIcmpSessDeleted.setStatus("current")
_AxIpNatLoggingIcmpResourceAllocated_Type = Counter64
_AxIpNatLoggingIcmpResourceAllocated_Object = MibScalar
axIpNatLoggingIcmpResourceAllocated = _AxIpNatLoggingIcmpResourceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 16),
    _AxIpNatLoggingIcmpResourceAllocated_Type()
)
axIpNatLoggingIcmpResourceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingIcmpResourceAllocated.setStatus("current")
_AxIpNatLoggingIcmpResourcetFreed_Type = Counter64
_AxIpNatLoggingIcmpResourcetFreed_Object = MibScalar
axIpNatLoggingIcmpResourcetFreed = _AxIpNatLoggingIcmpResourcetFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 17),
    _AxIpNatLoggingIcmpResourcetFreed_Type()
)
axIpNatLoggingIcmpResourcetFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingIcmpResourcetFreed.setStatus("current")
_AxIpNatLoggingIcmpV6SessCreated_Type = Counter64
_AxIpNatLoggingIcmpV6SessCreated_Object = MibScalar
axIpNatLoggingIcmpV6SessCreated = _AxIpNatLoggingIcmpV6SessCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 18),
    _AxIpNatLoggingIcmpV6SessCreated_Type()
)
axIpNatLoggingIcmpV6SessCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingIcmpV6SessCreated.setStatus("current")
_AxIpNatLoggingIcmpV6SessDeleted_Type = Counter64
_AxIpNatLoggingIcmpV6SessDeleted_Object = MibScalar
axIpNatLoggingIcmpV6SessDeleted = _AxIpNatLoggingIcmpV6SessDeleted_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 19),
    _AxIpNatLoggingIcmpV6SessDeleted_Type()
)
axIpNatLoggingIcmpV6SessDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingIcmpV6SessDeleted.setStatus("current")
_AxIpNatLoggingIcmpV6ResourceAllocated_Type = Counter64
_AxIpNatLoggingIcmpV6ResourceAllocated_Object = MibScalar
axIpNatLoggingIcmpV6ResourceAllocated = _AxIpNatLoggingIcmpV6ResourceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 20),
    _AxIpNatLoggingIcmpV6ResourceAllocated_Type()
)
axIpNatLoggingIcmpV6ResourceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingIcmpV6ResourceAllocated.setStatus("current")
_AxIpNatLoggingIcmpV6ResourcetFreed_Type = Counter64
_AxIpNatLoggingIcmpV6ResourcetFreed_Object = MibScalar
axIpNatLoggingIcmpV6ResourcetFreed = _AxIpNatLoggingIcmpV6ResourcetFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 21),
    _AxIpNatLoggingIcmpV6ResourcetFreed_Type()
)
axIpNatLoggingIcmpV6ResourcetFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingIcmpV6ResourcetFreed.setStatus("current")
_AxIpNatLoggingGreSessCreated_Type = Counter64
_AxIpNatLoggingGreSessCreated_Object = MibScalar
axIpNatLoggingGreSessCreated = _AxIpNatLoggingGreSessCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 22),
    _AxIpNatLoggingGreSessCreated_Type()
)
axIpNatLoggingGreSessCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingGreSessCreated.setStatus("current")
_AxIpNatLoggingGreSessDeleted_Type = Counter64
_AxIpNatLoggingGreSessDeleted_Object = MibScalar
axIpNatLoggingGreSessDeleted = _AxIpNatLoggingGreSessDeleted_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 23),
    _AxIpNatLoggingGreSessDeleted_Type()
)
axIpNatLoggingGreSessDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingGreSessDeleted.setStatus("current")
_AxIpNatLoggingGreResourceAllocated_Type = Counter64
_AxIpNatLoggingGreResourceAllocated_Object = MibScalar
axIpNatLoggingGreResourceAllocated = _AxIpNatLoggingGreResourceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 24),
    _AxIpNatLoggingGreResourceAllocated_Type()
)
axIpNatLoggingGreResourceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingGreResourceAllocated.setStatus("current")
_AxIpNatLoggingGreResourcetFreed_Type = Counter64
_AxIpNatLoggingGreResourcetFreed_Object = MibScalar
axIpNatLoggingGreResourcetFreed = _AxIpNatLoggingGreResourcetFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 25),
    _AxIpNatLoggingGreResourcetFreed_Type()
)
axIpNatLoggingGreResourcetFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingGreResourcetFreed.setStatus("current")
_AxIpNatLoggingEspSessCreated_Type = Counter64
_AxIpNatLoggingEspSessCreated_Object = MibScalar
axIpNatLoggingEspSessCreated = _AxIpNatLoggingEspSessCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 26),
    _AxIpNatLoggingEspSessCreated_Type()
)
axIpNatLoggingEspSessCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingEspSessCreated.setStatus("current")
_AxIpNatLoggingEspSessDeleted_Type = Counter64
_AxIpNatLoggingEspSessDeleted_Object = MibScalar
axIpNatLoggingEspSessDeleted = _AxIpNatLoggingEspSessDeleted_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 27),
    _AxIpNatLoggingEspSessDeleted_Type()
)
axIpNatLoggingEspSessDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingEspSessDeleted.setStatus("current")
_AxIpNatLoggingEspResourceAllocated_Type = Counter64
_AxIpNatLoggingEspResourceAllocated_Object = MibScalar
axIpNatLoggingEspResourceAllocated = _AxIpNatLoggingEspResourceAllocated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 28),
    _AxIpNatLoggingEspResourceAllocated_Type()
)
axIpNatLoggingEspResourceAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingEspResourceAllocated.setStatus("current")
_AxIpNatLoggingEspResourcetFreed_Type = Counter64
_AxIpNatLoggingEspResourcetFreed_Object = MibScalar
axIpNatLoggingEspResourcetFreed = _AxIpNatLoggingEspResourcetFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 29),
    _AxIpNatLoggingEspResourcetFreed_Type()
)
axIpNatLoggingEspResourcetFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingEspResourcetFreed.setStatus("current")
_AxIpNatLoggingFixedNatInsideUserPortMapping_Type = Counter64
_AxIpNatLoggingFixedNatInsideUserPortMapping_Object = MibScalar
axIpNatLoggingFixedNatInsideUserPortMapping = _AxIpNatLoggingFixedNatInsideUserPortMapping_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 30),
    _AxIpNatLoggingFixedNatInsideUserPortMapping_Type()
)
axIpNatLoggingFixedNatInsideUserPortMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingFixedNatInsideUserPortMapping.setStatus("current")
_AxIpNatLoggingFixedNatDisabledConfigLogged_Type = Counter64
_AxIpNatLoggingFixedNatDisabledConfigLogged_Object = MibScalar
axIpNatLoggingFixedNatDisabledConfigLogged = _AxIpNatLoggingFixedNatDisabledConfigLogged_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 31),
    _AxIpNatLoggingFixedNatDisabledConfigLogged_Type()
)
axIpNatLoggingFixedNatDisabledConfigLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingFixedNatDisabledConfigLogged.setStatus("current")
_AxIpNatLoggingFixedNatDisabledConfigLogsSent_Type = Counter64
_AxIpNatLoggingFixedNatDisabledConfigLogsSent_Object = MibScalar
axIpNatLoggingFixedNatDisabledConfigLogsSent = _AxIpNatLoggingFixedNatDisabledConfigLogsSent_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 32),
    _AxIpNatLoggingFixedNatDisabledConfigLogsSent_Type()
)
axIpNatLoggingFixedNatDisabledConfigLogsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingFixedNatDisabledConfigLogsSent.setStatus("current")
_AxIpNatLoggingFixedNatPeriodicConfigLogsSent_Type = Counter64
_AxIpNatLoggingFixedNatPeriodicConfigLogsSent_Object = MibScalar
axIpNatLoggingFixedNatPeriodicConfigLogsSent = _AxIpNatLoggingFixedNatPeriodicConfigLogsSent_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 33),
    _AxIpNatLoggingFixedNatPeriodicConfigLogsSent_Type()
)
axIpNatLoggingFixedNatPeriodicConfigLogsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingFixedNatPeriodicConfigLogsSent.setStatus("current")
_AxIpNatLoggingFixedNatPeriodicConfigLogged_Type = Counter64
_AxIpNatLoggingFixedNatPeriodicConfigLogged_Object = MibScalar
axIpNatLoggingFixedNatPeriodicConfigLogged = _AxIpNatLoggingFixedNatPeriodicConfigLogged_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 34),
    _AxIpNatLoggingFixedNatPeriodicConfigLogged_Type()
)
axIpNatLoggingFixedNatPeriodicConfigLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingFixedNatPeriodicConfigLogged.setStatus("current")
_AxIpNatLoggingLogPacketsDrop_Type = Counter64
_AxIpNatLoggingLogPacketsDrop_Object = MibScalar
axIpNatLoggingLogPacketsDrop = _AxIpNatLoggingLogPacketsDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 35),
    _AxIpNatLoggingLogPacketsDrop_Type()
)
axIpNatLoggingLogPacketsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatLoggingLogPacketsDrop.setStatus("current")
_AxIpNatTcpConnectionEstablished_Type = Counter64
_AxIpNatTcpConnectionEstablished_Object = MibScalar
axIpNatTcpConnectionEstablished = _AxIpNatTcpConnectionEstablished_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 36),
    _AxIpNatTcpConnectionEstablished_Type()
)
axIpNatTcpConnectionEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatTcpConnectionEstablished.setStatus("current")
_AxIpNatTcpConnectionLost_Type = Counter64
_AxIpNatTcpConnectionLost_Object = MibScalar
axIpNatTcpConnectionLost = _AxIpNatTcpConnectionLost_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 37),
    _AxIpNatTcpConnectionLost_Type()
)
axIpNatTcpConnectionLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatTcpConnectionLost.setStatus("current")
_AxIpNatTcpPortOverloadingAllocated_Type = Counter64
_AxIpNatTcpPortOverloadingAllocated_Object = MibScalar
axIpNatTcpPortOverloadingAllocated = _AxIpNatTcpPortOverloadingAllocated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 38),
    _AxIpNatTcpPortOverloadingAllocated_Type()
)
axIpNatTcpPortOverloadingAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatTcpPortOverloadingAllocated.setStatus("current")
_AxIpNatTcpPortOverloadingFreed_Type = Counter64
_AxIpNatTcpPortOverloadingFreed_Object = MibScalar
axIpNatTcpPortOverloadingFreed = _AxIpNatTcpPortOverloadingFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 39),
    _AxIpNatTcpPortOverloadingFreed_Type()
)
axIpNatTcpPortOverloadingFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatTcpPortOverloadingFreed.setStatus("current")
_AxIpNatUdpPortOverloadingAllocated_Type = Counter64
_AxIpNatUdpPortOverloadingAllocated_Object = MibScalar
axIpNatUdpPortOverloadingAllocated = _AxIpNatUdpPortOverloadingAllocated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 40),
    _AxIpNatUdpPortOverloadingAllocated_Type()
)
axIpNatUdpPortOverloadingAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatUdpPortOverloadingAllocated.setStatus("current")
_AxIpNatUdpPortOverloadingFreed_Type = Counter64
_AxIpNatUdpPortOverloadingFreed_Object = MibScalar
axIpNatUdpPortOverloadingFreed = _AxIpNatUdpPortOverloadingFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 41),
    _AxIpNatUdpPortOverloadingFreed_Type()
)
axIpNatUdpPortOverloadingFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatUdpPortOverloadingFreed.setStatus("current")
_AxIpNatHttpRequestLogged_Type = Counter64
_AxIpNatHttpRequestLogged_Object = MibScalar
axIpNatHttpRequestLogged = _AxIpNatHttpRequestLogged_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 101, 1, 42),
    _AxIpNatHttpRequestLogged_Type()
)
axIpNatHttpRequestLogged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpNatHttpRequestLogged.setStatus("current")
_AxFixedNatGlobalStats_ObjectIdentity = ObjectIdentity
axFixedNatGlobalStats = _AxFixedNatGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1)
)


class _AxFixedNatTotalNatAddressInUse_Type(CounterBasedGauge64):
    """Custom type axFixedNatTotalNatAddressInUse based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatTotalNatAddressInUse_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatTotalNatAddressInUse_Object = MibScalar
axFixedNatTotalNatAddressInUse = _AxFixedNatTotalNatAddressInUse_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 1),
    _AxFixedNatTotalNatAddressInUse_Type()
)
axFixedNatTotalNatAddressInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTotalNatAddressInUse.setStatus("current")


class _AxFixedNatTotalTcpPortsAllocated_Type(CounterBasedGauge64):
    """Custom type axFixedNatTotalTcpPortsAllocated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatTotalTcpPortsAllocated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatTotalTcpPortsAllocated_Object = MibScalar
axFixedNatTotalTcpPortsAllocated = _AxFixedNatTotalTcpPortsAllocated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 2),
    _AxFixedNatTotalTcpPortsAllocated_Type()
)
axFixedNatTotalTcpPortsAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTotalTcpPortsAllocated.setStatus("current")


class _AxFixedNatTotalTcpPortsFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatTotalTcpPortsFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatTotalTcpPortsFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatTotalTcpPortsFreed_Object = MibScalar
axFixedNatTotalTcpPortsFreed = _AxFixedNatTotalTcpPortsFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 3),
    _AxFixedNatTotalTcpPortsFreed_Type()
)
axFixedNatTotalTcpPortsFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTotalTcpPortsFreed.setStatus("current")


class _AxFixedNatTotalUdpPortsAllocated_Type(CounterBasedGauge64):
    """Custom type axFixedNatTotalUdpPortsAllocated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatTotalUdpPortsAllocated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatTotalUdpPortsAllocated_Object = MibScalar
axFixedNatTotalUdpPortsAllocated = _AxFixedNatTotalUdpPortsAllocated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 4),
    _AxFixedNatTotalUdpPortsAllocated_Type()
)
axFixedNatTotalUdpPortsAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTotalUdpPortsAllocated.setStatus("current")


class _AxFixedNatTotalUdpPortsFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatTotalUdpPortsFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatTotalUdpPortsFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatTotalUdpPortsFreed_Object = MibScalar
axFixedNatTotalUdpPortsFreed = _AxFixedNatTotalUdpPortsFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 5),
    _AxFixedNatTotalUdpPortsFreed_Type()
)
axFixedNatTotalUdpPortsFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTotalUdpPortsFreed.setStatus("current")


class _AxFixedNatTotalIcmpPortsAllocated_Type(CounterBasedGauge64):
    """Custom type axFixedNatTotalIcmpPortsAllocated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatTotalIcmpPortsAllocated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatTotalIcmpPortsAllocated_Object = MibScalar
axFixedNatTotalIcmpPortsAllocated = _AxFixedNatTotalIcmpPortsAllocated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 6),
    _AxFixedNatTotalIcmpPortsAllocated_Type()
)
axFixedNatTotalIcmpPortsAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTotalIcmpPortsAllocated.setStatus("current")


class _AxFixedNatTotalIcmpPortsFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatTotalIcmpPortsFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatTotalIcmpPortsFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatTotalIcmpPortsFreed_Object = MibScalar
axFixedNatTotalIcmpPortsFreed = _AxFixedNatTotalIcmpPortsFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 7),
    _AxFixedNatTotalIcmpPortsFreed_Type()
)
axFixedNatTotalIcmpPortsFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTotalIcmpPortsFreed.setStatus("current")


class _AxFixedNatTcpNatPortUnavailable_Type(CounterBasedGauge64):
    """Custom type axFixedNatTcpNatPortUnavailable based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatTcpNatPortUnavailable_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatTcpNatPortUnavailable_Object = MibScalar
axFixedNatTcpNatPortUnavailable = _AxFixedNatTcpNatPortUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 8),
    _AxFixedNatTcpNatPortUnavailable_Type()
)
axFixedNatTcpNatPortUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTcpNatPortUnavailable.setStatus("current")


class _AxFixedNatUdpNatPortUnavailable_Type(CounterBasedGauge64):
    """Custom type axFixedNatUdpNatPortUnavailable based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatUdpNatPortUnavailable_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatUdpNatPortUnavailable_Object = MibScalar
axFixedNatUdpNatPortUnavailable = _AxFixedNatUdpNatPortUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 9),
    _AxFixedNatUdpNatPortUnavailable_Type()
)
axFixedNatUdpNatPortUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatUdpNatPortUnavailable.setStatus("current")


class _AxFixedNatIcmpNatPortUnavailable_Type(CounterBasedGauge64):
    """Custom type axFixedNatIcmpNatPortUnavailable based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatIcmpNatPortUnavailable_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatIcmpNatPortUnavailable_Object = MibScalar
axFixedNatIcmpNatPortUnavailable = _AxFixedNatIcmpNatPortUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 10),
    _AxFixedNatIcmpNatPortUnavailable_Type()
)
axFixedNatIcmpNatPortUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatIcmpNatPortUnavailable.setStatus("current")


class _AxFixedNatSessionUserQuotaExceed_Type(CounterBasedGauge64):
    """Custom type axFixedNatSessionUserQuotaExceed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatSessionUserQuotaExceed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatSessionUserQuotaExceed_Object = MibScalar
axFixedNatSessionUserQuotaExceed = _AxFixedNatSessionUserQuotaExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 11),
    _AxFixedNatSessionUserQuotaExceed_Type()
)
axFixedNatSessionUserQuotaExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatSessionUserQuotaExceed.setStatus("current")


class _AxFixedNatFullConeSessionCreationFailed_Type(CounterBasedGauge64):
    """Custom type axFixedNatFullConeSessionCreationFailed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatFullConeSessionCreationFailed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatFullConeSessionCreationFailed_Object = MibScalar
axFixedNatFullConeSessionCreationFailed = _AxFixedNatFullConeSessionCreationFailed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 12),
    _AxFixedNatFullConeSessionCreationFailed_Type()
)
axFixedNatFullConeSessionCreationFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessionCreationFailed.setStatus("current")


class _AxFixedNatLidStandbyDrop_Type(CounterBasedGauge64):
    """Custom type axFixedNatLidStandbyDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatLidStandbyDrop_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatLidStandbyDrop_Object = MibScalar
axFixedNatLidStandbyDrop = _AxFixedNatLidStandbyDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 13),
    _AxFixedNatLidStandbyDrop_Type()
)
axFixedNatLidStandbyDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatLidStandbyDrop.setStatus("current")


class _AxFixedNatSelfHairpinningDrop_Type(CounterBasedGauge64):
    """Custom type axFixedNatSelfHairpinningDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatSelfHairpinningDrop_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatSelfHairpinningDrop_Object = MibScalar
axFixedNatSelfHairpinningDrop = _AxFixedNatSelfHairpinningDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 14),
    _AxFixedNatSelfHairpinningDrop_Type()
)
axFixedNatSelfHairpinningDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatSelfHairpinningDrop.setStatus("current")


class _AxFixedNatIpv6InIpv4PacketDrop_Type(CounterBasedGauge64):
    """Custom type axFixedNatIpv6InIpv4PacketDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatIpv6InIpv4PacketDrop_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatIpv6InIpv4PacketDrop_Object = MibScalar
axFixedNatIpv6InIpv4PacketDrop = _AxFixedNatIpv6InIpv4PacketDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 15),
    _AxFixedNatIpv6InIpv4PacketDrop_Type()
)
axFixedNatIpv6InIpv4PacketDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatIpv6InIpv4PacketDrop.setStatus("current")


class _AxFixedNatDestRuleListDrop_Type(CounterBasedGauge64):
    """Custom type axFixedNatDestRuleListDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatDestRuleListDrop_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatDestRuleListDrop_Object = MibScalar
axFixedNatDestRuleListDrop = _AxFixedNatDestRuleListDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 16),
    _AxFixedNatDestRuleListDrop_Type()
)
axFixedNatDestRuleListDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatDestRuleListDrop.setStatus("current")


class _AxFixedNatDestRuleListPassThrough_Type(CounterBasedGauge64):
    """Custom type axFixedNatDestRuleListPassThrough based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatDestRuleListPassThrough_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatDestRuleListPassThrough_Object = MibScalar
axFixedNatDestRuleListPassThrough = _AxFixedNatDestRuleListPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 17),
    _AxFixedNatDestRuleListPassThrough_Type()
)
axFixedNatDestRuleListPassThrough.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatDestRuleListPassThrough.setStatus("current")
_AxFixedNatNat44GlobalStats_ObjectIdentity = ObjectIdentity
axFixedNatNat44GlobalStats = _AxFixedNatNat44GlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 18)
)


class _AxFixedNatNat44DataSessionsCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat44DataSessionsCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat44DataSessionsCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat44DataSessionsCreated_Object = MibScalar
axFixedNatNat44DataSessionsCreated = _AxFixedNatNat44DataSessionsCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 18, 1),
    _AxFixedNatNat44DataSessionsCreated_Type()
)
axFixedNatNat44DataSessionsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat44DataSessionsCreated.setStatus("current")


class _AxFixedNatNat44DataSessionsFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat44DataSessionsFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat44DataSessionsFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat44DataSessionsFreed_Object = MibScalar
axFixedNatNat44DataSessionsFreed = _AxFixedNatNat44DataSessionsFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 18, 2),
    _AxFixedNatNat44DataSessionsFreed_Type()
)
axFixedNatNat44DataSessionsFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat44DataSessionsFreed.setStatus("current")


class _AxFixedNatNat44TcpFullConeCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat44TcpFullConeCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat44TcpFullConeCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat44TcpFullConeCreated_Object = MibScalar
axFixedNatNat44TcpFullConeCreated = _AxFixedNatNat44TcpFullConeCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 18, 3),
    _AxFixedNatNat44TcpFullConeCreated_Type()
)
axFixedNatNat44TcpFullConeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat44TcpFullConeCreated.setStatus("current")


class _AxFixedNatNat44TcpFullConeFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat44TcpFullConeFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat44TcpFullConeFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat44TcpFullConeFreed_Object = MibScalar
axFixedNatNat44TcpFullConeFreed = _AxFixedNatNat44TcpFullConeFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 18, 4),
    _AxFixedNatNat44TcpFullConeFreed_Type()
)
axFixedNatNat44TcpFullConeFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat44TcpFullConeFreed.setStatus("current")


class _AxFixedNatNat44UdpFullConeCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat44UdpFullConeCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat44UdpFullConeCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat44UdpFullConeCreated_Object = MibScalar
axFixedNatNat44UdpFullConeCreated = _AxFixedNatNat44UdpFullConeCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 18, 5),
    _AxFixedNatNat44UdpFullConeCreated_Type()
)
axFixedNatNat44UdpFullConeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat44UdpFullConeCreated.setStatus("current")


class _AxFixedNatNat44UdpFullConeFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat44UdpFullConeFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat44UdpFullConeFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat44UdpFullConeFreed_Object = MibScalar
axFixedNatNat44UdpFullConeFreed = _AxFixedNatNat44UdpFullConeFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 18, 6),
    _AxFixedNatNat44UdpFullConeFreed_Type()
)
axFixedNatNat44UdpFullConeFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat44UdpFullConeFreed.setStatus("current")


class _AxFixedNatNat44UdpAlgFullConeCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat44UdpAlgFullConeCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat44UdpAlgFullConeCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat44UdpAlgFullConeCreated_Object = MibScalar
axFixedNatNat44UdpAlgFullConeCreated = _AxFixedNatNat44UdpAlgFullConeCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 18, 7),
    _AxFixedNatNat44UdpAlgFullConeCreated_Type()
)
axFixedNatNat44UdpAlgFullConeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat44UdpAlgFullConeCreated.setStatus("current")


class _AxFixedNatNat44UdpAlgFullConeFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat44UdpAlgFullConeFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat44UdpAlgFullConeFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat44UdpAlgFullConeFreed_Object = MibScalar
axFixedNatNat44UdpAlgFullConeFreed = _AxFixedNatNat44UdpAlgFullConeFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 18, 8),
    _AxFixedNatNat44UdpAlgFullConeFreed_Type()
)
axFixedNatNat44UdpAlgFullConeFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat44UdpAlgFullConeFreed.setStatus("current")


class _AxFixedNatNat44EndpointIndependentMappingMatched_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat44EndpointIndependentMappingMatched based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat44EndpointIndependentMappingMatched_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat44EndpointIndependentMappingMatched_Object = MibScalar
axFixedNatNat44EndpointIndependentMappingMatched = _AxFixedNatNat44EndpointIndependentMappingMatched_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 18, 9),
    _AxFixedNatNat44EndpointIndependentMappingMatched_Type()
)
axFixedNatNat44EndpointIndependentMappingMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat44EndpointIndependentMappingMatched.setStatus("current")


class _AxFixedNatNat44EndpointIndependentFilteringMatched_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat44EndpointIndependentFilteringMatched based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat44EndpointIndependentFilteringMatched_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat44EndpointIndependentFilteringMatched_Object = MibScalar
axFixedNatNat44EndpointIndependentFilteringMatched = _AxFixedNatNat44EndpointIndependentFilteringMatched_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 18, 10),
    _AxFixedNatNat44EndpointIndependentFilteringMatched_Type()
)
axFixedNatNat44EndpointIndependentFilteringMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat44EndpointIndependentFilteringMatched.setStatus("current")


class _AxFixedNatNat44EndpointIndependentFilteringDrop_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat44EndpointIndependentFilteringDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat44EndpointIndependentFilteringDrop_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat44EndpointIndependentFilteringDrop_Object = MibScalar
axFixedNatNat44EndpointIndependentFilteringDrop = _AxFixedNatNat44EndpointIndependentFilteringDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 18, 11),
    _AxFixedNatNat44EndpointIndependentFilteringDrop_Type()
)
axFixedNatNat44EndpointIndependentFilteringDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat44EndpointIndependentFilteringDrop.setStatus("current")


class _AxFixedNatNat44EndpointIndependentFilteringLimitExceed_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat44EndpointIndependentFilteringLimitExceed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat44EndpointIndependentFilteringLimitExceed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat44EndpointIndependentFilteringLimitExceed_Object = MibScalar
axFixedNatNat44EndpointIndependentFilteringLimitExceed = _AxFixedNatNat44EndpointIndependentFilteringLimitExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 18, 12),
    _AxFixedNatNat44EndpointIndependentFilteringLimitExceed_Type()
)
axFixedNatNat44EndpointIndependentFilteringLimitExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat44EndpointIndependentFilteringLimitExceed.setStatus("current")


class _AxFixedNatNat44HairpinSessionCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat44HairpinSessionCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat44HairpinSessionCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat44HairpinSessionCreated_Object = MibScalar
axFixedNatNat44HairpinSessionCreated = _AxFixedNatNat44HairpinSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 18, 13),
    _AxFixedNatNat44HairpinSessionCreated_Type()
)
axFixedNatNat44HairpinSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat44HairpinSessionCreated.setStatus("current")
_AxFixedNatNat64GlobalStats_ObjectIdentity = ObjectIdentity
axFixedNatNat64GlobalStats = _AxFixedNatNat64GlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 19)
)


class _AxFixedNatNat64DataSessionsCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat64DataSessionsCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat64DataSessionsCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat64DataSessionsCreated_Object = MibScalar
axFixedNatNat64DataSessionsCreated = _AxFixedNatNat64DataSessionsCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 19, 1),
    _AxFixedNatNat64DataSessionsCreated_Type()
)
axFixedNatNat64DataSessionsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat64DataSessionsCreated.setStatus("current")


class _AxFixedNatNat64DataSessionsFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat64DataSessionsFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat64DataSessionsFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat64DataSessionsFreed_Object = MibScalar
axFixedNatNat64DataSessionsFreed = _AxFixedNatNat64DataSessionsFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 19, 2),
    _AxFixedNatNat64DataSessionsFreed_Type()
)
axFixedNatNat64DataSessionsFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat64DataSessionsFreed.setStatus("current")


class _AxFixedNatNat64TcpFullConeCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat64TcpFullConeCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat64TcpFullConeCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat64TcpFullConeCreated_Object = MibScalar
axFixedNatNat64TcpFullConeCreated = _AxFixedNatNat64TcpFullConeCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 19, 3),
    _AxFixedNatNat64TcpFullConeCreated_Type()
)
axFixedNatNat64TcpFullConeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat64TcpFullConeCreated.setStatus("current")


class _AxFixedNatNat64TcpFullConeFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat64TcpFullConeFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat64TcpFullConeFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat64TcpFullConeFreed_Object = MibScalar
axFixedNatNat64TcpFullConeFreed = _AxFixedNatNat64TcpFullConeFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 19, 4),
    _AxFixedNatNat64TcpFullConeFreed_Type()
)
axFixedNatNat64TcpFullConeFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat64TcpFullConeFreed.setStatus("current")


class _AxFixedNatNat64UdpFullConeCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat64UdpFullConeCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat64UdpFullConeCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat64UdpFullConeCreated_Object = MibScalar
axFixedNatNat64UdpFullConeCreated = _AxFixedNatNat64UdpFullConeCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 19, 5),
    _AxFixedNatNat64UdpFullConeCreated_Type()
)
axFixedNatNat64UdpFullConeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat64UdpFullConeCreated.setStatus("current")


class _AxFixedNatNat64UdpFullConeFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat64UdpFullConeFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat64UdpFullConeFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat64UdpFullConeFreed_Object = MibScalar
axFixedNatNat64UdpFullConeFreed = _AxFixedNatNat64UdpFullConeFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 19, 6),
    _AxFixedNatNat64UdpFullConeFreed_Type()
)
axFixedNatNat64UdpFullConeFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat64UdpFullConeFreed.setStatus("current")


class _AxFixedNatNat64UdpAlgFullConeCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat64UdpAlgFullConeCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat64UdpAlgFullConeCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat64UdpAlgFullConeCreated_Object = MibScalar
axFixedNatNat64UdpAlgFullConeCreated = _AxFixedNatNat64UdpAlgFullConeCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 19, 7),
    _AxFixedNatNat64UdpAlgFullConeCreated_Type()
)
axFixedNatNat64UdpAlgFullConeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat64UdpAlgFullConeCreated.setStatus("current")


class _AxFixedNatNat64UdpAlgFullConeFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat64UdpAlgFullConeFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat64UdpAlgFullConeFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat64UdpAlgFullConeFreed_Object = MibScalar
axFixedNatNat64UdpAlgFullConeFreed = _AxFixedNatNat64UdpAlgFullConeFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 19, 8),
    _AxFixedNatNat64UdpAlgFullConeFreed_Type()
)
axFixedNatNat64UdpAlgFullConeFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat64UdpAlgFullConeFreed.setStatus("current")


class _AxFixedNatNat64EndpointIndependentMappingMatched_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat64EndpointIndependentMappingMatched based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat64EndpointIndependentMappingMatched_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat64EndpointIndependentMappingMatched_Object = MibScalar
axFixedNatNat64EndpointIndependentMappingMatched = _AxFixedNatNat64EndpointIndependentMappingMatched_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 19, 9),
    _AxFixedNatNat64EndpointIndependentMappingMatched_Type()
)
axFixedNatNat64EndpointIndependentMappingMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat64EndpointIndependentMappingMatched.setStatus("current")


class _AxFixedNatNat64EndpointIndependentFilteringMatched_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat64EndpointIndependentFilteringMatched based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat64EndpointIndependentFilteringMatched_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat64EndpointIndependentFilteringMatched_Object = MibScalar
axFixedNatNat64EndpointIndependentFilteringMatched = _AxFixedNatNat64EndpointIndependentFilteringMatched_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 19, 10),
    _AxFixedNatNat64EndpointIndependentFilteringMatched_Type()
)
axFixedNatNat64EndpointIndependentFilteringMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat64EndpointIndependentFilteringMatched.setStatus("current")


class _AxFixedNatNat64EndpointIndependentFilteringDrop_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat64EndpointIndependentFilteringDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat64EndpointIndependentFilteringDrop_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat64EndpointIndependentFilteringDrop_Object = MibScalar
axFixedNatNat64EndpointIndependentFilteringDrop = _AxFixedNatNat64EndpointIndependentFilteringDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 19, 11),
    _AxFixedNatNat64EndpointIndependentFilteringDrop_Type()
)
axFixedNatNat64EndpointIndependentFilteringDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat64EndpointIndependentFilteringDrop.setStatus("current")


class _AxFixedNatNat64EndpointIndependentFilteringLimitExceed_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat64EndpointIndependentFilteringLimitExceed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat64EndpointIndependentFilteringLimitExceed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat64EndpointIndependentFilteringLimitExceed_Object = MibScalar
axFixedNatNat64EndpointIndependentFilteringLimitExceed = _AxFixedNatNat64EndpointIndependentFilteringLimitExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 19, 12),
    _AxFixedNatNat64EndpointIndependentFilteringLimitExceed_Type()
)
axFixedNatNat64EndpointIndependentFilteringLimitExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat64EndpointIndependentFilteringLimitExceed.setStatus("current")


class _AxFixedNatNat64HairpinSessionCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatNat64HairpinSessionCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatNat64HairpinSessionCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatNat64HairpinSessionCreated_Object = MibScalar
axFixedNatNat64HairpinSessionCreated = _AxFixedNatNat64HairpinSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 19, 13),
    _AxFixedNatNat64HairpinSessionCreated_Type()
)
axFixedNatNat64HairpinSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatNat64HairpinSessionCreated.setStatus("current")
_AxFixedNatDsliteGlobalStats_ObjectIdentity = ObjectIdentity
axFixedNatDsliteGlobalStats = _AxFixedNatDsliteGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 20)
)


class _AxFixedNatDsliteDataSessionsCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatDsliteDataSessionsCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatDsliteDataSessionsCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatDsliteDataSessionsCreated_Object = MibScalar
axFixedNatDsliteDataSessionsCreated = _AxFixedNatDsliteDataSessionsCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 20, 1),
    _AxFixedNatDsliteDataSessionsCreated_Type()
)
axFixedNatDsliteDataSessionsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatDsliteDataSessionsCreated.setStatus("current")


class _AxFixedNatDsliteDataSessionsFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatDsliteDataSessionsFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatDsliteDataSessionsFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatDsliteDataSessionsFreed_Object = MibScalar
axFixedNatDsliteDataSessionsFreed = _AxFixedNatDsliteDataSessionsFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 20, 2),
    _AxFixedNatDsliteDataSessionsFreed_Type()
)
axFixedNatDsliteDataSessionsFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatDsliteDataSessionsFreed.setStatus("current")


class _AxFixedNatDsliteTcpFullConeCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatDsliteTcpFullConeCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatDsliteTcpFullConeCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatDsliteTcpFullConeCreated_Object = MibScalar
axFixedNatDsliteTcpFullConeCreated = _AxFixedNatDsliteTcpFullConeCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 20, 3),
    _AxFixedNatDsliteTcpFullConeCreated_Type()
)
axFixedNatDsliteTcpFullConeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatDsliteTcpFullConeCreated.setStatus("current")


class _AxFixedNatDsliteTcpFullConeFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatDsliteTcpFullConeFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatDsliteTcpFullConeFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatDsliteTcpFullConeFreed_Object = MibScalar
axFixedNatDsliteTcpFullConeFreed = _AxFixedNatDsliteTcpFullConeFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 20, 4),
    _AxFixedNatDsliteTcpFullConeFreed_Type()
)
axFixedNatDsliteTcpFullConeFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatDsliteTcpFullConeFreed.setStatus("current")


class _AxFixedNatDsliteUdpFullConeCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatDsliteUdpFullConeCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatDsliteUdpFullConeCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatDsliteUdpFullConeCreated_Object = MibScalar
axFixedNatDsliteUdpFullConeCreated = _AxFixedNatDsliteUdpFullConeCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 20, 5),
    _AxFixedNatDsliteUdpFullConeCreated_Type()
)
axFixedNatDsliteUdpFullConeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatDsliteUdpFullConeCreated.setStatus("current")


class _AxFixedNatDsliteUdpFullConeFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatDsliteUdpFullConeFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatDsliteUdpFullConeFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatDsliteUdpFullConeFreed_Object = MibScalar
axFixedNatDsliteUdpFullConeFreed = _AxFixedNatDsliteUdpFullConeFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 20, 6),
    _AxFixedNatDsliteUdpFullConeFreed_Type()
)
axFixedNatDsliteUdpFullConeFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatDsliteUdpFullConeFreed.setStatus("current")


class _AxFixedNatDsliteUdpAlgFullConeCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatDsliteUdpAlgFullConeCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatDsliteUdpAlgFullConeCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatDsliteUdpAlgFullConeCreated_Object = MibScalar
axFixedNatDsliteUdpAlgFullConeCreated = _AxFixedNatDsliteUdpAlgFullConeCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 20, 7),
    _AxFixedNatDsliteUdpAlgFullConeCreated_Type()
)
axFixedNatDsliteUdpAlgFullConeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatDsliteUdpAlgFullConeCreated.setStatus("current")


class _AxFixedNatDsliteUdpAlgFullConeFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatDsliteUdpAlgFullConeFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatDsliteUdpAlgFullConeFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatDsliteUdpAlgFullConeFreed_Object = MibScalar
axFixedNatDsliteUdpAlgFullConeFreed = _AxFixedNatDsliteUdpAlgFullConeFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 20, 8),
    _AxFixedNatDsliteUdpAlgFullConeFreed_Type()
)
axFixedNatDsliteUdpAlgFullConeFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatDsliteUdpAlgFullConeFreed.setStatus("current")


class _AxFixedNatDsliteEndpointIndependentMappingMatched_Type(CounterBasedGauge64):
    """Custom type axFixedNatDsliteEndpointIndependentMappingMatched based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatDsliteEndpointIndependentMappingMatched_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatDsliteEndpointIndependentMappingMatched_Object = MibScalar
axFixedNatDsliteEndpointIndependentMappingMatched = _AxFixedNatDsliteEndpointIndependentMappingMatched_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 20, 9),
    _AxFixedNatDsliteEndpointIndependentMappingMatched_Type()
)
axFixedNatDsliteEndpointIndependentMappingMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatDsliteEndpointIndependentMappingMatched.setStatus("current")


class _AxFixedNatDsliteEndpointIndependentFilteringMatched_Type(CounterBasedGauge64):
    """Custom type axFixedNatDsliteEndpointIndependentFilteringMatched based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatDsliteEndpointIndependentFilteringMatched_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatDsliteEndpointIndependentFilteringMatched_Object = MibScalar
axFixedNatDsliteEndpointIndependentFilteringMatched = _AxFixedNatDsliteEndpointIndependentFilteringMatched_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 20, 10),
    _AxFixedNatDsliteEndpointIndependentFilteringMatched_Type()
)
axFixedNatDsliteEndpointIndependentFilteringMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatDsliteEndpointIndependentFilteringMatched.setStatus("current")


class _AxFixedNatDsliteEndpointIndependentFilteringDrop_Type(CounterBasedGauge64):
    """Custom type axFixedNatDsliteEndpointIndependentFilteringDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatDsliteEndpointIndependentFilteringDrop_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatDsliteEndpointIndependentFilteringDrop_Object = MibScalar
axFixedNatDsliteEndpointIndependentFilteringDrop = _AxFixedNatDsliteEndpointIndependentFilteringDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 20, 11),
    _AxFixedNatDsliteEndpointIndependentFilteringDrop_Type()
)
axFixedNatDsliteEndpointIndependentFilteringDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatDsliteEndpointIndependentFilteringDrop.setStatus("current")


class _AxFixedNatDsliteEndpointIndependentFilteringLimitExceed_Type(CounterBasedGauge64):
    """Custom type axFixedNatDsliteEndpointIndependentFilteringLimitExceed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatDsliteEndpointIndependentFilteringLimitExceed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatDsliteEndpointIndependentFilteringLimitExceed_Object = MibScalar
axFixedNatDsliteEndpointIndependentFilteringLimitExceed = _AxFixedNatDsliteEndpointIndependentFilteringLimitExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 20, 12),
    _AxFixedNatDsliteEndpointIndependentFilteringLimitExceed_Type()
)
axFixedNatDsliteEndpointIndependentFilteringLimitExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatDsliteEndpointIndependentFilteringLimitExceed.setStatus("current")


class _AxFixedNatDsliteHairpinSessionCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatDsliteHairpinSessionCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatDsliteHairpinSessionCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatDsliteHairpinSessionCreated_Object = MibScalar
axFixedNatDsliteHairpinSessionCreated = _AxFixedNatDsliteHairpinSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 1, 20, 13),
    _AxFixedNatDsliteHairpinSessionCreated_Type()
)
axFixedNatDsliteHairpinSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatDsliteHairpinSessionCreated.setStatus("current")
_AxFixedNatAlgStats_ObjectIdentity = ObjectIdentity
axFixedNatAlgStats = _AxFixedNatAlgStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2)
)
_AxFixedNatAlgEspStats_ObjectIdentity = ObjectIdentity
axFixedNatAlgEspStats = _AxFixedNatAlgEspStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 1)
)


class _AxFixedNatAlgEspSessionCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgEspSessionCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgEspSessionCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgEspSessionCreated_Object = MibScalar
axFixedNatAlgEspSessionCreated = _AxFixedNatAlgEspSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 1, 1),
    _AxFixedNatAlgEspSessionCreated_Type()
)
axFixedNatAlgEspSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgEspSessionCreated.setStatus("current")
_AxFixedNatAlgFtpStats_ObjectIdentity = ObjectIdentity
axFixedNatAlgFtpStats = _AxFixedNatAlgFtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 2)
)


class _AxFixedNatAlgFtpPortReqFromClient_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgFtpPortReqFromClient based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgFtpPortReqFromClient_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgFtpPortReqFromClient_Object = MibScalar
axFixedNatAlgFtpPortReqFromClient = _AxFixedNatAlgFtpPortReqFromClient_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 2, 1),
    _AxFixedNatAlgFtpPortReqFromClient_Type()
)
axFixedNatAlgFtpPortReqFromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgFtpPortReqFromClient.setStatus("current")


class _AxFixedNatAlgFtpEprtReqFromClient_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgFtpEprtReqFromClient based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgFtpEprtReqFromClient_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgFtpEprtReqFromClient_Object = MibScalar
axFixedNatAlgFtpEprtReqFromClient = _AxFixedNatAlgFtpEprtReqFromClient_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 2, 2),
    _AxFixedNatAlgFtpEprtReqFromClient_Type()
)
axFixedNatAlgFtpEprtReqFromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgFtpEprtReqFromClient.setStatus("current")


class _AxFixedNatAlgFtpLprtReqFromClient_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgFtpLprtReqFromClient based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgFtpLprtReqFromClient_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgFtpLprtReqFromClient_Object = MibScalar
axFixedNatAlgFtpLprtReqFromClient = _AxFixedNatAlgFtpLprtReqFromClient_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 2, 3),
    _AxFixedNatAlgFtpLprtReqFromClient_Type()
)
axFixedNatAlgFtpLprtReqFromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgFtpLprtReqFromClient.setStatus("current")


class _AxFixedNatAlgFtpPasvRepFromServer_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgFtpPasvRepFromServer based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgFtpPasvRepFromServer_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgFtpPasvRepFromServer_Object = MibScalar
axFixedNatAlgFtpPasvRepFromServer = _AxFixedNatAlgFtpPasvRepFromServer_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 2, 4),
    _AxFixedNatAlgFtpPasvRepFromServer_Type()
)
axFixedNatAlgFtpPasvRepFromServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgFtpPasvRepFromServer.setStatus("current")


class _AxFixedNatAlgFtpEpsvRepFromServer_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgFtpEpsvRepFromServer based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgFtpEpsvRepFromServer_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgFtpEpsvRepFromServer_Object = MibScalar
axFixedNatAlgFtpEpsvRepFromServer = _AxFixedNatAlgFtpEpsvRepFromServer_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 2, 5),
    _AxFixedNatAlgFtpEpsvRepFromServer_Type()
)
axFixedNatAlgFtpEpsvRepFromServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgFtpEpsvRepFromServer.setStatus("current")


class _AxFixedNatAlgFtpLpsvRepFromServer_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgFtpLpsvRepFromServer based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgFtpLpsvRepFromServer_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgFtpLpsvRepFromServer_Object = MibScalar
axFixedNatAlgFtpLpsvRepFromServer = _AxFixedNatAlgFtpLpsvRepFromServer_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 2, 6),
    _AxFixedNatAlgFtpLpsvRepFromServer_Type()
)
axFixedNatAlgFtpLpsvRepFromServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgFtpLpsvRepFromServer.setStatus("current")
_AxFixedNatAlgH323Stats_ObjectIdentity = ObjectIdentity
axFixedNatAlgH323Stats = _AxFixedNatAlgH323Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 3)
)


class _AxFixedNatAlgH323H225RasMsg_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgH323H225RasMsg based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgH323H225RasMsg_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgH323H225RasMsg_Object = MibScalar
axFixedNatAlgH323H225RasMsg = _AxFixedNatAlgH323H225RasMsg_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 3, 1),
    _AxFixedNatAlgH323H225RasMsg_Type()
)
axFixedNatAlgH323H225RasMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgH323H225RasMsg.setStatus("current")


class _AxFixedNatAlgH323H225CallSigMsg_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgH323H225CallSigMsg based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgH323H225CallSigMsg_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgH323H225CallSigMsg_Object = MibScalar
axFixedNatAlgH323H225CallSigMsg = _AxFixedNatAlgH323H225CallSigMsg_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 3, 2),
    _AxFixedNatAlgH323H225CallSigMsg_Type()
)
axFixedNatAlgH323H225CallSigMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgH323H225CallSigMsg.setStatus("current")


class _AxFixedNatAlgH323H245MedCtrMsg_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgH323H245MedCtrMsg based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgH323H245MedCtrMsg_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgH323H245MedCtrMsg_Object = MibScalar
axFixedNatAlgH323H245MedCtrMsg = _AxFixedNatAlgH323H245MedCtrMsg_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 3, 3),
    _AxFixedNatAlgH323H245MedCtrMsg_Type()
)
axFixedNatAlgH323H245MedCtrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgH323H245MedCtrMsg.setStatus("current")


class _AxFixedNatAlgH323H245TunnelMsg_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgH323H245TunnelMsg based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgH323H245TunnelMsg_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgH323H245TunnelMsg_Object = MibScalar
axFixedNatAlgH323H245TunnelMsg = _AxFixedNatAlgH323H245TunnelMsg_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 3, 4),
    _AxFixedNatAlgH323H245TunnelMsg_Type()
)
axFixedNatAlgH323H245TunnelMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgH323H245TunnelMsg.setStatus("current")


class _AxFixedNatAlgH323FastStart_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgH323FastStart based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgH323FastStart_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgH323FastStart_Object = MibScalar
axFixedNatAlgH323FastStart = _AxFixedNatAlgH323FastStart_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 3, 5),
    _AxFixedNatAlgH323FastStart_Type()
)
axFixedNatAlgH323FastStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgH323FastStart.setStatus("current")
_AxFixedNatAlgPptpStats_ObjectIdentity = ObjectIdentity
axFixedNatAlgPptpStats = _AxFixedNatAlgPptpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 4)
)


class _AxFixedNatAlgPptpCallEsp_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgPptpCallEsp based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgPptpCallEsp_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgPptpCallEsp_Object = MibScalar
axFixedNatAlgPptpCallEsp = _AxFixedNatAlgPptpCallEsp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 4, 1),
    _AxFixedNatAlgPptpCallEsp_Type()
)
axFixedNatAlgPptpCallEsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgPptpCallEsp.setStatus("current")


class _AxFixedNatAlgPptpMismatchedPnsCallId_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgPptpMismatchedPnsCallId based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgPptpMismatchedPnsCallId_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgPptpMismatchedPnsCallId_Object = MibScalar
axFixedNatAlgPptpMismatchedPnsCallId = _AxFixedNatAlgPptpMismatchedPnsCallId_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 4, 2),
    _AxFixedNatAlgPptpMismatchedPnsCallId_Type()
)
axFixedNatAlgPptpMismatchedPnsCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgPptpMismatchedPnsCallId.setStatus("current")


class _AxFixedNatAlgPptpGreSessionCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgPptpGreSessionCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgPptpGreSessionCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgPptpGreSessionCreated_Object = MibScalar
axFixedNatAlgPptpGreSessionCreated = _AxFixedNatAlgPptpGreSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 4, 3),
    _AxFixedNatAlgPptpGreSessionCreated_Type()
)
axFixedNatAlgPptpGreSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgPptpGreSessionCreated.setStatus("current")


class _AxFixedNatAlgPptpGreSessionFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgPptpGreSessionFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgPptpGreSessionFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgPptpGreSessionFreed_Object = MibScalar
axFixedNatAlgPptpGreSessionFreed = _AxFixedNatAlgPptpGreSessionFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 4, 4),
    _AxFixedNatAlgPptpGreSessionFreed_Type()
)
axFixedNatAlgPptpGreSessionFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgPptpGreSessionFreed.setStatus("current")


class _AxFixedNatAlgPptpGreNoMatchGreSession_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgPptpGreNoMatchGreSession based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgPptpGreNoMatchGreSession_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgPptpGreNoMatchGreSession_Object = MibScalar
axFixedNatAlgPptpGreNoMatchGreSession = _AxFixedNatAlgPptpGreNoMatchGreSession_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 4, 5),
    _AxFixedNatAlgPptpGreNoMatchGreSession_Type()
)
axFixedNatAlgPptpGreNoMatchGreSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgPptpGreNoMatchGreSession.setStatus("current")
_AxFixedNatAlgRtspStats_ObjectIdentity = ObjectIdentity
axFixedNatAlgRtspStats = _AxFixedNatAlgRtspStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 5)
)


class _AxFixedNatAlgRtspStreamCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgRtspStreamCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgRtspStreamCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgRtspStreamCreated_Object = MibScalar
axFixedNatAlgRtspStreamCreated = _AxFixedNatAlgRtspStreamCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 5, 1),
    _AxFixedNatAlgRtspStreamCreated_Type()
)
axFixedNatAlgRtspStreamCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgRtspStreamCreated.setStatus("current")


class _AxFixedNatAlgRtspStreamFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgRtspStreamFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgRtspStreamFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgRtspStreamFreed_Object = MibScalar
axFixedNatAlgRtspStreamFreed = _AxFixedNatAlgRtspStreamFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 5, 2),
    _AxFixedNatAlgRtspStreamFreed_Type()
)
axFixedNatAlgRtspStreamFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgRtspStreamFreed.setStatus("current")


class _AxFixedNatAlgRtspStreamCreationFailed_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgRtspStreamCreationFailed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgRtspStreamCreationFailed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgRtspStreamCreationFailed_Object = MibScalar
axFixedNatAlgRtspStreamCreationFailed = _AxFixedNatAlgRtspStreamCreationFailed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 5, 3),
    _AxFixedNatAlgRtspStreamCreationFailed_Type()
)
axFixedNatAlgRtspStreamCreationFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgRtspStreamCreationFailed.setStatus("current")


class _AxFixedNatAlgRtspStreamClientPortAllocated_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgRtspStreamClientPortAllocated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgRtspStreamClientPortAllocated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgRtspStreamClientPortAllocated_Object = MibScalar
axFixedNatAlgRtspStreamClientPortAllocated = _AxFixedNatAlgRtspStreamClientPortAllocated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 5, 4),
    _AxFixedNatAlgRtspStreamClientPortAllocated_Type()
)
axFixedNatAlgRtspStreamClientPortAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgRtspStreamClientPortAllocated.setStatus("current")


class _AxFixedNatAlgRtspStreamClientPortFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgRtspStreamClientPortFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgRtspStreamClientPortFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgRtspStreamClientPortFreed_Object = MibScalar
axFixedNatAlgRtspStreamClientPortFreed = _AxFixedNatAlgRtspStreamClientPortFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 5, 5),
    _AxFixedNatAlgRtspStreamClientPortFreed_Type()
)
axFixedNatAlgRtspStreamClientPortFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgRtspStreamClientPortFreed.setStatus("current")


class _AxFixedNatAlgRtspStreamClientPortAllocationFailed_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgRtspStreamClientPortAllocationFailed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgRtspStreamClientPortAllocationFailed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgRtspStreamClientPortAllocationFailed_Object = MibScalar
axFixedNatAlgRtspStreamClientPortAllocationFailed = _AxFixedNatAlgRtspStreamClientPortAllocationFailed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 5, 6),
    _AxFixedNatAlgRtspStreamClientPortAllocationFailed_Type()
)
axFixedNatAlgRtspStreamClientPortAllocationFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgRtspStreamClientPortAllocationFailed.setStatus("current")


class _AxFixedNatAlgRtspSrvRepWithUnknownClientPorts_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgRtspSrvRepWithUnknownClientPorts based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgRtspSrvRepWithUnknownClientPorts_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgRtspSrvRepWithUnknownClientPorts_Object = MibScalar
axFixedNatAlgRtspSrvRepWithUnknownClientPorts = _AxFixedNatAlgRtspSrvRepWithUnknownClientPorts_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 5, 7),
    _AxFixedNatAlgRtspSrvRepWithUnknownClientPorts_Type()
)
axFixedNatAlgRtspSrvRepWithUnknownClientPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgRtspSrvRepWithUnknownClientPorts.setStatus("current")


class _AxFixedNatAlgRtspDataSessionCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgRtspDataSessionCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgRtspDataSessionCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgRtspDataSessionCreated_Object = MibScalar
axFixedNatAlgRtspDataSessionCreated = _AxFixedNatAlgRtspDataSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 5, 8),
    _AxFixedNatAlgRtspDataSessionCreated_Type()
)
axFixedNatAlgRtspDataSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgRtspDataSessionCreated.setStatus("current")


class _AxFixedNatAlgRtspDataSessionFreed_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgRtspDataSessionFreed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgRtspDataSessionFreed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgRtspDataSessionFreed_Object = MibScalar
axFixedNatAlgRtspDataSessionFreed = _AxFixedNatAlgRtspDataSessionFreed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 5, 9),
    _AxFixedNatAlgRtspDataSessionFreed_Type()
)
axFixedNatAlgRtspDataSessionFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgRtspDataSessionFreed.setStatus("current")


class _AxFixedNatAlgRtspDataSessionCreationFailed_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgRtspDataSessionCreationFailed based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgRtspDataSessionCreationFailed_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgRtspDataSessionCreationFailed_Object = MibScalar
axFixedNatAlgRtspDataSessionCreationFailed = _AxFixedNatAlgRtspDataSessionCreationFailed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 5, 10),
    _AxFixedNatAlgRtspDataSessionCreationFailed_Type()
)
axFixedNatAlgRtspDataSessionCreationFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgRtspDataSessionCreationFailed.setStatus("current")
_AxFixedNatAlgSipStats_ObjectIdentity = ObjectIdentity
axFixedNatAlgSipStats = _AxFixedNatAlgSipStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 6)
)


class _AxFixedNatAlgSipMethodReg_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgSipMethodReg based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgSipMethodReg_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgSipMethodReg_Object = MibScalar
axFixedNatAlgSipMethodReg = _AxFixedNatAlgSipMethodReg_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 6, 1),
    _AxFixedNatAlgSipMethodReg_Type()
)
axFixedNatAlgSipMethodReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgSipMethodReg.setStatus("current")


class _AxFixedNatAlgSipMethodInvite_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgSipMethodInvite based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgSipMethodInvite_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgSipMethodInvite_Object = MibScalar
axFixedNatAlgSipMethodInvite = _AxFixedNatAlgSipMethodInvite_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 6, 2),
    _AxFixedNatAlgSipMethodInvite_Type()
)
axFixedNatAlgSipMethodInvite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgSipMethodInvite.setStatus("current")


class _AxFixedNatAlgSipMethodAck_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgSipMethodAck based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgSipMethodAck_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgSipMethodAck_Object = MibScalar
axFixedNatAlgSipMethodAck = _AxFixedNatAlgSipMethodAck_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 6, 3),
    _AxFixedNatAlgSipMethodAck_Type()
)
axFixedNatAlgSipMethodAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgSipMethodAck.setStatus("current")


class _AxFixedNatAlgSipMethodCancel_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgSipMethodCancel based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgSipMethodCancel_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgSipMethodCancel_Object = MibScalar
axFixedNatAlgSipMethodCancel = _AxFixedNatAlgSipMethodCancel_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 6, 4),
    _AxFixedNatAlgSipMethodCancel_Type()
)
axFixedNatAlgSipMethodCancel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgSipMethodCancel.setStatus("current")


class _AxFixedNatAlgSipMethodBye_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgSipMethodBye based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgSipMethodBye_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgSipMethodBye_Object = MibScalar
axFixedNatAlgSipMethodBye = _AxFixedNatAlgSipMethodBye_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 6, 5),
    _AxFixedNatAlgSipMethodBye_Type()
)
axFixedNatAlgSipMethodBye.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgSipMethodBye.setStatus("current")


class _AxFixedNatAlgSipMethodOptions_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgSipMethodOptions based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgSipMethodOptions_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgSipMethodOptions_Object = MibScalar
axFixedNatAlgSipMethodOptions = _AxFixedNatAlgSipMethodOptions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 6, 6),
    _AxFixedNatAlgSipMethodOptions_Type()
)
axFixedNatAlgSipMethodOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgSipMethodOptions.setStatus("current")


class _AxFixedNatAlgSipMethodPrack_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgSipMethodPrack based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgSipMethodPrack_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgSipMethodPrack_Object = MibScalar
axFixedNatAlgSipMethodPrack = _AxFixedNatAlgSipMethodPrack_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 6, 7),
    _AxFixedNatAlgSipMethodPrack_Type()
)
axFixedNatAlgSipMethodPrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgSipMethodPrack.setStatus("current")


class _AxFixedNatAlgSipMethodSubscribe_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgSipMethodSubscribe based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgSipMethodSubscribe_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgSipMethodSubscribe_Object = MibScalar
axFixedNatAlgSipMethodSubscribe = _AxFixedNatAlgSipMethodSubscribe_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 6, 8),
    _AxFixedNatAlgSipMethodSubscribe_Type()
)
axFixedNatAlgSipMethodSubscribe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgSipMethodSubscribe.setStatus("current")


class _AxFixedNatAlgSipMethodNotify_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgSipMethodNotify based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgSipMethodNotify_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgSipMethodNotify_Object = MibScalar
axFixedNatAlgSipMethodNotify = _AxFixedNatAlgSipMethodNotify_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 6, 9),
    _AxFixedNatAlgSipMethodNotify_Type()
)
axFixedNatAlgSipMethodNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgSipMethodNotify.setStatus("current")


class _AxFixedNatAlgSipMethodPublish_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgSipMethodPublish based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgSipMethodPublish_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgSipMethodPublish_Object = MibScalar
axFixedNatAlgSipMethodPublish = _AxFixedNatAlgSipMethodPublish_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 6, 10),
    _AxFixedNatAlgSipMethodPublish_Type()
)
axFixedNatAlgSipMethodPublish.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgSipMethodPublish.setStatus("current")


class _AxFixedNatAlgSipMethodInfo_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgSipMethodInfo based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgSipMethodInfo_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgSipMethodInfo_Object = MibScalar
axFixedNatAlgSipMethodInfo = _AxFixedNatAlgSipMethodInfo_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 6, 11),
    _AxFixedNatAlgSipMethodInfo_Type()
)
axFixedNatAlgSipMethodInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgSipMethodInfo.setStatus("current")


class _AxFixedNatAlgSipMethodRefer_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgSipMethodRefer based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgSipMethodRefer_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgSipMethodRefer_Object = MibScalar
axFixedNatAlgSipMethodRefer = _AxFixedNatAlgSipMethodRefer_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 6, 12),
    _AxFixedNatAlgSipMethodRefer_Type()
)
axFixedNatAlgSipMethodRefer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgSipMethodRefer.setStatus("current")


class _AxFixedNatAlgSipMethodMessage_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgSipMethodMessage based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgSipMethodMessage_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgSipMethodMessage_Object = MibScalar
axFixedNatAlgSipMethodMessage = _AxFixedNatAlgSipMethodMessage_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 6, 13),
    _AxFixedNatAlgSipMethodMessage_Type()
)
axFixedNatAlgSipMethodMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgSipMethodMessage.setStatus("current")


class _AxFixedNatAlgSipMethodUpdate_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgSipMethodUpdate based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgSipMethodUpdate_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgSipMethodUpdate_Object = MibScalar
axFixedNatAlgSipMethodUpdate = _AxFixedNatAlgSipMethodUpdate_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 6, 14),
    _AxFixedNatAlgSipMethodUpdate_Type()
)
axFixedNatAlgSipMethodUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgSipMethodUpdate.setStatus("current")


class _AxFixedNatAlgSipMethodUnknown_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgSipMethodUnknown based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgSipMethodUnknown_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgSipMethodUnknown_Object = MibScalar
axFixedNatAlgSipMethodUnknown = _AxFixedNatAlgSipMethodUnknown_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 6, 15),
    _AxFixedNatAlgSipMethodUnknown_Type()
)
axFixedNatAlgSipMethodUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgSipMethodUnknown.setStatus("current")
_AxFixedNatAlgTftpStats_ObjectIdentity = ObjectIdentity
axFixedNatAlgTftpStats = _AxFixedNatAlgTftpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 7)
)


class _AxFixedNatAlgTftpClientSessionCreated_Type(CounterBasedGauge64):
    """Custom type axFixedNatAlgTftpClientSessionCreated based on CounterBasedGauge64"""
    defaultValue = 0


_AxFixedNatAlgTftpClientSessionCreated_Type.__name__ = "CounterBasedGauge64"
_AxFixedNatAlgTftpClientSessionCreated_Object = MibScalar
axFixedNatAlgTftpClientSessionCreated = _AxFixedNatAlgTftpClientSessionCreated_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 2, 7, 1),
    _AxFixedNatAlgTftpClientSessionCreated_Type()
)
axFixedNatAlgTftpClientSessionCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatAlgTftpClientSessionCreated.setStatus("current")
_AxFixedNatMapping_ObjectIdentity = ObjectIdentity
axFixedNatMapping = _AxFixedNatMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 3)
)
_AxFixedNatPortMappingPortTable_Object = MibTable
axFixedNatPortMappingPortTable = _AxFixedNatPortMappingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 3, 1)
)
if mibBuilder.loadTexts:
    axFixedNatPortMappingPortTable.setStatus("current")
_AxFixedNatPortMappingPortEntry_Object = MibTableRow
axFixedNatPortMappingPortEntry = _AxFixedNatPortMappingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 3, 1, 1)
)
axFixedNatPortMappingPortEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axFixedNatPortMappingPortNatIpAddress"),
    (0, "A10-AX-CGN-MIB", "axFixedNatPortMappingPortInsideUser"),
)
if mibBuilder.loadTexts:
    axFixedNatPortMappingPortEntry.setStatus("current")
_AxFixedNatPortMappingPortNatIpAddress_Type = DisplayString
_AxFixedNatPortMappingPortNatIpAddress_Object = MibTableColumn
axFixedNatPortMappingPortNatIpAddress = _AxFixedNatPortMappingPortNatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 3, 1, 1, 1),
    _AxFixedNatPortMappingPortNatIpAddress_Type()
)
axFixedNatPortMappingPortNatIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatPortMappingPortNatIpAddress.setStatus("current")
_AxFixedNatPortMappingPortInsideUser_Type = DisplayString
_AxFixedNatPortMappingPortInsideUser_Object = MibTableColumn
axFixedNatPortMappingPortInsideUser = _AxFixedNatPortMappingPortInsideUser_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 3, 1, 1, 2),
    _AxFixedNatPortMappingPortInsideUser_Type()
)
axFixedNatPortMappingPortInsideUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatPortMappingPortInsideUser.setStatus("current")


class _AxFixedNatPortMappingPortInsideUserIpType_Type(Integer32):
    """Custom type axFixedNatPortMappingPortInsideUserIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1),
          ("dynamic", 2))
    )


_AxFixedNatPortMappingPortInsideUserIpType_Type.__name__ = "Integer32"
_AxFixedNatPortMappingPortInsideUserIpType_Object = MibTableColumn
axFixedNatPortMappingPortInsideUserIpType = _AxFixedNatPortMappingPortInsideUserIpType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 3, 1, 1, 3),
    _AxFixedNatPortMappingPortInsideUserIpType_Type()
)
axFixedNatPortMappingPortInsideUserIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatPortMappingPortInsideUserIpType.setStatus("current")
_AxFixedNatPortMappingPortTcpBeginPort_Type = Integer32
_AxFixedNatPortMappingPortTcpBeginPort_Object = MibTableColumn
axFixedNatPortMappingPortTcpBeginPort = _AxFixedNatPortMappingPortTcpBeginPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 3, 1, 1, 4),
    _AxFixedNatPortMappingPortTcpBeginPort_Type()
)
axFixedNatPortMappingPortTcpBeginPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatPortMappingPortTcpBeginPort.setStatus("current")
_AxFixedNatPortMappingPortTcpEndPort_Type = Integer32
_AxFixedNatPortMappingPortTcpEndPort_Object = MibTableColumn
axFixedNatPortMappingPortTcpEndPort = _AxFixedNatPortMappingPortTcpEndPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 3, 1, 1, 5),
    _AxFixedNatPortMappingPortTcpEndPort_Type()
)
axFixedNatPortMappingPortTcpEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatPortMappingPortTcpEndPort.setStatus("current")
_AxFixedNatPortMappingPortUdpBeginPort_Type = Integer32
_AxFixedNatPortMappingPortUdpBeginPort_Object = MibTableColumn
axFixedNatPortMappingPortUdpBeginPort = _AxFixedNatPortMappingPortUdpBeginPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 3, 1, 1, 6),
    _AxFixedNatPortMappingPortUdpBeginPort_Type()
)
axFixedNatPortMappingPortUdpBeginPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatPortMappingPortUdpBeginPort.setStatus("current")
_AxFixedNatPortMappingPortUdpEndPort_Type = Integer32
_AxFixedNatPortMappingPortUdpEndPort_Object = MibTableColumn
axFixedNatPortMappingPortUdpEndPort = _AxFixedNatPortMappingPortUdpEndPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 3, 1, 1, 7),
    _AxFixedNatPortMappingPortUdpEndPort_Type()
)
axFixedNatPortMappingPortUdpEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatPortMappingPortUdpEndPort.setStatus("current")
_AxFixedNatPortMappingPortIcmpBeginPort_Type = Integer32
_AxFixedNatPortMappingPortIcmpBeginPort_Object = MibTableColumn
axFixedNatPortMappingPortIcmpBeginPort = _AxFixedNatPortMappingPortIcmpBeginPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 3, 1, 1, 8),
    _AxFixedNatPortMappingPortIcmpBeginPort_Type()
)
axFixedNatPortMappingPortIcmpBeginPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatPortMappingPortIcmpBeginPort.setStatus("current")
_AxFixedNatPortMappingPortIcmpEndPort_Type = Integer32
_AxFixedNatPortMappingPortIcmpEndPort_Object = MibTableColumn
axFixedNatPortMappingPortIcmpEndPort = _AxFixedNatPortMappingPortIcmpEndPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 3, 1, 1, 9),
    _AxFixedNatPortMappingPortIcmpEndPort_Type()
)
axFixedNatPortMappingPortIcmpEndPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatPortMappingPortIcmpEndPort.setStatus("current")
_AxFixedNatFullConeSess_ObjectIdentity = ObjectIdentity
axFixedNatFullConeSess = _AxFixedNatFullConeSess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4)
)
_AxFixedNatFullConeSessDsliteTable_Object = MibTable
axFixedNatFullConeSessDsliteTable = _AxFixedNatFullConeSessDsliteTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 1)
)
if mibBuilder.loadTexts:
    axFixedNatFullConeSessDsliteTable.setStatus("current")
_AxFixedNatFullConeSessDsliteEntry_Object = MibTableRow
axFixedNatFullConeSessDsliteEntry = _AxFixedNatFullConeSessDsliteEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 1, 1)
)
axFixedNatFullConeSessDsliteEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axFixedNatFullConeSessDsliteNatIpAddress"),
    (0, "A10-AX-CGN-MIB", "axFixedNatFullConeSessDsliteInsideUser"),
    (0, "A10-AX-CGN-MIB", "axFixedNatFullConeSessDsliteProtType"),
)
if mibBuilder.loadTexts:
    axFixedNatFullConeSessDsliteEntry.setStatus("current")
_AxFixedNatFullConeSessDsliteNatIpAddress_Type = DisplayString
_AxFixedNatFullConeSessDsliteNatIpAddress_Object = MibTableColumn
axFixedNatFullConeSessDsliteNatIpAddress = _AxFixedNatFullConeSessDsliteNatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 1, 1, 1),
    _AxFixedNatFullConeSessDsliteNatIpAddress_Type()
)
axFixedNatFullConeSessDsliteNatIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessDsliteNatIpAddress.setStatus("current")
_AxFixedNatFullConeSessDsliteInsideUser_Type = DisplayString
_AxFixedNatFullConeSessDsliteInsideUser_Object = MibTableColumn
axFixedNatFullConeSessDsliteInsideUser = _AxFixedNatFullConeSessDsliteInsideUser_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 1, 1, 2),
    _AxFixedNatFullConeSessDsliteInsideUser_Type()
)
axFixedNatFullConeSessDsliteInsideUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessDsliteInsideUser.setStatus("current")


class _AxFixedNatFullConeSessDsliteProtType_Type(Integer32):
    """Custom type axFixedNatFullConeSessDsliteProtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("tcp", 1),
          ("udp", 2),
          ("alg", 3))
    )


_AxFixedNatFullConeSessDsliteProtType_Type.__name__ = "Integer32"
_AxFixedNatFullConeSessDsliteProtType_Object = MibTableColumn
axFixedNatFullConeSessDsliteProtType = _AxFixedNatFullConeSessDsliteProtType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 1, 1, 3),
    _AxFixedNatFullConeSessDsliteProtType_Type()
)
axFixedNatFullConeSessDsliteProtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessDsliteProtType.setStatus("current")
_AxFixedNatFullConeSessDsliteEIM_Type = Integer32
_AxFixedNatFullConeSessDsliteEIM_Object = MibTableColumn
axFixedNatFullConeSessDsliteEIM = _AxFixedNatFullConeSessDsliteEIM_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 1, 1, 4),
    _AxFixedNatFullConeSessDsliteEIM_Type()
)
axFixedNatFullConeSessDsliteEIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessDsliteEIM.setStatus("current")
_AxFixedNatFullConeSessDsliteEIF_Type = Integer32
_AxFixedNatFullConeSessDsliteEIF_Object = MibTableColumn
axFixedNatFullConeSessDsliteEIF = _AxFixedNatFullConeSessDsliteEIF_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 1, 1, 5),
    _AxFixedNatFullConeSessDsliteEIF_Type()
)
axFixedNatFullConeSessDsliteEIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessDsliteEIF.setStatus("current")
_AxFixedNatFullConeSessDsliteCPU_Type = Integer32
_AxFixedNatFullConeSessDsliteCPU_Object = MibTableColumn
axFixedNatFullConeSessDsliteCPU = _AxFixedNatFullConeSessDsliteCPU_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 1, 1, 6),
    _AxFixedNatFullConeSessDsliteCPU_Type()
)
axFixedNatFullConeSessDsliteCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessDsliteCPU.setStatus("current")
_AxFixedNatFullConeSessDsliteAge_Type = Integer32
_AxFixedNatFullConeSessDsliteAge_Object = MibTableColumn
axFixedNatFullConeSessDsliteAge = _AxFixedNatFullConeSessDsliteAge_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 1, 1, 7),
    _AxFixedNatFullConeSessDsliteAge_Type()
)
axFixedNatFullConeSessDsliteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessDsliteAge.setStatus("current")


class _AxFixedNatFullConeSessDslitePcpFlags_Type(Integer32):
    """Custom type axFixedNatFullConeSessDslitePcpFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("pcp", 1))
    )


_AxFixedNatFullConeSessDslitePcpFlags_Type.__name__ = "Integer32"
_AxFixedNatFullConeSessDslitePcpFlags_Object = MibTableColumn
axFixedNatFullConeSessDslitePcpFlags = _AxFixedNatFullConeSessDslitePcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 1, 1, 8),
    _AxFixedNatFullConeSessDslitePcpFlags_Type()
)
axFixedNatFullConeSessDslitePcpFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessDslitePcpFlags.setStatus("current")
_AxFixedNatFullConeSessNat44Table_Object = MibTable
axFixedNatFullConeSessNat44Table = _AxFixedNatFullConeSessNat44Table_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 2)
)
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat44Table.setStatus("current")
_AxFixedNatFullConeSessNat44Entry_Object = MibTableRow
axFixedNatFullConeSessNat44Entry = _AxFixedNatFullConeSessNat44Entry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 2, 1)
)
axFixedNatFullConeSessNat44Entry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axFixedNatFullConeSessNat44NatIpAddress"),
    (0, "A10-AX-CGN-MIB", "axFixedNatFullConeSessNat44InsideUser"),
    (0, "A10-AX-CGN-MIB", "axFixedNatFullConeSessNat44ProtType"),
)
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat44Entry.setStatus("current")
_AxFixedNatFullConeSessNat44NatIpAddress_Type = DisplayString
_AxFixedNatFullConeSessNat44NatIpAddress_Object = MibTableColumn
axFixedNatFullConeSessNat44NatIpAddress = _AxFixedNatFullConeSessNat44NatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 2, 1, 1),
    _AxFixedNatFullConeSessNat44NatIpAddress_Type()
)
axFixedNatFullConeSessNat44NatIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat44NatIpAddress.setStatus("current")
_AxFixedNatFullConeSessNat44InsideUser_Type = DisplayString
_AxFixedNatFullConeSessNat44InsideUser_Object = MibTableColumn
axFixedNatFullConeSessNat44InsideUser = _AxFixedNatFullConeSessNat44InsideUser_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 2, 1, 2),
    _AxFixedNatFullConeSessNat44InsideUser_Type()
)
axFixedNatFullConeSessNat44InsideUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat44InsideUser.setStatus("current")


class _AxFixedNatFullConeSessNat44ProtType_Type(Integer32):
    """Custom type axFixedNatFullConeSessNat44ProtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("tcp", 1),
          ("udp", 2),
          ("alg", 3))
    )


_AxFixedNatFullConeSessNat44ProtType_Type.__name__ = "Integer32"
_AxFixedNatFullConeSessNat44ProtType_Object = MibTableColumn
axFixedNatFullConeSessNat44ProtType = _AxFixedNatFullConeSessNat44ProtType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 2, 1, 3),
    _AxFixedNatFullConeSessNat44ProtType_Type()
)
axFixedNatFullConeSessNat44ProtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat44ProtType.setStatus("current")
_AxFixedNatFullConeSessNat44EIM_Type = Integer32
_AxFixedNatFullConeSessNat44EIM_Object = MibTableColumn
axFixedNatFullConeSessNat44EIM = _AxFixedNatFullConeSessNat44EIM_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 2, 1, 4),
    _AxFixedNatFullConeSessNat44EIM_Type()
)
axFixedNatFullConeSessNat44EIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat44EIM.setStatus("current")
_AxFixedNatFullConeSessNat44EIF_Type = Integer32
_AxFixedNatFullConeSessNat44EIF_Object = MibTableColumn
axFixedNatFullConeSessNat44EIF = _AxFixedNatFullConeSessNat44EIF_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 2, 1, 5),
    _AxFixedNatFullConeSessNat44EIF_Type()
)
axFixedNatFullConeSessNat44EIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat44EIF.setStatus("current")
_AxFixedNatFullConeSessNat44CPU_Type = Integer32
_AxFixedNatFullConeSessNat44CPU_Object = MibTableColumn
axFixedNatFullConeSessNat44CPU = _AxFixedNatFullConeSessNat44CPU_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 2, 1, 6),
    _AxFixedNatFullConeSessNat44CPU_Type()
)
axFixedNatFullConeSessNat44CPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat44CPU.setStatus("current")
_AxFixedNatFullConeSessNat44Age_Type = Integer32
_AxFixedNatFullConeSessNat44Age_Object = MibTableColumn
axFixedNatFullConeSessNat44Age = _AxFixedNatFullConeSessNat44Age_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 2, 1, 7),
    _AxFixedNatFullConeSessNat44Age_Type()
)
axFixedNatFullConeSessNat44Age.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat44Age.setStatus("current")


class _AxFixedNatFullConeSessNat44PcpFlags_Type(Integer32):
    """Custom type axFixedNatFullConeSessNat44PcpFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("pcp", 1))
    )


_AxFixedNatFullConeSessNat44PcpFlags_Type.__name__ = "Integer32"
_AxFixedNatFullConeSessNat44PcpFlags_Object = MibTableColumn
axFixedNatFullConeSessNat44PcpFlags = _AxFixedNatFullConeSessNat44PcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 2, 1, 8),
    _AxFixedNatFullConeSessNat44PcpFlags_Type()
)
axFixedNatFullConeSessNat44PcpFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat44PcpFlags.setStatus("current")
_AxFixedNatFullConeSessNat64Table_Object = MibTable
axFixedNatFullConeSessNat64Table = _AxFixedNatFullConeSessNat64Table_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 3)
)
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat64Table.setStatus("current")
_AxFixedNatFullConeSessNat64Entry_Object = MibTableRow
axFixedNatFullConeSessNat64Entry = _AxFixedNatFullConeSessNat64Entry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 3, 1)
)
axFixedNatFullConeSessNat64Entry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axFixedNatFullConeSessNat64NatIpAddress"),
    (0, "A10-AX-CGN-MIB", "axFixedNatFullConeSessNat64InsideUser"),
    (0, "A10-AX-CGN-MIB", "axFixedNatFullConeSessNat64ProtType"),
)
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat64Entry.setStatus("current")
_AxFixedNatFullConeSessNat64NatIpAddress_Type = DisplayString
_AxFixedNatFullConeSessNat64NatIpAddress_Object = MibTableColumn
axFixedNatFullConeSessNat64NatIpAddress = _AxFixedNatFullConeSessNat64NatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 3, 1, 1),
    _AxFixedNatFullConeSessNat64NatIpAddress_Type()
)
axFixedNatFullConeSessNat64NatIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat64NatIpAddress.setStatus("current")
_AxFixedNatFullConeSessNat64InsideUser_Type = DisplayString
_AxFixedNatFullConeSessNat64InsideUser_Object = MibTableColumn
axFixedNatFullConeSessNat64InsideUser = _AxFixedNatFullConeSessNat64InsideUser_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 3, 1, 2),
    _AxFixedNatFullConeSessNat64InsideUser_Type()
)
axFixedNatFullConeSessNat64InsideUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat64InsideUser.setStatus("current")


class _AxFixedNatFullConeSessNat64ProtType_Type(Integer32):
    """Custom type axFixedNatFullConeSessNat64ProtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("tcp", 1),
          ("udp", 2),
          ("alg", 3))
    )


_AxFixedNatFullConeSessNat64ProtType_Type.__name__ = "Integer32"
_AxFixedNatFullConeSessNat64ProtType_Object = MibTableColumn
axFixedNatFullConeSessNat64ProtType = _AxFixedNatFullConeSessNat64ProtType_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 3, 1, 3),
    _AxFixedNatFullConeSessNat64ProtType_Type()
)
axFixedNatFullConeSessNat64ProtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat64ProtType.setStatus("current")
_AxFixedNatFullConeSessNat64EIM_Type = Integer32
_AxFixedNatFullConeSessNat64EIM_Object = MibTableColumn
axFixedNatFullConeSessNat64EIM = _AxFixedNatFullConeSessNat64EIM_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 3, 1, 4),
    _AxFixedNatFullConeSessNat64EIM_Type()
)
axFixedNatFullConeSessNat64EIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat64EIM.setStatus("current")
_AxFixedNatFullConeSessNat64EIF_Type = Integer32
_AxFixedNatFullConeSessNat64EIF_Object = MibTableColumn
axFixedNatFullConeSessNat64EIF = _AxFixedNatFullConeSessNat64EIF_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 3, 1, 5),
    _AxFixedNatFullConeSessNat64EIF_Type()
)
axFixedNatFullConeSessNat64EIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat64EIF.setStatus("current")
_AxFixedNatFullConeSessNat64CPU_Type = Integer32
_AxFixedNatFullConeSessNat64CPU_Object = MibTableColumn
axFixedNatFullConeSessNat64CPU = _AxFixedNatFullConeSessNat64CPU_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 3, 1, 6),
    _AxFixedNatFullConeSessNat64CPU_Type()
)
axFixedNatFullConeSessNat64CPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat64CPU.setStatus("current")
_AxFixedNatFullConeSessNat64Age_Type = Integer32
_AxFixedNatFullConeSessNat64Age_Object = MibTableColumn
axFixedNatFullConeSessNat64Age = _AxFixedNatFullConeSessNat64Age_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 3, 1, 7),
    _AxFixedNatFullConeSessNat64Age_Type()
)
axFixedNatFullConeSessNat64Age.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat64Age.setStatus("current")


class _AxFixedNatFullConeSessNat64PcpFlags_Type(Integer32):
    """Custom type axFixedNatFullConeSessNat64PcpFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("pcp", 1))
    )


_AxFixedNatFullConeSessNat64PcpFlags_Type.__name__ = "Integer32"
_AxFixedNatFullConeSessNat64PcpFlags_Object = MibTableColumn
axFixedNatFullConeSessNat64PcpFlags = _AxFixedNatFullConeSessNat64PcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 4, 3, 1, 8),
    _AxFixedNatFullConeSessNat64PcpFlags_Type()
)
axFixedNatFullConeSessNat64PcpFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFullConeSessNat64PcpFlags.setStatus("current")
_AxFixedNatTop5PrivateIpAddrTotSessions_ObjectIdentity = ObjectIdentity
axFixedNatTop5PrivateIpAddrTotSessions = _AxFixedNatTop5PrivateIpAddrTotSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 5)
)
_AxFixedNatTop5PrivateIpAddrTotSessionTable_Object = MibTable
axFixedNatTop5PrivateIpAddrTotSessionTable = _AxFixedNatTop5PrivateIpAddrTotSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 5, 1)
)
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrTotSessionTable.setStatus("current")
_AxFixedNatTop5PrivateIpAddrTotSessionEntry_Object = MibTableRow
axFixedNatTop5PrivateIpAddrTotSessionEntry = _AxFixedNatTop5PrivateIpAddrTotSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 5, 1, 1)
)
axFixedNatTop5PrivateIpAddrTotSessionEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axFixedNatTop5PrivateIpAddr"),
)
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrTotSessionEntry.setStatus("current")
_AxFixedNatTop5PrivateIpAddr_Type = DisplayString
_AxFixedNatTop5PrivateIpAddr_Object = MibTableColumn
axFixedNatTop5PrivateIpAddr = _AxFixedNatTop5PrivateIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 5, 1, 1, 1),
    _AxFixedNatTop5PrivateIpAddr_Type()
)
axFixedNatTop5PrivateIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddr.setStatus("current")
_AxFixedNatTop5PrivateIpAddrTotNumSessions_Type = Integer32
_AxFixedNatTop5PrivateIpAddrTotNumSessions_Object = MibTableColumn
axFixedNatTop5PrivateIpAddrTotNumSessions = _AxFixedNatTop5PrivateIpAddrTotNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 5, 1, 1, 2),
    _AxFixedNatTop5PrivateIpAddrTotNumSessions_Type()
)
axFixedNatTop5PrivateIpAddrTotNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrTotNumSessions.setStatus("current")
_AxFixedNatTop5PrivateIpAddrGlobalIpAddr_Type = DisplayString
_AxFixedNatTop5PrivateIpAddrGlobalIpAddr_Object = MibTableColumn
axFixedNatTop5PrivateIpAddrGlobalIpAddr = _AxFixedNatTop5PrivateIpAddrGlobalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 5, 1, 1, 3),
    _AxFixedNatTop5PrivateIpAddrGlobalIpAddr_Type()
)
axFixedNatTop5PrivateIpAddrGlobalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrGlobalIpAddr.setStatus("current")
_AxFixedNatTop5PrivateIpAddrTotTcpPorts_ObjectIdentity = ObjectIdentity
axFixedNatTop5PrivateIpAddrTotTcpPorts = _AxFixedNatTop5PrivateIpAddrTotTcpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 6)
)
_AxFixedNatTop5PrivateIpAddrTotTcpPortTable_Object = MibTable
axFixedNatTop5PrivateIpAddrTotTcpPortTable = _AxFixedNatTop5PrivateIpAddrTotTcpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 6, 1)
)
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrTotTcpPortTable.setStatus("current")
_AxFixedNatTop5PrivateIpAddrTotTcpPortEntry_Object = MibTableRow
axFixedNatTop5PrivateIpAddrTotTcpPortEntry = _AxFixedNatTop5PrivateIpAddrTotTcpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 6, 1, 1)
)
axFixedNatTop5PrivateIpAddrTotTcpPortEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axFixedNatTop5PrivateIpAddrInTcpPort"),
)
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrTotTcpPortEntry.setStatus("current")
_AxFixedNatTop5PrivateIpAddrInTcpPort_Type = DisplayString
_AxFixedNatTop5PrivateIpAddrInTcpPort_Object = MibTableColumn
axFixedNatTop5PrivateIpAddrInTcpPort = _AxFixedNatTop5PrivateIpAddrInTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 6, 1, 1, 1),
    _AxFixedNatTop5PrivateIpAddrInTcpPort_Type()
)
axFixedNatTop5PrivateIpAddrInTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrInTcpPort.setStatus("current")
_AxFixedNatTop5PrivateIpAddrTotNumInTcpPort_Type = Integer32
_AxFixedNatTop5PrivateIpAddrTotNumInTcpPort_Object = MibTableColumn
axFixedNatTop5PrivateIpAddrTotNumInTcpPort = _AxFixedNatTop5PrivateIpAddrTotNumInTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 6, 1, 1, 2),
    _AxFixedNatTop5PrivateIpAddrTotNumInTcpPort_Type()
)
axFixedNatTop5PrivateIpAddrTotNumInTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrTotNumInTcpPort.setStatus("current")
_AxFixedNatTop5PrivateIpAddrGlobalIpAddrInTcpPort_Type = DisplayString
_AxFixedNatTop5PrivateIpAddrGlobalIpAddrInTcpPort_Object = MibTableColumn
axFixedNatTop5PrivateIpAddrGlobalIpAddrInTcpPort = _AxFixedNatTop5PrivateIpAddrGlobalIpAddrInTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 6, 1, 1, 3),
    _AxFixedNatTop5PrivateIpAddrGlobalIpAddrInTcpPort_Type()
)
axFixedNatTop5PrivateIpAddrGlobalIpAddrInTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrGlobalIpAddrInTcpPort.setStatus("current")
_AxFixedNatTop5PrivateIpAddrTotUdpPorts_ObjectIdentity = ObjectIdentity
axFixedNatTop5PrivateIpAddrTotUdpPorts = _AxFixedNatTop5PrivateIpAddrTotUdpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 7)
)
_AxFixedNatTop5PrivateIpAddrTotUdpPortTable_Object = MibTable
axFixedNatTop5PrivateIpAddrTotUdpPortTable = _AxFixedNatTop5PrivateIpAddrTotUdpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 7, 1)
)
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrTotUdpPortTable.setStatus("current")
_AxFixedNatTop5PrivateIpAddrTotUdpPortEntry_Object = MibTableRow
axFixedNatTop5PrivateIpAddrTotUdpPortEntry = _AxFixedNatTop5PrivateIpAddrTotUdpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 7, 1, 1)
)
axFixedNatTop5PrivateIpAddrTotUdpPortEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axFixedNatTop5PrivateIpAddrInUdpPort"),
)
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrTotUdpPortEntry.setStatus("current")
_AxFixedNatTop5PrivateIpAddrInUdpPort_Type = DisplayString
_AxFixedNatTop5PrivateIpAddrInUdpPort_Object = MibTableColumn
axFixedNatTop5PrivateIpAddrInUdpPort = _AxFixedNatTop5PrivateIpAddrInUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 7, 1, 1, 1),
    _AxFixedNatTop5PrivateIpAddrInUdpPort_Type()
)
axFixedNatTop5PrivateIpAddrInUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrInUdpPort.setStatus("current")
_AxFixedNatTop5PrivateIpAddrTotNumInUdpPort_Type = Integer32
_AxFixedNatTop5PrivateIpAddrTotNumInUdpPort_Object = MibTableColumn
axFixedNatTop5PrivateIpAddrTotNumInUdpPort = _AxFixedNatTop5PrivateIpAddrTotNumInUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 7, 1, 1, 2),
    _AxFixedNatTop5PrivateIpAddrTotNumInUdpPort_Type()
)
axFixedNatTop5PrivateIpAddrTotNumInUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrTotNumInUdpPort.setStatus("current")
_AxFixedNatTop5PrivateIpAddrGlobalIpAddrInUdpPort_Type = DisplayString
_AxFixedNatTop5PrivateIpAddrGlobalIpAddrInUdpPort_Object = MibTableColumn
axFixedNatTop5PrivateIpAddrGlobalIpAddrInUdpPort = _AxFixedNatTop5PrivateIpAddrGlobalIpAddrInUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 7, 1, 1, 3),
    _AxFixedNatTop5PrivateIpAddrGlobalIpAddrInUdpPort_Type()
)
axFixedNatTop5PrivateIpAddrGlobalIpAddrInUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrGlobalIpAddrInUdpPort.setStatus("current")
_AxFixedNatTop5PrivateIpAddrTotIcmpPorts_ObjectIdentity = ObjectIdentity
axFixedNatTop5PrivateIpAddrTotIcmpPorts = _AxFixedNatTop5PrivateIpAddrTotIcmpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 8)
)
_AxFixedNatTop5PrivateIpAddrTotIcmpPortTable_Object = MibTable
axFixedNatTop5PrivateIpAddrTotIcmpPortTable = _AxFixedNatTop5PrivateIpAddrTotIcmpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 8, 1)
)
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrTotIcmpPortTable.setStatus("current")
_AxFixedNatTop5PrivateIpAddrTotIcmpPortEntry_Object = MibTableRow
axFixedNatTop5PrivateIpAddrTotIcmpPortEntry = _AxFixedNatTop5PrivateIpAddrTotIcmpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 8, 1, 1)
)
axFixedNatTop5PrivateIpAddrTotIcmpPortEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axFixedNatTop5PrivateIpAddrInIcmpPort"),
)
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrTotIcmpPortEntry.setStatus("current")
_AxFixedNatTop5PrivateIpAddrInIcmpPort_Type = DisplayString
_AxFixedNatTop5PrivateIpAddrInIcmpPort_Object = MibTableColumn
axFixedNatTop5PrivateIpAddrInIcmpPort = _AxFixedNatTop5PrivateIpAddrInIcmpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 8, 1, 1, 1),
    _AxFixedNatTop5PrivateIpAddrInIcmpPort_Type()
)
axFixedNatTop5PrivateIpAddrInIcmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrInIcmpPort.setStatus("current")
_AxFixedNatTop5PrivateIpAddrTotNumInIcmpPort_Type = Integer32
_AxFixedNatTop5PrivateIpAddrTotNumInIcmpPort_Object = MibTableColumn
axFixedNatTop5PrivateIpAddrTotNumInIcmpPort = _AxFixedNatTop5PrivateIpAddrTotNumInIcmpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 8, 1, 1, 2),
    _AxFixedNatTop5PrivateIpAddrTotNumInIcmpPort_Type()
)
axFixedNatTop5PrivateIpAddrTotNumInIcmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrTotNumInIcmpPort.setStatus("current")
_AxFixedNatTop5PrivateIpAddrGlobalIpAddrInIcmpPort_Type = DisplayString
_AxFixedNatTop5PrivateIpAddrGlobalIpAddrInIcmpPort_Object = MibTableColumn
axFixedNatTop5PrivateIpAddrGlobalIpAddrInIcmpPort = _AxFixedNatTop5PrivateIpAddrGlobalIpAddrInIcmpPort_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 8, 1, 1, 3),
    _AxFixedNatTop5PrivateIpAddrGlobalIpAddrInIcmpPort_Type()
)
axFixedNatTop5PrivateIpAddrGlobalIpAddrInIcmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5PrivateIpAddrGlobalIpAddrInIcmpPort.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrTotSessions_ObjectIdentity = ObjectIdentity
axFixedNatTop5UserPrivateIpAddrTotSessions = _AxFixedNatTop5UserPrivateIpAddrTotSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 9)
)
_AxFixedNatTop5UserPrivateIpAddrTotSessionTable_Object = MibTable
axFixedNatTop5UserPrivateIpAddrTotSessionTable = _AxFixedNatTop5UserPrivateIpAddrTotSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 9, 1)
)
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrTotSessionTable.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrTotSessionEntry_Object = MibTableRow
axFixedNatTop5UserPrivateIpAddrTotSessionEntry = _AxFixedNatTop5UserPrivateIpAddrTotSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 9, 1, 1)
)
axFixedNatTop5UserPrivateIpAddrTotSessionEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axFixedNatTop5UserPrivateIpAddr"),
)
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrTotSessionEntry.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddr_Type = DisplayString
_AxFixedNatTop5UserPrivateIpAddr_Object = MibTableColumn
axFixedNatTop5UserPrivateIpAddr = _AxFixedNatTop5UserPrivateIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 9, 1, 1, 1),
    _AxFixedNatTop5UserPrivateIpAddr_Type()
)
axFixedNatTop5UserPrivateIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddr.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrTotNumSession_Type = Integer32
_AxFixedNatTop5UserPrivateIpAddrTotNumSession_Object = MibTableColumn
axFixedNatTop5UserPrivateIpAddrTotNumSession = _AxFixedNatTop5UserPrivateIpAddrTotNumSession_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 9, 1, 1, 2),
    _AxFixedNatTop5UserPrivateIpAddrTotNumSession_Type()
)
axFixedNatTop5UserPrivateIpAddrTotNumSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrTotNumSession.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrGlobalIpAddr_Type = DisplayString
_AxFixedNatTop5UserPrivateIpAddrGlobalIpAddr_Object = MibTableColumn
axFixedNatTop5UserPrivateIpAddrGlobalIpAddr = _AxFixedNatTop5UserPrivateIpAddrGlobalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 9, 1, 1, 3),
    _AxFixedNatTop5UserPrivateIpAddrGlobalIpAddr_Type()
)
axFixedNatTop5UserPrivateIpAddrGlobalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrGlobalIpAddr.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrTotTcpPorts_ObjectIdentity = ObjectIdentity
axFixedNatTop5UserPrivateIpAddrTotTcpPorts = _AxFixedNatTop5UserPrivateIpAddrTotTcpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 10)
)
_AxFixedNatTop5UserPrivateIpAddrTotTcpPortTable_Object = MibTable
axFixedNatTop5UserPrivateIpAddrTotTcpPortTable = _AxFixedNatTop5UserPrivateIpAddrTotTcpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 10, 1)
)
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrTotTcpPortTable.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrTotTcpPortEntry_Object = MibTableRow
axFixedNatTop5UserPrivateIpAddrTotTcpPortEntry = _AxFixedNatTop5UserPrivateIpAddrTotTcpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 10, 1, 1)
)
axFixedNatTop5UserPrivateIpAddrTotTcpPortEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axFixedNatTop5UserPrivateIpAddrInTcp"),
)
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrTotTcpPortEntry.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrInTcp_Type = DisplayString
_AxFixedNatTop5UserPrivateIpAddrInTcp_Object = MibTableColumn
axFixedNatTop5UserPrivateIpAddrInTcp = _AxFixedNatTop5UserPrivateIpAddrInTcp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 10, 1, 1, 1),
    _AxFixedNatTop5UserPrivateIpAddrInTcp_Type()
)
axFixedNatTop5UserPrivateIpAddrInTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrInTcp.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrTotNumInTcp_Type = Integer32
_AxFixedNatTop5UserPrivateIpAddrTotNumInTcp_Object = MibTableColumn
axFixedNatTop5UserPrivateIpAddrTotNumInTcp = _AxFixedNatTop5UserPrivateIpAddrTotNumInTcp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 10, 1, 1, 2),
    _AxFixedNatTop5UserPrivateIpAddrTotNumInTcp_Type()
)
axFixedNatTop5UserPrivateIpAddrTotNumInTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrTotNumInTcp.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrGlobalIpAddrInTcp_Type = DisplayString
_AxFixedNatTop5UserPrivateIpAddrGlobalIpAddrInTcp_Object = MibTableColumn
axFixedNatTop5UserPrivateIpAddrGlobalIpAddrInTcp = _AxFixedNatTop5UserPrivateIpAddrGlobalIpAddrInTcp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 10, 1, 1, 3),
    _AxFixedNatTop5UserPrivateIpAddrGlobalIpAddrInTcp_Type()
)
axFixedNatTop5UserPrivateIpAddrGlobalIpAddrInTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrGlobalIpAddrInTcp.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrTotUdpPorts_ObjectIdentity = ObjectIdentity
axFixedNatTop5UserPrivateIpAddrTotUdpPorts = _AxFixedNatTop5UserPrivateIpAddrTotUdpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 11)
)
_AxFixedNatTop5UserPrivateIpAddrTotUdpPortTable_Object = MibTable
axFixedNatTop5UserPrivateIpAddrTotUdpPortTable = _AxFixedNatTop5UserPrivateIpAddrTotUdpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 11, 1)
)
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrTotUdpPortTable.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrTotUdpPortEntry_Object = MibTableRow
axFixedNatTop5UserPrivateIpAddrTotUdpPortEntry = _AxFixedNatTop5UserPrivateIpAddrTotUdpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 11, 1, 1)
)
axFixedNatTop5UserPrivateIpAddrTotUdpPortEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axFixedNatTop5UserPrivateIpAddrInUdp"),
)
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrTotUdpPortEntry.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrInUdp_Type = DisplayString
_AxFixedNatTop5UserPrivateIpAddrInUdp_Object = MibTableColumn
axFixedNatTop5UserPrivateIpAddrInUdp = _AxFixedNatTop5UserPrivateIpAddrInUdp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 11, 1, 1, 1),
    _AxFixedNatTop5UserPrivateIpAddrInUdp_Type()
)
axFixedNatTop5UserPrivateIpAddrInUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrInUdp.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrTotNumInUdp_Type = Integer32
_AxFixedNatTop5UserPrivateIpAddrTotNumInUdp_Object = MibTableColumn
axFixedNatTop5UserPrivateIpAddrTotNumInUdp = _AxFixedNatTop5UserPrivateIpAddrTotNumInUdp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 11, 1, 1, 2),
    _AxFixedNatTop5UserPrivateIpAddrTotNumInUdp_Type()
)
axFixedNatTop5UserPrivateIpAddrTotNumInUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrTotNumInUdp.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrGlobalIpAddrInUdp_Type = DisplayString
_AxFixedNatTop5UserPrivateIpAddrGlobalIpAddrInUdp_Object = MibTableColumn
axFixedNatTop5UserPrivateIpAddrGlobalIpAddrInUdp = _AxFixedNatTop5UserPrivateIpAddrGlobalIpAddrInUdp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 11, 1, 1, 3),
    _AxFixedNatTop5UserPrivateIpAddrGlobalIpAddrInUdp_Type()
)
axFixedNatTop5UserPrivateIpAddrGlobalIpAddrInUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrGlobalIpAddrInUdp.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrTotIcmpPorts_ObjectIdentity = ObjectIdentity
axFixedNatTop5UserPrivateIpAddrTotIcmpPorts = _AxFixedNatTop5UserPrivateIpAddrTotIcmpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 12)
)
_AxFixedNatTop5UserPrivateIpAddrTotIcmpPortTable_Object = MibTable
axFixedNatTop5UserPrivateIpAddrTotIcmpPortTable = _AxFixedNatTop5UserPrivateIpAddrTotIcmpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 12, 1)
)
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrTotIcmpPortTable.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrTotIcmpPortEntry_Object = MibTableRow
axFixedNatTop5UserPrivateIpAddrTotIcmpPortEntry = _AxFixedNatTop5UserPrivateIpAddrTotIcmpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 12, 1, 1)
)
axFixedNatTop5UserPrivateIpAddrTotIcmpPortEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axFixedNatTop5UserPrivateIpAddrInIcmp"),
)
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrTotIcmpPortEntry.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrInIcmp_Type = DisplayString
_AxFixedNatTop5UserPrivateIpAddrInIcmp_Object = MibTableColumn
axFixedNatTop5UserPrivateIpAddrInIcmp = _AxFixedNatTop5UserPrivateIpAddrInIcmp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 12, 1, 1, 1),
    _AxFixedNatTop5UserPrivateIpAddrInIcmp_Type()
)
axFixedNatTop5UserPrivateIpAddrInIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrInIcmp.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrTotNumInIcmp_Type = Integer32
_AxFixedNatTop5UserPrivateIpAddrTotNumInIcmp_Object = MibTableColumn
axFixedNatTop5UserPrivateIpAddrTotNumInIcmp = _AxFixedNatTop5UserPrivateIpAddrTotNumInIcmp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 12, 1, 1, 2),
    _AxFixedNatTop5UserPrivateIpAddrTotNumInIcmp_Type()
)
axFixedNatTop5UserPrivateIpAddrTotNumInIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrTotNumInIcmp.setStatus("current")
_AxFixedNatTop5UserPrivateIpAddrGlobalIpAddrInIcmp_Type = DisplayString
_AxFixedNatTop5UserPrivateIpAddrGlobalIpAddrInIcmp_Object = MibTableColumn
axFixedNatTop5UserPrivateIpAddrGlobalIpAddrInIcmp = _AxFixedNatTop5UserPrivateIpAddrGlobalIpAddrInIcmp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 12, 1, 1, 3),
    _AxFixedNatTop5UserPrivateIpAddrGlobalIpAddrInIcmp_Type()
)
axFixedNatTop5UserPrivateIpAddrGlobalIpAddrInIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5UserPrivateIpAddrGlobalIpAddrInIcmp.setStatus("current")
_AxFixedNatTop5GlobalIpAddrTotUsers_ObjectIdentity = ObjectIdentity
axFixedNatTop5GlobalIpAddrTotUsers = _AxFixedNatTop5GlobalIpAddrTotUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 13)
)
_AxFixedNatTop5GlobalIpAddrTotUserTable_Object = MibTable
axFixedNatTop5GlobalIpAddrTotUserTable = _AxFixedNatTop5GlobalIpAddrTotUserTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 13, 1)
)
if mibBuilder.loadTexts:
    axFixedNatTop5GlobalIpAddrTotUserTable.setStatus("current")
_AxFixedNatTop5GlobalIpAddrTotUserEntry_Object = MibTableRow
axFixedNatTop5GlobalIpAddrTotUserEntry = _AxFixedNatTop5GlobalIpAddrTotUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 13, 1, 1)
)
axFixedNatTop5GlobalIpAddrTotUserEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axFixedNatTop5GlobalIpAddrUser"),
)
if mibBuilder.loadTexts:
    axFixedNatTop5GlobalIpAddrTotUserEntry.setStatus("current")
_AxFixedNatTop5GlobalIpAddrUser_Type = DisplayString
_AxFixedNatTop5GlobalIpAddrUser_Object = MibTableColumn
axFixedNatTop5GlobalIpAddrUser = _AxFixedNatTop5GlobalIpAddrUser_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 13, 1, 1, 1),
    _AxFixedNatTop5GlobalIpAddrUser_Type()
)
axFixedNatTop5GlobalIpAddrUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5GlobalIpAddrUser.setStatus("current")
_AxFixedNatTop5GlobalIpAddrTotNum_Type = Integer32
_AxFixedNatTop5GlobalIpAddrTotNum_Object = MibTableColumn
axFixedNatTop5GlobalIpAddrTotNum = _AxFixedNatTop5GlobalIpAddrTotNum_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 13, 1, 1, 2),
    _AxFixedNatTop5GlobalIpAddrTotNum_Type()
)
axFixedNatTop5GlobalIpAddrTotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5GlobalIpAddrTotNum.setStatus("current")
_AxFixedNatTop5GlobalIpAddrTotTcpPorts_ObjectIdentity = ObjectIdentity
axFixedNatTop5GlobalIpAddrTotTcpPorts = _AxFixedNatTop5GlobalIpAddrTotTcpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 14)
)
_AxFixedNatTop5GlobalIpAddrTotTcpPortTable_Object = MibTable
axFixedNatTop5GlobalIpAddrTotTcpPortTable = _AxFixedNatTop5GlobalIpAddrTotTcpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 14, 1)
)
if mibBuilder.loadTexts:
    axFixedNatTop5GlobalIpAddrTotTcpPortTable.setStatus("current")
_AxFixedNatTop5GlobalIpAddrTotTcpPortEntry_Object = MibTableRow
axFixedNatTop5GlobalIpAddrTotTcpPortEntry = _AxFixedNatTop5GlobalIpAddrTotTcpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 14, 1, 1)
)
axFixedNatTop5GlobalIpAddrTotTcpPortEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axFixedNatTop5GlobalIpAddrInTcp"),
)
if mibBuilder.loadTexts:
    axFixedNatTop5GlobalIpAddrTotTcpPortEntry.setStatus("current")
_AxFixedNatTop5GlobalIpAddrInTcp_Type = DisplayString
_AxFixedNatTop5GlobalIpAddrInTcp_Object = MibTableColumn
axFixedNatTop5GlobalIpAddrInTcp = _AxFixedNatTop5GlobalIpAddrInTcp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 14, 1, 1, 1),
    _AxFixedNatTop5GlobalIpAddrInTcp_Type()
)
axFixedNatTop5GlobalIpAddrInTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5GlobalIpAddrInTcp.setStatus("current")
_AxFixedNatTop5GlobalIpAddrTotNumInTcp_Type = Integer32
_AxFixedNatTop5GlobalIpAddrTotNumInTcp_Object = MibTableColumn
axFixedNatTop5GlobalIpAddrTotNumInTcp = _AxFixedNatTop5GlobalIpAddrTotNumInTcp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 14, 1, 1, 2),
    _AxFixedNatTop5GlobalIpAddrTotNumInTcp_Type()
)
axFixedNatTop5GlobalIpAddrTotNumInTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5GlobalIpAddrTotNumInTcp.setStatus("current")
_AxFixedNatTop5GlobalIpAddrTotUdpPorts_ObjectIdentity = ObjectIdentity
axFixedNatTop5GlobalIpAddrTotUdpPorts = _AxFixedNatTop5GlobalIpAddrTotUdpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 15)
)
_AxFixedNatTop5GlobalIpAddrTotUdpPortTable_Object = MibTable
axFixedNatTop5GlobalIpAddrTotUdpPortTable = _AxFixedNatTop5GlobalIpAddrTotUdpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 15, 1)
)
if mibBuilder.loadTexts:
    axFixedNatTop5GlobalIpAddrTotUdpPortTable.setStatus("current")
_AxFixedNatTop5GlobalIpAddrTotUdpPortEntry_Object = MibTableRow
axFixedNatTop5GlobalIpAddrTotUdpPortEntry = _AxFixedNatTop5GlobalIpAddrTotUdpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 15, 1, 1)
)
axFixedNatTop5GlobalIpAddrTotUdpPortEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axFixedNatTop5GlobalIpAddrInUdp"),
)
if mibBuilder.loadTexts:
    axFixedNatTop5GlobalIpAddrTotUdpPortEntry.setStatus("current")
_AxFixedNatTop5GlobalIpAddrInUdp_Type = DisplayString
_AxFixedNatTop5GlobalIpAddrInUdp_Object = MibTableColumn
axFixedNatTop5GlobalIpAddrInUdp = _AxFixedNatTop5GlobalIpAddrInUdp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 15, 1, 1, 1),
    _AxFixedNatTop5GlobalIpAddrInUdp_Type()
)
axFixedNatTop5GlobalIpAddrInUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5GlobalIpAddrInUdp.setStatus("current")
_AxFixedNatTop5GlobalIpAddrTotNumInUdp_Type = Integer32
_AxFixedNatTop5GlobalIpAddrTotNumInUdp_Object = MibTableColumn
axFixedNatTop5GlobalIpAddrTotNumInUdp = _AxFixedNatTop5GlobalIpAddrTotNumInUdp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 15, 1, 1, 2),
    _AxFixedNatTop5GlobalIpAddrTotNumInUdp_Type()
)
axFixedNatTop5GlobalIpAddrTotNumInUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatTop5GlobalIpAddrTotNumInUdp.setStatus("current")
_AxFixedNatFile_ObjectIdentity = ObjectIdentity
axFixedNatFile = _AxFixedNatFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 16)
)
_AxFixedNatFileTable_Object = MibTable
axFixedNatFileTable = _AxFixedNatFileTable_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 16, 1)
)
if mibBuilder.loadTexts:
    axFixedNatFileTable.setStatus("current")
_AxFixedNatFileEntry_Object = MibTableRow
axFixedNatFileEntry = _AxFixedNatFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 16, 1, 1)
)
axFixedNatFileEntry.setIndexNames(
    (0, "A10-AX-CGN-MIB", "axFixedNatFileName"),
)
if mibBuilder.loadTexts:
    axFixedNatFileEntry.setStatus("current")
_AxFixedNatFileName_Type = DisplayString
_AxFixedNatFileName_Object = MibTableColumn
axFixedNatFileName = _AxFixedNatFileName_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 16, 1, 1, 1),
    _AxFixedNatFileName_Type()
)
axFixedNatFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFileName.setStatus("current")
_AxFixedNatFileTimeStamp_Type = DisplayString
_AxFixedNatFileTimeStamp_Object = MibTableColumn
axFixedNatFileTimeStamp = _AxFixedNatFileTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 18, 120, 16, 1, 1, 2),
    _AxFixedNatFileTimeStamp_Type()
)
axFixedNatFileTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axFixedNatFileTimeStamp.setStatus("current")
_AxFragmentStats_ObjectIdentity = ObjectIdentity
axFragmentStats = _AxFragmentStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1)
)
_AxIpv4FragmentStats_ObjectIdentity = ObjectIdentity
axIpv4FragmentStats = _AxIpv4FragmentStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1)
)


class _AxIpv4SessionInsert_Type(CounterBasedGauge64):
    """Custom type axIpv4SessionInsert based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4SessionInsert_Type.__name__ = "CounterBasedGauge64"
_AxIpv4SessionInsert_Object = MibScalar
axIpv4SessionInsert = _AxIpv4SessionInsert_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 1),
    _AxIpv4SessionInsert_Type()
)
axIpv4SessionInsert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4SessionInsert.setStatus("current")


class _AxIpv4SessionExpired_Type(CounterBasedGauge64):
    """Custom type axIpv4SessionExpired based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4SessionExpired_Type.__name__ = "CounterBasedGauge64"
_AxIpv4SessionExpired_Object = MibScalar
axIpv4SessionExpired = _AxIpv4SessionExpired_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 2),
    _AxIpv4SessionExpired_Type()
)
axIpv4SessionExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4SessionExpired.setStatus("current")


class _AxIpv4IcmpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv4IcmpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4IcmpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv4IcmpReceived_Object = MibScalar
axIpv4IcmpReceived = _AxIpv4IcmpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 3),
    _AxIpv4IcmpReceived_Type()
)
axIpv4IcmpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4IcmpReceived.setStatus("current")


class _AxIpv4Icmpv6Received_Type(CounterBasedGauge64):
    """Custom type axIpv4Icmpv6Received based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4Icmpv6Received_Type.__name__ = "CounterBasedGauge64"
_AxIpv4Icmpv6Received_Object = MibScalar
axIpv4Icmpv6Received = _AxIpv4Icmpv6Received_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 4),
    _AxIpv4Icmpv6Received_Type()
)
axIpv4Icmpv6Received.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4Icmpv6Received.setStatus("current")


class _AxIpv4UdpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv4UdpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4UdpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv4UdpReceived_Object = MibScalar
axIpv4UdpReceived = _AxIpv4UdpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 5),
    _AxIpv4UdpReceived_Type()
)
axIpv4UdpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4UdpReceived.setStatus("current")


class _AxIpv4TcpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv4TcpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4TcpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv4TcpReceived_Object = MibScalar
axIpv4TcpReceived = _AxIpv4TcpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 6),
    _AxIpv4TcpReceived_Type()
)
axIpv4TcpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4TcpReceived.setStatus("current")


class _AxIpv4IpInIpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv4IpInIpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4IpInIpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv4IpInIpReceived_Object = MibScalar
axIpv4IpInIpReceived = _AxIpv4IpInIpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 7),
    _AxIpv4IpInIpReceived_Type()
)
axIpv4IpInIpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4IpInIpReceived.setStatus("current")


class _AxIpv4Ipv6InIpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv4Ipv6InIpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4Ipv6InIpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv4Ipv6InIpReceived_Object = MibScalar
axIpv4Ipv6InIpReceived = _AxIpv4Ipv6InIpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 8),
    _AxIpv4Ipv6InIpReceived_Type()
)
axIpv4Ipv6InIpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4Ipv6InIpReceived.setStatus("current")


class _AxIpv4OtherReceived_Type(CounterBasedGauge64):
    """Custom type axIpv4OtherReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4OtherReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv4OtherReceived_Object = MibScalar
axIpv4OtherReceived = _AxIpv4OtherReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 9),
    _AxIpv4OtherReceived_Type()
)
axIpv4OtherReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4OtherReceived.setStatus("current")


class _AxIpv4IcmpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv4IcmpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4IcmpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv4IcmpDropped_Object = MibScalar
axIpv4IcmpDropped = _AxIpv4IcmpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 10),
    _AxIpv4IcmpDropped_Type()
)
axIpv4IcmpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4IcmpDropped.setStatus("current")


class _AxIpv4Icmpv6Dropped_Type(CounterBasedGauge64):
    """Custom type axIpv4Icmpv6Dropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4Icmpv6Dropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv4Icmpv6Dropped_Object = MibScalar
axIpv4Icmpv6Dropped = _AxIpv4Icmpv6Dropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 11),
    _AxIpv4Icmpv6Dropped_Type()
)
axIpv4Icmpv6Dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4Icmpv6Dropped.setStatus("current")


class _AxIpv4UdpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv4UdpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4UdpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv4UdpDropped_Object = MibScalar
axIpv4UdpDropped = _AxIpv4UdpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 12),
    _AxIpv4UdpDropped_Type()
)
axIpv4UdpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4UdpDropped.setStatus("current")


class _AxIpv4TcpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv4TcpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4TcpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv4TcpDropped_Object = MibScalar
axIpv4TcpDropped = _AxIpv4TcpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 13),
    _AxIpv4TcpDropped_Type()
)
axIpv4TcpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4TcpDropped.setStatus("current")


class _AxIpv4IpInIpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv4IpInIpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4IpInIpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv4IpInIpDropped_Object = MibScalar
axIpv4IpInIpDropped = _AxIpv4IpInIpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 14),
    _AxIpv4IpInIpDropped_Type()
)
axIpv4IpInIpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4IpInIpDropped.setStatus("current")


class _AxIpv4Ipv6InIpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv4Ipv6InIpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4Ipv6InIpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv4Ipv6InIpDropped_Object = MibScalar
axIpv4Ipv6InIpDropped = _AxIpv4Ipv6InIpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 15),
    _AxIpv4Ipv6InIpDropped_Type()
)
axIpv4Ipv6InIpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4Ipv6InIpDropped.setStatus("current")


class _AxIpv4OtherDropped_Type(CounterBasedGauge64):
    """Custom type axIpv4OtherDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4OtherDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv4OtherDropped_Object = MibScalar
axIpv4OtherDropped = _AxIpv4OtherDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 16),
    _AxIpv4OtherDropped_Type()
)
axIpv4OtherDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4OtherDropped.setStatus("current")


class _AxIpv4OverlappingFragmentDropped_Type(CounterBasedGauge64):
    """Custom type axIpv4OverlappingFragmentDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4OverlappingFragmentDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv4OverlappingFragmentDropped_Object = MibScalar
axIpv4OverlappingFragmentDropped = _AxIpv4OverlappingFragmentDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 17),
    _AxIpv4OverlappingFragmentDropped_Type()
)
axIpv4OverlappingFragmentDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4OverlappingFragmentDropped.setStatus("current")


class _AxIpv4BadIpLength_Type(CounterBasedGauge64):
    """Custom type axIpv4BadIpLength based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4BadIpLength_Type.__name__ = "CounterBasedGauge64"
_AxIpv4BadIpLength_Object = MibScalar
axIpv4BadIpLength = _AxIpv4BadIpLength_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 18),
    _AxIpv4BadIpLength_Type()
)
axIpv4BadIpLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4BadIpLength.setStatus("current")


class _AxIpv4FragmentTooSmallDrop_Type(CounterBasedGauge64):
    """Custom type axIpv4FragmentTooSmallDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4FragmentTooSmallDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv4FragmentTooSmallDrop_Object = MibScalar
axIpv4FragmentTooSmallDrop = _AxIpv4FragmentTooSmallDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 19),
    _AxIpv4FragmentTooSmallDrop_Type()
)
axIpv4FragmentTooSmallDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4FragmentTooSmallDrop.setStatus("current")


class _AxIpv4FirstTcpFragmentTooSmallDrop_Type(CounterBasedGauge64):
    """Custom type axIpv4FirstTcpFragmentTooSmallDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4FirstTcpFragmentTooSmallDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv4FirstTcpFragmentTooSmallDrop_Object = MibScalar
axIpv4FirstTcpFragmentTooSmallDrop = _AxIpv4FirstTcpFragmentTooSmallDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 20),
    _AxIpv4FirstTcpFragmentTooSmallDrop_Type()
)
axIpv4FirstTcpFragmentTooSmallDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4FirstTcpFragmentTooSmallDrop.setStatus("current")


class _AxIpv4FirstL4FragmentTooSmallDrop_Type(CounterBasedGauge64):
    """Custom type axIpv4FirstL4FragmentTooSmallDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4FirstL4FragmentTooSmallDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv4FirstL4FragmentTooSmallDrop_Object = MibScalar
axIpv4FirstL4FragmentTooSmallDrop = _AxIpv4FirstL4FragmentTooSmallDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 21),
    _AxIpv4FirstL4FragmentTooSmallDrop_Type()
)
axIpv4FirstL4FragmentTooSmallDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4FirstL4FragmentTooSmallDrop.setStatus("current")


class _AxIpv4TotalSessionsExceedDrop_Type(CounterBasedGauge64):
    """Custom type axIpv4TotalSessionsExceedDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4TotalSessionsExceedDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv4TotalSessionsExceedDrop_Object = MibScalar
axIpv4TotalSessionsExceedDrop = _AxIpv4TotalSessionsExceedDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 22),
    _AxIpv4TotalSessionsExceedDrop_Type()
)
axIpv4TotalSessionsExceedDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4TotalSessionsExceedDrop.setStatus("current")


class _AxIpv4OutOfSessionMemory_Type(CounterBasedGauge64):
    """Custom type axIpv4OutOfSessionMemory based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4OutOfSessionMemory_Type.__name__ = "CounterBasedGauge64"
_AxIpv4OutOfSessionMemory_Object = MibScalar
axIpv4OutOfSessionMemory = _AxIpv4OutOfSessionMemory_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 23),
    _AxIpv4OutOfSessionMemory_Type()
)
axIpv4OutOfSessionMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4OutOfSessionMemory.setStatus("current")


class _AxIpv4FragmentationFastAgingSet_Type(CounterBasedGauge64):
    """Custom type axIpv4FragmentationFastAgingSet based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4FragmentationFastAgingSet_Type.__name__ = "CounterBasedGauge64"
_AxIpv4FragmentationFastAgingSet_Object = MibScalar
axIpv4FragmentationFastAgingSet = _AxIpv4FragmentationFastAgingSet_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 24),
    _AxIpv4FragmentationFastAgingSet_Type()
)
axIpv4FragmentationFastAgingSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4FragmentationFastAgingSet.setStatus("current")


class _AxIpv4FragmentationFastAgingUnset_Type(CounterBasedGauge64):
    """Custom type axIpv4FragmentationFastAgingUnset based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4FragmentationFastAgingUnset_Type.__name__ = "CounterBasedGauge64"
_AxIpv4FragmentationFastAgingUnset_Object = MibScalar
axIpv4FragmentationFastAgingUnset = _AxIpv4FragmentationFastAgingUnset_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 25),
    _AxIpv4FragmentationFastAgingUnset_Type()
)
axIpv4FragmentationFastAgingUnset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4FragmentationFastAgingUnset.setStatus("current")


class _AxIpv4FragmentQueueSuccess_Type(CounterBasedGauge64):
    """Custom type axIpv4FragmentQueueSuccess based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4FragmentQueueSuccess_Type.__name__ = "CounterBasedGauge64"
_AxIpv4FragmentQueueSuccess_Object = MibScalar
axIpv4FragmentQueueSuccess = _AxIpv4FragmentQueueSuccess_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 26),
    _AxIpv4FragmentQueueSuccess_Type()
)
axIpv4FragmentQueueSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4FragmentQueueSuccess.setStatus("current")


class _AxIpv4PayloadLengthUnaligned_Type(CounterBasedGauge64):
    """Custom type axIpv4PayloadLengthUnaligned based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4PayloadLengthUnaligned_Type.__name__ = "CounterBasedGauge64"
_AxIpv4PayloadLengthUnaligned_Object = MibScalar
axIpv4PayloadLengthUnaligned = _AxIpv4PayloadLengthUnaligned_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 27),
    _AxIpv4PayloadLengthUnaligned_Type()
)
axIpv4PayloadLengthUnaligned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4PayloadLengthUnaligned.setStatus("current")


class _AxIpv4PayloadLengthOutOfBounds_Type(CounterBasedGauge64):
    """Custom type axIpv4PayloadLengthOutOfBounds based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4PayloadLengthOutOfBounds_Type.__name__ = "CounterBasedGauge64"
_AxIpv4PayloadLengthOutOfBounds_Object = MibScalar
axIpv4PayloadLengthOutOfBounds = _AxIpv4PayloadLengthOutOfBounds_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 28),
    _AxIpv4PayloadLengthOutOfBounds_Type()
)
axIpv4PayloadLengthOutOfBounds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4PayloadLengthOutOfBounds.setStatus("current")


class _AxIpv4DuplicateFirstFragment_Type(CounterBasedGauge64):
    """Custom type axIpv4DuplicateFirstFragment based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4DuplicateFirstFragment_Type.__name__ = "CounterBasedGauge64"
_AxIpv4DuplicateFirstFragment_Object = MibScalar
axIpv4DuplicateFirstFragment = _AxIpv4DuplicateFirstFragment_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 29),
    _AxIpv4DuplicateFirstFragment_Type()
)
axIpv4DuplicateFirstFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4DuplicateFirstFragment.setStatus("current")


class _AxIpv4DuplicateLastFragment_Type(CounterBasedGauge64):
    """Custom type axIpv4DuplicateLastFragment based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4DuplicateLastFragment_Type.__name__ = "CounterBasedGauge64"
_AxIpv4DuplicateLastFragment_Object = MibScalar
axIpv4DuplicateLastFragment = _AxIpv4DuplicateLastFragment_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 30),
    _AxIpv4DuplicateLastFragment_Type()
)
axIpv4DuplicateLastFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4DuplicateLastFragment.setStatus("current")


class _AxIpv4TotalQueuedFragmentsExceed_Type(CounterBasedGauge64):
    """Custom type axIpv4TotalQueuedFragmentsExceed based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4TotalQueuedFragmentsExceed_Type.__name__ = "CounterBasedGauge64"
_AxIpv4TotalQueuedFragmentsExceed_Object = MibScalar
axIpv4TotalQueuedFragmentsExceed = _AxIpv4TotalQueuedFragmentsExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 31),
    _AxIpv4TotalQueuedFragmentsExceed_Type()
)
axIpv4TotalQueuedFragmentsExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4TotalQueuedFragmentsExceed.setStatus("current")


class _AxIpv4FragmentQueueFailure_Type(CounterBasedGauge64):
    """Custom type axIpv4FragmentQueueFailure based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4FragmentQueueFailure_Type.__name__ = "CounterBasedGauge64"
_AxIpv4FragmentQueueFailure_Object = MibScalar
axIpv4FragmentQueueFailure = _AxIpv4FragmentQueueFailure_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 32),
    _AxIpv4FragmentQueueFailure_Type()
)
axIpv4FragmentQueueFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4FragmentQueueFailure.setStatus("current")


class _AxIpv4FragmentReassemblySuccess_Type(CounterBasedGauge64):
    """Custom type axIpv4FragmentReassemblySuccess based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4FragmentReassemblySuccess_Type.__name__ = "CounterBasedGauge64"
_AxIpv4FragmentReassemblySuccess_Object = MibScalar
axIpv4FragmentReassemblySuccess = _AxIpv4FragmentReassemblySuccess_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 33),
    _AxIpv4FragmentReassemblySuccess_Type()
)
axIpv4FragmentReassemblySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4FragmentReassemblySuccess.setStatus("current")


class _AxIpv4FragmentMaxDataLengthExceed_Type(CounterBasedGauge64):
    """Custom type axIpv4FragmentMaxDataLengthExceed based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4FragmentMaxDataLengthExceed_Type.__name__ = "CounterBasedGauge64"
_AxIpv4FragmentMaxDataLengthExceed_Object = MibScalar
axIpv4FragmentMaxDataLengthExceed = _AxIpv4FragmentMaxDataLengthExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 34),
    _AxIpv4FragmentMaxDataLengthExceed_Type()
)
axIpv4FragmentMaxDataLengthExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4FragmentMaxDataLengthExceed.setStatus("current")


class _AxIpv4FragmentReassemblyFailure_Type(CounterBasedGauge64):
    """Custom type axIpv4FragmentReassemblyFailure based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4FragmentReassemblyFailure_Type.__name__ = "CounterBasedGauge64"
_AxIpv4FragmentReassemblyFailure_Object = MibScalar
axIpv4FragmentReassemblyFailure = _AxIpv4FragmentReassemblyFailure_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 35),
    _AxIpv4FragmentReassemblyFailure_Type()
)
axIpv4FragmentReassemblyFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4FragmentReassemblyFailure.setStatus("current")


class _AxIpv4MtuExceedPolicyDrop_Type(CounterBasedGauge64):
    """Custom type axIpv4MtuExceedPolicyDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4MtuExceedPolicyDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv4MtuExceedPolicyDrop_Object = MibScalar
axIpv4MtuExceedPolicyDrop = _AxIpv4MtuExceedPolicyDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 36),
    _AxIpv4MtuExceedPolicyDrop_Type()
)
axIpv4MtuExceedPolicyDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4MtuExceedPolicyDrop.setStatus("current")


class _AxIpv4FragmentProcessingDrop_Type(CounterBasedGauge64):
    """Custom type axIpv4FragmentProcessingDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4FragmentProcessingDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv4FragmentProcessingDrop_Object = MibScalar
axIpv4FragmentProcessingDrop = _AxIpv4FragmentProcessingDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 37),
    _AxIpv4FragmentProcessingDrop_Type()
)
axIpv4FragmentProcessingDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4FragmentProcessingDrop.setStatus("current")


class _AxIpv4TooManyPacketsPerReassemblyDrop_Type(CounterBasedGauge64):
    """Custom type axIpv4TooManyPacketsPerReassemblyDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4TooManyPacketsPerReassemblyDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv4TooManyPacketsPerReassemblyDrop_Object = MibScalar
axIpv4TooManyPacketsPerReassemblyDrop = _AxIpv4TooManyPacketsPerReassemblyDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 38),
    _AxIpv4TooManyPacketsPerReassemblyDrop_Type()
)
axIpv4TooManyPacketsPerReassemblyDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4TooManyPacketsPerReassemblyDrop.setStatus("current")


class _AxIpv4SessionMaxPacketsExceed_Type(CounterBasedGauge64):
    """Custom type axIpv4SessionMaxPacketsExceed based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4SessionMaxPacketsExceed_Type.__name__ = "CounterBasedGauge64"
_AxIpv4SessionMaxPacketsExceed_Object = MibScalar
axIpv4SessionMaxPacketsExceed = _AxIpv4SessionMaxPacketsExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 39),
    _AxIpv4SessionMaxPacketsExceed_Type()
)
axIpv4SessionMaxPacketsExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4SessionMaxPacketsExceed.setStatus("current")


class _AxIpv4HighCpuThresholdReached_Type(CounterBasedGauge64):
    """Custom type axIpv4HighCpuThresholdReached based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4HighCpuThresholdReached_Type.__name__ = "CounterBasedGauge64"
_AxIpv4HighCpuThresholdReached_Object = MibScalar
axIpv4HighCpuThresholdReached = _AxIpv4HighCpuThresholdReached_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 40),
    _AxIpv4HighCpuThresholdReached_Type()
)
axIpv4HighCpuThresholdReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4HighCpuThresholdReached.setStatus("current")


class _AxIpv4LowCpuThresholdReached_Type(CounterBasedGauge64):
    """Custom type axIpv4LowCpuThresholdReached based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4LowCpuThresholdReached_Type.__name__ = "CounterBasedGauge64"
_AxIpv4LowCpuThresholdReached_Object = MibScalar
axIpv4LowCpuThresholdReached = _AxIpv4LowCpuThresholdReached_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 41),
    _AxIpv4LowCpuThresholdReached_Type()
)
axIpv4LowCpuThresholdReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4LowCpuThresholdReached.setStatus("current")


class _AxIpv4HighCpuDrop_Type(CounterBasedGauge64):
    """Custom type axIpv4HighCpuDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4HighCpuDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv4HighCpuDrop_Object = MibScalar
axIpv4HighCpuDrop = _AxIpv4HighCpuDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 42),
    _AxIpv4HighCpuDrop_Type()
)
axIpv4HighCpuDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4HighCpuDrop.setStatus("current")


class _AxIpv4DDoSProtectionDrop_Type(CounterBasedGauge64):
    """Custom type axIpv4DDoSProtectionDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4DDoSProtectionDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv4DDoSProtectionDrop_Object = MibScalar
axIpv4DDoSProtectionDrop = _AxIpv4DDoSProtectionDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 1, 43),
    _AxIpv4DDoSProtectionDrop_Type()
)
axIpv4DDoSProtectionDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4DDoSProtectionDrop.setStatus("current")
_AxIpv6FragmentStats_ObjectIdentity = ObjectIdentity
axIpv6FragmentStats = _AxIpv6FragmentStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2)
)


class _AxIpv6SessionInsert_Type(CounterBasedGauge64):
    """Custom type axIpv6SessionInsert based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6SessionInsert_Type.__name__ = "CounterBasedGauge64"
_AxIpv6SessionInsert_Object = MibScalar
axIpv6SessionInsert = _AxIpv6SessionInsert_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 1),
    _AxIpv6SessionInsert_Type()
)
axIpv6SessionInsert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6SessionInsert.setStatus("current")


class _AxIpv6SessionExpired_Type(CounterBasedGauge64):
    """Custom type axIpv6SessionExpired based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6SessionExpired_Type.__name__ = "CounterBasedGauge64"
_AxIpv6SessionExpired_Object = MibScalar
axIpv6SessionExpired = _AxIpv6SessionExpired_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 2),
    _AxIpv6SessionExpired_Type()
)
axIpv6SessionExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6SessionExpired.setStatus("current")


class _AxIpv6IcmpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv6IcmpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6IcmpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv6IcmpReceived_Object = MibScalar
axIpv6IcmpReceived = _AxIpv6IcmpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 3),
    _AxIpv6IcmpReceived_Type()
)
axIpv6IcmpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6IcmpReceived.setStatus("current")


class _AxIpv6Icmpv6Received_Type(CounterBasedGauge64):
    """Custom type axIpv6Icmpv6Received based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6Icmpv6Received_Type.__name__ = "CounterBasedGauge64"
_AxIpv6Icmpv6Received_Object = MibScalar
axIpv6Icmpv6Received = _AxIpv6Icmpv6Received_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 4),
    _AxIpv6Icmpv6Received_Type()
)
axIpv6Icmpv6Received.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6Icmpv6Received.setStatus("current")


class _AxIpv6UdpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv6UdpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6UdpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv6UdpReceived_Object = MibScalar
axIpv6UdpReceived = _AxIpv6UdpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 5),
    _AxIpv6UdpReceived_Type()
)
axIpv6UdpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6UdpReceived.setStatus("current")


class _AxIpv6TcpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv6TcpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6TcpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv6TcpReceived_Object = MibScalar
axIpv6TcpReceived = _AxIpv6TcpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 6),
    _AxIpv6TcpReceived_Type()
)
axIpv6TcpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6TcpReceived.setStatus("current")


class _AxIpv6IpInIpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv6IpInIpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6IpInIpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv6IpInIpReceived_Object = MibScalar
axIpv6IpInIpReceived = _AxIpv6IpInIpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 7),
    _AxIpv6IpInIpReceived_Type()
)
axIpv6IpInIpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6IpInIpReceived.setStatus("current")


class _AxIpv6Ipv6InIpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv6Ipv6InIpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6Ipv6InIpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv6Ipv6InIpReceived_Object = MibScalar
axIpv6Ipv6InIpReceived = _AxIpv6Ipv6InIpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 8),
    _AxIpv6Ipv6InIpReceived_Type()
)
axIpv6Ipv6InIpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6Ipv6InIpReceived.setStatus("current")


class _AxIpv6OtherReceived_Type(CounterBasedGauge64):
    """Custom type axIpv6OtherReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6OtherReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv6OtherReceived_Object = MibScalar
axIpv6OtherReceived = _AxIpv6OtherReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 9),
    _AxIpv6OtherReceived_Type()
)
axIpv6OtherReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6OtherReceived.setStatus("current")


class _AxIpv6IcmpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv6IcmpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6IcmpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv6IcmpDropped_Object = MibScalar
axIpv6IcmpDropped = _AxIpv6IcmpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 10),
    _AxIpv6IcmpDropped_Type()
)
axIpv6IcmpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6IcmpDropped.setStatus("current")


class _AxIpv6Icmpv6Dropped_Type(CounterBasedGauge64):
    """Custom type axIpv6Icmpv6Dropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6Icmpv6Dropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv6Icmpv6Dropped_Object = MibScalar
axIpv6Icmpv6Dropped = _AxIpv6Icmpv6Dropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 11),
    _AxIpv6Icmpv6Dropped_Type()
)
axIpv6Icmpv6Dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6Icmpv6Dropped.setStatus("current")


class _AxIpv6UdpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv6UdpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6UdpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv6UdpDropped_Object = MibScalar
axIpv6UdpDropped = _AxIpv6UdpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 12),
    _AxIpv6UdpDropped_Type()
)
axIpv6UdpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6UdpDropped.setStatus("current")


class _AxIpv6TcpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv6TcpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6TcpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv6TcpDropped_Object = MibScalar
axIpv6TcpDropped = _AxIpv6TcpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 13),
    _AxIpv6TcpDropped_Type()
)
axIpv6TcpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6TcpDropped.setStatus("current")


class _AxIpv6IpInIpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv6IpInIpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6IpInIpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv6IpInIpDropped_Object = MibScalar
axIpv6IpInIpDropped = _AxIpv6IpInIpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 14),
    _AxIpv6IpInIpDropped_Type()
)
axIpv6IpInIpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6IpInIpDropped.setStatus("current")


class _AxIpv6Ipv6InIpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv6Ipv6InIpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6Ipv6InIpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv6Ipv6InIpDropped_Object = MibScalar
axIpv6Ipv6InIpDropped = _AxIpv6Ipv6InIpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 15),
    _AxIpv6Ipv6InIpDropped_Type()
)
axIpv6Ipv6InIpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6Ipv6InIpDropped.setStatus("current")


class _AxIpv6OtherDropped_Type(CounterBasedGauge64):
    """Custom type axIpv6OtherDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6OtherDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv6OtherDropped_Object = MibScalar
axIpv6OtherDropped = _AxIpv6OtherDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 16),
    _AxIpv6OtherDropped_Type()
)
axIpv6OtherDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6OtherDropped.setStatus("current")


class _AxIpv6OverlappingFragmentDropped_Type(CounterBasedGauge64):
    """Custom type axIpv6OverlappingFragmentDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6OverlappingFragmentDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv6OverlappingFragmentDropped_Object = MibScalar
axIpv6OverlappingFragmentDropped = _AxIpv6OverlappingFragmentDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 17),
    _AxIpv6OverlappingFragmentDropped_Type()
)
axIpv6OverlappingFragmentDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6OverlappingFragmentDropped.setStatus("current")


class _AxIpv6BadIpLength_Type(CounterBasedGauge64):
    """Custom type axIpv6BadIpLength based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6BadIpLength_Type.__name__ = "CounterBasedGauge64"
_AxIpv6BadIpLength_Object = MibScalar
axIpv6BadIpLength = _AxIpv6BadIpLength_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 18),
    _AxIpv6BadIpLength_Type()
)
axIpv6BadIpLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6BadIpLength.setStatus("current")


class _AxIpv6FragmentTooSmallDrop_Type(CounterBasedGauge64):
    """Custom type axIpv6FragmentTooSmallDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6FragmentTooSmallDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv6FragmentTooSmallDrop_Object = MibScalar
axIpv6FragmentTooSmallDrop = _AxIpv6FragmentTooSmallDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 19),
    _AxIpv6FragmentTooSmallDrop_Type()
)
axIpv6FragmentTooSmallDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6FragmentTooSmallDrop.setStatus("current")


class _AxIpv6FirstTcpFragmentTooSmallDrop_Type(CounterBasedGauge64):
    """Custom type axIpv6FirstTcpFragmentTooSmallDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6FirstTcpFragmentTooSmallDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv6FirstTcpFragmentTooSmallDrop_Object = MibScalar
axIpv6FirstTcpFragmentTooSmallDrop = _AxIpv6FirstTcpFragmentTooSmallDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 20),
    _AxIpv6FirstTcpFragmentTooSmallDrop_Type()
)
axIpv6FirstTcpFragmentTooSmallDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6FirstTcpFragmentTooSmallDrop.setStatus("current")


class _AxIpv6FirstL4FragmentTooSmallDrop_Type(CounterBasedGauge64):
    """Custom type axIpv6FirstL4FragmentTooSmallDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6FirstL4FragmentTooSmallDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv6FirstL4FragmentTooSmallDrop_Object = MibScalar
axIpv6FirstL4FragmentTooSmallDrop = _AxIpv6FirstL4FragmentTooSmallDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 21),
    _AxIpv6FirstL4FragmentTooSmallDrop_Type()
)
axIpv6FirstL4FragmentTooSmallDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6FirstL4FragmentTooSmallDrop.setStatus("current")


class _AxIpv6TotalSessionsExceedDrop_Type(CounterBasedGauge64):
    """Custom type axIpv6TotalSessionsExceedDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6TotalSessionsExceedDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv6TotalSessionsExceedDrop_Object = MibScalar
axIpv6TotalSessionsExceedDrop = _AxIpv6TotalSessionsExceedDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 22),
    _AxIpv6TotalSessionsExceedDrop_Type()
)
axIpv6TotalSessionsExceedDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6TotalSessionsExceedDrop.setStatus("current")


class _AxIpv6OutOfSessionMemory_Type(CounterBasedGauge64):
    """Custom type axIpv6OutOfSessionMemory based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6OutOfSessionMemory_Type.__name__ = "CounterBasedGauge64"
_AxIpv6OutOfSessionMemory_Object = MibScalar
axIpv6OutOfSessionMemory = _AxIpv6OutOfSessionMemory_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 23),
    _AxIpv6OutOfSessionMemory_Type()
)
axIpv6OutOfSessionMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6OutOfSessionMemory.setStatus("current")


class _AxIpv6FragmentationFastAgingSet_Type(CounterBasedGauge64):
    """Custom type axIpv6FragmentationFastAgingSet based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6FragmentationFastAgingSet_Type.__name__ = "CounterBasedGauge64"
_AxIpv6FragmentationFastAgingSet_Object = MibScalar
axIpv6FragmentationFastAgingSet = _AxIpv6FragmentationFastAgingSet_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 24),
    _AxIpv6FragmentationFastAgingSet_Type()
)
axIpv6FragmentationFastAgingSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6FragmentationFastAgingSet.setStatus("current")


class _AxIpv6FragmentationFastAgingUnset_Type(CounterBasedGauge64):
    """Custom type axIpv6FragmentationFastAgingUnset based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6FragmentationFastAgingUnset_Type.__name__ = "CounterBasedGauge64"
_AxIpv6FragmentationFastAgingUnset_Object = MibScalar
axIpv6FragmentationFastAgingUnset = _AxIpv6FragmentationFastAgingUnset_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 25),
    _AxIpv6FragmentationFastAgingUnset_Type()
)
axIpv6FragmentationFastAgingUnset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6FragmentationFastAgingUnset.setStatus("current")


class _AxIpv6FragmentQueueSuccess_Type(CounterBasedGauge64):
    """Custom type axIpv6FragmentQueueSuccess based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6FragmentQueueSuccess_Type.__name__ = "CounterBasedGauge64"
_AxIpv6FragmentQueueSuccess_Object = MibScalar
axIpv6FragmentQueueSuccess = _AxIpv6FragmentQueueSuccess_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 26),
    _AxIpv6FragmentQueueSuccess_Type()
)
axIpv6FragmentQueueSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6FragmentQueueSuccess.setStatus("current")


class _AxIpv6PayloadLengthUnaligned_Type(CounterBasedGauge64):
    """Custom type axIpv6PayloadLengthUnaligned based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6PayloadLengthUnaligned_Type.__name__ = "CounterBasedGauge64"
_AxIpv6PayloadLengthUnaligned_Object = MibScalar
axIpv6PayloadLengthUnaligned = _AxIpv6PayloadLengthUnaligned_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 27),
    _AxIpv6PayloadLengthUnaligned_Type()
)
axIpv6PayloadLengthUnaligned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6PayloadLengthUnaligned.setStatus("current")


class _AxIpv6PayloadLengthOutOfBounds_Type(CounterBasedGauge64):
    """Custom type axIpv6PayloadLengthOutOfBounds based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6PayloadLengthOutOfBounds_Type.__name__ = "CounterBasedGauge64"
_AxIpv6PayloadLengthOutOfBounds_Object = MibScalar
axIpv6PayloadLengthOutOfBounds = _AxIpv6PayloadLengthOutOfBounds_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 28),
    _AxIpv6PayloadLengthOutOfBounds_Type()
)
axIpv6PayloadLengthOutOfBounds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6PayloadLengthOutOfBounds.setStatus("current")


class _AxIpv6DuplicateFirstFragment_Type(CounterBasedGauge64):
    """Custom type axIpv6DuplicateFirstFragment based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6DuplicateFirstFragment_Type.__name__ = "CounterBasedGauge64"
_AxIpv6DuplicateFirstFragment_Object = MibScalar
axIpv6DuplicateFirstFragment = _AxIpv6DuplicateFirstFragment_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 29),
    _AxIpv6DuplicateFirstFragment_Type()
)
axIpv6DuplicateFirstFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6DuplicateFirstFragment.setStatus("current")


class _AxIpv6DuplicateLastFragment_Type(CounterBasedGauge64):
    """Custom type axIpv6DuplicateLastFragment based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6DuplicateLastFragment_Type.__name__ = "CounterBasedGauge64"
_AxIpv6DuplicateLastFragment_Object = MibScalar
axIpv6DuplicateLastFragment = _AxIpv6DuplicateLastFragment_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 30),
    _AxIpv6DuplicateLastFragment_Type()
)
axIpv6DuplicateLastFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6DuplicateLastFragment.setStatus("current")


class _AxIpv6TotalQueuedFragmentsExceed_Type(CounterBasedGauge64):
    """Custom type axIpv6TotalQueuedFragmentsExceed based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6TotalQueuedFragmentsExceed_Type.__name__ = "CounterBasedGauge64"
_AxIpv6TotalQueuedFragmentsExceed_Object = MibScalar
axIpv6TotalQueuedFragmentsExceed = _AxIpv6TotalQueuedFragmentsExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 31),
    _AxIpv6TotalQueuedFragmentsExceed_Type()
)
axIpv6TotalQueuedFragmentsExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6TotalQueuedFragmentsExceed.setStatus("current")


class _AxIpv6FragmentQueueFailure_Type(CounterBasedGauge64):
    """Custom type axIpv6FragmentQueueFailure based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6FragmentQueueFailure_Type.__name__ = "CounterBasedGauge64"
_AxIpv6FragmentQueueFailure_Object = MibScalar
axIpv6FragmentQueueFailure = _AxIpv6FragmentQueueFailure_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 32),
    _AxIpv6FragmentQueueFailure_Type()
)
axIpv6FragmentQueueFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6FragmentQueueFailure.setStatus("current")


class _AxIpv6FragmentReassemblySuccess_Type(CounterBasedGauge64):
    """Custom type axIpv6FragmentReassemblySuccess based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6FragmentReassemblySuccess_Type.__name__ = "CounterBasedGauge64"
_AxIpv6FragmentReassemblySuccess_Object = MibScalar
axIpv6FragmentReassemblySuccess = _AxIpv6FragmentReassemblySuccess_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 33),
    _AxIpv6FragmentReassemblySuccess_Type()
)
axIpv6FragmentReassemblySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6FragmentReassemblySuccess.setStatus("current")


class _AxIpv6FragmentMaxDataLengthExceed_Type(CounterBasedGauge64):
    """Custom type axIpv6FragmentMaxDataLengthExceed based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6FragmentMaxDataLengthExceed_Type.__name__ = "CounterBasedGauge64"
_AxIpv6FragmentMaxDataLengthExceed_Object = MibScalar
axIpv6FragmentMaxDataLengthExceed = _AxIpv6FragmentMaxDataLengthExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 34),
    _AxIpv6FragmentMaxDataLengthExceed_Type()
)
axIpv6FragmentMaxDataLengthExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6FragmentMaxDataLengthExceed.setStatus("current")


class _AxIpv6FragmentReassemblyFailure_Type(CounterBasedGauge64):
    """Custom type axIpv6FragmentReassemblyFailure based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6FragmentReassemblyFailure_Type.__name__ = "CounterBasedGauge64"
_AxIpv6FragmentReassemblyFailure_Object = MibScalar
axIpv6FragmentReassemblyFailure = _AxIpv6FragmentReassemblyFailure_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 35),
    _AxIpv6FragmentReassemblyFailure_Type()
)
axIpv6FragmentReassemblyFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6FragmentReassemblyFailure.setStatus("current")


class _AxIpv6MtuExceedPolicyDrop_Type(CounterBasedGauge64):
    """Custom type axIpv6MtuExceedPolicyDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6MtuExceedPolicyDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv6MtuExceedPolicyDrop_Object = MibScalar
axIpv6MtuExceedPolicyDrop = _AxIpv6MtuExceedPolicyDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 36),
    _AxIpv6MtuExceedPolicyDrop_Type()
)
axIpv6MtuExceedPolicyDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6MtuExceedPolicyDrop.setStatus("current")


class _AxIpv6FragmentProcessingDrop_Type(CounterBasedGauge64):
    """Custom type axIpv6FragmentProcessingDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6FragmentProcessingDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv6FragmentProcessingDrop_Object = MibScalar
axIpv6FragmentProcessingDrop = _AxIpv6FragmentProcessingDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 37),
    _AxIpv6FragmentProcessingDrop_Type()
)
axIpv6FragmentProcessingDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6FragmentProcessingDrop.setStatus("current")


class _AxIpv6TooManyPacketsPerReassemblyDrop_Type(CounterBasedGauge64):
    """Custom type axIpv6TooManyPacketsPerReassemblyDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6TooManyPacketsPerReassemblyDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv6TooManyPacketsPerReassemblyDrop_Object = MibScalar
axIpv6TooManyPacketsPerReassemblyDrop = _AxIpv6TooManyPacketsPerReassemblyDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 38),
    _AxIpv6TooManyPacketsPerReassemblyDrop_Type()
)
axIpv6TooManyPacketsPerReassemblyDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6TooManyPacketsPerReassemblyDrop.setStatus("current")


class _AxIpv6SessionMaxPacketsExceed_Type(CounterBasedGauge64):
    """Custom type axIpv6SessionMaxPacketsExceed based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6SessionMaxPacketsExceed_Type.__name__ = "CounterBasedGauge64"
_AxIpv6SessionMaxPacketsExceed_Object = MibScalar
axIpv6SessionMaxPacketsExceed = _AxIpv6SessionMaxPacketsExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 2, 39),
    _AxIpv6SessionMaxPacketsExceed_Type()
)
axIpv6SessionMaxPacketsExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6SessionMaxPacketsExceed.setStatus("current")
_AxIpv4InIpv6FragmentStats_ObjectIdentity = ObjectIdentity
axIpv4InIpv6FragmentStats = _AxIpv4InIpv6FragmentStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3)
)


class _AxIpv4InIpv6SessionInsert_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6SessionInsert based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6SessionInsert_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6SessionInsert_Object = MibScalar
axIpv4InIpv6SessionInsert = _AxIpv4InIpv6SessionInsert_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 1),
    _AxIpv4InIpv6SessionInsert_Type()
)
axIpv4InIpv6SessionInsert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6SessionInsert.setStatus("current")


class _AxIpv4InIpv6SessionExpired_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6SessionExpired based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6SessionExpired_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6SessionExpired_Object = MibScalar
axIpv4InIpv6SessionExpired = _AxIpv4InIpv6SessionExpired_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 2),
    _AxIpv4InIpv6SessionExpired_Type()
)
axIpv4InIpv6SessionExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6SessionExpired.setStatus("current")


class _AxIpv4InIpv6IcmpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6IcmpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6IcmpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6IcmpReceived_Object = MibScalar
axIpv4InIpv6IcmpReceived = _AxIpv4InIpv6IcmpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 3),
    _AxIpv4InIpv6IcmpReceived_Type()
)
axIpv4InIpv6IcmpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6IcmpReceived.setStatus("current")


class _AxIpv4InIpv6Icmpv6Received_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6Icmpv6Received based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6Icmpv6Received_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6Icmpv6Received_Object = MibScalar
axIpv4InIpv6Icmpv6Received = _AxIpv4InIpv6Icmpv6Received_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 4),
    _AxIpv4InIpv6Icmpv6Received_Type()
)
axIpv4InIpv6Icmpv6Received.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6Icmpv6Received.setStatus("current")


class _AxIpv4InIpv6UdpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6UdpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6UdpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6UdpReceived_Object = MibScalar
axIpv4InIpv6UdpReceived = _AxIpv4InIpv6UdpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 5),
    _AxIpv4InIpv6UdpReceived_Type()
)
axIpv4InIpv6UdpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6UdpReceived.setStatus("current")


class _AxIpv4InIpv6TcpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6TcpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6TcpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6TcpReceived_Object = MibScalar
axIpv4InIpv6TcpReceived = _AxIpv4InIpv6TcpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 6),
    _AxIpv4InIpv6TcpReceived_Type()
)
axIpv4InIpv6TcpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6TcpReceived.setStatus("current")


class _AxIpv4InIpv6IpInIpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6IpInIpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6IpInIpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6IpInIpReceived_Object = MibScalar
axIpv4InIpv6IpInIpReceived = _AxIpv4InIpv6IpInIpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 7),
    _AxIpv4InIpv6IpInIpReceived_Type()
)
axIpv4InIpv6IpInIpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6IpInIpReceived.setStatus("current")


class _AxIpv4InIpv6Ipv6InIpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6Ipv6InIpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6Ipv6InIpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6Ipv6InIpReceived_Object = MibScalar
axIpv4InIpv6Ipv6InIpReceived = _AxIpv4InIpv6Ipv6InIpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 8),
    _AxIpv4InIpv6Ipv6InIpReceived_Type()
)
axIpv4InIpv6Ipv6InIpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6Ipv6InIpReceived.setStatus("current")


class _AxIpv4InIpv6OtherReceived_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6OtherReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6OtherReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6OtherReceived_Object = MibScalar
axIpv4InIpv6OtherReceived = _AxIpv4InIpv6OtherReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 9),
    _AxIpv4InIpv6OtherReceived_Type()
)
axIpv4InIpv6OtherReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6OtherReceived.setStatus("current")


class _AxIpv4InIpv6IcmpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6IcmpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6IcmpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6IcmpDropped_Object = MibScalar
axIpv4InIpv6IcmpDropped = _AxIpv4InIpv6IcmpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 10),
    _AxIpv4InIpv6IcmpDropped_Type()
)
axIpv4InIpv6IcmpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6IcmpDropped.setStatus("current")


class _AxIpv4InIpv6Icmpv6Dropped_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6Icmpv6Dropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6Icmpv6Dropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6Icmpv6Dropped_Object = MibScalar
axIpv4InIpv6Icmpv6Dropped = _AxIpv4InIpv6Icmpv6Dropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 11),
    _AxIpv4InIpv6Icmpv6Dropped_Type()
)
axIpv4InIpv6Icmpv6Dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6Icmpv6Dropped.setStatus("current")


class _AxIpv4InIpv6UdpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6UdpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6UdpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6UdpDropped_Object = MibScalar
axIpv4InIpv6UdpDropped = _AxIpv4InIpv6UdpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 12),
    _AxIpv4InIpv6UdpDropped_Type()
)
axIpv4InIpv6UdpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6UdpDropped.setStatus("current")


class _AxIpv4InIpv6TcpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6TcpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6TcpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6TcpDropped_Object = MibScalar
axIpv4InIpv6TcpDropped = _AxIpv4InIpv6TcpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 13),
    _AxIpv4InIpv6TcpDropped_Type()
)
axIpv4InIpv6TcpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6TcpDropped.setStatus("current")


class _AxIpv4InIpv6IpInIpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6IpInIpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6IpInIpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6IpInIpDropped_Object = MibScalar
axIpv4InIpv6IpInIpDropped = _AxIpv4InIpv6IpInIpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 14),
    _AxIpv4InIpv6IpInIpDropped_Type()
)
axIpv4InIpv6IpInIpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6IpInIpDropped.setStatus("current")


class _AxIpv4InIpv6Ipv6InIpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6Ipv6InIpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6Ipv6InIpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6Ipv6InIpDropped_Object = MibScalar
axIpv4InIpv6Ipv6InIpDropped = _AxIpv4InIpv6Ipv6InIpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 15),
    _AxIpv4InIpv6Ipv6InIpDropped_Type()
)
axIpv4InIpv6Ipv6InIpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6Ipv6InIpDropped.setStatus("current")


class _AxIpv4InIpv6OtherDropped_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6OtherDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6OtherDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6OtherDropped_Object = MibScalar
axIpv4InIpv6OtherDropped = _AxIpv4InIpv6OtherDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 16),
    _AxIpv4InIpv6OtherDropped_Type()
)
axIpv4InIpv6OtherDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6OtherDropped.setStatus("current")


class _AxIpv4InIpv6OverlappingFragmentDropped_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6OverlappingFragmentDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6OverlappingFragmentDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6OverlappingFragmentDropped_Object = MibScalar
axIpv4InIpv6OverlappingFragmentDropped = _AxIpv4InIpv6OverlappingFragmentDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 17),
    _AxIpv4InIpv6OverlappingFragmentDropped_Type()
)
axIpv4InIpv6OverlappingFragmentDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6OverlappingFragmentDropped.setStatus("current")


class _AxIpv4InIpv6BadIpLength_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6BadIpLength based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6BadIpLength_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6BadIpLength_Object = MibScalar
axIpv4InIpv6BadIpLength = _AxIpv4InIpv6BadIpLength_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 18),
    _AxIpv4InIpv6BadIpLength_Type()
)
axIpv4InIpv6BadIpLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6BadIpLength.setStatus("current")


class _AxIpv4InIpv6FragmentTooSmallDrop_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6FragmentTooSmallDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6FragmentTooSmallDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6FragmentTooSmallDrop_Object = MibScalar
axIpv4InIpv6FragmentTooSmallDrop = _AxIpv4InIpv6FragmentTooSmallDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 19),
    _AxIpv4InIpv6FragmentTooSmallDrop_Type()
)
axIpv4InIpv6FragmentTooSmallDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6FragmentTooSmallDrop.setStatus("current")


class _AxIpv4InIpv6FirstTcpFragmentTooSmallDrop_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6FirstTcpFragmentTooSmallDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6FirstTcpFragmentTooSmallDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6FirstTcpFragmentTooSmallDrop_Object = MibScalar
axIpv4InIpv6FirstTcpFragmentTooSmallDrop = _AxIpv4InIpv6FirstTcpFragmentTooSmallDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 20),
    _AxIpv4InIpv6FirstTcpFragmentTooSmallDrop_Type()
)
axIpv4InIpv6FirstTcpFragmentTooSmallDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6FirstTcpFragmentTooSmallDrop.setStatus("current")


class _AxIpv4InIpv6FirstL4FragmentTooSmallDrop_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6FirstL4FragmentTooSmallDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6FirstL4FragmentTooSmallDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6FirstL4FragmentTooSmallDrop_Object = MibScalar
axIpv4InIpv6FirstL4FragmentTooSmallDrop = _AxIpv4InIpv6FirstL4FragmentTooSmallDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 21),
    _AxIpv4InIpv6FirstL4FragmentTooSmallDrop_Type()
)
axIpv4InIpv6FirstL4FragmentTooSmallDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6FirstL4FragmentTooSmallDrop.setStatus("current")


class _AxIpv4InIpv6TotalSessionsExceedDrop_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6TotalSessionsExceedDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6TotalSessionsExceedDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6TotalSessionsExceedDrop_Object = MibScalar
axIpv4InIpv6TotalSessionsExceedDrop = _AxIpv4InIpv6TotalSessionsExceedDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 22),
    _AxIpv4InIpv6TotalSessionsExceedDrop_Type()
)
axIpv4InIpv6TotalSessionsExceedDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6TotalSessionsExceedDrop.setStatus("current")


class _AxIpv4InIpv6OutOfSessionMemory_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6OutOfSessionMemory based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6OutOfSessionMemory_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6OutOfSessionMemory_Object = MibScalar
axIpv4InIpv6OutOfSessionMemory = _AxIpv4InIpv6OutOfSessionMemory_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 23),
    _AxIpv4InIpv6OutOfSessionMemory_Type()
)
axIpv4InIpv6OutOfSessionMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6OutOfSessionMemory.setStatus("current")


class _AxIpv4InIpv6FragmentationFastAgingSet_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6FragmentationFastAgingSet based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6FragmentationFastAgingSet_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6FragmentationFastAgingSet_Object = MibScalar
axIpv4InIpv6FragmentationFastAgingSet = _AxIpv4InIpv6FragmentationFastAgingSet_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 24),
    _AxIpv4InIpv6FragmentationFastAgingSet_Type()
)
axIpv4InIpv6FragmentationFastAgingSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6FragmentationFastAgingSet.setStatus("current")


class _AxIpv4InIpv6FragmentationFastAgingUnset_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6FragmentationFastAgingUnset based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6FragmentationFastAgingUnset_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6FragmentationFastAgingUnset_Object = MibScalar
axIpv4InIpv6FragmentationFastAgingUnset = _AxIpv4InIpv6FragmentationFastAgingUnset_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 25),
    _AxIpv4InIpv6FragmentationFastAgingUnset_Type()
)
axIpv4InIpv6FragmentationFastAgingUnset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6FragmentationFastAgingUnset.setStatus("current")


class _AxIpv4InIpv6FragmentQueueSuccess_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6FragmentQueueSuccess based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6FragmentQueueSuccess_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6FragmentQueueSuccess_Object = MibScalar
axIpv4InIpv6FragmentQueueSuccess = _AxIpv4InIpv6FragmentQueueSuccess_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 26),
    _AxIpv4InIpv6FragmentQueueSuccess_Type()
)
axIpv4InIpv6FragmentQueueSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6FragmentQueueSuccess.setStatus("current")


class _AxIpv4InIpv6PayloadLengthUnaligned_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6PayloadLengthUnaligned based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6PayloadLengthUnaligned_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6PayloadLengthUnaligned_Object = MibScalar
axIpv4InIpv6PayloadLengthUnaligned = _AxIpv4InIpv6PayloadLengthUnaligned_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 27),
    _AxIpv4InIpv6PayloadLengthUnaligned_Type()
)
axIpv4InIpv6PayloadLengthUnaligned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6PayloadLengthUnaligned.setStatus("current")


class _AxIpv4InIpv6PayloadLengthOutOfBounds_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6PayloadLengthOutOfBounds based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6PayloadLengthOutOfBounds_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6PayloadLengthOutOfBounds_Object = MibScalar
axIpv4InIpv6PayloadLengthOutOfBounds = _AxIpv4InIpv6PayloadLengthOutOfBounds_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 28),
    _AxIpv4InIpv6PayloadLengthOutOfBounds_Type()
)
axIpv4InIpv6PayloadLengthOutOfBounds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6PayloadLengthOutOfBounds.setStatus("current")


class _AxIpv4InIpv6DuplicateFirstFragment_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6DuplicateFirstFragment based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6DuplicateFirstFragment_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6DuplicateFirstFragment_Object = MibScalar
axIpv4InIpv6DuplicateFirstFragment = _AxIpv4InIpv6DuplicateFirstFragment_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 29),
    _AxIpv4InIpv6DuplicateFirstFragment_Type()
)
axIpv4InIpv6DuplicateFirstFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6DuplicateFirstFragment.setStatus("current")


class _AxIpv4InIpv6DuplicateLastFragment_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6DuplicateLastFragment based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6DuplicateLastFragment_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6DuplicateLastFragment_Object = MibScalar
axIpv4InIpv6DuplicateLastFragment = _AxIpv4InIpv6DuplicateLastFragment_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 30),
    _AxIpv4InIpv6DuplicateLastFragment_Type()
)
axIpv4InIpv6DuplicateLastFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6DuplicateLastFragment.setStatus("current")


class _AxIpv4InIpv6TotalQueuedFragmentsExceed_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6TotalQueuedFragmentsExceed based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6TotalQueuedFragmentsExceed_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6TotalQueuedFragmentsExceed_Object = MibScalar
axIpv4InIpv6TotalQueuedFragmentsExceed = _AxIpv4InIpv6TotalQueuedFragmentsExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 31),
    _AxIpv4InIpv6TotalQueuedFragmentsExceed_Type()
)
axIpv4InIpv6TotalQueuedFragmentsExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6TotalQueuedFragmentsExceed.setStatus("current")


class _AxIpv4InIpv6FragmentQueueFailure_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6FragmentQueueFailure based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6FragmentQueueFailure_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6FragmentQueueFailure_Object = MibScalar
axIpv4InIpv6FragmentQueueFailure = _AxIpv4InIpv6FragmentQueueFailure_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 32),
    _AxIpv4InIpv6FragmentQueueFailure_Type()
)
axIpv4InIpv6FragmentQueueFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6FragmentQueueFailure.setStatus("current")


class _AxIpv4InIpv6FragmentReassemblySuccess_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6FragmentReassemblySuccess based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6FragmentReassemblySuccess_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6FragmentReassemblySuccess_Object = MibScalar
axIpv4InIpv6FragmentReassemblySuccess = _AxIpv4InIpv6FragmentReassemblySuccess_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 33),
    _AxIpv4InIpv6FragmentReassemblySuccess_Type()
)
axIpv4InIpv6FragmentReassemblySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6FragmentReassemblySuccess.setStatus("current")


class _AxIpv4InIpv6FragmentMaxDataLengthExceed_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6FragmentMaxDataLengthExceed based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6FragmentMaxDataLengthExceed_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6FragmentMaxDataLengthExceed_Object = MibScalar
axIpv4InIpv6FragmentMaxDataLengthExceed = _AxIpv4InIpv6FragmentMaxDataLengthExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 34),
    _AxIpv4InIpv6FragmentMaxDataLengthExceed_Type()
)
axIpv4InIpv6FragmentMaxDataLengthExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6FragmentMaxDataLengthExceed.setStatus("current")


class _AxIpv4InIpv6FragmentReassemblyFailure_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6FragmentReassemblyFailure based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6FragmentReassemblyFailure_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6FragmentReassemblyFailure_Object = MibScalar
axIpv4InIpv6FragmentReassemblyFailure = _AxIpv4InIpv6FragmentReassemblyFailure_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 35),
    _AxIpv4InIpv6FragmentReassemblyFailure_Type()
)
axIpv4InIpv6FragmentReassemblyFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6FragmentReassemblyFailure.setStatus("current")


class _AxIpv4InIpv6MtuExceedPolicyDrop_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6MtuExceedPolicyDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6MtuExceedPolicyDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6MtuExceedPolicyDrop_Object = MibScalar
axIpv4InIpv6MtuExceedPolicyDrop = _AxIpv4InIpv6MtuExceedPolicyDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 36),
    _AxIpv4InIpv6MtuExceedPolicyDrop_Type()
)
axIpv4InIpv6MtuExceedPolicyDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6MtuExceedPolicyDrop.setStatus("current")


class _AxIpv4InIpv6FragmentProcessingDrop_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6FragmentProcessingDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6FragmentProcessingDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6FragmentProcessingDrop_Object = MibScalar
axIpv4InIpv6FragmentProcessingDrop = _AxIpv4InIpv6FragmentProcessingDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 37),
    _AxIpv4InIpv6FragmentProcessingDrop_Type()
)
axIpv4InIpv6FragmentProcessingDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6FragmentProcessingDrop.setStatus("current")


class _AxIpv4InIpv6TooManyPacketsPerReassemblyDrop_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6TooManyPacketsPerReassemblyDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6TooManyPacketsPerReassemblyDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6TooManyPacketsPerReassemblyDrop_Object = MibScalar
axIpv4InIpv6TooManyPacketsPerReassemblyDrop = _AxIpv4InIpv6TooManyPacketsPerReassemblyDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 38),
    _AxIpv4InIpv6TooManyPacketsPerReassemblyDrop_Type()
)
axIpv4InIpv6TooManyPacketsPerReassemblyDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6TooManyPacketsPerReassemblyDrop.setStatus("current")


class _AxIpv4InIpv6SessionMaxPacketsExceed_Type(CounterBasedGauge64):
    """Custom type axIpv4InIpv6SessionMaxPacketsExceed based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv4InIpv6SessionMaxPacketsExceed_Type.__name__ = "CounterBasedGauge64"
_AxIpv4InIpv6SessionMaxPacketsExceed_Object = MibScalar
axIpv4InIpv6SessionMaxPacketsExceed = _AxIpv4InIpv6SessionMaxPacketsExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 3, 39),
    _AxIpv4InIpv6SessionMaxPacketsExceed_Type()
)
axIpv4InIpv6SessionMaxPacketsExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv4InIpv6SessionMaxPacketsExceed.setStatus("current")
_AxIpv6InIpv4FragmentStats_ObjectIdentity = ObjectIdentity
axIpv6InIpv4FragmentStats = _AxIpv6InIpv4FragmentStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4)
)


class _AxIpv6InIpv4SessionInsert_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4SessionInsert based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4SessionInsert_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4SessionInsert_Object = MibScalar
axIpv6InIpv4SessionInsert = _AxIpv6InIpv4SessionInsert_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 1),
    _AxIpv6InIpv4SessionInsert_Type()
)
axIpv6InIpv4SessionInsert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4SessionInsert.setStatus("current")


class _AxIpv6InIpv4SessionExpired_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4SessionExpired based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4SessionExpired_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4SessionExpired_Object = MibScalar
axIpv6InIpv4SessionExpired = _AxIpv6InIpv4SessionExpired_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 2),
    _AxIpv6InIpv4SessionExpired_Type()
)
axIpv6InIpv4SessionExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4SessionExpired.setStatus("current")


class _AxIpv6InIpv4IcmpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4IcmpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4IcmpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4IcmpReceived_Object = MibScalar
axIpv6InIpv4IcmpReceived = _AxIpv6InIpv4IcmpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 3),
    _AxIpv6InIpv4IcmpReceived_Type()
)
axIpv6InIpv4IcmpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4IcmpReceived.setStatus("current")


class _AxIpv6InIpv4Icmpv6Received_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4Icmpv6Received based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4Icmpv6Received_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4Icmpv6Received_Object = MibScalar
axIpv6InIpv4Icmpv6Received = _AxIpv6InIpv4Icmpv6Received_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 4),
    _AxIpv6InIpv4Icmpv6Received_Type()
)
axIpv6InIpv4Icmpv6Received.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4Icmpv6Received.setStatus("current")


class _AxIpv6InIpv4UdpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4UdpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4UdpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4UdpReceived_Object = MibScalar
axIpv6InIpv4UdpReceived = _AxIpv6InIpv4UdpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 5),
    _AxIpv6InIpv4UdpReceived_Type()
)
axIpv6InIpv4UdpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4UdpReceived.setStatus("current")


class _AxIpv6InIpv4TcpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4TcpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4TcpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4TcpReceived_Object = MibScalar
axIpv6InIpv4TcpReceived = _AxIpv6InIpv4TcpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 6),
    _AxIpv6InIpv4TcpReceived_Type()
)
axIpv6InIpv4TcpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4TcpReceived.setStatus("current")


class _AxIpv6InIpv4IpInIpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4IpInIpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4IpInIpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4IpInIpReceived_Object = MibScalar
axIpv6InIpv4IpInIpReceived = _AxIpv6InIpv4IpInIpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 7),
    _AxIpv6InIpv4IpInIpReceived_Type()
)
axIpv6InIpv4IpInIpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4IpInIpReceived.setStatus("current")


class _AxIpv6InIpv4Ipv6InIpReceived_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4Ipv6InIpReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4Ipv6InIpReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4Ipv6InIpReceived_Object = MibScalar
axIpv6InIpv4Ipv6InIpReceived = _AxIpv6InIpv4Ipv6InIpReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 8),
    _AxIpv6InIpv4Ipv6InIpReceived_Type()
)
axIpv6InIpv4Ipv6InIpReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4Ipv6InIpReceived.setStatus("current")


class _AxIpv6InIpv4OtherReceived_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4OtherReceived based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4OtherReceived_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4OtherReceived_Object = MibScalar
axIpv6InIpv4OtherReceived = _AxIpv6InIpv4OtherReceived_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 9),
    _AxIpv6InIpv4OtherReceived_Type()
)
axIpv6InIpv4OtherReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4OtherReceived.setStatus("current")


class _AxIpv6InIpv4IcmpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4IcmpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4IcmpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4IcmpDropped_Object = MibScalar
axIpv6InIpv4IcmpDropped = _AxIpv6InIpv4IcmpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 10),
    _AxIpv6InIpv4IcmpDropped_Type()
)
axIpv6InIpv4IcmpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4IcmpDropped.setStatus("current")


class _AxIpv6InIpv4Icmpv6Dropped_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4Icmpv6Dropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4Icmpv6Dropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4Icmpv6Dropped_Object = MibScalar
axIpv6InIpv4Icmpv6Dropped = _AxIpv6InIpv4Icmpv6Dropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 11),
    _AxIpv6InIpv4Icmpv6Dropped_Type()
)
axIpv6InIpv4Icmpv6Dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4Icmpv6Dropped.setStatus("current")


class _AxIpv6InIpv4UdpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4UdpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4UdpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4UdpDropped_Object = MibScalar
axIpv6InIpv4UdpDropped = _AxIpv6InIpv4UdpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 12),
    _AxIpv6InIpv4UdpDropped_Type()
)
axIpv6InIpv4UdpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4UdpDropped.setStatus("current")


class _AxIpv6InIpv4TcpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4TcpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4TcpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4TcpDropped_Object = MibScalar
axIpv6InIpv4TcpDropped = _AxIpv6InIpv4TcpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 13),
    _AxIpv6InIpv4TcpDropped_Type()
)
axIpv6InIpv4TcpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4TcpDropped.setStatus("current")


class _AxIpv6InIpv4IpInIpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4IpInIpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4IpInIpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4IpInIpDropped_Object = MibScalar
axIpv6InIpv4IpInIpDropped = _AxIpv6InIpv4IpInIpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 14),
    _AxIpv6InIpv4IpInIpDropped_Type()
)
axIpv6InIpv4IpInIpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4IpInIpDropped.setStatus("current")


class _AxIpv6InIpv4Ipv6InIpDropped_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4Ipv6InIpDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4Ipv6InIpDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4Ipv6InIpDropped_Object = MibScalar
axIpv6InIpv4Ipv6InIpDropped = _AxIpv6InIpv4Ipv6InIpDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 15),
    _AxIpv6InIpv4Ipv6InIpDropped_Type()
)
axIpv6InIpv4Ipv6InIpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4Ipv6InIpDropped.setStatus("current")


class _AxIpv6InIpv4OtherDropped_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4OtherDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4OtherDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4OtherDropped_Object = MibScalar
axIpv6InIpv4OtherDropped = _AxIpv6InIpv4OtherDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 16),
    _AxIpv6InIpv4OtherDropped_Type()
)
axIpv6InIpv4OtherDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4OtherDropped.setStatus("current")


class _AxIpv6InIpv4OverlappingFragmentDropped_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4OverlappingFragmentDropped based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4OverlappingFragmentDropped_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4OverlappingFragmentDropped_Object = MibScalar
axIpv6InIpv4OverlappingFragmentDropped = _AxIpv6InIpv4OverlappingFragmentDropped_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 17),
    _AxIpv6InIpv4OverlappingFragmentDropped_Type()
)
axIpv6InIpv4OverlappingFragmentDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4OverlappingFragmentDropped.setStatus("current")


class _AxIpv6InIpv4BadIpLength_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4BadIpLength based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4BadIpLength_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4BadIpLength_Object = MibScalar
axIpv6InIpv4BadIpLength = _AxIpv6InIpv4BadIpLength_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 18),
    _AxIpv6InIpv4BadIpLength_Type()
)
axIpv6InIpv4BadIpLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4BadIpLength.setStatus("current")


class _AxIpv6InIpv4FragmentTooSmallDrop_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4FragmentTooSmallDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4FragmentTooSmallDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4FragmentTooSmallDrop_Object = MibScalar
axIpv6InIpv4FragmentTooSmallDrop = _AxIpv6InIpv4FragmentTooSmallDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 19),
    _AxIpv6InIpv4FragmentTooSmallDrop_Type()
)
axIpv6InIpv4FragmentTooSmallDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4FragmentTooSmallDrop.setStatus("current")


class _AxIpv6InIpv4FirstTcpFragmentTooSmallDrop_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4FirstTcpFragmentTooSmallDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4FirstTcpFragmentTooSmallDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4FirstTcpFragmentTooSmallDrop_Object = MibScalar
axIpv6InIpv4FirstTcpFragmentTooSmallDrop = _AxIpv6InIpv4FirstTcpFragmentTooSmallDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 20),
    _AxIpv6InIpv4FirstTcpFragmentTooSmallDrop_Type()
)
axIpv6InIpv4FirstTcpFragmentTooSmallDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4FirstTcpFragmentTooSmallDrop.setStatus("current")


class _AxIpv6InIpv4FirstL4FragmentTooSmallDrop_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4FirstL4FragmentTooSmallDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4FirstL4FragmentTooSmallDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4FirstL4FragmentTooSmallDrop_Object = MibScalar
axIpv6InIpv4FirstL4FragmentTooSmallDrop = _AxIpv6InIpv4FirstL4FragmentTooSmallDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 21),
    _AxIpv6InIpv4FirstL4FragmentTooSmallDrop_Type()
)
axIpv6InIpv4FirstL4FragmentTooSmallDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4FirstL4FragmentTooSmallDrop.setStatus("current")


class _AxIpv6InIpv4TotalSessionsExceedDrop_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4TotalSessionsExceedDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4TotalSessionsExceedDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4TotalSessionsExceedDrop_Object = MibScalar
axIpv6InIpv4TotalSessionsExceedDrop = _AxIpv6InIpv4TotalSessionsExceedDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 22),
    _AxIpv6InIpv4TotalSessionsExceedDrop_Type()
)
axIpv6InIpv4TotalSessionsExceedDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4TotalSessionsExceedDrop.setStatus("current")


class _AxIpv6InIpv4OutOfSessionMemory_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4OutOfSessionMemory based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4OutOfSessionMemory_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4OutOfSessionMemory_Object = MibScalar
axIpv6InIpv4OutOfSessionMemory = _AxIpv6InIpv4OutOfSessionMemory_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 23),
    _AxIpv6InIpv4OutOfSessionMemory_Type()
)
axIpv6InIpv4OutOfSessionMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4OutOfSessionMemory.setStatus("current")


class _AxIpv6InIpv4FragmentationFastAgingSet_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4FragmentationFastAgingSet based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4FragmentationFastAgingSet_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4FragmentationFastAgingSet_Object = MibScalar
axIpv6InIpv4FragmentationFastAgingSet = _AxIpv6InIpv4FragmentationFastAgingSet_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 24),
    _AxIpv6InIpv4FragmentationFastAgingSet_Type()
)
axIpv6InIpv4FragmentationFastAgingSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4FragmentationFastAgingSet.setStatus("current")


class _AxIpv6InIpv4FragmentationFastAgingUnset_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4FragmentationFastAgingUnset based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4FragmentationFastAgingUnset_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4FragmentationFastAgingUnset_Object = MibScalar
axIpv6InIpv4FragmentationFastAgingUnset = _AxIpv6InIpv4FragmentationFastAgingUnset_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 25),
    _AxIpv6InIpv4FragmentationFastAgingUnset_Type()
)
axIpv6InIpv4FragmentationFastAgingUnset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4FragmentationFastAgingUnset.setStatus("current")


class _AxIpv6InIpv4FragmentQueueSuccess_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4FragmentQueueSuccess based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4FragmentQueueSuccess_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4FragmentQueueSuccess_Object = MibScalar
axIpv6InIpv4FragmentQueueSuccess = _AxIpv6InIpv4FragmentQueueSuccess_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 26),
    _AxIpv6InIpv4FragmentQueueSuccess_Type()
)
axIpv6InIpv4FragmentQueueSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4FragmentQueueSuccess.setStatus("current")


class _AxIpv6InIpv4PayloadLengthUnaligned_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4PayloadLengthUnaligned based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4PayloadLengthUnaligned_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4PayloadLengthUnaligned_Object = MibScalar
axIpv6InIpv4PayloadLengthUnaligned = _AxIpv6InIpv4PayloadLengthUnaligned_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 27),
    _AxIpv6InIpv4PayloadLengthUnaligned_Type()
)
axIpv6InIpv4PayloadLengthUnaligned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4PayloadLengthUnaligned.setStatus("current")


class _AxIpv6InIpv4PayloadLengthOutOfBounds_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4PayloadLengthOutOfBounds based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4PayloadLengthOutOfBounds_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4PayloadLengthOutOfBounds_Object = MibScalar
axIpv6InIpv4PayloadLengthOutOfBounds = _AxIpv6InIpv4PayloadLengthOutOfBounds_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 28),
    _AxIpv6InIpv4PayloadLengthOutOfBounds_Type()
)
axIpv6InIpv4PayloadLengthOutOfBounds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4PayloadLengthOutOfBounds.setStatus("current")


class _AxIpv6InIpv4DuplicateFirstFragment_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4DuplicateFirstFragment based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4DuplicateFirstFragment_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4DuplicateFirstFragment_Object = MibScalar
axIpv6InIpv4DuplicateFirstFragment = _AxIpv6InIpv4DuplicateFirstFragment_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 29),
    _AxIpv6InIpv4DuplicateFirstFragment_Type()
)
axIpv6InIpv4DuplicateFirstFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4DuplicateFirstFragment.setStatus("current")


class _AxIpv6InIpv4DuplicateLastFragment_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4DuplicateLastFragment based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4DuplicateLastFragment_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4DuplicateLastFragment_Object = MibScalar
axIpv6InIpv4DuplicateLastFragment = _AxIpv6InIpv4DuplicateLastFragment_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 30),
    _AxIpv6InIpv4DuplicateLastFragment_Type()
)
axIpv6InIpv4DuplicateLastFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4DuplicateLastFragment.setStatus("current")


class _AxIpv6InIpv4TotalQueuedFragmentsExceed_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4TotalQueuedFragmentsExceed based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4TotalQueuedFragmentsExceed_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4TotalQueuedFragmentsExceed_Object = MibScalar
axIpv6InIpv4TotalQueuedFragmentsExceed = _AxIpv6InIpv4TotalQueuedFragmentsExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 31),
    _AxIpv6InIpv4TotalQueuedFragmentsExceed_Type()
)
axIpv6InIpv4TotalQueuedFragmentsExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4TotalQueuedFragmentsExceed.setStatus("current")


class _AxIpv6InIpv4FragmentQueueFailure_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4FragmentQueueFailure based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4FragmentQueueFailure_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4FragmentQueueFailure_Object = MibScalar
axIpv6InIpv4FragmentQueueFailure = _AxIpv6InIpv4FragmentQueueFailure_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 32),
    _AxIpv6InIpv4FragmentQueueFailure_Type()
)
axIpv6InIpv4FragmentQueueFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4FragmentQueueFailure.setStatus("current")


class _AxIpv6InIpv4FragmentReassemblySuccess_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4FragmentReassemblySuccess based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4FragmentReassemblySuccess_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4FragmentReassemblySuccess_Object = MibScalar
axIpv6InIpv4FragmentReassemblySuccess = _AxIpv6InIpv4FragmentReassemblySuccess_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 33),
    _AxIpv6InIpv4FragmentReassemblySuccess_Type()
)
axIpv6InIpv4FragmentReassemblySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4FragmentReassemblySuccess.setStatus("current")


class _AxIpv6InIpv4FragmentMaxDataLengthExceed_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4FragmentMaxDataLengthExceed based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4FragmentMaxDataLengthExceed_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4FragmentMaxDataLengthExceed_Object = MibScalar
axIpv6InIpv4FragmentMaxDataLengthExceed = _AxIpv6InIpv4FragmentMaxDataLengthExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 34),
    _AxIpv6InIpv4FragmentMaxDataLengthExceed_Type()
)
axIpv6InIpv4FragmentMaxDataLengthExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4FragmentMaxDataLengthExceed.setStatus("current")


class _AxIpv6InIpv4FragmentReassemblyFailure_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4FragmentReassemblyFailure based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4FragmentReassemblyFailure_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4FragmentReassemblyFailure_Object = MibScalar
axIpv6InIpv4FragmentReassemblyFailure = _AxIpv6InIpv4FragmentReassemblyFailure_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 35),
    _AxIpv6InIpv4FragmentReassemblyFailure_Type()
)
axIpv6InIpv4FragmentReassemblyFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4FragmentReassemblyFailure.setStatus("current")


class _AxIpv6InIpv4MtuExceedPolicyDrop_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4MtuExceedPolicyDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4MtuExceedPolicyDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4MtuExceedPolicyDrop_Object = MibScalar
axIpv6InIpv4MtuExceedPolicyDrop = _AxIpv6InIpv4MtuExceedPolicyDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 36),
    _AxIpv6InIpv4MtuExceedPolicyDrop_Type()
)
axIpv6InIpv4MtuExceedPolicyDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4MtuExceedPolicyDrop.setStatus("current")


class _AxIpv6InIpv4FragmentProcessingDrop_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4FragmentProcessingDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4FragmentProcessingDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4FragmentProcessingDrop_Object = MibScalar
axIpv6InIpv4FragmentProcessingDrop = _AxIpv6InIpv4FragmentProcessingDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 37),
    _AxIpv6InIpv4FragmentProcessingDrop_Type()
)
axIpv6InIpv4FragmentProcessingDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4FragmentProcessingDrop.setStatus("current")


class _AxIpv6InIpv4TooManyPacketsPerReassemblyDrop_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4TooManyPacketsPerReassemblyDrop based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4TooManyPacketsPerReassemblyDrop_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4TooManyPacketsPerReassemblyDrop_Object = MibScalar
axIpv6InIpv4TooManyPacketsPerReassemblyDrop = _AxIpv6InIpv4TooManyPacketsPerReassemblyDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 38),
    _AxIpv6InIpv4TooManyPacketsPerReassemblyDrop_Type()
)
axIpv6InIpv4TooManyPacketsPerReassemblyDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4TooManyPacketsPerReassemblyDrop.setStatus("current")


class _AxIpv6InIpv4SessionMaxPacketsExceed_Type(CounterBasedGauge64):
    """Custom type axIpv6InIpv4SessionMaxPacketsExceed based on CounterBasedGauge64"""
    defaultValue = 0


_AxIpv6InIpv4SessionMaxPacketsExceed_Type.__name__ = "CounterBasedGauge64"
_AxIpv6InIpv4SessionMaxPacketsExceed_Object = MibScalar
axIpv6InIpv4SessionMaxPacketsExceed = _AxIpv6InIpv4SessionMaxPacketsExceed_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 21, 1, 4, 39),
    _AxIpv6InIpv4SessionMaxPacketsExceed_Type()
)
axIpv6InIpv4SessionMaxPacketsExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axIpv6InIpv4SessionMaxPacketsExceed.setStatus("current")
_AxDDosStats_ObjectIdentity = ObjectIdentity
axDDosStats = _AxDDosStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 24, 1)
)
_AxDDosStatsL3EntryAdded_Type = CounterBasedGauge64
_AxDDosStatsL3EntryAdded_Object = MibScalar
axDDosStatsL3EntryAdded = _AxDDosStatsL3EntryAdded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 24, 1, 1),
    _AxDDosStatsL3EntryAdded_Type()
)
axDDosStatsL3EntryAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axDDosStatsL3EntryAdded.setStatus("current")
_AxDDosStatsL3EntryDeleted_Type = CounterBasedGauge64
_AxDDosStatsL3EntryDeleted_Object = MibScalar
axDDosStatsL3EntryDeleted = _AxDDosStatsL3EntryDeleted_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 24, 1, 2),
    _AxDDosStatsL3EntryDeleted_Type()
)
axDDosStatsL3EntryDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axDDosStatsL3EntryDeleted.setStatus("current")
_AxDDosStatsL3EntryAddedToBGP_Type = CounterBasedGauge64
_AxDDosStatsL3EntryAddedToBGP_Object = MibScalar
axDDosStatsL3EntryAddedToBGP = _AxDDosStatsL3EntryAddedToBGP_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 24, 1, 3),
    _AxDDosStatsL3EntryAddedToBGP_Type()
)
axDDosStatsL3EntryAddedToBGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axDDosStatsL3EntryAddedToBGP.setStatus("current")
_AxDDosStatsL3EntryRemovedFromBGP_Type = CounterBasedGauge64
_AxDDosStatsL3EntryRemovedFromBGP_Object = MibScalar
axDDosStatsL3EntryRemovedFromBGP = _AxDDosStatsL3EntryRemovedFromBGP_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 24, 1, 4),
    _AxDDosStatsL3EntryRemovedFromBGP_Type()
)
axDDosStatsL3EntryRemovedFromBGP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axDDosStatsL3EntryRemovedFromBGP.setStatus("current")
_AxDDosStatsL3EntryAddedToHW_Type = CounterBasedGauge64
_AxDDosStatsL3EntryAddedToHW_Object = MibScalar
axDDosStatsL3EntryAddedToHW = _AxDDosStatsL3EntryAddedToHW_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 24, 1, 5),
    _AxDDosStatsL3EntryAddedToHW_Type()
)
axDDosStatsL3EntryAddedToHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axDDosStatsL3EntryAddedToHW.setStatus("current")
_AxDDosStatsL3EntryRemovedFromHW_Type = CounterBasedGauge64
_AxDDosStatsL3EntryRemovedFromHW_Object = MibScalar
axDDosStatsL3EntryRemovedFromHW = _AxDDosStatsL3EntryRemovedFromHW_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 24, 1, 6),
    _AxDDosStatsL3EntryRemovedFromHW_Type()
)
axDDosStatsL3EntryRemovedFromHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axDDosStatsL3EntryRemovedFromHW.setStatus("current")
_AxDDosStatsTooManyL3Entries_Type = CounterBasedGauge64
_AxDDosStatsTooManyL3Entries_Object = MibScalar
axDDosStatsTooManyL3Entries = _AxDDosStatsTooManyL3Entries_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 24, 1, 7),
    _AxDDosStatsTooManyL3Entries_Type()
)
axDDosStatsTooManyL3Entries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axDDosStatsTooManyL3Entries.setStatus("current")
_AxDDosStatsL3EntryMatchDrop_Type = CounterBasedGauge64
_AxDDosStatsL3EntryMatchDrop_Object = MibScalar
axDDosStatsL3EntryMatchDrop = _AxDDosStatsL3EntryMatchDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 24, 1, 8),
    _AxDDosStatsL3EntryMatchDrop_Type()
)
axDDosStatsL3EntryMatchDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axDDosStatsL3EntryMatchDrop.setStatus("current")
_AxDDosStatsHWL3EntryMatchDrop_Type = CounterBasedGauge64
_AxDDosStatsHWL3EntryMatchDrop_Object = MibScalar
axDDosStatsHWL3EntryMatchDrop = _AxDDosStatsHWL3EntryMatchDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 24, 1, 9),
    _AxDDosStatsHWL3EntryMatchDrop_Type()
)
axDDosStatsHWL3EntryMatchDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axDDosStatsHWL3EntryMatchDrop.setStatus("current")
_AxDDosStatsL4EntryAdded_Type = CounterBasedGauge64
_AxDDosStatsL4EntryAdded_Object = MibScalar
axDDosStatsL4EntryAdded = _AxDDosStatsL4EntryAdded_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 24, 1, 10),
    _AxDDosStatsL4EntryAdded_Type()
)
axDDosStatsL4EntryAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axDDosStatsL4EntryAdded.setStatus("current")
_AxDDosStatsL4EntryDeleted_Type = CounterBasedGauge64
_AxDDosStatsL4EntryDeleted_Object = MibScalar
axDDosStatsL4EntryDeleted = _AxDDosStatsL4EntryDeleted_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 24, 1, 11),
    _AxDDosStatsL4EntryDeleted_Type()
)
axDDosStatsL4EntryDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axDDosStatsL4EntryDeleted.setStatus("current")
_AxDDosStatsL4EntryAddedToHW_Type = CounterBasedGauge64
_AxDDosStatsL4EntryAddedToHW_Object = MibScalar
axDDosStatsL4EntryAddedToHW = _AxDDosStatsL4EntryAddedToHW_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 24, 1, 12),
    _AxDDosStatsL4EntryAddedToHW_Type()
)
axDDosStatsL4EntryAddedToHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axDDosStatsL4EntryAddedToHW.setStatus("current")
_AxDDosStatsL4EntryRemovedFromHW_Type = CounterBasedGauge64
_AxDDosStatsL4EntryRemovedFromHW_Object = MibScalar
axDDosStatsL4EntryRemovedFromHW = _AxDDosStatsL4EntryRemovedFromHW_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 24, 1, 13),
    _AxDDosStatsL4EntryRemovedFromHW_Type()
)
axDDosStatsL4EntryRemovedFromHW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axDDosStatsL4EntryRemovedFromHW.setStatus("current")
_AxDDosStatsHWOutOfL4Entries_Type = CounterBasedGauge64
_AxDDosStatsHWOutOfL4Entries_Object = MibScalar
axDDosStatsHWOutOfL4Entries = _AxDDosStatsHWOutOfL4Entries_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 24, 1, 14),
    _AxDDosStatsHWOutOfL4Entries_Type()
)
axDDosStatsHWOutOfL4Entries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axDDosStatsHWOutOfL4Entries.setStatus("current")
_AxDDosStatsL4EntryMatchDrop_Type = CounterBasedGauge64
_AxDDosStatsL4EntryMatchDrop_Object = MibScalar
axDDosStatsL4EntryMatchDrop = _AxDDosStatsL4EntryMatchDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 24, 1, 15),
    _AxDDosStatsL4EntryMatchDrop_Type()
)
axDDosStatsL4EntryMatchDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axDDosStatsL4EntryMatchDrop.setStatus("current")
_AxDDosStatsHWL4EntryMatchDrop_Type = CounterBasedGauge64
_AxDDosStatsHWL4EntryMatchDrop_Object = MibScalar
axDDosStatsHWL4EntryMatchDrop = _AxDDosStatsHWL4EntryMatchDrop_Object(
    (1, 3, 6, 1, 4, 1, 22610, 2, 4, 3, 24, 1, 16),
    _AxDDosStatsHWL4EntryMatchDrop_Type()
)
axDDosStatsHWL4EntryMatchDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    axDDosStatsHWL4EntryMatchDrop.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A10-AX-CGN-MIB",
    **{"axIpNatLsnGlobalStats": axIpNatLsnGlobalStats,
       "axIpNatLsnTotalUserQuotaSessions": axIpNatLsnTotalUserQuotaSessions,
       "axIpNatLsnTotalIpAddrTranslated": axIpNatLsnTotalIpAddrTranslated,
       "axIpNatLsnTotalFullConeSessions": axIpNatLsnTotalFullConeSessions,
       "axIpNatLsnTrafficStats": axIpNatLsnTrafficStats,
       "axIpNatLsnTrafficFullConeSessionCreated": axIpNatLsnTrafficFullConeSessionCreated,
       "axIpNatLsnTrafficFullConeSessionFreed": axIpNatLsnTrafficFullConeSessionFreed,
       "axIpNatLsnTrafficFailsInFullConeSessionCreation": axIpNatLsnTrafficFailsInFullConeSessionCreation,
       "axIpNatLsnTrafficHairpinSessionCreated": axIpNatLsnTrafficHairpinSessionCreated,
       "axIpNatLsnTrafficEndpointIndepMapMatch": axIpNatLsnTrafficEndpointIndepMapMatch,
       "axIpNatLsnTrafficEndpointIndepFilterMatch": axIpNatLsnTrafficEndpointIndepFilterMatch,
       "axIpNatLsnTrafficUserQuotasCreated": axIpNatLsnTrafficUserQuotasCreated,
       "axIpNatLsnTrafficUserQuotasFreed": axIpNatLsnTrafficUserQuotasFreed,
       "axIpNatLsnTrafficFailsInUserQuotasCreation": axIpNatLsnTrafficFailsInUserQuotasCreation,
       "axIpNatLsnTrafficIcmpUserQuotasExceeded": axIpNatLsnTrafficIcmpUserQuotasExceeded,
       "axIpNatLsnTrafficUdpUserQuotasExceeded": axIpNatLsnTrafficUdpUserQuotasExceeded,
       "axIpNatLsnTrafficTcpUserQuotasExceeded": axIpNatLsnTrafficTcpUserQuotasExceeded,
       "axIpNatLsnTrafficExtendedUserQuotasMatch": axIpNatLsnTrafficExtendedUserQuotasMatch,
       "axIpNatLsnTrafficExtendedUserQuotasExceeded": axIpNatLsnTrafficExtendedUserQuotasExceeded,
       "axIpNatLsnTrafficNatPortUnavailable": axIpNatLsnTrafficNatPortUnavailable,
       "axIpNatLsnTrafficNewUserResourceUnavailable": axIpNatLsnTrafficNewUserResourceUnavailable,
       "axIpNatLsnSessionStats": axIpNatLsnSessionStats,
       "axIpNatLsnSessionDataSessionsUsed": axIpNatLsnSessionDataSessionsUsed,
       "axIpNatLsnSessionDataSessionsFree": axIpNatLsnSessionDataSessionsFree,
       "axIpNatLsnSessionSmpSessionsUsed": axIpNatLsnSessionSmpSessionsUsed,
       "axIpNatLsnSessionSmpSessionsFree": axIpNatLsnSessionSmpSessionsFree,
       "axIpNatLsnNatPortUsageStats": axIpNatLsnNatPortUsageStats,
       "axIpNatLsnNatPortTcpNatPortUsed": axIpNatLsnNatPortTcpNatPortUsed,
       "axIpNatLsnNatPortTcpNatPortFree": axIpNatLsnNatPortTcpNatPortFree,
       "axIpNatLsnNatPortUdpNatPortUsed": axIpNatLsnNatPortUdpNatPortUsed,
       "axIpNatLsnNatPortUdpNatPortFree": axIpNatLsnNatPortUdpNatPortFree,
       "axIpNatLsnTop5PrivateIpAddrTotSessions": axIpNatLsnTop5PrivateIpAddrTotSessions,
       "axIpNatLsnTop5PrivateIpAddrTotSessionTable": axIpNatLsnTop5PrivateIpAddrTotSessionTable,
       "axIpNatLsnTop5PrivateIpAddrTotSessionEntry": axIpNatLsnTop5PrivateIpAddrTotSessionEntry,
       "axIpNatLsnTop5PrivateIpAddr": axIpNatLsnTop5PrivateIpAddr,
       "axIpNatLsnTop5PrivateIpAddrTotNumSessions": axIpNatLsnTop5PrivateIpAddrTotNumSessions,
       "axIpNatLsnTop5PrivateIpAddrGlobalIpAddr": axIpNatLsnTop5PrivateIpAddrGlobalIpAddr,
       "axIpNatLsnTop5PrivateIpAddrTotTcpPorts": axIpNatLsnTop5PrivateIpAddrTotTcpPorts,
       "axIpNatLsnTop5PrivateIpAddrTotTcpPortTable": axIpNatLsnTop5PrivateIpAddrTotTcpPortTable,
       "axIpNatLsnTop5PrivateIpAddrTotTcpPortEntry": axIpNatLsnTop5PrivateIpAddrTotTcpPortEntry,
       "axIpNatLsnTop5PrivateIpAddrInTcpPort": axIpNatLsnTop5PrivateIpAddrInTcpPort,
       "axIpNatLsnTop5PrivateIpAddrTotNumTcpPorts": axIpNatLsnTop5PrivateIpAddrTotNumTcpPorts,
       "axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInTcpPort": axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInTcpPort,
       "axIpNatLsnTop5PrivateIpAddrTotUdpPorts": axIpNatLsnTop5PrivateIpAddrTotUdpPorts,
       "axIpNatLsnTop5PrivateIpAddrTotUdpPortTable": axIpNatLsnTop5PrivateIpAddrTotUdpPortTable,
       "axIpNatLsnTop5PrivateIpAddrTotUdpPortEntry": axIpNatLsnTop5PrivateIpAddrTotUdpPortEntry,
       "axIpNatLsnTop5PrivateIpAddrInUdpPort": axIpNatLsnTop5PrivateIpAddrInUdpPort,
       "axIpNatLsnTop5PrivateIpAddrTotNumUdpPorts": axIpNatLsnTop5PrivateIpAddrTotNumUdpPorts,
       "axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInUdpPort": axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInUdpPort,
       "axIpNatLsnTop5PrivateIpAddrTotIcmpPorts": axIpNatLsnTop5PrivateIpAddrTotIcmpPorts,
       "axIpNatLsnTop5PrivateIpAddrTotIcmpPortTable": axIpNatLsnTop5PrivateIpAddrTotIcmpPortTable,
       "axIpNatLsnTop5PrivateIpAddrTotIcmpPortEntry": axIpNatLsnTop5PrivateIpAddrTotIcmpPortEntry,
       "axIpNatLsnTop5PrivateIpAddrInIcmpPort": axIpNatLsnTop5PrivateIpAddrInIcmpPort,
       "axIpNatLsnTop5PrivateIpAddrTotNumIcmpPorts": axIpNatLsnTop5PrivateIpAddrTotNumIcmpPorts,
       "axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInIcmpPort": axIpNatLsnTop5PrivateIpAddrGlobalIpAddrInIcmpPort,
       "axIpNatLsnTop5UserPrivateIpAddrTotSessions": axIpNatLsnTop5UserPrivateIpAddrTotSessions,
       "axIpNatLsnTop5UserPrivateIpAddrTotSessionTable": axIpNatLsnTop5UserPrivateIpAddrTotSessionTable,
       "axIpNatLsnTop5UserPrivateIpAddrTotSessionEntry": axIpNatLsnTop5UserPrivateIpAddrTotSessionEntry,
       "axIpNatLsnTop5UserPrivateIpAddr": axIpNatLsnTop5UserPrivateIpAddr,
       "axIpNatLsnTop5UserPrivateIpAddrTotNumSessions": axIpNatLsnTop5UserPrivateIpAddrTotNumSessions,
       "axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddr": axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddr,
       "axIpNatLsnTop5UserPrivateIpAddrTotTcpSessions": axIpNatLsnTop5UserPrivateIpAddrTotTcpSessions,
       "axIpNatLsnTop5UserPrivateIpAddrTotTcpSessionTable": axIpNatLsnTop5UserPrivateIpAddrTotTcpSessionTable,
       "axIpNatLsnTop5UserPrivateIpAddrTotTcpSessionEntry": axIpNatLsnTop5UserPrivateIpAddrTotTcpSessionEntry,
       "axIpNatLsnTop5UserPrivateIpAddrInTcp": axIpNatLsnTop5UserPrivateIpAddrInTcp,
       "axIpNatLsnTop5UserPrivateIpAddrTotNumTcpSessions": axIpNatLsnTop5UserPrivateIpAddrTotNumTcpSessions,
       "axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInTcp": axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInTcp,
       "axIpNatLsnTop5UserPrivateIpAddrTotUdpSessions": axIpNatLsnTop5UserPrivateIpAddrTotUdpSessions,
       "axIpNatLsnTop5UserPrivateIpAddrTotUdpSessionTable": axIpNatLsnTop5UserPrivateIpAddrTotUdpSessionTable,
       "axIpNatLsnTop5UserPrivateIpAddrTotUdpSessionEntry": axIpNatLsnTop5UserPrivateIpAddrTotUdpSessionEntry,
       "axIpNatLsnTop5UserPrivateIpAddrInUdp": axIpNatLsnTop5UserPrivateIpAddrInUdp,
       "axIpNatLsnTop5UserPrivateIpAddrTotNumUdpSessions": axIpNatLsnTop5UserPrivateIpAddrTotNumUdpSessions,
       "axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInUdp": axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInUdp,
       "axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessions": axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessions,
       "axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionTable": axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionTable,
       "axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionEntry": axIpNatLsnTop5UserPrivateIpAddrTotIcmpSessionEntry,
       "axIpNatLsnTop5UserPrivateIpAddrInIcmp": axIpNatLsnTop5UserPrivateIpAddrInIcmp,
       "axIpNatLsnTop5UserPrivateIpAddrTotNumIcmpSessions": axIpNatLsnTop5UserPrivateIpAddrTotNumIcmpSessions,
       "axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInIcmp": axIpNatLsnTop5UserPrivateIpAddrGlobalIpAddrInIcmp,
       "axIpNatLsnTop5GlobalPoolIpAddrTotUsers": axIpNatLsnTop5GlobalPoolIpAddrTotUsers,
       "axIpNatLsnTop5GlobalPoolIpAddrTotUserTable": axIpNatLsnTop5GlobalPoolIpAddrTotUserTable,
       "axIpNatLsnTop5GlobalPoolIpAddrTotUserEntry": axIpNatLsnTop5GlobalPoolIpAddrTotUserEntry,
       "axIpNatLsnTop5GlobalPoolIpAddr": axIpNatLsnTop5GlobalPoolIpAddr,
       "axIpNatLsnTop5GlobalPoolIpAddrTotNumUsers": axIpNatLsnTop5GlobalPoolIpAddrTotNumUsers,
       "axIpNatLsnTop5GlobalPoolIpAddrTotTcpPorts": axIpNatLsnTop5GlobalPoolIpAddrTotTcpPorts,
       "axIpNatLsnTop5GlobalPoolIpAddrTotTcpPortTable": axIpNatLsnTop5GlobalPoolIpAddrTotTcpPortTable,
       "axIpNatLsnTop5GlobalPoolIpAddrTotTcpPortEntry": axIpNatLsnTop5GlobalPoolIpAddrTotTcpPortEntry,
       "axIpNatLsnTop5GlobalPoolIpAddrInTcp": axIpNatLsnTop5GlobalPoolIpAddrInTcp,
       "axIpNatLsnTop5GlobalPoolIpAddrTotNumTcpPorts": axIpNatLsnTop5GlobalPoolIpAddrTotNumTcpPorts,
       "axIpNatLsnTop5GlobalPoolIpAddrTotUdpPorts": axIpNatLsnTop5GlobalPoolIpAddrTotUdpPorts,
       "axIpNatLsnTop5GlobalPoolIpAddrTotUdpPortTable": axIpNatLsnTop5GlobalPoolIpAddrTotUdpPortTable,
       "axIpNatLsnTop5GlobalPoolIpAddrTotUdpPortEntry": axIpNatLsnTop5GlobalPoolIpAddrTotUdpPortEntry,
       "axIpNatLsnTop5GlobalPoolIpAddrInUdp": axIpNatLsnTop5GlobalPoolIpAddrInUdp,
       "axIpNatLsnTop5GlobalPoolIpAddrTotNumUdpPorts": axIpNatLsnTop5GlobalPoolIpAddrTotNumUdpPorts,
       "axIpNatLsnAlgSipStats": axIpNatLsnAlgSipStats,
       "axIpNatLsnAlgSipStatMethodRegister": axIpNatLsnAlgSipStatMethodRegister,
       "axIpNatLsnAlgSipStatMethodInvite": axIpNatLsnAlgSipStatMethodInvite,
       "axIpNatLsnAlgSipStatMethodAck": axIpNatLsnAlgSipStatMethodAck,
       "axIpNatLsnAlgSipStatMethodCancel": axIpNatLsnAlgSipStatMethodCancel,
       "axIpNatLsnAlgSipStatMethodBye": axIpNatLsnAlgSipStatMethodBye,
       "axIpNatLsnAlgSipStatMethodOptions": axIpNatLsnAlgSipStatMethodOptions,
       "axIpNatLsnAlgSipStatMethodPrack": axIpNatLsnAlgSipStatMethodPrack,
       "axIpNatLsnAlgSipStatMethodSubscribe": axIpNatLsnAlgSipStatMethodSubscribe,
       "axIpNatLsnAlgSipStatMethodNotify": axIpNatLsnAlgSipStatMethodNotify,
       "axIpNatLsnAlgSipStatMethodPublish": axIpNatLsnAlgSipStatMethodPublish,
       "axIpNatLsnAlgSipStatMethodInfo": axIpNatLsnAlgSipStatMethodInfo,
       "axIpNatLsnAlgSipStatMethodRefer": axIpNatLsnAlgSipStatMethodRefer,
       "axIpNatLsnAlgSipStatMethodMessage": axIpNatLsnAlgSipStatMethodMessage,
       "axIpNatLsnAlgSipStatMethodUpdate": axIpNatLsnAlgSipStatMethodUpdate,
       "axIpNatLsnAlgSipStatMethodUnknown": axIpNatLsnAlgSipStatMethodUnknown,
       "axIpNatLsnPoolStats": axIpNatLsnPoolStats,
       "axIpNatLsnDataSessionUsed": axIpNatLsnDataSessionUsed,
       "axIpNatLsnDataSessionFreed": axIpNatLsnDataSessionFreed,
       "axIpNatLsnTCPNatPortUsed": axIpNatLsnTCPNatPortUsed,
       "axIpNatLsnTCPNatPortFree": axIpNatLsnTCPNatPortFree,
       "axIpNatLsnUDPNatPortUsed": axIpNatLsnUDPNatPortUsed,
       "axIpNatLsnUDPNatPortFree": axIpNatLsnUDPNatPortFree,
       "axIpNatLsnPoolStatTable": axIpNatLsnPoolStatTable,
       "axIpNatLsnPoolStatEntry": axIpNatLsnPoolStatEntry,
       "axIpNatLsnPoolStatPoolName": axIpNatLsnPoolStatPoolName,
       "axIpNatLsnPoolStatAddress": axIpNatLsnPoolStatAddress,
       "axIpNatLsnPoolStatUsers": axIpNatLsnPoolStatUsers,
       "axIpNatLsnPoolStatIcmpUsed": axIpNatLsnPoolStatIcmpUsed,
       "axIpNatLsnPoolStatIcmpFreed": axIpNatLsnPoolStatIcmpFreed,
       "axIpNatLsnPoolStatIcmpTotal": axIpNatLsnPoolStatIcmpTotal,
       "axIpNatLsnPoolStatIcmpReserved": axIpNatLsnPoolStatIcmpReserved,
       "axIpNatLsnPoolStatIcmpPeak": axIpNatLsnPoolStatIcmpPeak,
       "axIpNatLsnPoolStatIcmpHitFull": axIpNatLsnPoolStatIcmpHitFull,
       "axIpNatLsnPoolStatTcpUsed": axIpNatLsnPoolStatTcpUsed,
       "axIpNatLsnPoolStatTcpFreed": axIpNatLsnPoolStatTcpFreed,
       "axIpNatLsnPoolStatTcpTotal": axIpNatLsnPoolStatTcpTotal,
       "axIpNatLsnPoolStatTcpReserved": axIpNatLsnPoolStatTcpReserved,
       "axIpNatLsnPoolStatTcpPeak": axIpNatLsnPoolStatTcpPeak,
       "axIpNatLsnPoolStatTcpHitFull": axIpNatLsnPoolStatTcpHitFull,
       "axIpNatLsnPoolStatUdpUsed": axIpNatLsnPoolStatUdpUsed,
       "axIpNatLsnPoolStatUdpFreed": axIpNatLsnPoolStatUdpFreed,
       "axIpNatLsnPoolStatUdpTotal": axIpNatLsnPoolStatUdpTotal,
       "axIpNatLsnPoolStatUdpReserved": axIpNatLsnPoolStatUdpReserved,
       "axIpNatLsnPoolStatUdpPeak": axIpNatLsnPoolStatUdpPeak,
       "axIpNatLsnPoolStatUdpHitFull": axIpNatLsnPoolStatUdpHitFull,
       "axIpNatLsnPoolNameStatTable": axIpNatLsnPoolNameStatTable,
       "axIpNatLsnPoolNameStatEntry": axIpNatLsnPoolNameStatEntry,
       "axIpNatLsnPoolNameStatPoolName": axIpNatLsnPoolNameStatPoolName,
       "axIpNatLsnPoolNameStatAddress": axIpNatLsnPoolNameStatAddress,
       "axIpNatLsnPoolNameEndAddress": axIpNatLsnPoolNameEndAddress,
       "axIpNatLsnPoolNameStatUsers": axIpNatLsnPoolNameStatUsers,
       "axIpNatLsnPoolNameStatIcmpUsed": axIpNatLsnPoolNameStatIcmpUsed,
       "axIpNatLsnPoolNameStatIcmpFreed": axIpNatLsnPoolNameStatIcmpFreed,
       "axIpNatLsnPoolNameStatIcmpTotal": axIpNatLsnPoolNameStatIcmpTotal,
       "axIpNatLsnPoolNameStatIcmpReserved": axIpNatLsnPoolNameStatIcmpReserved,
       "axIpNatLsnPoolNameStatIcmpPeak": axIpNatLsnPoolNameStatIcmpPeak,
       "axIpNatLsnPoolNameStatIcmpHitFull": axIpNatLsnPoolNameStatIcmpHitFull,
       "axIpNatLsnPoolNameStatTcpUsed": axIpNatLsnPoolNameStatTcpUsed,
       "axIpNatLsnPoolNameStatTcpFreed": axIpNatLsnPoolNameStatTcpFreed,
       "axIpNatLsnPoolNameStatTcpTotal": axIpNatLsnPoolNameStatTcpTotal,
       "axIpNatLsnPoolNameStatTcpReserved": axIpNatLsnPoolNameStatTcpReserved,
       "axIpNatLsnPoolNameStatTcpPeak": axIpNatLsnPoolNameStatTcpPeak,
       "axIpNatLsnPoolNameStatTcpHitFull": axIpNatLsnPoolNameStatTcpHitFull,
       "axIpNatLsnPoolNameStatUdpUsed": axIpNatLsnPoolNameStatUdpUsed,
       "axIpNatLsnPoolNameStatUdpFreed": axIpNatLsnPoolNameStatUdpFreed,
       "axIpNatLsnPoolNameStatUdpTotal": axIpNatLsnPoolNameStatUdpTotal,
       "axIpNatLsnPoolNameStatUdpReserved": axIpNatLsnPoolNameStatUdpReserved,
       "axIpNatLsnPoolNameStatUdpPeak": axIpNatLsnPoolNameStatUdpPeak,
       "axIpNatLsnPoolNameStatUdpHitFull": axIpNatLsnPoolNameStatUdpHitFull,
       "axIpNatLsnPoolGroup": axIpNatLsnPoolGroup,
       "axIpNatLsnPoolGroupCount": axIpNatLsnPoolGroupCount,
       "axIpNatLsnPoolGroupTable": axIpNatLsnPoolGroupTable,
       "axIpNatLsnPoolGroupEntry": axIpNatLsnPoolGroupEntry,
       "axIpNatLsnPoolGroupName": axIpNatLsnPoolGroupName,
       "axIpNatLsnPoolGroupUsers": axIpNatLsnPoolGroupUsers,
       "axIpNatLsnPoolGroupIcmpUsed": axIpNatLsnPoolGroupIcmpUsed,
       "axIpNatLsnPoolGroupIcmpFreed": axIpNatLsnPoolGroupIcmpFreed,
       "axIpNatLsnPoolGroupIcmpTotal": axIpNatLsnPoolGroupIcmpTotal,
       "axIpNatLsnPoolGroupIcmpReserved": axIpNatLsnPoolGroupIcmpReserved,
       "axIpNatLsnPoolGroupIcmpPeak": axIpNatLsnPoolGroupIcmpPeak,
       "axIpNatLsnPoolGroupIcmpHitFull": axIpNatLsnPoolGroupIcmpHitFull,
       "axIpNatLsnPoolGroupTcpUsed": axIpNatLsnPoolGroupTcpUsed,
       "axIpNatLsnPoolGroupTcpFreed": axIpNatLsnPoolGroupTcpFreed,
       "axIpNatLsnPoolGroupTcpTotal": axIpNatLsnPoolGroupTcpTotal,
       "axIpNatLsnPoolGroupTcpReserved": axIpNatLsnPoolGroupTcpReserved,
       "axIpNatLsnPoolGroupTcpPeak": axIpNatLsnPoolGroupTcpPeak,
       "axIpNatLsnPoolGroupTcpHitFull": axIpNatLsnPoolGroupTcpHitFull,
       "axIpNatLsnPoolGroupUdpUsed": axIpNatLsnPoolGroupUdpUsed,
       "axIpNatLsnPoolGroupUdpFreed": axIpNatLsnPoolGroupUdpFreed,
       "axIpNatLsnPoolGroupUdpTotal": axIpNatLsnPoolGroupUdpTotal,
       "axIpNatLsnPoolGroupUdpReserved": axIpNatLsnPoolGroupUdpReserved,
       "axIpNatLsnPoolGroupUdpPeak": axIpNatLsnPoolGroupUdpPeak,
       "axIpNatLsnPoolGroupUdpHitFull": axIpNatLsnPoolGroupUdpHitFull,
       "axIpNatLsnPoolGroupTotalIp": axIpNatLsnPoolGroupTotalIp,
       "axIpNatLsnPoolGroupUsedIp": axIpNatLsnPoolGroupUsedIp,
       "axIpNatLsnPoolGroupFreedIp": axIpNatLsnPoolGroupFreedIp,
       "axIpNatLsnRadiusStats": axIpNatLsnRadiusStats,
       "axIpNatLsnMSISDNReceived": axIpNatLsnMSISDNReceived,
       "axIpNatLsnRadiusIMEIReceived": axIpNatLsnRadiusIMEIReceived,
       "axIpNatLsnRadiusIMSIReceived": axIpNatLsnRadiusIMSIReceived,
       "axIpNatLsnCustAttrReceived": axIpNatLsnCustAttrReceived,
       "axIpNatLsnRadiusRequestReceived": axIpNatLsnRadiusRequestReceived,
       "axIpNatLsnRadiusRequestBadSecretDropped": axIpNatLsnRadiusRequestBadSecretDropped,
       "axIpNatLsnRadiusRequestNoKeyAttrDropped": axIpNatLsnRadiusRequestNoKeyAttrDropped,
       "axIpNatLsnRadiusRequestMalFormedDropped": axIpNatLsnRadiusRequestMalFormedDropped,
       "axIpNatLsnRadiusRequestIgnored": axIpNatLsnRadiusRequestIgnored,
       "axIpNatLsnRadiusRequestTableFullDropped": axIpNatLsnRadiusRequestTableFullDropped,
       "axIpNatLsnHAStandbyDropped": axIpNatLsnHAStandbyDropped,
       "axIpNatLsnRadiusSecretNotConfigDropped": axIpNatLsnRadiusSecretNotConfigDropped,
       "axIpNatNat64StatsGlobal": axIpNatNat64StatsGlobal,
       "axIpNatNat64StatTotalTcpPortAlloc": axIpNatNat64StatTotalTcpPortAlloc,
       "axIpNatNat64StatTotalTcpPortFreed": axIpNatNat64StatTotalTcpPortFreed,
       "axIpNatNat64StatTotalUdpPortAlloc": axIpNatNat64StatTotalUdpPortAlloc,
       "axIpNatNat64StatTotalUdpPortFreed": axIpNatNat64StatTotalUdpPortFreed,
       "axIpNatNat64StatTotalIcmpPortAlloc": axIpNatNat64StatTotalIcmpPortAlloc,
       "axIpNatNat64StatTotalIcmpPortFreed": axIpNatNat64StatTotalIcmpPortFreed,
       "axIpNatNat64StatDataSessionCreated": axIpNatNat64StatDataSessionCreated,
       "axIpNatNat64StatDataSessionFreed": axIpNatNat64StatDataSessionFreed,
       "axIpNatNat64UserQuotaCreated": axIpNatNat64UserQuotaCreated,
       "axIpNatNat64UserQuotaFreed": axIpNatNat64UserQuotaFreed,
       "axIpNatNat64UserQuotaCreateFailed": axIpNatNat64UserQuotaCreateFailed,
       "axIpNatNat64StatTcpNatPortUnAvail": axIpNatNat64StatTcpNatPortUnAvail,
       "axIpNatNat64StatUdpNatPortUnAvail": axIpNatNat64StatUdpNatPortUnAvail,
       "axIpNatNat64StatIcmpNatPortUnavail": axIpNatNat64StatIcmpNatPortUnavail,
       "axIpNatNat64StatNewUserResourceUnAvail": axIpNatNat64StatNewUserResourceUnAvail,
       "axIpNatNat64StatTcpUserQuotaExceed": axIpNatNat64StatTcpUserQuotaExceed,
       "axIpNatNat64StatUdpUserQuotaExceed": axIpNatNat64StatUdpUserQuotaExceed,
       "axIpNatNat64StatIcmpUserQuotaExceed": axIpNatNat64StatIcmpUserQuotaExceed,
       "axIpNatNat64StatExtendedUserQuotaMatched": axIpNatNat64StatExtendedUserQuotaMatched,
       "axIpNatNat64StatExtendedUserQuotaExceeded": axIpNatNat64StatExtendedUserQuotaExceeded,
       "axIpNatNat64StatTcpFullConeSessionCreated": axIpNatNat64StatTcpFullConeSessionCreated,
       "axIpNatNat64StatTcpFullConeSessionFreed": axIpNatNat64StatTcpFullConeSessionFreed,
       "axIpNatNat64StatUdpFullConeSessionCreated": axIpNatNat64StatUdpFullConeSessionCreated,
       "axIpNatNat64StatUdpFullConeSessionFreed": axIpNatNat64StatUdpFullConeSessionFreed,
       "axIpNatNat64StatFullConeSessionFailed": axIpNatNat64StatFullConeSessionFailed,
       "axIpNatNat64StatHairpinSessionCreated": axIpNatNat64StatHairpinSessionCreated,
       "axIpNatNat64StatSelfHairpinDrop": axIpNatNat64StatSelfHairpinDrop,
       "axIpNatNat64StatEndpointIndependentMapMatched": axIpNatNat64StatEndpointIndependentMapMatched,
       "axIpNatNat64StatEndpointIndependentFilterMatched": axIpNatNat64StatEndpointIndependentFilterMatched,
       "axIpNatNat64StatEndpointDependentFilterDrop": axIpNatNat64StatEndpointDependentFilterDrop,
       "axIpNatNat64StatLayer3ForwardPackets": axIpNatNat64StatLayer3ForwardPackets,
       "axIpNatNat64StatSourceAddrPrefixMatchDrop": axIpNatNat64StatSourceAddrPrefixMatchDrop,
       "axIpNatNat64StatLsnLidDrop": axIpNatNat64StatLsnLidDrop,
       "axIpNatNat64StatLsnLidPassThrough": axIpNatNat64StatLsnLidPassThrough,
       "axIpNatNat64StatNoClassListMatch": axIpNatNat64StatNoClassListMatch,
       "axIpNatNat64StatNatPoolMismatchDrop": axIpNatNat64StatNatPoolMismatchDrop,
       "axIpNatNat64StatDataSessionUserQuotaExceeded": axIpNatNat64StatDataSessionUserQuotaExceeded,
       "axIpNatNat64StatConnRateUserQuotaExceeded": axIpNatNat64StatConnRateUserQuotaExceeded,
       "axIpNatNat64StatEndPointIndependentFilteringInboundLimitExceeded": axIpNatNat64StatEndPointIndependentFilteringInboundLimitExceeded,
       "axIpNatNat64StatTcpPortOverloaded": axIpNatNat64StatTcpPortOverloaded,
       "axIpNatNat64StatUdpPortOverloaded": axIpNatNat64StatUdpPortOverloaded,
       "axIpNatNat64StatTcpPortOverloadingSessionCreated": axIpNatNat64StatTcpPortOverloadingSessionCreated,
       "axIpNatNat64StatUdpPortOverloadingSessionCreated": axIpNatNat64StatUdpPortOverloadingSessionCreated,
       "axIpNatNat64StatTcpPortOverloadingSessionFreed": axIpNatNat64StatTcpPortOverloadingSessionFreed,
       "axIpNatNat64StatUdpPortOverloadingSessionFreed": axIpNatNat64StatUdpPortOverloadingSessionFreed,
       "axIpNatNat64StatNatPoolUnusable": axIpNatNat64StatNatPoolUnusable,
       "axIpNatNat64StatHANatPoolUnusable": axIpNatNat64StatHANatPoolUnusable,
       "axIpNatNat64StatNoRadiusProfileMatch": axIpNatNat64StatNoRadiusProfileMatch,
       "axIpNatDsliteStatsGlobal": axIpNatDsliteStatsGlobal,
       "axIpNatDsliteStatTotalTcpPortAlloc": axIpNatDsliteStatTotalTcpPortAlloc,
       "axIpNatDsliteStatTotalTcpPortFreed": axIpNatDsliteStatTotalTcpPortFreed,
       "axIpNatDsliteStatTotalUdpPortAlloc": axIpNatDsliteStatTotalUdpPortAlloc,
       "axIpNatDsliteStatTotalUdpPortFreed": axIpNatDsliteStatTotalUdpPortFreed,
       "axIpNatDsliteStatTotalIcmpPortAlloc": axIpNatDsliteStatTotalIcmpPortAlloc,
       "axIpNatDsliteStatTotalIcmpPortFreed": axIpNatDsliteStatTotalIcmpPortFreed,
       "axIpNatDsliteStatDataSessionCreated": axIpNatDsliteStatDataSessionCreated,
       "axIpNatDsliteStatDataSessionFreed": axIpNatDsliteStatDataSessionFreed,
       "axIpNatDsliteUserQuotaCreated": axIpNatDsliteUserQuotaCreated,
       "axIpNatDsliteUserQuotaFreed": axIpNatDsliteUserQuotaFreed,
       "axIpNatDsliteUserQuotaCreateFailed": axIpNatDsliteUserQuotaCreateFailed,
       "axIpNatDsliteStatTcpNatPortUnAvail": axIpNatDsliteStatTcpNatPortUnAvail,
       "axIpNatDsliteStatUdpNatPortUnAvail": axIpNatDsliteStatUdpNatPortUnAvail,
       "axIpNatDsliteStatIcmpNatPortUnavail": axIpNatDsliteStatIcmpNatPortUnavail,
       "axIpNatDsliteStatNewUserResourceUnAvail": axIpNatDsliteStatNewUserResourceUnAvail,
       "axIpNatDsliteStatTcpUserQuotaExceed": axIpNatDsliteStatTcpUserQuotaExceed,
       "axIpNatDsliteStatUdpUserQuotaExceed": axIpNatDsliteStatUdpUserQuotaExceed,
       "axIpNatDsliteStatIcmpUserQuotaExceed": axIpNatDsliteStatIcmpUserQuotaExceed,
       "axIpNatDsliteStatExtendedUserQuotaMatched": axIpNatDsliteStatExtendedUserQuotaMatched,
       "axIpNatDsliteStatExtendedUserQuotaExceeded": axIpNatDsliteStatExtendedUserQuotaExceeded,
       "axIpNatDsliteStatTcpFullConeSessionCreated": axIpNatDsliteStatTcpFullConeSessionCreated,
       "axIpNatDsliteStatTcpFullConeSessionFreed": axIpNatDsliteStatTcpFullConeSessionFreed,
       "axIpNatDsliteStatUdpFullConeSessionCreated": axIpNatDsliteStatUdpFullConeSessionCreated,
       "axIpNatDsLiteStatUdpFullConeSessionFreed": axIpNatDsLiteStatUdpFullConeSessionFreed,
       "axIpNatDsLiteStatFullConeSessionFailed": axIpNatDsLiteStatFullConeSessionFailed,
       "axIpNatDsliteStatHairpinSessionCreated": axIpNatDsliteStatHairpinSessionCreated,
       "axIpNatDsliteStatSelfHairpinDrop": axIpNatDsliteStatSelfHairpinDrop,
       "axIpNatDsliteStatEndpointIndependentMapMatched": axIpNatDsliteStatEndpointIndependentMapMatched,
       "axIpNatDsliteStatEndpointIndependentFilterMatched": axIpNatDsliteStatEndpointIndependentFilterMatched,
       "axIpNatDsliteStatEndpointDependentFilterDrop": axIpNatDsliteStatEndpointDependentFilterDrop,
       "axIpNatDsliteStatTruncatedPacket": axIpNatDsliteStatTruncatedPacket,
       "axIpNatDsliteStatLsnLidDrop": axIpNatDsliteStatLsnLidDrop,
       "axIpNatDsliteStatLsnLidPassThrough": axIpNatDsliteStatLsnLidPassThrough,
       "axIpNatDsliteStatNoClassListMatch": axIpNatDsliteStatNoClassListMatch,
       "axIpNatDsliteStatPermitClassListDrop": axIpNatDsliteStatPermitClassListDrop,
       "axIpNatDsliteStatDataSessionUserQuotaExceeded": axIpNatDsliteStatDataSessionUserQuotaExceeded,
       "axIpNatDsliteStatConnRateUserQuotaExceeded": axIpNatDsliteStatConnRateUserQuotaExceeded,
       "axIpNatDsliteStatEndpointIndependentFilterInboundLimitExceeded": axIpNatDsliteStatEndpointIndependentFilterInboundLimitExceeded,
       "axIpNatDsliteStatNatPoolMismatchDrop": axIpNatDsliteStatNatPoolMismatchDrop,
       "axIpNatDsliteStatTcpPortOverloaded": axIpNatDsliteStatTcpPortOverloaded,
       "axIpNatDsliteStatUdpPortOverloaded": axIpNatDsliteStatUdpPortOverloaded,
       "axIpNatDsliteStatTcpPortOverloadingSessionCreated": axIpNatDsliteStatTcpPortOverloadingSessionCreated,
       "axIpNatDsliteStatUdpPortOverloadingSessionCreated": axIpNatDsliteStatUdpPortOverloadingSessionCreated,
       "axIpNatDsliteStatTcpPortOverloadingSessionFreed": axIpNatDsliteStatTcpPortOverloadingSessionFreed,
       "axIpNatDsliteStatUdpPortOverloadingSessionFreed": axIpNatDsliteStatUdpPortOverloadingSessionFreed,
       "axIpNatDsliteStatNatPoolUnusable": axIpNatDsliteStatNatPoolUnusable,
       "axIpNatDsliteStatNatHANatPoolUnusable": axIpNatDsliteStatNatHANatPoolUnusable,
       "axIpNatDsliteStatNoRadiusProfileMatch": axIpNatDsliteStatNoRadiusProfileMatch,
       "axIpNatStatsDynamicMappingAclNameTable": axIpNatStatsDynamicMappingAclNameTable,
       "axIpNatStatsDynamicMappingAclNameEntry": axIpNatStatsDynamicMappingAclNameEntry,
       "axIpNatStatsDynamicMappingAclNameAccessListName": axIpNatStatsDynamicMappingAclNameAccessListName,
       "axIpNatStatsDynamicMappingAclNameAccessListID": axIpNatStatsDynamicMappingAclNameAccessListID,
       "axIpNatStatsDynamicMappingAclNamePoolName": axIpNatStatsDynamicMappingAclNamePoolName,
       "axIpNatStatsDynamicMappingAclNameStartAddress": axIpNatStatsDynamicMappingAclNameStartAddress,
       "axIpNatStatsDynamicMappingAclNameEndAddress": axIpNatStatsDynamicMappingAclNameEndAddress,
       "axIpNatStatsDynamicMappingAclNameTotalAddresses": axIpNatStatsDynamicMappingAclNameTotalAddresses,
       "axIpNatStatsDynamicMappingAclNameAllocAddresses": axIpNatStatsDynamicMappingAclNameAllocAddresses,
       "axIpNatStatsDynamicMappingAclNameMissAddresses": axIpNatStatsDynamicMappingAclNameMissAddresses,
       "axIpNatStatsDynamicMappingAclNameStartAddressType": axIpNatStatsDynamicMappingAclNameStartAddressType,
       "axIpNatStatsDynamicMappingAclNameEndAddressType": axIpNatStatsDynamicMappingAclNameEndAddressType,
       "axIpNatLoggingGlobalStats": axIpNatLoggingGlobalStats,
       "axIpNatLoggingLogPktSent": axIpNatLoggingLogPktSent,
       "axIpNatLoggingTcpSessCreated": axIpNatLoggingTcpSessCreated,
       "axIpNatLoggingTcpSessDeleted": axIpNatLoggingTcpSessDeleted,
       "axIpNatLoggingTcpPortAllocated": axIpNatLoggingTcpPortAllocated,
       "axIpNatLoggingTcpPortFreed": axIpNatLoggingTcpPortFreed,
       "axIpNatLoggingTcpPortBatchAllocated": axIpNatLoggingTcpPortBatchAllocated,
       "axIpNatLoggingTcpPortBatchFreed": axIpNatLoggingTcpPortBatchFreed,
       "axIpNatLoggingUdpSessCreated": axIpNatLoggingUdpSessCreated,
       "axIpNatLoggingUdpSessDeleted": axIpNatLoggingUdpSessDeleted,
       "axIpNatLoggingUdpPortAllocated": axIpNatLoggingUdpPortAllocated,
       "axIpNatLoggingUdpPortFreed": axIpNatLoggingUdpPortFreed,
       "axIpNatLoggingUdpPortBatchAllocated": axIpNatLoggingUdpPortBatchAllocated,
       "axIpNatLoggingUdpPortBatchFreed": axIpNatLoggingUdpPortBatchFreed,
       "axIpNatLoggingIcmpSessCreated": axIpNatLoggingIcmpSessCreated,
       "axIpNatLoggingIcmpSessDeleted": axIpNatLoggingIcmpSessDeleted,
       "axIpNatLoggingIcmpResourceAllocated": axIpNatLoggingIcmpResourceAllocated,
       "axIpNatLoggingIcmpResourcetFreed": axIpNatLoggingIcmpResourcetFreed,
       "axIpNatLoggingIcmpV6SessCreated": axIpNatLoggingIcmpV6SessCreated,
       "axIpNatLoggingIcmpV6SessDeleted": axIpNatLoggingIcmpV6SessDeleted,
       "axIpNatLoggingIcmpV6ResourceAllocated": axIpNatLoggingIcmpV6ResourceAllocated,
       "axIpNatLoggingIcmpV6ResourcetFreed": axIpNatLoggingIcmpV6ResourcetFreed,
       "axIpNatLoggingGreSessCreated": axIpNatLoggingGreSessCreated,
       "axIpNatLoggingGreSessDeleted": axIpNatLoggingGreSessDeleted,
       "axIpNatLoggingGreResourceAllocated": axIpNatLoggingGreResourceAllocated,
       "axIpNatLoggingGreResourcetFreed": axIpNatLoggingGreResourcetFreed,
       "axIpNatLoggingEspSessCreated": axIpNatLoggingEspSessCreated,
       "axIpNatLoggingEspSessDeleted": axIpNatLoggingEspSessDeleted,
       "axIpNatLoggingEspResourceAllocated": axIpNatLoggingEspResourceAllocated,
       "axIpNatLoggingEspResourcetFreed": axIpNatLoggingEspResourcetFreed,
       "axIpNatLoggingFixedNatInsideUserPortMapping": axIpNatLoggingFixedNatInsideUserPortMapping,
       "axIpNatLoggingFixedNatDisabledConfigLogged": axIpNatLoggingFixedNatDisabledConfigLogged,
       "axIpNatLoggingFixedNatDisabledConfigLogsSent": axIpNatLoggingFixedNatDisabledConfigLogsSent,
       "axIpNatLoggingFixedNatPeriodicConfigLogsSent": axIpNatLoggingFixedNatPeriodicConfigLogsSent,
       "axIpNatLoggingFixedNatPeriodicConfigLogged": axIpNatLoggingFixedNatPeriodicConfigLogged,
       "axIpNatLoggingLogPacketsDrop": axIpNatLoggingLogPacketsDrop,
       "axIpNatTcpConnectionEstablished": axIpNatTcpConnectionEstablished,
       "axIpNatTcpConnectionLost": axIpNatTcpConnectionLost,
       "axIpNatTcpPortOverloadingAllocated": axIpNatTcpPortOverloadingAllocated,
       "axIpNatTcpPortOverloadingFreed": axIpNatTcpPortOverloadingFreed,
       "axIpNatUdpPortOverloadingAllocated": axIpNatUdpPortOverloadingAllocated,
       "axIpNatUdpPortOverloadingFreed": axIpNatUdpPortOverloadingFreed,
       "axIpNatHttpRequestLogged": axIpNatHttpRequestLogged,
       "axFixedNatGlobalStats": axFixedNatGlobalStats,
       "axFixedNatTotalNatAddressInUse": axFixedNatTotalNatAddressInUse,
       "axFixedNatTotalTcpPortsAllocated": axFixedNatTotalTcpPortsAllocated,
       "axFixedNatTotalTcpPortsFreed": axFixedNatTotalTcpPortsFreed,
       "axFixedNatTotalUdpPortsAllocated": axFixedNatTotalUdpPortsAllocated,
       "axFixedNatTotalUdpPortsFreed": axFixedNatTotalUdpPortsFreed,
       "axFixedNatTotalIcmpPortsAllocated": axFixedNatTotalIcmpPortsAllocated,
       "axFixedNatTotalIcmpPortsFreed": axFixedNatTotalIcmpPortsFreed,
       "axFixedNatTcpNatPortUnavailable": axFixedNatTcpNatPortUnavailable,
       "axFixedNatUdpNatPortUnavailable": axFixedNatUdpNatPortUnavailable,
       "axFixedNatIcmpNatPortUnavailable": axFixedNatIcmpNatPortUnavailable,
       "axFixedNatSessionUserQuotaExceed": axFixedNatSessionUserQuotaExceed,
       "axFixedNatFullConeSessionCreationFailed": axFixedNatFullConeSessionCreationFailed,
       "axFixedNatLidStandbyDrop": axFixedNatLidStandbyDrop,
       "axFixedNatSelfHairpinningDrop": axFixedNatSelfHairpinningDrop,
       "axFixedNatIpv6InIpv4PacketDrop": axFixedNatIpv6InIpv4PacketDrop,
       "axFixedNatDestRuleListDrop": axFixedNatDestRuleListDrop,
       "axFixedNatDestRuleListPassThrough": axFixedNatDestRuleListPassThrough,
       "axFixedNatNat44GlobalStats": axFixedNatNat44GlobalStats,
       "axFixedNatNat44DataSessionsCreated": axFixedNatNat44DataSessionsCreated,
       "axFixedNatNat44DataSessionsFreed": axFixedNatNat44DataSessionsFreed,
       "axFixedNatNat44TcpFullConeCreated": axFixedNatNat44TcpFullConeCreated,
       "axFixedNatNat44TcpFullConeFreed": axFixedNatNat44TcpFullConeFreed,
       "axFixedNatNat44UdpFullConeCreated": axFixedNatNat44UdpFullConeCreated,
       "axFixedNatNat44UdpFullConeFreed": axFixedNatNat44UdpFullConeFreed,
       "axFixedNatNat44UdpAlgFullConeCreated": axFixedNatNat44UdpAlgFullConeCreated,
       "axFixedNatNat44UdpAlgFullConeFreed": axFixedNatNat44UdpAlgFullConeFreed,
       "axFixedNatNat44EndpointIndependentMappingMatched": axFixedNatNat44EndpointIndependentMappingMatched,
       "axFixedNatNat44EndpointIndependentFilteringMatched": axFixedNatNat44EndpointIndependentFilteringMatched,
       "axFixedNatNat44EndpointIndependentFilteringDrop": axFixedNatNat44EndpointIndependentFilteringDrop,
       "axFixedNatNat44EndpointIndependentFilteringLimitExceed": axFixedNatNat44EndpointIndependentFilteringLimitExceed,
       "axFixedNatNat44HairpinSessionCreated": axFixedNatNat44HairpinSessionCreated,
       "axFixedNatNat64GlobalStats": axFixedNatNat64GlobalStats,
       "axFixedNatNat64DataSessionsCreated": axFixedNatNat64DataSessionsCreated,
       "axFixedNatNat64DataSessionsFreed": axFixedNatNat64DataSessionsFreed,
       "axFixedNatNat64TcpFullConeCreated": axFixedNatNat64TcpFullConeCreated,
       "axFixedNatNat64TcpFullConeFreed": axFixedNatNat64TcpFullConeFreed,
       "axFixedNatNat64UdpFullConeCreated": axFixedNatNat64UdpFullConeCreated,
       "axFixedNatNat64UdpFullConeFreed": axFixedNatNat64UdpFullConeFreed,
       "axFixedNatNat64UdpAlgFullConeCreated": axFixedNatNat64UdpAlgFullConeCreated,
       "axFixedNatNat64UdpAlgFullConeFreed": axFixedNatNat64UdpAlgFullConeFreed,
       "axFixedNatNat64EndpointIndependentMappingMatched": axFixedNatNat64EndpointIndependentMappingMatched,
       "axFixedNatNat64EndpointIndependentFilteringMatched": axFixedNatNat64EndpointIndependentFilteringMatched,
       "axFixedNatNat64EndpointIndependentFilteringDrop": axFixedNatNat64EndpointIndependentFilteringDrop,
       "axFixedNatNat64EndpointIndependentFilteringLimitExceed": axFixedNatNat64EndpointIndependentFilteringLimitExceed,
       "axFixedNatNat64HairpinSessionCreated": axFixedNatNat64HairpinSessionCreated,
       "axFixedNatDsliteGlobalStats": axFixedNatDsliteGlobalStats,
       "axFixedNatDsliteDataSessionsCreated": axFixedNatDsliteDataSessionsCreated,
       "axFixedNatDsliteDataSessionsFreed": axFixedNatDsliteDataSessionsFreed,
       "axFixedNatDsliteTcpFullConeCreated": axFixedNatDsliteTcpFullConeCreated,
       "axFixedNatDsliteTcpFullConeFreed": axFixedNatDsliteTcpFullConeFreed,
       "axFixedNatDsliteUdpFullConeCreated": axFixedNatDsliteUdpFullConeCreated,
       "axFixedNatDsliteUdpFullConeFreed": axFixedNatDsliteUdpFullConeFreed,
       "axFixedNatDsliteUdpAlgFullConeCreated": axFixedNatDsliteUdpAlgFullConeCreated,
       "axFixedNatDsliteUdpAlgFullConeFreed": axFixedNatDsliteUdpAlgFullConeFreed,
       "axFixedNatDsliteEndpointIndependentMappingMatched": axFixedNatDsliteEndpointIndependentMappingMatched,
       "axFixedNatDsliteEndpointIndependentFilteringMatched": axFixedNatDsliteEndpointIndependentFilteringMatched,
       "axFixedNatDsliteEndpointIndependentFilteringDrop": axFixedNatDsliteEndpointIndependentFilteringDrop,
       "axFixedNatDsliteEndpointIndependentFilteringLimitExceed": axFixedNatDsliteEndpointIndependentFilteringLimitExceed,
       "axFixedNatDsliteHairpinSessionCreated": axFixedNatDsliteHairpinSessionCreated,
       "axFixedNatAlgStats": axFixedNatAlgStats,
       "axFixedNatAlgEspStats": axFixedNatAlgEspStats,
       "axFixedNatAlgEspSessionCreated": axFixedNatAlgEspSessionCreated,
       "axFixedNatAlgFtpStats": axFixedNatAlgFtpStats,
       "axFixedNatAlgFtpPortReqFromClient": axFixedNatAlgFtpPortReqFromClient,
       "axFixedNatAlgFtpEprtReqFromClient": axFixedNatAlgFtpEprtReqFromClient,
       "axFixedNatAlgFtpLprtReqFromClient": axFixedNatAlgFtpLprtReqFromClient,
       "axFixedNatAlgFtpPasvRepFromServer": axFixedNatAlgFtpPasvRepFromServer,
       "axFixedNatAlgFtpEpsvRepFromServer": axFixedNatAlgFtpEpsvRepFromServer,
       "axFixedNatAlgFtpLpsvRepFromServer": axFixedNatAlgFtpLpsvRepFromServer,
       "axFixedNatAlgH323Stats": axFixedNatAlgH323Stats,
       "axFixedNatAlgH323H225RasMsg": axFixedNatAlgH323H225RasMsg,
       "axFixedNatAlgH323H225CallSigMsg": axFixedNatAlgH323H225CallSigMsg,
       "axFixedNatAlgH323H245MedCtrMsg": axFixedNatAlgH323H245MedCtrMsg,
       "axFixedNatAlgH323H245TunnelMsg": axFixedNatAlgH323H245TunnelMsg,
       "axFixedNatAlgH323FastStart": axFixedNatAlgH323FastStart,
       "axFixedNatAlgPptpStats": axFixedNatAlgPptpStats,
       "axFixedNatAlgPptpCallEsp": axFixedNatAlgPptpCallEsp,
       "axFixedNatAlgPptpMismatchedPnsCallId": axFixedNatAlgPptpMismatchedPnsCallId,
       "axFixedNatAlgPptpGreSessionCreated": axFixedNatAlgPptpGreSessionCreated,
       "axFixedNatAlgPptpGreSessionFreed": axFixedNatAlgPptpGreSessionFreed,
       "axFixedNatAlgPptpGreNoMatchGreSession": axFixedNatAlgPptpGreNoMatchGreSession,
       "axFixedNatAlgRtspStats": axFixedNatAlgRtspStats,
       "axFixedNatAlgRtspStreamCreated": axFixedNatAlgRtspStreamCreated,
       "axFixedNatAlgRtspStreamFreed": axFixedNatAlgRtspStreamFreed,
       "axFixedNatAlgRtspStreamCreationFailed": axFixedNatAlgRtspStreamCreationFailed,
       "axFixedNatAlgRtspStreamClientPortAllocated": axFixedNatAlgRtspStreamClientPortAllocated,
       "axFixedNatAlgRtspStreamClientPortFreed": axFixedNatAlgRtspStreamClientPortFreed,
       "axFixedNatAlgRtspStreamClientPortAllocationFailed": axFixedNatAlgRtspStreamClientPortAllocationFailed,
       "axFixedNatAlgRtspSrvRepWithUnknownClientPorts": axFixedNatAlgRtspSrvRepWithUnknownClientPorts,
       "axFixedNatAlgRtspDataSessionCreated": axFixedNatAlgRtspDataSessionCreated,
       "axFixedNatAlgRtspDataSessionFreed": axFixedNatAlgRtspDataSessionFreed,
       "axFixedNatAlgRtspDataSessionCreationFailed": axFixedNatAlgRtspDataSessionCreationFailed,
       "axFixedNatAlgSipStats": axFixedNatAlgSipStats,
       "axFixedNatAlgSipMethodReg": axFixedNatAlgSipMethodReg,
       "axFixedNatAlgSipMethodInvite": axFixedNatAlgSipMethodInvite,
       "axFixedNatAlgSipMethodAck": axFixedNatAlgSipMethodAck,
       "axFixedNatAlgSipMethodCancel": axFixedNatAlgSipMethodCancel,
       "axFixedNatAlgSipMethodBye": axFixedNatAlgSipMethodBye,
       "axFixedNatAlgSipMethodOptions": axFixedNatAlgSipMethodOptions,
       "axFixedNatAlgSipMethodPrack": axFixedNatAlgSipMethodPrack,
       "axFixedNatAlgSipMethodSubscribe": axFixedNatAlgSipMethodSubscribe,
       "axFixedNatAlgSipMethodNotify": axFixedNatAlgSipMethodNotify,
       "axFixedNatAlgSipMethodPublish": axFixedNatAlgSipMethodPublish,
       "axFixedNatAlgSipMethodInfo": axFixedNatAlgSipMethodInfo,
       "axFixedNatAlgSipMethodRefer": axFixedNatAlgSipMethodRefer,
       "axFixedNatAlgSipMethodMessage": axFixedNatAlgSipMethodMessage,
       "axFixedNatAlgSipMethodUpdate": axFixedNatAlgSipMethodUpdate,
       "axFixedNatAlgSipMethodUnknown": axFixedNatAlgSipMethodUnknown,
       "axFixedNatAlgTftpStats": axFixedNatAlgTftpStats,
       "axFixedNatAlgTftpClientSessionCreated": axFixedNatAlgTftpClientSessionCreated,
       "axFixedNatMapping": axFixedNatMapping,
       "axFixedNatPortMappingPortTable": axFixedNatPortMappingPortTable,
       "axFixedNatPortMappingPortEntry": axFixedNatPortMappingPortEntry,
       "axFixedNatPortMappingPortNatIpAddress": axFixedNatPortMappingPortNatIpAddress,
       "axFixedNatPortMappingPortInsideUser": axFixedNatPortMappingPortInsideUser,
       "axFixedNatPortMappingPortInsideUserIpType": axFixedNatPortMappingPortInsideUserIpType,
       "axFixedNatPortMappingPortTcpBeginPort": axFixedNatPortMappingPortTcpBeginPort,
       "axFixedNatPortMappingPortTcpEndPort": axFixedNatPortMappingPortTcpEndPort,
       "axFixedNatPortMappingPortUdpBeginPort": axFixedNatPortMappingPortUdpBeginPort,
       "axFixedNatPortMappingPortUdpEndPort": axFixedNatPortMappingPortUdpEndPort,
       "axFixedNatPortMappingPortIcmpBeginPort": axFixedNatPortMappingPortIcmpBeginPort,
       "axFixedNatPortMappingPortIcmpEndPort": axFixedNatPortMappingPortIcmpEndPort,
       "axFixedNatFullConeSess": axFixedNatFullConeSess,
       "axFixedNatFullConeSessDsliteTable": axFixedNatFullConeSessDsliteTable,
       "axFixedNatFullConeSessDsliteEntry": axFixedNatFullConeSessDsliteEntry,
       "axFixedNatFullConeSessDsliteNatIpAddress": axFixedNatFullConeSessDsliteNatIpAddress,
       "axFixedNatFullConeSessDsliteInsideUser": axFixedNatFullConeSessDsliteInsideUser,
       "axFixedNatFullConeSessDsliteProtType": axFixedNatFullConeSessDsliteProtType,
       "axFixedNatFullConeSessDsliteEIM": axFixedNatFullConeSessDsliteEIM,
       "axFixedNatFullConeSessDsliteEIF": axFixedNatFullConeSessDsliteEIF,
       "axFixedNatFullConeSessDsliteCPU": axFixedNatFullConeSessDsliteCPU,
       "axFixedNatFullConeSessDsliteAge": axFixedNatFullConeSessDsliteAge,
       "axFixedNatFullConeSessDslitePcpFlags": axFixedNatFullConeSessDslitePcpFlags,
       "axFixedNatFullConeSessNat44Table": axFixedNatFullConeSessNat44Table,
       "axFixedNatFullConeSessNat44Entry": axFixedNatFullConeSessNat44Entry,
       "axFixedNatFullConeSessNat44NatIpAddress": axFixedNatFullConeSessNat44NatIpAddress,
       "axFixedNatFullConeSessNat44InsideUser": axFixedNatFullConeSessNat44InsideUser,
       "axFixedNatFullConeSessNat44ProtType": axFixedNatFullConeSessNat44ProtType,
       "axFixedNatFullConeSessNat44EIM": axFixedNatFullConeSessNat44EIM,
       "axFixedNatFullConeSessNat44EIF": axFixedNatFullConeSessNat44EIF,
       "axFixedNatFullConeSessNat44CPU": axFixedNatFullConeSessNat44CPU,
       "axFixedNatFullConeSessNat44Age": axFixedNatFullConeSessNat44Age,
       "axFixedNatFullConeSessNat44PcpFlags": axFixedNatFullConeSessNat44PcpFlags,
       "axFixedNatFullConeSessNat64Table": axFixedNatFullConeSessNat64Table,
       "axFixedNatFullConeSessNat64Entry": axFixedNatFullConeSessNat64Entry,
       "axFixedNatFullConeSessNat64NatIpAddress": axFixedNatFullConeSessNat64NatIpAddress,
       "axFixedNatFullConeSessNat64InsideUser": axFixedNatFullConeSessNat64InsideUser,
       "axFixedNatFullConeSessNat64ProtType": axFixedNatFullConeSessNat64ProtType,
       "axFixedNatFullConeSessNat64EIM": axFixedNatFullConeSessNat64EIM,
       "axFixedNatFullConeSessNat64EIF": axFixedNatFullConeSessNat64EIF,
       "axFixedNatFullConeSessNat64CPU": axFixedNatFullConeSessNat64CPU,
       "axFixedNatFullConeSessNat64Age": axFixedNatFullConeSessNat64Age,
       "axFixedNatFullConeSessNat64PcpFlags": axFixedNatFullConeSessNat64PcpFlags,
       "axFixedNatTop5PrivateIpAddrTotSessions": axFixedNatTop5PrivateIpAddrTotSessions,
       "axFixedNatTop5PrivateIpAddrTotSessionTable": axFixedNatTop5PrivateIpAddrTotSessionTable,
       "axFixedNatTop5PrivateIpAddrTotSessionEntry": axFixedNatTop5PrivateIpAddrTotSessionEntry,
       "axFixedNatTop5PrivateIpAddr": axFixedNatTop5PrivateIpAddr,
       "axFixedNatTop5PrivateIpAddrTotNumSessions": axFixedNatTop5PrivateIpAddrTotNumSessions,
       "axFixedNatTop5PrivateIpAddrGlobalIpAddr": axFixedNatTop5PrivateIpAddrGlobalIpAddr,
       "axFixedNatTop5PrivateIpAddrTotTcpPorts": axFixedNatTop5PrivateIpAddrTotTcpPorts,
       "axFixedNatTop5PrivateIpAddrTotTcpPortTable": axFixedNatTop5PrivateIpAddrTotTcpPortTable,
       "axFixedNatTop5PrivateIpAddrTotTcpPortEntry": axFixedNatTop5PrivateIpAddrTotTcpPortEntry,
       "axFixedNatTop5PrivateIpAddrInTcpPort": axFixedNatTop5PrivateIpAddrInTcpPort,
       "axFixedNatTop5PrivateIpAddrTotNumInTcpPort": axFixedNatTop5PrivateIpAddrTotNumInTcpPort,
       "axFixedNatTop5PrivateIpAddrGlobalIpAddrInTcpPort": axFixedNatTop5PrivateIpAddrGlobalIpAddrInTcpPort,
       "axFixedNatTop5PrivateIpAddrTotUdpPorts": axFixedNatTop5PrivateIpAddrTotUdpPorts,
       "axFixedNatTop5PrivateIpAddrTotUdpPortTable": axFixedNatTop5PrivateIpAddrTotUdpPortTable,
       "axFixedNatTop5PrivateIpAddrTotUdpPortEntry": axFixedNatTop5PrivateIpAddrTotUdpPortEntry,
       "axFixedNatTop5PrivateIpAddrInUdpPort": axFixedNatTop5PrivateIpAddrInUdpPort,
       "axFixedNatTop5PrivateIpAddrTotNumInUdpPort": axFixedNatTop5PrivateIpAddrTotNumInUdpPort,
       "axFixedNatTop5PrivateIpAddrGlobalIpAddrInUdpPort": axFixedNatTop5PrivateIpAddrGlobalIpAddrInUdpPort,
       "axFixedNatTop5PrivateIpAddrTotIcmpPorts": axFixedNatTop5PrivateIpAddrTotIcmpPorts,
       "axFixedNatTop5PrivateIpAddrTotIcmpPortTable": axFixedNatTop5PrivateIpAddrTotIcmpPortTable,
       "axFixedNatTop5PrivateIpAddrTotIcmpPortEntry": axFixedNatTop5PrivateIpAddrTotIcmpPortEntry,
       "axFixedNatTop5PrivateIpAddrInIcmpPort": axFixedNatTop5PrivateIpAddrInIcmpPort,
       "axFixedNatTop5PrivateIpAddrTotNumInIcmpPort": axFixedNatTop5PrivateIpAddrTotNumInIcmpPort,
       "axFixedNatTop5PrivateIpAddrGlobalIpAddrInIcmpPort": axFixedNatTop5PrivateIpAddrGlobalIpAddrInIcmpPort,
       "axFixedNatTop5UserPrivateIpAddrTotSessions": axFixedNatTop5UserPrivateIpAddrTotSessions,
       "axFixedNatTop5UserPrivateIpAddrTotSessionTable": axFixedNatTop5UserPrivateIpAddrTotSessionTable,
       "axFixedNatTop5UserPrivateIpAddrTotSessionEntry": axFixedNatTop5UserPrivateIpAddrTotSessionEntry,
       "axFixedNatTop5UserPrivateIpAddr": axFixedNatTop5UserPrivateIpAddr,
       "axFixedNatTop5UserPrivateIpAddrTotNumSession": axFixedNatTop5UserPrivateIpAddrTotNumSession,
       "axFixedNatTop5UserPrivateIpAddrGlobalIpAddr": axFixedNatTop5UserPrivateIpAddrGlobalIpAddr,
       "axFixedNatTop5UserPrivateIpAddrTotTcpPorts": axFixedNatTop5UserPrivateIpAddrTotTcpPorts,
       "axFixedNatTop5UserPrivateIpAddrTotTcpPortTable": axFixedNatTop5UserPrivateIpAddrTotTcpPortTable,
       "axFixedNatTop5UserPrivateIpAddrTotTcpPortEntry": axFixedNatTop5UserPrivateIpAddrTotTcpPortEntry,
       "axFixedNatTop5UserPrivateIpAddrInTcp": axFixedNatTop5UserPrivateIpAddrInTcp,
       "axFixedNatTop5UserPrivateIpAddrTotNumInTcp": axFixedNatTop5UserPrivateIpAddrTotNumInTcp,
       "axFixedNatTop5UserPrivateIpAddrGlobalIpAddrInTcp": axFixedNatTop5UserPrivateIpAddrGlobalIpAddrInTcp,
       "axFixedNatTop5UserPrivateIpAddrTotUdpPorts": axFixedNatTop5UserPrivateIpAddrTotUdpPorts,
       "axFixedNatTop5UserPrivateIpAddrTotUdpPortTable": axFixedNatTop5UserPrivateIpAddrTotUdpPortTable,
       "axFixedNatTop5UserPrivateIpAddrTotUdpPortEntry": axFixedNatTop5UserPrivateIpAddrTotUdpPortEntry,
       "axFixedNatTop5UserPrivateIpAddrInUdp": axFixedNatTop5UserPrivateIpAddrInUdp,
       "axFixedNatTop5UserPrivateIpAddrTotNumInUdp": axFixedNatTop5UserPrivateIpAddrTotNumInUdp,
       "axFixedNatTop5UserPrivateIpAddrGlobalIpAddrInUdp": axFixedNatTop5UserPrivateIpAddrGlobalIpAddrInUdp,
       "axFixedNatTop5UserPrivateIpAddrTotIcmpPorts": axFixedNatTop5UserPrivateIpAddrTotIcmpPorts,
       "axFixedNatTop5UserPrivateIpAddrTotIcmpPortTable": axFixedNatTop5UserPrivateIpAddrTotIcmpPortTable,
       "axFixedNatTop5UserPrivateIpAddrTotIcmpPortEntry": axFixedNatTop5UserPrivateIpAddrTotIcmpPortEntry,
       "axFixedNatTop5UserPrivateIpAddrInIcmp": axFixedNatTop5UserPrivateIpAddrInIcmp,
       "axFixedNatTop5UserPrivateIpAddrTotNumInIcmp": axFixedNatTop5UserPrivateIpAddrTotNumInIcmp,
       "axFixedNatTop5UserPrivateIpAddrGlobalIpAddrInIcmp": axFixedNatTop5UserPrivateIpAddrGlobalIpAddrInIcmp,
       "axFixedNatTop5GlobalIpAddrTotUsers": axFixedNatTop5GlobalIpAddrTotUsers,
       "axFixedNatTop5GlobalIpAddrTotUserTable": axFixedNatTop5GlobalIpAddrTotUserTable,
       "axFixedNatTop5GlobalIpAddrTotUserEntry": axFixedNatTop5GlobalIpAddrTotUserEntry,
       "axFixedNatTop5GlobalIpAddrUser": axFixedNatTop5GlobalIpAddrUser,
       "axFixedNatTop5GlobalIpAddrTotNum": axFixedNatTop5GlobalIpAddrTotNum,
       "axFixedNatTop5GlobalIpAddrTotTcpPorts": axFixedNatTop5GlobalIpAddrTotTcpPorts,
       "axFixedNatTop5GlobalIpAddrTotTcpPortTable": axFixedNatTop5GlobalIpAddrTotTcpPortTable,
       "axFixedNatTop5GlobalIpAddrTotTcpPortEntry": axFixedNatTop5GlobalIpAddrTotTcpPortEntry,
       "axFixedNatTop5GlobalIpAddrInTcp": axFixedNatTop5GlobalIpAddrInTcp,
       "axFixedNatTop5GlobalIpAddrTotNumInTcp": axFixedNatTop5GlobalIpAddrTotNumInTcp,
       "axFixedNatTop5GlobalIpAddrTotUdpPorts": axFixedNatTop5GlobalIpAddrTotUdpPorts,
       "axFixedNatTop5GlobalIpAddrTotUdpPortTable": axFixedNatTop5GlobalIpAddrTotUdpPortTable,
       "axFixedNatTop5GlobalIpAddrTotUdpPortEntry": axFixedNatTop5GlobalIpAddrTotUdpPortEntry,
       "axFixedNatTop5GlobalIpAddrInUdp": axFixedNatTop5GlobalIpAddrInUdp,
       "axFixedNatTop5GlobalIpAddrTotNumInUdp": axFixedNatTop5GlobalIpAddrTotNumInUdp,
       "axFixedNatFile": axFixedNatFile,
       "axFixedNatFileTable": axFixedNatFileTable,
       "axFixedNatFileEntry": axFixedNatFileEntry,
       "axFixedNatFileName": axFixedNatFileName,
       "axFixedNatFileTimeStamp": axFixedNatFileTimeStamp,
       "axFragmentStats": axFragmentStats,
       "axIpv4FragmentStats": axIpv4FragmentStats,
       "axIpv4SessionInsert": axIpv4SessionInsert,
       "axIpv4SessionExpired": axIpv4SessionExpired,
       "axIpv4IcmpReceived": axIpv4IcmpReceived,
       "axIpv4Icmpv6Received": axIpv4Icmpv6Received,
       "axIpv4UdpReceived": axIpv4UdpReceived,
       "axIpv4TcpReceived": axIpv4TcpReceived,
       "axIpv4IpInIpReceived": axIpv4IpInIpReceived,
       "axIpv4Ipv6InIpReceived": axIpv4Ipv6InIpReceived,
       "axIpv4OtherReceived": axIpv4OtherReceived,
       "axIpv4IcmpDropped": axIpv4IcmpDropped,
       "axIpv4Icmpv6Dropped": axIpv4Icmpv6Dropped,
       "axIpv4UdpDropped": axIpv4UdpDropped,
       "axIpv4TcpDropped": axIpv4TcpDropped,
       "axIpv4IpInIpDropped": axIpv4IpInIpDropped,
       "axIpv4Ipv6InIpDropped": axIpv4Ipv6InIpDropped,
       "axIpv4OtherDropped": axIpv4OtherDropped,
       "axIpv4OverlappingFragmentDropped": axIpv4OverlappingFragmentDropped,
       "axIpv4BadIpLength": axIpv4BadIpLength,
       "axIpv4FragmentTooSmallDrop": axIpv4FragmentTooSmallDrop,
       "axIpv4FirstTcpFragmentTooSmallDrop": axIpv4FirstTcpFragmentTooSmallDrop,
       "axIpv4FirstL4FragmentTooSmallDrop": axIpv4FirstL4FragmentTooSmallDrop,
       "axIpv4TotalSessionsExceedDrop": axIpv4TotalSessionsExceedDrop,
       "axIpv4OutOfSessionMemory": axIpv4OutOfSessionMemory,
       "axIpv4FragmentationFastAgingSet": axIpv4FragmentationFastAgingSet,
       "axIpv4FragmentationFastAgingUnset": axIpv4FragmentationFastAgingUnset,
       "axIpv4FragmentQueueSuccess": axIpv4FragmentQueueSuccess,
       "axIpv4PayloadLengthUnaligned": axIpv4PayloadLengthUnaligned,
       "axIpv4PayloadLengthOutOfBounds": axIpv4PayloadLengthOutOfBounds,
       "axIpv4DuplicateFirstFragment": axIpv4DuplicateFirstFragment,
       "axIpv4DuplicateLastFragment": axIpv4DuplicateLastFragment,
       "axIpv4TotalQueuedFragmentsExceed": axIpv4TotalQueuedFragmentsExceed,
       "axIpv4FragmentQueueFailure": axIpv4FragmentQueueFailure,
       "axIpv4FragmentReassemblySuccess": axIpv4FragmentReassemblySuccess,
       "axIpv4FragmentMaxDataLengthExceed": axIpv4FragmentMaxDataLengthExceed,
       "axIpv4FragmentReassemblyFailure": axIpv4FragmentReassemblyFailure,
       "axIpv4MtuExceedPolicyDrop": axIpv4MtuExceedPolicyDrop,
       "axIpv4FragmentProcessingDrop": axIpv4FragmentProcessingDrop,
       "axIpv4TooManyPacketsPerReassemblyDrop": axIpv4TooManyPacketsPerReassemblyDrop,
       "axIpv4SessionMaxPacketsExceed": axIpv4SessionMaxPacketsExceed,
       "axIpv4HighCpuThresholdReached": axIpv4HighCpuThresholdReached,
       "axIpv4LowCpuThresholdReached": axIpv4LowCpuThresholdReached,
       "axIpv4HighCpuDrop": axIpv4HighCpuDrop,
       "axIpv4DDoSProtectionDrop": axIpv4DDoSProtectionDrop,
       "axIpv6FragmentStats": axIpv6FragmentStats,
       "axIpv6SessionInsert": axIpv6SessionInsert,
       "axIpv6SessionExpired": axIpv6SessionExpired,
       "axIpv6IcmpReceived": axIpv6IcmpReceived,
       "axIpv6Icmpv6Received": axIpv6Icmpv6Received,
       "axIpv6UdpReceived": axIpv6UdpReceived,
       "axIpv6TcpReceived": axIpv6TcpReceived,
       "axIpv6IpInIpReceived": axIpv6IpInIpReceived,
       "axIpv6Ipv6InIpReceived": axIpv6Ipv6InIpReceived,
       "axIpv6OtherReceived": axIpv6OtherReceived,
       "axIpv6IcmpDropped": axIpv6IcmpDropped,
       "axIpv6Icmpv6Dropped": axIpv6Icmpv6Dropped,
       "axIpv6UdpDropped": axIpv6UdpDropped,
       "axIpv6TcpDropped": axIpv6TcpDropped,
       "axIpv6IpInIpDropped": axIpv6IpInIpDropped,
       "axIpv6Ipv6InIpDropped": axIpv6Ipv6InIpDropped,
       "axIpv6OtherDropped": axIpv6OtherDropped,
       "axIpv6OverlappingFragmentDropped": axIpv6OverlappingFragmentDropped,
       "axIpv6BadIpLength": axIpv6BadIpLength,
       "axIpv6FragmentTooSmallDrop": axIpv6FragmentTooSmallDrop,
       "axIpv6FirstTcpFragmentTooSmallDrop": axIpv6FirstTcpFragmentTooSmallDrop,
       "axIpv6FirstL4FragmentTooSmallDrop": axIpv6FirstL4FragmentTooSmallDrop,
       "axIpv6TotalSessionsExceedDrop": axIpv6TotalSessionsExceedDrop,
       "axIpv6OutOfSessionMemory": axIpv6OutOfSessionMemory,
       "axIpv6FragmentationFastAgingSet": axIpv6FragmentationFastAgingSet,
       "axIpv6FragmentationFastAgingUnset": axIpv6FragmentationFastAgingUnset,
       "axIpv6FragmentQueueSuccess": axIpv6FragmentQueueSuccess,
       "axIpv6PayloadLengthUnaligned": axIpv6PayloadLengthUnaligned,
       "axIpv6PayloadLengthOutOfBounds": axIpv6PayloadLengthOutOfBounds,
       "axIpv6DuplicateFirstFragment": axIpv6DuplicateFirstFragment,
       "axIpv6DuplicateLastFragment": axIpv6DuplicateLastFragment,
       "axIpv6TotalQueuedFragmentsExceed": axIpv6TotalQueuedFragmentsExceed,
       "axIpv6FragmentQueueFailure": axIpv6FragmentQueueFailure,
       "axIpv6FragmentReassemblySuccess": axIpv6FragmentReassemblySuccess,
       "axIpv6FragmentMaxDataLengthExceed": axIpv6FragmentMaxDataLengthExceed,
       "axIpv6FragmentReassemblyFailure": axIpv6FragmentReassemblyFailure,
       "axIpv6MtuExceedPolicyDrop": axIpv6MtuExceedPolicyDrop,
       "axIpv6FragmentProcessingDrop": axIpv6FragmentProcessingDrop,
       "axIpv6TooManyPacketsPerReassemblyDrop": axIpv6TooManyPacketsPerReassemblyDrop,
       "axIpv6SessionMaxPacketsExceed": axIpv6SessionMaxPacketsExceed,
       "axIpv4InIpv6FragmentStats": axIpv4InIpv6FragmentStats,
       "axIpv4InIpv6SessionInsert": axIpv4InIpv6SessionInsert,
       "axIpv4InIpv6SessionExpired": axIpv4InIpv6SessionExpired,
       "axIpv4InIpv6IcmpReceived": axIpv4InIpv6IcmpReceived,
       "axIpv4InIpv6Icmpv6Received": axIpv4InIpv6Icmpv6Received,
       "axIpv4InIpv6UdpReceived": axIpv4InIpv6UdpReceived,
       "axIpv4InIpv6TcpReceived": axIpv4InIpv6TcpReceived,
       "axIpv4InIpv6IpInIpReceived": axIpv4InIpv6IpInIpReceived,
       "axIpv4InIpv6Ipv6InIpReceived": axIpv4InIpv6Ipv6InIpReceived,
       "axIpv4InIpv6OtherReceived": axIpv4InIpv6OtherReceived,
       "axIpv4InIpv6IcmpDropped": axIpv4InIpv6IcmpDropped,
       "axIpv4InIpv6Icmpv6Dropped": axIpv4InIpv6Icmpv6Dropped,
       "axIpv4InIpv6UdpDropped": axIpv4InIpv6UdpDropped,
       "axIpv4InIpv6TcpDropped": axIpv4InIpv6TcpDropped,
       "axIpv4InIpv6IpInIpDropped": axIpv4InIpv6IpInIpDropped,
       "axIpv4InIpv6Ipv6InIpDropped": axIpv4InIpv6Ipv6InIpDropped,
       "axIpv4InIpv6OtherDropped": axIpv4InIpv6OtherDropped,
       "axIpv4InIpv6OverlappingFragmentDropped": axIpv4InIpv6OverlappingFragmentDropped,
       "axIpv4InIpv6BadIpLength": axIpv4InIpv6BadIpLength,
       "axIpv4InIpv6FragmentTooSmallDrop": axIpv4InIpv6FragmentTooSmallDrop,
       "axIpv4InIpv6FirstTcpFragmentTooSmallDrop": axIpv4InIpv6FirstTcpFragmentTooSmallDrop,
       "axIpv4InIpv6FirstL4FragmentTooSmallDrop": axIpv4InIpv6FirstL4FragmentTooSmallDrop,
       "axIpv4InIpv6TotalSessionsExceedDrop": axIpv4InIpv6TotalSessionsExceedDrop,
       "axIpv4InIpv6OutOfSessionMemory": axIpv4InIpv6OutOfSessionMemory,
       "axIpv4InIpv6FragmentationFastAgingSet": axIpv4InIpv6FragmentationFastAgingSet,
       "axIpv4InIpv6FragmentationFastAgingUnset": axIpv4InIpv6FragmentationFastAgingUnset,
       "axIpv4InIpv6FragmentQueueSuccess": axIpv4InIpv6FragmentQueueSuccess,
       "axIpv4InIpv6PayloadLengthUnaligned": axIpv4InIpv6PayloadLengthUnaligned,
       "axIpv4InIpv6PayloadLengthOutOfBounds": axIpv4InIpv6PayloadLengthOutOfBounds,
       "axIpv4InIpv6DuplicateFirstFragment": axIpv4InIpv6DuplicateFirstFragment,
       "axIpv4InIpv6DuplicateLastFragment": axIpv4InIpv6DuplicateLastFragment,
       "axIpv4InIpv6TotalQueuedFragmentsExceed": axIpv4InIpv6TotalQueuedFragmentsExceed,
       "axIpv4InIpv6FragmentQueueFailure": axIpv4InIpv6FragmentQueueFailure,
       "axIpv4InIpv6FragmentReassemblySuccess": axIpv4InIpv6FragmentReassemblySuccess,
       "axIpv4InIpv6FragmentMaxDataLengthExceed": axIpv4InIpv6FragmentMaxDataLengthExceed,
       "axIpv4InIpv6FragmentReassemblyFailure": axIpv4InIpv6FragmentReassemblyFailure,
       "axIpv4InIpv6MtuExceedPolicyDrop": axIpv4InIpv6MtuExceedPolicyDrop,
       "axIpv4InIpv6FragmentProcessingDrop": axIpv4InIpv6FragmentProcessingDrop,
       "axIpv4InIpv6TooManyPacketsPerReassemblyDrop": axIpv4InIpv6TooManyPacketsPerReassemblyDrop,
       "axIpv4InIpv6SessionMaxPacketsExceed": axIpv4InIpv6SessionMaxPacketsExceed,
       "axIpv6InIpv4FragmentStats": axIpv6InIpv4FragmentStats,
       "axIpv6InIpv4SessionInsert": axIpv6InIpv4SessionInsert,
       "axIpv6InIpv4SessionExpired": axIpv6InIpv4SessionExpired,
       "axIpv6InIpv4IcmpReceived": axIpv6InIpv4IcmpReceived,
       "axIpv6InIpv4Icmpv6Received": axIpv6InIpv4Icmpv6Received,
       "axIpv6InIpv4UdpReceived": axIpv6InIpv4UdpReceived,
       "axIpv6InIpv4TcpReceived": axIpv6InIpv4TcpReceived,
       "axIpv6InIpv4IpInIpReceived": axIpv6InIpv4IpInIpReceived,
       "axIpv6InIpv4Ipv6InIpReceived": axIpv6InIpv4Ipv6InIpReceived,
       "axIpv6InIpv4OtherReceived": axIpv6InIpv4OtherReceived,
       "axIpv6InIpv4IcmpDropped": axIpv6InIpv4IcmpDropped,
       "axIpv6InIpv4Icmpv6Dropped": axIpv6InIpv4Icmpv6Dropped,
       "axIpv6InIpv4UdpDropped": axIpv6InIpv4UdpDropped,
       "axIpv6InIpv4TcpDropped": axIpv6InIpv4TcpDropped,
       "axIpv6InIpv4IpInIpDropped": axIpv6InIpv4IpInIpDropped,
       "axIpv6InIpv4Ipv6InIpDropped": axIpv6InIpv4Ipv6InIpDropped,
       "axIpv6InIpv4OtherDropped": axIpv6InIpv4OtherDropped,
       "axIpv6InIpv4OverlappingFragmentDropped": axIpv6InIpv4OverlappingFragmentDropped,
       "axIpv6InIpv4BadIpLength": axIpv6InIpv4BadIpLength,
       "axIpv6InIpv4FragmentTooSmallDrop": axIpv6InIpv4FragmentTooSmallDrop,
       "axIpv6InIpv4FirstTcpFragmentTooSmallDrop": axIpv6InIpv4FirstTcpFragmentTooSmallDrop,
       "axIpv6InIpv4FirstL4FragmentTooSmallDrop": axIpv6InIpv4FirstL4FragmentTooSmallDrop,
       "axIpv6InIpv4TotalSessionsExceedDrop": axIpv6InIpv4TotalSessionsExceedDrop,
       "axIpv6InIpv4OutOfSessionMemory": axIpv6InIpv4OutOfSessionMemory,
       "axIpv6InIpv4FragmentationFastAgingSet": axIpv6InIpv4FragmentationFastAgingSet,
       "axIpv6InIpv4FragmentationFastAgingUnset": axIpv6InIpv4FragmentationFastAgingUnset,
       "axIpv6InIpv4FragmentQueueSuccess": axIpv6InIpv4FragmentQueueSuccess,
       "axIpv6InIpv4PayloadLengthUnaligned": axIpv6InIpv4PayloadLengthUnaligned,
       "axIpv6InIpv4PayloadLengthOutOfBounds": axIpv6InIpv4PayloadLengthOutOfBounds,
       "axIpv6InIpv4DuplicateFirstFragment": axIpv6InIpv4DuplicateFirstFragment,
       "axIpv6InIpv4DuplicateLastFragment": axIpv6InIpv4DuplicateLastFragment,
       "axIpv6InIpv4TotalQueuedFragmentsExceed": axIpv6InIpv4TotalQueuedFragmentsExceed,
       "axIpv6InIpv4FragmentQueueFailure": axIpv6InIpv4FragmentQueueFailure,
       "axIpv6InIpv4FragmentReassemblySuccess": axIpv6InIpv4FragmentReassemblySuccess,
       "axIpv6InIpv4FragmentMaxDataLengthExceed": axIpv6InIpv4FragmentMaxDataLengthExceed,
       "axIpv6InIpv4FragmentReassemblyFailure": axIpv6InIpv4FragmentReassemblyFailure,
       "axIpv6InIpv4MtuExceedPolicyDrop": axIpv6InIpv4MtuExceedPolicyDrop,
       "axIpv6InIpv4FragmentProcessingDrop": axIpv6InIpv4FragmentProcessingDrop,
       "axIpv6InIpv4TooManyPacketsPerReassemblyDrop": axIpv6InIpv4TooManyPacketsPerReassemblyDrop,
       "axIpv6InIpv4SessionMaxPacketsExceed": axIpv6InIpv4SessionMaxPacketsExceed,
       "axDDosStats": axDDosStats,
       "axDDosStatsL3EntryAdded": axDDosStatsL3EntryAdded,
       "axDDosStatsL3EntryDeleted": axDDosStatsL3EntryDeleted,
       "axDDosStatsL3EntryAddedToBGP": axDDosStatsL3EntryAddedToBGP,
       "axDDosStatsL3EntryRemovedFromBGP": axDDosStatsL3EntryRemovedFromBGP,
       "axDDosStatsL3EntryAddedToHW": axDDosStatsL3EntryAddedToHW,
       "axDDosStatsL3EntryRemovedFromHW": axDDosStatsL3EntryRemovedFromHW,
       "axDDosStatsTooManyL3Entries": axDDosStatsTooManyL3Entries,
       "axDDosStatsL3EntryMatchDrop": axDDosStatsL3EntryMatchDrop,
       "axDDosStatsHWL3EntryMatchDrop": axDDosStatsHWL3EntryMatchDrop,
       "axDDosStatsL4EntryAdded": axDDosStatsL4EntryAdded,
       "axDDosStatsL4EntryDeleted": axDDosStatsL4EntryDeleted,
       "axDDosStatsL4EntryAddedToHW": axDDosStatsL4EntryAddedToHW,
       "axDDosStatsL4EntryRemovedFromHW": axDDosStatsL4EntryRemovedFromHW,
       "axDDosStatsHWOutOfL4Entries": axDDosStatsHWOutOfL4Entries,
       "axDDosStatsL4EntryMatchDrop": axDDosStatsL4EntryMatchDrop,
       "axDDosStatsHWL4EntryMatchDrop": axDDosStatsHWL4EntryMatchDrop}
)
