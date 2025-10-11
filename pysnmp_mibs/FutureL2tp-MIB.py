# SNMP MIB module (FutureL2tp-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/FutureL2tp-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:43 2025
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
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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
 MacAddress,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

futureL2tpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108)
)
if mibBuilder.loadTexts:
    futureL2tpMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_L2tp_ObjectIdentity = ObjectIdentity
l2tp = _L2tp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1)
)
_L2tpGlobalInfo_ObjectIdentity = ObjectIdentity
l2tpGlobalInfo = _L2tpGlobalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 1)
)


class _L2tpSystemControl_Type(Integer32):
    """Custom type l2tpSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_L2tpSystemControl_Type.__name__ = "Integer32"
_L2tpSystemControl_Object = MibScalar
l2tpSystemControl = _L2tpSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 1, 1),
    _L2tpSystemControl_Type()
)
l2tpSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpSystemControl.setStatus("current")


class _L2tpGlobalEnable_Type(EnabledStatus):
    """Custom type l2tpGlobalEnable based on EnabledStatus"""
    defaultValue = 2


_L2tpGlobalEnable_Type.__name__ = "EnabledStatus"
_L2tpGlobalEnable_Object = MibScalar
l2tpGlobalEnable = _L2tpGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 1, 2),
    _L2tpGlobalEnable_Type()
)
l2tpGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpGlobalEnable.setStatus("current")


class _L2tpVersion_Type(Integer32):
    """Custom type l2tpVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("version3", 1)
    )


_L2tpVersion_Type.__name__ = "Integer32"
_L2tpVersion_Object = MibScalar
l2tpVersion = _L2tpVersion_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 1, 3),
    _L2tpVersion_Type()
)
l2tpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpVersion.setStatus("current")
_L2tpTotalConfiguredPw_Type = Counter32
_L2tpTotalConfiguredPw_Object = MibScalar
l2tpTotalConfiguredPw = _L2tpTotalConfiguredPw_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 1, 4),
    _L2tpTotalConfiguredPw_Type()
)
l2tpTotalConfiguredPw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTotalConfiguredPw.setStatus("current")
_L2tpTotalConfiguredSessions_Type = Counter32
_L2tpTotalConfiguredSessions_Object = MibScalar
l2tpTotalConfiguredSessions = _L2tpTotalConfiguredSessions_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 1, 5),
    _L2tpTotalConfiguredSessions_Type()
)
l2tpTotalConfiguredSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTotalConfiguredSessions.setStatus("current")
_L2tpTotalActiveSessions_Type = Counter32
_L2tpTotalActiveSessions_Object = MibScalar
l2tpTotalActiveSessions = _L2tpTotalActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 1, 6),
    _L2tpTotalActiveSessions_Type()
)
l2tpTotalActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTotalActiveSessions.setStatus("current")
_L2tpClearGlobalStats_Type = TruthValue
_L2tpClearGlobalStats_Object = MibScalar
l2tpClearGlobalStats = _L2tpClearGlobalStats_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 1, 7),
    _L2tpClearGlobalStats_Type()
)
l2tpClearGlobalStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpClearGlobalStats.setStatus("current")
_L2tpClearSessionStats_Type = TruthValue
_L2tpClearSessionStats_Object = MibScalar
l2tpClearSessionStats = _L2tpClearSessionStats_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 1, 8),
    _L2tpClearSessionStats_Type()
)
l2tpClearSessionStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpClearSessionStats.setStatus("current")
_L2tpInvalidEncapInfoDrop_Type = Counter32
_L2tpInvalidEncapInfoDrop_Object = MibScalar
l2tpInvalidEncapInfoDrop = _L2tpInvalidEncapInfoDrop_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 1, 9),
    _L2tpInvalidEncapInfoDrop_Type()
)
l2tpInvalidEncapInfoDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpInvalidEncapInfoDrop.setStatus("current")
_L2tpInvalidDecapInfoDrop_Type = Counter32
_L2tpInvalidDecapInfoDrop_Object = MibScalar
l2tpInvalidDecapInfoDrop = _L2tpInvalidDecapInfoDrop_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 1, 10),
    _L2tpInvalidDecapInfoDrop_Type()
)
l2tpInvalidDecapInfoDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpInvalidDecapInfoDrop.setStatus("current")
_L2tpInvalidSessionStatsInfoDrop_Type = Counter32
_L2tpInvalidSessionStatsInfoDrop_Object = MibScalar
l2tpInvalidSessionStatsInfoDrop = _L2tpInvalidSessionStatsInfoDrop_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 1, 11),
    _L2tpInvalidSessionStatsInfoDrop_Type()
)
l2tpInvalidSessionStatsInfoDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpInvalidSessionStatsInfoDrop.setStatus("current")
_L2tpInvalidL2tpPacketDrop_Type = Counter32
_L2tpInvalidL2tpPacketDrop_Object = MibScalar
l2tpInvalidL2tpPacketDrop = _L2tpInvalidL2tpPacketDrop_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 1, 12),
    _L2tpInvalidL2tpPacketDrop_Type()
)
l2tpInvalidL2tpPacketDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpInvalidL2tpPacketDrop.setStatus("current")
_L2tpTotalEncapedPackets_Type = Counter32
_L2tpTotalEncapedPackets_Object = MibScalar
l2tpTotalEncapedPackets = _L2tpTotalEncapedPackets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 1, 13),
    _L2tpTotalEncapedPackets_Type()
)
l2tpTotalEncapedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTotalEncapedPackets.setStatus("current")
_L2tpTotalDecapedPackets_Type = Counter32
_L2tpTotalDecapedPackets_Object = MibScalar
l2tpTotalDecapedPackets = _L2tpTotalDecapedPackets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 1, 14),
    _L2tpTotalDecapedPackets_Type()
)
l2tpTotalDecapedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpTotalDecapedPackets.setStatus("current")


