# SNMP MIB module (ARICENT-MISTD-IPVX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-MISTD-IPVX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:57 2025
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

(IANAipRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipRouteProtocol")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber,
 InetZoneIndex) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber",
    "InetZoneIndex")

(IpAddressOriginTC,
 IpAddressPrefixOriginTC,
 IpAddressStatusTC,
 Ipv6AddressIfIdentifierTC) = mibBuilder.importSymbols(
    "IP-MIB",
    "IpAddressOriginTC",
    "IpAddressPrefixOriginTC",
    "IpAddressStatusTC",
    "Ipv6AddressIfIdentifierTC")

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
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

fsMIStdIp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37)
)
if mibBuilder.loadTexts:
    fsMIStdIp.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FsInetVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2))
    )



# MIB Managed Objects in the order of their OIDs

_FsMIStdIpv4InterfaceTableLastChange_Type = TimeStamp
_FsMIStdIpv4InterfaceTableLastChange_Object = MibScalar
fsMIStdIpv4InterfaceTableLastChange = _FsMIStdIpv4InterfaceTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 1),
    _FsMIStdIpv4InterfaceTableLastChange_Type()
)
fsMIStdIpv4InterfaceTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv4InterfaceTableLastChange.setStatus("current")
_FsMIStdIpv6InterfaceTableLastChange_Type = TimeStamp
_FsMIStdIpv6InterfaceTableLastChange_Object = MibScalar
fsMIStdIpv6InterfaceTableLastChange = _FsMIStdIpv6InterfaceTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 2),
    _FsMIStdIpv6InterfaceTableLastChange_Type()
)
fsMIStdIpv6InterfaceTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6InterfaceTableLastChange.setStatus("current")
_FsMIStdIpIfStatsTableLastChange_Type = TimeStamp
_FsMIStdIpIfStatsTableLastChange_Object = MibScalar
fsMIStdIpIfStatsTableLastChange = _FsMIStdIpIfStatsTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 3),
    _FsMIStdIpIfStatsTableLastChange_Type()
)
fsMIStdIpIfStatsTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsTableLastChange.setStatus("current")
_FsMIStdIpGlobalTable_Object = MibTable
fsMIStdIpGlobalTable = _FsMIStdIpGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 4)
)
if mibBuilder.loadTexts:
    fsMIStdIpGlobalTable.setStatus("current")
_FsMIStdIpGlobalEntry_Object = MibTableRow
fsMIStdIpGlobalEntry = _FsMIStdIpGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 4, 1)
)
fsMIStdIpGlobalEntry.setIndexNames(
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
)
if mibBuilder.loadTexts:
    fsMIStdIpGlobalEntry.setStatus("current")


class _FsMIStdIpContextId_Type(Integer32):
    """Custom type fsMIStdIpContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_FsMIStdIpContextId_Type.__name__ = "Integer32"
_FsMIStdIpContextId_Object = MibTableColumn
fsMIStdIpContextId = _FsMIStdIpContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 4, 1, 1),
    _FsMIStdIpContextId_Type()
)
fsMIStdIpContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpContextId.setStatus("current")


class _FsMIStdIpForwarding_Type(Integer32):
    """Custom type fsMIStdIpForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notForwarding", 2))
    )


_FsMIStdIpForwarding_Type.__name__ = "Integer32"
_FsMIStdIpForwarding_Object = MibTableColumn
fsMIStdIpForwarding = _FsMIStdIpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 4, 1, 2),
    _FsMIStdIpForwarding_Type()
)
fsMIStdIpForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdIpForwarding.setStatus("current")


class _FsMIStdIpDefaultTTL_Type(Integer32):
    """Custom type fsMIStdIpDefaultTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsMIStdIpDefaultTTL_Type.__name__ = "Integer32"
_FsMIStdIpDefaultTTL_Object = MibTableColumn
fsMIStdIpDefaultTTL = _FsMIStdIpDefaultTTL_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 4, 1, 3),
    _FsMIStdIpDefaultTTL_Type()
)
fsMIStdIpDefaultTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdIpDefaultTTL.setStatus("current")
_FsMIStdIpReasmTimeout_Type = Integer32
_FsMIStdIpReasmTimeout_Object = MibTableColumn
fsMIStdIpReasmTimeout = _FsMIStdIpReasmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 4, 1, 4),
    _FsMIStdIpReasmTimeout_Type()
)
fsMIStdIpReasmTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpReasmTimeout.setStatus("current")
if mibBuilder.loadTexts:
    fsMIStdIpReasmTimeout.setUnits("seconds")


class _FsMIStdIpv6IpForwarding_Type(Integer32):
    """Custom type fsMIStdIpv6IpForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notForwarding", 2))
    )


_FsMIStdIpv6IpForwarding_Type.__name__ = "Integer32"
_FsMIStdIpv6IpForwarding_Object = MibTableColumn
fsMIStdIpv6IpForwarding = _FsMIStdIpv6IpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 4, 1, 5),
    _FsMIStdIpv6IpForwarding_Type()
)
fsMIStdIpv6IpForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdIpv6IpForwarding.setStatus("current")


class _FsMIStdIpv6IpDefaultHopLimit_Type(Integer32):
    """Custom type fsMIStdIpv6IpDefaultHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIStdIpv6IpDefaultHopLimit_Type.__name__ = "Integer32"
_FsMIStdIpv6IpDefaultHopLimit_Object = MibTableColumn
fsMIStdIpv6IpDefaultHopLimit = _FsMIStdIpv6IpDefaultHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 4, 1, 6),
    _FsMIStdIpv6IpDefaultHopLimit_Type()
)
fsMIStdIpv6IpDefaultHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdIpv6IpDefaultHopLimit.setStatus("current")
_FsMIStdInetCidrRouteNumber_Type = Gauge32
_FsMIStdInetCidrRouteNumber_Object = MibTableColumn
fsMIStdInetCidrRouteNumber = _FsMIStdInetCidrRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 4, 1, 7),
    _FsMIStdInetCidrRouteNumber_Type()
)
fsMIStdInetCidrRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteNumber.setStatus("current")
_FsMIStdInetCidrRouteDiscards_Type = Counter32
_FsMIStdInetCidrRouteDiscards_Object = MibTableColumn
fsMIStdInetCidrRouteDiscards = _FsMIStdInetCidrRouteDiscards_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 4, 1, 8),
    _FsMIStdInetCidrRouteDiscards_Type()
)
fsMIStdInetCidrRouteDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteDiscards.setStatus("current")
_FsMIStdIpv4InterfaceTable_Object = MibTable
fsMIStdIpv4InterfaceTable = _FsMIStdIpv4InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 5)
)
if mibBuilder.loadTexts:
    fsMIStdIpv4InterfaceTable.setStatus("current")
_FsMIStdIpv4InterfaceEntry_Object = MibTableRow
fsMIStdIpv4InterfaceEntry = _FsMIStdIpv4InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 5, 1)
)
fsMIStdIpv4InterfaceEntry.setIndexNames(
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpv4InterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    fsMIStdIpv4InterfaceEntry.setStatus("current")
_FsMIStdIpv4InterfaceIfIndex_Type = InterfaceIndex
_FsMIStdIpv4InterfaceIfIndex_Object = MibTableColumn
fsMIStdIpv4InterfaceIfIndex = _FsMIStdIpv4InterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 5, 1, 1),
    _FsMIStdIpv4InterfaceIfIndex_Type()
)
fsMIStdIpv4InterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpv4InterfaceIfIndex.setStatus("current")


class _FsMIStdIpv4InterfaceReasmMaxSize_Type(Integer32):
    """Custom type fsMIStdIpv4InterfaceReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIStdIpv4InterfaceReasmMaxSize_Type.__name__ = "Integer32"
_FsMIStdIpv4InterfaceReasmMaxSize_Object = MibTableColumn
fsMIStdIpv4InterfaceReasmMaxSize = _FsMIStdIpv4InterfaceReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 5, 1, 2),
    _FsMIStdIpv4InterfaceReasmMaxSize_Type()
)
fsMIStdIpv4InterfaceReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv4InterfaceReasmMaxSize.setStatus("current")


class _FsMIStdIpv4InterfaceEnableStatus_Type(Integer32):
    """Custom type fsMIStdIpv4InterfaceEnableStatus based on Integer32"""
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


_FsMIStdIpv4InterfaceEnableStatus_Type.__name__ = "Integer32"
_FsMIStdIpv4InterfaceEnableStatus_Object = MibTableColumn
fsMIStdIpv4InterfaceEnableStatus = _FsMIStdIpv4InterfaceEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 5, 1, 3),
    _FsMIStdIpv4InterfaceEnableStatus_Type()
)
fsMIStdIpv4InterfaceEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdIpv4InterfaceEnableStatus.setStatus("current")


class _FsMIStdIpv4InterfaceRetransmitTime_Type(Unsigned32):
    """Custom type fsMIStdIpv4InterfaceRetransmitTime based on Unsigned32"""
    defaultValue = 1000


_FsMIStdIpv4InterfaceRetransmitTime_Type.__name__ = "Unsigned32"
_FsMIStdIpv4InterfaceRetransmitTime_Object = MibTableColumn
fsMIStdIpv4InterfaceRetransmitTime = _FsMIStdIpv4InterfaceRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 5, 1, 4),
    _FsMIStdIpv4InterfaceRetransmitTime_Type()
)
fsMIStdIpv4InterfaceRetransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv4InterfaceRetransmitTime.setStatus("current")
if mibBuilder.loadTexts:
    fsMIStdIpv4InterfaceRetransmitTime.setUnits("milliseconds")
_FsMIStdIpv4IfContextId_Type = Integer32
_FsMIStdIpv4IfContextId_Object = MibTableColumn
fsMIStdIpv4IfContextId = _FsMIStdIpv4IfContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 5, 1, 5),
    _FsMIStdIpv4IfContextId_Type()
)
fsMIStdIpv4IfContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv4IfContextId.setStatus("current")
_FsMIStdIpv6InterfaceTable_Object = MibTable
fsMIStdIpv6InterfaceTable = _FsMIStdIpv6InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 6)
)
if mibBuilder.loadTexts:
    fsMIStdIpv6InterfaceTable.setStatus("current")
_FsMIStdIpv6InterfaceEntry_Object = MibTableRow
fsMIStdIpv6InterfaceEntry = _FsMIStdIpv6InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 6, 1)
)
fsMIStdIpv6InterfaceEntry.setIndexNames(
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpv6InterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    fsMIStdIpv6InterfaceEntry.setStatus("current")
_FsMIStdIpv6InterfaceIfIndex_Type = InterfaceIndex
_FsMIStdIpv6InterfaceIfIndex_Object = MibTableColumn
fsMIStdIpv6InterfaceIfIndex = _FsMIStdIpv6InterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 6, 1, 1),
    _FsMIStdIpv6InterfaceIfIndex_Type()
)
fsMIStdIpv6InterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpv6InterfaceIfIndex.setStatus("current")


class _FsMIStdIpv6InterfaceReasmMaxSize_Type(Unsigned32):
    """Custom type fsMIStdIpv6InterfaceReasmMaxSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 65535),
    )


_FsMIStdIpv6InterfaceReasmMaxSize_Type.__name__ = "Unsigned32"
_FsMIStdIpv6InterfaceReasmMaxSize_Object = MibTableColumn
fsMIStdIpv6InterfaceReasmMaxSize = _FsMIStdIpv6InterfaceReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 6, 1, 2),
    _FsMIStdIpv6InterfaceReasmMaxSize_Type()
)
fsMIStdIpv6InterfaceReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6InterfaceReasmMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    fsMIStdIpv6InterfaceReasmMaxSize.setUnits("octets")
_FsMIStdIpv6InterfaceIdentifier_Type = Ipv6AddressIfIdentifierTC
_FsMIStdIpv6InterfaceIdentifier_Object = MibTableColumn
fsMIStdIpv6InterfaceIdentifier = _FsMIStdIpv6InterfaceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 6, 1, 3),
    _FsMIStdIpv6InterfaceIdentifier_Type()
)
fsMIStdIpv6InterfaceIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6InterfaceIdentifier.setStatus("current")


class _FsMIStdIpv6InterfaceEnableStatus_Type(Integer32):
    """Custom type fsMIStdIpv6InterfaceEnableStatus based on Integer32"""
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


_FsMIStdIpv6InterfaceEnableStatus_Type.__name__ = "Integer32"
_FsMIStdIpv6InterfaceEnableStatus_Object = MibTableColumn
fsMIStdIpv6InterfaceEnableStatus = _FsMIStdIpv6InterfaceEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 6, 1, 4),
    _FsMIStdIpv6InterfaceEnableStatus_Type()
)
fsMIStdIpv6InterfaceEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdIpv6InterfaceEnableStatus.setStatus("current")
_FsMIStdIpv6InterfaceReachableTime_Type = Unsigned32
_FsMIStdIpv6InterfaceReachableTime_Object = MibTableColumn
fsMIStdIpv6InterfaceReachableTime = _FsMIStdIpv6InterfaceReachableTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 6, 1, 5),
    _FsMIStdIpv6InterfaceReachableTime_Type()
)
fsMIStdIpv6InterfaceReachableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6InterfaceReachableTime.setStatus("current")
if mibBuilder.loadTexts:
    fsMIStdIpv6InterfaceReachableTime.setUnits("milliseconds")
_FsMIStdIpv6InterfaceRetransmitTime_Type = Unsigned32
_FsMIStdIpv6InterfaceRetransmitTime_Object = MibTableColumn
fsMIStdIpv6InterfaceRetransmitTime = _FsMIStdIpv6InterfaceRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 6, 1, 6),
    _FsMIStdIpv6InterfaceRetransmitTime_Type()
)
fsMIStdIpv6InterfaceRetransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6InterfaceRetransmitTime.setStatus("current")
if mibBuilder.loadTexts:
    fsMIStdIpv6InterfaceRetransmitTime.setUnits("milliseconds")


class _FsMIStdIpv6InterfaceForwarding_Type(Integer32):
    """Custom type fsMIStdIpv6InterfaceForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notForwarding", 2))
    )


