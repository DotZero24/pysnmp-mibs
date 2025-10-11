# SNMP MIB module (FUTURESOFT-RIP2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/FUTURESOFT-RIP2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:54 2025
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

(rip2IfStatEntry,
 rip2PeerAddress,
 rip2PeerEntry) = mibBuilder.importSymbols(
    "RIPv2-MIB",
    "rip2IfStatEntry",
    "rip2PeerAddress",
    "rip2PeerEntry")

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

fsrip = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 75)
)
if mibBuilder.loadTexts:
    fsrip.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rip2GeneralGroup_ObjectIdentity = ObjectIdentity
rip2GeneralGroup = _Rip2GeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1)
)


class _FsRip2Security_Type(Integer32):
    """Custom type fsRip2Security based on Integer32"""
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


_FsRip2Security_Type.__name__ = "Integer32"
_FsRip2Security_Object = MibScalar
fsRip2Security = _FsRip2Security_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 1),
    _FsRip2Security_Type()
)
fsRip2Security.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2Security.setStatus("current")


class _FsRip2Peers_Type(Integer32):
    """Custom type fsRip2Peers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsRip2Peers_Type.__name__ = "Integer32"
_FsRip2Peers_Object = MibScalar
fsRip2Peers = _FsRip2Peers_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 2),
    _FsRip2Peers_Type()
)
fsRip2Peers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2Peers.setStatus("current")


class _FsRip2TrustNBRListEnable_Type(Integer32):
    """Custom type fsRip2TrustNBRListEnable based on Integer32"""
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


_FsRip2TrustNBRListEnable_Type.__name__ = "Integer32"
_FsRip2TrustNBRListEnable_Object = MibScalar
fsRip2TrustNBRListEnable = _FsRip2TrustNBRListEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 3),
    _FsRip2TrustNBRListEnable_Type()
)
fsRip2TrustNBRListEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2TrustNBRListEnable.setStatus("current")
_FsRip2NumberOfDroppedPkts_Type = Counter32
_FsRip2NumberOfDroppedPkts_Object = MibScalar
fsRip2NumberOfDroppedPkts = _FsRip2NumberOfDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 4),
    _FsRip2NumberOfDroppedPkts_Type()
)
fsRip2NumberOfDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRip2NumberOfDroppedPkts.setStatus("current")


class _FsRip2SpacingEnable_Type(Integer32):
    """Custom type fsRip2SpacingEnable based on Integer32"""
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


_FsRip2SpacingEnable_Type.__name__ = "Integer32"
_FsRip2SpacingEnable_Object = MibScalar
fsRip2SpacingEnable = _FsRip2SpacingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 5),
    _FsRip2SpacingEnable_Type()
)
fsRip2SpacingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2SpacingEnable.setStatus("current")


class _FsRip2AutoSummaryStatus_Type(Integer32):
    """Custom type fsRip2AutoSummaryStatus based on Integer32"""
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


_FsRip2AutoSummaryStatus_Type.__name__ = "Integer32"
_FsRip2AutoSummaryStatus_Object = MibScalar
fsRip2AutoSummaryStatus = _FsRip2AutoSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 6),
    _FsRip2AutoSummaryStatus_Type()
)
fsRip2AutoSummaryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2AutoSummaryStatus.setStatus("current")


class _FsRip2RetransTimeoutInt_Type(Integer32):
    """Custom type fsRip2RetransTimeoutInt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10),
    )


_FsRip2RetransTimeoutInt_Type.__name__ = "Integer32"
_FsRip2RetransTimeoutInt_Object = MibScalar
fsRip2RetransTimeoutInt = _FsRip2RetransTimeoutInt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 7),
    _FsRip2RetransTimeoutInt_Type()
)
fsRip2RetransTimeoutInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2RetransTimeoutInt.setStatus("current")


class _FsRip2MaxRetransmissions_Type(Integer32):
    """Custom type fsRip2MaxRetransmissions based on Integer32"""
    defaultValue = 36

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 40),
    )


_FsRip2MaxRetransmissions_Type.__name__ = "Integer32"
_FsRip2MaxRetransmissions_Object = MibScalar
fsRip2MaxRetransmissions = _FsRip2MaxRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 8),
    _FsRip2MaxRetransmissions_Type()
)
fsRip2MaxRetransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2MaxRetransmissions.setStatus("current")


class _FsRip2OverSubscriptionTimeout_Type(Integer32):
    """Custom type fsRip2OverSubscriptionTimeout based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 300),
    )


_FsRip2OverSubscriptionTimeout_Type.__name__ = "Integer32"
_FsRip2OverSubscriptionTimeout_Object = MibScalar
fsRip2OverSubscriptionTimeout = _FsRip2OverSubscriptionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 9),
    _FsRip2OverSubscriptionTimeout_Type()
)
fsRip2OverSubscriptionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2OverSubscriptionTimeout.setStatus("current")


class _FsRip2Propagate_Type(Integer32):
    """Custom type fsRip2Propagate based on Integer32"""
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


_FsRip2Propagate_Type.__name__ = "Integer32"
_FsRip2Propagate_Object = MibScalar
fsRip2Propagate = _FsRip2Propagate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 10),
    _FsRip2Propagate_Type()
)
fsRip2Propagate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2Propagate.setStatus("current")


class _FsRip2MaxRoutes_Type(Integer32):
    """Custom type fsRip2MaxRoutes based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 10000),
    )


_FsRip2MaxRoutes_Type.__name__ = "Integer32"
_FsRip2MaxRoutes_Object = MibScalar
fsRip2MaxRoutes = _FsRip2MaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 11),
    _FsRip2MaxRoutes_Type()
)
fsRip2MaxRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2MaxRoutes.setStatus("deprecated")


