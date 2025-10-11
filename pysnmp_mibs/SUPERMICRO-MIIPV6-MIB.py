# SNMP MIB module (SUPERMICRO-MIIPV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-MIIPV6-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:49 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetScopeType,
 InetZoneIndex) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetScopeType",
    "InetZoneIndex")

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

(fsMIStdIpContextId,
 fsMIStdIpIfStatsIfIndex,
 fsMIStdIpv6InterfaceEntry,
 fsMIStdIpv6InterfaceIfIndex) = mibBuilder.importSymbols(
    "SUPERMICRO-MISTD-IPVX-MIB",
    "fsMIStdIpContextId",
    "fsMIStdIpIfStatsIfIndex",
    "fsMIStdIpv6InterfaceEntry",
    "fsMIStdIpv6InterfaceIfIndex")


# MODULE-IDENTITY

fsMIipv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35)
)
if mibBuilder.loadTexts:
    fsMIipv6MIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_FsMIipv6_ObjectIdentity = ObjectIdentity
fsMIipv6 = _FsMIipv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1)
)
_FsMIIpv6ContextTable_Object = MibTable
fsMIIpv6ContextTable = _FsMIIpv6ContextTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIIpv6ContextTable.setStatus("current")
_FsMIIpv6ContextEntry_Object = MibTableRow
fsMIIpv6ContextEntry = _FsMIIpv6ContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 1, 1)
)
fsMIIpv6ContextEntry.setIndexNames(
    (0, "SUPERMICRO-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
)
if mibBuilder.loadTexts:
    fsMIIpv6ContextEntry.setStatus("current")


class _FsMIIpv6NdCacheMaxRetries_Type(Integer32):
    """Custom type fsMIIpv6NdCacheMaxRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsMIIpv6NdCacheMaxRetries_Type.__name__ = "Integer32"
_FsMIIpv6NdCacheMaxRetries_Object = MibTableColumn
fsMIIpv6NdCacheMaxRetries = _FsMIIpv6NdCacheMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 1, 1, 1),
    _FsMIIpv6NdCacheMaxRetries_Type()
)
fsMIIpv6NdCacheMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6NdCacheMaxRetries.setStatus("current")


class _FsMIIpv6PmtuConfigStatus_Type(Integer32):
    """Custom type fsMIIpv6PmtuConfigStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FsMIIpv6PmtuConfigStatus_Type.__name__ = "Integer32"
_FsMIIpv6PmtuConfigStatus_Object = MibTableColumn
fsMIIpv6PmtuConfigStatus = _FsMIIpv6PmtuConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 1, 1, 2),
    _FsMIIpv6PmtuConfigStatus_Type()
)
fsMIIpv6PmtuConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6PmtuConfigStatus.setStatus("current")


class _FsMIIpv6PmtuTimeOutInterval_Type(Unsigned32):
    """Custom type fsMIIpv6PmtuTimeOutInterval based on Unsigned32"""
    defaultValue = 60


_FsMIIpv6PmtuTimeOutInterval_Type.__name__ = "Unsigned32"
_FsMIIpv6PmtuTimeOutInterval_Object = MibTableColumn
fsMIIpv6PmtuTimeOutInterval = _FsMIIpv6PmtuTimeOutInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 1, 1, 3),
    _FsMIIpv6PmtuTimeOutInterval_Type()
)
fsMIIpv6PmtuTimeOutInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6PmtuTimeOutInterval.setStatus("current")


class _FsMIIpv6JumboEnable_Type(Integer32):
    """Custom type fsMIIpv6JumboEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_FsMIIpv6JumboEnable_Type.__name__ = "Integer32"
_FsMIIpv6JumboEnable_Object = MibTableColumn
fsMIIpv6JumboEnable = _FsMIIpv6JumboEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 1, 1, 4),
    _FsMIIpv6JumboEnable_Type()
)
fsMIIpv6JumboEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6JumboEnable.setStatus("current")
_FsMIIpv6NumOfSendJumbo_Type = Integer32
_FsMIIpv6NumOfSendJumbo_Object = MibTableColumn
fsMIIpv6NumOfSendJumbo = _FsMIIpv6NumOfSendJumbo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 1, 1, 5),
    _FsMIIpv6NumOfSendJumbo_Type()
)
fsMIIpv6NumOfSendJumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6NumOfSendJumbo.setStatus("current")
_FsMIIpv6NumOfRecvJumbo_Type = Integer32
_FsMIIpv6NumOfRecvJumbo_Object = MibTableColumn
fsMIIpv6NumOfRecvJumbo = _FsMIIpv6NumOfRecvJumbo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 1, 1, 6),
    _FsMIIpv6NumOfRecvJumbo_Type()
)
fsMIIpv6NumOfRecvJumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6NumOfRecvJumbo.setStatus("current")
_FsMIIpv6ErrJumbo_Type = Integer32
_FsMIIpv6ErrJumbo_Object = MibTableColumn
fsMIIpv6ErrJumbo = _FsMIIpv6ErrJumbo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 1, 1, 7),
    _FsMIIpv6ErrJumbo_Type()
)
fsMIIpv6ErrJumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6ErrJumbo.setStatus("current")
_FsMIIpv6ContextDebug_Type = Unsigned32
_FsMIIpv6ContextDebug_Object = MibTableColumn
fsMIIpv6ContextDebug = _FsMIIpv6ContextDebug_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 1, 1, 8),
    _FsMIIpv6ContextDebug_Type()
)
fsMIIpv6ContextDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6ContextDebug.setStatus("current")


class _FsMIIpv6RFC5095Compatibility_Type(Integer32):
    """Custom type fsMIIpv6RFC5095Compatibility based on Integer32"""
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


_FsMIIpv6RFC5095Compatibility_Type.__name__ = "Integer32"
_FsMIIpv6RFC5095Compatibility_Object = MibTableColumn
fsMIIpv6RFC5095Compatibility = _FsMIIpv6RFC5095Compatibility_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 1, 1, 9),
    _FsMIIpv6RFC5095Compatibility_Type()
)
fsMIIpv6RFC5095Compatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6RFC5095Compatibility.setStatus("current")
_FsMIIpv6IfTable_Object = MibTable
fsMIIpv6IfTable = _FsMIIpv6IfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2)
)
if mibBuilder.loadTexts:
    fsMIIpv6IfTable.setStatus("current")
_FsMIIpv6IfEntry_Object = MibTableRow
fsMIIpv6IfEntry = _FsMIIpv6IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsMIIpv6IfEntry.setStatus("current")


class _FsMIIpv6IfType_Type(Integer32):
    """Custom type fsMIIpv6IfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              23,
              32,
              131,
              136)
        )
    )
    namedValues = NamedValues(
        *(("ethernetcsmacd", 6),
          ("ppp", 23),
          ("framerelay", 32),
          ("tunnel", 131),
          ("l3ipvlan", 136))
    )


_FsMIIpv6IfType_Type.__name__ = "Integer32"
_FsMIIpv6IfType_Object = MibTableColumn
fsMIIpv6IfType = _FsMIIpv6IfType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 1),
    _FsMIIpv6IfType_Type()
)
fsMIIpv6IfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfType.setStatus("current")


class _FsMIIpv6IfPortNum_Type(Integer32):
    """Custom type fsMIIpv6IfPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsMIIpv6IfPortNum_Type.__name__ = "Integer32"
_FsMIIpv6IfPortNum_Object = MibTableColumn
fsMIIpv6IfPortNum = _FsMIIpv6IfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 2),
    _FsMIIpv6IfPortNum_Type()
)
fsMIIpv6IfPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfPortNum.setStatus("current")
_FsMIIpv6IfCircuitNum_Type = Integer32
_FsMIIpv6IfCircuitNum_Object = MibTableColumn
fsMIIpv6IfCircuitNum = _FsMIIpv6IfCircuitNum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 3),
    _FsMIIpv6IfCircuitNum_Type()
)
fsMIIpv6IfCircuitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfCircuitNum.setStatus("current")


class _FsMIIpv6IfToken_Type(OctetString):
    """Custom type fsMIIpv6IfToken based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_FsMIIpv6IfToken_Type.__name__ = "OctetString"
_FsMIIpv6IfToken_Object = MibTableColumn
fsMIIpv6IfToken = _FsMIIpv6IfToken_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 4),
    _FsMIIpv6IfToken_Type()
)
fsMIIpv6IfToken.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6IfToken.setStatus("current")


class _FsMIIpv6IfOperStatus_Type(Integer32):
    """Custom type fsMIIpv6IfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("stale", 3))
    )


_FsMIIpv6IfOperStatus_Type.__name__ = "Integer32"
_FsMIIpv6IfOperStatus_Object = MibTableColumn
fsMIIpv6IfOperStatus = _FsMIIpv6IfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 5),
    _FsMIIpv6IfOperStatus_Type()
)
fsMIIpv6IfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfOperStatus.setStatus("current")


class _FsMIIpv6IfRouterAdvStatus_Type(Integer32):
    """Custom type fsMIIpv6IfRouterAdvStatus based on Integer32"""
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


_FsMIIpv6IfRouterAdvStatus_Type.__name__ = "Integer32"
_FsMIIpv6IfRouterAdvStatus_Object = MibTableColumn
fsMIIpv6IfRouterAdvStatus = _FsMIIpv6IfRouterAdvStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 6),
    _FsMIIpv6IfRouterAdvStatus_Type()
)
fsMIIpv6IfRouterAdvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6IfRouterAdvStatus.setStatus("current")


class _FsMIIpv6IfRouterAdvFlags_Type(Integer32):
    """Custom type fsMIIpv6IfRouterAdvFlags based on Integer32"""
    defaultValue = 6

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
        *(("mbit", 1),
          ("obit", 2),
          ("nombit", 3),
          ("noobit", 4),
          ("mobits", 5),
          ("none", 6))
    )


_FsMIIpv6IfRouterAdvFlags_Type.__name__ = "Integer32"
_FsMIIpv6IfRouterAdvFlags_Object = MibTableColumn
fsMIIpv6IfRouterAdvFlags = _FsMIIpv6IfRouterAdvFlags_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 7),
    _FsMIIpv6IfRouterAdvFlags_Type()
)
fsMIIpv6IfRouterAdvFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6IfRouterAdvFlags.setStatus("current")


class _FsMIIpv6IfHopLimit_Type(Integer32):
    """Custom type fsMIIpv6IfHopLimit based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsMIIpv6IfHopLimit_Type.__name__ = "Integer32"
_FsMIIpv6IfHopLimit_Object = MibTableColumn
fsMIIpv6IfHopLimit = _FsMIIpv6IfHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 8),
    _FsMIIpv6IfHopLimit_Type()
)
fsMIIpv6IfHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6IfHopLimit.setStatus("current")


class _FsMIIpv6IfDefRouterTime_Type(Integer32):
    """Custom type fsMIIpv6IfDefRouterTime based on Integer32"""
    defaultValue = 0


_FsMIIpv6IfDefRouterTime_Type.__name__ = "Integer32"
_FsMIIpv6IfDefRouterTime_Object = MibTableColumn
fsMIIpv6IfDefRouterTime = _FsMIIpv6IfDefRouterTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 9),
    _FsMIIpv6IfDefRouterTime_Type()
)
fsMIIpv6IfDefRouterTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6IfDefRouterTime.setStatus("current")


class _FsMIIpv6IfReachableTime_Type(Integer32):
    """Custom type fsMIIpv6IfReachableTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FsMIIpv6IfReachableTime_Type.__name__ = "Integer32"
_FsMIIpv6IfReachableTime_Object = MibTableColumn
fsMIIpv6IfReachableTime = _FsMIIpv6IfReachableTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 10),
    _FsMIIpv6IfReachableTime_Type()
)
fsMIIpv6IfReachableTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6IfReachableTime.setStatus("current")


class _FsMIIpv6IfRetransmitTime_Type(Integer32):
    """Custom type fsMIIpv6IfRetransmitTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_FsMIIpv6IfRetransmitTime_Type.__name__ = "Integer32"
_FsMIIpv6IfRetransmitTime_Object = MibTableColumn
fsMIIpv6IfRetransmitTime = _FsMIIpv6IfRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 11),
    _FsMIIpv6IfRetransmitTime_Type()
)
fsMIIpv6IfRetransmitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6IfRetransmitTime.setStatus("current")


class _FsMIIpv6IfDelayProbeTime_Type(Integer32):
    """Custom type fsMIIpv6IfDelayProbeTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsMIIpv6IfDelayProbeTime_Type.__name__ = "Integer32"
_FsMIIpv6IfDelayProbeTime_Object = MibTableColumn
fsMIIpv6IfDelayProbeTime = _FsMIIpv6IfDelayProbeTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 12),
    _FsMIIpv6IfDelayProbeTime_Type()
)
fsMIIpv6IfDelayProbeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6IfDelayProbeTime.setStatus("current")


class _FsMIIpv6IfPrefixAdvStatus_Type(Integer32):
    """Custom type fsMIIpv6IfPrefixAdvStatus based on Integer32"""
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


_FsMIIpv6IfPrefixAdvStatus_Type.__name__ = "Integer32"
_FsMIIpv6IfPrefixAdvStatus_Object = MibTableColumn
fsMIIpv6IfPrefixAdvStatus = _FsMIIpv6IfPrefixAdvStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 13),
    _FsMIIpv6IfPrefixAdvStatus_Type()
)
fsMIIpv6IfPrefixAdvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6IfPrefixAdvStatus.setStatus("current")


class _FsMIIpv6IfMinRouterAdvTime_Type(Integer32):
    """Custom type fsMIIpv6IfMinRouterAdvTime based on Integer32"""
    defaultValue = 198


_FsMIIpv6IfMinRouterAdvTime_Type.__name__ = "Integer32"
_FsMIIpv6IfMinRouterAdvTime_Object = MibTableColumn
fsMIIpv6IfMinRouterAdvTime = _FsMIIpv6IfMinRouterAdvTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 14),
    _FsMIIpv6IfMinRouterAdvTime_Type()
)
fsMIIpv6IfMinRouterAdvTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6IfMinRouterAdvTime.setStatus("current")


class _FsMIIpv6IfMaxRouterAdvTime_Type(Integer32):
    """Custom type fsMIIpv6IfMaxRouterAdvTime based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_FsMIIpv6IfMaxRouterAdvTime_Type.__name__ = "Integer32"
