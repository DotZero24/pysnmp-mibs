# SNMP MIB module (SUPERMICRO-MIRIP2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-MIRIP2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:26 2025
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

fsMIRip = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151)
)
if mibBuilder.loadTexts:
    fsMIRip.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIRip2GeneralGroup_ObjectIdentity = ObjectIdentity
fsMIRip2GeneralGroup = _FsMIRip2GeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1)
)
_FsMIRip2GlobalTable_Object = MibTable
fsMIRip2GlobalTable = _FsMIRip2GlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 1)
)
if mibBuilder.loadTexts:
    fsMIRip2GlobalTable.setStatus("current")
_FsMIRip2GlobalEntry_Object = MibTableRow
fsMIRip2GlobalEntry = _FsMIRip2GlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 1, 1)
)
fsMIRip2GlobalEntry.setIndexNames(
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipContextId"),
)
if mibBuilder.loadTexts:
    fsMIRip2GlobalEntry.setStatus("current")


class _FsMIRipContextId_Type(Integer32):
    """Custom type fsMIRipContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIRipContextId_Type.__name__ = "Integer32"
_FsMIRipContextId_Object = MibTableColumn
fsMIRipContextId = _FsMIRipContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 1, 1, 1),
    _FsMIRipContextId_Type()
)
fsMIRipContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRipContextId.setStatus("current")


class _FsMIRip2Security_Type(Integer32):
    """Custom type fsMIRip2Security based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("minimumSecurity", 1),
          ("maximumSecurity", 2))
    )


_FsMIRip2Security_Type.__name__ = "Integer32"
_FsMIRip2Security_Object = MibTableColumn
fsMIRip2Security = _FsMIRip2Security_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 1, 1, 2),
    _FsMIRip2Security_Type()
)
fsMIRip2Security.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2Security.setStatus("current")


class _FsMIRip2Peers_Type(Integer32):
    """Custom type fsMIRip2Peers based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIRip2Peers_Type.__name__ = "Integer32"
_FsMIRip2Peers_Object = MibTableColumn
fsMIRip2Peers = _FsMIRip2Peers_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 1, 1, 3),
    _FsMIRip2Peers_Type()
)
fsMIRip2Peers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2Peers.setStatus("current")


class _FsMIRip2TrustNBRListEnable_Type(Integer32):
    """Custom type fsMIRip2TrustNBRListEnable based on Integer32"""
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


_FsMIRip2TrustNBRListEnable_Type.__name__ = "Integer32"
_FsMIRip2TrustNBRListEnable_Object = MibTableColumn
fsMIRip2TrustNBRListEnable = _FsMIRip2TrustNBRListEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 1, 1, 4),
    _FsMIRip2TrustNBRListEnable_Type()
)
fsMIRip2TrustNBRListEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2TrustNBRListEnable.setStatus("current")
_FsMIRip2NumberOfDroppedPkts_Type = Counter32
_FsMIRip2NumberOfDroppedPkts_Object = MibTableColumn
fsMIRip2NumberOfDroppedPkts = _FsMIRip2NumberOfDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 1, 1, 5),
    _FsMIRip2NumberOfDroppedPkts_Type()
)
fsMIRip2NumberOfDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRip2NumberOfDroppedPkts.setStatus("current")


class _FsMIRip2SpacingEnable_Type(Integer32):
    """Custom type fsMIRip2SpacingEnable based on Integer32"""
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


_FsMIRip2SpacingEnable_Type.__name__ = "Integer32"
_FsMIRip2SpacingEnable_Object = MibTableColumn
fsMIRip2SpacingEnable = _FsMIRip2SpacingEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 1, 1, 6),
    _FsMIRip2SpacingEnable_Type()
)
fsMIRip2SpacingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2SpacingEnable.setStatus("current")


class _FsMIRip2AutoSummaryStatus_Type(Integer32):
    """Custom type fsMIRip2AutoSummaryStatus based on Integer32"""
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


_FsMIRip2AutoSummaryStatus_Type.__name__ = "Integer32"
_FsMIRip2AutoSummaryStatus_Object = MibTableColumn
fsMIRip2AutoSummaryStatus = _FsMIRip2AutoSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 1, 1, 7),
    _FsMIRip2AutoSummaryStatus_Type()
)
fsMIRip2AutoSummaryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2AutoSummaryStatus.setStatus("current")


class _FsMIRip2RetransTimeoutInt_Type(Integer32):
    """Custom type fsMIRip2RetransTimeoutInt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10),
    )


_FsMIRip2RetransTimeoutInt_Type.__name__ = "Integer32"
_FsMIRip2RetransTimeoutInt_Object = MibTableColumn
fsMIRip2RetransTimeoutInt = _FsMIRip2RetransTimeoutInt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 1, 1, 8),
    _FsMIRip2RetransTimeoutInt_Type()
)
fsMIRip2RetransTimeoutInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2RetransTimeoutInt.setStatus("current")


class _FsMIRip2MaxRetransmissions_Type(Integer32):
    """Custom type fsMIRip2MaxRetransmissions based on Integer32"""
    defaultValue = 36

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 40),
    )


_FsMIRip2MaxRetransmissions_Type.__name__ = "Integer32"
_FsMIRip2MaxRetransmissions_Object = MibTableColumn
fsMIRip2MaxRetransmissions = _FsMIRip2MaxRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 1, 1, 9),
    _FsMIRip2MaxRetransmissions_Type()
)
fsMIRip2MaxRetransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2MaxRetransmissions.setStatus("current")


class _FsMIRip2OverSubscriptionTimeout_Type(Integer32):
    """Custom type fsMIRip2OverSubscriptionTimeout based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 300),
    )


_FsMIRip2OverSubscriptionTimeout_Type.__name__ = "Integer32"
_FsMIRip2OverSubscriptionTimeout_Object = MibTableColumn
fsMIRip2OverSubscriptionTimeout = _FsMIRip2OverSubscriptionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 1, 1, 10),
    _FsMIRip2OverSubscriptionTimeout_Type()
)
fsMIRip2OverSubscriptionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2OverSubscriptionTimeout.setStatus("current")


class _FsMIRip2Propagate_Type(Integer32):
    """Custom type fsMIRip2Propagate based on Integer32"""
    defaultValue = 2

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


_FsMIRip2Propagate_Type.__name__ = "Integer32"
_FsMIRip2Propagate_Object = MibTableColumn
fsMIRip2Propagate = _FsMIRip2Propagate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 1, 1, 11),
    _FsMIRip2Propagate_Type()
)
fsMIRip2Propagate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2Propagate.setStatus("current")


class _FsMIRipTrcFlag_Type(Integer32):
    """Custom type fsMIRipTrcFlag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIRipTrcFlag_Type.__name__ = "Integer32"
_FsMIRipTrcFlag_Object = MibTableColumn
fsMIRipTrcFlag = _FsMIRipTrcFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 1, 1, 12),
    _FsMIRipTrcFlag_Type()
)
fsMIRipTrcFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipTrcFlag.setStatus("current")
_FsMIRipRowStatus_Type = RowStatus
_FsMIRipRowStatus_Object = MibTableColumn
fsMIRipRowStatus = _FsMIRipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 1, 1, 13),
    _FsMIRipRowStatus_Type()
)
fsMIRipRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipRowStatus.setStatus("current")