class _L2tpTrcFlag_Type(Integer32):
    """Custom type l2tpTrcFlag based on Integer32"""
    defaultValue = 0


_L2tpTrcFlag_Type.__name__ = "Integer32"
_L2tpTrcFlag_Object = MibScalar
l2tpTrcFlag = _L2tpTrcFlag_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 1, 15),
    _L2tpTrcFlag_Type()
)
l2tpTrcFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpTrcFlag.setStatus("current")


class _L2tpErrTrapType_Type(Integer32):
    """Custom type l2tpErrTrapType based on Integer32"""
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
          ("memfail", 1),
          ("bufffail", 2))
    )


_L2tpErrTrapType_Type.__name__ = "Integer32"
_L2tpErrTrapType_Object = MibScalar
l2tpErrTrapType = _L2tpErrTrapType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 1, 16),
    _L2tpErrTrapType_Type()
)
l2tpErrTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpErrTrapType.setStatus("current")


class _L2tpSetTraps_Type(Integer32):
    """Custom type l2tpSetTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_L2tpSetTraps_Type.__name__ = "Integer32"
_L2tpSetTraps_Object = MibScalar
l2tpSetTraps = _L2tpSetTraps_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 1, 17),
    _L2tpSetTraps_Type()
)
l2tpSetTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l2tpSetTraps.setStatus("current")
_L2tpPort_ObjectIdentity = ObjectIdentity
l2tpPort = _L2tpPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 2)
)
_L2tpPortTable_Object = MibTable
l2tpPortTable = _L2tpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 2, 1)
)
if mibBuilder.loadTexts:
    l2tpPortTable.setStatus("current")
_L2tpPortEntry_Object = MibTableRow
l2tpPortEntry = _L2tpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 2, 1, 1)
)
l2tpPortEntry.setIndexNames(
    (0, "FutureL2tp-MIB", "l2tpPortIfIndex"),
)
if mibBuilder.loadTexts:
    l2tpPortEntry.setStatus("current")
_L2tpPortIfIndex_Type = Integer32
_L2tpPortIfIndex_Object = MibTableColumn
l2tpPortIfIndex = _L2tpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 2, 1, 1, 1),
    _L2tpPortIfIndex_Type()
)
l2tpPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2tpPortIfIndex.setStatus("current")
_L2tpEnabledStatus_Type = EnabledStatus
_L2tpEnabledStatus_Object = MibTableColumn
l2tpEnabledStatus = _L2tpEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 2, 1, 1, 2),
    _L2tpEnabledStatus_Type()
)
l2tpEnabledStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpEnabledStatus.setStatus("current")


class _L2tpPortEncapType_Type(Integer32):
    """Custom type l2tpPortEncapType based on Integer32"""
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
        *(("port", 1),
          ("port-vlan", 2),
          ("qinq", 3),
          ("qinAny", 4))
    )


_L2tpPortEncapType_Type.__name__ = "Integer32"
_L2tpPortEncapType_Object = MibTableColumn
l2tpPortEncapType = _L2tpPortEncapType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 2, 1, 1, 3),
    _L2tpPortEncapType_Type()
)
l2tpPortEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpPortEncapType.setStatus("current")
_L2tpPortRowStatus_Type = RowStatus
_L2tpPortRowStatus_Object = MibTableColumn
l2tpPortRowStatus = _L2tpPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 2, 1, 1, 4),
    _L2tpPortRowStatus_Type()
)
l2tpPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpPortRowStatus.setStatus("current")
_L2tpPseudowire_ObjectIdentity = ObjectIdentity
l2tpPseudowire = _L2tpPseudowire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 3)
)
_L2tpPseudowireTable_Object = MibTable
l2tpPseudowireTable = _L2tpPseudowireTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 3, 1)
)
if mibBuilder.loadTexts:
    l2tpPseudowireTable.setStatus("current")
_L2tpPseudowireEntry_Object = MibTableRow
l2tpPseudowireEntry = _L2tpPseudowireEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 3, 1, 1)
)
l2tpPseudowireEntry.setIndexNames(
    (0, "FutureL2tp-MIB", "l2tpPwIndex"),
)
if mibBuilder.loadTexts:
    l2tpPseudowireEntry.setStatus("current")
_L2tpPwIndex_Type = Unsigned32
_L2tpPwIndex_Object = MibTableColumn
l2tpPwIndex = _L2tpPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 3, 1, 1, 1),
    _L2tpPwIndex_Type()
)
l2tpPwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2tpPwIndex.setStatus("current")


class _L2tpPwEncapMode_Type(Integer32):
    """Custom type l2tpPwEncapMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l2tpv3", 1),
          ("mpls", 2))
    )