_FsMIIpv6IfMaxRouterAdvTime_Object = MibTableColumn
fsMIIpv6IfMaxRouterAdvTime = _FsMIIpv6IfMaxRouterAdvTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 15),
    _FsMIIpv6IfMaxRouterAdvTime_Type()
)
fsMIIpv6IfMaxRouterAdvTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6IfMaxRouterAdvTime.setStatus("current")


class _FsMIIpv6IfDADRetries_Type(Integer32):
    """Custom type fsMIIpv6IfDADRetries based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsMIIpv6IfDADRetries_Type.__name__ = "Integer32"
_FsMIIpv6IfDADRetries_Object = MibTableColumn
fsMIIpv6IfDADRetries = _FsMIIpv6IfDADRetries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 16),
    _FsMIIpv6IfDADRetries_Type()
)
fsMIIpv6IfDADRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6IfDADRetries.setStatus("current")


class _FsMIIpv6IfForwarding_Type(Integer32):
    """Custom type fsMIIpv6IfForwarding based on Integer32"""
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


_FsMIIpv6IfForwarding_Type.__name__ = "Integer32"
_FsMIIpv6IfForwarding_Object = MibTableColumn
fsMIIpv6IfForwarding = _FsMIIpv6IfForwarding_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 17),
    _FsMIIpv6IfForwarding_Type()
)
fsMIIpv6IfForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6IfForwarding.setStatus("current")


class _FsMIIpv6IfRoutingStatus_Type(Integer32):
    """Custom type fsMIIpv6IfRoutingStatus based on Integer32"""
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


_FsMIIpv6IfRoutingStatus_Type.__name__ = "Integer32"
_FsMIIpv6IfRoutingStatus_Object = MibTableColumn
fsMIIpv6IfRoutingStatus = _FsMIIpv6IfRoutingStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 18),
    _FsMIIpv6IfRoutingStatus_Type()
)
fsMIIpv6IfRoutingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfRoutingStatus.setStatus("current")


class _FsMIIpv6IfIcmpErrInterval_Type(Integer32):
    """Custom type fsMIIpv6IfIcmpErrInterval based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIIpv6IfIcmpErrInterval_Type.__name__ = "Integer32"
_FsMIIpv6IfIcmpErrInterval_Object = MibTableColumn
fsMIIpv6IfIcmpErrInterval = _FsMIIpv6IfIcmpErrInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 19),
    _FsMIIpv6IfIcmpErrInterval_Type()
)
fsMIIpv6IfIcmpErrInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6IfIcmpErrInterval.setStatus("current")


class _FsMIIpv6IfIcmpTokenBucketSize_Type(Integer32):
    """Custom type fsMIIpv6IfIcmpTokenBucketSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_FsMIIpv6IfIcmpTokenBucketSize_Type.__name__ = "Integer32"
_FsMIIpv6IfIcmpTokenBucketSize_Object = MibTableColumn
fsMIIpv6IfIcmpTokenBucketSize = _FsMIIpv6IfIcmpTokenBucketSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 20),
    _FsMIIpv6IfIcmpTokenBucketSize_Type()
)
fsMIIpv6IfIcmpTokenBucketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6IfIcmpTokenBucketSize.setStatus("current")


class _FsMIIpv6IfDestUnreachableMsg_Type(Integer32):
    """Custom type fsMIIpv6IfDestUnreachableMsg based on Integer32"""
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


_FsMIIpv6IfDestUnreachableMsg_Type.__name__ = "Integer32"
_FsMIIpv6IfDestUnreachableMsg_Object = MibTableColumn
fsMIIpv6IfDestUnreachableMsg = _FsMIIpv6IfDestUnreachableMsg_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 2, 1, 21),
    _FsMIIpv6IfDestUnreachableMsg_Type()
)
fsMIIpv6IfDestUnreachableMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6IfDestUnreachableMsg.setStatus("current")
_FsMIIpv6IfStatsTable_Object = MibTable
fsMIIpv6IfStatsTable = _FsMIIpv6IfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 3)
)
if mibBuilder.loadTexts:
    fsMIIpv6IfStatsTable.setStatus("current")
_FsMIIpv6IfStatsEntry_Object = MibTableRow
fsMIIpv6IfStatsEntry = _FsMIIpv6IfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 3, 1)
)
fsMIIpv6IfStatsEntry.setIndexNames(
    (0, "SUPERMICRO-MISTD-IPVX-MIB", "fsMIStdIpIfStatsIfIndex"),
)
if mibBuilder.loadTexts:
    fsMIIpv6IfStatsEntry.setStatus("current")
_FsMIIpv6IfStatsTooBigErrors_Type = Counter32
_FsMIIpv6IfStatsTooBigErrors_Object = MibTableColumn
fsMIIpv6IfStatsTooBigErrors = _FsMIIpv6IfStatsTooBigErrors_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 3, 1, 1),
    _FsMIIpv6IfStatsTooBigErrors_Type()
)
fsMIIpv6IfStatsTooBigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfStatsTooBigErrors.setStatus("current")
_FsMIIpv6IfStatsInRouterSols_Type = Counter32
_FsMIIpv6IfStatsInRouterSols_Object = MibTableColumn
fsMIIpv6IfStatsInRouterSols = _FsMIIpv6IfStatsInRouterSols_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 3, 1, 2),
    _FsMIIpv6IfStatsInRouterSols_Type()
)
fsMIIpv6IfStatsInRouterSols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfStatsInRouterSols.setStatus("current")
_FsMIIpv6IfStatsInRouterAdvs_Type = Counter32
_FsMIIpv6IfStatsInRouterAdvs_Object = MibTableColumn
fsMIIpv6IfStatsInRouterAdvs = _FsMIIpv6IfStatsInRouterAdvs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 3, 1, 3),
    _FsMIIpv6IfStatsInRouterAdvs_Type()
)
fsMIIpv6IfStatsInRouterAdvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfStatsInRouterAdvs.setStatus("current")
_FsMIIpv6IfStatsInNeighSols_Type = Counter32
_FsMIIpv6IfStatsInNeighSols_Object = MibTableColumn
fsMIIpv6IfStatsInNeighSols = _FsMIIpv6IfStatsInNeighSols_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 3, 1, 4),
    _FsMIIpv6IfStatsInNeighSols_Type()
)
fsMIIpv6IfStatsInNeighSols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfStatsInNeighSols.setStatus("current")
_FsMIIpv6IfStatsInNeighAdvs_Type = Counter32
_FsMIIpv6IfStatsInNeighAdvs_Object = MibTableColumn
fsMIIpv6IfStatsInNeighAdvs = _FsMIIpv6IfStatsInNeighAdvs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 3, 1, 5),
    _FsMIIpv6IfStatsInNeighAdvs_Type()
)
fsMIIpv6IfStatsInNeighAdvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfStatsInNeighAdvs.setStatus("current")
_FsMIIpv6IfStatsInRedirects_Type = Counter32
_FsMIIpv6IfStatsInRedirects_Object = MibTableColumn
fsMIIpv6IfStatsInRedirects = _FsMIIpv6IfStatsInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 3, 1, 6),
    _FsMIIpv6IfStatsInRedirects_Type()
)
fsMIIpv6IfStatsInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfStatsInRedirects.setStatus("current")
_FsMIIpv6IfStatsOutRouterSols_Type = Counter32
_FsMIIpv6IfStatsOutRouterSols_Object = MibTableColumn
fsMIIpv6IfStatsOutRouterSols = _FsMIIpv6IfStatsOutRouterSols_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 3, 1, 7),
    _FsMIIpv6IfStatsOutRouterSols_Type()
)
fsMIIpv6IfStatsOutRouterSols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfStatsOutRouterSols.setStatus("current")
_FsMIIpv6IfStatsOutRouterAdvs_Type = Counter32
_FsMIIpv6IfStatsOutRouterAdvs_Object = MibTableColumn
fsMIIpv6IfStatsOutRouterAdvs = _FsMIIpv6IfStatsOutRouterAdvs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 3, 1, 8),
    _FsMIIpv6IfStatsOutRouterAdvs_Type()
)
fsMIIpv6IfStatsOutRouterAdvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfStatsOutRouterAdvs.setStatus("current")
_FsMIIpv6IfStatsOutNeighSols_Type = Counter32
_FsMIIpv6IfStatsOutNeighSols_Object = MibTableColumn
fsMIIpv6IfStatsOutNeighSols = _FsMIIpv6IfStatsOutNeighSols_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 3, 1, 9),
    _FsMIIpv6IfStatsOutNeighSols_Type()
)
fsMIIpv6IfStatsOutNeighSols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfStatsOutNeighSols.setStatus("current")
_FsMIIpv6IfStatsOutNeighAdvs_Type = Counter32
_FsMIIpv6IfStatsOutNeighAdvs_Object = MibTableColumn
fsMIIpv6IfStatsOutNeighAdvs = _FsMIIpv6IfStatsOutNeighAdvs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 3, 1, 10),
    _FsMIIpv6IfStatsOutNeighAdvs_Type()
)
fsMIIpv6IfStatsOutNeighAdvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfStatsOutNeighAdvs.setStatus("current")
_FsMIIpv6IfStatsOutRedirects_Type = Counter32
_FsMIIpv6IfStatsOutRedirects_Object = MibTableColumn
fsMIIpv6IfStatsOutRedirects = _FsMIIpv6IfStatsOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 3, 1, 11),
    _FsMIIpv6IfStatsOutRedirects_Type()
)
fsMIIpv6IfStatsOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfStatsOutRedirects.setStatus("current")
_FsMIIpv6IfStatsLastRouterAdvTime_Type = TimeTicks
_FsMIIpv6IfStatsLastRouterAdvTime_Object = MibTableColumn
fsMIIpv6IfStatsLastRouterAdvTime = _FsMIIpv6IfStatsLastRouterAdvTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 3, 1, 12),
    _FsMIIpv6IfStatsLastRouterAdvTime_Type()
)
fsMIIpv6IfStatsLastRouterAdvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfStatsLastRouterAdvTime.setStatus("current")
_FsMIIpv6IfStatsNextRouterAdvTime_Type = TimeTicks
_FsMIIpv6IfStatsNextRouterAdvTime_Object = MibTableColumn
fsMIIpv6IfStatsNextRouterAdvTime = _FsMIIpv6IfStatsNextRouterAdvTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 3, 1, 13),
    _FsMIIpv6IfStatsNextRouterAdvTime_Type()
)
fsMIIpv6IfStatsNextRouterAdvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfStatsNextRouterAdvTime.setStatus("current")
_FsMIIpv6IfStatsIcmp6ErrRateLmtd_Type = Counter32
_FsMIIpv6IfStatsIcmp6ErrRateLmtd_Object = MibTableColumn
fsMIIpv6IfStatsIcmp6ErrRateLmtd = _FsMIIpv6IfStatsIcmp6ErrRateLmtd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 3, 1, 14),
    _FsMIIpv6IfStatsIcmp6ErrRateLmtd_Type()
)
fsMIIpv6IfStatsIcmp6ErrRateLmtd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfStatsIcmp6ErrRateLmtd.setStatus("current")
_FsMIIpv6AddrTable_Object = MibTable
fsMIIpv6AddrTable = _FsMIIpv6AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 4)
)
if mibBuilder.loadTexts:
    fsMIIpv6AddrTable.setStatus("current")
_FsMIIpv6AddrEntry_Object = MibTableRow
fsMIIpv6AddrEntry = _FsMIIpv6AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 4, 1)
)
fsMIIpv6AddrEntry.setIndexNames(
    (0, "SUPERMICRO-MISTD-IPVX-MIB", "fsMIStdIpv6InterfaceIfIndex"),
    (0, "SUPERMICRO-MIIPV6-MIB", "fsMIIpv6AddrAddress"),
    (0, "SUPERMICRO-MIIPV6-MIB", "fsMIIpv6AddrPrefixLen"),
)
if mibBuilder.loadTexts:
    fsMIIpv6AddrEntry.setStatus("current")


class _FsMIIpv6AddrAddress_Type(OctetString):
    """Custom type fsMIIpv6AddrAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIIpv6AddrAddress_Type.__name__ = "OctetString"
_FsMIIpv6AddrAddress_Object = MibTableColumn
fsMIIpv6AddrAddress = _FsMIIpv6AddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 4, 1, 1),
    _FsMIIpv6AddrAddress_Type()
)
fsMIIpv6AddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpv6AddrAddress.setStatus("current")


class _FsMIIpv6AddrPrefixLen_Type(Integer32):
    """Custom type fsMIIpv6AddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsMIIpv6AddrPrefixLen_Type.__name__ = "Integer32"
_FsMIIpv6AddrPrefixLen_Object = MibTableColumn
fsMIIpv6AddrPrefixLen = _FsMIIpv6AddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 4, 1, 2),
    _FsMIIpv6AddrPrefixLen_Type()
)
fsMIIpv6AddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpv6AddrPrefixLen.setStatus("current")
_FsMIIpv6AddrAdminStatus_Type = RowStatus
_FsMIIpv6AddrAdminStatus_Object = MibTableColumn
fsMIIpv6AddrAdminStatus = _FsMIIpv6AddrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 4, 1, 3),
    _FsMIIpv6AddrAdminStatus_Type()
)
fsMIIpv6AddrAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIIpv6AddrAdminStatus.setStatus("current")


class _FsMIIpv6AddrType_Type(Integer32):
    """Custom type fsMIIpv6AddrType based on Integer32"""
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
          ("linklocal", 3))
    )


_FsMIIpv6AddrType_Type.__name__ = "Integer32"
_FsMIIpv6AddrType_Object = MibTableColumn
fsMIIpv6AddrType = _FsMIIpv6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 4, 1, 4),
    _FsMIIpv6AddrType_Type()
)
fsMIIpv6AddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6AddrType.setStatus("current")


class _FsMIIpv6AddrProfIndex_Type(Integer32):
    """Custom type fsMIIpv6AddrProfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_FsMIIpv6AddrProfIndex_Type.__name__ = "Integer32"