class _FsMIRipAdminStatus_Type(Integer32):
    """Custom type fsMIRipAdminStatus based on Integer32"""
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


_FsMIRipAdminStatus_Type.__name__ = "Integer32"
_FsMIRipAdminStatus_Object = MibTableColumn
fsMIRipAdminStatus = _FsMIRipAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 1, 1, 14),
    _FsMIRipAdminStatus_Type()
)
fsMIRipAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipAdminStatus.setStatus("current")


class _FsMIRip2LastAuthKeyLifetimeStatus_Type(TruthValue):
    """Custom type fsMIRip2LastAuthKeyLifetimeStatus based on TruthValue"""
    defaultValue = 1


_FsMIRip2LastAuthKeyLifetimeStatus_Type.__name__ = "TruthValue"
_FsMIRip2LastAuthKeyLifetimeStatus_Object = MibTableColumn
fsMIRip2LastAuthKeyLifetimeStatus = _FsMIRip2LastAuthKeyLifetimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 1, 1, 15),
    _FsMIRip2LastAuthKeyLifetimeStatus_Type()
)
fsMIRip2LastAuthKeyLifetimeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2LastAuthKeyLifetimeStatus.setStatus("current")
_FsMIRipRtCount_Type = Integer32
_FsMIRipRtCount_Object = MibTableColumn
fsMIRipRtCount = _FsMIRipRtCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 1, 1, 16),
    _FsMIRipRtCount_Type()
)
fsMIRipRtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRipRtCount.setStatus("current")


class _FsMIRipGlobalTrcFlag_Type(Integer32):
    """Custom type fsMIRipGlobalTrcFlag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIRipGlobalTrcFlag_Type.__name__ = "Integer32"
_FsMIRipGlobalTrcFlag_Object = MibScalar
fsMIRipGlobalTrcFlag = _FsMIRipGlobalTrcFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 2),
    _FsMIRipGlobalTrcFlag_Type()
)
fsMIRipGlobalTrcFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipGlobalTrcFlag.setStatus("current")
_FsMIRip2NBRTrustListTable_Object = MibTable
fsMIRip2NBRTrustListTable = _FsMIRip2NBRTrustListTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 3)
)
if mibBuilder.loadTexts:
    fsMIRip2NBRTrustListTable.setStatus("current")
_FsMIRip2NBRTrustListEntry_Object = MibTableRow
fsMIRip2NBRTrustListEntry = _FsMIRip2NBRTrustListEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 3, 1)
)
fsMIRip2NBRTrustListEntry.setIndexNames(
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipContextId"),
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRip2TrustNBRIpAddr"),
)
if mibBuilder.loadTexts:
    fsMIRip2NBRTrustListEntry.setStatus("current")
_FsMIRip2TrustNBRIpAddr_Type = IpAddress
_FsMIRip2TrustNBRIpAddr_Object = MibTableColumn
fsMIRip2TrustNBRIpAddr = _FsMIRip2TrustNBRIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 3, 1, 1),
    _FsMIRip2TrustNBRIpAddr_Type()
)
fsMIRip2TrustNBRIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRip2TrustNBRIpAddr.setStatus("current")
_FsMIRip2TrustNBRRowStatus_Type = RowStatus
_FsMIRip2TrustNBRRowStatus_Object = MibTableColumn
fsMIRip2TrustNBRRowStatus = _FsMIRip2TrustNBRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 3, 1, 2),
    _FsMIRip2TrustNBRRowStatus_Type()
)
fsMIRip2TrustNBRRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2TrustNBRRowStatus.setStatus("current")
_FsMIRip2IfConfTable_Object = MibTable
fsMIRip2IfConfTable = _FsMIRip2IfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 4)
)
if mibBuilder.loadTexts:
    fsMIRip2IfConfTable.setStatus("current")
_FsMIRip2IfConfEntry_Object = MibTableRow
fsMIRip2IfConfEntry = _FsMIRip2IfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 4, 1)
)
fsMIRip2IfConfEntry.setIndexNames(
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipContextId"),
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRip2IfConfAddress"),
)
if mibBuilder.loadTexts:
    fsMIRip2IfConfEntry.setStatus("current")
_FsMIRip2IfConfAddress_Type = IpAddress
_FsMIRip2IfConfAddress_Object = MibTableColumn
fsMIRip2IfConfAddress = _FsMIRip2IfConfAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 4, 1, 1),
    _FsMIRip2IfConfAddress_Type()
)
fsMIRip2IfConfAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRip2IfConfAddress.setStatus("current")


class _FsMIRip2IfAdminStat_Type(Integer32):
    """Custom type fsMIRip2IfAdminStat based on Integer32"""
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
          ("passive", 3))
    )


_FsMIRip2IfAdminStat_Type.__name__ = "Integer32"
_FsMIRip2IfAdminStat_Object = MibTableColumn
fsMIRip2IfAdminStat = _FsMIRip2IfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 4, 1, 2),
    _FsMIRip2IfAdminStat_Type()
)
fsMIRip2IfAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2IfAdminStat.setStatus("current")


class _FsMIRip2IfConfOperState_Type(Integer32):
    """Custom type fsMIRip2IfConfOperState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operup", 1),
          ("operdown", 2))
    )


_FsMIRip2IfConfOperState_Type.__name__ = "Integer32"
_FsMIRip2IfConfOperState_Object = MibTableColumn
fsMIRip2IfConfOperState = _FsMIRip2IfConfOperState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 4, 1, 3),
    _FsMIRip2IfConfOperState_Type()
)
fsMIRip2IfConfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRip2IfConfOperState.setStatus("current")


class _FsMIRip2IfConfUpdateTmr_Type(Integer32):
    """Custom type fsMIRip2IfConfUpdateTmr based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_FsMIRip2IfConfUpdateTmr_Type.__name__ = "Integer32"
_FsMIRip2IfConfUpdateTmr_Object = MibTableColumn
fsMIRip2IfConfUpdateTmr = _FsMIRip2IfConfUpdateTmr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 4, 1, 4),
    _FsMIRip2IfConfUpdateTmr_Type()
)
fsMIRip2IfConfUpdateTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2IfConfUpdateTmr.setStatus("current")


class _FsMIRip2IfConfGarbgCollectTmr_Type(Integer32):
    """Custom type fsMIRip2IfConfGarbgCollectTmr based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 180),
    )


_FsMIRip2IfConfGarbgCollectTmr_Type.__name__ = "Integer32"
_FsMIRip2IfConfGarbgCollectTmr_Object = MibTableColumn
fsMIRip2IfConfGarbgCollectTmr = _FsMIRip2IfConfGarbgCollectTmr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 4, 1, 5),
    _FsMIRip2IfConfGarbgCollectTmr_Type()
)
fsMIRip2IfConfGarbgCollectTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2IfConfGarbgCollectTmr.setStatus("current")