_L2tpPwEncapMode_Type.__name__ = "Integer32"
_L2tpPwEncapMode_Object = MibTableColumn
l2tpPwEncapMode = _L2tpPwEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 3, 1, 1, 2),
    _L2tpPwEncapMode_Type()
)
l2tpPwEncapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpPwEncapMode.setStatus("current")


class _L2tpIPSecEnabledStatus_Type(EnabledStatus):
    """Custom type l2tpIPSecEnabledStatus based on EnabledStatus"""
    defaultValue = 2


_L2tpIPSecEnabledStatus_Type.__name__ = "EnabledStatus"
_L2tpIPSecEnabledStatus_Object = MibTableColumn
l2tpIPSecEnabledStatus = _L2tpIPSecEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 3, 1, 1, 3),
    _L2tpIPSecEnabledStatus_Type()
)
l2tpIPSecEnabledStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpIPSecEnabledStatus.setStatus("current")


class _L2tpIPSecMode_Type(Integer32):
    """Custom type l2tpIPSecMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tunnel", 1),
          ("transparent", 2))
    )


_L2tpIPSecMode_Type.__name__ = "Integer32"
_L2tpIPSecMode_Object = MibTableColumn
l2tpIPSecMode = _L2tpIPSecMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 3, 1, 1, 4),
    _L2tpIPSecMode_Type()
)
l2tpIPSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpIPSecMode.setStatus("current")
_L2tpPwLoopBack_Type = DisplayString
_L2tpPwLoopBack_Object = MibTableColumn
l2tpPwLoopBack = _L2tpPwLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 3, 1, 1, 5),
    _L2tpPwLoopBack_Type()
)
l2tpPwLoopBack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpPwLoopBack.setStatus("current")
_L2tpRemoteIpAddress_Type = IpAddress
_L2tpRemoteIpAddress_Object = MibTableColumn
l2tpRemoteIpAddress = _L2tpRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 3, 1, 1, 6),
    _L2tpRemoteIpAddress_Type()
)
l2tpRemoteIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpRemoteIpAddress.setStatus("current")
_L2tpPwSrcMacAddr_Type = MacAddress
_L2tpPwSrcMacAddr_Object = MibTableColumn
l2tpPwSrcMacAddr = _L2tpPwSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 3, 1, 1, 7),
    _L2tpPwSrcMacAddr_Type()
)
l2tpPwSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpPwSrcMacAddr.setStatus("current")
_L2tpPwDestMacAddr_Type = MacAddress
_L2tpPwDestMacAddr_Object = MibTableColumn
l2tpPwDestMacAddr = _L2tpPwDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 3, 1, 1, 8),
    _L2tpPwDestMacAddr_Type()
)
l2tpPwDestMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpPwDestMacAddr.setStatus("current")
_L2tpPwRowStatus_Type = RowStatus
_L2tpPwRowStatus_Object = MibTableColumn
l2tpPwRowStatus = _L2tpPwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 3, 1, 1, 9),
    _L2tpPwRowStatus_Type()
)
l2tpPwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpPwRowStatus.setStatus("current")
_L2tpSession_ObjectIdentity = ObjectIdentity
l2tpSession = _L2tpSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 4)
)
_L2tpSessionTable_Object = MibTable
l2tpSessionTable = _L2tpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 4, 1)
)
if mibBuilder.loadTexts:
    l2tpSessionTable.setStatus("current")
_L2tpSessionEntry_Object = MibTableRow
l2tpSessionEntry = _L2tpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 4, 1, 1)
)
l2tpSessionEntry.setIndexNames(
    (0, "FutureL2tp-MIB", "l2tpRemoteEndId"),
)
if mibBuilder.loadTexts:
    l2tpSessionEntry.setStatus("current")


class _L2tpRemoteEndId_Type(Unsigned32):
    """Custom type l2tpRemoteEndId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpRemoteEndId_Type.__name__ = "Unsigned32"