_FsMIIpv6AddrProfIndex_Object = MibTableColumn
fsMIIpv6AddrProfIndex = _FsMIIpv6AddrProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 4, 1, 5),
    _FsMIIpv6AddrProfIndex_Type()
)
fsMIIpv6AddrProfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6AddrProfIndex.setStatus("current")


class _FsMIIpv6AddrOperStatus_Type(Integer32):
    """Custom type fsMIIpv6AddrOperStatus based on Integer32"""
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
        *(("tentative", 1),
          ("complete", 2),
          ("down", 3),
          ("failed", 4))
    )


_FsMIIpv6AddrOperStatus_Type.__name__ = "Integer32"
_FsMIIpv6AddrOperStatus_Object = MibTableColumn
fsMIIpv6AddrOperStatus = _FsMIIpv6AddrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 4, 1, 6),
    _FsMIIpv6AddrOperStatus_Type()
)
fsMIIpv6AddrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6AddrOperStatus.setStatus("current")


class _FsMIIpv6AddrContextId_Type(Integer32):
    """Custom type fsMIIpv6AddrContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIIpv6AddrContextId_Type.__name__ = "Integer32"
_FsMIIpv6AddrContextId_Object = MibTableColumn
fsMIIpv6AddrContextId = _FsMIIpv6AddrContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 4, 1, 7),
    _FsMIIpv6AddrContextId_Type()
)
fsMIIpv6AddrContextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6AddrContextId.setStatus("current")
_FsMIIpv6AddrScope_Type = InetScopeType
_FsMIIpv6AddrScope_Object = MibTableColumn
fsMIIpv6AddrScope = _FsMIIpv6AddrScope_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 4, 1, 8),
    _FsMIIpv6AddrScope_Type()
)
fsMIIpv6AddrScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6AddrScope.setStatus("current")
_FsMIIpv6AddrProfileTable_Object = MibTable
fsMIIpv6AddrProfileTable = _FsMIIpv6AddrProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 5)
)
if mibBuilder.loadTexts:
    fsMIIpv6AddrProfileTable.setStatus("current")
_FsMIIpv6AddrProfileEntry_Object = MibTableRow
fsMIIpv6AddrProfileEntry = _FsMIIpv6AddrProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 5, 1)
)
fsMIIpv6AddrProfileEntry.setIndexNames(
    (0, "SUPERMICRO-MIIPV6-MIB", "fsMIIpv6AddrProfileIndex"),
)
if mibBuilder.loadTexts:
    fsMIIpv6AddrProfileEntry.setStatus("current")


class _FsMIIpv6AddrProfileIndex_Type(Unsigned32):
    """Custom type fsMIIpv6AddrProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_FsMIIpv6AddrProfileIndex_Type.__name__ = "Unsigned32"
_FsMIIpv6AddrProfileIndex_Object = MibTableColumn
fsMIIpv6AddrProfileIndex = _FsMIIpv6AddrProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 5, 1, 1),
    _FsMIIpv6AddrProfileIndex_Type()
)
fsMIIpv6AddrProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpv6AddrProfileIndex.setStatus("current")


class _FsMIIpv6AddrProfileStatus_Type(Integer32):
    """Custom type fsMIIpv6AddrProfileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_FsMIIpv6AddrProfileStatus_Type.__name__ = "Integer32"
_FsMIIpv6AddrProfileStatus_Object = MibTableColumn
fsMIIpv6AddrProfileStatus = _FsMIIpv6AddrProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 5, 1, 2),
    _FsMIIpv6AddrProfileStatus_Type()
)
fsMIIpv6AddrProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6AddrProfileStatus.setStatus("current")


class _FsMIIpv6AddrProfilePrefixAdvStatus_Type(Integer32):
    """Custom type fsMIIpv6AddrProfilePrefixAdvStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_FsMIIpv6AddrProfilePrefixAdvStatus_Type.__name__ = "Integer32"
_FsMIIpv6AddrProfilePrefixAdvStatus_Object = MibTableColumn
fsMIIpv6AddrProfilePrefixAdvStatus = _FsMIIpv6AddrProfilePrefixAdvStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 5, 1, 3),
    _FsMIIpv6AddrProfilePrefixAdvStatus_Type()
)
fsMIIpv6AddrProfilePrefixAdvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6AddrProfilePrefixAdvStatus.setStatus("current")


class _FsMIIpv6AddrProfileOnLinkAdvStatus_Type(Integer32):
    """Custom type fsMIIpv6AddrProfileOnLinkAdvStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_FsMIIpv6AddrProfileOnLinkAdvStatus_Type.__name__ = "Integer32"
_FsMIIpv6AddrProfileOnLinkAdvStatus_Object = MibTableColumn
fsMIIpv6AddrProfileOnLinkAdvStatus = _FsMIIpv6AddrProfileOnLinkAdvStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 5, 1, 4),
    _FsMIIpv6AddrProfileOnLinkAdvStatus_Type()
)
fsMIIpv6AddrProfileOnLinkAdvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6AddrProfileOnLinkAdvStatus.setStatus("current")


class _FsMIIpv6AddrProfileAutoConfAdvStatus_Type(Integer32):
    """Custom type fsMIIpv6AddrProfileAutoConfAdvStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_FsMIIpv6AddrProfileAutoConfAdvStatus_Type.__name__ = "Integer32"
_FsMIIpv6AddrProfileAutoConfAdvStatus_Object = MibTableColumn
fsMIIpv6AddrProfileAutoConfAdvStatus = _FsMIIpv6AddrProfileAutoConfAdvStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 5, 1, 5),
    _FsMIIpv6AddrProfileAutoConfAdvStatus_Type()
)
fsMIIpv6AddrProfileAutoConfAdvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6AddrProfileAutoConfAdvStatus.setStatus("current")


class _FsMIIpv6AddrProfilePreferredTime_Type(Unsigned32):
    """Custom type fsMIIpv6AddrProfilePreferredTime based on Unsigned32"""
    defaultValue = 604800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIIpv6AddrProfilePreferredTime_Type.__name__ = "Unsigned32"
_FsMIIpv6AddrProfilePreferredTime_Object = MibTableColumn
fsMIIpv6AddrProfilePreferredTime = _FsMIIpv6AddrProfilePreferredTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 5, 1, 6),
    _FsMIIpv6AddrProfilePreferredTime_Type()
)
fsMIIpv6AddrProfilePreferredTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6AddrProfilePreferredTime.setStatus("current")


class _FsMIIpv6AddrProfileValidTime_Type(Unsigned32):
    """Custom type fsMIIpv6AddrProfileValidTime based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIIpv6AddrProfileValidTime_Type.__name__ = "Unsigned32"
_FsMIIpv6AddrProfileValidTime_Object = MibTableColumn
fsMIIpv6AddrProfileValidTime = _FsMIIpv6AddrProfileValidTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 5, 1, 7),
    _FsMIIpv6AddrProfileValidTime_Type()
)
fsMIIpv6AddrProfileValidTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6AddrProfileValidTime.setStatus("current")


class _FsMIIpv6AddrProfileValidLifeTimeFlag_Type(Integer32):
    """Custom type fsMIIpv6AddrProfileValidLifeTimeFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("variable", 2))
    )


_FsMIIpv6AddrProfileValidLifeTimeFlag_Type.__name__ = "Integer32"
_FsMIIpv6AddrProfileValidLifeTimeFlag_Object = MibTableColumn
fsMIIpv6AddrProfileValidLifeTimeFlag = _FsMIIpv6AddrProfileValidLifeTimeFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 5, 1, 8),
    _FsMIIpv6AddrProfileValidLifeTimeFlag_Type()
)
fsMIIpv6AddrProfileValidLifeTimeFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6AddrProfileValidLifeTimeFlag.setStatus("current")