_FsMIStdIpv6InterfaceForwarding_Type.__name__ = "Integer32"
_FsMIStdIpv6InterfaceForwarding_Object = MibTableColumn
fsMIStdIpv6InterfaceForwarding = _FsMIStdIpv6InterfaceForwarding_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 6, 1, 7),
    _FsMIStdIpv6InterfaceForwarding_Type()
)
fsMIStdIpv6InterfaceForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdIpv6InterfaceForwarding.setStatus("current")
_FsMIStdIpv6IfContextId_Type = Integer32
_FsMIStdIpv6IfContextId_Object = MibTableColumn
fsMIStdIpv6IfContextId = _FsMIStdIpv6IfContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 6, 1, 8),
    _FsMIStdIpv6IfContextId_Type()
)
fsMIStdIpv6IfContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6IfContextId.setStatus("current")
_FsMIStdIpSystemStatsTable_Object = MibTable
fsMIStdIpSystemStatsTable = _FsMIStdIpSystemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7)
)
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsTable.setStatus("current")
_FsMIStdIpSystemStatsEntry_Object = MibTableRow
fsMIStdIpSystemStatsEntry = _FsMIStdIpSystemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1)
)
fsMIStdIpSystemStatsEntry.setIndexNames(
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpSystemStatsIPVersion"),
)
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsEntry.setStatus("current")
_FsMIStdIpSystemStatsIPVersion_Type = FsInetVersion
_FsMIStdIpSystemStatsIPVersion_Object = MibTableColumn
fsMIStdIpSystemStatsIPVersion = _FsMIStdIpSystemStatsIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 1),
    _FsMIStdIpSystemStatsIPVersion_Type()
)
fsMIStdIpSystemStatsIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsIPVersion.setStatus("current")
_FsMIStdIpSystemStatsInReceives_Type = Counter32
_FsMIStdIpSystemStatsInReceives_Object = MibTableColumn
fsMIStdIpSystemStatsInReceives = _FsMIStdIpSystemStatsInReceives_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 2),
    _FsMIStdIpSystemStatsInReceives_Type()
)
fsMIStdIpSystemStatsInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsInReceives.setStatus("current")
_FsMIStdIpSystemStatsHCInReceives_Type = Counter64
_FsMIStdIpSystemStatsHCInReceives_Object = MibTableColumn
fsMIStdIpSystemStatsHCInReceives = _FsMIStdIpSystemStatsHCInReceives_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 3),
    _FsMIStdIpSystemStatsHCInReceives_Type()
)
fsMIStdIpSystemStatsHCInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsHCInReceives.setStatus("current")
_FsMIStdIpSystemStatsInOctets_Type = Counter32
_FsMIStdIpSystemStatsInOctets_Object = MibTableColumn
fsMIStdIpSystemStatsInOctets = _FsMIStdIpSystemStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 4),
    _FsMIStdIpSystemStatsInOctets_Type()
)
fsMIStdIpSystemStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsInOctets.setStatus("current")
_FsMIStdIpSystemStatsHCInOctets_Type = Counter64
_FsMIStdIpSystemStatsHCInOctets_Object = MibTableColumn
fsMIStdIpSystemStatsHCInOctets = _FsMIStdIpSystemStatsHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 5),
    _FsMIStdIpSystemStatsHCInOctets_Type()
)
fsMIStdIpSystemStatsHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsHCInOctets.setStatus("current")
_FsMIStdIpSystemStatsInHdrErrors_Type = Counter32
_FsMIStdIpSystemStatsInHdrErrors_Object = MibTableColumn
fsMIStdIpSystemStatsInHdrErrors = _FsMIStdIpSystemStatsInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 6),
    _FsMIStdIpSystemStatsInHdrErrors_Type()
)
fsMIStdIpSystemStatsInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsInHdrErrors.setStatus("current")
_FsMIStdIpSystemStatsInNoRoutes_Type = Counter32
_FsMIStdIpSystemStatsInNoRoutes_Object = MibTableColumn
fsMIStdIpSystemStatsInNoRoutes = _FsMIStdIpSystemStatsInNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 7),
    _FsMIStdIpSystemStatsInNoRoutes_Type()
)
fsMIStdIpSystemStatsInNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsInNoRoutes.setStatus("current")
_FsMIStdIpSystemStatsInAddrErrors_Type = Counter32
_FsMIStdIpSystemStatsInAddrErrors_Object = MibTableColumn
fsMIStdIpSystemStatsInAddrErrors = _FsMIStdIpSystemStatsInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 8),
    _FsMIStdIpSystemStatsInAddrErrors_Type()
)
fsMIStdIpSystemStatsInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsInAddrErrors.setStatus("current")
_FsMIStdIpSystemStatsInUnknownProtos_Type = Counter32
_FsMIStdIpSystemStatsInUnknownProtos_Object = MibTableColumn
fsMIStdIpSystemStatsInUnknownProtos = _FsMIStdIpSystemStatsInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 9),
    _FsMIStdIpSystemStatsInUnknownProtos_Type()
)
fsMIStdIpSystemStatsInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsInUnknownProtos.setStatus("current")
_FsMIStdIpSystemStatsInTruncatedPkts_Type = Counter32
_FsMIStdIpSystemStatsInTruncatedPkts_Object = MibTableColumn
fsMIStdIpSystemStatsInTruncatedPkts = _FsMIStdIpSystemStatsInTruncatedPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 10),
    _FsMIStdIpSystemStatsInTruncatedPkts_Type()
)
fsMIStdIpSystemStatsInTruncatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsInTruncatedPkts.setStatus("current")
_FsMIStdIpSystemStatsInForwDatagrams_Type = Counter32
_FsMIStdIpSystemStatsInForwDatagrams_Object = MibTableColumn
fsMIStdIpSystemStatsInForwDatagrams = _FsMIStdIpSystemStatsInForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 11),
    _FsMIStdIpSystemStatsInForwDatagrams_Type()
)
fsMIStdIpSystemStatsInForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsInForwDatagrams.setStatus("current")
_FsMIStdIpSystemStatsHCInForwDatagrams_Type = Counter64
_FsMIStdIpSystemStatsHCInForwDatagrams_Object = MibTableColumn
fsMIStdIpSystemStatsHCInForwDatagrams = _FsMIStdIpSystemStatsHCInForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 12),
    _FsMIStdIpSystemStatsHCInForwDatagrams_Type()
)
fsMIStdIpSystemStatsHCInForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsHCInForwDatagrams.setStatus("current")
_FsMIStdIpSystemStatsReasmReqds_Type = Counter32
_FsMIStdIpSystemStatsReasmReqds_Object = MibTableColumn
fsMIStdIpSystemStatsReasmReqds = _FsMIStdIpSystemStatsReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 13),
    _FsMIStdIpSystemStatsReasmReqds_Type()
)
fsMIStdIpSystemStatsReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsReasmReqds.setStatus("current")
_FsMIStdIpSystemStatsReasmOKs_Type = Counter32
_FsMIStdIpSystemStatsReasmOKs_Object = MibTableColumn
fsMIStdIpSystemStatsReasmOKs = _FsMIStdIpSystemStatsReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 14),
    _FsMIStdIpSystemStatsReasmOKs_Type()
)
fsMIStdIpSystemStatsReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsReasmOKs.setStatus("current")
_FsMIStdIpSystemStatsReasmFails_Type = Counter32
_FsMIStdIpSystemStatsReasmFails_Object = MibTableColumn
fsMIStdIpSystemStatsReasmFails = _FsMIStdIpSystemStatsReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 15),
    _FsMIStdIpSystemStatsReasmFails_Type()
)
fsMIStdIpSystemStatsReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsReasmFails.setStatus("current")
_FsMIStdIpSystemStatsInDiscards_Type = Counter32
_FsMIStdIpSystemStatsInDiscards_Object = MibTableColumn
fsMIStdIpSystemStatsInDiscards = _FsMIStdIpSystemStatsInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 16),
    _FsMIStdIpSystemStatsInDiscards_Type()
)
fsMIStdIpSystemStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsInDiscards.setStatus("current")
_FsMIStdIpSystemStatsInDelivers_Type = Counter32
_FsMIStdIpSystemStatsInDelivers_Object = MibTableColumn
fsMIStdIpSystemStatsInDelivers = _FsMIStdIpSystemStatsInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 17),
    _FsMIStdIpSystemStatsInDelivers_Type()
)
fsMIStdIpSystemStatsInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsInDelivers.setStatus("current")
_FsMIStdIpSystemStatsHCInDelivers_Type = Counter64
_FsMIStdIpSystemStatsHCInDelivers_Object = MibTableColumn
fsMIStdIpSystemStatsHCInDelivers = _FsMIStdIpSystemStatsHCInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 18),
    _FsMIStdIpSystemStatsHCInDelivers_Type()
)
fsMIStdIpSystemStatsHCInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsHCInDelivers.setStatus("current")
_FsMIStdIpSystemStatsOutRequests_Type = Counter32
_FsMIStdIpSystemStatsOutRequests_Object = MibTableColumn
fsMIStdIpSystemStatsOutRequests = _FsMIStdIpSystemStatsOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 19),
    _FsMIStdIpSystemStatsOutRequests_Type()
)
fsMIStdIpSystemStatsOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsOutRequests.setStatus("current")
_FsMIStdIpSystemStatsHCOutRequests_Type = Counter64
_FsMIStdIpSystemStatsHCOutRequests_Object = MibTableColumn
fsMIStdIpSystemStatsHCOutRequests = _FsMIStdIpSystemStatsHCOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 20),
    _FsMIStdIpSystemStatsHCOutRequests_Type()
)
fsMIStdIpSystemStatsHCOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsHCOutRequests.setStatus("current")
_FsMIStdIpSystemStatsOutNoRoutes_Type = Counter32
_FsMIStdIpSystemStatsOutNoRoutes_Object = MibTableColumn
fsMIStdIpSystemStatsOutNoRoutes = _FsMIStdIpSystemStatsOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 21),
    _FsMIStdIpSystemStatsOutNoRoutes_Type()
)
fsMIStdIpSystemStatsOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsOutNoRoutes.setStatus("current")
_FsMIStdIpSystemStatsOutForwDatagrams_Type = Counter32
_FsMIStdIpSystemStatsOutForwDatagrams_Object = MibTableColumn
fsMIStdIpSystemStatsOutForwDatagrams = _FsMIStdIpSystemStatsOutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 22),
    _FsMIStdIpSystemStatsOutForwDatagrams_Type()
)
fsMIStdIpSystemStatsOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsOutForwDatagrams.setStatus("current")
_FsMIStdIpSystemStatsHCOutForwDatagrams_Type = Counter64
_FsMIStdIpSystemStatsHCOutForwDatagrams_Object = MibTableColumn
fsMIStdIpSystemStatsHCOutForwDatagrams = _FsMIStdIpSystemStatsHCOutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 23),
    _FsMIStdIpSystemStatsHCOutForwDatagrams_Type()
)
fsMIStdIpSystemStatsHCOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsHCOutForwDatagrams.setStatus("current")
_FsMIStdIpSystemStatsOutDiscards_Type = Counter32
_FsMIStdIpSystemStatsOutDiscards_Object = MibTableColumn
fsMIStdIpSystemStatsOutDiscards = _FsMIStdIpSystemStatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 24),
    _FsMIStdIpSystemStatsOutDiscards_Type()
)
fsMIStdIpSystemStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsOutDiscards.setStatus("current")
_FsMIStdIpSystemStatsOutFragReqds_Type = Counter32
_FsMIStdIpSystemStatsOutFragReqds_Object = MibTableColumn
fsMIStdIpSystemStatsOutFragReqds = _FsMIStdIpSystemStatsOutFragReqds_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 25),
    _FsMIStdIpSystemStatsOutFragReqds_Type()
)
fsMIStdIpSystemStatsOutFragReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsOutFragReqds.setStatus("current")
_FsMIStdIpSystemStatsOutFragOKs_Type = Counter32
_FsMIStdIpSystemStatsOutFragOKs_Object = MibTableColumn
fsMIStdIpSystemStatsOutFragOKs = _FsMIStdIpSystemStatsOutFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 26),
    _FsMIStdIpSystemStatsOutFragOKs_Type()
)
fsMIStdIpSystemStatsOutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsOutFragOKs.setStatus("current")
_FsMIStdIpSystemStatsOutFragFails_Type = Counter32
_FsMIStdIpSystemStatsOutFragFails_Object = MibTableColumn
fsMIStdIpSystemStatsOutFragFails = _FsMIStdIpSystemStatsOutFragFails_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 27),
    _FsMIStdIpSystemStatsOutFragFails_Type()
)
fsMIStdIpSystemStatsOutFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsOutFragFails.setStatus("current")
_FsMIStdIpSystemStatsOutFragCreates_Type = Counter32
_FsMIStdIpSystemStatsOutFragCreates_Object = MibTableColumn
fsMIStdIpSystemStatsOutFragCreates = _FsMIStdIpSystemStatsOutFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 28),
    _FsMIStdIpSystemStatsOutFragCreates_Type()
)
fsMIStdIpSystemStatsOutFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsOutFragCreates.setStatus("current")
_FsMIStdIpSystemStatsOutTransmits_Type = Counter32
_FsMIStdIpSystemStatsOutTransmits_Object = MibTableColumn
fsMIStdIpSystemStatsOutTransmits = _FsMIStdIpSystemStatsOutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 29),
    _FsMIStdIpSystemStatsOutTransmits_Type()
)
fsMIStdIpSystemStatsOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsOutTransmits.setStatus("current")
_FsMIStdIpSystemStatsHCOutTransmits_Type = Counter64
_FsMIStdIpSystemStatsHCOutTransmits_Object = MibTableColumn
fsMIStdIpSystemStatsHCOutTransmits = _FsMIStdIpSystemStatsHCOutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 30),
    _FsMIStdIpSystemStatsHCOutTransmits_Type()
)
fsMIStdIpSystemStatsHCOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsHCOutTransmits.setStatus("current")
_FsMIStdIpSystemStatsOutOctets_Type = Counter32
_FsMIStdIpSystemStatsOutOctets_Object = MibTableColumn
fsMIStdIpSystemStatsOutOctets = _FsMIStdIpSystemStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 31),
    _FsMIStdIpSystemStatsOutOctets_Type()
)
fsMIStdIpSystemStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsOutOctets.setStatus("current")
_FsMIStdIpSystemStatsHCOutOctets_Type = Counter64
_FsMIStdIpSystemStatsHCOutOctets_Object = MibTableColumn
fsMIStdIpSystemStatsHCOutOctets = _FsMIStdIpSystemStatsHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 32),
    _FsMIStdIpSystemStatsHCOutOctets_Type()
)
fsMIStdIpSystemStatsHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsHCOutOctets.setStatus("current")
_FsMIStdIpSystemStatsInMcastPkts_Type = Counter32
_FsMIStdIpSystemStatsInMcastPkts_Object = MibTableColumn
fsMIStdIpSystemStatsInMcastPkts = _FsMIStdIpSystemStatsInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 33),
    _FsMIStdIpSystemStatsInMcastPkts_Type()
)
fsMIStdIpSystemStatsInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsInMcastPkts.setStatus("current")
_FsMIStdIpSystemStatsHCInMcastPkts_Type = Counter64
_FsMIStdIpSystemStatsHCInMcastPkts_Object = MibTableColumn
fsMIStdIpSystemStatsHCInMcastPkts = _FsMIStdIpSystemStatsHCInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 34),
    _FsMIStdIpSystemStatsHCInMcastPkts_Type()
)
fsMIStdIpSystemStatsHCInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsHCInMcastPkts.setStatus("current")
_FsMIStdIpSystemStatsInMcastOctets_Type = Counter32
_FsMIStdIpSystemStatsInMcastOctets_Object = MibTableColumn
fsMIStdIpSystemStatsInMcastOctets = _FsMIStdIpSystemStatsInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 35),
    _FsMIStdIpSystemStatsInMcastOctets_Type()
)
fsMIStdIpSystemStatsInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsInMcastOctets.setStatus("current")
_FsMIStdIpSystemStatsHCInMcastOctets_Type = Counter64
_FsMIStdIpSystemStatsHCInMcastOctets_Object = MibTableColumn
fsMIStdIpSystemStatsHCInMcastOctets = _FsMIStdIpSystemStatsHCInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 36),
    _FsMIStdIpSystemStatsHCInMcastOctets_Type()
)
fsMIStdIpSystemStatsHCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsHCInMcastOctets.setStatus("current")
_FsMIStdIpSystemStatsOutMcastPkts_Type = Counter32
_FsMIStdIpSystemStatsOutMcastPkts_Object = MibTableColumn
fsMIStdIpSystemStatsOutMcastPkts = _FsMIStdIpSystemStatsOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 37),
    _FsMIStdIpSystemStatsOutMcastPkts_Type()
)
fsMIStdIpSystemStatsOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsOutMcastPkts.setStatus("current")
_FsMIStdIpSystemStatsHCOutMcastPkts_Type = Counter64
_FsMIStdIpSystemStatsHCOutMcastPkts_Object = MibTableColumn
fsMIStdIpSystemStatsHCOutMcastPkts = _FsMIStdIpSystemStatsHCOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 38),
    _FsMIStdIpSystemStatsHCOutMcastPkts_Type()
)
fsMIStdIpSystemStatsHCOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsHCOutMcastPkts.setStatus("current")
_FsMIStdIpSystemStatsOutMcastOctets_Type = Counter32
_FsMIStdIpSystemStatsOutMcastOctets_Object = MibTableColumn
fsMIStdIpSystemStatsOutMcastOctets = _FsMIStdIpSystemStatsOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 39),
    _FsMIStdIpSystemStatsOutMcastOctets_Type()
)
fsMIStdIpSystemStatsOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsOutMcastOctets.setStatus("current")
_FsMIStdIpSystemStatsHCOutMcastOctets_Type = Counter64
_FsMIStdIpSystemStatsHCOutMcastOctets_Object = MibTableColumn
fsMIStdIpSystemStatsHCOutMcastOctets = _FsMIStdIpSystemStatsHCOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 40),
    _FsMIStdIpSystemStatsHCOutMcastOctets_Type()
)
fsMIStdIpSystemStatsHCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsHCOutMcastOctets.setStatus("current")
_FsMIStdIpSystemStatsInBcastPkts_Type = Counter32
_FsMIStdIpSystemStatsInBcastPkts_Object = MibTableColumn
fsMIStdIpSystemStatsInBcastPkts = _FsMIStdIpSystemStatsInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 41),
    _FsMIStdIpSystemStatsInBcastPkts_Type()
)
fsMIStdIpSystemStatsInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsInBcastPkts.setStatus("current")
_FsMIStdIpSystemStatsHCInBcastPkts_Type = Counter64
_FsMIStdIpSystemStatsHCInBcastPkts_Object = MibTableColumn
fsMIStdIpSystemStatsHCInBcastPkts = _FsMIStdIpSystemStatsHCInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 42),
    _FsMIStdIpSystemStatsHCInBcastPkts_Type()
)
fsMIStdIpSystemStatsHCInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsHCInBcastPkts.setStatus("current")
_FsMIStdIpSystemStatsOutBcastPkts_Type = Counter32
_FsMIStdIpSystemStatsOutBcastPkts_Object = MibTableColumn
fsMIStdIpSystemStatsOutBcastPkts = _FsMIStdIpSystemStatsOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 43),
    _FsMIStdIpSystemStatsOutBcastPkts_Type()
)
fsMIStdIpSystemStatsOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsOutBcastPkts.setStatus("current")
_FsMIStdIpSystemStatsHCOutBcastPkts_Type = Counter64
_FsMIStdIpSystemStatsHCOutBcastPkts_Object = MibTableColumn
fsMIStdIpSystemStatsHCOutBcastPkts = _FsMIStdIpSystemStatsHCOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 44),
    _FsMIStdIpSystemStatsHCOutBcastPkts_Type()
)
fsMIStdIpSystemStatsHCOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsHCOutBcastPkts.setStatus("current")
_FsMIStdIpSystemStatsDiscontinuityTime_Type = TimeStamp
_FsMIStdIpSystemStatsDiscontinuityTime_Object = MibTableColumn
fsMIStdIpSystemStatsDiscontinuityTime = _FsMIStdIpSystemStatsDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 45),
    _FsMIStdIpSystemStatsDiscontinuityTime_Type()
)
fsMIStdIpSystemStatsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsDiscontinuityTime.setStatus("current")
_FsMIStdIpSystemStatsRefreshRate_Type = Unsigned32
_FsMIStdIpSystemStatsRefreshRate_Object = MibTableColumn
fsMIStdIpSystemStatsRefreshRate = _FsMIStdIpSystemStatsRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 7, 1, 46),
    _FsMIStdIpSystemStatsRefreshRate_Type()
)
fsMIStdIpSystemStatsRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsRefreshRate.setStatus("current")
if mibBuilder.loadTexts:
    fsMIStdIpSystemStatsRefreshRate.setUnits("milli-seconds")