class _FsMIRip2IfConfRouteAgeTmr_Type(Integer32):
    """Custom type fsMIRip2IfConfRouteAgeTmr based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 500),
    )


_FsMIRip2IfConfRouteAgeTmr_Type.__name__ = "Integer32"
_FsMIRip2IfConfRouteAgeTmr_Object = MibTableColumn
fsMIRip2IfConfRouteAgeTmr = _FsMIRip2IfConfRouteAgeTmr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 4, 1, 6),
    _FsMIRip2IfConfRouteAgeTmr_Type()
)
fsMIRip2IfConfRouteAgeTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2IfConfRouteAgeTmr.setStatus("current")


class _FsMIRip2IfSplitHorizonStatus_Type(Integer32):
    """Custom type fsMIRip2IfSplitHorizonStatus based on Integer32"""
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
        *(("splitHorizon", 1),
          ("splitHorizonWithPoisRev", 2),
          ("disable", 3))
    )


_FsMIRip2IfSplitHorizonStatus_Type.__name__ = "Integer32"
_FsMIRip2IfSplitHorizonStatus_Object = MibTableColumn
fsMIRip2IfSplitHorizonStatus = _FsMIRip2IfSplitHorizonStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 4, 1, 7),
    _FsMIRip2IfSplitHorizonStatus_Type()
)
fsMIRip2IfSplitHorizonStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2IfSplitHorizonStatus.setStatus("current")


class _FsMIRip2IfConfDefRtInstall_Type(Integer32):
    """Custom type fsMIRip2IfConfDefRtInstall based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installDefRt", 1),
          ("doNotInstallDefRt", 2))
    )


_FsMIRip2IfConfDefRtInstall_Type.__name__ = "Integer32"
_FsMIRip2IfConfDefRtInstall_Object = MibTableColumn
fsMIRip2IfConfDefRtInstall = _FsMIRip2IfConfDefRtInstall_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 4, 1, 8),
    _FsMIRip2IfConfDefRtInstall_Type()
)
fsMIRip2IfConfDefRtInstall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2IfConfDefRtInstall.setStatus("current")


class _FsMIRip2IfConfSpacingTmr_Type(Integer32):
    """Custom type fsMIRip2IfConfSpacingTmr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 360),
    )


_FsMIRip2IfConfSpacingTmr_Type.__name__ = "Integer32"
_FsMIRip2IfConfSpacingTmr_Object = MibTableColumn
fsMIRip2IfConfSpacingTmr = _FsMIRip2IfConfSpacingTmr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 4, 1, 9),
    _FsMIRip2IfConfSpacingTmr_Type()
)
fsMIRip2IfConfSpacingTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2IfConfSpacingTmr.setStatus("current")


class _FsMIRip2IfConfInUseKey_Type(Integer32):
    """Custom type fsMIRip2IfConfInUseKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIRip2IfConfInUseKey_Type.__name__ = "Integer32"
_FsMIRip2IfConfInUseKey_Object = MibTableColumn
fsMIRip2IfConfInUseKey = _FsMIRip2IfConfInUseKey_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 4, 1, 10),
    _FsMIRip2IfConfInUseKey_Type()
)
fsMIRip2IfConfInUseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRip2IfConfInUseKey.setStatus("current")


class _FsMIRip2IfConfAuthLastKeyStatus_Type(TruthValue):
    """Custom type fsMIRip2IfConfAuthLastKeyStatus based on TruthValue"""
    defaultValue = 2


_FsMIRip2IfConfAuthLastKeyStatus_Type.__name__ = "TruthValue"
_FsMIRip2IfConfAuthLastKeyStatus_Object = MibTableColumn
fsMIRip2IfConfAuthLastKeyStatus = _FsMIRip2IfConfAuthLastKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 4, 1, 11),
    _FsMIRip2IfConfAuthLastKeyStatus_Type()
)
fsMIRip2IfConfAuthLastKeyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRip2IfConfAuthLastKeyStatus.setStatus("current")
_FsMIRipMd5AuthTable_Object = MibTable
fsMIRipMd5AuthTable = _FsMIRipMd5AuthTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 5)
)
if mibBuilder.loadTexts:
    fsMIRipMd5AuthTable.setStatus("current")
_FsMIRipMd5AuthEntry_Object = MibTableRow
fsMIRipMd5AuthEntry = _FsMIRipMd5AuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 5, 1)
)
fsMIRipMd5AuthEntry.setIndexNames(
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipContextId"),
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipMd5AuthAddress"),
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipMd5AuthKeyId"),
)
if mibBuilder.loadTexts:
    fsMIRipMd5AuthEntry.setStatus("current")
_FsMIRipMd5AuthAddress_Type = IpAddress
_FsMIRipMd5AuthAddress_Object = MibTableColumn
fsMIRipMd5AuthAddress = _FsMIRipMd5AuthAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 5, 1, 1),
    _FsMIRipMd5AuthAddress_Type()
)
fsMIRipMd5AuthAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRipMd5AuthAddress.setStatus("current")


class _FsMIRipMd5AuthKeyId_Type(Integer32):
    """Custom type fsMIRipMd5AuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIRipMd5AuthKeyId_Type.__name__ = "Integer32"
_FsMIRipMd5AuthKeyId_Object = MibTableColumn
fsMIRipMd5AuthKeyId = _FsMIRipMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 5, 1, 2),
    _FsMIRipMd5AuthKeyId_Type()
)
fsMIRipMd5AuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRipMd5AuthKeyId.setStatus("current")


class _FsMIRipMd5AuthKey_Type(OctetString):
    """Custom type fsMIRipMd5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsMIRipMd5AuthKey_Type.__name__ = "OctetString"
_FsMIRipMd5AuthKey_Object = MibTableColumn
fsMIRipMd5AuthKey = _FsMIRipMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 5, 1, 3),
    _FsMIRipMd5AuthKey_Type()
)
fsMIRipMd5AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipMd5AuthKey.setStatus("current")
_FsMIRipMd5KeyStartTime_Type = Integer32
_FsMIRipMd5KeyStartTime_Object = MibTableColumn
fsMIRipMd5KeyStartTime = _FsMIRipMd5KeyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 5, 1, 4),
    _FsMIRipMd5KeyStartTime_Type()
)
fsMIRipMd5KeyStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipMd5KeyStartTime.setStatus("current")
_FsMIRipMd5KeyExpiryTime_Type = Integer32
_FsMIRipMd5KeyExpiryTime_Object = MibTableColumn
fsMIRipMd5KeyExpiryTime = _FsMIRipMd5KeyExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 5, 1, 5),
    _FsMIRipMd5KeyExpiryTime_Type()
)
fsMIRipMd5KeyExpiryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipMd5KeyExpiryTime.setStatus("current")
_FsMIRipMd5KeyRowStatus_Type = RowStatus
_FsMIRipMd5KeyRowStatus_Object = MibTableColumn
fsMIRipMd5KeyRowStatus = _FsMIRipMd5KeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 5, 1, 6),
    _FsMIRipMd5KeyRowStatus_Type()
)
fsMIRipMd5KeyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipMd5KeyRowStatus.setStatus("current")
_FsMIRip2NBRUnicastListTable_Object = MibTable
fsMIRip2NBRUnicastListTable = _FsMIRip2NBRUnicastListTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 6)
)
if mibBuilder.loadTexts:
    fsMIRip2NBRUnicastListTable.setStatus("current")