class _FsMIIpv6AddrProfilePreferredLifeTimeFlag_Type(Integer32):
    """Custom type fsMIIpv6AddrProfilePreferredLifeTimeFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("variable", 2))
    )


_FsMIIpv6AddrProfilePreferredLifeTimeFlag_Type.__name__ = "Integer32"
_FsMIIpv6AddrProfilePreferredLifeTimeFlag_Object = MibTableColumn
fsMIIpv6AddrProfilePreferredLifeTimeFlag = _FsMIIpv6AddrProfilePreferredLifeTimeFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 5, 1, 9),
    _FsMIIpv6AddrProfilePreferredLifeTimeFlag_Type()
)
fsMIIpv6AddrProfilePreferredLifeTimeFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6AddrProfilePreferredLifeTimeFlag.setStatus("current")
_FsMIIpv6IcmpStatsTable_Object = MibTable
fsMIIpv6IcmpStatsTable = _FsMIIpv6IcmpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6)
)
if mibBuilder.loadTexts:
    fsMIIpv6IcmpStatsTable.setStatus("current")
_FsMIIpv6IcmpStatsEntry_Object = MibTableRow
fsMIIpv6IcmpStatsEntry = _FsMIIpv6IcmpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1)
)
fsMIIpv6IcmpStatsEntry.setIndexNames(
    (0, "SUPERMICRO-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
)
if mibBuilder.loadTexts:
    fsMIIpv6IcmpStatsEntry.setStatus("current")
_FsMIIpv6IcmpInMsgs_Type = Counter32
_FsMIIpv6IcmpInMsgs_Object = MibTableColumn
fsMIIpv6IcmpInMsgs = _FsMIIpv6IcmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 1),
    _FsMIIpv6IcmpInMsgs_Type()
)
fsMIIpv6IcmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpInMsgs.setStatus("current")
_FsMIIpv6IcmpInErrors_Type = Counter32
_FsMIIpv6IcmpInErrors_Object = MibTableColumn
fsMIIpv6IcmpInErrors = _FsMIIpv6IcmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 2),
    _FsMIIpv6IcmpInErrors_Type()
)
fsMIIpv6IcmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpInErrors.setStatus("current")
_FsMIIpv6IcmpInDestUnreachs_Type = Counter32
_FsMIIpv6IcmpInDestUnreachs_Object = MibTableColumn
fsMIIpv6IcmpInDestUnreachs = _FsMIIpv6IcmpInDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 3),
    _FsMIIpv6IcmpInDestUnreachs_Type()
)
fsMIIpv6IcmpInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpInDestUnreachs.setStatus("current")
_FsMIIpv6IcmpInTimeExcds_Type = Counter32
_FsMIIpv6IcmpInTimeExcds_Object = MibTableColumn
fsMIIpv6IcmpInTimeExcds = _FsMIIpv6IcmpInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 4),
    _FsMIIpv6IcmpInTimeExcds_Type()
)
fsMIIpv6IcmpInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpInTimeExcds.setStatus("current")
_FsMIIpv6IcmpInParmProbs_Type = Counter32
_FsMIIpv6IcmpInParmProbs_Object = MibTableColumn
fsMIIpv6IcmpInParmProbs = _FsMIIpv6IcmpInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 5),
    _FsMIIpv6IcmpInParmProbs_Type()
)
fsMIIpv6IcmpInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpInParmProbs.setStatus("current")
_FsMIIpv6IcmpInPktTooBigs_Type = Counter32
_FsMIIpv6IcmpInPktTooBigs_Object = MibTableColumn
fsMIIpv6IcmpInPktTooBigs = _FsMIIpv6IcmpInPktTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 6),
    _FsMIIpv6IcmpInPktTooBigs_Type()
)
fsMIIpv6IcmpInPktTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpInPktTooBigs.setStatus("current")
_FsMIIpv6IcmpInEchos_Type = Counter32
_FsMIIpv6IcmpInEchos_Object = MibTableColumn
fsMIIpv6IcmpInEchos = _FsMIIpv6IcmpInEchos_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 7),
    _FsMIIpv6IcmpInEchos_Type()
)
fsMIIpv6IcmpInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpInEchos.setStatus("current")
_FsMIIpv6IcmpInEchoReps_Type = Counter32
_FsMIIpv6IcmpInEchoReps_Object = MibTableColumn
fsMIIpv6IcmpInEchoReps = _FsMIIpv6IcmpInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 8),
    _FsMIIpv6IcmpInEchoReps_Type()
)
fsMIIpv6IcmpInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpInEchoReps.setStatus("current")
_FsMIIpv6IcmpInRouterSolicits_Type = Counter32
_FsMIIpv6IcmpInRouterSolicits_Object = MibTableColumn
fsMIIpv6IcmpInRouterSolicits = _FsMIIpv6IcmpInRouterSolicits_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 9),
    _FsMIIpv6IcmpInRouterSolicits_Type()
)
fsMIIpv6IcmpInRouterSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpInRouterSolicits.setStatus("current")
_FsMIIpv6IcmpInRouterAdvertisements_Type = Counter32
_FsMIIpv6IcmpInRouterAdvertisements_Object = MibTableColumn
fsMIIpv6IcmpInRouterAdvertisements = _FsMIIpv6IcmpInRouterAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 10),
    _FsMIIpv6IcmpInRouterAdvertisements_Type()
)
fsMIIpv6IcmpInRouterAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpInRouterAdvertisements.setStatus("current")
_FsMIIpv6IcmpInNeighborSolicits_Type = Counter32
_FsMIIpv6IcmpInNeighborSolicits_Object = MibTableColumn
fsMIIpv6IcmpInNeighborSolicits = _FsMIIpv6IcmpInNeighborSolicits_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 11),
    _FsMIIpv6IcmpInNeighborSolicits_Type()
)
fsMIIpv6IcmpInNeighborSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpInNeighborSolicits.setStatus("current")
_FsMIIpv6IcmpInNeighborAdvertisements_Type = Counter32
_FsMIIpv6IcmpInNeighborAdvertisements_Object = MibTableColumn
fsMIIpv6IcmpInNeighborAdvertisements = _FsMIIpv6IcmpInNeighborAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 12),
    _FsMIIpv6IcmpInNeighborAdvertisements_Type()
)
fsMIIpv6IcmpInNeighborAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpInNeighborAdvertisements.setStatus("current")
_FsMIIpv6IcmpInRedirects_Type = Counter32
_FsMIIpv6IcmpInRedirects_Object = MibTableColumn
fsMIIpv6IcmpInRedirects = _FsMIIpv6IcmpInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 13),
    _FsMIIpv6IcmpInRedirects_Type()
)
fsMIIpv6IcmpInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpInRedirects.setStatus("current")
_FsMIIpv6IcmpInAdminProhib_Type = Counter32
_FsMIIpv6IcmpInAdminProhib_Object = MibTableColumn
fsMIIpv6IcmpInAdminProhib = _FsMIIpv6IcmpInAdminProhib_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 14),
    _FsMIIpv6IcmpInAdminProhib_Type()
)
fsMIIpv6IcmpInAdminProhib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpInAdminProhib.setStatus("current")
_FsMIIpv6IcmpOutMsgs_Type = Counter32
_FsMIIpv6IcmpOutMsgs_Object = MibTableColumn
fsMIIpv6IcmpOutMsgs = _FsMIIpv6IcmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 15),
    _FsMIIpv6IcmpOutMsgs_Type()
)
fsMIIpv6IcmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpOutMsgs.setStatus("current")
_FsMIIpv6IcmpOutErrors_Type = Counter32
_FsMIIpv6IcmpOutErrors_Object = MibTableColumn
fsMIIpv6IcmpOutErrors = _FsMIIpv6IcmpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 16),
    _FsMIIpv6IcmpOutErrors_Type()
)
fsMIIpv6IcmpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpOutErrors.setStatus("current")
_FsMIIpv6IcmpOutDestUnreachs_Type = Counter32
_FsMIIpv6IcmpOutDestUnreachs_Object = MibTableColumn
fsMIIpv6IcmpOutDestUnreachs = _FsMIIpv6IcmpOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 17),
    _FsMIIpv6IcmpOutDestUnreachs_Type()
)
fsMIIpv6IcmpOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpOutDestUnreachs.setStatus("current")
_FsMIIpv6IcmpOutTimeExcds_Type = Counter32
_FsMIIpv6IcmpOutTimeExcds_Object = MibTableColumn
fsMIIpv6IcmpOutTimeExcds = _FsMIIpv6IcmpOutTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 18),
    _FsMIIpv6IcmpOutTimeExcds_Type()
)
fsMIIpv6IcmpOutTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpOutTimeExcds.setStatus("current")
_FsMIIpv6IcmpOutParmProbs_Type = Counter32
_FsMIIpv6IcmpOutParmProbs_Object = MibTableColumn
fsMIIpv6IcmpOutParmProbs = _FsMIIpv6IcmpOutParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 19),
    _FsMIIpv6IcmpOutParmProbs_Type()
)
fsMIIpv6IcmpOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpOutParmProbs.setStatus("current")
_FsMIIpv6IcmpOutPktTooBigs_Type = Counter32
_FsMIIpv6IcmpOutPktTooBigs_Object = MibTableColumn
fsMIIpv6IcmpOutPktTooBigs = _FsMIIpv6IcmpOutPktTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 20),
    _FsMIIpv6IcmpOutPktTooBigs_Type()
)
fsMIIpv6IcmpOutPktTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpOutPktTooBigs.setStatus("current")
_FsMIIpv6IcmpOutEchos_Type = Counter32
_FsMIIpv6IcmpOutEchos_Object = MibTableColumn
fsMIIpv6IcmpOutEchos = _FsMIIpv6IcmpOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 21),
    _FsMIIpv6IcmpOutEchos_Type()
)
fsMIIpv6IcmpOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpOutEchos.setStatus("current")
_FsMIIpv6IcmpOutEchoReps_Type = Counter32
_FsMIIpv6IcmpOutEchoReps_Object = MibTableColumn
fsMIIpv6IcmpOutEchoReps = _FsMIIpv6IcmpOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 22),
    _FsMIIpv6IcmpOutEchoReps_Type()
)
fsMIIpv6IcmpOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpOutEchoReps.setStatus("current")
_FsMIIpv6IcmpOutRouterSolicits_Type = Counter32
_FsMIIpv6IcmpOutRouterSolicits_Object = MibTableColumn
fsMIIpv6IcmpOutRouterSolicits = _FsMIIpv6IcmpOutRouterSolicits_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 23),
    _FsMIIpv6IcmpOutRouterSolicits_Type()
)
fsMIIpv6IcmpOutRouterSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpOutRouterSolicits.setStatus("current")
_FsMIIpv6IcmpOutRouterAdvertisements_Type = Counter32
_FsMIIpv6IcmpOutRouterAdvertisements_Object = MibTableColumn
fsMIIpv6IcmpOutRouterAdvertisements = _FsMIIpv6IcmpOutRouterAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 24),
    _FsMIIpv6IcmpOutRouterAdvertisements_Type()
)
fsMIIpv6IcmpOutRouterAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpOutRouterAdvertisements.setStatus("current")
_FsMIIpv6IcmpOutNeighborSolicits_Type = Counter32
_FsMIIpv6IcmpOutNeighborSolicits_Object = MibTableColumn
fsMIIpv6IcmpOutNeighborSolicits = _FsMIIpv6IcmpOutNeighborSolicits_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 25),
    _FsMIIpv6IcmpOutNeighborSolicits_Type()
)
fsMIIpv6IcmpOutNeighborSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpOutNeighborSolicits.setStatus("current")
_FsMIIpv6IcmpOutNeighborAdvertisements_Type = Counter32
_FsMIIpv6IcmpOutNeighborAdvertisements_Object = MibTableColumn
fsMIIpv6IcmpOutNeighborAdvertisements = _FsMIIpv6IcmpOutNeighborAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 26),
    _FsMIIpv6IcmpOutNeighborAdvertisements_Type()
)
fsMIIpv6IcmpOutNeighborAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpOutNeighborAdvertisements.setStatus("current")
_FsMIIpv6IcmpOutRedirects_Type = Counter32
_FsMIIpv6IcmpOutRedirects_Object = MibTableColumn
fsMIIpv6IcmpOutRedirects = _FsMIIpv6IcmpOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 27),
    _FsMIIpv6IcmpOutRedirects_Type()
)
fsMIIpv6IcmpOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpOutRedirects.setStatus("current")
_FsMIIpv6IcmpOutAdminProhib_Type = Counter32
_FsMIIpv6IcmpOutAdminProhib_Object = MibTableColumn
fsMIIpv6IcmpOutAdminProhib = _FsMIIpv6IcmpOutAdminProhib_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 28),
    _FsMIIpv6IcmpOutAdminProhib_Type()
)
fsMIIpv6IcmpOutAdminProhib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpOutAdminProhib.setStatus("current")
_FsMIIpv6IcmpInBadCode_Type = Counter32
_FsMIIpv6IcmpInBadCode_Object = MibTableColumn
fsMIIpv6IcmpInBadCode = _FsMIIpv6IcmpInBadCode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 29),
    _FsMIIpv6IcmpInBadCode_Type()
)
fsMIIpv6IcmpInBadCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpInBadCode.setStatus("current")
_FsMIIpv6IcmpInNARouterFlagSet_Type = Counter32
_FsMIIpv6IcmpInNARouterFlagSet_Object = MibTableColumn
fsMIIpv6IcmpInNARouterFlagSet = _FsMIIpv6IcmpInNARouterFlagSet_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 30),
    _FsMIIpv6IcmpInNARouterFlagSet_Type()
)
fsMIIpv6IcmpInNARouterFlagSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpInNARouterFlagSet.setStatus("current")
_FsMIIpv6IcmpInNASolicitedFlagSet_Type = Counter32
_FsMIIpv6IcmpInNASolicitedFlagSet_Object = MibTableColumn
fsMIIpv6IcmpInNASolicitedFlagSet = _FsMIIpv6IcmpInNASolicitedFlagSet_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 31),
    _FsMIIpv6IcmpInNASolicitedFlagSet_Type()
)
fsMIIpv6IcmpInNASolicitedFlagSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpInNASolicitedFlagSet.setStatus("current")
_FsMIIpv6IcmpInNAOverrideFlagSet_Type = Counter32
_FsMIIpv6IcmpInNAOverrideFlagSet_Object = MibTableColumn
fsMIIpv6IcmpInNAOverrideFlagSet = _FsMIIpv6IcmpInNAOverrideFlagSet_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 32),
    _FsMIIpv6IcmpInNAOverrideFlagSet_Type()
)
fsMIIpv6IcmpInNAOverrideFlagSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpInNAOverrideFlagSet.setStatus("current")
_FsMIIpv6IcmpOutNARouterFlagSet_Type = Counter32
_FsMIIpv6IcmpOutNARouterFlagSet_Object = MibTableColumn
fsMIIpv6IcmpOutNARouterFlagSet = _FsMIIpv6IcmpOutNARouterFlagSet_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 33),
    _FsMIIpv6IcmpOutNARouterFlagSet_Type()
)
fsMIIpv6IcmpOutNARouterFlagSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpOutNARouterFlagSet.setStatus("current")
_FsMIIpv6IcmpOutNASolicitedFlagSet_Type = Counter32
_FsMIIpv6IcmpOutNASolicitedFlagSet_Object = MibTableColumn
fsMIIpv6IcmpOutNASolicitedFlagSet = _FsMIIpv6IcmpOutNASolicitedFlagSet_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 34),
    _FsMIIpv6IcmpOutNASolicitedFlagSet_Type()
)
fsMIIpv6IcmpOutNASolicitedFlagSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpOutNASolicitedFlagSet.setStatus("current")
_FsMIIpv6IcmpOutNAOverrideFlagSet_Type = Counter32
_FsMIIpv6IcmpOutNAOverrideFlagSet_Object = MibTableColumn
fsMIIpv6IcmpOutNAOverrideFlagSet = _FsMIIpv6IcmpOutNAOverrideFlagSet_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 6, 1, 35),
    _FsMIIpv6IcmpOutNAOverrideFlagSet_Type()
)
fsMIIpv6IcmpOutNAOverrideFlagSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IcmpOutNAOverrideFlagSet.setStatus("current")
_FsMIIpv6PmtuTable_Object = MibTable
fsMIIpv6PmtuTable = _FsMIIpv6PmtuTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 7)
)
if mibBuilder.loadTexts:
    fsMIIpv6PmtuTable.setStatus("current")
_FsMIIpv6PmtuEntry_Object = MibTableRow
fsMIIpv6PmtuEntry = _FsMIIpv6PmtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 7, 1)
)
fsMIIpv6PmtuEntry.setIndexNames(
    (0, "SUPERMICRO-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
    (0, "SUPERMICRO-MIIPV6-MIB", "fsMIIpv6PmtuDest"),
)
if mibBuilder.loadTexts:
    fsMIIpv6PmtuEntry.setStatus("current")


class _FsMIIpv6PmtuDest_Type(OctetString):
    """Custom type fsMIIpv6PmtuDest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIIpv6PmtuDest_Type.__name__ = "OctetString"
_FsMIIpv6PmtuDest_Object = MibTableColumn
fsMIIpv6PmtuDest = _FsMIIpv6PmtuDest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 7, 1, 1),
    _FsMIIpv6PmtuDest_Type()
)
fsMIIpv6PmtuDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpv6PmtuDest.setStatus("current")
_FsMIIpv6Pmtu_Type = Integer32
_FsMIIpv6Pmtu_Object = MibTableColumn
fsMIIpv6Pmtu = _FsMIIpv6Pmtu_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 7, 1, 2),
    _FsMIIpv6Pmtu_Type()
)
fsMIIpv6Pmtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6Pmtu.setStatus("current")
_FsMIIpv6PmtuTimeStamp_Type = Integer32
_FsMIIpv6PmtuTimeStamp_Object = MibTableColumn
fsMIIpv6PmtuTimeStamp = _FsMIIpv6PmtuTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 7, 1, 3),
    _FsMIIpv6PmtuTimeStamp_Type()
)
fsMIIpv6PmtuTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6PmtuTimeStamp.setStatus("current")


class _FsMIIpv6PmtuAdminStatus_Type(Integer32):
    """Custom type fsMIIpv6PmtuAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_FsMIIpv6PmtuAdminStatus_Type.__name__ = "Integer32"
_FsMIIpv6PmtuAdminStatus_Object = MibTableColumn
fsMIIpv6PmtuAdminStatus = _FsMIIpv6PmtuAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 7, 1, 4),
    _FsMIIpv6PmtuAdminStatus_Type()
)
fsMIIpv6PmtuAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6PmtuAdminStatus.setStatus("current")
_FsMIIpv6NDProxyListTable_Object = MibTable
fsMIIpv6NDProxyListTable = _FsMIIpv6NDProxyListTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 9)
)
if mibBuilder.loadTexts:
    fsMIIpv6NDProxyListTable.setStatus("current")
_FsMIIpv6NDProxyListEntry_Object = MibTableRow
fsMIIpv6NDProxyListEntry = _FsMIIpv6NDProxyListEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 9, 1)
)
fsMIIpv6NDProxyListEntry.setIndexNames(
    (0, "SUPERMICRO-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
    (0, "SUPERMICRO-MIIPV6-MIB", "fsMIIpv6NDProxyAddr"),
)
if mibBuilder.loadTexts:
    fsMIIpv6NDProxyListEntry.setStatus("current")


class _FsMIIpv6NDProxyAddr_Type(OctetString):
    """Custom type fsMIIpv6NDProxyAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIIpv6NDProxyAddr_Type.__name__ = "OctetString"
_FsMIIpv6NDProxyAddr_Object = MibTableColumn
fsMIIpv6NDProxyAddr = _FsMIIpv6NDProxyAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 9, 1, 1),
    _FsMIIpv6NDProxyAddr_Type()
)
fsMIIpv6NDProxyAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpv6NDProxyAddr.setStatus("current")


class _FsMIIpv6NDProxyAdminStatus_Type(Integer32):
    """Custom type fsMIIpv6NDProxyAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("invalid", 2))
    )


_FsMIIpv6NDProxyAdminStatus_Type.__name__ = "Integer32"
_FsMIIpv6NDProxyAdminStatus_Object = MibTableColumn
fsMIIpv6NDProxyAdminStatus = _FsMIIpv6NDProxyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 9, 1, 2),
    _FsMIIpv6NDProxyAdminStatus_Type()
)
fsMIIpv6NDProxyAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6NDProxyAdminStatus.setStatus("current")
_FsMIIpv6PingTable_Object = MibTable
fsMIIpv6PingTable = _FsMIIpv6PingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10)
)
if mibBuilder.loadTexts:
    fsMIIpv6PingTable.setStatus("current")
_FsMIIpv6PingEntry_Object = MibTableRow
fsMIIpv6PingEntry = _FsMIIpv6PingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1)
)
fsMIIpv6PingEntry.setIndexNames(
    (0, "SUPERMICRO-MIIPV6-MIB", "fsMIIpv6PingIndex"),
)
if mibBuilder.loadTexts:
    fsMIIpv6PingEntry.setStatus("current")


class _FsMIIpv6PingIndex_Type(Integer32):
    """Custom type fsMIIpv6PingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_FsMIIpv6PingIndex_Type.__name__ = "Integer32"