_FsMIStdIpIfStatsTable_Object = MibTable
fsMIStdIpIfStatsTable = _FsMIStdIpIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8)
)
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsTable.setStatus("current")
_FsMIStdIpIfStatsEntry_Object = MibTableRow
fsMIStdIpIfStatsEntry = _FsMIStdIpIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1)
)
fsMIStdIpIfStatsEntry.setIndexNames(
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpIfStatsIPVersion"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpIfStatsIfIndex"),
)
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsEntry.setStatus("current")
_FsMIStdIpIfStatsIPVersion_Type = FsInetVersion
_FsMIStdIpIfStatsIPVersion_Object = MibTableColumn
fsMIStdIpIfStatsIPVersion = _FsMIStdIpIfStatsIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 1),
    _FsMIStdIpIfStatsIPVersion_Type()
)
fsMIStdIpIfStatsIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsIPVersion.setStatus("current")
_FsMIStdIpIfStatsIfIndex_Type = InterfaceIndex
_FsMIStdIpIfStatsIfIndex_Object = MibTableColumn
fsMIStdIpIfStatsIfIndex = _FsMIStdIpIfStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 2),
    _FsMIStdIpIfStatsIfIndex_Type()
)
fsMIStdIpIfStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsIfIndex.setStatus("current")
_FsMIStdIpIfStatsInReceives_Type = Counter32
_FsMIStdIpIfStatsInReceives_Object = MibTableColumn
fsMIStdIpIfStatsInReceives = _FsMIStdIpIfStatsInReceives_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 3),
    _FsMIStdIpIfStatsInReceives_Type()
)
fsMIStdIpIfStatsInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsInReceives.setStatus("current")
_FsMIStdIpIfStatsHCInReceives_Type = Counter64
_FsMIStdIpIfStatsHCInReceives_Object = MibTableColumn
fsMIStdIpIfStatsHCInReceives = _FsMIStdIpIfStatsHCInReceives_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 4),
    _FsMIStdIpIfStatsHCInReceives_Type()
)
fsMIStdIpIfStatsHCInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsHCInReceives.setStatus("current")
_FsMIStdIpIfStatsInOctets_Type = Counter32
_FsMIStdIpIfStatsInOctets_Object = MibTableColumn
fsMIStdIpIfStatsInOctets = _FsMIStdIpIfStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 5),
    _FsMIStdIpIfStatsInOctets_Type()
)
fsMIStdIpIfStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsInOctets.setStatus("current")
_FsMIStdIpIfStatsHCInOctets_Type = Counter64
_FsMIStdIpIfStatsHCInOctets_Object = MibTableColumn
fsMIStdIpIfStatsHCInOctets = _FsMIStdIpIfStatsHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 6),
    _FsMIStdIpIfStatsHCInOctets_Type()
)
fsMIStdIpIfStatsHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsHCInOctets.setStatus("current")
_FsMIStdIpIfStatsInHdrErrors_Type = Counter32
_FsMIStdIpIfStatsInHdrErrors_Object = MibTableColumn
fsMIStdIpIfStatsInHdrErrors = _FsMIStdIpIfStatsInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 7),
    _FsMIStdIpIfStatsInHdrErrors_Type()
)
fsMIStdIpIfStatsInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsInHdrErrors.setStatus("current")
_FsMIStdIpIfStatsInNoRoutes_Type = Counter32
_FsMIStdIpIfStatsInNoRoutes_Object = MibTableColumn
fsMIStdIpIfStatsInNoRoutes = _FsMIStdIpIfStatsInNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 8),
    _FsMIStdIpIfStatsInNoRoutes_Type()
)
fsMIStdIpIfStatsInNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsInNoRoutes.setStatus("current")
_FsMIStdIpIfStatsInAddrErrors_Type = Counter32
_FsMIStdIpIfStatsInAddrErrors_Object = MibTableColumn
fsMIStdIpIfStatsInAddrErrors = _FsMIStdIpIfStatsInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 9),
    _FsMIStdIpIfStatsInAddrErrors_Type()
)
fsMIStdIpIfStatsInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsInAddrErrors.setStatus("current")
_FsMIStdIpIfStatsInUnknownProtos_Type = Counter32
_FsMIStdIpIfStatsInUnknownProtos_Object = MibTableColumn
fsMIStdIpIfStatsInUnknownProtos = _FsMIStdIpIfStatsInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 10),
    _FsMIStdIpIfStatsInUnknownProtos_Type()
)
fsMIStdIpIfStatsInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsInUnknownProtos.setStatus("current")
_FsMIStdIpIfStatsInTruncatedPkts_Type = Counter32
_FsMIStdIpIfStatsInTruncatedPkts_Object = MibTableColumn
fsMIStdIpIfStatsInTruncatedPkts = _FsMIStdIpIfStatsInTruncatedPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 11),
    _FsMIStdIpIfStatsInTruncatedPkts_Type()
)
fsMIStdIpIfStatsInTruncatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsInTruncatedPkts.setStatus("current")
_FsMIStdIpIfStatsInForwDatagrams_Type = Counter32
_FsMIStdIpIfStatsInForwDatagrams_Object = MibTableColumn
fsMIStdIpIfStatsInForwDatagrams = _FsMIStdIpIfStatsInForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 12),
    _FsMIStdIpIfStatsInForwDatagrams_Type()
)
fsMIStdIpIfStatsInForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsInForwDatagrams.setStatus("current")
_FsMIStdIpIfStatsHCInForwDatagrams_Type = Counter64
_FsMIStdIpIfStatsHCInForwDatagrams_Object = MibTableColumn
fsMIStdIpIfStatsHCInForwDatagrams = _FsMIStdIpIfStatsHCInForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 13),
    _FsMIStdIpIfStatsHCInForwDatagrams_Type()
)
fsMIStdIpIfStatsHCInForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsHCInForwDatagrams.setStatus("current")
_FsMIStdIpIfStatsReasmReqds_Type = Counter32
_FsMIStdIpIfStatsReasmReqds_Object = MibTableColumn
fsMIStdIpIfStatsReasmReqds = _FsMIStdIpIfStatsReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 14),
    _FsMIStdIpIfStatsReasmReqds_Type()
)
fsMIStdIpIfStatsReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsReasmReqds.setStatus("current")
_FsMIStdIpIfStatsReasmOKs_Type = Counter32
_FsMIStdIpIfStatsReasmOKs_Object = MibTableColumn
fsMIStdIpIfStatsReasmOKs = _FsMIStdIpIfStatsReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 15),
    _FsMIStdIpIfStatsReasmOKs_Type()
)
fsMIStdIpIfStatsReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsReasmOKs.setStatus("current")
_FsMIStdIpIfStatsReasmFails_Type = Counter32
_FsMIStdIpIfStatsReasmFails_Object = MibTableColumn
fsMIStdIpIfStatsReasmFails = _FsMIStdIpIfStatsReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 16),
    _FsMIStdIpIfStatsReasmFails_Type()
)
fsMIStdIpIfStatsReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsReasmFails.setStatus("current")
_FsMIStdIpIfStatsInDiscards_Type = Counter32
_FsMIStdIpIfStatsInDiscards_Object = MibTableColumn
fsMIStdIpIfStatsInDiscards = _FsMIStdIpIfStatsInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 17),
    _FsMIStdIpIfStatsInDiscards_Type()
)
fsMIStdIpIfStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsInDiscards.setStatus("current")
_FsMIStdIpIfStatsInDelivers_Type = Counter32
_FsMIStdIpIfStatsInDelivers_Object = MibTableColumn
fsMIStdIpIfStatsInDelivers = _FsMIStdIpIfStatsInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 18),
    _FsMIStdIpIfStatsInDelivers_Type()
)
fsMIStdIpIfStatsInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsInDelivers.setStatus("current")
_FsMIStdIpIfStatsHCInDelivers_Type = Counter64
_FsMIStdIpIfStatsHCInDelivers_Object = MibTableColumn
fsMIStdIpIfStatsHCInDelivers = _FsMIStdIpIfStatsHCInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 19),
    _FsMIStdIpIfStatsHCInDelivers_Type()
)
fsMIStdIpIfStatsHCInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsHCInDelivers.setStatus("current")
_FsMIStdIpIfStatsOutRequests_Type = Counter32
_FsMIStdIpIfStatsOutRequests_Object = MibTableColumn
fsMIStdIpIfStatsOutRequests = _FsMIStdIpIfStatsOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 20),
    _FsMIStdIpIfStatsOutRequests_Type()
)
fsMIStdIpIfStatsOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsOutRequests.setStatus("current")
_FsMIStdIpIfStatsHCOutRequests_Type = Counter64
_FsMIStdIpIfStatsHCOutRequests_Object = MibTableColumn
fsMIStdIpIfStatsHCOutRequests = _FsMIStdIpIfStatsHCOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 21),
    _FsMIStdIpIfStatsHCOutRequests_Type()
)
fsMIStdIpIfStatsHCOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsHCOutRequests.setStatus("current")
_FsMIStdIpIfStatsOutForwDatagrams_Type = Counter32
_FsMIStdIpIfStatsOutForwDatagrams_Object = MibTableColumn
fsMIStdIpIfStatsOutForwDatagrams = _FsMIStdIpIfStatsOutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 22),
    _FsMIStdIpIfStatsOutForwDatagrams_Type()
)
fsMIStdIpIfStatsOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsOutForwDatagrams.setStatus("current")
_FsMIStdIpIfStatsHCOutForwDatagrams_Type = Counter64
_FsMIStdIpIfStatsHCOutForwDatagrams_Object = MibTableColumn
fsMIStdIpIfStatsHCOutForwDatagrams = _FsMIStdIpIfStatsHCOutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 23),
    _FsMIStdIpIfStatsHCOutForwDatagrams_Type()
)
fsMIStdIpIfStatsHCOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsHCOutForwDatagrams.setStatus("current")
_FsMIStdIpIfStatsOutDiscards_Type = Counter32
_FsMIStdIpIfStatsOutDiscards_Object = MibTableColumn
fsMIStdIpIfStatsOutDiscards = _FsMIStdIpIfStatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 24),
    _FsMIStdIpIfStatsOutDiscards_Type()
)
fsMIStdIpIfStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsOutDiscards.setStatus("current")
_FsMIStdIpIfStatsOutFragReqds_Type = Counter32
_FsMIStdIpIfStatsOutFragReqds_Object = MibTableColumn
fsMIStdIpIfStatsOutFragReqds = _FsMIStdIpIfStatsOutFragReqds_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 25),
    _FsMIStdIpIfStatsOutFragReqds_Type()
)
fsMIStdIpIfStatsOutFragReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsOutFragReqds.setStatus("current")
_FsMIStdIpIfStatsOutFragOKs_Type = Counter32
_FsMIStdIpIfStatsOutFragOKs_Object = MibTableColumn
fsMIStdIpIfStatsOutFragOKs = _FsMIStdIpIfStatsOutFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 26),
    _FsMIStdIpIfStatsOutFragOKs_Type()
)
fsMIStdIpIfStatsOutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsOutFragOKs.setStatus("current")
_FsMIStdIpIfStatsOutFragFails_Type = Counter32
_FsMIStdIpIfStatsOutFragFails_Object = MibTableColumn
fsMIStdIpIfStatsOutFragFails = _FsMIStdIpIfStatsOutFragFails_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 27),
    _FsMIStdIpIfStatsOutFragFails_Type()
)
fsMIStdIpIfStatsOutFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsOutFragFails.setStatus("current")
_FsMIStdIpIfStatsOutFragCreates_Type = Counter32
_FsMIStdIpIfStatsOutFragCreates_Object = MibTableColumn
fsMIStdIpIfStatsOutFragCreates = _FsMIStdIpIfStatsOutFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 28),
    _FsMIStdIpIfStatsOutFragCreates_Type()
)
fsMIStdIpIfStatsOutFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsOutFragCreates.setStatus("current")
_FsMIStdIpIfStatsOutTransmits_Type = Counter32
_FsMIStdIpIfStatsOutTransmits_Object = MibTableColumn
fsMIStdIpIfStatsOutTransmits = _FsMIStdIpIfStatsOutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 29),
    _FsMIStdIpIfStatsOutTransmits_Type()
)
fsMIStdIpIfStatsOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsOutTransmits.setStatus("current")
_FsMIStdIpIfStatsHCOutTransmits_Type = Counter64
_FsMIStdIpIfStatsHCOutTransmits_Object = MibTableColumn
fsMIStdIpIfStatsHCOutTransmits = _FsMIStdIpIfStatsHCOutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 30),
    _FsMIStdIpIfStatsHCOutTransmits_Type()
)
fsMIStdIpIfStatsHCOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsHCOutTransmits.setStatus("current")
_FsMIStdIpIfStatsOutOctets_Type = Counter32
_FsMIStdIpIfStatsOutOctets_Object = MibTableColumn
fsMIStdIpIfStatsOutOctets = _FsMIStdIpIfStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 31),
    _FsMIStdIpIfStatsOutOctets_Type()
)
fsMIStdIpIfStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsOutOctets.setStatus("current")
_FsMIStdIpIfStatsHCOutOctets_Type = Counter64
_FsMIStdIpIfStatsHCOutOctets_Object = MibTableColumn
fsMIStdIpIfStatsHCOutOctets = _FsMIStdIpIfStatsHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 32),
    _FsMIStdIpIfStatsHCOutOctets_Type()
)
fsMIStdIpIfStatsHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsHCOutOctets.setStatus("current")
_FsMIStdIpIfStatsInMcastPkts_Type = Counter32
_FsMIStdIpIfStatsInMcastPkts_Object = MibTableColumn
fsMIStdIpIfStatsInMcastPkts = _FsMIStdIpIfStatsInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 33),
    _FsMIStdIpIfStatsInMcastPkts_Type()
)
fsMIStdIpIfStatsInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsInMcastPkts.setStatus("current")
_FsMIStdIpIfStatsHCInMcastPkts_Type = Counter64
_FsMIStdIpIfStatsHCInMcastPkts_Object = MibTableColumn
fsMIStdIpIfStatsHCInMcastPkts = _FsMIStdIpIfStatsHCInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 34),
    _FsMIStdIpIfStatsHCInMcastPkts_Type()
)
fsMIStdIpIfStatsHCInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsHCInMcastPkts.setStatus("current")
_FsMIStdIpIfStatsInMcastOctets_Type = Counter32
_FsMIStdIpIfStatsInMcastOctets_Object = MibTableColumn
fsMIStdIpIfStatsInMcastOctets = _FsMIStdIpIfStatsInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 35),
    _FsMIStdIpIfStatsInMcastOctets_Type()
)
fsMIStdIpIfStatsInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsInMcastOctets.setStatus("current")
_FsMIStdIpIfStatsHCInMcastOctets_Type = Counter64
_FsMIStdIpIfStatsHCInMcastOctets_Object = MibTableColumn
fsMIStdIpIfStatsHCInMcastOctets = _FsMIStdIpIfStatsHCInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 36),
    _FsMIStdIpIfStatsHCInMcastOctets_Type()
)
fsMIStdIpIfStatsHCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsHCInMcastOctets.setStatus("current")
_FsMIStdIpIfStatsOutMcastPkts_Type = Counter32
_FsMIStdIpIfStatsOutMcastPkts_Object = MibTableColumn
fsMIStdIpIfStatsOutMcastPkts = _FsMIStdIpIfStatsOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 37),
    _FsMIStdIpIfStatsOutMcastPkts_Type()
)
fsMIStdIpIfStatsOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsOutMcastPkts.setStatus("current")
_FsMIStdIpIfStatsHCOutMcastPkts_Type = Counter64
_FsMIStdIpIfStatsHCOutMcastPkts_Object = MibTableColumn
fsMIStdIpIfStatsHCOutMcastPkts = _FsMIStdIpIfStatsHCOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 38),
    _FsMIStdIpIfStatsHCOutMcastPkts_Type()
)
fsMIStdIpIfStatsHCOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsHCOutMcastPkts.setStatus("current")
_FsMIStdIpIfStatsOutMcastOctets_Type = Counter32
_FsMIStdIpIfStatsOutMcastOctets_Object = MibTableColumn
fsMIStdIpIfStatsOutMcastOctets = _FsMIStdIpIfStatsOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 39),
    _FsMIStdIpIfStatsOutMcastOctets_Type()
)
fsMIStdIpIfStatsOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsOutMcastOctets.setStatus("current")
_FsMIStdIpIfStatsHCOutMcastOctets_Type = Counter64
_FsMIStdIpIfStatsHCOutMcastOctets_Object = MibTableColumn
fsMIStdIpIfStatsHCOutMcastOctets = _FsMIStdIpIfStatsHCOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 40),
    _FsMIStdIpIfStatsHCOutMcastOctets_Type()
)
fsMIStdIpIfStatsHCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsHCOutMcastOctets.setStatus("current")
_FsMIStdIpIfStatsInBcastPkts_Type = Counter32
_FsMIStdIpIfStatsInBcastPkts_Object = MibTableColumn
fsMIStdIpIfStatsInBcastPkts = _FsMIStdIpIfStatsInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 41),
    _FsMIStdIpIfStatsInBcastPkts_Type()
)
fsMIStdIpIfStatsInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsInBcastPkts.setStatus("current")
_FsMIStdIpIfStatsHCInBcastPkts_Type = Counter64
_FsMIStdIpIfStatsHCInBcastPkts_Object = MibTableColumn
fsMIStdIpIfStatsHCInBcastPkts = _FsMIStdIpIfStatsHCInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 42),
    _FsMIStdIpIfStatsHCInBcastPkts_Type()
)
fsMIStdIpIfStatsHCInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsHCInBcastPkts.setStatus("current")
_FsMIStdIpIfStatsOutBcastPkts_Type = Counter32
_FsMIStdIpIfStatsOutBcastPkts_Object = MibTableColumn
fsMIStdIpIfStatsOutBcastPkts = _FsMIStdIpIfStatsOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 43),
    _FsMIStdIpIfStatsOutBcastPkts_Type()
)
fsMIStdIpIfStatsOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsOutBcastPkts.setStatus("current")
_FsMIStdIpIfStatsHCOutBcastPkts_Type = Counter64
_FsMIStdIpIfStatsHCOutBcastPkts_Object = MibTableColumn
fsMIStdIpIfStatsHCOutBcastPkts = _FsMIStdIpIfStatsHCOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 44),
    _FsMIStdIpIfStatsHCOutBcastPkts_Type()
)
fsMIStdIpIfStatsHCOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsHCOutBcastPkts.setStatus("current")
_FsMIStdIpIfStatsDiscontinuityTime_Type = TimeStamp
_FsMIStdIpIfStatsDiscontinuityTime_Object = MibTableColumn
fsMIStdIpIfStatsDiscontinuityTime = _FsMIStdIpIfStatsDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 45),
    _FsMIStdIpIfStatsDiscontinuityTime_Type()
)
fsMIStdIpIfStatsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsDiscontinuityTime.setStatus("current")
_FsMIStdIpIfStatsRefreshRate_Type = Unsigned32
_FsMIStdIpIfStatsRefreshRate_Object = MibTableColumn
fsMIStdIpIfStatsRefreshRate = _FsMIStdIpIfStatsRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 47),
    _FsMIStdIpIfStatsRefreshRate_Type()
)
fsMIStdIpIfStatsRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsRefreshRate.setStatus("current")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsRefreshRate.setUnits("milli-seconds")
_FsMIStdIpIfStatsContextId_Type = Integer32
_FsMIStdIpIfStatsContextId_Object = MibTableColumn
fsMIStdIpIfStatsContextId = _FsMIStdIpIfStatsContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 8, 1, 48),
    _FsMIStdIpIfStatsContextId_Type()
)
fsMIStdIpIfStatsContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpIfStatsContextId.setStatus("current")
_FsMIStdIpAddressPrefixTable_Object = MibTable
fsMIStdIpAddressPrefixTable = _FsMIStdIpAddressPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 9)
)
if mibBuilder.loadTexts:
    fsMIStdIpAddressPrefixTable.setStatus("current")