class _FsRipTrcFlag_Type(Integer32):
    """Custom type fsRipTrcFlag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsRipTrcFlag_Type.__name__ = "Integer32"
_FsRipTrcFlag_Object = MibScalar
fsRipTrcFlag = _FsRipTrcFlag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 12),
    _FsRipTrcFlag_Type()
)
fsRipTrcFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipTrcFlag.setStatus("current")
_FsRip2NBRTrustListTable_Object = MibTable
fsRip2NBRTrustListTable = _FsRip2NBRTrustListTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 13)
)
if mibBuilder.loadTexts:
    fsRip2NBRTrustListTable.setStatus("current")
_FsRip2NBRTrustListEntry_Object = MibTableRow
fsRip2NBRTrustListEntry = _FsRip2NBRTrustListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 13, 1)
)
fsRip2NBRTrustListEntry.setIndexNames(
    (0, "FUTURESOFT-RIP2-MIB", "fsRip2TrustNBRIpAddr"),
)
if mibBuilder.loadTexts:
    fsRip2NBRTrustListEntry.setStatus("current")
_FsRip2TrustNBRIpAddr_Type = IpAddress
_FsRip2TrustNBRIpAddr_Object = MibTableColumn
fsRip2TrustNBRIpAddr = _FsRip2TrustNBRIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 13, 1, 1),
    _FsRip2TrustNBRIpAddr_Type()
)
fsRip2TrustNBRIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRip2TrustNBRIpAddr.setStatus("current")
_FsRip2TrustNBRRowStatus_Type = RowStatus
_FsRip2TrustNBRRowStatus_Object = MibTableColumn
fsRip2TrustNBRRowStatus = _FsRip2TrustNBRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 13, 1, 2),
    _FsRip2TrustNBRRowStatus_Type()
)
fsRip2TrustNBRRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2TrustNBRRowStatus.setStatus("current")
_FsRip2IfConfTable_Object = MibTable
fsRip2IfConfTable = _FsRip2IfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 14)
)
if mibBuilder.loadTexts:
    fsRip2IfConfTable.setStatus("current")
_FsRip2IfConfEntry_Object = MibTableRow
fsRip2IfConfEntry = _FsRip2IfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 14, 1)
)
fsRip2IfConfEntry.setIndexNames(
    (0, "FUTURESOFT-RIP2-MIB", "fsRip2IfConfAddress"),
)
if mibBuilder.loadTexts:
    fsRip2IfConfEntry.setStatus("current")
_FsRip2IfConfAddress_Type = IpAddress
_FsRip2IfConfAddress_Object = MibTableColumn
fsRip2IfConfAddress = _FsRip2IfConfAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 14, 1, 1),
    _FsRip2IfConfAddress_Type()
)
fsRip2IfConfAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRip2IfConfAddress.setStatus("current")


class _FsRip2IfAdminStat_Type(Integer32):
    """Custom type fsRip2IfAdminStat based on Integer32"""
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


_FsRip2IfAdminStat_Type.__name__ = "Integer32"
_FsRip2IfAdminStat_Object = MibTableColumn
fsRip2IfAdminStat = _FsRip2IfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 14, 1, 2),
    _FsRip2IfAdminStat_Type()
)
fsRip2IfAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2IfAdminStat.setStatus("current")


class _FsRip2IfConfOperState_Type(Integer32):
    """Custom type fsRip2IfConfOperState based on Integer32"""
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


_FsRip2IfConfOperState_Type.__name__ = "Integer32"
_FsRip2IfConfOperState_Object = MibTableColumn
fsRip2IfConfOperState = _FsRip2IfConfOperState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 14, 1, 3),
    _FsRip2IfConfOperState_Type()
)
fsRip2IfConfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRip2IfConfOperState.setStatus("current")


class _FsRip2IfConfUpdateTmr_Type(Integer32):
    """Custom type fsRip2IfConfUpdateTmr based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_FsRip2IfConfUpdateTmr_Type.__name__ = "Integer32"
_FsRip2IfConfUpdateTmr_Object = MibTableColumn
fsRip2IfConfUpdateTmr = _FsRip2IfConfUpdateTmr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 14, 1, 4),
    _FsRip2IfConfUpdateTmr_Type()
)
fsRip2IfConfUpdateTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2IfConfUpdateTmr.setStatus("current")


class _FsRip2IfConfGarbgCollectTmr_Type(Integer32):
    """Custom type fsRip2IfConfGarbgCollectTmr based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 180),
    )


_FsRip2IfConfGarbgCollectTmr_Type.__name__ = "Integer32"
_FsRip2IfConfGarbgCollectTmr_Object = MibTableColumn
fsRip2IfConfGarbgCollectTmr = _FsRip2IfConfGarbgCollectTmr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 14, 1, 5),
    _FsRip2IfConfGarbgCollectTmr_Type()
)
fsRip2IfConfGarbgCollectTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2IfConfGarbgCollectTmr.setStatus("current")


class _FsRip2IfConfRouteAgeTmr_Type(Integer32):
    """Custom type fsRip2IfConfRouteAgeTmr based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 500),
    )


_FsRip2IfConfRouteAgeTmr_Type.__name__ = "Integer32"
_FsRip2IfConfRouteAgeTmr_Object = MibTableColumn
fsRip2IfConfRouteAgeTmr = _FsRip2IfConfRouteAgeTmr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 14, 1, 6),
    _FsRip2IfConfRouteAgeTmr_Type()
)
fsRip2IfConfRouteAgeTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2IfConfRouteAgeTmr.setStatus("current")


class _FsRip2IfSplitHorizonStatus_Type(Integer32):
    """Custom type fsRip2IfSplitHorizonStatus based on Integer32"""
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


_FsRip2IfSplitHorizonStatus_Type.__name__ = "Integer32"
_FsRip2IfSplitHorizonStatus_Object = MibTableColumn
fsRip2IfSplitHorizonStatus = _FsRip2IfSplitHorizonStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 14, 1, 7),
    _FsRip2IfSplitHorizonStatus_Type()
)
fsRip2IfSplitHorizonStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2IfSplitHorizonStatus.setStatus("current")


class _FsRip2IfConfDefRtInstall_Type(Integer32):
    """Custom type fsRip2IfConfDefRtInstall based on Integer32"""
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


_FsRip2IfConfDefRtInstall_Type.__name__ = "Integer32"
_FsRip2IfConfDefRtInstall_Object = MibTableColumn
fsRip2IfConfDefRtInstall = _FsRip2IfConfDefRtInstall_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 14, 1, 8),
    _FsRip2IfConfDefRtInstall_Type()
)
fsRip2IfConfDefRtInstall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2IfConfDefRtInstall.setStatus("current")


class _FsRip2IfConfSpacingTmr_Type(Integer32):
    """Custom type fsRip2IfConfSpacingTmr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 360),
    )


_FsRip2IfConfSpacingTmr_Type.__name__ = "Integer32"
_FsRip2IfConfSpacingTmr_Object = MibTableColumn
fsRip2IfConfSpacingTmr = _FsRip2IfConfSpacingTmr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 14, 1, 9),
    _FsRip2IfConfSpacingTmr_Type()
)
fsRip2IfConfSpacingTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2IfConfSpacingTmr.setStatus("current")


class _FsRip2IfConfAuthType_Type(Integer32):
    """Custom type fsRip2IfConfAuthType based on Integer32"""
    defaultValue = 1

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
        *(("md5", 1),
          ("sha1", 2),
          ("sha256", 3),
          ("sha384", 4),
          ("sha512", 5))
    )


_FsRip2IfConfAuthType_Type.__name__ = "Integer32"
_FsRip2IfConfAuthType_Object = MibTableColumn
fsRip2IfConfAuthType = _FsRip2IfConfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 14, 1, 10),
    _FsRip2IfConfAuthType_Type()
)
fsRip2IfConfAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRip2IfConfAuthType.setStatus("current")


class _FsRip2IfConfInUseKey_Type(Integer32):
    """Custom type fsRip2IfConfInUseKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsRip2IfConfInUseKey_Type.__name__ = "Integer32"