_FsMIIpv6PingIndex_Object = MibTableColumn
fsMIIpv6PingIndex = _FsMIIpv6PingIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 1),
    _FsMIIpv6PingIndex_Type()
)
fsMIIpv6PingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpv6PingIndex.setStatus("current")


class _FsMIIpv6PingDest_Type(OctetString):
    """Custom type fsMIIpv6PingDest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIIpv6PingDest_Type.__name__ = "OctetString"
_FsMIIpv6PingDest_Object = MibTableColumn
fsMIIpv6PingDest = _FsMIIpv6PingDest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 2),
    _FsMIIpv6PingDest_Type()
)
fsMIIpv6PingDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6PingDest.setStatus("current")
_FsMIIpv6PingIfIndex_Type = InterfaceIndex
_FsMIIpv6PingIfIndex_Object = MibTableColumn
fsMIIpv6PingIfIndex = _FsMIIpv6PingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 3),
    _FsMIIpv6PingIfIndex_Type()
)
fsMIIpv6PingIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6PingIfIndex.setStatus("current")


class _FsMIIpv6PingContextId_Type(Integer32):
    """Custom type fsMIIpv6PingContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIIpv6PingContextId_Type.__name__ = "Integer32"
_FsMIIpv6PingContextId_Object = MibTableColumn
fsMIIpv6PingContextId = _FsMIIpv6PingContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 4),
    _FsMIIpv6PingContextId_Type()
)
fsMIIpv6PingContextId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6PingContextId.setStatus("current")


class _FsMIIpv6PingAdminStatus_Type(Integer32):
    """Custom type fsMIIpv6PingAdminStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("invalid", 3),
          ("create", 4))
    )


_FsMIIpv6PingAdminStatus_Type.__name__ = "Integer32"
_FsMIIpv6PingAdminStatus_Object = MibTableColumn
fsMIIpv6PingAdminStatus = _FsMIIpv6PingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 5),
    _FsMIIpv6PingAdminStatus_Type()
)
fsMIIpv6PingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6PingAdminStatus.setStatus("current")


class _FsMIIpv6PingInterval_Type(Integer32):
    """Custom type fsMIIpv6PingInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsMIIpv6PingInterval_Type.__name__ = "Integer32"
_FsMIIpv6PingInterval_Object = MibTableColumn
fsMIIpv6PingInterval = _FsMIIpv6PingInterval_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 6),
    _FsMIIpv6PingInterval_Type()
)
fsMIIpv6PingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6PingInterval.setStatus("current")


class _FsMIIpv6PingRcvTimeout_Type(Integer32):
    """Custom type fsMIIpv6PingRcvTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsMIIpv6PingRcvTimeout_Type.__name__ = "Integer32"
_FsMIIpv6PingRcvTimeout_Object = MibTableColumn
fsMIIpv6PingRcvTimeout = _FsMIIpv6PingRcvTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 7),
    _FsMIIpv6PingRcvTimeout_Type()
)
fsMIIpv6PingRcvTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6PingRcvTimeout.setStatus("current")


class _FsMIIpv6PingTries_Type(Integer32):
    """Custom type fsMIIpv6PingTries based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FsMIIpv6PingTries_Type.__name__ = "Integer32"
_FsMIIpv6PingTries_Object = MibTableColumn
fsMIIpv6PingTries = _FsMIIpv6PingTries_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 8),
    _FsMIIpv6PingTries_Type()
)
fsMIIpv6PingTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6PingTries.setStatus("current")


class _FsMIIpv6PingSize_Type(Integer32):
    """Custom type fsMIIpv6PingSize based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 2080),
    )


_FsMIIpv6PingSize_Type.__name__ = "Integer32"
_FsMIIpv6PingSize_Object = MibTableColumn
fsMIIpv6PingSize = _FsMIIpv6PingSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 9),
    _FsMIIpv6PingSize_Type()
)
fsMIIpv6PingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6PingSize.setStatus("current")
_FsMIIpv6PingSentCount_Type = Integer32
_FsMIIpv6PingSentCount_Object = MibTableColumn
fsMIIpv6PingSentCount = _FsMIIpv6PingSentCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 10),
    _FsMIIpv6PingSentCount_Type()
)
fsMIIpv6PingSentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6PingSentCount.setStatus("current")
_FsMIIpv6PingAverageTime_Type = Integer32
_FsMIIpv6PingAverageTime_Object = MibTableColumn
fsMIIpv6PingAverageTime = _FsMIIpv6PingAverageTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 11),
    _FsMIIpv6PingAverageTime_Type()
)
fsMIIpv6PingAverageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6PingAverageTime.setStatus("current")
_FsMIIpv6PingMaxTime_Type = Integer32
_FsMIIpv6PingMaxTime_Object = MibTableColumn
fsMIIpv6PingMaxTime = _FsMIIpv6PingMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 12),
    _FsMIIpv6PingMaxTime_Type()
)
fsMIIpv6PingMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6PingMaxTime.setStatus("current")
_FsMIIpv6PingMinTime_Type = Integer32
_FsMIIpv6PingMinTime_Object = MibTableColumn
fsMIIpv6PingMinTime = _FsMIIpv6PingMinTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 13),
    _FsMIIpv6PingMinTime_Type()
)
fsMIIpv6PingMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6PingMinTime.setStatus("current")


class _FsMIIpv6PingOperStatus_Type(Integer32):
    """Custom type fsMIIpv6PingOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inprogress", 1),
          ("notinprogress", 2))
    )


_FsMIIpv6PingOperStatus_Type.__name__ = "Integer32"
_FsMIIpv6PingOperStatus_Object = MibTableColumn
fsMIIpv6PingOperStatus = _FsMIIpv6PingOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 14),
    _FsMIIpv6PingOperStatus_Type()
)
fsMIIpv6PingOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6PingOperStatus.setStatus("current")
_FsMIIpv6PingSuccesses_Type = Counter32
_FsMIIpv6PingSuccesses_Object = MibTableColumn
fsMIIpv6PingSuccesses = _FsMIIpv6PingSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 15),
    _FsMIIpv6PingSuccesses_Type()
)
fsMIIpv6PingSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6PingSuccesses.setStatus("current")
_FsMIIpv6PingPercentageLoss_Type = Integer32
_FsMIIpv6PingPercentageLoss_Object = MibTableColumn
fsMIIpv6PingPercentageLoss = _FsMIIpv6PingPercentageLoss_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 16),
    _FsMIIpv6PingPercentageLoss_Type()
)
fsMIIpv6PingPercentageLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6PingPercentageLoss.setStatus("current")


class _FsMIIpv6PingData_Type(OctetString):
    """Custom type fsMIIpv6PingData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_FsMIIpv6PingData_Type.__name__ = "OctetString"
_FsMIIpv6PingData_Object = MibTableColumn
fsMIIpv6PingData = _FsMIIpv6PingData_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 17),
    _FsMIIpv6PingData_Type()
)
fsMIIpv6PingData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6PingData.setStatus("current")


class _FsMIIpv6PingSrcAddr_Type(OctetString):
    """Custom type fsMIIpv6PingSrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIIpv6PingSrcAddr_Type.__name__ = "OctetString"
_FsMIIpv6PingSrcAddr_Object = MibTableColumn
fsMIIpv6PingSrcAddr = _FsMIIpv6PingSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 18),
    _FsMIIpv6PingSrcAddr_Type()
)
fsMIIpv6PingSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6PingSrcAddr.setStatus("current")
_FsMIIpv6PingZoneId_Type = DisplayString
_FsMIIpv6PingZoneId_Object = MibTableColumn
fsMIIpv6PingZoneId = _FsMIIpv6PingZoneId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 19),
    _FsMIIpv6PingZoneId_Type()
)
fsMIIpv6PingZoneId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6PingZoneId.setStatus("current")


class _FsMIIpv6PingDestAddrType_Type(Integer32):
    """Custom type fsMIIpv6PingDestAddrType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("anycast", 2))
    )


_FsMIIpv6PingDestAddrType_Type.__name__ = "Integer32"
_FsMIIpv6PingDestAddrType_Object = MibTableColumn
fsMIIpv6PingDestAddrType = _FsMIIpv6PingDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 10, 1, 20),
    _FsMIIpv6PingDestAddrType_Type()
)
fsMIIpv6PingDestAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6PingDestAddrType.setStatus("current")
_FsMIIpv6GlobalDebug_Type = Unsigned32
_FsMIIpv6GlobalDebug_Object = MibScalar
fsMIIpv6GlobalDebug = _FsMIIpv6GlobalDebug_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 11),
    _FsMIIpv6GlobalDebug_Type()
)
fsMIIpv6GlobalDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6GlobalDebug.setStatus("current")
_FsMIIpv6AddrSelPolicyTable_Object = MibTable
fsMIIpv6AddrSelPolicyTable = _FsMIIpv6AddrSelPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 12)
)
if mibBuilder.loadTexts:
    fsMIIpv6AddrSelPolicyTable.setStatus("current")
_FsMIIpv6AddrSelPolicyEntry_Object = MibTableRow
fsMIIpv6AddrSelPolicyEntry = _FsMIIpv6AddrSelPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 12, 1)
)
fsMIIpv6AddrSelPolicyEntry.setIndexNames(
    (0, "SUPERMICRO-MIIPV6-MIB", "fsMIIpv6AddrSelPolicyPrefix"),
    (0, "SUPERMICRO-MIIPV6-MIB", "fsMIIpv6AddrSelPolicyPrefixLen"),
    (0, "SUPERMICRO-MIIPV6-MIB", "fsMIIpv6AddrSelPolicyIfIndex"),
)
if mibBuilder.loadTexts:
    fsMIIpv6AddrSelPolicyEntry.setStatus("current")


class _FsMIIpv6AddrSelPolicyPrefix_Type(OctetString):
    """Custom type fsMIIpv6AddrSelPolicyPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIIpv6AddrSelPolicyPrefix_Type.__name__ = "OctetString"
_FsMIIpv6AddrSelPolicyPrefix_Object = MibTableColumn
fsMIIpv6AddrSelPolicyPrefix = _FsMIIpv6AddrSelPolicyPrefix_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 12, 1, 1),
    _FsMIIpv6AddrSelPolicyPrefix_Type()
)
fsMIIpv6AddrSelPolicyPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpv6AddrSelPolicyPrefix.setStatus("current")


class _FsMIIpv6AddrSelPolicyPrefixLen_Type(Integer32):
    """Custom type fsMIIpv6AddrSelPolicyPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_FsMIIpv6AddrSelPolicyPrefixLen_Type.__name__ = "Integer32"
_FsMIIpv6AddrSelPolicyPrefixLen_Object = MibTableColumn
fsMIIpv6AddrSelPolicyPrefixLen = _FsMIIpv6AddrSelPolicyPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 12, 1, 2),
    _FsMIIpv6AddrSelPolicyPrefixLen_Type()
)
fsMIIpv6AddrSelPolicyPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpv6AddrSelPolicyPrefixLen.setStatus("current")
_FsMIIpv6AddrSelPolicyIfIndex_Type = InterfaceIndex
_FsMIIpv6AddrSelPolicyIfIndex_Object = MibTableColumn
fsMIIpv6AddrSelPolicyIfIndex = _FsMIIpv6AddrSelPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 12, 1, 3),
    _FsMIIpv6AddrSelPolicyIfIndex_Type()
)
fsMIIpv6AddrSelPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpv6AddrSelPolicyIfIndex.setStatus("current")


class _FsMIIpv6AddrSelPolicyScope_Type(Integer32):
    """Custom type fsMIIpv6AddrSelPolicyScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsMIIpv6AddrSelPolicyScope_Type.__name__ = "Integer32"
_FsMIIpv6AddrSelPolicyScope_Object = MibTableColumn
fsMIIpv6AddrSelPolicyScope = _FsMIIpv6AddrSelPolicyScope_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 12, 1, 4),
    _FsMIIpv6AddrSelPolicyScope_Type()
)
fsMIIpv6AddrSelPolicyScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6AddrSelPolicyScope.setStatus("current")


class _FsMIIpv6AddrSelPolicyPrecedence_Type(Integer32):
    """Custom type fsMIIpv6AddrSelPolicyPrecedence based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_FsMIIpv6AddrSelPolicyPrecedence_Type.__name__ = "Integer32"
_FsMIIpv6AddrSelPolicyPrecedence_Object = MibTableColumn
fsMIIpv6AddrSelPolicyPrecedence = _FsMIIpv6AddrSelPolicyPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 12, 1, 5),
    _FsMIIpv6AddrSelPolicyPrecedence_Type()
)
fsMIIpv6AddrSelPolicyPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6AddrSelPolicyPrecedence.setStatus("current")


class _FsMIIpv6AddrSelPolicyLabel_Type(Integer32):
    """Custom type fsMIIpv6AddrSelPolicyLabel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIIpv6AddrSelPolicyLabel_Type.__name__ = "Integer32"
_FsMIIpv6AddrSelPolicyLabel_Object = MibTableColumn
fsMIIpv6AddrSelPolicyLabel = _FsMIIpv6AddrSelPolicyLabel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 12, 1, 6),
    _FsMIIpv6AddrSelPolicyLabel_Type()
)
fsMIIpv6AddrSelPolicyLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6AddrSelPolicyLabel.setStatus("current")


class _FsMIIpv6AddrSelPolicyAddrType_Type(Integer32):
    """Custom type fsMIIpv6AddrSelPolicyAddrType based on Integer32"""
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
          ("multicast", 3))
    )