_FsMIStdIpAddressPrefixEntry_Object = MibTableRow
fsMIStdIpAddressPrefixEntry = _FsMIStdIpAddressPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 9, 1)
)
fsMIStdIpAddressPrefixEntry.setIndexNames(
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpAddressPrefixIfIndex"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpAddressPrefixType"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpAddressPrefixPrefix"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpAddressPrefixLength"),
)
if mibBuilder.loadTexts:
    fsMIStdIpAddressPrefixEntry.setStatus("current")
_FsMIStdIpAddressPrefixIfIndex_Type = InterfaceIndex
_FsMIStdIpAddressPrefixIfIndex_Object = MibTableColumn
fsMIStdIpAddressPrefixIfIndex = _FsMIStdIpAddressPrefixIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 9, 1, 1),
    _FsMIStdIpAddressPrefixIfIndex_Type()
)
fsMIStdIpAddressPrefixIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpAddressPrefixIfIndex.setStatus("current")
_FsMIStdIpAddressPrefixType_Type = InetAddressType
_FsMIStdIpAddressPrefixType_Object = MibTableColumn
fsMIStdIpAddressPrefixType = _FsMIStdIpAddressPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 9, 1, 2),
    _FsMIStdIpAddressPrefixType_Type()
)
fsMIStdIpAddressPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpAddressPrefixType.setStatus("current")


class _FsMIStdIpAddressPrefixPrefix_Type(InetAddress):
    """Custom type fsMIStdIpAddressPrefixPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIStdIpAddressPrefixPrefix_Type.__name__ = "InetAddress"
_FsMIStdIpAddressPrefixPrefix_Object = MibTableColumn
fsMIStdIpAddressPrefixPrefix = _FsMIStdIpAddressPrefixPrefix_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 9, 1, 3),
    _FsMIStdIpAddressPrefixPrefix_Type()
)
fsMIStdIpAddressPrefixPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpAddressPrefixPrefix.setStatus("current")
_FsMIStdIpAddressPrefixLength_Type = InetAddressPrefixLength
_FsMIStdIpAddressPrefixLength_Object = MibTableColumn
fsMIStdIpAddressPrefixLength = _FsMIStdIpAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 9, 1, 4),
    _FsMIStdIpAddressPrefixLength_Type()
)
fsMIStdIpAddressPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpAddressPrefixLength.setStatus("current")
_FsMIStdIpAddressPrefixOrigin_Type = IpAddressPrefixOriginTC
_FsMIStdIpAddressPrefixOrigin_Object = MibTableColumn
fsMIStdIpAddressPrefixOrigin = _FsMIStdIpAddressPrefixOrigin_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 9, 1, 5),
    _FsMIStdIpAddressPrefixOrigin_Type()
)
fsMIStdIpAddressPrefixOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpAddressPrefixOrigin.setStatus("current")
_FsMIStdIpAddressPrefixOnLinkFlag_Type = TruthValue
_FsMIStdIpAddressPrefixOnLinkFlag_Object = MibTableColumn
fsMIStdIpAddressPrefixOnLinkFlag = _FsMIStdIpAddressPrefixOnLinkFlag_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 9, 1, 6),
    _FsMIStdIpAddressPrefixOnLinkFlag_Type()
)
fsMIStdIpAddressPrefixOnLinkFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpAddressPrefixOnLinkFlag.setStatus("current")
_FsMIStdIpAddressPrefixAutonomousFlag_Type = TruthValue
_FsMIStdIpAddressPrefixAutonomousFlag_Object = MibTableColumn
fsMIStdIpAddressPrefixAutonomousFlag = _FsMIStdIpAddressPrefixAutonomousFlag_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 9, 1, 7),
    _FsMIStdIpAddressPrefixAutonomousFlag_Type()
)
fsMIStdIpAddressPrefixAutonomousFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpAddressPrefixAutonomousFlag.setStatus("current")
_FsMIStdIpAddressPrefixAdvPreferredLifetime_Type = Unsigned32
_FsMIStdIpAddressPrefixAdvPreferredLifetime_Object = MibTableColumn
fsMIStdIpAddressPrefixAdvPreferredLifetime = _FsMIStdIpAddressPrefixAdvPreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 9, 1, 8),
    _FsMIStdIpAddressPrefixAdvPreferredLifetime_Type()
)
fsMIStdIpAddressPrefixAdvPreferredLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpAddressPrefixAdvPreferredLifetime.setStatus("current")
if mibBuilder.loadTexts:
    fsMIStdIpAddressPrefixAdvPreferredLifetime.setUnits("seconds")
_FsMIStdIpAddressPrefixAdvValidLifetime_Type = Unsigned32
_FsMIStdIpAddressPrefixAdvValidLifetime_Object = MibTableColumn
fsMIStdIpAddressPrefixAdvValidLifetime = _FsMIStdIpAddressPrefixAdvValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 9, 1, 9),
    _FsMIStdIpAddressPrefixAdvValidLifetime_Type()
)
fsMIStdIpAddressPrefixAdvValidLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpAddressPrefixAdvValidLifetime.setStatus("current")
if mibBuilder.loadTexts:
    fsMIStdIpAddressPrefixAdvValidLifetime.setUnits("seconds")
_FsMIStdIpAddressContextId_Type = Integer32
_FsMIStdIpAddressContextId_Object = MibTableColumn
fsMIStdIpAddressContextId = _FsMIStdIpAddressContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 9, 1, 10),
    _FsMIStdIpAddressContextId_Type()
)
fsMIStdIpAddressContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpAddressContextId.setStatus("current")
_FsMIStdIpAddressTable_Object = MibTable
fsMIStdIpAddressTable = _FsMIStdIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 10)
)
if mibBuilder.loadTexts:
    fsMIStdIpAddressTable.setStatus("current")
_FsMIStdIpAddressEntry_Object = MibTableRow
fsMIStdIpAddressEntry = _FsMIStdIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 10, 1)
)
fsMIStdIpAddressEntry.setIndexNames(
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpAddressAddrType"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpAddressAddr"),
)
if mibBuilder.loadTexts:
    fsMIStdIpAddressEntry.setStatus("current")
_FsMIStdIpAddressAddrType_Type = InetAddressType
_FsMIStdIpAddressAddrType_Object = MibTableColumn
fsMIStdIpAddressAddrType = _FsMIStdIpAddressAddrType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 10, 1, 2),
    _FsMIStdIpAddressAddrType_Type()
)
fsMIStdIpAddressAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpAddressAddrType.setStatus("current")


class _FsMIStdIpAddressAddr_Type(InetAddress):
    """Custom type fsMIStdIpAddressAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIStdIpAddressAddr_Type.__name__ = "InetAddress"
_FsMIStdIpAddressAddr_Object = MibTableColumn
fsMIStdIpAddressAddr = _FsMIStdIpAddressAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 10, 1, 3),
    _FsMIStdIpAddressAddr_Type()
)
fsMIStdIpAddressAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpAddressAddr.setStatus("current")
_FsMIStdIpAddressIfIndex_Type = InterfaceIndex
_FsMIStdIpAddressIfIndex_Object = MibTableColumn
fsMIStdIpAddressIfIndex = _FsMIStdIpAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 10, 1, 4),
    _FsMIStdIpAddressIfIndex_Type()
)
fsMIStdIpAddressIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpAddressIfIndex.setStatus("current")


class _FsMIStdIpAddressType_Type(Integer32):
    """Custom type fsMIStdIpAddressType based on Integer32"""
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
        *(("unicast", 1),
          ("anycast", 2),
          ("broadcast", 3))
    )


_FsMIStdIpAddressType_Type.__name__ = "Integer32"
_FsMIStdIpAddressType_Object = MibTableColumn
fsMIStdIpAddressType = _FsMIStdIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 10, 1, 5),
    _FsMIStdIpAddressType_Type()
)
fsMIStdIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpAddressType.setStatus("current")
_FsMIStdIpAddressPrefix_Type = RowPointer
_FsMIStdIpAddressPrefix_Object = MibTableColumn
fsMIStdIpAddressPrefix = _FsMIStdIpAddressPrefix_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 10, 1, 6),
    _FsMIStdIpAddressPrefix_Type()
)
fsMIStdIpAddressPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpAddressPrefix.setStatus("current")
_FsMIStdIpAddressOrigin_Type = IpAddressOriginTC
_FsMIStdIpAddressOrigin_Object = MibTableColumn
fsMIStdIpAddressOrigin = _FsMIStdIpAddressOrigin_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 10, 1, 7),
    _FsMIStdIpAddressOrigin_Type()
)
fsMIStdIpAddressOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpAddressOrigin.setStatus("current")
_FsMIStdIpAddressStatus_Type = IpAddressStatusTC
_FsMIStdIpAddressStatus_Object = MibTableColumn
fsMIStdIpAddressStatus = _FsMIStdIpAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 10, 1, 8),
    _FsMIStdIpAddressStatus_Type()
)
fsMIStdIpAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpAddressStatus.setStatus("current")
_FsMIStdIpAddressCreated_Type = TimeStamp
_FsMIStdIpAddressCreated_Object = MibTableColumn
fsMIStdIpAddressCreated = _FsMIStdIpAddressCreated_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 10, 1, 9),
    _FsMIStdIpAddressCreated_Type()
)
fsMIStdIpAddressCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpAddressCreated.setStatus("current")
_FsMIStdIpAddressLastChanged_Type = TimeStamp
_FsMIStdIpAddressLastChanged_Object = MibTableColumn
fsMIStdIpAddressLastChanged = _FsMIStdIpAddressLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 10, 1, 10),
    _FsMIStdIpAddressLastChanged_Type()
)
fsMIStdIpAddressLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpAddressLastChanged.setStatus("current")
_FsMIStdIpAddressRowStatus_Type = RowStatus
_FsMIStdIpAddressRowStatus_Object = MibTableColumn
fsMIStdIpAddressRowStatus = _FsMIStdIpAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 10, 1, 11),
    _FsMIStdIpAddressRowStatus_Type()
)
fsMIStdIpAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpAddressRowStatus.setStatus("current")


class _FsMIStdIpAddressStorageType_Type(StorageType):
    """Custom type fsMIStdIpAddressStorageType based on StorageType"""
    defaultValue = 2


_FsMIStdIpAddressStorageType_Type.__name__ = "StorageType"
_FsMIStdIpAddressStorageType_Object = MibTableColumn
fsMIStdIpAddressStorageType = _FsMIStdIpAddressStorageType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 10, 1, 12),
    _FsMIStdIpAddressStorageType_Type()
)
fsMIStdIpAddressStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpAddressStorageType.setStatus("current")
_FsMIStdIpNetToPhysicalTable_Object = MibTable
fsMIStdIpNetToPhysicalTable = _FsMIStdIpNetToPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 11)
)
if mibBuilder.loadTexts:
    fsMIStdIpNetToPhysicalTable.setStatus("current")
_FsMIStdIpNetToPhysicalEntry_Object = MibTableRow
fsMIStdIpNetToPhysicalEntry = _FsMIStdIpNetToPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 11, 1)
)
fsMIStdIpNetToPhysicalEntry.setIndexNames(
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpNetToPhysicalIfIndex"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpNetToPhysicalNetAddressType"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpNetToPhysicalNetAddress"),
)
if mibBuilder.loadTexts:
    fsMIStdIpNetToPhysicalEntry.setStatus("current")
_FsMIStdIpNetToPhysicalIfIndex_Type = InterfaceIndex
_FsMIStdIpNetToPhysicalIfIndex_Object = MibTableColumn
fsMIStdIpNetToPhysicalIfIndex = _FsMIStdIpNetToPhysicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 11, 1, 1),
    _FsMIStdIpNetToPhysicalIfIndex_Type()
)
fsMIStdIpNetToPhysicalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpNetToPhysicalIfIndex.setStatus("current")
_FsMIStdIpNetToPhysicalNetAddressType_Type = InetAddressType
_FsMIStdIpNetToPhysicalNetAddressType_Object = MibTableColumn
fsMIStdIpNetToPhysicalNetAddressType = _FsMIStdIpNetToPhysicalNetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 11, 1, 2),
    _FsMIStdIpNetToPhysicalNetAddressType_Type()
)
fsMIStdIpNetToPhysicalNetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpNetToPhysicalNetAddressType.setStatus("current")


class _FsMIStdIpNetToPhysicalNetAddress_Type(InetAddress):
    """Custom type fsMIStdIpNetToPhysicalNetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIStdIpNetToPhysicalNetAddress_Type.__name__ = "InetAddress"
_FsMIStdIpNetToPhysicalNetAddress_Object = MibTableColumn
fsMIStdIpNetToPhysicalNetAddress = _FsMIStdIpNetToPhysicalNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 11, 1, 3),
    _FsMIStdIpNetToPhysicalNetAddress_Type()
)
fsMIStdIpNetToPhysicalNetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpNetToPhysicalNetAddress.setStatus("current")


class _FsMIStdIpNetToPhysicalPhysAddress_Type(PhysAddress):
    """Custom type fsMIStdIpNetToPhysicalPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_FsMIStdIpNetToPhysicalPhysAddress_Type.__name__ = "PhysAddress"