_FsRip2IfConfInUseKey_Object = MibTableColumn
fsRip2IfConfInUseKey = _FsRip2IfConfInUseKey_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 14, 1, 11),
    _FsRip2IfConfInUseKey_Type()
)
fsRip2IfConfInUseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRip2IfConfInUseKey.setStatus("current")


class _FsRip2IfConfAuthLastKeyStatus_Type(TruthValue):
    """Custom type fsRip2IfConfAuthLastKeyStatus based on TruthValue"""
    defaultValue = 2


_FsRip2IfConfAuthLastKeyStatus_Type.__name__ = "TruthValue"
_FsRip2IfConfAuthLastKeyStatus_Object = MibTableColumn
fsRip2IfConfAuthLastKeyStatus = _FsRip2IfConfAuthLastKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 14, 1, 12),
    _FsRip2IfConfAuthLastKeyStatus_Type()
)
fsRip2IfConfAuthLastKeyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRip2IfConfAuthLastKeyStatus.setStatus("current")
_FsRipMd5AuthTable_Object = MibTable
fsRipMd5AuthTable = _FsRipMd5AuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 15)
)
if mibBuilder.loadTexts:
    fsRipMd5AuthTable.setStatus("current")
_FsRipMd5AuthEntry_Object = MibTableRow
fsRipMd5AuthEntry = _FsRipMd5AuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 15, 1)
)
fsRipMd5AuthEntry.setIndexNames(
    (0, "FUTURESOFT-RIP2-MIB", "fsRipMd5AuthAddress"),
    (0, "FUTURESOFT-RIP2-MIB", "fsRipMd5AuthKeyId"),
)
if mibBuilder.loadTexts:
    fsRipMd5AuthEntry.setStatus("current")
_FsRipMd5AuthAddress_Type = IpAddress
_FsRipMd5AuthAddress_Object = MibTableColumn
fsRipMd5AuthAddress = _FsRipMd5AuthAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 15, 1, 1),
    _FsRipMd5AuthAddress_Type()
)
fsRipMd5AuthAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRipMd5AuthAddress.setStatus("current")


class _FsRipMd5AuthKeyId_Type(Integer32):
    """Custom type fsRipMd5AuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsRipMd5AuthKeyId_Type.__name__ = "Integer32"
_FsRipMd5AuthKeyId_Object = MibTableColumn
fsRipMd5AuthKeyId = _FsRipMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 15, 1, 2),
    _FsRipMd5AuthKeyId_Type()
)
fsRipMd5AuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRipMd5AuthKeyId.setStatus("current")


class _FsRipMd5AuthKey_Type(OctetString):
    """Custom type fsRipMd5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsRipMd5AuthKey_Type.__name__ = "OctetString"
_FsRipMd5AuthKey_Object = MibTableColumn
fsRipMd5AuthKey = _FsRipMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 15, 1, 3),
    _FsRipMd5AuthKey_Type()
)
fsRipMd5AuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipMd5AuthKey.setStatus("current")
_FsRipMd5KeyStartTime_Type = Integer32
_FsRipMd5KeyStartTime_Object = MibTableColumn
fsRipMd5KeyStartTime = _FsRipMd5KeyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 15, 1, 4),
    _FsRipMd5KeyStartTime_Type()
)
fsRipMd5KeyStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipMd5KeyStartTime.setStatus("current")
_FsRipMd5KeyExpiryTime_Type = Integer32
_FsRipMd5KeyExpiryTime_Object = MibTableColumn
fsRipMd5KeyExpiryTime = _FsRipMd5KeyExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 15, 1, 5),
    _FsRipMd5KeyExpiryTime_Type()
)
fsRipMd5KeyExpiryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipMd5KeyExpiryTime.setStatus("current")
_FsRipMd5KeyRowStatus_Type = RowStatus
_FsRipMd5KeyRowStatus_Object = MibTableColumn
fsRipMd5KeyRowStatus = _FsRipMd5KeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 15, 1, 6),
    _FsRipMd5KeyRowStatus_Type()
)
fsRipMd5KeyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipMd5KeyRowStatus.setStatus("current")
_FsRip2NBRUnicastListTable_Object = MibTable
fsRip2NBRUnicastListTable = _FsRip2NBRUnicastListTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 16)
)
if mibBuilder.loadTexts:
    fsRip2NBRUnicastListTable.setStatus("current")
_FsRip2NBRUnicastListEntry_Object = MibTableRow
fsRip2NBRUnicastListEntry = _FsRip2NBRUnicastListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 16, 1)
)
fsRip2NBRUnicastListEntry.setIndexNames(
    (0, "FUTURESOFT-RIP2-MIB", "fsRip2NBRUnicastIpAddr"),
)
if mibBuilder.loadTexts:
    fsRip2NBRUnicastListEntry.setStatus("current")
_FsRip2NBRUnicastIpAddr_Type = IpAddress
_FsRip2NBRUnicastIpAddr_Object = MibTableColumn
fsRip2NBRUnicastIpAddr = _FsRip2NBRUnicastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 16, 1, 1),
    _FsRip2NBRUnicastIpAddr_Type()
)
fsRip2NBRUnicastIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRip2NBRUnicastIpAddr.setStatus("current")
_FsRip2NBRUnicastNBRRowStatus_Type = RowStatus
_FsRip2NBRUnicastNBRRowStatus_Object = MibTableColumn
fsRip2NBRUnicastNBRRowStatus = _FsRip2NBRUnicastNBRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 16, 1, 2),
    _FsRip2NBRUnicastNBRRowStatus_Type()
)
fsRip2NBRUnicastNBRRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2NBRUnicastNBRRowStatus.setStatus("current")
_FsRip2LocalRoutingTable_Object = MibTable
fsRip2LocalRoutingTable = _FsRip2LocalRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 17)
)
if mibBuilder.loadTexts:
    fsRip2LocalRoutingTable.setStatus("current")
_FsRip2LocalRoutingEntry_Object = MibTableRow
fsRip2LocalRoutingEntry = _FsRip2LocalRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 17, 1)
)
fsRip2LocalRoutingEntry.setIndexNames(
    (0, "FUTURESOFT-RIP2-MIB", "fsRip2DestNet"),
    (0, "FUTURESOFT-RIP2-MIB", "fsRip2DestMask"),
    (0, "FUTURESOFT-RIP2-MIB", "fsRip2Tos"),
    (0, "FUTURESOFT-RIP2-MIB", "fsRip2NextHop"),
)
if mibBuilder.loadTexts:
    fsRip2LocalRoutingEntry.setStatus("current")