_FsMIIpv6AddrSelPolicyAddrType_Type.__name__ = "Integer32"
_FsMIIpv6AddrSelPolicyAddrType_Object = MibTableColumn
fsMIIpv6AddrSelPolicyAddrType = _FsMIIpv6AddrSelPolicyAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 12, 1, 7),
    _FsMIIpv6AddrSelPolicyAddrType_Type()
)
fsMIIpv6AddrSelPolicyAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6AddrSelPolicyAddrType.setStatus("current")


class _FsMIIpv6AddrSelPolicyIsPublicAddr_Type(Integer32):
    """Custom type fsMIIpv6AddrSelPolicyIsPublicAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_FsMIIpv6AddrSelPolicyIsPublicAddr_Type.__name__ = "Integer32"
_FsMIIpv6AddrSelPolicyIsPublicAddr_Object = MibTableColumn
fsMIIpv6AddrSelPolicyIsPublicAddr = _FsMIIpv6AddrSelPolicyIsPublicAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 12, 1, 8),
    _FsMIIpv6AddrSelPolicyIsPublicAddr_Type()
)
fsMIIpv6AddrSelPolicyIsPublicAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6AddrSelPolicyIsPublicAddr.setStatus("current")


class _FsMIIpv6AddrSelPolicyIsSelfAddr_Type(Integer32):
    """Custom type fsMIIpv6AddrSelPolicyIsSelfAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_FsMIIpv6AddrSelPolicyIsSelfAddr_Type.__name__ = "Integer32"
_FsMIIpv6AddrSelPolicyIsSelfAddr_Object = MibTableColumn
fsMIIpv6AddrSelPolicyIsSelfAddr = _FsMIIpv6AddrSelPolicyIsSelfAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 12, 1, 9),
    _FsMIIpv6AddrSelPolicyIsSelfAddr_Type()
)
fsMIIpv6AddrSelPolicyIsSelfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6AddrSelPolicyIsSelfAddr.setStatus("current")


class _FsMIIpv6AddrSelPolicyReachabilityStatus_Type(Integer32):
    """Custom type fsMIIpv6AddrSelPolicyReachabilityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 1),
          ("unreachable", 2))
    )


_FsMIIpv6AddrSelPolicyReachabilityStatus_Type.__name__ = "Integer32"
_FsMIIpv6AddrSelPolicyReachabilityStatus_Object = MibTableColumn
fsMIIpv6AddrSelPolicyReachabilityStatus = _FsMIIpv6AddrSelPolicyReachabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 12, 1, 10),
    _FsMIIpv6AddrSelPolicyReachabilityStatus_Type()
)
fsMIIpv6AddrSelPolicyReachabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6AddrSelPolicyReachabilityStatus.setStatus("current")


class _FsMIIpv6AddrSelPolicyConfigStatus_Type(Integer32):
    """Custom type fsMIIpv6AddrSelPolicyConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("management", 2))
    )


_FsMIIpv6AddrSelPolicyConfigStatus_Type.__name__ = "Integer32"
_FsMIIpv6AddrSelPolicyConfigStatus_Object = MibTableColumn
fsMIIpv6AddrSelPolicyConfigStatus = _FsMIIpv6AddrSelPolicyConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 12, 1, 11),
    _FsMIIpv6AddrSelPolicyConfigStatus_Type()
)
fsMIIpv6AddrSelPolicyConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6AddrSelPolicyConfigStatus.setStatus("current")
_FsMIIpv6AddrSelPolicyRowStatus_Type = RowStatus
_FsMIIpv6AddrSelPolicyRowStatus_Object = MibTableColumn
fsMIIpv6AddrSelPolicyRowStatus = _FsMIIpv6AddrSelPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 12, 1, 12),
    _FsMIIpv6AddrSelPolicyRowStatus_Type()
)
fsMIIpv6AddrSelPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIIpv6AddrSelPolicyRowStatus.setStatus("current")
_FsMIIpv6IfScopeZoneMapTable_Object = MibTable
fsMIIpv6IfScopeZoneMapTable = _FsMIIpv6IfScopeZoneMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13)
)
if mibBuilder.loadTexts:
    fsMIIpv6IfScopeZoneMapTable.setStatus("current")
_FsMIIpv6IfScopeZoneMapEntry_Object = MibTableRow
fsMIIpv6IfScopeZoneMapEntry = _FsMIIpv6IfScopeZoneMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13, 1)
)
fsMIIpv6IfScopeZoneMapEntry.setIndexNames(
    (0, "SUPERMICRO-MIIPV6-MIB", "fsMIIpv6ScopeZoneIndexIfIndex"),
)
if mibBuilder.loadTexts:
    fsMIIpv6IfScopeZoneMapEntry.setStatus("current")
_FsMIIpv6ScopeZoneIndexIfIndex_Type = InterfaceIndex
_FsMIIpv6ScopeZoneIndexIfIndex_Object = MibTableColumn
fsMIIpv6ScopeZoneIndexIfIndex = _FsMIIpv6ScopeZoneIndexIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13, 1, 1),
    _FsMIIpv6ScopeZoneIndexIfIndex_Type()
)
fsMIIpv6ScopeZoneIndexIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneIndexIfIndex.setStatus("current")


class _FsMIIpv6ScopeZoneIndexInterfaceLocal_Type(DisplayString):
    """Custom type fsMIIpv6ScopeZoneIndexInterfaceLocal based on DisplayString"""
    defaultValue = OctetString("Invalid")


_FsMIIpv6ScopeZoneIndexInterfaceLocal_Type.__name__ = "DisplayString"
_FsMIIpv6ScopeZoneIndexInterfaceLocal_Object = MibTableColumn
fsMIIpv6ScopeZoneIndexInterfaceLocal = _FsMIIpv6ScopeZoneIndexInterfaceLocal_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13, 1, 2),
    _FsMIIpv6ScopeZoneIndexInterfaceLocal_Type()
)
fsMIIpv6ScopeZoneIndexInterfaceLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneIndexInterfaceLocal.setStatus("current")


class _FsMIIpv6ScopeZoneIndexLinkLocal_Type(DisplayString):
    """Custom type fsMIIpv6ScopeZoneIndexLinkLocal based on DisplayString"""
    defaultValue = OctetString("Invalid")


_FsMIIpv6ScopeZoneIndexLinkLocal_Type.__name__ = "DisplayString"
_FsMIIpv6ScopeZoneIndexLinkLocal_Object = MibTableColumn
fsMIIpv6ScopeZoneIndexLinkLocal = _FsMIIpv6ScopeZoneIndexLinkLocal_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13, 1, 3),
    _FsMIIpv6ScopeZoneIndexLinkLocal_Type()
)
fsMIIpv6ScopeZoneIndexLinkLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneIndexLinkLocal.setStatus("current")


class _FsMIIpv6ScopeZoneIndex3_Type(DisplayString):
    """Custom type fsMIIpv6ScopeZoneIndex3 based on DisplayString"""
    defaultValue = OctetString("Invalid")


_FsMIIpv6ScopeZoneIndex3_Type.__name__ = "DisplayString"
_FsMIIpv6ScopeZoneIndex3_Object = MibTableColumn
fsMIIpv6ScopeZoneIndex3 = _FsMIIpv6ScopeZoneIndex3_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13, 1, 4),
    _FsMIIpv6ScopeZoneIndex3_Type()
)
fsMIIpv6ScopeZoneIndex3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneIndex3.setStatus("current")


class _FsMIIpv6ScopeZoneIndexAdminLocal_Type(DisplayString):
    """Custom type fsMIIpv6ScopeZoneIndexAdminLocal based on DisplayString"""
    defaultValue = OctetString("Invalid")


_FsMIIpv6ScopeZoneIndexAdminLocal_Type.__name__ = "DisplayString"
_FsMIIpv6ScopeZoneIndexAdminLocal_Object = MibTableColumn
fsMIIpv6ScopeZoneIndexAdminLocal = _FsMIIpv6ScopeZoneIndexAdminLocal_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13, 1, 5),
    _FsMIIpv6ScopeZoneIndexAdminLocal_Type()
)
fsMIIpv6ScopeZoneIndexAdminLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneIndexAdminLocal.setStatus("current")


class _FsMIIpv6ScopeZoneIndexSiteLocal_Type(DisplayString):
    """Custom type fsMIIpv6ScopeZoneIndexSiteLocal based on DisplayString"""
    defaultValue = OctetString("Invalid")


_FsMIIpv6ScopeZoneIndexSiteLocal_Type.__name__ = "DisplayString"
_FsMIIpv6ScopeZoneIndexSiteLocal_Object = MibTableColumn
fsMIIpv6ScopeZoneIndexSiteLocal = _FsMIIpv6ScopeZoneIndexSiteLocal_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13, 1, 6),
    _FsMIIpv6ScopeZoneIndexSiteLocal_Type()
)
fsMIIpv6ScopeZoneIndexSiteLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneIndexSiteLocal.setStatus("current")


class _FsMIIpv6ScopeZoneIndex6_Type(DisplayString):
    """Custom type fsMIIpv6ScopeZoneIndex6 based on DisplayString"""
    defaultValue = OctetString("Invalid")


_FsMIIpv6ScopeZoneIndex6_Type.__name__ = "DisplayString"
_FsMIIpv6ScopeZoneIndex6_Object = MibTableColumn
fsMIIpv6ScopeZoneIndex6 = _FsMIIpv6ScopeZoneIndex6_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13, 1, 7),
    _FsMIIpv6ScopeZoneIndex6_Type()
)
fsMIIpv6ScopeZoneIndex6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneIndex6.setStatus("current")


class _FsMIIpv6ScopeZoneIndex7_Type(DisplayString):
    """Custom type fsMIIpv6ScopeZoneIndex7 based on DisplayString"""
    defaultValue = OctetString("Invalid")


_FsMIIpv6ScopeZoneIndex7_Type.__name__ = "DisplayString"
_FsMIIpv6ScopeZoneIndex7_Object = MibTableColumn
fsMIIpv6ScopeZoneIndex7 = _FsMIIpv6ScopeZoneIndex7_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13, 1, 8),
    _FsMIIpv6ScopeZoneIndex7_Type()
)
fsMIIpv6ScopeZoneIndex7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneIndex7.setStatus("current")


class _FsMIIpv6ScopeZoneIndexOrganizationLocal_Type(DisplayString):
    """Custom type fsMIIpv6ScopeZoneIndexOrganizationLocal based on DisplayString"""
    defaultValue = OctetString("Invalid")


_FsMIIpv6ScopeZoneIndexOrganizationLocal_Type.__name__ = "DisplayString"
_FsMIIpv6ScopeZoneIndexOrganizationLocal_Object = MibTableColumn
fsMIIpv6ScopeZoneIndexOrganizationLocal = _FsMIIpv6ScopeZoneIndexOrganizationLocal_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13, 1, 9),
    _FsMIIpv6ScopeZoneIndexOrganizationLocal_Type()
)
fsMIIpv6ScopeZoneIndexOrganizationLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneIndexOrganizationLocal.setStatus("current")


class _FsMIIpv6ScopeZoneIndex9_Type(DisplayString):
    """Custom type fsMIIpv6ScopeZoneIndex9 based on DisplayString"""
    defaultValue = OctetString("Invalid")


_FsMIIpv6ScopeZoneIndex9_Type.__name__ = "DisplayString"
_FsMIIpv6ScopeZoneIndex9_Object = MibTableColumn
fsMIIpv6ScopeZoneIndex9 = _FsMIIpv6ScopeZoneIndex9_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13, 1, 10),
    _FsMIIpv6ScopeZoneIndex9_Type()
)
fsMIIpv6ScopeZoneIndex9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneIndex9.setStatus("current")


class _FsMIIpv6ScopeZoneIndexA_Type(DisplayString):
    """Custom type fsMIIpv6ScopeZoneIndexA based on DisplayString"""
    defaultValue = OctetString("Invalid")


_FsMIIpv6ScopeZoneIndexA_Type.__name__ = "DisplayString"
_FsMIIpv6ScopeZoneIndexA_Object = MibTableColumn
fsMIIpv6ScopeZoneIndexA = _FsMIIpv6ScopeZoneIndexA_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13, 1, 11),
    _FsMIIpv6ScopeZoneIndexA_Type()
)
fsMIIpv6ScopeZoneIndexA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneIndexA.setStatus("current")


class _FsMIIpv6ScopeZoneIndexB_Type(DisplayString):
    """Custom type fsMIIpv6ScopeZoneIndexB based on DisplayString"""
    defaultValue = OctetString("Invalid")


_FsMIIpv6ScopeZoneIndexB_Type.__name__ = "DisplayString"
_FsMIIpv6ScopeZoneIndexB_Object = MibTableColumn
fsMIIpv6ScopeZoneIndexB = _FsMIIpv6ScopeZoneIndexB_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13, 1, 12),
    _FsMIIpv6ScopeZoneIndexB_Type()
)
fsMIIpv6ScopeZoneIndexB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneIndexB.setStatus("current")


class _FsMIIpv6ScopeZoneIndexC_Type(DisplayString):
    """Custom type fsMIIpv6ScopeZoneIndexC based on DisplayString"""
    defaultValue = OctetString("Invalid")


_FsMIIpv6ScopeZoneIndexC_Type.__name__ = "DisplayString"
_FsMIIpv6ScopeZoneIndexC_Object = MibTableColumn
fsMIIpv6ScopeZoneIndexC = _FsMIIpv6ScopeZoneIndexC_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13, 1, 13),
    _FsMIIpv6ScopeZoneIndexC_Type()
)
fsMIIpv6ScopeZoneIndexC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneIndexC.setStatus("current")


class _FsMIIpv6ScopeZoneIndexD_Type(DisplayString):
    """Custom type fsMIIpv6ScopeZoneIndexD based on DisplayString"""
    defaultValue = OctetString("Invalid")


_FsMIIpv6ScopeZoneIndexD_Type.__name__ = "DisplayString"
_FsMIIpv6ScopeZoneIndexD_Object = MibTableColumn
fsMIIpv6ScopeZoneIndexD = _FsMIIpv6ScopeZoneIndexD_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13, 1, 14),
    _FsMIIpv6ScopeZoneIndexD_Type()
)
fsMIIpv6ScopeZoneIndexD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneIndexD.setStatus("current")