_FsMIStdIpNetToPhysicalPhysAddress_Object = MibTableColumn
fsMIStdIpNetToPhysicalPhysAddress = _FsMIStdIpNetToPhysicalPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 11, 1, 4),
    _FsMIStdIpNetToPhysicalPhysAddress_Type()
)
fsMIStdIpNetToPhysicalPhysAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpNetToPhysicalPhysAddress.setStatus("current")
_FsMIStdIpNetToPhysicalLastUpdated_Type = TimeStamp
_FsMIStdIpNetToPhysicalLastUpdated_Object = MibTableColumn
fsMIStdIpNetToPhysicalLastUpdated = _FsMIStdIpNetToPhysicalLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 11, 1, 5),
    _FsMIStdIpNetToPhysicalLastUpdated_Type()
)
fsMIStdIpNetToPhysicalLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpNetToPhysicalLastUpdated.setStatus("current")


class _FsMIStdIpNetToPhysicalType_Type(Integer32):
    """Custom type fsMIStdIpNetToPhysicalType based on Integer32"""
    defaultValue = 4

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
        *(("other", 1),
          ("invalid", 2),
          ("dynamic", 3),
          ("static", 4),
          ("local", 5))
    )


_FsMIStdIpNetToPhysicalType_Type.__name__ = "Integer32"
_FsMIStdIpNetToPhysicalType_Object = MibTableColumn
fsMIStdIpNetToPhysicalType = _FsMIStdIpNetToPhysicalType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 11, 1, 6),
    _FsMIStdIpNetToPhysicalType_Type()
)
fsMIStdIpNetToPhysicalType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpNetToPhysicalType.setStatus("current")


class _FsMIStdIpNetToPhysicalState_Type(Integer32):
    """Custom type fsMIStdIpNetToPhysicalState based on Integer32"""
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
        *(("reachable", 1),
          ("stale", 2),
          ("delay", 3),
          ("probe", 4),
          ("invalid", 5),
          ("unknown", 6),
          ("incomplete", 7))
    )


_FsMIStdIpNetToPhysicalState_Type.__name__ = "Integer32"
_FsMIStdIpNetToPhysicalState_Object = MibTableColumn
fsMIStdIpNetToPhysicalState = _FsMIStdIpNetToPhysicalState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 11, 1, 7),
    _FsMIStdIpNetToPhysicalState_Type()
)
fsMIStdIpNetToPhysicalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpNetToPhysicalState.setStatus("current")
_FsMIStdIpNetToPhysicalRowStatus_Type = RowStatus
_FsMIStdIpNetToPhysicalRowStatus_Object = MibTableColumn
fsMIStdIpNetToPhysicalRowStatus = _FsMIStdIpNetToPhysicalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 11, 1, 8),
    _FsMIStdIpNetToPhysicalRowStatus_Type()
)
fsMIStdIpNetToPhysicalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpNetToPhysicalRowStatus.setStatus("current")
_FsMIStdIpNetToPhysicalContextId_Type = Integer32
_FsMIStdIpNetToPhysicalContextId_Object = MibTableColumn
fsMIStdIpNetToPhysicalContextId = _FsMIStdIpNetToPhysicalContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 11, 1, 9),
    _FsMIStdIpNetToPhysicalContextId_Type()
)
fsMIStdIpNetToPhysicalContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpNetToPhysicalContextId.setStatus("current")
_FsMIStdIpv6ScopeZoneIndexTable_Object = MibTable
fsMIStdIpv6ScopeZoneIndexTable = _FsMIStdIpv6ScopeZoneIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 12)
)
if mibBuilder.loadTexts:
    fsMIStdIpv6ScopeZoneIndexTable.setStatus("current")
_FsMIStdIpv6ScopeZoneIndexEntry_Object = MibTableRow
fsMIStdIpv6ScopeZoneIndexEntry = _FsMIStdIpv6ScopeZoneIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 12, 1)
)
fsMIStdIpv6ScopeZoneIndexEntry.setIndexNames(
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpv6ScopeZoneIndexIfIndex"),
)
if mibBuilder.loadTexts:
    fsMIStdIpv6ScopeZoneIndexEntry.setStatus("current")
_FsMIStdIpv6ScopeZoneIndexIfIndex_Type = InterfaceIndex
_FsMIStdIpv6ScopeZoneIndexIfIndex_Object = MibTableColumn
fsMIStdIpv6ScopeZoneIndexIfIndex = _FsMIStdIpv6ScopeZoneIndexIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 12, 1, 1),
    _FsMIStdIpv6ScopeZoneIndexIfIndex_Type()
)
fsMIStdIpv6ScopeZoneIndexIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpv6ScopeZoneIndexIfIndex.setStatus("current")
_FsMIStdIpv6ScopeZoneIndexLinkLocal_Type = InetZoneIndex
_FsMIStdIpv6ScopeZoneIndexLinkLocal_Object = MibTableColumn
fsMIStdIpv6ScopeZoneIndexLinkLocal = _FsMIStdIpv6ScopeZoneIndexLinkLocal_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 12, 1, 2),
    _FsMIStdIpv6ScopeZoneIndexLinkLocal_Type()
)
fsMIStdIpv6ScopeZoneIndexLinkLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6ScopeZoneIndexLinkLocal.setStatus("current")
_FsMIStdIpv6ScopeZoneIndex3_Type = InetZoneIndex
_FsMIStdIpv6ScopeZoneIndex3_Object = MibTableColumn
fsMIStdIpv6ScopeZoneIndex3 = _FsMIStdIpv6ScopeZoneIndex3_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 12, 1, 3),
    _FsMIStdIpv6ScopeZoneIndex3_Type()
)
fsMIStdIpv6ScopeZoneIndex3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6ScopeZoneIndex3.setStatus("current")
_FsMIStdIpv6ScopeZoneIndexAdminLocal_Type = InetZoneIndex
_FsMIStdIpv6ScopeZoneIndexAdminLocal_Object = MibTableColumn
fsMIStdIpv6ScopeZoneIndexAdminLocal = _FsMIStdIpv6ScopeZoneIndexAdminLocal_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 12, 1, 4),
    _FsMIStdIpv6ScopeZoneIndexAdminLocal_Type()
)
fsMIStdIpv6ScopeZoneIndexAdminLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6ScopeZoneIndexAdminLocal.setStatus("current")
_FsMIStdIpv6ScopeZoneIndexSiteLocal_Type = InetZoneIndex
_FsMIStdIpv6ScopeZoneIndexSiteLocal_Object = MibTableColumn
fsMIStdIpv6ScopeZoneIndexSiteLocal = _FsMIStdIpv6ScopeZoneIndexSiteLocal_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 12, 1, 5),
    _FsMIStdIpv6ScopeZoneIndexSiteLocal_Type()
)
fsMIStdIpv6ScopeZoneIndexSiteLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6ScopeZoneIndexSiteLocal.setStatus("current")
_FsMIStdIpv6ScopeZoneIndex6_Type = InetZoneIndex
_FsMIStdIpv6ScopeZoneIndex6_Object = MibTableColumn
fsMIStdIpv6ScopeZoneIndex6 = _FsMIStdIpv6ScopeZoneIndex6_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 12, 1, 6),
    _FsMIStdIpv6ScopeZoneIndex6_Type()
)
fsMIStdIpv6ScopeZoneIndex6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6ScopeZoneIndex6.setStatus("current")
_FsMIStdIpv6ScopeZoneIndex7_Type = InetZoneIndex
_FsMIStdIpv6ScopeZoneIndex7_Object = MibTableColumn
fsMIStdIpv6ScopeZoneIndex7 = _FsMIStdIpv6ScopeZoneIndex7_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 12, 1, 7),
    _FsMIStdIpv6ScopeZoneIndex7_Type()
)
fsMIStdIpv6ScopeZoneIndex7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6ScopeZoneIndex7.setStatus("current")
_FsMIStdIpv6ScopeZoneIndexOrganizationLocal_Type = InetZoneIndex
_FsMIStdIpv6ScopeZoneIndexOrganizationLocal_Object = MibTableColumn
fsMIStdIpv6ScopeZoneIndexOrganizationLocal = _FsMIStdIpv6ScopeZoneIndexOrganizationLocal_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 12, 1, 8),
    _FsMIStdIpv6ScopeZoneIndexOrganizationLocal_Type()
)
fsMIStdIpv6ScopeZoneIndexOrganizationLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6ScopeZoneIndexOrganizationLocal.setStatus("current")
_FsMIStdIpv6ScopeZoneIndex9_Type = InetZoneIndex
_FsMIStdIpv6ScopeZoneIndex9_Object = MibTableColumn
fsMIStdIpv6ScopeZoneIndex9 = _FsMIStdIpv6ScopeZoneIndex9_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 12, 1, 9),
    _FsMIStdIpv6ScopeZoneIndex9_Type()
)
fsMIStdIpv6ScopeZoneIndex9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6ScopeZoneIndex9.setStatus("current")
_FsMIStdIpv6ScopeZoneIndexA_Type = InetZoneIndex
_FsMIStdIpv6ScopeZoneIndexA_Object = MibTableColumn
fsMIStdIpv6ScopeZoneIndexA = _FsMIStdIpv6ScopeZoneIndexA_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 12, 1, 10),
    _FsMIStdIpv6ScopeZoneIndexA_Type()
)
fsMIStdIpv6ScopeZoneIndexA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6ScopeZoneIndexA.setStatus("current")
_FsMIStdIpv6ScopeZoneIndexB_Type = InetZoneIndex
_FsMIStdIpv6ScopeZoneIndexB_Object = MibTableColumn
fsMIStdIpv6ScopeZoneIndexB = _FsMIStdIpv6ScopeZoneIndexB_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 12, 1, 11),
    _FsMIStdIpv6ScopeZoneIndexB_Type()
)
fsMIStdIpv6ScopeZoneIndexB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6ScopeZoneIndexB.setStatus("current")
_FsMIStdIpv6ScopeZoneIndexC_Type = InetZoneIndex
_FsMIStdIpv6ScopeZoneIndexC_Object = MibTableColumn
fsMIStdIpv6ScopeZoneIndexC = _FsMIStdIpv6ScopeZoneIndexC_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 12, 1, 12),
    _FsMIStdIpv6ScopeZoneIndexC_Type()
)
fsMIStdIpv6ScopeZoneIndexC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6ScopeZoneIndexC.setStatus("current")
_FsMIStdIpv6ScopeZoneIndexD_Type = InetZoneIndex
_FsMIStdIpv6ScopeZoneIndexD_Object = MibTableColumn
fsMIStdIpv6ScopeZoneIndexD = _FsMIStdIpv6ScopeZoneIndexD_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 12, 1, 13),
    _FsMIStdIpv6ScopeZoneIndexD_Type()
)
fsMIStdIpv6ScopeZoneIndexD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6ScopeZoneIndexD.setStatus("current")
_FsMIStdIpv6ScopeZoneContextId_Type = Integer32
_FsMIStdIpv6ScopeZoneContextId_Object = MibTableColumn
fsMIStdIpv6ScopeZoneContextId = _FsMIStdIpv6ScopeZoneContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 12, 1, 14),
    _FsMIStdIpv6ScopeZoneContextId_Type()
)
fsMIStdIpv6ScopeZoneContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6ScopeZoneContextId.setStatus("current")
_FsMIStdIpDefaultRouterTable_Object = MibTable
fsMIStdIpDefaultRouterTable = _FsMIStdIpDefaultRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 13)
)
if mibBuilder.loadTexts:
    fsMIStdIpDefaultRouterTable.setStatus("current")
_FsMIStdIpDefaultRouterEntry_Object = MibTableRow
fsMIStdIpDefaultRouterEntry = _FsMIStdIpDefaultRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 13, 1)
)
fsMIStdIpDefaultRouterEntry.setIndexNames(
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpDefaultRouterAddressType"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpDefaultRouterAddress"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpDefaultRouterIfIndex"),
)
if mibBuilder.loadTexts:
    fsMIStdIpDefaultRouterEntry.setStatus("current")
_FsMIStdIpDefaultRouterAddressType_Type = InetAddressType
_FsMIStdIpDefaultRouterAddressType_Object = MibTableColumn
fsMIStdIpDefaultRouterAddressType = _FsMIStdIpDefaultRouterAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 13, 1, 1),
    _FsMIStdIpDefaultRouterAddressType_Type()
)
fsMIStdIpDefaultRouterAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpDefaultRouterAddressType.setStatus("current")


class _FsMIStdIpDefaultRouterAddress_Type(InetAddress):
    """Custom type fsMIStdIpDefaultRouterAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIStdIpDefaultRouterAddress_Type.__name__ = "InetAddress"
_FsMIStdIpDefaultRouterAddress_Object = MibTableColumn
fsMIStdIpDefaultRouterAddress = _FsMIStdIpDefaultRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 13, 1, 2),
    _FsMIStdIpDefaultRouterAddress_Type()
)
fsMIStdIpDefaultRouterAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpDefaultRouterAddress.setStatus("current")
_FsMIStdIpDefaultRouterIfIndex_Type = InterfaceIndex
_FsMIStdIpDefaultRouterIfIndex_Object = MibTableColumn
fsMIStdIpDefaultRouterIfIndex = _FsMIStdIpDefaultRouterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 13, 1, 3),
    _FsMIStdIpDefaultRouterIfIndex_Type()
)
fsMIStdIpDefaultRouterIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpDefaultRouterIfIndex.setStatus("current")


class _FsMIStdIpDefaultRouterLifetime_Type(Unsigned32):
    """Custom type fsMIStdIpDefaultRouterLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIStdIpDefaultRouterLifetime_Type.__name__ = "Unsigned32"
_FsMIStdIpDefaultRouterLifetime_Object = MibTableColumn
fsMIStdIpDefaultRouterLifetime = _FsMIStdIpDefaultRouterLifetime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 13, 1, 4),
    _FsMIStdIpDefaultRouterLifetime_Type()
)
fsMIStdIpDefaultRouterLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpDefaultRouterLifetime.setStatus("current")
if mibBuilder.loadTexts:
    fsMIStdIpDefaultRouterLifetime.setUnits("seconds")


class _FsMIStdIpDefaultRouterPreference_Type(Integer32):
    """Custom type fsMIStdIpDefaultRouterPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("reserved", -2),
          ("low", -1),
          ("medium", 0),
          ("high", 1))
    )


_FsMIStdIpDefaultRouterPreference_Type.__name__ = "Integer32"
_FsMIStdIpDefaultRouterPreference_Object = MibTableColumn
fsMIStdIpDefaultRouterPreference = _FsMIStdIpDefaultRouterPreference_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 13, 1, 5),
    _FsMIStdIpDefaultRouterPreference_Type()
)
fsMIStdIpDefaultRouterPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpDefaultRouterPreference.setStatus("current")
_FsMIStdIpv6RouterAdvertTable_Object = MibTable
fsMIStdIpv6RouterAdvertTable = _FsMIStdIpv6RouterAdvertTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 14)
)
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertTable.setStatus("current")
_FsMIStdIpv6RouterAdvertEntry_Object = MibTableRow
fsMIStdIpv6RouterAdvertEntry = _FsMIStdIpv6RouterAdvertEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 14, 1)
)
fsMIStdIpv6RouterAdvertEntry.setIndexNames(
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpv6RouterAdvertIfIndex"),
)
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertEntry.setStatus("current")
_FsMIStdIpv6RouterAdvertIfIndex_Type = InterfaceIndex
_FsMIStdIpv6RouterAdvertIfIndex_Object = MibTableColumn
fsMIStdIpv6RouterAdvertIfIndex = _FsMIStdIpv6RouterAdvertIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 14, 1, 1),
    _FsMIStdIpv6RouterAdvertIfIndex_Type()
)
fsMIStdIpv6RouterAdvertIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertIfIndex.setStatus("current")


class _FsMIStdIpv6RouterAdvertSendAdverts_Type(TruthValue):
    """Custom type fsMIStdIpv6RouterAdvertSendAdverts based on TruthValue"""
    defaultValue = 2


_FsMIStdIpv6RouterAdvertSendAdverts_Type.__name__ = "TruthValue"
_FsMIStdIpv6RouterAdvertSendAdverts_Object = MibTableColumn
fsMIStdIpv6RouterAdvertSendAdverts = _FsMIStdIpv6RouterAdvertSendAdverts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 14, 1, 2),
    _FsMIStdIpv6RouterAdvertSendAdverts_Type()
)
fsMIStdIpv6RouterAdvertSendAdverts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertSendAdverts.setStatus("current")


class _FsMIStdIpv6RouterAdvertMaxInterval_Type(Unsigned32):
    """Custom type fsMIStdIpv6RouterAdvertMaxInterval based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_FsMIStdIpv6RouterAdvertMaxInterval_Type.__name__ = "Unsigned32"
_FsMIStdIpv6RouterAdvertMaxInterval_Object = MibTableColumn
fsMIStdIpv6RouterAdvertMaxInterval = _FsMIStdIpv6RouterAdvertMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 14, 1, 3),
    _FsMIStdIpv6RouterAdvertMaxInterval_Type()
)
fsMIStdIpv6RouterAdvertMaxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertMaxInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertMaxInterval.setUnits("seconds")