_FsRip2DestNet_Type = IpAddress
_FsRip2DestNet_Object = MibTableColumn
fsRip2DestNet = _FsRip2DestNet_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 17, 1, 1),
    _FsRip2DestNet_Type()
)
fsRip2DestNet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRip2DestNet.setStatus("current")
_FsRip2DestMask_Type = IpAddress
_FsRip2DestMask_Object = MibTableColumn
fsRip2DestMask = _FsRip2DestMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 17, 1, 2),
    _FsRip2DestMask_Type()
)
fsRip2DestMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRip2DestMask.setStatus("current")


class _FsRip2Tos_Type(Integer32):
    """Custom type fsRip2Tos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsRip2Tos_Type.__name__ = "Integer32"
_FsRip2Tos_Object = MibTableColumn
fsRip2Tos = _FsRip2Tos_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 17, 1, 3),
    _FsRip2Tos_Type()
)
fsRip2Tos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRip2Tos.setStatus("current")
_FsRip2NextHop_Type = IpAddress
_FsRip2NextHop_Object = MibTableColumn
fsRip2NextHop = _FsRip2NextHop_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 17, 1, 4),
    _FsRip2NextHop_Type()
)
fsRip2NextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRip2NextHop.setStatus("current")
_FsRip2RtIfIndex_Type = Integer32
_FsRip2RtIfIndex_Object = MibTableColumn
fsRip2RtIfIndex = _FsRip2RtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 17, 1, 5),
    _FsRip2RtIfIndex_Type()
)
fsRip2RtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRip2RtIfIndex.setStatus("current")
_FsRip2RtType_Type = Integer32
_FsRip2RtType_Object = MibTableColumn
fsRip2RtType = _FsRip2RtType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 17, 1, 6),
    _FsRip2RtType_Type()
)
fsRip2RtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRip2RtType.setStatus("current")
_FsRip2Proto_Type = Integer32
_FsRip2Proto_Object = MibTableColumn
fsRip2Proto = _FsRip2Proto_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 17, 1, 7),
    _FsRip2Proto_Type()
)
fsRip2Proto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRip2Proto.setStatus("current")
_FsRip2ChgTime_Type = Integer32
_FsRip2ChgTime_Object = MibTableColumn
fsRip2ChgTime = _FsRip2ChgTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 17, 1, 8),
    _FsRip2ChgTime_Type()
)
fsRip2ChgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRip2ChgTime.setStatus("current")
_FsRip2Metric_Type = Integer32
_FsRip2Metric_Object = MibTableColumn
fsRip2Metric = _FsRip2Metric_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 17, 1, 9),
    _FsRip2Metric_Type()
)
fsRip2Metric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRip2Metric.setStatus("current")
_FsRip2RowStatus_Type = Integer32
_FsRip2RowStatus_Object = MibTableColumn
fsRip2RowStatus = _FsRip2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 17, 1, 10),
    _FsRip2RowStatus_Type()
)
fsRip2RowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRip2RowStatus.setStatus("current")
_FsRip2Gateway_Type = IpAddress
_FsRip2Gateway_Object = MibTableColumn
fsRip2Gateway = _FsRip2Gateway_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 17, 1, 11),
    _FsRip2Gateway_Type()
)
fsRip2Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRip2Gateway.setStatus("current")
_FsRipAggTable_Object = MibTable
fsRipAggTable = _FsRipAggTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 18)
)
if mibBuilder.loadTexts:
    fsRipAggTable.setStatus("current")
_FsRipAggEntry_Object = MibTableRow
fsRipAggEntry = _FsRipAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 18, 1)
)
fsRipAggEntry.setIndexNames(
    (0, "FUTURESOFT-RIP2-MIB", "fsRipIfIndex"),
    (0, "FUTURESOFT-RIP2-MIB", "fsRipAggAddress"),
    (0, "FUTURESOFT-RIP2-MIB", "fsRipAggAddressMask"),
)
if mibBuilder.loadTexts:
    fsRipAggEntry.setStatus("current")


class _FsRipIfIndex_Type(Integer32):
    """Custom type fsRipIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsRipIfIndex_Type.__name__ = "Integer32"
_FsRipIfIndex_Object = MibTableColumn
fsRipIfIndex = _FsRipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 18, 1, 1),
    _FsRipIfIndex_Type()
)
fsRipIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRipIfIndex.setStatus("current")
_FsRipAggAddress_Type = IpAddress
_FsRipAggAddress_Object = MibTableColumn
fsRipAggAddress = _FsRipAggAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 18, 1, 2),
    _FsRipAggAddress_Type()
)
fsRipAggAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRipAggAddress.setStatus("current")
_FsRipAggAddressMask_Type = IpAddress
_FsRipAggAddressMask_Object = MibTableColumn
fsRipAggAddressMask = _FsRipAggAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 18, 1, 3),
    _FsRipAggAddressMask_Type()
)
fsRipAggAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRipAggAddressMask.setStatus("current")
_FsRipAggStatus_Type = RowStatus
_FsRipAggStatus_Object = MibTableColumn
fsRipAggStatus = _FsRipAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 18, 1, 4),
    _FsRipAggStatus_Type()
)
fsRipAggStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipAggStatus.setStatus("current")


class _FsRipAdminStatus_Type(Integer32):
    """Custom type fsRipAdminStatus based on Integer32"""
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


_FsRipAdminStatus_Type.__name__ = "Integer32"
_FsRipAdminStatus_Object = MibScalar
fsRipAdminStatus = _FsRipAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 19),
    _FsRipAdminStatus_Type()
)
fsRipAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipAdminStatus.setStatus("current")
_FsRipCryptoAuthTable_Object = MibTable
fsRipCryptoAuthTable = _FsRipCryptoAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 20)
)
if mibBuilder.loadTexts:
    fsRipCryptoAuthTable.setStatus("current")
_FsRipCryptoAuthEntry_Object = MibTableRow
fsRipCryptoAuthEntry = _FsRipCryptoAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 20, 1)
)
fsRipCryptoAuthEntry.setIndexNames(
    (0, "FUTURESOFT-RIP2-MIB", "fsRipCryptoAuthIfIndex"),
    (0, "FUTURESOFT-RIP2-MIB", "fsRipCryptoAuthAddress"),
    (0, "FUTURESOFT-RIP2-MIB", "fsRipCryptoAuthKeyId"),
)
if mibBuilder.loadTexts:
    fsRipCryptoAuthEntry.setStatus("current")