class _FsMIIpv6ScopeZoneIndexE_Type(DisplayString):
    """Custom type fsMIIpv6ScopeZoneIndexE based on DisplayString"""
    defaultValue = OctetString("Invalid")


_FsMIIpv6ScopeZoneIndexE_Type.__name__ = "DisplayString"
_FsMIIpv6ScopeZoneIndexE_Object = MibTableColumn
fsMIIpv6ScopeZoneIndexE = _FsMIIpv6ScopeZoneIndexE_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13, 1, 15),
    _FsMIIpv6ScopeZoneIndexE_Type()
)
fsMIIpv6ScopeZoneIndexE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneIndexE.setStatus("current")


class _FsMIIpv6IfScopeZoneCreationStatus_Type(Integer32):
    """Custom type fsMIIpv6IfScopeZoneCreationStatus based on Integer32"""
    defaultValue = 1

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
        *(("notcreated", 0),
          ("automatic", 1),
          ("mgmt", 2),
          ("overridden", 3))
    )


_FsMIIpv6IfScopeZoneCreationStatus_Type.__name__ = "Integer32"
_FsMIIpv6IfScopeZoneCreationStatus_Object = MibTableColumn
fsMIIpv6IfScopeZoneCreationStatus = _FsMIIpv6IfScopeZoneCreationStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13, 1, 16),
    _FsMIIpv6IfScopeZoneCreationStatus_Type()
)
fsMIIpv6IfScopeZoneCreationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6IfScopeZoneCreationStatus.setStatus("current")
_FsMIIpv6IfScopeZoneRowStatus_Type = RowStatus
_FsMIIpv6IfScopeZoneRowStatus_Object = MibTableColumn
fsMIIpv6IfScopeZoneRowStatus = _FsMIIpv6IfScopeZoneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 13, 1, 17),
    _FsMIIpv6IfScopeZoneRowStatus_Type()
)
fsMIIpv6IfScopeZoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIIpv6IfScopeZoneRowStatus.setStatus("current")
_FsMIIpv6ScopeZoneTable_Object = MibTable
fsMIIpv6ScopeZoneTable = _FsMIIpv6ScopeZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 14)
)
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneTable.setStatus("current")
_FsMIIpv6ScopeZoneEntry_Object = MibTableRow
fsMIIpv6ScopeZoneEntry = _FsMIIpv6ScopeZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 14, 1)
)
fsMIIpv6ScopeZoneEntry.setIndexNames(
    (0, "SUPERMICRO-MIIPV6-MIB", "fsMIIpv6ScopeZoneContextId"),
    (0, "SUPERMICRO-MIIPV6-MIB", "fsMIIpv6ScopeZoneName"),
)
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneEntry.setStatus("current")


class _FsMIIpv6ScopeZoneContextId_Type(Integer32):
    """Custom type fsMIIpv6ScopeZoneContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIIpv6ScopeZoneContextId_Type.__name__ = "Integer32"
_FsMIIpv6ScopeZoneContextId_Object = MibTableColumn
fsMIIpv6ScopeZoneContextId = _FsMIIpv6ScopeZoneContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 14, 1, 1),
    _FsMIIpv6ScopeZoneContextId_Type()
)
fsMIIpv6ScopeZoneContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneContextId.setStatus("current")
_FsMIIpv6ScopeZoneName_Type = DisplayString
_FsMIIpv6ScopeZoneName_Object = MibTableColumn
fsMIIpv6ScopeZoneName = _FsMIIpv6ScopeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 14, 1, 2),
    _FsMIIpv6ScopeZoneName_Type()
)
fsMIIpv6ScopeZoneName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneName.setStatus("current")
_FsMIIpv6ScopeZoneIndex_Type = InetZoneIndex
_FsMIIpv6ScopeZoneIndex_Object = MibTableColumn
fsMIIpv6ScopeZoneIndex = _FsMIIpv6ScopeZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 14, 1, 3),
    _FsMIIpv6ScopeZoneIndex_Type()
)
fsMIIpv6ScopeZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneIndex.setStatus("current")


class _FsMIIpv6ScopeZoneCreationStatus_Type(Integer32):
    """Custom type fsMIIpv6ScopeZoneCreationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("mgmt", 2),
          ("overridden", 3))
    )


_FsMIIpv6ScopeZoneCreationStatus_Type.__name__ = "Integer32"
_FsMIIpv6ScopeZoneCreationStatus_Object = MibTableColumn
fsMIIpv6ScopeZoneCreationStatus = _FsMIIpv6ScopeZoneCreationStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 14, 1, 4),
    _FsMIIpv6ScopeZoneCreationStatus_Type()
)
fsMIIpv6ScopeZoneCreationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneCreationStatus.setStatus("current")
_FsMIIpv6ScopeZoneInterfaceList_Type = InterfaceList
_FsMIIpv6ScopeZoneInterfaceList_Object = MibTableColumn
fsMIIpv6ScopeZoneInterfaceList = _FsMIIpv6ScopeZoneInterfaceList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 14, 1, 5),
    _FsMIIpv6ScopeZoneInterfaceList_Type()
)
fsMIIpv6ScopeZoneInterfaceList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6ScopeZoneInterfaceList.setStatus("current")


class _FsMIIpv6IsDefaultScopeZone_Type(Integer32):
    """Custom type fsMIIpv6IsDefaultScopeZone based on Integer32"""
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


_FsMIIpv6IsDefaultScopeZone_Type.__name__ = "Integer32"
_FsMIIpv6IsDefaultScopeZone_Object = MibTableColumn
fsMIIpv6IsDefaultScopeZone = _FsMIIpv6IsDefaultScopeZone_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 1, 14, 1, 6),
    _FsMIIpv6IsDefaultScopeZone_Type()
)
fsMIIpv6IsDefaultScopeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6IsDefaultScopeZone.setStatus("current")
_FsMIipv6Route_ObjectIdentity = ObjectIdentity
fsMIipv6Route = _FsMIipv6Route_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 2)
)
_FsMIIpv6PrefTable_Object = MibTable
fsMIIpv6PrefTable = _FsMIIpv6PrefTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 2, 1)
)
if mibBuilder.loadTexts:
    fsMIIpv6PrefTable.setStatus("current")
_FsMIIpv6PrefEntry_Object = MibTableRow
fsMIIpv6PrefEntry = _FsMIIpv6PrefEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 2, 1, 1)
)
fsMIIpv6PrefEntry.setIndexNames(
    (0, "SUPERMICRO-MISTD-IPVX-MIB", "fsMIStdIpContextId"),
    (0, "SUPERMICRO-MIIPV6-MIB", "fsMIIpv6Protocol"),
)
if mibBuilder.loadTexts:
    fsMIIpv6PrefEntry.setStatus("current")


class _FsMIIpv6Protocol_Type(Integer32):
    """Custom type fsMIIpv6Protocol based on Integer32"""
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
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("ndisc", 4),
          ("rip", 5),
          ("ospf", 6),
          ("bgp", 7),
          ("idrp", 8),
          ("igrp", 9))
    )


_FsMIIpv6Protocol_Type.__name__ = "Integer32"
_FsMIIpv6Protocol_Object = MibTableColumn
fsMIIpv6Protocol = _FsMIIpv6Protocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 2, 1, 1, 1),
    _FsMIIpv6Protocol_Type()
)
fsMIIpv6Protocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpv6Protocol.setStatus("current")


