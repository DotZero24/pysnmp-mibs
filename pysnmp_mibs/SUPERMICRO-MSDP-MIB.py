# SNMP MIB module (SUPERMICRO-MSDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-MSDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:01:53 2025
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

fsMsdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61)
)
if mibBuilder.loadTexts:
    fsMsdpMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMsdp_ObjectIdentity = ObjectIdentity
fsMsdp = _FsMsdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1)
)
_FsMsdpTraps_ObjectIdentity = ObjectIdentity
fsMsdpTraps = _FsMsdpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 0)
)


class _FsMsdpTraceLevel_Type(Integer32):
    """Custom type fsMsdpTraceLevel based on Integer32"""
    defaultValue = 0


_FsMsdpTraceLevel_Type.__name__ = "Integer32"
_FsMsdpTraceLevel_Object = MibScalar
fsMsdpTraceLevel = _FsMsdpTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 1),
    _FsMsdpTraceLevel_Type()
)
fsMsdpTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMsdpTraceLevel.setStatus("current")


class _FsMsdpIPv4AdminStat_Type(Integer32):
    """Custom type fsMsdpIPv4AdminStat based on Integer32"""
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


_FsMsdpIPv4AdminStat_Type.__name__ = "Integer32"
_FsMsdpIPv4AdminStat_Object = MibScalar
fsMsdpIPv4AdminStat = _FsMsdpIPv4AdminStat_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 2),
    _FsMsdpIPv4AdminStat_Type()
)
fsMsdpIPv4AdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMsdpIPv4AdminStat.setStatus("current")


class _FsMsdpIPv6AdminStat_Type(Integer32):
    """Custom type fsMsdpIPv6AdminStat based on Integer32"""
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


_FsMsdpIPv6AdminStat_Type.__name__ = "Integer32"
_FsMsdpIPv6AdminStat_Object = MibScalar
fsMsdpIPv6AdminStat = _FsMsdpIPv6AdminStat_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 3),
    _FsMsdpIPv6AdminStat_Type()
)
fsMsdpIPv6AdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMsdpIPv6AdminStat.setStatus("current")


class _FsMsdpCacheLifetime_Type(TimeTicks):
    """Custom type fsMsdpCacheLifetime based on TimeTicks"""
    defaultValue = 0


_FsMsdpCacheLifetime_Type.__name__ = "TimeTicks"
_FsMsdpCacheLifetime_Object = MibScalar
fsMsdpCacheLifetime = _FsMsdpCacheLifetime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 4),
    _FsMsdpCacheLifetime_Type()
)
fsMsdpCacheLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMsdpCacheLifetime.setStatus("current")
_FsMsdpNumSACacheEntries_Type = Gauge32
_FsMsdpNumSACacheEntries_Object = MibScalar
fsMsdpNumSACacheEntries = _FsMsdpNumSACacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 5),
    _FsMsdpNumSACacheEntries_Type()
)
fsMsdpNumSACacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpNumSACacheEntries.setStatus("current")


class _FsMsdpMaxPeerSessions_Type(Integer32):
    """Custom type fsMsdpMaxPeerSessions based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsMsdpMaxPeerSessions_Type.__name__ = "Integer32"
_FsMsdpMaxPeerSessions_Object = MibScalar
fsMsdpMaxPeerSessions = _FsMsdpMaxPeerSessions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 6),
    _FsMsdpMaxPeerSessions_Type()
)
fsMsdpMaxPeerSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMsdpMaxPeerSessions.setStatus("current")


class _FsMsdpMappingComponentId_Type(Integer32):
    """Custom type fsMsdpMappingComponentId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsMsdpMappingComponentId_Type.__name__ = "Integer32"
_FsMsdpMappingComponentId_Object = MibScalar
fsMsdpMappingComponentId = _FsMsdpMappingComponentId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 7),
    _FsMsdpMappingComponentId_Type()
)
fsMsdpMappingComponentId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMsdpMappingComponentId.setStatus("current")


class _FsMsdpListenerPort_Type(Integer32):
    """Custom type fsMsdpListenerPort based on Integer32"""
    defaultValue = 639

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(639, 639),
        ValueRangeConstraint(1024, 65535),
    )


_FsMsdpListenerPort_Type.__name__ = "Integer32"
_FsMsdpListenerPort_Object = MibScalar
fsMsdpListenerPort = _FsMsdpListenerPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 8),
    _FsMsdpListenerPort_Type()
)
fsMsdpListenerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMsdpListenerPort.setStatus("current")


class _FsMsdpPeerFilter_Type(Integer32):
    """Custom type fsMsdpPeerFilter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("denyall", 0),
          ("acceptall", 1))
    )


_FsMsdpPeerFilter_Type.__name__ = "Integer32"
_FsMsdpPeerFilter_Object = MibScalar
fsMsdpPeerFilter = _FsMsdpPeerFilter_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 9),
    _FsMsdpPeerFilter_Type()
)
fsMsdpPeerFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMsdpPeerFilter.setStatus("current")
_FsMsdpPeerCount_Type = Integer32
_FsMsdpPeerCount_Object = MibScalar
fsMsdpPeerCount = _FsMsdpPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 10),
    _FsMsdpPeerCount_Type()
)
fsMsdpPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerCount.setStatus("current")
_FsMsdpPeerTable_Object = MibTable
fsMsdpPeerTable = _FsMsdpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11)
)
if mibBuilder.loadTexts:
    fsMsdpPeerTable.setStatus("current")
_FsMsdpPeerEntry_Object = MibTableRow
fsMsdpPeerEntry = _FsMsdpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1)
)
fsMsdpPeerEntry.setIndexNames(
    (0, "SUPERMICRO-MSDP-MIB", "fsMsdpPeerAddrType"),
    (0, "SUPERMICRO-MSDP-MIB", "fsMsdpPeerRemoteAddress"),
)
if mibBuilder.loadTexts:
    fsMsdpPeerEntry.setStatus("current")
_FsMsdpPeerAddrType_Type = InetAddressType
_FsMsdpPeerAddrType_Object = MibTableColumn
fsMsdpPeerAddrType = _FsMsdpPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 1),
    _FsMsdpPeerAddrType_Type()
)
fsMsdpPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMsdpPeerAddrType.setStatus("current")


class _FsMsdpPeerRemoteAddress_Type(InetAddress):
    """Custom type fsMsdpPeerRemoteAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMsdpPeerRemoteAddress_Type.__name__ = "InetAddress"