class _FsMIStdIpv6RouterAdvertMinInterval_Type(Unsigned32):
    """Custom type fsMIStdIpv6RouterAdvertMinInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1350),
    )


_FsMIStdIpv6RouterAdvertMinInterval_Type.__name__ = "Unsigned32"
_FsMIStdIpv6RouterAdvertMinInterval_Object = MibTableColumn
fsMIStdIpv6RouterAdvertMinInterval = _FsMIStdIpv6RouterAdvertMinInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 14, 1, 4),
    _FsMIStdIpv6RouterAdvertMinInterval_Type()
)
fsMIStdIpv6RouterAdvertMinInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertMinInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertMinInterval.setUnits("seconds")


class _FsMIStdIpv6RouterAdvertManagedFlag_Type(TruthValue):
    """Custom type fsMIStdIpv6RouterAdvertManagedFlag based on TruthValue"""
    defaultValue = 2


_FsMIStdIpv6RouterAdvertManagedFlag_Type.__name__ = "TruthValue"
_FsMIStdIpv6RouterAdvertManagedFlag_Object = MibTableColumn
fsMIStdIpv6RouterAdvertManagedFlag = _FsMIStdIpv6RouterAdvertManagedFlag_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 14, 1, 5),
    _FsMIStdIpv6RouterAdvertManagedFlag_Type()
)
fsMIStdIpv6RouterAdvertManagedFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertManagedFlag.setStatus("current")


class _FsMIStdIpv6RouterAdvertOtherConfigFlag_Type(TruthValue):
    """Custom type fsMIStdIpv6RouterAdvertOtherConfigFlag based on TruthValue"""
    defaultValue = 2


_FsMIStdIpv6RouterAdvertOtherConfigFlag_Type.__name__ = "TruthValue"
_FsMIStdIpv6RouterAdvertOtherConfigFlag_Object = MibTableColumn
fsMIStdIpv6RouterAdvertOtherConfigFlag = _FsMIStdIpv6RouterAdvertOtherConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 14, 1, 6),
    _FsMIStdIpv6RouterAdvertOtherConfigFlag_Type()
)
fsMIStdIpv6RouterAdvertOtherConfigFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertOtherConfigFlag.setStatus("current")


class _FsMIStdIpv6RouterAdvertLinkMTU_Type(Unsigned32):
    """Custom type fsMIStdIpv6RouterAdvertLinkMTU based on Unsigned32"""
    defaultValue = 0


_FsMIStdIpv6RouterAdvertLinkMTU_Type.__name__ = "Unsigned32"
_FsMIStdIpv6RouterAdvertLinkMTU_Object = MibTableColumn
fsMIStdIpv6RouterAdvertLinkMTU = _FsMIStdIpv6RouterAdvertLinkMTU_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 14, 1, 7),
    _FsMIStdIpv6RouterAdvertLinkMTU_Type()
)
fsMIStdIpv6RouterAdvertLinkMTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertLinkMTU.setStatus("current")


class _FsMIStdIpv6RouterAdvertReachableTime_Type(Unsigned32):
    """Custom type fsMIStdIpv6RouterAdvertReachableTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_FsMIStdIpv6RouterAdvertReachableTime_Type.__name__ = "Unsigned32"
_FsMIStdIpv6RouterAdvertReachableTime_Object = MibTableColumn
fsMIStdIpv6RouterAdvertReachableTime = _FsMIStdIpv6RouterAdvertReachableTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 14, 1, 8),
    _FsMIStdIpv6RouterAdvertReachableTime_Type()
)
fsMIStdIpv6RouterAdvertReachableTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertReachableTime.setStatus("current")
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertReachableTime.setUnits("milliseconds")


class _FsMIStdIpv6RouterAdvertRetransmitTime_Type(Unsigned32):
    """Custom type fsMIStdIpv6RouterAdvertRetransmitTime based on Unsigned32"""
    defaultValue = 0


_FsMIStdIpv6RouterAdvertRetransmitTime_Type.__name__ = "Unsigned32"
_FsMIStdIpv6RouterAdvertRetransmitTime_Object = MibTableColumn
fsMIStdIpv6RouterAdvertRetransmitTime = _FsMIStdIpv6RouterAdvertRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 14, 1, 9),
    _FsMIStdIpv6RouterAdvertRetransmitTime_Type()
)
fsMIStdIpv6RouterAdvertRetransmitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertRetransmitTime.setStatus("current")
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertRetransmitTime.setUnits("milliseconds")


class _FsMIStdIpv6RouterAdvertCurHopLimit_Type(Unsigned32):
    """Custom type fsMIStdIpv6RouterAdvertCurHopLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIStdIpv6RouterAdvertCurHopLimit_Type.__name__ = "Unsigned32"
_FsMIStdIpv6RouterAdvertCurHopLimit_Object = MibTableColumn
fsMIStdIpv6RouterAdvertCurHopLimit = _FsMIStdIpv6RouterAdvertCurHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 14, 1, 10),
    _FsMIStdIpv6RouterAdvertCurHopLimit_Type()
)
fsMIStdIpv6RouterAdvertCurHopLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertCurHopLimit.setStatus("current")


class _FsMIStdIpv6RouterAdvertDefaultLifetime_Type(Unsigned32):
    """Custom type fsMIStdIpv6RouterAdvertDefaultLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 9000),
    )


_FsMIStdIpv6RouterAdvertDefaultLifetime_Type.__name__ = "Unsigned32"
_FsMIStdIpv6RouterAdvertDefaultLifetime_Object = MibTableColumn
fsMIStdIpv6RouterAdvertDefaultLifetime = _FsMIStdIpv6RouterAdvertDefaultLifetime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 14, 1, 11),
    _FsMIStdIpv6RouterAdvertDefaultLifetime_Type()
)
fsMIStdIpv6RouterAdvertDefaultLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertDefaultLifetime.setStatus("current")
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertDefaultLifetime.setUnits("seconds")
_FsMIStdIpv6RouterAdvertRowStatus_Type = RowStatus
_FsMIStdIpv6RouterAdvertRowStatus_Object = MibTableColumn
fsMIStdIpv6RouterAdvertRowStatus = _FsMIStdIpv6RouterAdvertRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 14, 1, 12),
    _FsMIStdIpv6RouterAdvertRowStatus_Type()
)
fsMIStdIpv6RouterAdvertRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertRowStatus.setStatus("current")
_FsMIStdIpv6RouterAdvertContextId_Type = Integer32
_FsMIStdIpv6RouterAdvertContextId_Object = MibTableColumn
fsMIStdIpv6RouterAdvertContextId = _FsMIStdIpv6RouterAdvertContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 14, 1, 13),
    _FsMIStdIpv6RouterAdvertContextId_Type()
)
fsMIStdIpv6RouterAdvertContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIpv6RouterAdvertContextId.setStatus("current")
_FsMIStdIcmpStatsTable_Object = MibTable
fsMIStdIcmpStatsTable = _FsMIStdIcmpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 15)
)
if mibBuilder.loadTexts:
    fsMIStdIcmpStatsTable.setStatus("current")
_FsMIStdIcmpStatsEntry_Object = MibTableRow
fsMIStdIcmpStatsEntry = _FsMIStdIcmpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 15, 1)
)
fsMIStdIcmpStatsEntry.setIndexNames(
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIcmpStatsIPVersion"),
)
if mibBuilder.loadTexts:
    fsMIStdIcmpStatsEntry.setStatus("current")
_FsMIStdIcmpStatsIPVersion_Type = FsInetVersion
_FsMIStdIcmpStatsIPVersion_Object = MibTableColumn
fsMIStdIcmpStatsIPVersion = _FsMIStdIcmpStatsIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 15, 1, 1),
    _FsMIStdIcmpStatsIPVersion_Type()
)
fsMIStdIcmpStatsIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIcmpStatsIPVersion.setStatus("current")
_FsMIStdIcmpStatsInMsgs_Type = Counter32
_FsMIStdIcmpStatsInMsgs_Object = MibTableColumn
fsMIStdIcmpStatsInMsgs = _FsMIStdIcmpStatsInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 15, 1, 2),
    _FsMIStdIcmpStatsInMsgs_Type()
)
fsMIStdIcmpStatsInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIcmpStatsInMsgs.setStatus("current")
_FsMIStdIcmpStatsInErrors_Type = Counter32
_FsMIStdIcmpStatsInErrors_Object = MibTableColumn
fsMIStdIcmpStatsInErrors = _FsMIStdIcmpStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 15, 1, 3),
    _FsMIStdIcmpStatsInErrors_Type()
)
fsMIStdIcmpStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIcmpStatsInErrors.setStatus("current")
_FsMIStdIcmpStatsOutMsgs_Type = Counter32
_FsMIStdIcmpStatsOutMsgs_Object = MibTableColumn
fsMIStdIcmpStatsOutMsgs = _FsMIStdIcmpStatsOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 15, 1, 4),
    _FsMIStdIcmpStatsOutMsgs_Type()
)
fsMIStdIcmpStatsOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIcmpStatsOutMsgs.setStatus("current")
_FsMIStdIcmpStatsOutErrors_Type = Counter32
_FsMIStdIcmpStatsOutErrors_Object = MibTableColumn
fsMIStdIcmpStatsOutErrors = _FsMIStdIcmpStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 15, 1, 5),
    _FsMIStdIcmpStatsOutErrors_Type()
)
fsMIStdIcmpStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIcmpStatsOutErrors.setStatus("current")
_FsMIStdIcmpMsgStatsTable_Object = MibTable
fsMIStdIcmpMsgStatsTable = _FsMIStdIcmpMsgStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 16)
)
if mibBuilder.loadTexts:
    fsMIStdIcmpMsgStatsTable.setStatus("current")
_FsMIStdIcmpMsgStatsEntry_Object = MibTableRow
fsMIStdIcmpMsgStatsEntry = _FsMIStdIcmpMsgStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 16, 1)
)
fsMIStdIcmpMsgStatsEntry.setIndexNames(
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIcmpMsgStatsIPVersion"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIcmpMsgStatsType"),
)
if mibBuilder.loadTexts:
    fsMIStdIcmpMsgStatsEntry.setStatus("current")
_FsMIStdIcmpMsgStatsIPVersion_Type = FsInetVersion
_FsMIStdIcmpMsgStatsIPVersion_Object = MibTableColumn
fsMIStdIcmpMsgStatsIPVersion = _FsMIStdIcmpMsgStatsIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 16, 1, 1),
    _FsMIStdIcmpMsgStatsIPVersion_Type()
)
fsMIStdIcmpMsgStatsIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIcmpMsgStatsIPVersion.setStatus("current")


class _FsMIStdIcmpMsgStatsType_Type(Integer32):
    """Custom type fsMIStdIcmpMsgStatsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIStdIcmpMsgStatsType_Type.__name__ = "Integer32"
_FsMIStdIcmpMsgStatsType_Object = MibTableColumn
fsMIStdIcmpMsgStatsType = _FsMIStdIcmpMsgStatsType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 16, 1, 2),
    _FsMIStdIcmpMsgStatsType_Type()
)
fsMIStdIcmpMsgStatsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIcmpMsgStatsType.setStatus("current")
_FsMIStdIcmpMsgStatsInPkts_Type = Counter32
_FsMIStdIcmpMsgStatsInPkts_Object = MibTableColumn
fsMIStdIcmpMsgStatsInPkts = _FsMIStdIcmpMsgStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 16, 1, 3),
    _FsMIStdIcmpMsgStatsInPkts_Type()
)
fsMIStdIcmpMsgStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIcmpMsgStatsInPkts.setStatus("current")
_FsMIStdIcmpMsgStatsOutPkts_Type = Counter32
_FsMIStdIcmpMsgStatsOutPkts_Object = MibTableColumn
fsMIStdIcmpMsgStatsOutPkts = _FsMIStdIcmpMsgStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 16, 1, 4),
    _FsMIStdIcmpMsgStatsOutPkts_Type()
)
fsMIStdIcmpMsgStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdIcmpMsgStatsOutPkts.setStatus("current")
_FsMIStdInetCidrRouteTable_Object = MibTable
fsMIStdInetCidrRouteTable = _FsMIStdInetCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17)
)
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteTable.setStatus("current")
_FsMIStdInetCidrRouteEntry_Object = MibTableRow
fsMIStdInetCidrRouteEntry = _FsMIStdInetCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1)
)
fsMIStdInetCidrRouteEntry.setIndexNames(
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdInetCidrRouteDestType"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdInetCidrRouteDest"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdInetCidrRoutePfxLen"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdInetCidrRoutePolicy"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdInetCidrRouteNextHopType"),
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdInetCidrRouteNextHop"),
)
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteEntry.setStatus("current")
_FsMIStdInetCidrRouteDestType_Type = InetAddressType
_FsMIStdInetCidrRouteDestType_Object = MibTableColumn
fsMIStdInetCidrRouteDestType = _FsMIStdInetCidrRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 1),
    _FsMIStdInetCidrRouteDestType_Type()
)
fsMIStdInetCidrRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteDestType.setStatus("current")


class _FsMIStdInetCidrRouteDest_Type(InetAddress):
    """Custom type fsMIStdInetCidrRouteDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIStdInetCidrRouteDest_Type.__name__ = "InetAddress"
_FsMIStdInetCidrRouteDest_Object = MibTableColumn
fsMIStdInetCidrRouteDest = _FsMIStdInetCidrRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 2),
    _FsMIStdInetCidrRouteDest_Type()
)
fsMIStdInetCidrRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteDest.setStatus("current")
_FsMIStdInetCidrRoutePfxLen_Type = InetAddressPrefixLength
_FsMIStdInetCidrRoutePfxLen_Object = MibTableColumn
fsMIStdInetCidrRoutePfxLen = _FsMIStdInetCidrRoutePfxLen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 3),
    _FsMIStdInetCidrRoutePfxLen_Type()
)
fsMIStdInetCidrRoutePfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRoutePfxLen.setStatus("current")
_FsMIStdInetCidrRoutePolicy_Type = ObjectIdentifier
_FsMIStdInetCidrRoutePolicy_Object = MibTableColumn
fsMIStdInetCidrRoutePolicy = _FsMIStdInetCidrRoutePolicy_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 4),
    _FsMIStdInetCidrRoutePolicy_Type()
)
fsMIStdInetCidrRoutePolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRoutePolicy.setStatus("current")
_FsMIStdInetCidrRouteNextHopType_Type = InetAddressType
_FsMIStdInetCidrRouteNextHopType_Object = MibTableColumn
fsMIStdInetCidrRouteNextHopType = _FsMIStdInetCidrRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 5),
    _FsMIStdInetCidrRouteNextHopType_Type()
)
fsMIStdInetCidrRouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteNextHopType.setStatus("current")