class _FsMIIpv6Preference_Type(Unsigned32):
    """Custom type fsMIIpv6Preference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIIpv6Preference_Type.__name__ = "Unsigned32"
_FsMIIpv6Preference_Object = MibTableColumn
fsMIIpv6Preference = _FsMIIpv6Preference_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 2, 1, 1, 2),
    _FsMIIpv6Preference_Type()
)
fsMIIpv6Preference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpv6Preference.setStatus("current")
_FsMIIpv6Test_ObjectIdentity = ObjectIdentity
fsMIIpv6Test = _FsMIIpv6Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 3)
)
_FsMIIpv6TestRedEntryTime_Type = Integer32
_FsMIIpv6TestRedEntryTime_Object = MibScalar
fsMIIpv6TestRedEntryTime = _FsMIIpv6TestRedEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 3, 1),
    _FsMIIpv6TestRedEntryTime_Type()
)
fsMIIpv6TestRedEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6TestRedEntryTime.setStatus("current")
_FsMIIpv6TestRedExitTime_Type = Integer32
_FsMIIpv6TestRedExitTime_Object = MibScalar
fsMIIpv6TestRedExitTime = _FsMIIpv6TestRedExitTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 35, 3, 2),
    _FsMIIpv6TestRedExitTime_Type()
)
fsMIIpv6TestRedExitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpv6TestRedExitTime.setStatus("current")
fsMIStdIpv6InterfaceEntry.registerAugmentions(
    ("SUPERMICRO-MIIPV6-MIB",
     "fsMIIpv6IfEntry")
)
fsMIIpv6IfEntry.setIndexNames(*fsMIStdIpv6InterfaceEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-MIIPV6-MIB",
    **{"InterfaceList": InterfaceList,
       "fsMIipv6MIB": fsMIipv6MIB,
       "fsMIipv6": fsMIipv6,
       "fsMIIpv6ContextTable": fsMIIpv6ContextTable,
       "fsMIIpv6ContextEntry": fsMIIpv6ContextEntry,
       "fsMIIpv6NdCacheMaxRetries": fsMIIpv6NdCacheMaxRetries,
       "fsMIIpv6PmtuConfigStatus": fsMIIpv6PmtuConfigStatus,
       "fsMIIpv6PmtuTimeOutInterval": fsMIIpv6PmtuTimeOutInterval,
       "fsMIIpv6JumboEnable": fsMIIpv6JumboEnable,
       "fsMIIpv6NumOfSendJumbo": fsMIIpv6NumOfSendJumbo,
       "fsMIIpv6NumOfRecvJumbo": fsMIIpv6NumOfRecvJumbo,
       "fsMIIpv6ErrJumbo": fsMIIpv6ErrJumbo,
       "fsMIIpv6ContextDebug": fsMIIpv6ContextDebug,
       "fsMIIpv6RFC5095Compatibility": fsMIIpv6RFC5095Compatibility,
       "fsMIIpv6IfTable": fsMIIpv6IfTable,
       "fsMIIpv6IfEntry": fsMIIpv6IfEntry,
       "fsMIIpv6IfType": fsMIIpv6IfType,
       "fsMIIpv6IfPortNum": fsMIIpv6IfPortNum,
       "fsMIIpv6IfCircuitNum": fsMIIpv6IfCircuitNum,
       "fsMIIpv6IfToken": fsMIIpv6IfToken,
       "fsMIIpv6IfOperStatus": fsMIIpv6IfOperStatus,
       "fsMIIpv6IfRouterAdvStatus": fsMIIpv6IfRouterAdvStatus,
       "fsMIIpv6IfRouterAdvFlags": fsMIIpv6IfRouterAdvFlags,
       "fsMIIpv6IfHopLimit": fsMIIpv6IfHopLimit,
       "fsMIIpv6IfDefRouterTime": fsMIIpv6IfDefRouterTime,
       "fsMIIpv6IfReachableTime": fsMIIpv6IfReachableTime,
       "fsMIIpv6IfRetransmitTime": fsMIIpv6IfRetransmitTime,
       "fsMIIpv6IfDelayProbeTime": fsMIIpv6IfDelayProbeTime,
       "fsMIIpv6IfPrefixAdvStatus": fsMIIpv6IfPrefixAdvStatus,
       "fsMIIpv6IfMinRouterAdvTime": fsMIIpv6IfMinRouterAdvTime,
       "fsMIIpv6IfMaxRouterAdvTime": fsMIIpv6IfMaxRouterAdvTime,
       "fsMIIpv6IfDADRetries": fsMIIpv6IfDADRetries,
       "fsMIIpv6IfForwarding": fsMIIpv6IfForwarding,
       "fsMIIpv6IfRoutingStatus": fsMIIpv6IfRoutingStatus,
       "fsMIIpv6IfIcmpErrInterval": fsMIIpv6IfIcmpErrInterval,
       "fsMIIpv6IfIcmpTokenBucketSize": fsMIIpv6IfIcmpTokenBucketSize,
       "fsMIIpv6IfDestUnreachableMsg": fsMIIpv6IfDestUnreachableMsg,
       "fsMIIpv6IfStatsTable": fsMIIpv6IfStatsTable,
       "fsMIIpv6IfStatsEntry": fsMIIpv6IfStatsEntry,
       "fsMIIpv6IfStatsTooBigErrors": fsMIIpv6IfStatsTooBigErrors,
       "fsMIIpv6IfStatsInRouterSols": fsMIIpv6IfStatsInRouterSols,
       "fsMIIpv6IfStatsInRouterAdvs": fsMIIpv6IfStatsInRouterAdvs,
       "fsMIIpv6IfStatsInNeighSols": fsMIIpv6IfStatsInNeighSols,
       "fsMIIpv6IfStatsInNeighAdvs": fsMIIpv6IfStatsInNeighAdvs,
       "fsMIIpv6IfStatsInRedirects": fsMIIpv6IfStatsInRedirects,
       "fsMIIpv6IfStatsOutRouterSols": fsMIIpv6IfStatsOutRouterSols,
       "fsMIIpv6IfStatsOutRouterAdvs": fsMIIpv6IfStatsOutRouterAdvs,
       "fsMIIpv6IfStatsOutNeighSols": fsMIIpv6IfStatsOutNeighSols,
       "fsMIIpv6IfStatsOutNeighAdvs": fsMIIpv6IfStatsOutNeighAdvs,
       "fsMIIpv6IfStatsOutRedirects": fsMIIpv6IfStatsOutRedirects,
       "fsMIIpv6IfStatsLastRouterAdvTime": fsMIIpv6IfStatsLastRouterAdvTime,
       "fsMIIpv6IfStatsNextRouterAdvTime": fsMIIpv6IfStatsNextRouterAdvTime,
       "fsMIIpv6IfStatsIcmp6ErrRateLmtd": fsMIIpv6IfStatsIcmp6ErrRateLmtd,
       "fsMIIpv6AddrTable": fsMIIpv6AddrTable,
       "fsMIIpv6AddrEntry": fsMIIpv6AddrEntry,
       "fsMIIpv6AddrAddress": fsMIIpv6AddrAddress,
       "fsMIIpv6AddrPrefixLen": fsMIIpv6AddrPrefixLen,
       "fsMIIpv6AddrAdminStatus": fsMIIpv6AddrAdminStatus,
       "fsMIIpv6AddrType": fsMIIpv6AddrType,
       "fsMIIpv6AddrProfIndex": fsMIIpv6AddrProfIndex,
       "fsMIIpv6AddrOperStatus": fsMIIpv6AddrOperStatus,
       "fsMIIpv6AddrContextId": fsMIIpv6AddrContextId,
       "fsMIIpv6AddrScope": fsMIIpv6AddrScope,
       "fsMIIpv6AddrProfileTable": fsMIIpv6AddrProfileTable,
       "fsMIIpv6AddrProfileEntry": fsMIIpv6AddrProfileEntry,
       "fsMIIpv6AddrProfileIndex": fsMIIpv6AddrProfileIndex,
       "fsMIIpv6AddrProfileStatus": fsMIIpv6AddrProfileStatus,
       "fsMIIpv6AddrProfilePrefixAdvStatus": fsMIIpv6AddrProfilePrefixAdvStatus,
       "fsMIIpv6AddrProfileOnLinkAdvStatus": fsMIIpv6AddrProfileOnLinkAdvStatus,
       "fsMIIpv6AddrProfileAutoConfAdvStatus": fsMIIpv6AddrProfileAutoConfAdvStatus,
       "fsMIIpv6AddrProfilePreferredTime": fsMIIpv6AddrProfilePreferredTime,
       "fsMIIpv6AddrProfileValidTime": fsMIIpv6AddrProfileValidTime,
       "fsMIIpv6AddrProfileValidLifeTimeFlag": fsMIIpv6AddrProfileValidLifeTimeFlag,
       "fsMIIpv6AddrProfilePreferredLifeTimeFlag": fsMIIpv6AddrProfilePreferredLifeTimeFlag,
       "fsMIIpv6IcmpStatsTable": fsMIIpv6IcmpStatsTable,
       "fsMIIpv6IcmpStatsEntry": fsMIIpv6IcmpStatsEntry,
       "fsMIIpv6IcmpInMsgs": fsMIIpv6IcmpInMsgs,
       "fsMIIpv6IcmpInErrors": fsMIIpv6IcmpInErrors,
       "fsMIIpv6IcmpInDestUnreachs": fsMIIpv6IcmpInDestUnreachs,
       "fsMIIpv6IcmpInTimeExcds": fsMIIpv6IcmpInTimeExcds,
       "fsMIIpv6IcmpInParmProbs": fsMIIpv6IcmpInParmProbs,
       "fsMIIpv6IcmpInPktTooBigs": fsMIIpv6IcmpInPktTooBigs,
       "fsMIIpv6IcmpInEchos": fsMIIpv6IcmpInEchos,
       "fsMIIpv6IcmpInEchoReps": fsMIIpv6IcmpInEchoReps,
       "fsMIIpv6IcmpInRouterSolicits": fsMIIpv6IcmpInRouterSolicits,
       "fsMIIpv6IcmpInRouterAdvertisements": fsMIIpv6IcmpInRouterAdvertisements,
       "fsMIIpv6IcmpInNeighborSolicits": fsMIIpv6IcmpInNeighborSolicits,
       "fsMIIpv6IcmpInNeighborAdvertisements": fsMIIpv6IcmpInNeighborAdvertisements,
       "fsMIIpv6IcmpInRedirects": fsMIIpv6IcmpInRedirects,
       "fsMIIpv6IcmpInAdminProhib": fsMIIpv6IcmpInAdminProhib,
       "fsMIIpv6IcmpOutMsgs": fsMIIpv6IcmpOutMsgs,
       "fsMIIpv6IcmpOutErrors": fsMIIpv6IcmpOutErrors,
       "fsMIIpv6IcmpOutDestUnreachs": fsMIIpv6IcmpOutDestUnreachs,
       "fsMIIpv6IcmpOutTimeExcds": fsMIIpv6IcmpOutTimeExcds,
       "fsMIIpv6IcmpOutParmProbs": fsMIIpv6IcmpOutParmProbs,
       "fsMIIpv6IcmpOutPktTooBigs": fsMIIpv6IcmpOutPktTooBigs,
       "fsMIIpv6IcmpOutEchos": fsMIIpv6IcmpOutEchos,
       "fsMIIpv6IcmpOutEchoReps": fsMIIpv6IcmpOutEchoReps,
       "fsMIIpv6IcmpOutRouterSolicits": fsMIIpv6IcmpOutRouterSolicits,
       "fsMIIpv6IcmpOutRouterAdvertisements": fsMIIpv6IcmpOutRouterAdvertisements,
       "fsMIIpv6IcmpOutNeighborSolicits": fsMIIpv6IcmpOutNeighborSolicits,
       "fsMIIpv6IcmpOutNeighborAdvertisements": fsMIIpv6IcmpOutNeighborAdvertisements,
       "fsMIIpv6IcmpOutRedirects": fsMIIpv6IcmpOutRedirects,
       "fsMIIpv6IcmpOutAdminProhib": fsMIIpv6IcmpOutAdminProhib,
       "fsMIIpv6IcmpInBadCode": fsMIIpv6IcmpInBadCode,
       "fsMIIpv6IcmpInNARouterFlagSet": fsMIIpv6IcmpInNARouterFlagSet,
       "fsMIIpv6IcmpInNASolicitedFlagSet": fsMIIpv6IcmpInNASolicitedFlagSet,
       "fsMIIpv6IcmpInNAOverrideFlagSet": fsMIIpv6IcmpInNAOverrideFlagSet,
       "fsMIIpv6IcmpOutNARouterFlagSet": fsMIIpv6IcmpOutNARouterFlagSet,
       "fsMIIpv6IcmpOutNASolicitedFlagSet": fsMIIpv6IcmpOutNASolicitedFlagSet,
       "fsMIIpv6IcmpOutNAOverrideFlagSet": fsMIIpv6IcmpOutNAOverrideFlagSet,
       "fsMIIpv6PmtuTable": fsMIIpv6PmtuTable,
       "fsMIIpv6PmtuEntry": fsMIIpv6PmtuEntry,
       "fsMIIpv6PmtuDest": fsMIIpv6PmtuDest,
       "fsMIIpv6Pmtu": fsMIIpv6Pmtu,
       "fsMIIpv6PmtuTimeStamp": fsMIIpv6PmtuTimeStamp,
       "fsMIIpv6PmtuAdminStatus": fsMIIpv6PmtuAdminStatus,
       "fsMIIpv6NDProxyListTable": fsMIIpv6NDProxyListTable,
       "fsMIIpv6NDProxyListEntry": fsMIIpv6NDProxyListEntry,
       "fsMIIpv6NDProxyAddr": fsMIIpv6NDProxyAddr,
       "fsMIIpv6NDProxyAdminStatus": fsMIIpv6NDProxyAdminStatus,
       "fsMIIpv6PingTable": fsMIIpv6PingTable,
       "fsMIIpv6PingEntry": fsMIIpv6PingEntry,
       "fsMIIpv6PingIndex": fsMIIpv6PingIndex,
       "fsMIIpv6PingDest": fsMIIpv6PingDest,
       "fsMIIpv6PingIfIndex": fsMIIpv6PingIfIndex,
       "fsMIIpv6PingContextId": fsMIIpv6PingContextId,
       "fsMIIpv6PingAdminStatus": fsMIIpv6PingAdminStatus,
       "fsMIIpv6PingInterval": fsMIIpv6PingInterval,
       "fsMIIpv6PingRcvTimeout": fsMIIpv6PingRcvTimeout,
       "fsMIIpv6PingTries": fsMIIpv6PingTries,
       "fsMIIpv6PingSize": fsMIIpv6PingSize,
       "fsMIIpv6PingSentCount": fsMIIpv6PingSentCount,
       "fsMIIpv6PingAverageTime": fsMIIpv6PingAverageTime,
       "fsMIIpv6PingMaxTime": fsMIIpv6PingMaxTime,
       "fsMIIpv6PingMinTime": fsMIIpv6PingMinTime,
       "fsMIIpv6PingOperStatus": fsMIIpv6PingOperStatus,
       "fsMIIpv6PingSuccesses": fsMIIpv6PingSuccesses,
       "fsMIIpv6PingPercentageLoss": fsMIIpv6PingPercentageLoss,
       "fsMIIpv6PingData": fsMIIpv6PingData,
       "fsMIIpv6PingSrcAddr": fsMIIpv6PingSrcAddr,
       "fsMIIpv6PingZoneId": fsMIIpv6PingZoneId,
       "fsMIIpv6PingDestAddrType": fsMIIpv6PingDestAddrType,
       "fsMIIpv6GlobalDebug": fsMIIpv6GlobalDebug,
       "fsMIIpv6AddrSelPolicyTable": fsMIIpv6AddrSelPolicyTable,
       "fsMIIpv6AddrSelPolicyEntry": fsMIIpv6AddrSelPolicyEntry,
       "fsMIIpv6AddrSelPolicyPrefix": fsMIIpv6AddrSelPolicyPrefix,
       "fsMIIpv6AddrSelPolicyPrefixLen": fsMIIpv6AddrSelPolicyPrefixLen,
       "fsMIIpv6AddrSelPolicyIfIndex": fsMIIpv6AddrSelPolicyIfIndex,
       "fsMIIpv6AddrSelPolicyScope": fsMIIpv6AddrSelPolicyScope,
       "fsMIIpv6AddrSelPolicyPrecedence": fsMIIpv6AddrSelPolicyPrecedence,
       "fsMIIpv6AddrSelPolicyLabel": fsMIIpv6AddrSelPolicyLabel,
       "fsMIIpv6AddrSelPolicyAddrType": fsMIIpv6AddrSelPolicyAddrType,
       "fsMIIpv6AddrSelPolicyIsPublicAddr": fsMIIpv6AddrSelPolicyIsPublicAddr,
       "fsMIIpv6AddrSelPolicyIsSelfAddr": fsMIIpv6AddrSelPolicyIsSelfAddr,
       "fsMIIpv6AddrSelPolicyReachabilityStatus": fsMIIpv6AddrSelPolicyReachabilityStatus,
       "fsMIIpv6AddrSelPolicyConfigStatus": fsMIIpv6AddrSelPolicyConfigStatus,
       "fsMIIpv6AddrSelPolicyRowStatus": fsMIIpv6AddrSelPolicyRowStatus,
       "fsMIIpv6IfScopeZoneMapTable": fsMIIpv6IfScopeZoneMapTable,
       "fsMIIpv6IfScopeZoneMapEntry": fsMIIpv6IfScopeZoneMapEntry,
       "fsMIIpv6ScopeZoneIndexIfIndex": fsMIIpv6ScopeZoneIndexIfIndex,
       "fsMIIpv6ScopeZoneIndexInterfaceLocal": fsMIIpv6ScopeZoneIndexInterfaceLocal,
       "fsMIIpv6ScopeZoneIndexLinkLocal": fsMIIpv6ScopeZoneIndexLinkLocal,
       "fsMIIpv6ScopeZoneIndex3": fsMIIpv6ScopeZoneIndex3,
       "fsMIIpv6ScopeZoneIndexAdminLocal": fsMIIpv6ScopeZoneIndexAdminLocal,
       "fsMIIpv6ScopeZoneIndexSiteLocal": fsMIIpv6ScopeZoneIndexSiteLocal,
       "fsMIIpv6ScopeZoneIndex6": fsMIIpv6ScopeZoneIndex6,
       "fsMIIpv6ScopeZoneIndex7": fsMIIpv6ScopeZoneIndex7,
       "fsMIIpv6ScopeZoneIndexOrganizationLocal": fsMIIpv6ScopeZoneIndexOrganizationLocal,
       "fsMIIpv6ScopeZoneIndex9": fsMIIpv6ScopeZoneIndex9,
       "fsMIIpv6ScopeZoneIndexA": fsMIIpv6ScopeZoneIndexA,
       "fsMIIpv6ScopeZoneIndexB": fsMIIpv6ScopeZoneIndexB,
       "fsMIIpv6ScopeZoneIndexC": fsMIIpv6ScopeZoneIndexC,
       "fsMIIpv6ScopeZoneIndexD": fsMIIpv6ScopeZoneIndexD,
       "fsMIIpv6ScopeZoneIndexE": fsMIIpv6ScopeZoneIndexE,
       "fsMIIpv6IfScopeZoneCreationStatus": fsMIIpv6IfScopeZoneCreationStatus,
       "fsMIIpv6IfScopeZoneRowStatus": fsMIIpv6IfScopeZoneRowStatus,
       "fsMIIpv6ScopeZoneTable": fsMIIpv6ScopeZoneTable,
       "fsMIIpv6ScopeZoneEntry": fsMIIpv6ScopeZoneEntry,
       "fsMIIpv6ScopeZoneContextId": fsMIIpv6ScopeZoneContextId,
       "fsMIIpv6ScopeZoneName": fsMIIpv6ScopeZoneName,
       "fsMIIpv6ScopeZoneIndex": fsMIIpv6ScopeZoneIndex,
       "fsMIIpv6ScopeZoneCreationStatus": fsMIIpv6ScopeZoneCreationStatus,
       "fsMIIpv6ScopeZoneInterfaceList": fsMIIpv6ScopeZoneInterfaceList,
       "fsMIIpv6IsDefaultScopeZone": fsMIIpv6IsDefaultScopeZone,
       "fsMIipv6Route": fsMIipv6Route,
       "fsMIIpv6PrefTable": fsMIIpv6PrefTable,
       "fsMIIpv6PrefEntry": fsMIIpv6PrefEntry,
       "fsMIIpv6Protocol": fsMIIpv6Protocol,
       "fsMIIpv6Preference": fsMIIpv6Preference,
       "fsMIIpv6Test": fsMIIpv6Test,
       "fsMIIpv6TestRedEntryTime": fsMIIpv6TestRedEntryTime,
       "fsMIIpv6TestRedExitTime": fsMIIpv6TestRedExitTime}
)