_L2tpRemoteEndId_Object = MibTableColumn
l2tpRemoteEndId = _L2tpRemoteEndId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 4, 1, 1, 1),
    _L2tpRemoteEndId_Type()
)
l2tpRemoteEndId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2tpRemoteEndId.setStatus("current")


class _L2tpLocalSessionId_Type(Unsigned32):
    """Custom type l2tpLocalSessionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpLocalSessionId_Type.__name__ = "Unsigned32"
_L2tpLocalSessionId_Object = MibTableColumn
l2tpLocalSessionId = _L2tpLocalSessionId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 4, 1, 1, 2),
    _L2tpLocalSessionId_Type()
)
l2tpLocalSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpLocalSessionId.setStatus("current")


class _L2tpRemoteSessionId_Type(Unsigned32):
    """Custom type l2tpRemoteSessionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpRemoteSessionId_Type.__name__ = "Unsigned32"
_L2tpRemoteSessionId_Object = MibTableColumn
l2tpRemoteSessionId = _L2tpRemoteSessionId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 4, 1, 1, 3),
    _L2tpRemoteSessionId_Type()
)
l2tpRemoteSessionId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpRemoteSessionId.setStatus("current")
_L2tpSessionPwIndex_Type = Integer32
_L2tpSessionPwIndex_Object = MibTableColumn
l2tpSessionPwIndex = _L2tpSessionPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 4, 1, 1, 4),
    _L2tpSessionPwIndex_Type()
)
l2tpSessionPwIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpSessionPwIndex.setStatus("current")