_FsMsdpPeerRemoteAddress_Object = MibTableColumn
fsMsdpPeerRemoteAddress = _FsMsdpPeerRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 2),
    _FsMsdpPeerRemoteAddress_Type()
)
fsMsdpPeerRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMsdpPeerRemoteAddress.setStatus("current")


class _FsMsdpPeerState_Type(Integer32):
    """Custom type fsMsdpPeerState based on Integer32"""
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
        *(("inactive", 1),
          ("listen", 2),
          ("connecting", 3),
          ("established", 4),
          ("disabled", 5))
    )


_FsMsdpPeerState_Type.__name__ = "Integer32"
_FsMsdpPeerState_Object = MibTableColumn
fsMsdpPeerState = _FsMsdpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 3),
    _FsMsdpPeerState_Type()
)
fsMsdpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerState.setStatus("current")
_FsMsdpPeerRPFFailures_Type = Counter32
_FsMsdpPeerRPFFailures_Object = MibTableColumn
fsMsdpPeerRPFFailures = _FsMsdpPeerRPFFailures_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 4),
    _FsMsdpPeerRPFFailures_Type()
)
fsMsdpPeerRPFFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerRPFFailures.setStatus("current")
_FsMsdpPeerInSAs_Type = Counter32
_FsMsdpPeerInSAs_Object = MibTableColumn
fsMsdpPeerInSAs = _FsMsdpPeerInSAs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 5),
    _FsMsdpPeerInSAs_Type()
)
fsMsdpPeerInSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerInSAs.setStatus("current")
_FsMsdpPeerOutSAs_Type = Counter32
_FsMsdpPeerOutSAs_Object = MibTableColumn
fsMsdpPeerOutSAs = _FsMsdpPeerOutSAs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 6),
    _FsMsdpPeerOutSAs_Type()
)
fsMsdpPeerOutSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerOutSAs.setStatus("current")
_FsMsdpPeerInSARequests_Type = Counter32
_FsMsdpPeerInSARequests_Object = MibTableColumn
fsMsdpPeerInSARequests = _FsMsdpPeerInSARequests_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 7),
    _FsMsdpPeerInSARequests_Type()
)
fsMsdpPeerInSARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerInSARequests.setStatus("current")
_FsMsdpPeerOutSARequests_Type = Counter32
_FsMsdpPeerOutSARequests_Object = MibTableColumn
fsMsdpPeerOutSARequests = _FsMsdpPeerOutSARequests_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 8),
    _FsMsdpPeerOutSARequests_Type()
)
fsMsdpPeerOutSARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerOutSARequests.setStatus("current")
_FsMsdpPeerInControlMessages_Type = Counter32
_FsMsdpPeerInControlMessages_Object = MibTableColumn
fsMsdpPeerInControlMessages = _FsMsdpPeerInControlMessages_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 9),
    _FsMsdpPeerInControlMessages_Type()
)
fsMsdpPeerInControlMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerInControlMessages.setStatus("current")
_FsMsdpPeerOutControlMessages_Type = Counter32
_FsMsdpPeerOutControlMessages_Object = MibTableColumn
fsMsdpPeerOutControlMessages = _FsMsdpPeerOutControlMessages_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 10),
    _FsMsdpPeerOutControlMessages_Type()
)
fsMsdpPeerOutControlMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerOutControlMessages.setStatus("current")
_FsMsdpPeerInDataPackets_Type = Counter32
_FsMsdpPeerInDataPackets_Object = MibTableColumn
fsMsdpPeerInDataPackets = _FsMsdpPeerInDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 11),
    _FsMsdpPeerInDataPackets_Type()
)
fsMsdpPeerInDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerInDataPackets.setStatus("current")
_FsMsdpPeerOutDataPackets_Type = Counter32
_FsMsdpPeerOutDataPackets_Object = MibTableColumn
fsMsdpPeerOutDataPackets = _FsMsdpPeerOutDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 12),
    _FsMsdpPeerOutDataPackets_Type()
)
fsMsdpPeerOutDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerOutDataPackets.setStatus("current")
_FsMsdpPeerFsmEstablishedTransitions_Type = Counter32
_FsMsdpPeerFsmEstablishedTransitions_Object = MibTableColumn
fsMsdpPeerFsmEstablishedTransitions = _FsMsdpPeerFsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 13),
    _FsMsdpPeerFsmEstablishedTransitions_Type()
)
fsMsdpPeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerFsmEstablishedTransitions.setStatus("current")
_FsMsdpPeerFsmEstablishedTime_Type = TimeStamp
_FsMsdpPeerFsmEstablishedTime_Object = MibTableColumn
fsMsdpPeerFsmEstablishedTime = _FsMsdpPeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 14),
    _FsMsdpPeerFsmEstablishedTime_Type()
)
fsMsdpPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerFsmEstablishedTime.setStatus("current")
_FsMsdpPeerInMessageTime_Type = TimeStamp
_FsMsdpPeerInMessageTime_Object = MibTableColumn
fsMsdpPeerInMessageTime = _FsMsdpPeerInMessageTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 15),
    _FsMsdpPeerInMessageTime_Type()
)
fsMsdpPeerInMessageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerInMessageTime.setStatus("current")