_FsMIRip2NBRUnicastListEntry_Object = MibTableRow
fsMIRip2NBRUnicastListEntry = _FsMIRip2NBRUnicastListEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 6, 1)
)
fsMIRip2NBRUnicastListEntry.setIndexNames(
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipContextId"),
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRip2NBRUnicastIpAddr"),
)
if mibBuilder.loadTexts:
    fsMIRip2NBRUnicastListEntry.setStatus("current")
_FsMIRip2NBRUnicastIpAddr_Type = IpAddress
_FsMIRip2NBRUnicastIpAddr_Object = MibTableColumn
fsMIRip2NBRUnicastIpAddr = _FsMIRip2NBRUnicastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 6, 1, 1),
    _FsMIRip2NBRUnicastIpAddr_Type()
)
fsMIRip2NBRUnicastIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRip2NBRUnicastIpAddr.setStatus("current")
_FsMIRip2NBRUnicastNBRRowStatus_Type = RowStatus
_FsMIRip2NBRUnicastNBRRowStatus_Object = MibTableColumn
fsMIRip2NBRUnicastNBRRowStatus = _FsMIRip2NBRUnicastNBRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 6, 1, 2),
    _FsMIRip2NBRUnicastNBRRowStatus_Type()
)
fsMIRip2NBRUnicastNBRRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRip2NBRUnicastNBRRowStatus.setStatus("current")
_FsMIRip2LocalRouteTable_Object = MibTable
fsMIRip2LocalRouteTable = _FsMIRip2LocalRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 7)
)
if mibBuilder.loadTexts:
    fsMIRip2LocalRouteTable.setStatus("current")
_FsMIRip2LocalRouteEntry_Object = MibTableRow
fsMIRip2LocalRouteEntry = _FsMIRip2LocalRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 7, 1)
)
fsMIRip2LocalRouteEntry.setIndexNames(
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipContextId"),
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRip2DestNet"),
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRip2DestMask"),
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRip2Tos"),
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRip2NextHop"),
)
if mibBuilder.loadTexts:
    fsMIRip2LocalRouteEntry.setStatus("current")
_FsMIRip2DestNet_Type = IpAddress
_FsMIRip2DestNet_Object = MibTableColumn
fsMIRip2DestNet = _FsMIRip2DestNet_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 7, 1, 1),
    _FsMIRip2DestNet_Type()
)
fsMIRip2DestNet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRip2DestNet.setStatus("current")
_FsMIRip2DestMask_Type = IpAddress
_FsMIRip2DestMask_Object = MibTableColumn
fsMIRip2DestMask = _FsMIRip2DestMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 7, 1, 2),
    _FsMIRip2DestMask_Type()
)
fsMIRip2DestMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRip2DestMask.setStatus("current")


class _FsMIRip2Tos_Type(Integer32):
    """Custom type fsMIRip2Tos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIRip2Tos_Type.__name__ = "Integer32"
_FsMIRip2Tos_Object = MibTableColumn
fsMIRip2Tos = _FsMIRip2Tos_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 7, 1, 3),
    _FsMIRip2Tos_Type()
)
fsMIRip2Tos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRip2Tos.setStatus("current")
_FsMIRip2NextHop_Type = IpAddress
_FsMIRip2NextHop_Object = MibTableColumn
fsMIRip2NextHop = _FsMIRip2NextHop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 7, 1, 4),
    _FsMIRip2NextHop_Type()
)
fsMIRip2NextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRip2NextHop.setStatus("current")
_FsMIRip2RtIfIndex_Type = Integer32
_FsMIRip2RtIfIndex_Object = MibTableColumn
fsMIRip2RtIfIndex = _FsMIRip2RtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 7, 1, 5),
    _FsMIRip2RtIfIndex_Type()
)
fsMIRip2RtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRip2RtIfIndex.setStatus("current")
_FsMIRip2RtType_Type = Integer32
_FsMIRip2RtType_Object = MibTableColumn
fsMIRip2RtType = _FsMIRip2RtType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 7, 1, 6),
    _FsMIRip2RtType_Type()
)
fsMIRip2RtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRip2RtType.setStatus("current")
_FsMIRip2Proto_Type = Integer32
_FsMIRip2Proto_Object = MibTableColumn
fsMIRip2Proto = _FsMIRip2Proto_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 7, 1, 7),
    _FsMIRip2Proto_Type()
)
fsMIRip2Proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRip2Proto.setStatus("current")
_FsMIRip2ChgTime_Type = Integer32
_FsMIRip2ChgTime_Object = MibTableColumn
fsMIRip2ChgTime = _FsMIRip2ChgTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 7, 1, 8),
    _FsMIRip2ChgTime_Type()
)
fsMIRip2ChgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRip2ChgTime.setStatus("current")
_FsMIRip2Metric_Type = Integer32
_FsMIRip2Metric_Object = MibTableColumn
fsMIRip2Metric = _FsMIRip2Metric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 7, 1, 9),
    _FsMIRip2Metric_Type()
)
fsMIRip2Metric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRip2Metric.setStatus("current")
_FsMIRip2RowStatus_Type = Integer32
_FsMIRip2RowStatus_Object = MibTableColumn
fsMIRip2RowStatus = _FsMIRip2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 7, 1, 10),
    _FsMIRip2RowStatus_Type()
)
fsMIRip2RowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRip2RowStatus.setStatus("current")
_FsMIRip2Gateway_Type = IpAddress
_FsMIRip2Gateway_Object = MibTableColumn
fsMIRip2Gateway = _FsMIRip2Gateway_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 7, 1, 11),
    _FsMIRip2Gateway_Type()
)
fsMIRip2Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRip2Gateway.setStatus("current")
_FsMIRipAggTable_Object = MibTable
fsMIRipAggTable = _FsMIRipAggTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 8)
)
if mibBuilder.loadTexts:
    fsMIRipAggTable.setStatus("current")
_FsMIRipAggEntry_Object = MibTableRow
fsMIRipAggEntry = _FsMIRipAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 8, 1)
)
fsMIRipAggEntry.setIndexNames(
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipContextId"),
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipIfIndex"),
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipAggAddress"),
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipAggAddressMask"),
)
if mibBuilder.loadTexts:
    fsMIRipAggEntry.setStatus("current")


class _FsMIRipIfIndex_Type(Integer32):
    """Custom type fsMIRipIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsMIRipIfIndex_Type.__name__ = "Integer32"