class _FsRipCryptoAuthIfIndex_Type(InterfaceIndex):
    """Custom type fsRipCryptoAuthIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsRipCryptoAuthIfIndex_Type.__name__ = "InterfaceIndex"
_FsRipCryptoAuthIfIndex_Object = MibTableColumn
fsRipCryptoAuthIfIndex = _FsRipCryptoAuthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 20, 1, 1),
    _FsRipCryptoAuthIfIndex_Type()
)
fsRipCryptoAuthIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRipCryptoAuthIfIndex.setStatus("current")
_FsRipCryptoAuthAddress_Type = IpAddress
_FsRipCryptoAuthAddress_Object = MibTableColumn
fsRipCryptoAuthAddress = _FsRipCryptoAuthAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 20, 1, 2),
    _FsRipCryptoAuthAddress_Type()
)
fsRipCryptoAuthAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRipCryptoAuthAddress.setStatus("current")


class _FsRipCryptoAuthKeyId_Type(Integer32):
    """Custom type fsRipCryptoAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsRipCryptoAuthKeyId_Type.__name__ = "Integer32"
_FsRipCryptoAuthKeyId_Object = MibTableColumn
fsRipCryptoAuthKeyId = _FsRipCryptoAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 20, 1, 3),
    _FsRipCryptoAuthKeyId_Type()
)
fsRipCryptoAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRipCryptoAuthKeyId.setStatus("current")


class _FsRipCryptoAuthKey_Type(OctetString):
    """Custom type fsRipCryptoAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsRipCryptoAuthKey_Type.__name__ = "OctetString"
_FsRipCryptoAuthKey_Object = MibTableColumn
fsRipCryptoAuthKey = _FsRipCryptoAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 20, 1, 4),
    _FsRipCryptoAuthKey_Type()
)
fsRipCryptoAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipCryptoAuthKey.setStatus("current")
_FsRipCryptoKeyStartAccept_Type = DateAndTime
_FsRipCryptoKeyStartAccept_Object = MibTableColumn
fsRipCryptoKeyStartAccept = _FsRipCryptoKeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 20, 1, 5),
    _FsRipCryptoKeyStartAccept_Type()
)
fsRipCryptoKeyStartAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipCryptoKeyStartAccept.setStatus("current")
_FsRipCryptoKeyStartGenerate_Type = DateAndTime
_FsRipCryptoKeyStartGenerate_Object = MibTableColumn
fsRipCryptoKeyStartGenerate = _FsRipCryptoKeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 20, 1, 6),
    _FsRipCryptoKeyStartGenerate_Type()
)
fsRipCryptoKeyStartGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipCryptoKeyStartGenerate.setStatus("current")
_FsRipCryptoKeyStopGenerate_Type = DateAndTime
_FsRipCryptoKeyStopGenerate_Object = MibTableColumn
fsRipCryptoKeyStopGenerate = _FsRipCryptoKeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 20, 1, 7),
    _FsRipCryptoKeyStopGenerate_Type()
)
fsRipCryptoKeyStopGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipCryptoKeyStopGenerate.setStatus("current")
_FsRipCryptoKeyStopAccept_Type = DateAndTime
_FsRipCryptoKeyStopAccept_Object = MibTableColumn
fsRipCryptoKeyStopAccept = _FsRipCryptoKeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 20, 1, 8),
    _FsRipCryptoKeyStopAccept_Type()
)
fsRipCryptoKeyStopAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipCryptoKeyStopAccept.setStatus("current")


class _FsRipCryptoKeyStatus_Type(Integer32):
    """Custom type fsRipCryptoKeyStatus based on Integer32"""
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


_FsRipCryptoKeyStatus_Type.__name__ = "Integer32"
_FsRipCryptoKeyStatus_Object = MibTableColumn
fsRipCryptoKeyStatus = _FsRipCryptoKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 20, 1, 9),
    _FsRipCryptoKeyStatus_Type()
)
fsRipCryptoKeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipCryptoKeyStatus.setStatus("current")
_FsRip2PeerTable_Object = MibTable
fsRip2PeerTable = _FsRip2PeerTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 21)
)
if mibBuilder.loadTexts:
    fsRip2PeerTable.setStatus("current")
_FsRip2PeerEntry_Object = MibTableRow
fsRip2PeerEntry = _FsRip2PeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 21, 1)
)
if mibBuilder.loadTexts:
    fsRip2PeerEntry.setStatus("current")


class _FsRip2PeerInUseKey_Type(Integer32):
    """Custom type fsRip2PeerInUseKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsRip2PeerInUseKey_Type.__name__ = "Integer32"
_FsRip2PeerInUseKey_Object = MibTableColumn
fsRip2PeerInUseKey = _FsRip2PeerInUseKey_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 21, 1, 1),
    _FsRip2PeerInUseKey_Type()
)
fsRip2PeerInUseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRip2PeerInUseKey.setStatus("current")


class _FsRip2LastAuthKeyLifetimeStatus_Type(TruthValue):
    """Custom type fsRip2LastAuthKeyLifetimeStatus based on TruthValue"""
    defaultValue = 1


_FsRip2LastAuthKeyLifetimeStatus_Type.__name__ = "TruthValue"
_FsRip2LastAuthKeyLifetimeStatus_Object = MibScalar
fsRip2LastAuthKeyLifetimeStatus = _FsRip2LastAuthKeyLifetimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 22),
    _FsRip2LastAuthKeyLifetimeStatus_Type()
)
fsRip2LastAuthKeyLifetimeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2LastAuthKeyLifetimeStatus.setStatus("current")
_FsRip2IfStatTable_Object = MibTable
fsRip2IfStatTable = _FsRip2IfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 23)
)
if mibBuilder.loadTexts:
    fsRip2IfStatTable.setStatus("current")
_FsRip2IfStatEntry_Object = MibTableRow
fsRip2IfStatEntry = _FsRip2IfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 23, 1)
)
if mibBuilder.loadTexts:
    fsRip2IfStatEntry.setStatus("current")
_FsRip2IfStatRcvBadAuthPackets_Type = Counter32
_FsRip2IfStatRcvBadAuthPackets_Object = MibTableColumn
fsRip2IfStatRcvBadAuthPackets = _FsRip2IfStatRcvBadAuthPackets_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 23, 1, 1),
    _FsRip2IfStatRcvBadAuthPackets_Type()
)
fsRip2IfStatRcvBadAuthPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRip2IfStatRcvBadAuthPackets.setStatus("current")
_FsRipRtCount_Type = Integer32
_FsRipRtCount_Object = MibScalar
fsRipRtCount = _FsRipRtCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 1, 24),
    _FsRipRtCount_Type()
)
fsRipRtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRipRtCount.setStatus("current")
_FsRipRRDGeneralGroup_ObjectIdentity = ObjectIdentity
fsRipRRDGeneralGroup = _FsRipRRDGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 75, 2)
)