class _L2tpSessionCookieSize_Type(Integer32):
    """Custom type l2tpSessionCookieSize based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("four-byte", 1),
          ("eight-byte", 2),
          ("none", 3))
    )


_L2tpSessionCookieSize_Type.__name__ = "Integer32"
_L2tpSessionCookieSize_Object = MibTableColumn
l2tpSessionCookieSize = _L2tpSessionCookieSize_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 4, 1, 1, 5),
    _L2tpSessionCookieSize_Type()
)
l2tpSessionCookieSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpSessionCookieSize.setStatus("current")
_L2tpSessionLocalCookie_Type = OctetString
_L2tpSessionLocalCookie_Object = MibTableColumn
l2tpSessionLocalCookie = _L2tpSessionLocalCookie_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 4, 1, 1, 6),
    _L2tpSessionLocalCookie_Type()
)
l2tpSessionLocalCookie.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpSessionLocalCookie.setStatus("current")
_L2tpSessionRemoteCookie_Type = OctetString
_L2tpSessionRemoteCookie_Object = MibTableColumn
l2tpSessionRemoteCookie = _L2tpSessionRemoteCookie_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 4, 1, 1, 7),
    _L2tpSessionRemoteCookie_Type()
)
l2tpSessionRemoteCookie.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpSessionRemoteCookie.setStatus("current")


class _L2tpSessionStatus_Type(Integer32):
    """Custom type l2tpSessionStatus based on Integer32"""
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


_L2tpSessionStatus_Type.__name__ = "Integer32"
_L2tpSessionStatus_Object = MibTableColumn
l2tpSessionStatus = _L2tpSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 4, 1, 1, 8),
    _L2tpSessionStatus_Type()
)
l2tpSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatus.setStatus("current")
_L2tpSessionClearStatistics_Type = TruthValue
_L2tpSessionClearStatistics_Object = MibTableColumn
l2tpSessionClearStatistics = _L2tpSessionClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 4, 1, 1, 9),
    _L2tpSessionClearStatistics_Type()
)
l2tpSessionClearStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpSessionClearStatistics.setStatus("current")
_L2tpSessionRowStatus_Type = RowStatus
_L2tpSessionRowStatus_Object = MibTableColumn
l2tpSessionRowStatus = _L2tpSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 4, 1, 1, 10),
    _L2tpSessionRowStatus_Type()
)
l2tpSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpSessionRowStatus.setStatus("current")
_L2tpXconnect_ObjectIdentity = ObjectIdentity
l2tpXconnect = _L2tpXconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 5)
)
_L2tpXconnectTable_Object = MibTable
l2tpXconnectTable = _L2tpXconnectTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 5, 1)
)
if mibBuilder.loadTexts:
    l2tpXconnectTable.setStatus("current")
_L2tpXconnectEntry_Object = MibTableRow
l2tpXconnectEntry = _L2tpXconnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 5, 1, 1)
)
l2tpXconnectEntry.setIndexNames(
    (0, "FutureL2tp-MIB", "l2tpXconnectIfIndex"),
    (0, "FutureL2tp-MIB", "l2tpXconnectId"),
)
if mibBuilder.loadTexts:
    l2tpXconnectEntry.setStatus("current")
_L2tpXconnectIfIndex_Type = Integer32
_L2tpXconnectIfIndex_Object = MibTableColumn
l2tpXconnectIfIndex = _L2tpXconnectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 5, 1, 1, 1),
    _L2tpXconnectIfIndex_Type()
)
l2tpXconnectIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2tpXconnectIfIndex.setStatus("current")


class _L2tpXconnectId_Type(Unsigned32):
    """Custom type l2tpXconnectId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpXconnectId_Type.__name__ = "Unsigned32"
_L2tpXconnectId_Object = MibTableColumn
l2tpXconnectId = _L2tpXconnectId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 5, 1, 1, 2),
    _L2tpXconnectId_Type()
)
l2tpXconnectId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2tpXconnectId.setStatus("current")