_FsMIRipIfIndex_Object = MibTableColumn
fsMIRipIfIndex = _FsMIRipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 8, 1, 1),
    _FsMIRipIfIndex_Type()
)
fsMIRipIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRipIfIndex.setStatus("current")
_FsMIRipAggAddress_Type = IpAddress
_FsMIRipAggAddress_Object = MibTableColumn
fsMIRipAggAddress = _FsMIRipAggAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 8, 1, 2),
    _FsMIRipAggAddress_Type()
)
fsMIRipAggAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRipAggAddress.setStatus("current")
_FsMIRipAggAddressMask_Type = IpAddress
_FsMIRipAggAddressMask_Object = MibTableColumn
fsMIRipAggAddressMask = _FsMIRipAggAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 8, 1, 3),
    _FsMIRipAggAddressMask_Type()
)
fsMIRipAggAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRipAggAddressMask.setStatus("current")
_FsMIRipAggStatus_Type = RowStatus
_FsMIRipAggStatus_Object = MibTableColumn
fsMIRipAggStatus = _FsMIRipAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 8, 1, 4),
    _FsMIRipAggStatus_Type()
)
fsMIRipAggStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipAggStatus.setStatus("current")
_FsMIRipCryptoAuthTable_Object = MibTable
fsMIRipCryptoAuthTable = _FsMIRipCryptoAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 9)
)
if mibBuilder.loadTexts:
    fsMIRipCryptoAuthTable.setStatus("current")
_FsMIRipCryptoAuthEntry_Object = MibTableRow
fsMIRipCryptoAuthEntry = _FsMIRipCryptoAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 9, 1)
)
fsMIRipCryptoAuthEntry.setIndexNames(
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipContextId"),
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipCryptoAuthIfIndex"),
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipCryptoAuthAddress"),
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipCryptoAuthKeyId"),
)
if mibBuilder.loadTexts:
    fsMIRipCryptoAuthEntry.setStatus("current")


class _FsMIRipCryptoAuthIfIndex_Type(InterfaceIndex):
    """Custom type fsMIRipCryptoAuthIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIRipCryptoAuthIfIndex_Type.__name__ = "InterfaceIndex"
_FsMIRipCryptoAuthIfIndex_Object = MibTableColumn
fsMIRipCryptoAuthIfIndex = _FsMIRipCryptoAuthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 9, 1, 1),
    _FsMIRipCryptoAuthIfIndex_Type()
)
fsMIRipCryptoAuthIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRipCryptoAuthIfIndex.setStatus("current")
_FsMIRipCryptoAuthAddress_Type = IpAddress
_FsMIRipCryptoAuthAddress_Object = MibTableColumn
fsMIRipCryptoAuthAddress = _FsMIRipCryptoAuthAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 9, 1, 2),
    _FsMIRipCryptoAuthAddress_Type()
)
fsMIRipCryptoAuthAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRipCryptoAuthAddress.setStatus("current")


class _FsMIRipCryptoAuthKeyId_Type(Integer32):
    """Custom type fsMIRipCryptoAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIRipCryptoAuthKeyId_Type.__name__ = "Integer32"
_FsMIRipCryptoAuthKeyId_Object = MibTableColumn
fsMIRipCryptoAuthKeyId = _FsMIRipCryptoAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 9, 1, 3),
    _FsMIRipCryptoAuthKeyId_Type()
)
fsMIRipCryptoAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRipCryptoAuthKeyId.setStatus("current")


class _FsMIRipCryptoAuthKey_Type(OctetString):
    """Custom type fsMIRipCryptoAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsMIRipCryptoAuthKey_Type.__name__ = "OctetString"
_FsMIRipCryptoAuthKey_Object = MibTableColumn
fsMIRipCryptoAuthKey = _FsMIRipCryptoAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 9, 1, 4),
    _FsMIRipCryptoAuthKey_Type()
)
fsMIRipCryptoAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipCryptoAuthKey.setStatus("current")
_FsMIRipCryptoKeyStartAccept_Type = DateAndTime
_FsMIRipCryptoKeyStartAccept_Object = MibTableColumn
fsMIRipCryptoKeyStartAccept = _FsMIRipCryptoKeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 9, 1, 5),
    _FsMIRipCryptoKeyStartAccept_Type()
)
fsMIRipCryptoKeyStartAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipCryptoKeyStartAccept.setStatus("current")
_FsMIRipCryptoKeyStartGenerate_Type = DateAndTime
_FsMIRipCryptoKeyStartGenerate_Object = MibTableColumn
fsMIRipCryptoKeyStartGenerate = _FsMIRipCryptoKeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 9, 1, 6),
    _FsMIRipCryptoKeyStartGenerate_Type()
)
fsMIRipCryptoKeyStartGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipCryptoKeyStartGenerate.setStatus("current")
_FsMIRipCryptoKeyStopGenerate_Type = DateAndTime
_FsMIRipCryptoKeyStopGenerate_Object = MibTableColumn
fsMIRipCryptoKeyStopGenerate = _FsMIRipCryptoKeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 9, 1, 7),
    _FsMIRipCryptoKeyStopGenerate_Type()
)
fsMIRipCryptoKeyStopGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipCryptoKeyStopGenerate.setStatus("current")
_FsMIRipCryptoKeyStopAccept_Type = DateAndTime
_FsMIRipCryptoKeyStopAccept_Object = MibTableColumn
fsMIRipCryptoKeyStopAccept = _FsMIRipCryptoKeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 9, 1, 8),
    _FsMIRipCryptoKeyStopAccept_Type()
)
fsMIRipCryptoKeyStopAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipCryptoKeyStopAccept.setStatus("current")


class _FsMIRipCryptoKeyStatus_Type(Integer32):
    """Custom type fsMIRipCryptoKeyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("delete", 2))
    )


_FsMIRipCryptoKeyStatus_Type.__name__ = "Integer32"
_FsMIRipCryptoKeyStatus_Object = MibTableColumn
fsMIRipCryptoKeyStatus = _FsMIRipCryptoKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 1, 9, 1, 9),
    _FsMIRipCryptoKeyStatus_Type()
)
fsMIRipCryptoKeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipCryptoKeyStatus.setStatus("current")
_FsMIRipRRDGeneralGroup_ObjectIdentity = ObjectIdentity
fsMIRipRRDGeneralGroup = _FsMIRipRRDGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 2)
)
_FsMIRipRRDGlobalTable_Object = MibTable
fsMIRipRRDGlobalTable = _FsMIRipRRDGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 2, 1)
)
if mibBuilder.loadTexts:
    fsMIRipRRDGlobalTable.setStatus("current")
_FsMIRipRRDGlobalEntry_Object = MibTableRow
fsMIRipRRDGlobalEntry = _FsMIRipRRDGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 2, 1, 1)
)
fsMIRipRRDGlobalEntry.setIndexNames(
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipContextId"),
)
if mibBuilder.loadTexts:
    fsMIRipRRDGlobalEntry.setStatus("current")


class _FsMIRipRRDGlobalStatus_Type(Integer32):
    """Custom type fsMIRipRRDGlobalStatus based on Integer32"""
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