class _FsMsdpPeerLocalAddress_Type(InetAddress):
    """Custom type fsMsdpPeerLocalAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMsdpPeerLocalAddress_Type.__name__ = "InetAddress"
_FsMsdpPeerLocalAddress_Object = MibTableColumn
fsMsdpPeerLocalAddress = _FsMsdpPeerLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 16),
    _FsMsdpPeerLocalAddress_Type()
)
fsMsdpPeerLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMsdpPeerLocalAddress.setStatus("current")


class _FsMsdpPeerConnectRetryInterval_Type(Integer32):
    """Custom type fsMsdpPeerConnectRetryInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMsdpPeerConnectRetryInterval_Type.__name__ = "Integer32"
_FsMsdpPeerConnectRetryInterval_Object = MibTableColumn
fsMsdpPeerConnectRetryInterval = _FsMsdpPeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 17),
    _FsMsdpPeerConnectRetryInterval_Type()
)
fsMsdpPeerConnectRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMsdpPeerConnectRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsMsdpPeerConnectRetryInterval.setUnits("seconds")


class _FsMsdpPeerHoldTimeConfigured_Type(Integer32):
    """Custom type fsMsdpPeerHoldTimeConfigured based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_FsMsdpPeerHoldTimeConfigured_Type.__name__ = "Integer32"
_FsMsdpPeerHoldTimeConfigured_Object = MibTableColumn
fsMsdpPeerHoldTimeConfigured = _FsMsdpPeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 18),
    _FsMsdpPeerHoldTimeConfigured_Type()
)
fsMsdpPeerHoldTimeConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMsdpPeerHoldTimeConfigured.setStatus("current")
if mibBuilder.loadTexts:
    fsMsdpPeerHoldTimeConfigured.setUnits("seconds")


class _FsMsdpPeerKeepAliveConfigured_Type(Integer32):
    """Custom type fsMsdpPeerKeepAliveConfigured based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_FsMsdpPeerKeepAliveConfigured_Type.__name__ = "Integer32"
_FsMsdpPeerKeepAliveConfigured_Object = MibTableColumn
fsMsdpPeerKeepAliveConfigured = _FsMsdpPeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 19),
    _FsMsdpPeerKeepAliveConfigured_Type()
)
fsMsdpPeerKeepAliveConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMsdpPeerKeepAliveConfigured.setStatus("current")
if mibBuilder.loadTexts:
    fsMsdpPeerKeepAliveConfigured.setUnits("seconds")


class _FsMsdpPeerDataTtl_Type(Integer32):
    """Custom type fsMsdpPeerDataTtl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMsdpPeerDataTtl_Type.__name__ = "Integer32"
_FsMsdpPeerDataTtl_Object = MibTableColumn
fsMsdpPeerDataTtl = _FsMsdpPeerDataTtl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 20),
    _FsMsdpPeerDataTtl_Type()
)
fsMsdpPeerDataTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMsdpPeerDataTtl.setStatus("current")
_FsMsdpPeerStatus_Type = RowStatus
_FsMsdpPeerStatus_Object = MibTableColumn
fsMsdpPeerStatus = _FsMsdpPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 21),
    _FsMsdpPeerStatus_Type()
)
fsMsdpPeerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMsdpPeerStatus.setStatus("current")


class _FsMsdpPeerRemotePort_Type(Integer32):
    """Custom type fsMsdpPeerRemotePort based on Integer32"""
    defaultValue = 639

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMsdpPeerRemotePort_Type.__name__ = "Integer32"
_FsMsdpPeerRemotePort_Object = MibTableColumn
fsMsdpPeerRemotePort = _FsMsdpPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 22),
    _FsMsdpPeerRemotePort_Type()
)
fsMsdpPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerRemotePort.setStatus("current")


class _FsMsdpPeerLocalPort_Type(Integer32):
    """Custom type fsMsdpPeerLocalPort based on Integer32"""
    defaultValue = 639

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMsdpPeerLocalPort_Type.__name__ = "Integer32"
_FsMsdpPeerLocalPort_Object = MibTableColumn
fsMsdpPeerLocalPort = _FsMsdpPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 23),
    _FsMsdpPeerLocalPort_Type()
)
fsMsdpPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerLocalPort.setStatus("current")


class _FsMsdpPeerEncapsulationType_Type(Integer32):
    """Custom type fsMsdpPeerEncapsulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tcp", 1))
    )


_FsMsdpPeerEncapsulationType_Type.__name__ = "Integer32"
_FsMsdpPeerEncapsulationType_Object = MibTableColumn
fsMsdpPeerEncapsulationType = _FsMsdpPeerEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 24),
    _FsMsdpPeerEncapsulationType_Type()
)
fsMsdpPeerEncapsulationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMsdpPeerEncapsulationType.setStatus("current")
_FsMsdpPeerConnectionAttempts_Type = Counter32
_FsMsdpPeerConnectionAttempts_Object = MibTableColumn
fsMsdpPeerConnectionAttempts = _FsMsdpPeerConnectionAttempts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 25),
    _FsMsdpPeerConnectionAttempts_Type()
)
fsMsdpPeerConnectionAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerConnectionAttempts.setStatus("current")
_FsMsdpPeerDiscontinuityTime_Type = TimeStamp
_FsMsdpPeerDiscontinuityTime_Object = MibTableColumn
fsMsdpPeerDiscontinuityTime = _FsMsdpPeerDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 26),
    _FsMsdpPeerDiscontinuityTime_Type()
)
fsMsdpPeerDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerDiscontinuityTime.setStatus("current")