class _L2tpXconnectRemoteEndId_Type(Unsigned32):
    """Custom type l2tpXconnectRemoteEndId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_L2tpXconnectRemoteEndId_Type.__name__ = "Unsigned32"
_L2tpXconnectRemoteEndId_Object = MibTableColumn
l2tpXconnectRemoteEndId = _L2tpXconnectRemoteEndId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 5, 1, 1, 3),
    _L2tpXconnectRemoteEndId_Type()
)
l2tpXconnectRemoteEndId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpXconnectRemoteEndId.setStatus("current")


class _L2tpXconnectInnerVlanId_Type(Integer32):
    """Custom type l2tpXconnectInnerVlanId based on Integer32"""
    defaultValue = 1


_L2tpXconnectInnerVlanId_Type.__name__ = "Integer32"
_L2tpXconnectInnerVlanId_Object = MibTableColumn
l2tpXconnectInnerVlanId = _L2tpXconnectInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 5, 1, 1, 4),
    _L2tpXconnectInnerVlanId_Type()
)
l2tpXconnectInnerVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpXconnectInnerVlanId.setStatus("current")


class _L2tpXconnectOuterVlanId_Type(Integer32):
    """Custom type l2tpXconnectOuterVlanId based on Integer32"""
    defaultValue = 1


_L2tpXconnectOuterVlanId_Type.__name__ = "Integer32"
_L2tpXconnectOuterVlanId_Object = MibTableColumn
l2tpXconnectOuterVlanId = _L2tpXconnectOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 5, 1, 1, 5),
    _L2tpXconnectOuterVlanId_Type()
)
l2tpXconnectOuterVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpXconnectOuterVlanId.setStatus("current")
_L2tpXconnectRowStatus_Type = RowStatus
_L2tpXconnectRowStatus_Object = MibTableColumn
l2tpXconnectRowStatus = _L2tpXconnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 5, 1, 1, 6),
    _L2tpXconnectRowStatus_Type()
)
l2tpXconnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l2tpXconnectRowStatus.setStatus("current")
_L2tpSessionStats_ObjectIdentity = ObjectIdentity
l2tpSessionStats = _L2tpSessionStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 6)
)
_L2tpSessionStatsTable_Object = MibTable
l2tpSessionStatsTable = _L2tpSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 6, 1)
)
if mibBuilder.loadTexts:
    l2tpSessionStatsTable.setStatus("current")
_L2tpSessionStatsEntry_Object = MibTableRow
l2tpSessionStatsEntry = _L2tpSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 6, 1, 1)
)
l2tpSessionStatsEntry.setIndexNames(
    (0, "FutureL2tp-MIB", "l2tpSessionRemoteEndId"),
)
if mibBuilder.loadTexts:
    l2tpSessionStatsEntry.setStatus("current")
_L2tpSessionRemoteEndId_Type = Unsigned32
_L2tpSessionRemoteEndId_Object = MibTableColumn
l2tpSessionRemoteEndId = _L2tpSessionRemoteEndId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 6, 1, 1, 1),
    _L2tpSessionRemoteEndId_Type()
)
l2tpSessionRemoteEndId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2tpSessionRemoteEndId.setStatus("current")
_L2tpSessionStatsTotalEncap_Type = Counter32
_L2tpSessionStatsTotalEncap_Object = MibTableColumn
l2tpSessionStatsTotalEncap = _L2tpSessionStatsTotalEncap_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 6, 1, 1, 2),
    _L2tpSessionStatsTotalEncap_Type()
)
l2tpSessionStatsTotalEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsTotalEncap.setStatus("current")
_L2tpSessionStatsTotalDecap_Type = Counter32
_L2tpSessionStatsTotalDecap_Object = MibTableColumn
l2tpSessionStatsTotalDecap = _L2tpSessionStatsTotalDecap_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 6, 1, 1, 3),
    _L2tpSessionStatsTotalDecap_Type()
)
l2tpSessionStatsTotalDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsTotalDecap.setStatus("current")
_L2tpSessionStatsCookieMismatch_Type = Counter32
_L2tpSessionStatsCookieMismatch_Object = MibTableColumn
l2tpSessionStatsCookieMismatch = _L2tpSessionStatsCookieMismatch_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 6, 1, 1, 4),
    _L2tpSessionStatsCookieMismatch_Type()
)
l2tpSessionStatsCookieMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsCookieMismatch.setStatus("current")
_L2tpSessionStatsInvalidPeerIp_Type = Counter32
_L2tpSessionStatsInvalidPeerIp_Object = MibTableColumn
l2tpSessionStatsInvalidPeerIp = _L2tpSessionStatsInvalidPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 6, 1, 1, 5),
    _L2tpSessionStatsInvalidPeerIp_Type()
)
l2tpSessionStatsInvalidPeerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpSessionStatsInvalidPeerIp.setStatus("current")
_L2tpPortStats_ObjectIdentity = ObjectIdentity
l2tpPortStats = _L2tpPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 7)
)
_L2tpPortStatsTable_Object = MibTable
l2tpPortStatsTable = _L2tpPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 7, 1)
)
if mibBuilder.loadTexts:
    l2tpPortStatsTable.setStatus("current")
_L2tpPortStatsEntry_Object = MibTableRow
l2tpPortStatsEntry = _L2tpPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 7, 1, 1)
)
l2tpPortStatsEntry.setIndexNames(
    (0, "FutureL2tp-MIB", "l2tpPortStatsIfIndex"),
)
if mibBuilder.loadTexts:
    l2tpPortStatsEntry.setStatus("current")
_L2tpPortStatsIfIndex_Type = Integer32
_L2tpPortStatsIfIndex_Object = MibTableColumn
l2tpPortStatsIfIndex = _L2tpPortStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 7, 1, 1, 1),
    _L2tpPortStatsIfIndex_Type()
)
l2tpPortStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2tpPortStatsIfIndex.setStatus("current")
_L2tpPortStatsInvalidFrames_Type = Counter32
_L2tpPortStatsInvalidFrames_Object = MibTableColumn
l2tpPortStatsInvalidFrames = _L2tpPortStatsInvalidFrames_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 7, 1, 1, 2),
    _L2tpPortStatsInvalidFrames_Type()
)
l2tpPortStatsInvalidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpPortStatsInvalidFrames.setStatus("current")
_L2tpPortTotalTx_Type = Counter32
_L2tpPortTotalTx_Object = MibTableColumn
l2tpPortTotalTx = _L2tpPortTotalTx_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 7, 1, 1, 3),
    _L2tpPortTotalTx_Type()
)
l2tpPortTotalTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpPortTotalTx.setStatus("current")
_L2tpPortTotalRx_Type = Counter32
_L2tpPortTotalRx_Object = MibTableColumn
l2tpPortTotalRx = _L2tpPortTotalRx_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 7, 1, 1, 4),
    _L2tpPortTotalRx_Type()
)
l2tpPortTotalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2tpPortTotalRx.setStatus("current")
_L2tpNotifications_ObjectIdentity = ObjectIdentity
l2tpNotifications = _L2tpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 8)
)
_L2tpTraps_ObjectIdentity = ObjectIdentity
l2tpTraps = _L2tpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 8, 0)
)

# Managed Objects groups


# Notification objects

l2tpTrapGlobalInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 8, 0, 1)
)
l2tpTrapGlobalInfo.setObjects(
      *(("FutureL2tp-MIB", "l2tpGlobalEnable"),
        ("FutureL2tp-MIB", "l2tpTotalConfiguredPw"),
        ("FutureL2tp-MIB", "l2tpTotalConfiguredSessions"),
        ("FutureL2tp-MIB", "l2tpTotalActiveSessions"))
)
if mibBuilder.loadTexts:
    l2tpTrapGlobalInfo.setStatus(
        "current"
    )

l2tpTrapSessionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 8, 0, 2)
)
l2tpTrapSessionStatus.setObjects(
      *(("FutureL2tp-MIB", "l2tpRemoteEndId"),
        ("FutureL2tp-MIB", "l2tpLocalSessionId"),
        ("FutureL2tp-MIB", "l2tpRemoteSessionId"),
        ("FutureL2tp-MIB", "l2tpSessionStatus"))
)
if mibBuilder.loadTexts:
    l2tpTrapSessionStatus.setStatus(
        "current"
    )

l2tpErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 108, 1, 8, 0, 3)
)
l2tpErrTrap.setObjects(
    ("FutureL2tp-MIB", "l2tpErrTrapType")
)
if mibBuilder.loadTexts:
    l2tpErrTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FutureL2tp-MIB",
    **{"EnabledStatus": EnabledStatus,
       "futureL2tpMIB": futureL2tpMIB,
       "l2tp": l2tp,
       "l2tpGlobalInfo": l2tpGlobalInfo,
       "l2tpSystemControl": l2tpSystemControl,
       "l2tpGlobalEnable": l2tpGlobalEnable,
       "l2tpVersion": l2tpVersion,
       "l2tpTotalConfiguredPw": l2tpTotalConfiguredPw,
       "l2tpTotalConfiguredSessions": l2tpTotalConfiguredSessions,
       "l2tpTotalActiveSessions": l2tpTotalActiveSessions,
       "l2tpClearGlobalStats": l2tpClearGlobalStats,
       "l2tpClearSessionStats": l2tpClearSessionStats,
       "l2tpInvalidEncapInfoDrop": l2tpInvalidEncapInfoDrop,
       "l2tpInvalidDecapInfoDrop": l2tpInvalidDecapInfoDrop,
       "l2tpInvalidSessionStatsInfoDrop": l2tpInvalidSessionStatsInfoDrop,
       "l2tpInvalidL2tpPacketDrop": l2tpInvalidL2tpPacketDrop,
       "l2tpTotalEncapedPackets": l2tpTotalEncapedPackets,
       "l2tpTotalDecapedPackets": l2tpTotalDecapedPackets,
       "l2tpTrcFlag": l2tpTrcFlag,
       "l2tpErrTrapType": l2tpErrTrapType,
       "l2tpSetTraps": l2tpSetTraps,
       "l2tpPort": l2tpPort,
       "l2tpPortTable": l2tpPortTable,
       "l2tpPortEntry": l2tpPortEntry,
       "l2tpPortIfIndex": l2tpPortIfIndex,
       "l2tpEnabledStatus": l2tpEnabledStatus,
       "l2tpPortEncapType": l2tpPortEncapType,
       "l2tpPortRowStatus": l2tpPortRowStatus,
       "l2tpPseudowire": l2tpPseudowire,
       "l2tpPseudowireTable": l2tpPseudowireTable,
       "l2tpPseudowireEntry": l2tpPseudowireEntry,
       "l2tpPwIndex": l2tpPwIndex,
       "l2tpPwEncapMode": l2tpPwEncapMode,
       "l2tpIPSecEnabledStatus": l2tpIPSecEnabledStatus,
       "l2tpIPSecMode": l2tpIPSecMode,
       "l2tpPwLoopBack": l2tpPwLoopBack,
       "l2tpRemoteIpAddress": l2tpRemoteIpAddress,
       "l2tpPwSrcMacAddr": l2tpPwSrcMacAddr,
       "l2tpPwDestMacAddr": l2tpPwDestMacAddr,
       "l2tpPwRowStatus": l2tpPwRowStatus,
       "l2tpSession": l2tpSession,
       "l2tpSessionTable": l2tpSessionTable,
       "l2tpSessionEntry": l2tpSessionEntry,
       "l2tpRemoteEndId": l2tpRemoteEndId,
       "l2tpLocalSessionId": l2tpLocalSessionId,
       "l2tpRemoteSessionId": l2tpRemoteSessionId,
       "l2tpSessionPwIndex": l2tpSessionPwIndex,
       "l2tpSessionCookieSize": l2tpSessionCookieSize,
       "l2tpSessionLocalCookie": l2tpSessionLocalCookie,
       "l2tpSessionRemoteCookie": l2tpSessionRemoteCookie,
       "l2tpSessionStatus": l2tpSessionStatus,
       "l2tpSessionClearStatistics": l2tpSessionClearStatistics,
       "l2tpSessionRowStatus": l2tpSessionRowStatus,
       "l2tpXconnect": l2tpXconnect,
       "l2tpXconnectTable": l2tpXconnectTable,
       "l2tpXconnectEntry": l2tpXconnectEntry,
       "l2tpXconnectIfIndex": l2tpXconnectIfIndex,
       "l2tpXconnectId": l2tpXconnectId,
       "l2tpXconnectRemoteEndId": l2tpXconnectRemoteEndId,
       "l2tpXconnectInnerVlanId": l2tpXconnectInnerVlanId,
       "l2tpXconnectOuterVlanId": l2tpXconnectOuterVlanId,
       "l2tpXconnectRowStatus": l2tpXconnectRowStatus,
       "l2tpSessionStats": l2tpSessionStats,
       "l2tpSessionStatsTable": l2tpSessionStatsTable,
       "l2tpSessionStatsEntry": l2tpSessionStatsEntry,
       "l2tpSessionRemoteEndId": l2tpSessionRemoteEndId,
       "l2tpSessionStatsTotalEncap": l2tpSessionStatsTotalEncap,
       "l2tpSessionStatsTotalDecap": l2tpSessionStatsTotalDecap,
       "l2tpSessionStatsCookieMismatch": l2tpSessionStatsCookieMismatch,
       "l2tpSessionStatsInvalidPeerIp": l2tpSessionStatsInvalidPeerIp,
       "l2tpPortStats": l2tpPortStats,
       "l2tpPortStatsTable": l2tpPortStatsTable,
       "l2tpPortStatsEntry": l2tpPortStatsEntry,
       "l2tpPortStatsIfIndex": l2tpPortStatsIfIndex,
       "l2tpPortStatsInvalidFrames": l2tpPortStatsInvalidFrames,
       "l2tpPortTotalTx": l2tpPortTotalTx,
       "l2tpPortTotalRx": l2tpPortTotalRx,
       "l2tpNotifications": l2tpNotifications,
       "l2tpTraps": l2tpTraps,
       "l2tpTrapGlobalInfo": l2tpTrapGlobalInfo,
       "l2tpTrapSessionStatus": l2tpTrapSessionStatus,
       "l2tpErrTrap": l2tpErrTrap}
)