class _FsRipRRDGlobalStatus_Type(Integer32):
    """Custom type fsRipRRDGlobalStatus based on Integer32"""
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


_FsRipRRDGlobalStatus_Type.__name__ = "Integer32"
_FsRipRRDGlobalStatus_Object = MibScalar
fsRipRRDGlobalStatus = _FsRipRRDGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 2, 1),
    _FsRipRRDGlobalStatus_Type()
)
fsRipRRDGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipRRDGlobalStatus.setStatus("current")


class _FsRipRRDSrcProtoMaskEnable_Type(Integer32):
    """Custom type fsRipRRDSrcProtoMaskEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsRipRRDSrcProtoMaskEnable_Type.__name__ = "Integer32"
_FsRipRRDSrcProtoMaskEnable_Object = MibScalar
fsRipRRDSrcProtoMaskEnable = _FsRipRRDSrcProtoMaskEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 2, 2),
    _FsRipRRDSrcProtoMaskEnable_Type()
)
fsRipRRDSrcProtoMaskEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipRRDSrcProtoMaskEnable.setStatus("current")


class _FsRipRRDSrcProtoMaskDisable_Type(Integer32):
    """Custom type fsRipRRDSrcProtoMaskDisable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsRipRRDSrcProtoMaskDisable_Type.__name__ = "Integer32"
_FsRipRRDSrcProtoMaskDisable_Object = MibScalar
fsRipRRDSrcProtoMaskDisable = _FsRipRRDSrcProtoMaskDisable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 2, 3),
    _FsRipRRDSrcProtoMaskDisable_Type()
)
fsRipRRDSrcProtoMaskDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipRRDSrcProtoMaskDisable.setStatus("current")


class _FsRipRRDRouteTagType_Type(Integer32):
    """Custom type fsRipRRDRouteTagType based on Integer32"""
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


_FsRipRRDRouteTagType_Type.__name__ = "Integer32"
_FsRipRRDRouteTagType_Object = MibScalar
fsRipRRDRouteTagType = _FsRipRRDRouteTagType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 2, 4),
    _FsRipRRDRouteTagType_Type()
)
fsRipRRDRouteTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipRRDRouteTagType.setStatus("current")


class _FsRipRRDRouteTag_Type(Integer32):
    """Custom type fsRipRRDRouteTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsRipRRDRouteTag_Type.__name__ = "Integer32"
_FsRipRRDRouteTag_Object = MibScalar
fsRipRRDRouteTag = _FsRipRRDRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 2, 5),
    _FsRipRRDRouteTag_Type()
)
fsRipRRDRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipRRDRouteTag.setStatus("current")


class _FsRipRRDRouteDefMetric_Type(Integer32):
    """Custom type fsRipRRDRouteDefMetric based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FsRipRRDRouteDefMetric_Type.__name__ = "Integer32"
_FsRipRRDRouteDefMetric_Object = MibScalar
fsRipRRDRouteDefMetric = _FsRipRRDRouteDefMetric_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 2, 6),
    _FsRipRRDRouteDefMetric_Type()
)
fsRipRRDRouteDefMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipRRDRouteDefMetric.setStatus("current")


class _FsRipRRDRouteMapEnable_Type(DisplayString):
    """Custom type fsRipRRDRouteMapEnable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_FsRipRRDRouteMapEnable_Type.__name__ = "DisplayString"
_FsRipRRDRouteMapEnable_Object = MibScalar
fsRipRRDRouteMapEnable = _FsRipRRDRouteMapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 2, 7),
    _FsRipRRDRouteMapEnable_Type()
)
fsRipRRDRouteMapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipRRDRouteMapEnable.setStatus("current")
_FsripDistInOutRouteMap_ObjectIdentity = ObjectIdentity
fsripDistInOutRouteMap = _FsripDistInOutRouteMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 75, 3)
)
_FsRipDistInOutRouteMapTable_Object = MibTable
fsRipDistInOutRouteMapTable = _FsRipDistInOutRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 3, 1)
)
if mibBuilder.loadTexts:
    fsRipDistInOutRouteMapTable.setStatus("current")
_FsRipDistInOutRouteMapEntry_Object = MibTableRow
fsRipDistInOutRouteMapEntry = _FsRipDistInOutRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 3, 1, 1)
)
fsRipDistInOutRouteMapEntry.setIndexNames(
    (0, "FUTURESOFT-RIP2-MIB", "fsRipDistInOutRouteMapName"),
    (0, "FUTURESOFT-RIP2-MIB", "fsRipDistInOutRouteMapType"),
)
if mibBuilder.loadTexts:
    fsRipDistInOutRouteMapEntry.setStatus("current")


class _FsRipDistInOutRouteMapName_Type(DisplayString):
    """Custom type fsRipDistInOutRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsRipDistInOutRouteMapName_Type.__name__ = "DisplayString"
_FsRipDistInOutRouteMapName_Object = MibTableColumn
fsRipDistInOutRouteMapName = _FsRipDistInOutRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 3, 1, 1, 1),
    _FsRipDistInOutRouteMapName_Type()
)
fsRipDistInOutRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRipDistInOutRouteMapName.setStatus("current")


class _FsRipDistInOutRouteMapType_Type(Integer32):
    """Custom type fsRipDistInOutRouteMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsRipDistInOutRouteMapType_Type.__name__ = "Integer32"
_FsRipDistInOutRouteMapType_Object = MibTableColumn
fsRipDistInOutRouteMapType = _FsRipDistInOutRouteMapType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 3, 1, 1, 3),
    _FsRipDistInOutRouteMapType_Type()
)
fsRipDistInOutRouteMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRipDistInOutRouteMapType.setStatus("current")


class _FsRipDistInOutRouteMapValue_Type(Integer32):
    """Custom type fsRipDistInOutRouteMapValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsRipDistInOutRouteMapValue_Type.__name__ = "Integer32"
_FsRipDistInOutRouteMapValue_Object = MibTableColumn
fsRipDistInOutRouteMapValue = _FsRipDistInOutRouteMapValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 3, 1, 1, 4),
    _FsRipDistInOutRouteMapValue_Type()
)
fsRipDistInOutRouteMapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipDistInOutRouteMapValue.setStatus("current")
_FsRipDistInOutRouteMapRowStatus_Type = RowStatus
_FsRipDistInOutRouteMapRowStatus_Object = MibTableColumn
fsRipDistInOutRouteMapRowStatus = _FsRipDistInOutRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 3, 1, 1, 5),
    _FsRipDistInOutRouteMapRowStatus_Type()
)
fsRipDistInOutRouteMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipDistInOutRouteMapRowStatus.setStatus("current")
_FsripPreferenceGroup_ObjectIdentity = ObjectIdentity
fsripPreferenceGroup = _FsripPreferenceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 75, 4)
)