class _FsMsdpPeerMD5AuthPassword_Type(DisplayString):
    """Custom type fsMsdpPeerMD5AuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_FsMsdpPeerMD5AuthPassword_Type.__name__ = "DisplayString"
_FsMsdpPeerMD5AuthPassword_Object = MibTableColumn
fsMsdpPeerMD5AuthPassword = _FsMsdpPeerMD5AuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 27),
    _FsMsdpPeerMD5AuthPassword_Type()
)
fsMsdpPeerMD5AuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMsdpPeerMD5AuthPassword.setStatus("current")


class _FsMsdpPeerMD5AuthPwdStat_Type(Integer32):
    """Custom type fsMsdpPeerMD5AuthPwdStat based on Integer32"""
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


_FsMsdpPeerMD5AuthPwdStat_Type.__name__ = "Integer32"
_FsMsdpPeerMD5AuthPwdStat_Object = MibTableColumn
fsMsdpPeerMD5AuthPwdStat = _FsMsdpPeerMD5AuthPwdStat_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 28),
    _FsMsdpPeerMD5AuthPwdStat_Type()
)
fsMsdpPeerMD5AuthPwdStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMsdpPeerMD5AuthPwdStat.setStatus("current")
_FsMsdpPeerMD5FailCount_Type = Integer32
_FsMsdpPeerMD5FailCount_Object = MibTableColumn
fsMsdpPeerMD5FailCount = _FsMsdpPeerMD5FailCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 29),
    _FsMsdpPeerMD5FailCount_Type()
)
fsMsdpPeerMD5FailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerMD5FailCount.setStatus("current")
_FsMsdpPeerMD5SuccessCount_Type = Integer32
_FsMsdpPeerMD5SuccessCount_Object = MibTableColumn
fsMsdpPeerMD5SuccessCount = _FsMsdpPeerMD5SuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 30),
    _FsMsdpPeerMD5SuccessCount_Type()
)
fsMsdpPeerMD5SuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerMD5SuccessCount.setStatus("current")
_FsMsdpPeerInSAResponses_Type = Counter32
_FsMsdpPeerInSAResponses_Object = MibTableColumn
fsMsdpPeerInSAResponses = _FsMsdpPeerInSAResponses_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 31),
    _FsMsdpPeerInSAResponses_Type()
)
fsMsdpPeerInSAResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerInSAResponses.setStatus("current")
_FsMsdpPeerOutSAResponses_Type = Counter32
_FsMsdpPeerOutSAResponses_Object = MibTableColumn
fsMsdpPeerOutSAResponses = _FsMsdpPeerOutSAResponses_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 32),
    _FsMsdpPeerOutSAResponses_Type()
)
fsMsdpPeerOutSAResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerOutSAResponses.setStatus("current")
_FsMsdpPeerUpTime_Type = TimeTicks
_FsMsdpPeerUpTime_Object = MibTableColumn
fsMsdpPeerUpTime = _FsMsdpPeerUpTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 33),
    _FsMsdpPeerUpTime_Type()
)
fsMsdpPeerUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerUpTime.setStatus("current")
_FsMsdpPeerInKeepAliveCount_Type = Counter32
_FsMsdpPeerInKeepAliveCount_Object = MibTableColumn
fsMsdpPeerInKeepAliveCount = _FsMsdpPeerInKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 34),
    _FsMsdpPeerInKeepAliveCount_Type()
)
fsMsdpPeerInKeepAliveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerInKeepAliveCount.setStatus("current")
_FsMsdpPeerOutKeepAliveCount_Type = Counter32
_FsMsdpPeerOutKeepAliveCount_Object = MibTableColumn
fsMsdpPeerOutKeepAliveCount = _FsMsdpPeerOutKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 35),
    _FsMsdpPeerOutKeepAliveCount_Type()
)
fsMsdpPeerOutKeepAliveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerOutKeepAliveCount.setStatus("current")
_FsMsdpPeerDataTtlErrorCount_Type = Counter32
_FsMsdpPeerDataTtlErrorCount_Object = MibTableColumn
fsMsdpPeerDataTtlErrorCount = _FsMsdpPeerDataTtlErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 36),
    _FsMsdpPeerDataTtlErrorCount_Type()
)
fsMsdpPeerDataTtlErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpPeerDataTtlErrorCount.setStatus("current")


class _FsMsdpPeerAdminStatus_Type(Integer32):
    """Custom type fsMsdpPeerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("established", 1),
          ("disabled", 2))
    )


_FsMsdpPeerAdminStatus_Type.__name__ = "Integer32"
_FsMsdpPeerAdminStatus_Object = MibTableColumn
fsMsdpPeerAdminStatus = _FsMsdpPeerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 11, 1, 37),
    _FsMsdpPeerAdminStatus_Type()
)
fsMsdpPeerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMsdpPeerAdminStatus.setStatus("current")
_FsMsdpSACacheTable_Object = MibTable
fsMsdpSACacheTable = _FsMsdpSACacheTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 12)
)
if mibBuilder.loadTexts:
    fsMsdpSACacheTable.setStatus("current")
_FsMsdpSACacheEntry_Object = MibTableRow
fsMsdpSACacheEntry = _FsMsdpSACacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 12, 1)
)
fsMsdpSACacheEntry.setIndexNames(
    (0, "SUPERMICRO-MSDP-MIB", "fsMsdpSACacheAddrType"),
    (0, "SUPERMICRO-MSDP-MIB", "fsMsdpSACacheGroupAddr"),
    (0, "SUPERMICRO-MSDP-MIB", "fsMsdpSACacheSourceAddr"),
    (0, "SUPERMICRO-MSDP-MIB", "fsMsdpSACacheOriginRP"),
)
if mibBuilder.loadTexts:
    fsMsdpSACacheEntry.setStatus("current")
_FsMsdpSACacheAddrType_Type = InetAddressType
_FsMsdpSACacheAddrType_Object = MibTableColumn
fsMsdpSACacheAddrType = _FsMsdpSACacheAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 12, 1, 1),
    _FsMsdpSACacheAddrType_Type()
)
fsMsdpSACacheAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMsdpSACacheAddrType.setStatus("current")


class _FsMsdpSACacheGroupAddr_Type(InetAddress):
    """Custom type fsMsdpSACacheGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMsdpSACacheGroupAddr_Type.__name__ = "InetAddress"
_FsMsdpSACacheGroupAddr_Object = MibTableColumn
fsMsdpSACacheGroupAddr = _FsMsdpSACacheGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 12, 1, 2),
    _FsMsdpSACacheGroupAddr_Type()
)
fsMsdpSACacheGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMsdpSACacheGroupAddr.setStatus("current")


class _FsMsdpSACacheSourceAddr_Type(InetAddress):
    """Custom type fsMsdpSACacheSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMsdpSACacheSourceAddr_Type.__name__ = "InetAddress"