class _FsMIStdInetCidrRouteNextHop_Type(InetAddress):
    """Custom type fsMIStdInetCidrRouteNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIStdInetCidrRouteNextHop_Type.__name__ = "InetAddress"
_FsMIStdInetCidrRouteNextHop_Object = MibTableColumn
fsMIStdInetCidrRouteNextHop = _FsMIStdInetCidrRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 6),
    _FsMIStdInetCidrRouteNextHop_Type()
)
fsMIStdInetCidrRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteNextHop.setStatus("current")
_FsMIStdInetCidrRouteIfIndex_Type = InterfaceIndexOrZero
_FsMIStdInetCidrRouteIfIndex_Object = MibTableColumn
fsMIStdInetCidrRouteIfIndex = _FsMIStdInetCidrRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 7),
    _FsMIStdInetCidrRouteIfIndex_Type()
)
fsMIStdInetCidrRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteIfIndex.setStatus("current")


class _FsMIStdInetCidrRouteType_Type(Integer32):
    """Custom type fsMIStdInetCidrRouteType based on Integer32"""
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
        *(("other", 1),
          ("reject", 2),
          ("local", 3),
          ("remote", 4),
          ("blackhole", 5))
    )


_FsMIStdInetCidrRouteType_Type.__name__ = "Integer32"
_FsMIStdInetCidrRouteType_Object = MibTableColumn
fsMIStdInetCidrRouteType = _FsMIStdInetCidrRouteType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 8),
    _FsMIStdInetCidrRouteType_Type()
)
fsMIStdInetCidrRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteType.setStatus("current")
_FsMIStdInetCidrRouteProto_Type = IANAipRouteProtocol
_FsMIStdInetCidrRouteProto_Object = MibTableColumn
fsMIStdInetCidrRouteProto = _FsMIStdInetCidrRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 9),
    _FsMIStdInetCidrRouteProto_Type()
)
fsMIStdInetCidrRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteProto.setStatus("current")
_FsMIStdInetCidrRouteAge_Type = Gauge32
_FsMIStdInetCidrRouteAge_Object = MibTableColumn
fsMIStdInetCidrRouteAge = _FsMIStdInetCidrRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 10),
    _FsMIStdInetCidrRouteAge_Type()
)
fsMIStdInetCidrRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteAge.setStatus("current")


class _FsMIStdInetCidrRouteNextHopAS_Type(InetAutonomousSystemNumber):
    """Custom type fsMIStdInetCidrRouteNextHopAS based on InetAutonomousSystemNumber"""
    defaultValue = 0


_FsMIStdInetCidrRouteNextHopAS_Type.__name__ = "InetAutonomousSystemNumber"
_FsMIStdInetCidrRouteNextHopAS_Object = MibTableColumn
fsMIStdInetCidrRouteNextHopAS = _FsMIStdInetCidrRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 11),
    _FsMIStdInetCidrRouteNextHopAS_Type()
)
fsMIStdInetCidrRouteNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteNextHopAS.setStatus("current")


class _FsMIStdInetCidrRouteMetric1_Type(Integer32):
    """Custom type fsMIStdInetCidrRouteMetric1 based on Integer32"""
    defaultValue = -1


_FsMIStdInetCidrRouteMetric1_Type.__name__ = "Integer32"
_FsMIStdInetCidrRouteMetric1_Object = MibTableColumn
fsMIStdInetCidrRouteMetric1 = _FsMIStdInetCidrRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 12),
    _FsMIStdInetCidrRouteMetric1_Type()
)
fsMIStdInetCidrRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteMetric1.setStatus("current")


class _FsMIStdInetCidrRouteMetric2_Type(Integer32):
    """Custom type fsMIStdInetCidrRouteMetric2 based on Integer32"""
    defaultValue = -1


_FsMIStdInetCidrRouteMetric2_Type.__name__ = "Integer32"
_FsMIStdInetCidrRouteMetric2_Object = MibTableColumn
fsMIStdInetCidrRouteMetric2 = _FsMIStdInetCidrRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 13),
    _FsMIStdInetCidrRouteMetric2_Type()
)
fsMIStdInetCidrRouteMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteMetric2.setStatus("current")


class _FsMIStdInetCidrRouteMetric3_Type(Integer32):
    """Custom type fsMIStdInetCidrRouteMetric3 based on Integer32"""
    defaultValue = -1


_FsMIStdInetCidrRouteMetric3_Type.__name__ = "Integer32"
_FsMIStdInetCidrRouteMetric3_Object = MibTableColumn
fsMIStdInetCidrRouteMetric3 = _FsMIStdInetCidrRouteMetric3_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 14),
    _FsMIStdInetCidrRouteMetric3_Type()
)
fsMIStdInetCidrRouteMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteMetric3.setStatus("current")


class _FsMIStdInetCidrRouteMetric4_Type(Integer32):
    """Custom type fsMIStdInetCidrRouteMetric4 based on Integer32"""
    defaultValue = -1


_FsMIStdInetCidrRouteMetric4_Type.__name__ = "Integer32"
_FsMIStdInetCidrRouteMetric4_Object = MibTableColumn
fsMIStdInetCidrRouteMetric4 = _FsMIStdInetCidrRouteMetric4_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 15),
    _FsMIStdInetCidrRouteMetric4_Type()
)
fsMIStdInetCidrRouteMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteMetric4.setStatus("current")


class _FsMIStdInetCidrRouteMetric5_Type(Integer32):
    """Custom type fsMIStdInetCidrRouteMetric5 based on Integer32"""
    defaultValue = -1


_FsMIStdInetCidrRouteMetric5_Type.__name__ = "Integer32"
_FsMIStdInetCidrRouteMetric5_Object = MibTableColumn
fsMIStdInetCidrRouteMetric5 = _FsMIStdInetCidrRouteMetric5_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 16),
    _FsMIStdInetCidrRouteMetric5_Type()
)
fsMIStdInetCidrRouteMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteMetric5.setStatus("current")
_FsMIStdInetCidrRouteStatus_Type = RowStatus
_FsMIStdInetCidrRouteStatus_Object = MibTableColumn
fsMIStdInetCidrRouteStatus = _FsMIStdInetCidrRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 17),
    _FsMIStdInetCidrRouteStatus_Type()
)
fsMIStdInetCidrRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteStatus.setStatus("current")


class _FsMIStdInetCidrRouteAddrType_Type(Integer32):
    """Custom type fsMIStdInetCidrRouteAddrType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("anycast", 2))
    )


_FsMIStdInetCidrRouteAddrType_Type.__name__ = "Integer32"
_FsMIStdInetCidrRouteAddrType_Object = MibTableColumn
fsMIStdInetCidrRouteAddrType = _FsMIStdInetCidrRouteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 18),
    _FsMIStdInetCidrRouteAddrType_Type()
)
fsMIStdInetCidrRouteAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteAddrType.setStatus("current")


class _FsMIStdInetCidrRouteHWStatus_Type(Bits):
    """Custom type fsMIStdInetCidrRouteHWStatus based on Bits"""
    namedValues = NamedValues(
        *(("bestRoute", 40),
          ("hardwareStatus", 80),
          ("reachable", 100))
    )

_FsMIStdInetCidrRouteHWStatus_Type.__name__ = "Bits"
_FsMIStdInetCidrRouteHWStatus_Object = MibTableColumn
fsMIStdInetCidrRouteHWStatus = _FsMIStdInetCidrRouteHWStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 19),
    _FsMIStdInetCidrRouteHWStatus_Type()
)
fsMIStdInetCidrRouteHWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRouteHWStatus.setStatus("current")


class _FsMIStdInetCidrRoutePreference_Type(Integer32):
    """Custom type fsMIStdInetCidrRoutePreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsMIStdInetCidrRoutePreference_Type.__name__ = "Integer32"
_FsMIStdInetCidrRoutePreference_Object = MibTableColumn
fsMIStdInetCidrRoutePreference = _FsMIStdInetCidrRoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 17, 1, 20),
    _FsMIStdInetCidrRoutePreference_Type()
)
fsMIStdInetCidrRoutePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIStdInetCidrRoutePreference.setStatus("current")
_FsMIStdIpifTable_Object = MibTable
fsMIStdIpifTable = _FsMIStdIpifTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 18)
)
if mibBuilder.loadTexts:
    fsMIStdIpifTable.setStatus("current")
_FsMIStdIpifEntry_Object = MibTableRow
fsMIStdIpifEntry = _FsMIStdIpifEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 18, 1)
)
fsMIStdIpifEntry.setIndexNames(
    (0, "ARICENT-MISTD-IPVX-MIB", "fsMIStdIpIndex"),
)
if mibBuilder.loadTexts:
    fsMIStdIpifEntry.setStatus("current")


class _FsMIStdIpIndex_Type(Integer32):
    """Custom type fsMIStdIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIStdIpIndex_Type.__name__ = "Integer32"
_FsMIStdIpIndex_Object = MibTableColumn
fsMIStdIpIndex = _FsMIStdIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 18, 1, 1),
    _FsMIStdIpIndex_Type()
)
fsMIStdIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdIpIndex.setStatus("current")


class _FsMIStdIpProxyArpAdminStatus_Type(Integer32):
    """Custom type fsMIStdIpProxyArpAdminStatus based on Integer32"""
    defaultValue = 2

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


_FsMIStdIpProxyArpAdminStatus_Type.__name__ = "Integer32"
_FsMIStdIpProxyArpAdminStatus_Object = MibTableColumn
fsMIStdIpProxyArpAdminStatus = _FsMIStdIpProxyArpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 18, 1, 2),
    _FsMIStdIpProxyArpAdminStatus_Type()
)
fsMIStdIpProxyArpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdIpProxyArpAdminStatus.setStatus("current")


class _FsMIStdIpLocalProxyArpAdminStatus_Type(Integer32):
    """Custom type fsMIStdIpLocalProxyArpAdminStatus based on Integer32"""
    defaultValue = 2

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


_FsMIStdIpLocalProxyArpAdminStatus_Type.__name__ = "Integer32"
_FsMIStdIpLocalProxyArpAdminStatus_Object = MibTableColumn
fsMIStdIpLocalProxyArpAdminStatus = _FsMIStdIpLocalProxyArpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 18, 1, 3),
    _FsMIStdIpLocalProxyArpAdminStatus_Type()
)
fsMIStdIpLocalProxyArpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdIpLocalProxyArpAdminStatus.setStatus("current")


class _FsMIStdIpProxyArpSubnetOption_Type(Integer32):
    """Custom type fsMIStdIpProxyArpSubnetOption based on Integer32"""
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