_FsMIRipRRDGlobalStatus_Type.__name__ = "Integer32"
_FsMIRipRRDGlobalStatus_Object = MibTableColumn
fsMIRipRRDGlobalStatus = _FsMIRipRRDGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 2, 1, 1, 1),
    _FsMIRipRRDGlobalStatus_Type()
)
fsMIRipRRDGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipRRDGlobalStatus.setStatus("current")


class _FsMIRipRRDSrcProtoMaskEnable_Type(Integer32):
    """Custom type fsMIRipRRDSrcProtoMaskEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIRipRRDSrcProtoMaskEnable_Type.__name__ = "Integer32"
_FsMIRipRRDSrcProtoMaskEnable_Object = MibTableColumn
fsMIRipRRDSrcProtoMaskEnable = _FsMIRipRRDSrcProtoMaskEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 2, 1, 1, 2),
    _FsMIRipRRDSrcProtoMaskEnable_Type()
)
fsMIRipRRDSrcProtoMaskEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipRRDSrcProtoMaskEnable.setStatus("current")


class _FsMIRipRRDSrcProtoMaskDisable_Type(Integer32):
    """Custom type fsMIRipRRDSrcProtoMaskDisable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIRipRRDSrcProtoMaskDisable_Type.__name__ = "Integer32"
_FsMIRipRRDSrcProtoMaskDisable_Object = MibTableColumn
fsMIRipRRDSrcProtoMaskDisable = _FsMIRipRRDSrcProtoMaskDisable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 2, 1, 1, 3),
    _FsMIRipRRDSrcProtoMaskDisable_Type()
)
fsMIRipRRDSrcProtoMaskDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipRRDSrcProtoMaskDisable.setStatus("current")


class _FsMIRipRRDRouteTagType_Type(Integer32):
    """Custom type fsMIRipRRDRouteTagType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("automatic", 2))
    )


_FsMIRipRRDRouteTagType_Type.__name__ = "Integer32"
_FsMIRipRRDRouteTagType_Object = MibTableColumn
fsMIRipRRDRouteTagType = _FsMIRipRRDRouteTagType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 2, 1, 1, 4),
    _FsMIRipRRDRouteTagType_Type()
)
fsMIRipRRDRouteTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipRRDRouteTagType.setStatus("current")


class _FsMIRipRRDRouteTag_Type(Integer32):
    """Custom type fsMIRipRRDRouteTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIRipRRDRouteTag_Type.__name__ = "Integer32"
_FsMIRipRRDRouteTag_Object = MibTableColumn
fsMIRipRRDRouteTag = _FsMIRipRRDRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 2, 1, 1, 5),
    _FsMIRipRRDRouteTag_Type()
)
fsMIRipRRDRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipRRDRouteTag.setStatus("current")


class _FsMIRipRRDRouteDefMetric_Type(Integer32):
    """Custom type fsMIRipRRDRouteDefMetric based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FsMIRipRRDRouteDefMetric_Type.__name__ = "Integer32"
_FsMIRipRRDRouteDefMetric_Object = MibTableColumn
fsMIRipRRDRouteDefMetric = _FsMIRipRRDRouteDefMetric_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 2, 1, 1, 6),
    _FsMIRipRRDRouteDefMetric_Type()
)
fsMIRipRRDRouteDefMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipRRDRouteDefMetric.setStatus("current")


class _FsMIRipRRDRouteMapEnable_Type(DisplayString):
    """Custom type fsMIRipRRDRouteMapEnable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_FsMIRipRRDRouteMapEnable_Type.__name__ = "DisplayString"
_FsMIRipRRDRouteMapEnable_Object = MibTableColumn
fsMIRipRRDRouteMapEnable = _FsMIRipRRDRouteMapEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 2, 1, 1, 7),
    _FsMIRipRRDRouteMapEnable_Type()
)
fsMIRipRRDRouteMapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipRRDRouteMapEnable.setStatus("current")
_FsMIripDistInOutRouteMap_ObjectIdentity = ObjectIdentity
fsMIripDistInOutRouteMap = _FsMIripDistInOutRouteMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 3)
)
_FsMIRipDistInOutRouteMapTable_Object = MibTable
fsMIRipDistInOutRouteMapTable = _FsMIRipDistInOutRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 3, 1)
)
if mibBuilder.loadTexts:
    fsMIRipDistInOutRouteMapTable.setStatus("current")
_FsMIRipDistInOutRouteMapEntry_Object = MibTableRow
fsMIRipDistInOutRouteMapEntry = _FsMIRipDistInOutRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 3, 1, 1)
)
fsMIRipDistInOutRouteMapEntry.setIndexNames(
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipContextId"),
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipDistInOutRouteMapName"),
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipDistInOutRouteMapType"),
)
if mibBuilder.loadTexts:
    fsMIRipDistInOutRouteMapEntry.setStatus("current")


class _FsMIRipDistInOutRouteMapName_Type(DisplayString):
    """Custom type fsMIRipDistInOutRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsMIRipDistInOutRouteMapName_Type.__name__ = "DisplayString"
_FsMIRipDistInOutRouteMapName_Object = MibTableColumn
fsMIRipDistInOutRouteMapName = _FsMIRipDistInOutRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 3, 1, 1, 1),
    _FsMIRipDistInOutRouteMapName_Type()
)
fsMIRipDistInOutRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRipDistInOutRouteMapName.setStatus("current")


class _FsMIRipDistInOutRouteMapType_Type(Integer32):
    """Custom type fsMIRipDistInOutRouteMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsMIRipDistInOutRouteMapType_Type.__name__ = "Integer32"
_FsMIRipDistInOutRouteMapType_Object = MibTableColumn
fsMIRipDistInOutRouteMapType = _FsMIRipDistInOutRouteMapType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 3, 1, 1, 2),
    _FsMIRipDistInOutRouteMapType_Type()
)
fsMIRipDistInOutRouteMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRipDistInOutRouteMapType.setStatus("current")


class _FsMIRipDistInOutRouteMapValue_Type(Integer32):
    """Custom type fsMIRipDistInOutRouteMapValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsMIRipDistInOutRouteMapValue_Type.__name__ = "Integer32"
_FsMIRipDistInOutRouteMapValue_Object = MibTableColumn
fsMIRipDistInOutRouteMapValue = _FsMIRipDistInOutRouteMapValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 3, 1, 1, 3),
    _FsMIRipDistInOutRouteMapValue_Type()
)
fsMIRipDistInOutRouteMapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipDistInOutRouteMapValue.setStatus("current")
_FsMIRipDistInOutRouteMapRowStatus_Type = RowStatus
_FsMIRipDistInOutRouteMapRowStatus_Object = MibTableColumn
fsMIRipDistInOutRouteMapRowStatus = _FsMIRipDistInOutRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 3, 1, 1, 4),
    _FsMIRipDistInOutRouteMapRowStatus_Type()
)
fsMIRipDistInOutRouteMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipDistInOutRouteMapRowStatus.setStatus("current")
_FsMIripPreferenceGroup_ObjectIdentity = ObjectIdentity
fsMIripPreferenceGroup = _FsMIripPreferenceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 4)
)
_FsMIRipPreferenceTable_Object = MibTable
fsMIRipPreferenceTable = _FsMIRipPreferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 4, 1)
)
if mibBuilder.loadTexts:
    fsMIRipPreferenceTable.setStatus("current")
_FsMIRipPreferenceEntry_Object = MibTableRow
fsMIRipPreferenceEntry = _FsMIRipPreferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 4, 1, 1)
)
fsMIRipPreferenceEntry.setIndexNames(
    (0, "SUPERMICRO-MIRIP2-MIB", "fsMIRipContextId"),
)
if mibBuilder.loadTexts:
    fsMIRipPreferenceEntry.setStatus("current")


class _FsMIRipPreferenceValue_Type(Integer32):
    """Custom type fsMIRipPreferenceValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIRipPreferenceValue_Type.__name__ = "Integer32"