_FsMsdpSACacheSourceAddr_Object = MibTableColumn
fsMsdpSACacheSourceAddr = _FsMsdpSACacheSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 12, 1, 3),
    _FsMsdpSACacheSourceAddr_Type()
)
fsMsdpSACacheSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMsdpSACacheSourceAddr.setStatus("current")


class _FsMsdpSACacheOriginRP_Type(InetAddress):
    """Custom type fsMsdpSACacheOriginRP based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMsdpSACacheOriginRP_Type.__name__ = "InetAddress"
_FsMsdpSACacheOriginRP_Object = MibTableColumn
fsMsdpSACacheOriginRP = _FsMsdpSACacheOriginRP_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 12, 1, 4),
    _FsMsdpSACacheOriginRP_Type()
)
fsMsdpSACacheOriginRP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMsdpSACacheOriginRP.setStatus("current")


class _FsMsdpSACachePeerLearnedFrom_Type(InetAddress):
    """Custom type fsMsdpSACachePeerLearnedFrom based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMsdpSACachePeerLearnedFrom_Type.__name__ = "InetAddress"
_FsMsdpSACachePeerLearnedFrom_Object = MibTableColumn
fsMsdpSACachePeerLearnedFrom = _FsMsdpSACachePeerLearnedFrom_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 12, 1, 5),
    _FsMsdpSACachePeerLearnedFrom_Type()
)
fsMsdpSACachePeerLearnedFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpSACachePeerLearnedFrom.setStatus("current")


class _FsMsdpSACacheRPFPeer_Type(InetAddress):
    """Custom type fsMsdpSACacheRPFPeer based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMsdpSACacheRPFPeer_Type.__name__ = "InetAddress"
_FsMsdpSACacheRPFPeer_Object = MibTableColumn
fsMsdpSACacheRPFPeer = _FsMsdpSACacheRPFPeer_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 12, 1, 6),
    _FsMsdpSACacheRPFPeer_Type()
)
fsMsdpSACacheRPFPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpSACacheRPFPeer.setStatus("current")
_FsMsdpSACacheInSAs_Type = Counter32
_FsMsdpSACacheInSAs_Object = MibTableColumn
fsMsdpSACacheInSAs = _FsMsdpSACacheInSAs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 12, 1, 7),
    _FsMsdpSACacheInSAs_Type()
)
fsMsdpSACacheInSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpSACacheInSAs.setStatus("current")
_FsMsdpSACacheInDataPackets_Type = Counter32
_FsMsdpSACacheInDataPackets_Object = MibTableColumn
fsMsdpSACacheInDataPackets = _FsMsdpSACacheInDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 12, 1, 8),
    _FsMsdpSACacheInDataPackets_Type()
)
fsMsdpSACacheInDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpSACacheInDataPackets.setStatus("current")
_FsMsdpSACacheUpTime_Type = TimeTicks
_FsMsdpSACacheUpTime_Object = MibTableColumn
fsMsdpSACacheUpTime = _FsMsdpSACacheUpTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 12, 1, 9),
    _FsMsdpSACacheUpTime_Type()
)
fsMsdpSACacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpSACacheUpTime.setStatus("current")
_FsMsdpSACacheExpiryTime_Type = TimeTicks
_FsMsdpSACacheExpiryTime_Object = MibTableColumn
fsMsdpSACacheExpiryTime = _FsMsdpSACacheExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 12, 1, 10),
    _FsMsdpSACacheExpiryTime_Type()
)
fsMsdpSACacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpSACacheExpiryTime.setStatus("current")


class _FsMsdpSACacheStatus_Type(RowStatus):
    """Custom type fsMsdpSACacheStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destroy", 6))
    )


_FsMsdpSACacheStatus_Type.__name__ = "RowStatus"
_FsMsdpSACacheStatus_Object = MibTableColumn
fsMsdpSACacheStatus = _FsMsdpSACacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 12, 1, 11),
    _FsMsdpSACacheStatus_Type()
)
fsMsdpSACacheStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMsdpSACacheStatus.setStatus("current")
_FsMsdpMeshGroupTable_Object = MibTable
fsMsdpMeshGroupTable = _FsMsdpMeshGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 13)
)
if mibBuilder.loadTexts:
    fsMsdpMeshGroupTable.setStatus("current")
_FsMsdpMeshGroupEntry_Object = MibTableRow
fsMsdpMeshGroupEntry = _FsMsdpMeshGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 13, 1)
)
fsMsdpMeshGroupEntry.setIndexNames(
    (0, "SUPERMICRO-MSDP-MIB", "fsMsdpMeshGroupName"),
    (0, "SUPERMICRO-MSDP-MIB", "fsMsdpMeshGroupAddrType"),
    (0, "SUPERMICRO-MSDP-MIB", "fsMsdpMeshGroupPeerAddress"),
)
if mibBuilder.loadTexts:
    fsMsdpMeshGroupEntry.setStatus("current")


class _FsMsdpMeshGroupName_Type(DisplayString):
    """Custom type fsMsdpMeshGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsMsdpMeshGroupName_Type.__name__ = "DisplayString"
_FsMsdpMeshGroupName_Object = MibTableColumn
fsMsdpMeshGroupName = _FsMsdpMeshGroupName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 13, 1, 1),
    _FsMsdpMeshGroupName_Type()
)
fsMsdpMeshGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMsdpMeshGroupName.setStatus("current")
_FsMsdpMeshGroupAddrType_Type = InetAddressType
_FsMsdpMeshGroupAddrType_Object = MibTableColumn
fsMsdpMeshGroupAddrType = _FsMsdpMeshGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 13, 1, 2),
    _FsMsdpMeshGroupAddrType_Type()
)
fsMsdpMeshGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMsdpMeshGroupAddrType.setStatus("current")


class _FsMsdpMeshGroupPeerAddress_Type(InetAddress):
    """Custom type fsMsdpMeshGroupPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMsdpMeshGroupPeerAddress_Type.__name__ = "InetAddress"