class _FsRipPreferenceValue_Type(Integer32):
    """Custom type fsRipPreferenceValue based on Integer32"""
    defaultValue = 121

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsRipPreferenceValue_Type.__name__ = "Integer32"
_FsRipPreferenceValue_Object = MibScalar
fsRipPreferenceValue = _FsRipPreferenceValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 4, 1),
    _FsRipPreferenceValue_Type()
)
fsRipPreferenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRipPreferenceValue.setStatus("current")
_FsRip2TrapsControl_ObjectIdentity = ObjectIdentity
fsRip2TrapsControl = _FsRip2TrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 75, 5)
)


class _FsRipAuthIfIndex_Type(InterfaceIndex):
    """Custom type fsRipAuthIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsRipAuthIfIndex_Type.__name__ = "InterfaceIndex"
_FsRipAuthIfIndex_Object = MibScalar
fsRipAuthIfIndex = _FsRipAuthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 5, 1),
    _FsRipAuthIfIndex_Type()
)
fsRipAuthIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRipAuthIfIndex.setStatus("current")


class _FsRipAuthKeyId_Type(Integer32):
    """Custom type fsRipAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsRipAuthKeyId_Type.__name__ = "Integer32"
_FsRipAuthKeyId_Object = MibScalar
fsRipAuthKeyId = _FsRipAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 5, 2),
    _FsRipAuthKeyId_Type()
)
fsRipAuthKeyId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRipAuthKeyId.setStatus("current")
_FsRipPeerAddress_Type = IpAddress
_FsRipPeerAddress_Object = MibScalar
fsRipPeerAddress = _FsRipPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 5, 3),
    _FsRipPeerAddress_Type()
)
fsRipPeerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsRipPeerAddress.setStatus("current")
_FsRip2Notification_ObjectIdentity = ObjectIdentity
fsRip2Notification = _FsRip2Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 75, 6)
)
_FsRip2Traps_ObjectIdentity = ObjectIdentity
fsRip2Traps = _FsRip2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 75, 6, 0)
)
_FsRip2Test_ObjectIdentity = ObjectIdentity
fsRip2Test = _FsRip2Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 75, 7)
)


class _FsRip2TestBulkUpd_Type(Integer32):
    """Custom type fsRip2TestBulkUpd based on Integer32"""
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


_FsRip2TestBulkUpd_Type.__name__ = "Integer32"
_FsRip2TestBulkUpd_Object = MibScalar
fsRip2TestBulkUpd = _FsRip2TestBulkUpd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 7, 1),
    _FsRip2TestBulkUpd_Type()
)
fsRip2TestBulkUpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2TestBulkUpd.setStatus("current")


class _FsRip2TestDynamicUpd_Type(Integer32):
    """Custom type fsRip2TestDynamicUpd based on Integer32"""
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


_FsRip2TestDynamicUpd_Type.__name__ = "Integer32"
_FsRip2TestDynamicUpd_Object = MibScalar
fsRip2TestDynamicUpd = _FsRip2TestDynamicUpd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 75, 7, 2),
    _FsRip2TestDynamicUpd_Type()
)
fsRip2TestDynamicUpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRip2TestDynamicUpd.setStatus("current")
rip2PeerEntry.registerAugmentions(
    ("FUTURESOFT-RIP2-MIB",
     "fsRip2PeerEntry")
)
fsRip2PeerEntry.setIndexNames(*rip2PeerEntry.getIndexNames())
rip2IfStatEntry.registerAugmentions(
    ("FUTURESOFT-RIP2-MIB",
     "fsRip2IfStatEntry")
)
fsRip2IfStatEntry.setIndexNames(*rip2IfStatEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fsRip2AuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 75, 6, 0, 1)
)
fsRip2AuthenticationFailure.setObjects(
      *(("FUTURESOFT-RIP2-MIB", "fsRipPeerAddress"),
        ("FUTURESOFT-RIP2-MIB", "fsRipAuthIfIndex"),
        ("FUTURESOFT-RIP2-MIB", "fsRipAuthKeyId"))
)
if mibBuilder.loadTexts:
    fsRip2AuthenticationFailure.setStatus(
        "current"
    )