_FsMIRipPreferenceValue_Object = MibTableColumn
fsMIRipPreferenceValue = _FsMIRipPreferenceValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 4, 1, 1, 1),
    _FsMIRipPreferenceValue_Type()
)
fsMIRipPreferenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRipPreferenceValue.setStatus("current")
_FsMIRip2TrapsControl_ObjectIdentity = ObjectIdentity
fsMIRip2TrapsControl = _FsMIRip2TrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 5)
)


class _FsMIRip2ContextId_Type(Integer32):
    """Custom type fsMIRip2ContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIRip2ContextId_Type.__name__ = "Integer32"
_FsMIRip2ContextId_Object = MibScalar
fsMIRip2ContextId = _FsMIRip2ContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 5, 1),
    _FsMIRip2ContextId_Type()
)
fsMIRip2ContextId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMIRip2ContextId.setStatus("current")


class _FsMIRipAuthIfIndex_Type(InterfaceIndex):
    """Custom type fsMIRipAuthIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIRipAuthIfIndex_Type.__name__ = "InterfaceIndex"
_FsMIRipAuthIfIndex_Object = MibScalar
fsMIRipAuthIfIndex = _FsMIRipAuthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 5, 2),
    _FsMIRipAuthIfIndex_Type()
)
fsMIRipAuthIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMIRipAuthIfIndex.setStatus("current")