_FsMsdpMeshGroupPeerAddress_Object = MibTableColumn
fsMsdpMeshGroupPeerAddress = _FsMsdpMeshGroupPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 13, 1, 3),
    _FsMsdpMeshGroupPeerAddress_Type()
)
fsMsdpMeshGroupPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMsdpMeshGroupPeerAddress.setStatus("current")
_FsMsdpMeshGroupStatus_Type = RowStatus
_FsMsdpMeshGroupStatus_Object = MibTableColumn
fsMsdpMeshGroupStatus = _FsMsdpMeshGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 13, 1, 4),
    _FsMsdpMeshGroupStatus_Type()
)
fsMsdpMeshGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMsdpMeshGroupStatus.setStatus("current")
_FsMsdpRPTable_Object = MibTable
fsMsdpRPTable = _FsMsdpRPTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 14)
)
if mibBuilder.loadTexts:
    fsMsdpRPTable.setStatus("current")
_FsMsdpRPEntry_Object = MibTableRow
fsMsdpRPEntry = _FsMsdpRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 14, 1)
)
fsMsdpRPEntry.setIndexNames(
    (0, "SUPERMICRO-MSDP-MIB", "fsMsdpRPAddrType"),
)
if mibBuilder.loadTexts:
    fsMsdpRPEntry.setStatus("current")
_FsMsdpRPAddrType_Type = InetAddressType
_FsMsdpRPAddrType_Object = MibTableColumn
fsMsdpRPAddrType = _FsMsdpRPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 14, 1, 1),
    _FsMsdpRPAddrType_Type()
)
fsMsdpRPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMsdpRPAddrType.setStatus("current")


class _FsMsdpRPAddress_Type(InetAddress):
    """Custom type fsMsdpRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMsdpRPAddress_Type.__name__ = "InetAddress"
_FsMsdpRPAddress_Object = MibTableColumn
fsMsdpRPAddress = _FsMsdpRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 14, 1, 2),
    _FsMsdpRPAddress_Type()
)
fsMsdpRPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMsdpRPAddress.setStatus("current")


class _FsMsdpRPOperStatus_Type(Integer32):
    """Custom type fsMsdpRPOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_FsMsdpRPOperStatus_Type.__name__ = "Integer32"
_FsMsdpRPOperStatus_Object = MibTableColumn
fsMsdpRPOperStatus = _FsMsdpRPOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 14, 1, 3),
    _FsMsdpRPOperStatus_Type()
)
fsMsdpRPOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpRPOperStatus.setStatus("current")
_FsMsdpRPStatus_Type = RowStatus
_FsMsdpRPStatus_Object = MibTableColumn
fsMsdpRPStatus = _FsMsdpRPStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 14, 1, 4),
    _FsMsdpRPStatus_Type()
)
fsMsdpRPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMsdpRPStatus.setStatus("current")
_FsMsdpPeerFilterTable_Object = MibTable
fsMsdpPeerFilterTable = _FsMsdpPeerFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 15)
)
if mibBuilder.loadTexts:
    fsMsdpPeerFilterTable.setStatus("current")
_FsMsdpPeerFilterEntry_Object = MibTableRow
fsMsdpPeerFilterEntry = _FsMsdpPeerFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 15, 1)
)
fsMsdpPeerFilterEntry.setIndexNames(
    (0, "SUPERMICRO-MSDP-MIB", "fsMsdpPeerFilterAddrType"),
)
if mibBuilder.loadTexts:
    fsMsdpPeerFilterEntry.setStatus("current")
_FsMsdpPeerFilterAddrType_Type = InetAddressType
_FsMsdpPeerFilterAddrType_Object = MibTableColumn
fsMsdpPeerFilterAddrType = _FsMsdpPeerFilterAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 15, 1, 1),
    _FsMsdpPeerFilterAddrType_Type()
)
fsMsdpPeerFilterAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMsdpPeerFilterAddrType.setStatus("current")


class _FsMsdpPeerFilterRouteMap_Type(DisplayString):
    """Custom type fsMsdpPeerFilterRouteMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsMsdpPeerFilterRouteMap_Type.__name__ = "DisplayString"
_FsMsdpPeerFilterRouteMap_Object = MibTableColumn
fsMsdpPeerFilterRouteMap = _FsMsdpPeerFilterRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 15, 1, 2),
    _FsMsdpPeerFilterRouteMap_Type()
)
fsMsdpPeerFilterRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMsdpPeerFilterRouteMap.setStatus("current")
_FsMsdpPeerFilterStatus_Type = RowStatus
_FsMsdpPeerFilterStatus_Object = MibTableColumn
fsMsdpPeerFilterStatus = _FsMsdpPeerFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 15, 1, 3),
    _FsMsdpPeerFilterStatus_Type()
)
fsMsdpPeerFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMsdpPeerFilterStatus.setStatus("current")
_FsMsdpSARedistributionTable_Object = MibTable
fsMsdpSARedistributionTable = _FsMsdpSARedistributionTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 16)
)
if mibBuilder.loadTexts:
    fsMsdpSARedistributionTable.setStatus("current")
_FsMsdpSARedistributionEntry_Object = MibTableRow
fsMsdpSARedistributionEntry = _FsMsdpSARedistributionEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 16, 1)
)
fsMsdpSARedistributionEntry.setIndexNames(
    (0, "SUPERMICRO-MSDP-MIB", "fsMsdpSARedistributionAddrType"),
)
if mibBuilder.loadTexts:
    fsMsdpSARedistributionEntry.setStatus("current")
_FsMsdpSARedistributionAddrType_Type = InetAddressType
_FsMsdpSARedistributionAddrType_Object = MibTableColumn
fsMsdpSARedistributionAddrType = _FsMsdpSARedistributionAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 16, 1, 1),
    _FsMsdpSARedistributionAddrType_Type()
)
fsMsdpSARedistributionAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMsdpSARedistributionAddrType.setStatus("current")
_FsMsdpSARedistributionStatus_Type = RowStatus
_FsMsdpSARedistributionStatus_Object = MibTableColumn
fsMsdpSARedistributionStatus = _FsMsdpSARedistributionStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 16, 1, 2),
    _FsMsdpSARedistributionStatus_Type()
)
fsMsdpSARedistributionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMsdpSARedistributionStatus.setStatus("current")


class _FsMsdpSARedistributionRouteMap_Type(DisplayString):
    """Custom type fsMsdpSARedistributionRouteMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsMsdpSARedistributionRouteMap_Type.__name__ = "DisplayString"