fsRip2AuthLastKey = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 75, 6, 0, 2)
)
fsRip2AuthLastKey.setObjects(
      *(("FUTURESOFT-RIP2-MIB", "fsRipAuthIfIndex"),
        ("FUTURESOFT-RIP2-MIB", "fsRipAuthKeyId"))
)
if mibBuilder.loadTexts:
    fsRip2AuthLastKey.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FUTURESOFT-RIP2-MIB",
    **{"fsrip": fsrip,
       "rip2GeneralGroup": rip2GeneralGroup,
       "fsRip2Security": fsRip2Security,
       "fsRip2Peers": fsRip2Peers,
       "fsRip2TrustNBRListEnable": fsRip2TrustNBRListEnable,
       "fsRip2NumberOfDroppedPkts": fsRip2NumberOfDroppedPkts,
       "fsRip2SpacingEnable": fsRip2SpacingEnable,
       "fsRip2AutoSummaryStatus": fsRip2AutoSummaryStatus,
       "fsRip2RetransTimeoutInt": fsRip2RetransTimeoutInt,
       "fsRip2MaxRetransmissions": fsRip2MaxRetransmissions,
       "fsRip2OverSubscriptionTimeout": fsRip2OverSubscriptionTimeout,
       "fsRip2Propagate": fsRip2Propagate,
       "fsRip2MaxRoutes": fsRip2MaxRoutes,
       "fsRipTrcFlag": fsRipTrcFlag,
       "fsRip2NBRTrustListTable": fsRip2NBRTrustListTable,
       "fsRip2NBRTrustListEntry": fsRip2NBRTrustListEntry,
       "fsRip2TrustNBRIpAddr": fsRip2TrustNBRIpAddr,
       "fsRip2TrustNBRRowStatus": fsRip2TrustNBRRowStatus,
       "fsRip2IfConfTable": fsRip2IfConfTable,
       "fsRip2IfConfEntry": fsRip2IfConfEntry,
       "fsRip2IfConfAddress": fsRip2IfConfAddress,
       "fsRip2IfAdminStat": fsRip2IfAdminStat,
       "fsRip2IfConfOperState": fsRip2IfConfOperState,
       "fsRip2IfConfUpdateTmr": fsRip2IfConfUpdateTmr,
       "fsRip2IfConfGarbgCollectTmr": fsRip2IfConfGarbgCollectTmr,
       "fsRip2IfConfRouteAgeTmr": fsRip2IfConfRouteAgeTmr,
       "fsRip2IfSplitHorizonStatus": fsRip2IfSplitHorizonStatus,
       "fsRip2IfConfDefRtInstall": fsRip2IfConfDefRtInstall,
       "fsRip2IfConfSpacingTmr": fsRip2IfConfSpacingTmr,
       "fsRip2IfConfAuthType": fsRip2IfConfAuthType,
       "fsRip2IfConfInUseKey": fsRip2IfConfInUseKey,
       "fsRip2IfConfAuthLastKeyStatus": fsRip2IfConfAuthLastKeyStatus,
       "fsRipMd5AuthTable": fsRipMd5AuthTable,
       "fsRipMd5AuthEntry": fsRipMd5AuthEntry,
       "fsRipMd5AuthAddress": fsRipMd5AuthAddress,
       "fsRipMd5AuthKeyId": fsRipMd5AuthKeyId,
       "fsRipMd5AuthKey": fsRipMd5AuthKey,
       "fsRipMd5KeyStartTime": fsRipMd5KeyStartTime,
       "fsRipMd5KeyExpiryTime": fsRipMd5KeyExpiryTime,
       "fsRipMd5KeyRowStatus": fsRipMd5KeyRowStatus,
       "fsRip2NBRUnicastListTable": fsRip2NBRUnicastListTable,
       "fsRip2NBRUnicastListEntry": fsRip2NBRUnicastListEntry,
       "fsRip2NBRUnicastIpAddr": fsRip2NBRUnicastIpAddr,
       "fsRip2NBRUnicastNBRRowStatus": fsRip2NBRUnicastNBRRowStatus,
       "fsRip2LocalRoutingTable": fsRip2LocalRoutingTable,
       "fsRip2LocalRoutingEntry": fsRip2LocalRoutingEntry,
       "fsRip2DestNet": fsRip2DestNet,
       "fsRip2DestMask": fsRip2DestMask,
       "fsRip2Tos": fsRip2Tos,
       "fsRip2NextHop": fsRip2NextHop,
       "fsRip2RtIfIndex": fsRip2RtIfIndex,
       "fsRip2RtType": fsRip2RtType,
       "fsRip2Proto": fsRip2Proto,
       "fsRip2ChgTime": fsRip2ChgTime,
       "fsRip2Metric": fsRip2Metric,
       "fsRip2RowStatus": fsRip2RowStatus,
       "fsRip2Gateway": fsRip2Gateway,
       "fsRipAggTable": fsRipAggTable,
       "fsRipAggEntry": fsRipAggEntry,
       "fsRipIfIndex": fsRipIfIndex,
       "fsRipAggAddress": fsRipAggAddress,
       "fsRipAggAddressMask": fsRipAggAddressMask,
       "fsRipAggStatus": fsRipAggStatus,
       "fsRipAdminStatus": fsRipAdminStatus,
       "fsRipCryptoAuthTable": fsRipCryptoAuthTable,
       "fsRipCryptoAuthEntry": fsRipCryptoAuthEntry,
       "fsRipCryptoAuthIfIndex": fsRipCryptoAuthIfIndex,
       "fsRipCryptoAuthAddress": fsRipCryptoAuthAddress,
       "fsRipCryptoAuthKeyId": fsRipCryptoAuthKeyId,
       "fsRipCryptoAuthKey": fsRipCryptoAuthKey,
       "fsRipCryptoKeyStartAccept": fsRipCryptoKeyStartAccept,
       "fsRipCryptoKeyStartGenerate": fsRipCryptoKeyStartGenerate,
       "fsRipCryptoKeyStopGenerate": fsRipCryptoKeyStopGenerate,
       "fsRipCryptoKeyStopAccept": fsRipCryptoKeyStopAccept,
       "fsRipCryptoKeyStatus": fsRipCryptoKeyStatus,
       "fsRip2PeerTable": fsRip2PeerTable,
       "fsRip2PeerEntry": fsRip2PeerEntry,
       "fsRip2PeerInUseKey": fsRip2PeerInUseKey,
       "fsRip2LastAuthKeyLifetimeStatus": fsRip2LastAuthKeyLifetimeStatus,
       "fsRip2IfStatTable": fsRip2IfStatTable,
       "fsRip2IfStatEntry": fsRip2IfStatEntry,
       "fsRip2IfStatRcvBadAuthPackets": fsRip2IfStatRcvBadAuthPackets,
       "fsRipRtCount": fsRipRtCount,
       "fsRipRRDGeneralGroup": fsRipRRDGeneralGroup,
       "fsRipRRDGlobalStatus": fsRipRRDGlobalStatus,
       "fsRipRRDSrcProtoMaskEnable": fsRipRRDSrcProtoMaskEnable,
       "fsRipRRDSrcProtoMaskDisable": fsRipRRDSrcProtoMaskDisable,
       "fsRipRRDRouteTagType": fsRipRRDRouteTagType,
       "fsRipRRDRouteTag": fsRipRRDRouteTag,
       "fsRipRRDRouteDefMetric": fsRipRRDRouteDefMetric,
       "fsRipRRDRouteMapEnable": fsRipRRDRouteMapEnable,
       "fsripDistInOutRouteMap": fsripDistInOutRouteMap,
       "fsRipDistInOutRouteMapTable": fsRipDistInOutRouteMapTable,
       "fsRipDistInOutRouteMapEntry": fsRipDistInOutRouteMapEntry,
       "fsRipDistInOutRouteMapName": fsRipDistInOutRouteMapName,
       "fsRipDistInOutRouteMapType": fsRipDistInOutRouteMapType,
       "fsRipDistInOutRouteMapValue": fsRipDistInOutRouteMapValue,
       "fsRipDistInOutRouteMapRowStatus": fsRipDistInOutRouteMapRowStatus,
       "fsripPreferenceGroup": fsripPreferenceGroup,
       "fsRipPreferenceValue": fsRipPreferenceValue,
       "fsRip2TrapsControl": fsRip2TrapsControl,
       "fsRipAuthIfIndex": fsRipAuthIfIndex,
       "fsRipAuthKeyId": fsRipAuthKeyId,
       "fsRipPeerAddress": fsRipPeerAddress,
       "fsRip2Notification": fsRip2Notification,
       "fsRip2Traps": fsRip2Traps,
       "fsRip2AuthenticationFailure": fsRip2AuthenticationFailure,
       "fsRip2AuthLastKey": fsRip2AuthLastKey,
       "fsRip2Test": fsRip2Test,
       "fsRip2TestBulkUpd": fsRip2TestBulkUpd,
       "fsRip2TestDynamicUpd": fsRip2TestDynamicUpd}
)