class _FsMIRipAuthKeyId_Type(Integer32):
    """Custom type fsMIRipAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIRipAuthKeyId_Type.__name__ = "Integer32"
_FsMIRipAuthKeyId_Object = MibScalar
fsMIRipAuthKeyId = _FsMIRipAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 5, 3),
    _FsMIRipAuthKeyId_Type()
)
fsMIRipAuthKeyId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMIRipAuthKeyId.setStatus("current")
_FsMIRipPeerAddress_Type = IpAddress
_FsMIRipPeerAddress_Object = MibScalar
fsMIRipPeerAddress = _FsMIRipPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 5, 4),
    _FsMIRipPeerAddress_Type()
)
fsMIRipPeerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMIRipPeerAddress.setStatus("current")
_FsMIRip2Notification_ObjectIdentity = ObjectIdentity
fsMIRip2Notification = _FsMIRip2Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 6)
)
_FsMIRip2Traps_ObjectIdentity = ObjectIdentity
fsMIRip2Traps = _FsMIRip2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 6, 0)
)

# Managed Objects groups


# Notification objects

fsMIRip2AuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 6, 0, 1)
)
fsMIRip2AuthenticationFailure.setObjects(
      *(("SUPERMICRO-MIRIP2-MIB", "fsMIRip2ContextId"),
        ("SUPERMICRO-MIRIP2-MIB", "fsMIRipPeerAddress"),
        ("SUPERMICRO-MIRIP2-MIB", "fsMIRipAuthIfIndex"),
        ("SUPERMICRO-MIRIP2-MIB", "fsMIRipAuthKeyId"))
)
if mibBuilder.loadTexts:
    fsMIRip2AuthenticationFailure.setStatus(
        "current"
    )

fsMIRip2AuthLastKey = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 151, 6, 0, 2)
)
fsMIRip2AuthLastKey.setObjects(
      *(("SUPERMICRO-MIRIP2-MIB", "fsMIRip2ContextId"),
        ("SUPERMICRO-MIRIP2-MIB", "fsMIRipAuthIfIndex"),
        ("SUPERMICRO-MIRIP2-MIB", "fsMIRipAuthKeyId"))
)
if mibBuilder.loadTexts:
    fsMIRip2AuthLastKey.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-MIRIP2-MIB",
    **{"fsMIRip": fsMIRip,
       "fsMIRip2GeneralGroup": fsMIRip2GeneralGroup,
       "fsMIRip2GlobalTable": fsMIRip2GlobalTable,
       "fsMIRip2GlobalEntry": fsMIRip2GlobalEntry,
       "fsMIRipContextId": fsMIRipContextId,
       "fsMIRip2Security": fsMIRip2Security,
       "fsMIRip2Peers": fsMIRip2Peers,
       "fsMIRip2TrustNBRListEnable": fsMIRip2TrustNBRListEnable,
       "fsMIRip2NumberOfDroppedPkts": fsMIRip2NumberOfDroppedPkts,
       "fsMIRip2SpacingEnable": fsMIRip2SpacingEnable,
       "fsMIRip2AutoSummaryStatus": fsMIRip2AutoSummaryStatus,
       "fsMIRip2RetransTimeoutInt": fsMIRip2RetransTimeoutInt,
       "fsMIRip2MaxRetransmissions": fsMIRip2MaxRetransmissions,
       "fsMIRip2OverSubscriptionTimeout": fsMIRip2OverSubscriptionTimeout,
       "fsMIRip2Propagate": fsMIRip2Propagate,
       "fsMIRipTrcFlag": fsMIRipTrcFlag,
       "fsMIRipRowStatus": fsMIRipRowStatus,
       "fsMIRipAdminStatus": fsMIRipAdminStatus,
       "fsMIRip2LastAuthKeyLifetimeStatus": fsMIRip2LastAuthKeyLifetimeStatus,
       "fsMIRipRtCount": fsMIRipRtCount,
       "fsMIRipGlobalTrcFlag": fsMIRipGlobalTrcFlag,
       "fsMIRip2NBRTrustListTable": fsMIRip2NBRTrustListTable,
       "fsMIRip2NBRTrustListEntry": fsMIRip2NBRTrustListEntry,
       "fsMIRip2TrustNBRIpAddr": fsMIRip2TrustNBRIpAddr,
       "fsMIRip2TrustNBRRowStatus": fsMIRip2TrustNBRRowStatus,
       "fsMIRip2IfConfTable": fsMIRip2IfConfTable,
       "fsMIRip2IfConfEntry": fsMIRip2IfConfEntry,
       "fsMIRip2IfConfAddress": fsMIRip2IfConfAddress,
       "fsMIRip2IfAdminStat": fsMIRip2IfAdminStat,
       "fsMIRip2IfConfOperState": fsMIRip2IfConfOperState,
       "fsMIRip2IfConfUpdateTmr": fsMIRip2IfConfUpdateTmr,
       "fsMIRip2IfConfGarbgCollectTmr": fsMIRip2IfConfGarbgCollectTmr,
       "fsMIRip2IfConfRouteAgeTmr": fsMIRip2IfConfRouteAgeTmr,
       "fsMIRip2IfSplitHorizonStatus": fsMIRip2IfSplitHorizonStatus,
       "fsMIRip2IfConfDefRtInstall": fsMIRip2IfConfDefRtInstall,
       "fsMIRip2IfConfSpacingTmr": fsMIRip2IfConfSpacingTmr,
       "fsMIRip2IfConfInUseKey": fsMIRip2IfConfInUseKey,
       "fsMIRip2IfConfAuthLastKeyStatus": fsMIRip2IfConfAuthLastKeyStatus,
       "fsMIRipMd5AuthTable": fsMIRipMd5AuthTable,
       "fsMIRipMd5AuthEntry": fsMIRipMd5AuthEntry,
       "fsMIRipMd5AuthAddress": fsMIRipMd5AuthAddress,
       "fsMIRipMd5AuthKeyId": fsMIRipMd5AuthKeyId,
       "fsMIRipMd5AuthKey": fsMIRipMd5AuthKey,
       "fsMIRipMd5KeyStartTime": fsMIRipMd5KeyStartTime,
       "fsMIRipMd5KeyExpiryTime": fsMIRipMd5KeyExpiryTime,
       "fsMIRipMd5KeyRowStatus": fsMIRipMd5KeyRowStatus,
       "fsMIRip2NBRUnicastListTable": fsMIRip2NBRUnicastListTable,
       "fsMIRip2NBRUnicastListEntry": fsMIRip2NBRUnicastListEntry,
       "fsMIRip2NBRUnicastIpAddr": fsMIRip2NBRUnicastIpAddr,
       "fsMIRip2NBRUnicastNBRRowStatus": fsMIRip2NBRUnicastNBRRowStatus,
       "fsMIRip2LocalRouteTable": fsMIRip2LocalRouteTable,
       "fsMIRip2LocalRouteEntry": fsMIRip2LocalRouteEntry,
       "fsMIRip2DestNet": fsMIRip2DestNet,
       "fsMIRip2DestMask": fsMIRip2DestMask,
       "fsMIRip2Tos": fsMIRip2Tos,
       "fsMIRip2NextHop": fsMIRip2NextHop,
       "fsMIRip2RtIfIndex": fsMIRip2RtIfIndex,
       "fsMIRip2RtType": fsMIRip2RtType,
       "fsMIRip2Proto": fsMIRip2Proto,
       "fsMIRip2ChgTime": fsMIRip2ChgTime,
       "fsMIRip2Metric": fsMIRip2Metric,
       "fsMIRip2RowStatus": fsMIRip2RowStatus,
       "fsMIRip2Gateway": fsMIRip2Gateway,
       "fsMIRipAggTable": fsMIRipAggTable,
       "fsMIRipAggEntry": fsMIRipAggEntry,
       "fsMIRipIfIndex": fsMIRipIfIndex,
       "fsMIRipAggAddress": fsMIRipAggAddress,
       "fsMIRipAggAddressMask": fsMIRipAggAddressMask,
       "fsMIRipAggStatus": fsMIRipAggStatus,
       "fsMIRipCryptoAuthTable": fsMIRipCryptoAuthTable,
       "fsMIRipCryptoAuthEntry": fsMIRipCryptoAuthEntry,
       "fsMIRipCryptoAuthIfIndex": fsMIRipCryptoAuthIfIndex,
       "fsMIRipCryptoAuthAddress": fsMIRipCryptoAuthAddress,
       "fsMIRipCryptoAuthKeyId": fsMIRipCryptoAuthKeyId,
       "fsMIRipCryptoAuthKey": fsMIRipCryptoAuthKey,
       "fsMIRipCryptoKeyStartAccept": fsMIRipCryptoKeyStartAccept,
       "fsMIRipCryptoKeyStartGenerate": fsMIRipCryptoKeyStartGenerate,
       "fsMIRipCryptoKeyStopGenerate": fsMIRipCryptoKeyStopGenerate,
       "fsMIRipCryptoKeyStopAccept": fsMIRipCryptoKeyStopAccept,
       "fsMIRipCryptoKeyStatus": fsMIRipCryptoKeyStatus,
       "fsMIRipRRDGeneralGroup": fsMIRipRRDGeneralGroup,
       "fsMIRipRRDGlobalTable": fsMIRipRRDGlobalTable,
       "fsMIRipRRDGlobalEntry": fsMIRipRRDGlobalEntry,
       "fsMIRipRRDGlobalStatus": fsMIRipRRDGlobalStatus,
       "fsMIRipRRDSrcProtoMaskEnable": fsMIRipRRDSrcProtoMaskEnable,
       "fsMIRipRRDSrcProtoMaskDisable": fsMIRipRRDSrcProtoMaskDisable,
       "fsMIRipRRDRouteTagType": fsMIRipRRDRouteTagType,
       "fsMIRipRRDRouteTag": fsMIRipRRDRouteTag,
       "fsMIRipRRDRouteDefMetric": fsMIRipRRDRouteDefMetric,
       "fsMIRipRRDRouteMapEnable": fsMIRipRRDRouteMapEnable,
       "fsMIripDistInOutRouteMap": fsMIripDistInOutRouteMap,
       "fsMIRipDistInOutRouteMapTable": fsMIRipDistInOutRouteMapTable,
       "fsMIRipDistInOutRouteMapEntry": fsMIRipDistInOutRouteMapEntry,
       "fsMIRipDistInOutRouteMapName": fsMIRipDistInOutRouteMapName,
       "fsMIRipDistInOutRouteMapType": fsMIRipDistInOutRouteMapType,
       "fsMIRipDistInOutRouteMapValue": fsMIRipDistInOutRouteMapValue,
       "fsMIRipDistInOutRouteMapRowStatus": fsMIRipDistInOutRouteMapRowStatus,
       "fsMIripPreferenceGroup": fsMIripPreferenceGroup,
       "fsMIRipPreferenceTable": fsMIRipPreferenceTable,
       "fsMIRipPreferenceEntry": fsMIRipPreferenceEntry,
       "fsMIRipPreferenceValue": fsMIRipPreferenceValue,
       "fsMIRip2TrapsControl": fsMIRip2TrapsControl,
       "fsMIRip2ContextId": fsMIRip2ContextId,
       "fsMIRipAuthIfIndex": fsMIRipAuthIfIndex,
       "fsMIRipAuthKeyId": fsMIRipAuthKeyId,
       "fsMIRipPeerAddress": fsMIRipPeerAddress,
       "fsMIRip2Notification": fsMIRip2Notification,
       "fsMIRip2Traps": fsMIRip2Traps,
       "fsMIRip2AuthenticationFailure": fsMIRip2AuthenticationFailure,
       "fsMIRip2AuthLastKey": fsMIRip2AuthLastKey}
)