_FsMsdpSARedistributionRouteMap_Object = MibTableColumn
fsMsdpSARedistributionRouteMap = _FsMsdpSARedistributionRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 16, 1, 3),
    _FsMsdpSARedistributionRouteMap_Type()
)
fsMsdpSARedistributionRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMsdpSARedistributionRouteMap.setStatus("current")


class _FsMsdpSARedistributionRouteMapStat_Type(Integer32):
    """Custom type fsMsdpSARedistributionRouteMapStat based on Integer32"""
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


_FsMsdpSARedistributionRouteMapStat_Type.__name__ = "Integer32"
_FsMsdpSARedistributionRouteMapStat_Object = MibTableColumn
fsMsdpSARedistributionRouteMapStat = _FsMsdpSARedistributionRouteMapStat_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 16, 1, 4),
    _FsMsdpSARedistributionRouteMapStat_Type()
)
fsMsdpSARedistributionRouteMapStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMsdpSARedistributionRouteMapStat.setStatus("current")
_FsMsdpRtrId_Type = IpAddress
_FsMsdpRtrId_Object = MibScalar
fsMsdpRtrId = _FsMsdpRtrId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 17),
    _FsMsdpRtrId_Type()
)
fsMsdpRtrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMsdpRtrId.setStatus("current")
_FsMsdpStat_ObjectIdentity = ObjectIdentity
fsMsdpStat = _FsMsdpStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 2)
)
_FsMsdpStatEstPeerCount_Type = Integer32
_FsMsdpStatEstPeerCount_Object = MibScalar
fsMsdpStatEstPeerCount = _FsMsdpStatEstPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 2, 1),
    _FsMsdpStatEstPeerCount_Type()
)
fsMsdpStatEstPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMsdpStatEstPeerCount.setStatus("current")

# Managed Objects groups


# Notification objects

fsMsdpEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 0, 1)
)
fsMsdpEstablished.setObjects(
      *(("SUPERMICRO-MSDP-MIB", "fsMsdpRtrId"),
        ("SUPERMICRO-MSDP-MIB", "fsMsdpPeerFsmEstablishedTransitions"))
)
if mibBuilder.loadTexts:
    fsMsdpEstablished.setStatus(
        "current"
    )

fsMsdpBackwardTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 0, 2)
)
fsMsdpBackwardTransition.setObjects(
      *(("SUPERMICRO-MSDP-MIB", "fsMsdpRtrId"),
        ("SUPERMICRO-MSDP-MIB", "fsMsdpPeerState"))
)
if mibBuilder.loadTexts:
    fsMsdpBackwardTransition.setStatus(
        "current"
    )

fsMsdpRPOperStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 61, 1, 0, 3)
)
fsMsdpRPOperStatusChange.setObjects(
      *(("SUPERMICRO-MSDP-MIB", "fsMsdpRtrId"),
        ("SUPERMICRO-MSDP-MIB", "fsMsdpRPOperStatus"))
)
if mibBuilder.loadTexts:
    fsMsdpRPOperStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-MSDP-MIB",
    **{"fsMsdpMIB": fsMsdpMIB,
       "fsMsdp": fsMsdp,
       "fsMsdpTraps": fsMsdpTraps,
       "fsMsdpEstablished": fsMsdpEstablished,
       "fsMsdpBackwardTransition": fsMsdpBackwardTransition,
       "fsMsdpRPOperStatusChange": fsMsdpRPOperStatusChange,
       "fsMsdpTraceLevel": fsMsdpTraceLevel,
       "fsMsdpIPv4AdminStat": fsMsdpIPv4AdminStat,
       "fsMsdpIPv6AdminStat": fsMsdpIPv6AdminStat,
       "fsMsdpCacheLifetime": fsMsdpCacheLifetime,
       "fsMsdpNumSACacheEntries": fsMsdpNumSACacheEntries,
       "fsMsdpMaxPeerSessions": fsMsdpMaxPeerSessions,
       "fsMsdpMappingComponentId": fsMsdpMappingComponentId,
       "fsMsdpListenerPort": fsMsdpListenerPort,
       "fsMsdpPeerFilter": fsMsdpPeerFilter,
       "fsMsdpPeerCount": fsMsdpPeerCount,
       "fsMsdpPeerTable": fsMsdpPeerTable,
       "fsMsdpPeerEntry": fsMsdpPeerEntry,
       "fsMsdpPeerAddrType": fsMsdpPeerAddrType,
       "fsMsdpPeerRemoteAddress": fsMsdpPeerRemoteAddress,
       "fsMsdpPeerState": fsMsdpPeerState,
       "fsMsdpPeerRPFFailures": fsMsdpPeerRPFFailures,
       "fsMsdpPeerInSAs": fsMsdpPeerInSAs,
       "fsMsdpPeerOutSAs": fsMsdpPeerOutSAs,
       "fsMsdpPeerInSARequests": fsMsdpPeerInSARequests,
       "fsMsdpPeerOutSARequests": fsMsdpPeerOutSARequests,
       "fsMsdpPeerInControlMessages": fsMsdpPeerInControlMessages,
       "fsMsdpPeerOutControlMessages": fsMsdpPeerOutControlMessages,
       "fsMsdpPeerInDataPackets": fsMsdpPeerInDataPackets,
       "fsMsdpPeerOutDataPackets": fsMsdpPeerOutDataPackets,
       "fsMsdpPeerFsmEstablishedTransitions": fsMsdpPeerFsmEstablishedTransitions,
       "fsMsdpPeerFsmEstablishedTime": fsMsdpPeerFsmEstablishedTime,
       "fsMsdpPeerInMessageTime": fsMsdpPeerInMessageTime,
       "fsMsdpPeerLocalAddress": fsMsdpPeerLocalAddress,
       "fsMsdpPeerConnectRetryInterval": fsMsdpPeerConnectRetryInterval,
       "fsMsdpPeerHoldTimeConfigured": fsMsdpPeerHoldTimeConfigured,
       "fsMsdpPeerKeepAliveConfigured": fsMsdpPeerKeepAliveConfigured,
       "fsMsdpPeerDataTtl": fsMsdpPeerDataTtl,
       "fsMsdpPeerStatus": fsMsdpPeerStatus,
       "fsMsdpPeerRemotePort": fsMsdpPeerRemotePort,
       "fsMsdpPeerLocalPort": fsMsdpPeerLocalPort,
       "fsMsdpPeerEncapsulationType": fsMsdpPeerEncapsulationType,
       "fsMsdpPeerConnectionAttempts": fsMsdpPeerConnectionAttempts,
       "fsMsdpPeerDiscontinuityTime": fsMsdpPeerDiscontinuityTime,
       "fsMsdpPeerMD5AuthPassword": fsMsdpPeerMD5AuthPassword,
       "fsMsdpPeerMD5AuthPwdStat": fsMsdpPeerMD5AuthPwdStat,
       "fsMsdpPeerMD5FailCount": fsMsdpPeerMD5FailCount,
       "fsMsdpPeerMD5SuccessCount": fsMsdpPeerMD5SuccessCount,
       "fsMsdpPeerInSAResponses": fsMsdpPeerInSAResponses,
       "fsMsdpPeerOutSAResponses": fsMsdpPeerOutSAResponses,
       "fsMsdpPeerUpTime": fsMsdpPeerUpTime,
       "fsMsdpPeerInKeepAliveCount": fsMsdpPeerInKeepAliveCount,
       "fsMsdpPeerOutKeepAliveCount": fsMsdpPeerOutKeepAliveCount,
       "fsMsdpPeerDataTtlErrorCount": fsMsdpPeerDataTtlErrorCount,
       "fsMsdpPeerAdminStatus": fsMsdpPeerAdminStatus,
       "fsMsdpSACacheTable": fsMsdpSACacheTable,
       "fsMsdpSACacheEntry": fsMsdpSACacheEntry,
       "fsMsdpSACacheAddrType": fsMsdpSACacheAddrType,
       "fsMsdpSACacheGroupAddr": fsMsdpSACacheGroupAddr,
       "fsMsdpSACacheSourceAddr": fsMsdpSACacheSourceAddr,
       "fsMsdpSACacheOriginRP": fsMsdpSACacheOriginRP,
       "fsMsdpSACachePeerLearnedFrom": fsMsdpSACachePeerLearnedFrom,
       "fsMsdpSACacheRPFPeer": fsMsdpSACacheRPFPeer,
       "fsMsdpSACacheInSAs": fsMsdpSACacheInSAs,
       "fsMsdpSACacheInDataPackets": fsMsdpSACacheInDataPackets,
       "fsMsdpSACacheUpTime": fsMsdpSACacheUpTime,
       "fsMsdpSACacheExpiryTime": fsMsdpSACacheExpiryTime,
       "fsMsdpSACacheStatus": fsMsdpSACacheStatus,
       "fsMsdpMeshGroupTable": fsMsdpMeshGroupTable,
       "fsMsdpMeshGroupEntry": fsMsdpMeshGroupEntry,
       "fsMsdpMeshGroupName": fsMsdpMeshGroupName,
       "fsMsdpMeshGroupAddrType": fsMsdpMeshGroupAddrType,
       "fsMsdpMeshGroupPeerAddress": fsMsdpMeshGroupPeerAddress,
       "fsMsdpMeshGroupStatus": fsMsdpMeshGroupStatus,
       "fsMsdpRPTable": fsMsdpRPTable,
       "fsMsdpRPEntry": fsMsdpRPEntry,
       "fsMsdpRPAddrType": fsMsdpRPAddrType,
       "fsMsdpRPAddress": fsMsdpRPAddress,
       "fsMsdpRPOperStatus": fsMsdpRPOperStatus,
       "fsMsdpRPStatus": fsMsdpRPStatus,
       "fsMsdpPeerFilterTable": fsMsdpPeerFilterTable,
       "fsMsdpPeerFilterEntry": fsMsdpPeerFilterEntry,
       "fsMsdpPeerFilterAddrType": fsMsdpPeerFilterAddrType,
       "fsMsdpPeerFilterRouteMap": fsMsdpPeerFilterRouteMap,
       "fsMsdpPeerFilterStatus": fsMsdpPeerFilterStatus,
       "fsMsdpSARedistributionTable": fsMsdpSARedistributionTable,
       "fsMsdpSARedistributionEntry": fsMsdpSARedistributionEntry,
       "fsMsdpSARedistributionAddrType": fsMsdpSARedistributionAddrType,
       "fsMsdpSARedistributionStatus": fsMsdpSARedistributionStatus,
       "fsMsdpSARedistributionRouteMap": fsMsdpSARedistributionRouteMap,
       "fsMsdpSARedistributionRouteMapStat": fsMsdpSARedistributionRouteMapStat,
       "fsMsdpRtrId": fsMsdpRtrId,
       "fsMsdpStat": fsMsdpStat,
       "fsMsdpStatEstPeerCount": fsMsdpStatEstPeerCount}
)