_FsMIStdIpProxyArpSubnetOption_Type.__name__ = "Integer32"
_FsMIStdIpProxyArpSubnetOption_Object = MibScalar
fsMIStdIpProxyArpSubnetOption = _FsMIStdIpProxyArpSubnetOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 37, 19),
    _FsMIStdIpProxyArpSubnetOption_Type()
)
fsMIStdIpProxyArpSubnetOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdIpProxyArpSubnetOption.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-MISTD-IPVX-MIB",
    **{"FsInetVersion": FsInetVersion,
       "fsMIStdIp": fsMIStdIp,
       "fsMIStdIpv4InterfaceTableLastChange": fsMIStdIpv4InterfaceTableLastChange,
       "fsMIStdIpv6InterfaceTableLastChange": fsMIStdIpv6InterfaceTableLastChange,
       "fsMIStdIpIfStatsTableLastChange": fsMIStdIpIfStatsTableLastChange,
       "fsMIStdIpGlobalTable": fsMIStdIpGlobalTable,
       "fsMIStdIpGlobalEntry": fsMIStdIpGlobalEntry,
       "fsMIStdIpContextId": fsMIStdIpContextId,
       "fsMIStdIpForwarding": fsMIStdIpForwarding,
       "fsMIStdIpDefaultTTL": fsMIStdIpDefaultTTL,
       "fsMIStdIpReasmTimeout": fsMIStdIpReasmTimeout,
       "fsMIStdIpv6IpForwarding": fsMIStdIpv6IpForwarding,
       "fsMIStdIpv6IpDefaultHopLimit": fsMIStdIpv6IpDefaultHopLimit,
       "fsMIStdInetCidrRouteNumber": fsMIStdInetCidrRouteNumber,
       "fsMIStdInetCidrRouteDiscards": fsMIStdInetCidrRouteDiscards,
       "fsMIStdIpv4InterfaceTable": fsMIStdIpv4InterfaceTable,
       "fsMIStdIpv4InterfaceEntry": fsMIStdIpv4InterfaceEntry,
       "fsMIStdIpv4InterfaceIfIndex": fsMIStdIpv4InterfaceIfIndex,
       "fsMIStdIpv4InterfaceReasmMaxSize": fsMIStdIpv4InterfaceReasmMaxSize,
       "fsMIStdIpv4InterfaceEnableStatus": fsMIStdIpv4InterfaceEnableStatus,
       "fsMIStdIpv4InterfaceRetransmitTime": fsMIStdIpv4InterfaceRetransmitTime,
       "fsMIStdIpv4IfContextId": fsMIStdIpv4IfContextId,
       "fsMIStdIpv6InterfaceTable": fsMIStdIpv6InterfaceTable,
       "fsMIStdIpv6InterfaceEntry": fsMIStdIpv6InterfaceEntry,
       "fsMIStdIpv6InterfaceIfIndex": fsMIStdIpv6InterfaceIfIndex,
       "fsMIStdIpv6InterfaceReasmMaxSize": fsMIStdIpv6InterfaceReasmMaxSize,
       "fsMIStdIpv6InterfaceIdentifier": fsMIStdIpv6InterfaceIdentifier,
       "fsMIStdIpv6InterfaceEnableStatus": fsMIStdIpv6InterfaceEnableStatus,
       "fsMIStdIpv6InterfaceReachableTime": fsMIStdIpv6InterfaceReachableTime,
       "fsMIStdIpv6InterfaceRetransmitTime": fsMIStdIpv6InterfaceRetransmitTime,
       "fsMIStdIpv6InterfaceForwarding": fsMIStdIpv6InterfaceForwarding,
       "fsMIStdIpv6IfContextId": fsMIStdIpv6IfContextId,
       "fsMIStdIpSystemStatsTable": fsMIStdIpSystemStatsTable,
       "fsMIStdIpSystemStatsEntry": fsMIStdIpSystemStatsEntry,
       "fsMIStdIpSystemStatsIPVersion": fsMIStdIpSystemStatsIPVersion,
       "fsMIStdIpSystemStatsInReceives": fsMIStdIpSystemStatsInReceives,
       "fsMIStdIpSystemStatsHCInReceives": fsMIStdIpSystemStatsHCInReceives,
       "fsMIStdIpSystemStatsInOctets": fsMIStdIpSystemStatsInOctets,
       "fsMIStdIpSystemStatsHCInOctets": fsMIStdIpSystemStatsHCInOctets,
       "fsMIStdIpSystemStatsInHdrErrors": fsMIStdIpSystemStatsInHdrErrors,
       "fsMIStdIpSystemStatsInNoRoutes": fsMIStdIpSystemStatsInNoRoutes,
       "fsMIStdIpSystemStatsInAddrErrors": fsMIStdIpSystemStatsInAddrErrors,
       "fsMIStdIpSystemStatsInUnknownProtos": fsMIStdIpSystemStatsInUnknownProtos,
       "fsMIStdIpSystemStatsInTruncatedPkts": fsMIStdIpSystemStatsInTruncatedPkts,
       "fsMIStdIpSystemStatsInForwDatagrams": fsMIStdIpSystemStatsInForwDatagrams,
       "fsMIStdIpSystemStatsHCInForwDatagrams": fsMIStdIpSystemStatsHCInForwDatagrams,
       "fsMIStdIpSystemStatsReasmReqds": fsMIStdIpSystemStatsReasmReqds,
       "fsMIStdIpSystemStatsReasmOKs": fsMIStdIpSystemStatsReasmOKs,
       "fsMIStdIpSystemStatsReasmFails": fsMIStdIpSystemStatsReasmFails,
       "fsMIStdIpSystemStatsInDiscards": fsMIStdIpSystemStatsInDiscards,
       "fsMIStdIpSystemStatsInDelivers": fsMIStdIpSystemStatsInDelivers,
       "fsMIStdIpSystemStatsHCInDelivers": fsMIStdIpSystemStatsHCInDelivers,
       "fsMIStdIpSystemStatsOutRequests": fsMIStdIpSystemStatsOutRequests,
       "fsMIStdIpSystemStatsHCOutRequests": fsMIStdIpSystemStatsHCOutRequests,
       "fsMIStdIpSystemStatsOutNoRoutes": fsMIStdIpSystemStatsOutNoRoutes,
       "fsMIStdIpSystemStatsOutForwDatagrams": fsMIStdIpSystemStatsOutForwDatagrams,
       "fsMIStdIpSystemStatsHCOutForwDatagrams": fsMIStdIpSystemStatsHCOutForwDatagrams,
       "fsMIStdIpSystemStatsOutDiscards": fsMIStdIpSystemStatsOutDiscards,
       "fsMIStdIpSystemStatsOutFragReqds": fsMIStdIpSystemStatsOutFragReqds,
       "fsMIStdIpSystemStatsOutFragOKs": fsMIStdIpSystemStatsOutFragOKs,
       "fsMIStdIpSystemStatsOutFragFails": fsMIStdIpSystemStatsOutFragFails,
       "fsMIStdIpSystemStatsOutFragCreates": fsMIStdIpSystemStatsOutFragCreates,
       "fsMIStdIpSystemStatsOutTransmits": fsMIStdIpSystemStatsOutTransmits,
       "fsMIStdIpSystemStatsHCOutTransmits": fsMIStdIpSystemStatsHCOutTransmits,
       "fsMIStdIpSystemStatsOutOctets": fsMIStdIpSystemStatsOutOctets,
       "fsMIStdIpSystemStatsHCOutOctets": fsMIStdIpSystemStatsHCOutOctets,
       "fsMIStdIpSystemStatsInMcastPkts": fsMIStdIpSystemStatsInMcastPkts,
       "fsMIStdIpSystemStatsHCInMcastPkts": fsMIStdIpSystemStatsHCInMcastPkts,
       "fsMIStdIpSystemStatsInMcastOctets": fsMIStdIpSystemStatsInMcastOctets,
       "fsMIStdIpSystemStatsHCInMcastOctets": fsMIStdIpSystemStatsHCInMcastOctets,
       "fsMIStdIpSystemStatsOutMcastPkts": fsMIStdIpSystemStatsOutMcastPkts,
       "fsMIStdIpSystemStatsHCOutMcastPkts": fsMIStdIpSystemStatsHCOutMcastPkts,
       "fsMIStdIpSystemStatsOutMcastOctets": fsMIStdIpSystemStatsOutMcastOctets,
       "fsMIStdIpSystemStatsHCOutMcastOctets": fsMIStdIpSystemStatsHCOutMcastOctets,
       "fsMIStdIpSystemStatsInBcastPkts": fsMIStdIpSystemStatsInBcastPkts,
       "fsMIStdIpSystemStatsHCInBcastPkts": fsMIStdIpSystemStatsHCInBcastPkts,
       "fsMIStdIpSystemStatsOutBcastPkts": fsMIStdIpSystemStatsOutBcastPkts,
       "fsMIStdIpSystemStatsHCOutBcastPkts": fsMIStdIpSystemStatsHCOutBcastPkts,
       "fsMIStdIpSystemStatsDiscontinuityTime": fsMIStdIpSystemStatsDiscontinuityTime,
       "fsMIStdIpSystemStatsRefreshRate": fsMIStdIpSystemStatsRefreshRate,
       "fsMIStdIpIfStatsTable": fsMIStdIpIfStatsTable,
       "fsMIStdIpIfStatsEntry": fsMIStdIpIfStatsEntry,
       "fsMIStdIpIfStatsIPVersion": fsMIStdIpIfStatsIPVersion,
       "fsMIStdIpIfStatsIfIndex": fsMIStdIpIfStatsIfIndex,
       "fsMIStdIpIfStatsInReceives": fsMIStdIpIfStatsInReceives,
       "fsMIStdIpIfStatsHCInReceives": fsMIStdIpIfStatsHCInReceives,
       "fsMIStdIpIfStatsInOctets": fsMIStdIpIfStatsInOctets,
       "fsMIStdIpIfStatsHCInOctets": fsMIStdIpIfStatsHCInOctets,
       "fsMIStdIpIfStatsInHdrErrors": fsMIStdIpIfStatsInHdrErrors,
       "fsMIStdIpIfStatsInNoRoutes": fsMIStdIpIfStatsInNoRoutes,
       "fsMIStdIpIfStatsInAddrErrors": fsMIStdIpIfStatsInAddrErrors,
       "fsMIStdIpIfStatsInUnknownProtos": fsMIStdIpIfStatsInUnknownProtos,
       "fsMIStdIpIfStatsInTruncatedPkts": fsMIStdIpIfStatsInTruncatedPkts,
       "fsMIStdIpIfStatsInForwDatagrams": fsMIStdIpIfStatsInForwDatagrams,
       "fsMIStdIpIfStatsHCInForwDatagrams": fsMIStdIpIfStatsHCInForwDatagrams,
       "fsMIStdIpIfStatsReasmReqds": fsMIStdIpIfStatsReasmReqds,
       "fsMIStdIpIfStatsReasmOKs": fsMIStdIpIfStatsReasmOKs,
       "fsMIStdIpIfStatsReasmFails": fsMIStdIpIfStatsReasmFails,
       "fsMIStdIpIfStatsInDiscards": fsMIStdIpIfStatsInDiscards,
       "fsMIStdIpIfStatsInDelivers": fsMIStdIpIfStatsInDelivers,
       "fsMIStdIpIfStatsHCInDelivers": fsMIStdIpIfStatsHCInDelivers,
       "fsMIStdIpIfStatsOutRequests": fsMIStdIpIfStatsOutRequests,
       "fsMIStdIpIfStatsHCOutRequests": fsMIStdIpIfStatsHCOutRequests,
       "fsMIStdIpIfStatsOutForwDatagrams": fsMIStdIpIfStatsOutForwDatagrams,
       "fsMIStdIpIfStatsHCOutForwDatagrams": fsMIStdIpIfStatsHCOutForwDatagrams,
       "fsMIStdIpIfStatsOutDiscards": fsMIStdIpIfStatsOutDiscards,
       "fsMIStdIpIfStatsOutFragReqds": fsMIStdIpIfStatsOutFragReqds,
       "fsMIStdIpIfStatsOutFragOKs": fsMIStdIpIfStatsOutFragOKs,
       "fsMIStdIpIfStatsOutFragFails": fsMIStdIpIfStatsOutFragFails,
       "fsMIStdIpIfStatsOutFragCreates": fsMIStdIpIfStatsOutFragCreates,
       "fsMIStdIpIfStatsOutTransmits": fsMIStdIpIfStatsOutTransmits,
       "fsMIStdIpIfStatsHCOutTransmits": fsMIStdIpIfStatsHCOutTransmits,
       "fsMIStdIpIfStatsOutOctets": fsMIStdIpIfStatsOutOctets,
       "fsMIStdIpIfStatsHCOutOctets": fsMIStdIpIfStatsHCOutOctets,
       "fsMIStdIpIfStatsInMcastPkts": fsMIStdIpIfStatsInMcastPkts,
       "fsMIStdIpIfStatsHCInMcastPkts": fsMIStdIpIfStatsHCInMcastPkts,
       "fsMIStdIpIfStatsInMcastOctets": fsMIStdIpIfStatsInMcastOctets,
       "fsMIStdIpIfStatsHCInMcastOctets": fsMIStdIpIfStatsHCInMcastOctets,
       "fsMIStdIpIfStatsOutMcastPkts": fsMIStdIpIfStatsOutMcastPkts,
       "fsMIStdIpIfStatsHCOutMcastPkts": fsMIStdIpIfStatsHCOutMcastPkts,
       "fsMIStdIpIfStatsOutMcastOctets": fsMIStdIpIfStatsOutMcastOctets,
       "fsMIStdIpIfStatsHCOutMcastOctets": fsMIStdIpIfStatsHCOutMcastOctets,
       "fsMIStdIpIfStatsInBcastPkts": fsMIStdIpIfStatsInBcastPkts,
       "fsMIStdIpIfStatsHCInBcastPkts": fsMIStdIpIfStatsHCInBcastPkts,
       "fsMIStdIpIfStatsOutBcastPkts": fsMIStdIpIfStatsOutBcastPkts,
       "fsMIStdIpIfStatsHCOutBcastPkts": fsMIStdIpIfStatsHCOutBcastPkts,
       "fsMIStdIpIfStatsDiscontinuityTime": fsMIStdIpIfStatsDiscontinuityTime,
       "fsMIStdIpIfStatsRefreshRate": fsMIStdIpIfStatsRefreshRate,
       "fsMIStdIpIfStatsContextId": fsMIStdIpIfStatsContextId,
       "fsMIStdIpAddressPrefixTable": fsMIStdIpAddressPrefixTable,
       "fsMIStdIpAddressPrefixEntry": fsMIStdIpAddressPrefixEntry,
       "fsMIStdIpAddressPrefixIfIndex": fsMIStdIpAddressPrefixIfIndex,
       "fsMIStdIpAddressPrefixType": fsMIStdIpAddressPrefixType,
       "fsMIStdIpAddressPrefixPrefix": fsMIStdIpAddressPrefixPrefix,
       "fsMIStdIpAddressPrefixLength": fsMIStdIpAddressPrefixLength,
       "fsMIStdIpAddressPrefixOrigin": fsMIStdIpAddressPrefixOrigin,
       "fsMIStdIpAddressPrefixOnLinkFlag": fsMIStdIpAddressPrefixOnLinkFlag,
       "fsMIStdIpAddressPrefixAutonomousFlag": fsMIStdIpAddressPrefixAutonomousFlag,
       "fsMIStdIpAddressPrefixAdvPreferredLifetime": fsMIStdIpAddressPrefixAdvPreferredLifetime,
       "fsMIStdIpAddressPrefixAdvValidLifetime": fsMIStdIpAddressPrefixAdvValidLifetime,
       "fsMIStdIpAddressContextId": fsMIStdIpAddressContextId,
       "fsMIStdIpAddressTable": fsMIStdIpAddressTable,
       "fsMIStdIpAddressEntry": fsMIStdIpAddressEntry,
       "fsMIStdIpAddressAddrType": fsMIStdIpAddressAddrType,
       "fsMIStdIpAddressAddr": fsMIStdIpAddressAddr,
       "fsMIStdIpAddressIfIndex": fsMIStdIpAddressIfIndex,
       "fsMIStdIpAddressType": fsMIStdIpAddressType,
       "fsMIStdIpAddressPrefix": fsMIStdIpAddressPrefix,
       "fsMIStdIpAddressOrigin": fsMIStdIpAddressOrigin,
       "fsMIStdIpAddressStatus": fsMIStdIpAddressStatus,
       "fsMIStdIpAddressCreated": fsMIStdIpAddressCreated,
       "fsMIStdIpAddressLastChanged": fsMIStdIpAddressLastChanged,
       "fsMIStdIpAddressRowStatus": fsMIStdIpAddressRowStatus,
       "fsMIStdIpAddressStorageType": fsMIStdIpAddressStorageType,
       "fsMIStdIpNetToPhysicalTable": fsMIStdIpNetToPhysicalTable,
       "fsMIStdIpNetToPhysicalEntry": fsMIStdIpNetToPhysicalEntry,
       "fsMIStdIpNetToPhysicalIfIndex": fsMIStdIpNetToPhysicalIfIndex,
       "fsMIStdIpNetToPhysicalNetAddressType": fsMIStdIpNetToPhysicalNetAddressType,
       "fsMIStdIpNetToPhysicalNetAddress": fsMIStdIpNetToPhysicalNetAddress,
       "fsMIStdIpNetToPhysicalPhysAddress": fsMIStdIpNetToPhysicalPhysAddress,
       "fsMIStdIpNetToPhysicalLastUpdated": fsMIStdIpNetToPhysicalLastUpdated,
       "fsMIStdIpNetToPhysicalType": fsMIStdIpNetToPhysicalType,
       "fsMIStdIpNetToPhysicalState": fsMIStdIpNetToPhysicalState,
       "fsMIStdIpNetToPhysicalRowStatus": fsMIStdIpNetToPhysicalRowStatus,
       "fsMIStdIpNetToPhysicalContextId": fsMIStdIpNetToPhysicalContextId,
       "fsMIStdIpv6ScopeZoneIndexTable": fsMIStdIpv6ScopeZoneIndexTable,
       "fsMIStdIpv6ScopeZoneIndexEntry": fsMIStdIpv6ScopeZoneIndexEntry,
       "fsMIStdIpv6ScopeZoneIndexIfIndex": fsMIStdIpv6ScopeZoneIndexIfIndex,
       "fsMIStdIpv6ScopeZoneIndexLinkLocal": fsMIStdIpv6ScopeZoneIndexLinkLocal,
       "fsMIStdIpv6ScopeZoneIndex3": fsMIStdIpv6ScopeZoneIndex3,
       "fsMIStdIpv6ScopeZoneIndexAdminLocal": fsMIStdIpv6ScopeZoneIndexAdminLocal,
       "fsMIStdIpv6ScopeZoneIndexSiteLocal": fsMIStdIpv6ScopeZoneIndexSiteLocal,
       "fsMIStdIpv6ScopeZoneIndex6": fsMIStdIpv6ScopeZoneIndex6,
       "fsMIStdIpv6ScopeZoneIndex7": fsMIStdIpv6ScopeZoneIndex7,
       "fsMIStdIpv6ScopeZoneIndexOrganizationLocal": fsMIStdIpv6ScopeZoneIndexOrganizationLocal,
       "fsMIStdIpv6ScopeZoneIndex9": fsMIStdIpv6ScopeZoneIndex9,
       "fsMIStdIpv6ScopeZoneIndexA": fsMIStdIpv6ScopeZoneIndexA,
       "fsMIStdIpv6ScopeZoneIndexB": fsMIStdIpv6ScopeZoneIndexB,
       "fsMIStdIpv6ScopeZoneIndexC": fsMIStdIpv6ScopeZoneIndexC,
       "fsMIStdIpv6ScopeZoneIndexD": fsMIStdIpv6ScopeZoneIndexD,
       "fsMIStdIpv6ScopeZoneContextId": fsMIStdIpv6ScopeZoneContextId,
       "fsMIStdIpDefaultRouterTable": fsMIStdIpDefaultRouterTable,
       "fsMIStdIpDefaultRouterEntry": fsMIStdIpDefaultRouterEntry,
       "fsMIStdIpDefaultRouterAddressType": fsMIStdIpDefaultRouterAddressType,
       "fsMIStdIpDefaultRouterAddress": fsMIStdIpDefaultRouterAddress,
       "fsMIStdIpDefaultRouterIfIndex": fsMIStdIpDefaultRouterIfIndex,
       "fsMIStdIpDefaultRouterLifetime": fsMIStdIpDefaultRouterLifetime,
       "fsMIStdIpDefaultRouterPreference": fsMIStdIpDefaultRouterPreference,
       "fsMIStdIpv6RouterAdvertTable": fsMIStdIpv6RouterAdvertTable,
       "fsMIStdIpv6RouterAdvertEntry": fsMIStdIpv6RouterAdvertEntry,
       "fsMIStdIpv6RouterAdvertIfIndex": fsMIStdIpv6RouterAdvertIfIndex,
       "fsMIStdIpv6RouterAdvertSendAdverts": fsMIStdIpv6RouterAdvertSendAdverts,
       "fsMIStdIpv6RouterAdvertMaxInterval": fsMIStdIpv6RouterAdvertMaxInterval,
       "fsMIStdIpv6RouterAdvertMinInterval": fsMIStdIpv6RouterAdvertMinInterval,
       "fsMIStdIpv6RouterAdvertManagedFlag": fsMIStdIpv6RouterAdvertManagedFlag,
       "fsMIStdIpv6RouterAdvertOtherConfigFlag": fsMIStdIpv6RouterAdvertOtherConfigFlag,
       "fsMIStdIpv6RouterAdvertLinkMTU": fsMIStdIpv6RouterAdvertLinkMTU,
       "fsMIStdIpv6RouterAdvertReachableTime": fsMIStdIpv6RouterAdvertReachableTime,
       "fsMIStdIpv6RouterAdvertRetransmitTime": fsMIStdIpv6RouterAdvertRetransmitTime,
       "fsMIStdIpv6RouterAdvertCurHopLimit": fsMIStdIpv6RouterAdvertCurHopLimit,
       "fsMIStdIpv6RouterAdvertDefaultLifetime": fsMIStdIpv6RouterAdvertDefaultLifetime,
       "fsMIStdIpv6RouterAdvertRowStatus": fsMIStdIpv6RouterAdvertRowStatus,
       "fsMIStdIpv6RouterAdvertContextId": fsMIStdIpv6RouterAdvertContextId,
       "fsMIStdIcmpStatsTable": fsMIStdIcmpStatsTable,
       "fsMIStdIcmpStatsEntry": fsMIStdIcmpStatsEntry,
       "fsMIStdIcmpStatsIPVersion": fsMIStdIcmpStatsIPVersion,
       "fsMIStdIcmpStatsInMsgs": fsMIStdIcmpStatsInMsgs,
       "fsMIStdIcmpStatsInErrors": fsMIStdIcmpStatsInErrors,
       "fsMIStdIcmpStatsOutMsgs": fsMIStdIcmpStatsOutMsgs,
       "fsMIStdIcmpStatsOutErrors": fsMIStdIcmpStatsOutErrors,
       "fsMIStdIcmpMsgStatsTable": fsMIStdIcmpMsgStatsTable,
       "fsMIStdIcmpMsgStatsEntry": fsMIStdIcmpMsgStatsEntry,
       "fsMIStdIcmpMsgStatsIPVersion": fsMIStdIcmpMsgStatsIPVersion,
       "fsMIStdIcmpMsgStatsType": fsMIStdIcmpMsgStatsType,
       "fsMIStdIcmpMsgStatsInPkts": fsMIStdIcmpMsgStatsInPkts,
       "fsMIStdIcmpMsgStatsOutPkts": fsMIStdIcmpMsgStatsOutPkts,
       "fsMIStdInetCidrRouteTable": fsMIStdInetCidrRouteTable,
       "fsMIStdInetCidrRouteEntry": fsMIStdInetCidrRouteEntry,
       "fsMIStdInetCidrRouteDestType": fsMIStdInetCidrRouteDestType,
       "fsMIStdInetCidrRouteDest": fsMIStdInetCidrRouteDest,
       "fsMIStdInetCidrRoutePfxLen": fsMIStdInetCidrRoutePfxLen,
       "fsMIStdInetCidrRoutePolicy": fsMIStdInetCidrRoutePolicy,
       "fsMIStdInetCidrRouteNextHopType": fsMIStdInetCidrRouteNextHopType,
       "fsMIStdInetCidrRouteNextHop": fsMIStdInetCidrRouteNextHop,
       "fsMIStdInetCidrRouteIfIndex": fsMIStdInetCidrRouteIfIndex,
       "fsMIStdInetCidrRouteType": fsMIStdInetCidrRouteType,
       "fsMIStdInetCidrRouteProto": fsMIStdInetCidrRouteProto,
       "fsMIStdInetCidrRouteAge": fsMIStdInetCidrRouteAge,
       "fsMIStdInetCidrRouteNextHopAS": fsMIStdInetCidrRouteNextHopAS,
       "fsMIStdInetCidrRouteMetric1": fsMIStdInetCidrRouteMetric1,
       "fsMIStdInetCidrRouteMetric2": fsMIStdInetCidrRouteMetric2,
       "fsMIStdInetCidrRouteMetric3": fsMIStdInetCidrRouteMetric3,
       "fsMIStdInetCidrRouteMetric4": fsMIStdInetCidrRouteMetric4,
       "fsMIStdInetCidrRouteMetric5": fsMIStdInetCidrRouteMetric5,
       "fsMIStdInetCidrRouteStatus": fsMIStdInetCidrRouteStatus,
       "fsMIStdInetCidrRouteAddrType": fsMIStdInetCidrRouteAddrType,
       "fsMIStdInetCidrRouteHWStatus": fsMIStdInetCidrRouteHWStatus,
       "fsMIStdInetCidrRoutePreference": fsMIStdInetCidrRoutePreference,
       "fsMIStdIpifTable": fsMIStdIpifTable,
       "fsMIStdIpifEntry": fsMIStdIpifEntry,
       "fsMIStdIpIndex": fsMIStdIpIndex,
       "fsMIStdIpProxyArpAdminStatus": fsMIStdIpProxyArpAdminStatus,
       "fsMIStdIpLocalProxyArpAdminStatus": fsMIStdIpLocalProxyArpAdminStatus,
       "fsMIStdIpProxyArpSubnetOption": fsMIStdIpProxyArpSubnetOption}
)
