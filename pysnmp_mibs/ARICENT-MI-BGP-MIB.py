# SNMP MIB module (ARICENT-MI-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-MI-BGP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:50 2025
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

(BgpSafi,
 InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "ARICENT-BGP-MIB",
    "BgpSafi",
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

fsMIBgp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIBgp4GlobalTraceDebug_Type = Integer32
_FsMIBgp4GlobalTraceDebug_Object = MibScalar
fsMIBgp4GlobalTraceDebug = _FsMIBgp4GlobalTraceDebug_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 1),
    _FsMIBgp4GlobalTraceDebug_Type()
)
fsMIBgp4GlobalTraceDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4GlobalTraceDebug.setStatus("current")


class _FsMIBgp4LocalAs_Type(Unsigned32):
    """Custom type fsMIBgp4LocalAs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIBgp4LocalAs_Type.__name__ = "Unsigned32"
_FsMIBgp4LocalAs_Object = MibScalar
fsMIBgp4LocalAs = _FsMIBgp4LocalAs_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 2),
    _FsMIBgp4LocalAs_Type()
)
fsMIBgp4LocalAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4LocalAs.setStatus("current")


class _FsMIBgp4MaxPeerEntry_Type(Integer32):
    """Custom type fsMIBgp4MaxPeerEntry based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_FsMIBgp4MaxPeerEntry_Type.__name__ = "Integer32"
_FsMIBgp4MaxPeerEntry_Object = MibScalar
fsMIBgp4MaxPeerEntry = _FsMIBgp4MaxPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 3),
    _FsMIBgp4MaxPeerEntry_Type()
)
fsMIBgp4MaxPeerEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4MaxPeerEntry.setStatus("current")


class _FsMIBgp4MaxNoofRoutes_Type(Integer32):
    """Custom type fsMIBgp4MaxNoofRoutes based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_FsMIBgp4MaxNoofRoutes_Type.__name__ = "Integer32"
_FsMIBgp4MaxNoofRoutes_Object = MibScalar
fsMIBgp4MaxNoofRoutes = _FsMIBgp4MaxNoofRoutes_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 4),
    _FsMIBgp4MaxNoofRoutes_Type()
)
fsMIBgp4MaxNoofRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4MaxNoofRoutes.setStatus("current")


class _FsMIBgp4GRAdminStatus_Type(Integer32):
    """Custom type fsMIBgp4GRAdminStatus based on Integer32"""
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


_FsMIBgp4GRAdminStatus_Type.__name__ = "Integer32"
_FsMIBgp4GRAdminStatus_Object = MibScalar
fsMIBgp4GRAdminStatus = _FsMIBgp4GRAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 5),
    _FsMIBgp4GRAdminStatus_Type()
)
fsMIBgp4GRAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4GRAdminStatus.setStatus("current")


class _FsMIBgp4GRRestartTimeInterval_Type(Integer32):
    """Custom type fsMIBgp4GRRestartTimeInterval based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FsMIBgp4GRRestartTimeInterval_Type.__name__ = "Integer32"
_FsMIBgp4GRRestartTimeInterval_Object = MibScalar
fsMIBgp4GRRestartTimeInterval = _FsMIBgp4GRRestartTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 6),
    _FsMIBgp4GRRestartTimeInterval_Type()
)
fsMIBgp4GRRestartTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4GRRestartTimeInterval.setStatus("current")


class _FsMIBgp4RestartExitReason_Type(Integer32):
    """Custom type fsMIBgp4RestartExitReason based on Integer32"""
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
          ("inProgress", 2),
          ("completed", 3),
          ("failure", 4))
    )


_FsMIBgp4RestartExitReason_Type.__name__ = "Integer32"
_FsMIBgp4RestartExitReason_Object = MibScalar
fsMIBgp4RestartExitReason = _FsMIBgp4RestartExitReason_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 7),
    _FsMIBgp4RestartExitReason_Type()
)
fsMIBgp4RestartExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4RestartExitReason.setStatus("current")


class _FsMIBgp4GRSelectionDeferralTimeInterval_Type(Integer32):
    """Custom type fsMIBgp4GRSelectionDeferralTimeInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1800),
    )


_FsMIBgp4GRSelectionDeferralTimeInterval_Type.__name__ = "Integer32"
_FsMIBgp4GRSelectionDeferralTimeInterval_Object = MibScalar
fsMIBgp4GRSelectionDeferralTimeInterval = _FsMIBgp4GRSelectionDeferralTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 8),
    _FsMIBgp4GRSelectionDeferralTimeInterval_Type()
)
fsMIBgp4GRSelectionDeferralTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4GRSelectionDeferralTimeInterval.setStatus("current")


class _FsMIBgp4GRStaleTimeInterval_Type(Integer32):
    """Custom type fsMIBgp4GRStaleTimeInterval based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 3600),
    )


_FsMIBgp4GRStaleTimeInterval_Type.__name__ = "Integer32"
_FsMIBgp4GRStaleTimeInterval_Object = MibScalar
fsMIBgp4GRStaleTimeInterval = _FsMIBgp4GRStaleTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 9),
    _FsMIBgp4GRStaleTimeInterval_Type()
)
fsMIBgp4GRStaleTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4GRStaleTimeInterval.setStatus("current")


class _FsMIBgp4GRMode_Type(Integer32):
    """Custom type fsMIBgp4GRMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("restarting", 1),
          ("receiving", 2),
          ("none", 3))
    )


_FsMIBgp4GRMode_Type.__name__ = "Integer32"
_FsMIBgp4GRMode_Object = MibScalar
fsMIBgp4GRMode = _FsMIBgp4GRMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 10),
    _FsMIBgp4GRMode_Type()
)
fsMIBgp4GRMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4GRMode.setStatus("current")


class _FsMIBgp4RestartSupport_Type(Integer32):
    """Custom type fsMIBgp4RestartSupport based on Integer32"""
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
        *(("none", 1),
          ("plannedOnly", 2),
          ("plannedAndUnplanned", 3))
    )


_FsMIBgp4RestartSupport_Type.__name__ = "Integer32"
_FsMIBgp4RestartSupport_Object = MibScalar
fsMIBgp4RestartSupport = _FsMIBgp4RestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 11),
    _FsMIBgp4RestartSupport_Type()
)
fsMIBgp4RestartSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RestartSupport.setStatus("current")


class _FsMIBgp4RestartStatus_Type(Integer32):
    """Custom type fsMIBgp4RestartStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("plannedRestart", 2),
          ("unplannedRestart", 3))
    )


_FsMIBgp4RestartStatus_Type.__name__ = "Integer32"
_FsMIBgp4RestartStatus_Object = MibScalar
fsMIBgp4RestartStatus = _FsMIBgp4RestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 12),
    _FsMIBgp4RestartStatus_Type()
)
fsMIBgp4RestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4RestartStatus.setStatus("current")


class _FsMIBgp4ForwardingPreservation_Type(Integer32):
    """Custom type fsMIBgp4ForwardingPreservation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("preserved", 1),
          ("notPreserved", 2))
    )


_FsMIBgp4ForwardingPreservation_Type.__name__ = "Integer32"
_FsMIBgp4ForwardingPreservation_Object = MibScalar
fsMIBgp4ForwardingPreservation = _FsMIBgp4ForwardingPreservation_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 13),
    _FsMIBgp4ForwardingPreservation_Type()
)
fsMIBgp4ForwardingPreservation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4ForwardingPreservation.setStatus("current")
_FsMIBgpContextTable_Object = MibTable
fsMIBgpContextTable = _FsMIBgpContextTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14)
)
if mibBuilder.loadTexts:
    fsMIBgpContextTable.setStatus("current")
_FsMIBgpContextEntry_Object = MibTableRow
fsMIBgpContextEntry = _FsMIBgpContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1)
)
fsMIBgpContextEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
)
if mibBuilder.loadTexts:
    fsMIBgpContextEntry.setStatus("current")


class _FsMIBgp4ContextId_Type(Integer32):
    """Custom type fsMIBgp4ContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIBgp4ContextId_Type.__name__ = "Integer32"
_FsMIBgp4ContextId_Object = MibTableColumn
fsMIBgp4ContextId = _FsMIBgp4ContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 1),
    _FsMIBgp4ContextId_Type()
)
fsMIBgp4ContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4ContextId.setStatus("current")


class _FsMIBgp4GlobalAdminStatus_Type(Integer32):
    """Custom type fsMIBgp4GlobalAdminStatus based on Integer32"""
    defaultValue = 2

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


_FsMIBgp4GlobalAdminStatus_Type.__name__ = "Integer32"
_FsMIBgp4GlobalAdminStatus_Object = MibTableColumn
fsMIBgp4GlobalAdminStatus = _FsMIBgp4GlobalAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 2),
    _FsMIBgp4GlobalAdminStatus_Type()
)
fsMIBgp4GlobalAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4GlobalAdminStatus.setStatus("current")
_FsMIBgp4Identifier_Type = IpAddress
_FsMIBgp4Identifier_Object = MibTableColumn
fsMIBgp4Identifier = _FsMIBgp4Identifier_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 3),
    _FsMIBgp4Identifier_Type()
)
fsMIBgp4Identifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4Identifier.setStatus("current")


class _FsMIBgp4Synchronization_Type(Integer32):
    """Custom type fsMIBgp4Synchronization based on Integer32"""
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


_FsMIBgp4Synchronization_Type.__name__ = "Integer32"
_FsMIBgp4Synchronization_Object = MibTableColumn
fsMIBgp4Synchronization = _FsMIBgp4Synchronization_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 4),
    _FsMIBgp4Synchronization_Type()
)
fsMIBgp4Synchronization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4Synchronization.setStatus("current")


class _FsMIBgp4DefaultLocalPref_Type(Unsigned32):
    """Custom type fsMIBgp4DefaultLocalPref based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIBgp4DefaultLocalPref_Type.__name__ = "Unsigned32"
_FsMIBgp4DefaultLocalPref_Object = MibTableColumn
fsMIBgp4DefaultLocalPref = _FsMIBgp4DefaultLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 5),
    _FsMIBgp4DefaultLocalPref_Type()
)
fsMIBgp4DefaultLocalPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4DefaultLocalPref.setStatus("current")


class _FsMIBgp4AdvtNonBgpRt_Type(Integer32):
    """Custom type fsMIBgp4AdvtNonBgpRt based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("externalAndinternal", 2))
    )


_FsMIBgp4AdvtNonBgpRt_Type.__name__ = "Integer32"
_FsMIBgp4AdvtNonBgpRt_Object = MibTableColumn
fsMIBgp4AdvtNonBgpRt = _FsMIBgp4AdvtNonBgpRt_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 6),
    _FsMIBgp4AdvtNonBgpRt_Type()
)
fsMIBgp4AdvtNonBgpRt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4AdvtNonBgpRt.setStatus("current")


class _FsMIBgp4TraceEnable_Type(Unsigned32):
    """Custom type fsMIBgp4TraceEnable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIBgp4TraceEnable_Type.__name__ = "Unsigned32"
_FsMIBgp4TraceEnable_Object = MibTableColumn
fsMIBgp4TraceEnable = _FsMIBgp4TraceEnable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 7),
    _FsMIBgp4TraceEnable_Type()
)
fsMIBgp4TraceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4TraceEnable.setStatus("current")


class _FsMIBgp4DebugEnable_Type(Unsigned32):
    """Custom type fsMIBgp4DebugEnable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIBgp4DebugEnable_Type.__name__ = "Unsigned32"
_FsMIBgp4DebugEnable_Object = MibTableColumn
fsMIBgp4DebugEnable = _FsMIBgp4DebugEnable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 8),
    _FsMIBgp4DebugEnable_Type()
)
fsMIBgp4DebugEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4DebugEnable.setStatus("current")


class _FsMIBgp4OverlappingRoute_Type(Integer32):
    """Custom type fsMIBgp4OverlappingRoute based on Integer32"""
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
        *(("moreSpecific", 1),
          ("lessSpecific", 2),
          ("both", 3))
    )


_FsMIBgp4OverlappingRoute_Type.__name__ = "Integer32"
_FsMIBgp4OverlappingRoute_Object = MibTableColumn
fsMIBgp4OverlappingRoute = _FsMIBgp4OverlappingRoute_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 9),
    _FsMIBgp4OverlappingRoute_Type()
)
fsMIBgp4OverlappingRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4OverlappingRoute.setStatus("current")


class _FsMIBgp4AlwaysCompareMED_Type(Integer32):
    """Custom type fsMIBgp4AlwaysCompareMED based on Integer32"""
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


_FsMIBgp4AlwaysCompareMED_Type.__name__ = "Integer32"
_FsMIBgp4AlwaysCompareMED_Object = MibTableColumn
fsMIBgp4AlwaysCompareMED = _FsMIBgp4AlwaysCompareMED_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 10),
    _FsMIBgp4AlwaysCompareMED_Type()
)
fsMIBgp4AlwaysCompareMED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4AlwaysCompareMED.setStatus("current")


class _FsMIBgp4DefaultOriginate_Type(Integer32):
    """Custom type fsMIBgp4DefaultOriginate based on Integer32"""
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


_FsMIBgp4DefaultOriginate_Type.__name__ = "Integer32"
_FsMIBgp4DefaultOriginate_Object = MibTableColumn
fsMIBgp4DefaultOriginate = _FsMIBgp4DefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 11),
    _FsMIBgp4DefaultOriginate_Type()
)
fsMIBgp4DefaultOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4DefaultOriginate.setStatus("current")


class _FsMIBgp4DefaultIpv4UniCast_Type(Integer32):
    """Custom type fsMIBgp4DefaultIpv4UniCast based on Integer32"""
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


_FsMIBgp4DefaultIpv4UniCast_Type.__name__ = "Integer32"
_FsMIBgp4DefaultIpv4UniCast_Object = MibTableColumn
fsMIBgp4DefaultIpv4UniCast = _FsMIBgp4DefaultIpv4UniCast_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 12),
    _FsMIBgp4DefaultIpv4UniCast_Type()
)
fsMIBgp4DefaultIpv4UniCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4DefaultIpv4UniCast.setStatus("current")


class _FsMIBgp4IsTrapEnabled_Type(Integer32):
    """Custom type fsMIBgp4IsTrapEnabled based on Integer32"""
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


_FsMIBgp4IsTrapEnabled_Type.__name__ = "Integer32"
_FsMIBgp4IsTrapEnabled_Object = MibTableColumn
fsMIBgp4IsTrapEnabled = _FsMIBgp4IsTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 13),
    _FsMIBgp4IsTrapEnabled_Type()
)
fsMIBgp4IsTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4IsTrapEnabled.setStatus("current")


class _FsMIBgp4NextHopProcessingInterval_Type(Integer32):
    """Custom type fsMIBgp4NextHopProcessingInterval based on Integer32"""
    defaultValue = 60


_FsMIBgp4NextHopProcessingInterval_Type.__name__ = "Integer32"
_FsMIBgp4NextHopProcessingInterval_Object = MibTableColumn
fsMIBgp4NextHopProcessingInterval = _FsMIBgp4NextHopProcessingInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 14),
    _FsMIBgp4NextHopProcessingInterval_Type()
)
fsMIBgp4NextHopProcessingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4NextHopProcessingInterval.setStatus("current")


class _FsMIBgp4IBGPRedistributionStatus_Type(Integer32):
    """Custom type fsMIBgp4IBGPRedistributionStatus based on Integer32"""
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


_FsMIBgp4IBGPRedistributionStatus_Type.__name__ = "Integer32"
_FsMIBgp4IBGPRedistributionStatus_Object = MibTableColumn
fsMIBgp4IBGPRedistributionStatus = _FsMIBgp4IBGPRedistributionStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 15),
    _FsMIBgp4IBGPRedistributionStatus_Type()
)
fsMIBgp4IBGPRedistributionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4IBGPRedistributionStatus.setStatus("current")


class _FsMIBgp4RRDAdminStatus_Type(Integer32):
    """Custom type fsMIBgp4RRDAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsMIBgp4RRDAdminStatus_Type.__name__ = "Integer32"
_FsMIBgp4RRDAdminStatus_Object = MibTableColumn
fsMIBgp4RRDAdminStatus = _FsMIBgp4RRDAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 16),
    _FsMIBgp4RRDAdminStatus_Type()
)
fsMIBgp4RRDAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RRDAdminStatus.setStatus("current")
_FsMIBgp4RRDProtoMaskForEnable_Type = Integer32
_FsMIBgp4RRDProtoMaskForEnable_Object = MibTableColumn
fsMIBgp4RRDProtoMaskForEnable = _FsMIBgp4RRDProtoMaskForEnable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 17),
    _FsMIBgp4RRDProtoMaskForEnable_Type()
)
fsMIBgp4RRDProtoMaskForEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RRDProtoMaskForEnable.setStatus("current")
_FsMIBgp4RRDSrcProtoMaskForDisable_Type = Integer32
_FsMIBgp4RRDSrcProtoMaskForDisable_Object = MibTableColumn
fsMIBgp4RRDSrcProtoMaskForDisable = _FsMIBgp4RRDSrcProtoMaskForDisable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 18),
    _FsMIBgp4RRDSrcProtoMaskForDisable_Type()
)
fsMIBgp4RRDSrcProtoMaskForDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RRDSrcProtoMaskForDisable.setStatus("current")


class _FsMIBgp4RRDDefaultMetric_Type(Unsigned32):
    """Custom type fsMIBgp4RRDDefaultMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIBgp4RRDDefaultMetric_Type.__name__ = "Unsigned32"
_FsMIBgp4RRDDefaultMetric_Object = MibTableColumn
fsMIBgp4RRDDefaultMetric = _FsMIBgp4RRDDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 19),
    _FsMIBgp4RRDDefaultMetric_Type()
)
fsMIBgp4RRDDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RRDDefaultMetric.setStatus("current")


class _FsMIBgp4RRDRouteMapName_Type(DisplayString):
    """Custom type fsMIBgp4RRDRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_FsMIBgp4RRDRouteMapName_Type.__name__ = "DisplayString"
_FsMIBgp4RRDRouteMapName_Object = MibTableColumn
fsMIBgp4RRDRouteMapName = _FsMIBgp4RRDRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 20),
    _FsMIBgp4RRDRouteMapName_Type()
)
fsMIBgp4RRDRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RRDRouteMapName.setStatus("current")


class _FsMIBgp4RRDMatchTypeEnable_Type(Integer32):
    """Custom type fsMIBgp4RRDMatchTypeEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2),
          ("nssaExternal", 4))
    )


_FsMIBgp4RRDMatchTypeEnable_Type.__name__ = "Integer32"
_FsMIBgp4RRDMatchTypeEnable_Object = MibTableColumn
fsMIBgp4RRDMatchTypeEnable = _FsMIBgp4RRDMatchTypeEnable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 21),
    _FsMIBgp4RRDMatchTypeEnable_Type()
)
fsMIBgp4RRDMatchTypeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RRDMatchTypeEnable.setStatus("current")


class _FsMIBgp4RRDMatchTypeDisable_Type(Integer32):
    """Custom type fsMIBgp4RRDMatchTypeDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 2),
          ("nssaExternal", 4))
    )


_FsMIBgp4RRDMatchTypeDisable_Type.__name__ = "Integer32"
_FsMIBgp4RRDMatchTypeDisable_Object = MibTableColumn
fsMIBgp4RRDMatchTypeDisable = _FsMIBgp4RRDMatchTypeDisable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 22),
    _FsMIBgp4RRDMatchTypeDisable_Type()
)
fsMIBgp4RRDMatchTypeDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RRDMatchTypeDisable.setStatus("current")


class _FsMIBgp4AscConfedId_Type(Unsigned32):
    """Custom type fsMIBgp4AscConfedId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIBgp4AscConfedId_Type.__name__ = "Unsigned32"
_FsMIBgp4AscConfedId_Object = MibTableColumn
fsMIBgp4AscConfedId = _FsMIBgp4AscConfedId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 23),
    _FsMIBgp4AscConfedId_Type()
)
fsMIBgp4AscConfedId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4AscConfedId.setStatus("current")


class _FsMIBgp4AscConfedBestPathCompareMED_Type(Integer32):
    """Custom type fsMIBgp4AscConfedBestPathCompareMED based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("clear", 2))
    )


_FsMIBgp4AscConfedBestPathCompareMED_Type.__name__ = "Integer32"
_FsMIBgp4AscConfedBestPathCompareMED_Object = MibTableColumn
fsMIBgp4AscConfedBestPathCompareMED = _FsMIBgp4AscConfedBestPathCompareMED_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 24),
    _FsMIBgp4AscConfedBestPathCompareMED_Type()
)
fsMIBgp4AscConfedBestPathCompareMED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4AscConfedBestPathCompareMED.setStatus("current")


class _FsMIBgp4RflbgpClusterId_Type(OctetString):
    """Custom type fsMIBgp4RflbgpClusterId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_FsMIBgp4RflbgpClusterId_Type.__name__ = "OctetString"
_FsMIBgp4RflbgpClusterId_Object = MibTableColumn
fsMIBgp4RflbgpClusterId = _FsMIBgp4RflbgpClusterId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 25),
    _FsMIBgp4RflbgpClusterId_Type()
)
fsMIBgp4RflbgpClusterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RflbgpClusterId.setStatus("current")


class _FsMIBgp4RflRflSupport_Type(Integer32):
    """Custom type fsMIBgp4RflRflSupport based on Integer32"""
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
        *(("none", 1),
          ("clientsupport", 2),
          ("noClientSupport", 3))
    )


_FsMIBgp4RflRflSupport_Type.__name__ = "Integer32"
_FsMIBgp4RflRflSupport_Object = MibTableColumn
fsMIBgp4RflRflSupport = _FsMIBgp4RflRflSupport_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 26),
    _FsMIBgp4RflRflSupport_Type()
)
fsMIBgp4RflRflSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RflRflSupport.setStatus("current")


class _FsMIBgp4RfdCutOff_Type(Integer32):
    """Custom type fsMIBgp4RfdCutOff based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 3999),
    )


_FsMIBgp4RfdCutOff_Type.__name__ = "Integer32"
_FsMIBgp4RfdCutOff_Object = MibTableColumn
fsMIBgp4RfdCutOff = _FsMIBgp4RfdCutOff_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 27),
    _FsMIBgp4RfdCutOff_Type()
)
fsMIBgp4RfdCutOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RfdCutOff.setStatus("current")


class _FsMIBgp4RfdReuse_Type(Integer32):
    """Custom type fsMIBgp4RfdReuse based on Integer32"""
    defaultValue = 750

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1999),
    )


_FsMIBgp4RfdReuse_Type.__name__ = "Integer32"
_FsMIBgp4RfdReuse_Object = MibTableColumn
fsMIBgp4RfdReuse = _FsMIBgp4RfdReuse_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 28),
    _FsMIBgp4RfdReuse_Type()
)
fsMIBgp4RfdReuse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RfdReuse.setStatus("current")


class _FsMIBgp4RfdCeiling_Type(Integer32):
    """Custom type fsMIBgp4RfdCeiling based on Integer32"""
    defaultValue = 8000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 10000),
    )


_FsMIBgp4RfdCeiling_Type.__name__ = "Integer32"
_FsMIBgp4RfdCeiling_Object = MibTableColumn
fsMIBgp4RfdCeiling = _FsMIBgp4RfdCeiling_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 29),
    _FsMIBgp4RfdCeiling_Type()
)
fsMIBgp4RfdCeiling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4RfdCeiling.setStatus("current")


class _FsMIBgp4RfdMaxHoldDownTime_Type(Integer32):
    """Custom type fsMIBgp4RfdMaxHoldDownTime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 10800),
    )


_FsMIBgp4RfdMaxHoldDownTime_Type.__name__ = "Integer32"
_FsMIBgp4RfdMaxHoldDownTime_Object = MibTableColumn
fsMIBgp4RfdMaxHoldDownTime = _FsMIBgp4RfdMaxHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 30),
    _FsMIBgp4RfdMaxHoldDownTime_Type()
)
fsMIBgp4RfdMaxHoldDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RfdMaxHoldDownTime.setStatus("current")


class _FsMIBgp4RfdDecayHalfLifeTime_Type(Integer32):
    """Custom type fsMIBgp4RfdDecayHalfLifeTime based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 2700),
    )


_FsMIBgp4RfdDecayHalfLifeTime_Type.__name__ = "Integer32"
_FsMIBgp4RfdDecayHalfLifeTime_Object = MibTableColumn
fsMIBgp4RfdDecayHalfLifeTime = _FsMIBgp4RfdDecayHalfLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 31),
    _FsMIBgp4RfdDecayHalfLifeTime_Type()
)
fsMIBgp4RfdDecayHalfLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RfdDecayHalfLifeTime.setStatus("current")


class _FsMIBgp4RfdDecayTimerGranularity_Type(Integer32):
    """Custom type fsMIBgp4RfdDecayTimerGranularity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10800),
    )


_FsMIBgp4RfdDecayTimerGranularity_Type.__name__ = "Integer32"
_FsMIBgp4RfdDecayTimerGranularity_Object = MibTableColumn
fsMIBgp4RfdDecayTimerGranularity = _FsMIBgp4RfdDecayTimerGranularity_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 32),
    _FsMIBgp4RfdDecayTimerGranularity_Type()
)
fsMIBgp4RfdDecayTimerGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RfdDecayTimerGranularity.setStatus("current")


class _FsMIBgp4RfdReuseTimerGranularity_Type(Integer32):
    """Custom type fsMIBgp4RfdReuseTimerGranularity based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 10800),
    )


_FsMIBgp4RfdReuseTimerGranularity_Type.__name__ = "Integer32"
_FsMIBgp4RfdReuseTimerGranularity_Object = MibTableColumn
fsMIBgp4RfdReuseTimerGranularity = _FsMIBgp4RfdReuseTimerGranularity_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 33),
    _FsMIBgp4RfdReuseTimerGranularity_Type()
)
fsMIBgp4RfdReuseTimerGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RfdReuseTimerGranularity.setStatus("current")


class _FsMIBgp4RfdReuseIndxArraySize_Type(Integer32):
    """Custom type fsMIBgp4RfdReuseIndxArraySize based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 65535),
    )


_FsMIBgp4RfdReuseIndxArraySize_Type.__name__ = "Integer32"
_FsMIBgp4RfdReuseIndxArraySize_Object = MibTableColumn
fsMIBgp4RfdReuseIndxArraySize = _FsMIBgp4RfdReuseIndxArraySize_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 34),
    _FsMIBgp4RfdReuseIndxArraySize_Type()
)
fsMIBgp4RfdReuseIndxArraySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RfdReuseIndxArraySize.setStatus("current")


class _FsMIBgp4RfdAdminStatus_Type(Integer32):
    """Custom type fsMIBgp4RfdAdminStatus based on Integer32"""
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


_FsMIBgp4RfdAdminStatus_Type.__name__ = "Integer32"
_FsMIBgp4RfdAdminStatus_Object = MibTableColumn
fsMIBgp4RfdAdminStatus = _FsMIBgp4RfdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 35),
    _FsMIBgp4RfdAdminStatus_Type()
)
fsMIBgp4RfdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RfdAdminStatus.setStatus("current")


class _FsMIBgp4CommMaxInFTblEntries_Type(Integer32):
    """Custom type fsMIBgp4CommMaxInFTblEntries based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50000),
    )


_FsMIBgp4CommMaxInFTblEntries_Type.__name__ = "Integer32"
_FsMIBgp4CommMaxInFTblEntries_Object = MibTableColumn
fsMIBgp4CommMaxInFTblEntries = _FsMIBgp4CommMaxInFTblEntries_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 36),
    _FsMIBgp4CommMaxInFTblEntries_Type()
)
fsMIBgp4CommMaxInFTblEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4CommMaxInFTblEntries.setStatus("current")


class _FsMIBgp4CommMaxOutFTblEntries_Type(Integer32):
    """Custom type fsMIBgp4CommMaxOutFTblEntries based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50000),
    )


_FsMIBgp4CommMaxOutFTblEntries_Type.__name__ = "Integer32"
_FsMIBgp4CommMaxOutFTblEntries_Object = MibTableColumn
fsMIBgp4CommMaxOutFTblEntries = _FsMIBgp4CommMaxOutFTblEntries_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 37),
    _FsMIBgp4CommMaxOutFTblEntries_Type()
)
fsMIBgp4CommMaxOutFTblEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4CommMaxOutFTblEntries.setStatus("current")


class _FsMIBgp4ExtCommMaxInFTblEntries_Type(Integer32):
    """Custom type fsMIBgp4ExtCommMaxInFTblEntries based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_FsMIBgp4ExtCommMaxInFTblEntries_Type.__name__ = "Integer32"
_FsMIBgp4ExtCommMaxInFTblEntries_Object = MibTableColumn
fsMIBgp4ExtCommMaxInFTblEntries = _FsMIBgp4ExtCommMaxInFTblEntries_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 38),
    _FsMIBgp4ExtCommMaxInFTblEntries_Type()
)
fsMIBgp4ExtCommMaxInFTblEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4ExtCommMaxInFTblEntries.setStatus("current")


class _FsMIBgp4ExtCommMaxOutFTblEntries_Type(Integer32):
    """Custom type fsMIBgp4ExtCommMaxOutFTblEntries based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_FsMIBgp4ExtCommMaxOutFTblEntries_Type.__name__ = "Integer32"
_FsMIBgp4ExtCommMaxOutFTblEntries_Object = MibTableColumn
fsMIBgp4ExtCommMaxOutFTblEntries = _FsMIBgp4ExtCommMaxOutFTblEntries_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 39),
    _FsMIBgp4ExtCommMaxOutFTblEntries_Type()
)
fsMIBgp4ExtCommMaxOutFTblEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4ExtCommMaxOutFTblEntries.setStatus("current")


class _FsMIBgp4CapabilitySupportAvailable_Type(TruthValue):
    """Custom type fsMIBgp4CapabilitySupportAvailable based on TruthValue"""
    defaultValue = 1


_FsMIBgp4CapabilitySupportAvailable_Type.__name__ = "TruthValue"
_FsMIBgp4CapabilitySupportAvailable_Object = MibTableColumn
fsMIBgp4CapabilitySupportAvailable = _FsMIBgp4CapabilitySupportAvailable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 40),
    _FsMIBgp4CapabilitySupportAvailable_Type()
)
fsMIBgp4CapabilitySupportAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4CapabilitySupportAvailable.setStatus("current")


class _FsMIBgp4MaxCapsPerPeer_Type(Integer32):
    """Custom type fsMIBgp4MaxCapsPerPeer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsMIBgp4MaxCapsPerPeer_Type.__name__ = "Integer32"
_FsMIBgp4MaxCapsPerPeer_Object = MibTableColumn
fsMIBgp4MaxCapsPerPeer = _FsMIBgp4MaxCapsPerPeer_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 41),
    _FsMIBgp4MaxCapsPerPeer_Type()
)
fsMIBgp4MaxCapsPerPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4MaxCapsPerPeer.setStatus("current")


class _FsMIBgp4MaxInstancesPerCap_Type(Integer32):
    """Custom type fsMIBgp4MaxInstancesPerCap based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsMIBgp4MaxInstancesPerCap_Type.__name__ = "Integer32"
_FsMIBgp4MaxInstancesPerCap_Object = MibTableColumn
fsMIBgp4MaxInstancesPerCap = _FsMIBgp4MaxInstancesPerCap_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 42),
    _FsMIBgp4MaxInstancesPerCap_Type()
)
fsMIBgp4MaxInstancesPerCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4MaxInstancesPerCap.setStatus("current")


class _FsMIBgp4MaxCapDataSize_Type(Integer32):
    """Custom type fsMIBgp4MaxCapDataSize based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 252),
    )


_FsMIBgp4MaxCapDataSize_Type.__name__ = "Integer32"
_FsMIBgp4MaxCapDataSize_Object = MibTableColumn
fsMIBgp4MaxCapDataSize = _FsMIBgp4MaxCapDataSize_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 43),
    _FsMIBgp4MaxCapDataSize_Type()
)
fsMIBgp4MaxCapDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4MaxCapDataSize.setStatus("current")


class _FsMIBgp4PreferenceValue_Type(Integer32):
    """Custom type fsMIBgp4PreferenceValue based on Integer32"""
    defaultValue = 122

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIBgp4PreferenceValue_Type.__name__ = "Integer32"
_FsMIBgp4PreferenceValue_Object = MibTableColumn
fsMIBgp4PreferenceValue = _FsMIBgp4PreferenceValue_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 44),
    _FsMIBgp4PreferenceValue_Type()
)
fsMIBgp4PreferenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PreferenceValue.setStatus("current")


class _FsMIBgp4ContextStatus_Type(Integer32):
    """Custom type fsMIBgp4ContextStatus based on Integer32"""
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


_FsMIBgp4ContextStatus_Type.__name__ = "Integer32"
_FsMIBgp4ContextStatus_Object = MibTableColumn
fsMIBgp4ContextStatus = _FsMIBgp4ContextStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 45),
    _FsMIBgp4ContextStatus_Type()
)
fsMIBgp4ContextStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4ContextStatus.setStatus("current")


class _FsMIBgp4IBGPMaxPaths_Type(Integer32):
    """Custom type fsMIBgp4IBGPMaxPaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FsMIBgp4IBGPMaxPaths_Type.__name__ = "Integer32"
_FsMIBgp4IBGPMaxPaths_Object = MibTableColumn
fsMIBgp4IBGPMaxPaths = _FsMIBgp4IBGPMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 46),
    _FsMIBgp4IBGPMaxPaths_Type()
)
fsMIBgp4IBGPMaxPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4IBGPMaxPaths.setStatus("current")


class _FsMIBgp4EBGPMaxPaths_Type(Integer32):
    """Custom type fsMIBgp4EBGPMaxPaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FsMIBgp4EBGPMaxPaths_Type.__name__ = "Integer32"
_FsMIBgp4EBGPMaxPaths_Object = MibTableColumn
fsMIBgp4EBGPMaxPaths = _FsMIBgp4EBGPMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 47),
    _FsMIBgp4EBGPMaxPaths_Type()
)
fsMIBgp4EBGPMaxPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4EBGPMaxPaths.setStatus("current")


class _FsMIBgp4EIBGPMaxPaths_Type(Integer32):
    """Custom type fsMIBgp4EIBGPMaxPaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FsMIBgp4EIBGPMaxPaths_Type.__name__ = "Integer32"
_FsMIBgp4EIBGPMaxPaths_Object = MibTableColumn
fsMIBgp4EIBGPMaxPaths = _FsMIBgp4EIBGPMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 48),
    _FsMIBgp4EIBGPMaxPaths_Type()
)
fsMIBgp4EIBGPMaxPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4EIBGPMaxPaths.setStatus("current")


class _FsMIBgp4OperIBGPMaxPaths_Type(Integer32):
    """Custom type fsMIBgp4OperIBGPMaxPaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FsMIBgp4OperIBGPMaxPaths_Type.__name__ = "Integer32"
_FsMIBgp4OperIBGPMaxPaths_Object = MibTableColumn
fsMIBgp4OperIBGPMaxPaths = _FsMIBgp4OperIBGPMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 49),
    _FsMIBgp4OperIBGPMaxPaths_Type()
)
fsMIBgp4OperIBGPMaxPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4OperIBGPMaxPaths.setStatus("current")


class _FsMIBgp4OperEBGPMaxPaths_Type(Integer32):
    """Custom type fsMIBgp4OperEBGPMaxPaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FsMIBgp4OperEBGPMaxPaths_Type.__name__ = "Integer32"
_FsMIBgp4OperEBGPMaxPaths_Object = MibTableColumn
fsMIBgp4OperEBGPMaxPaths = _FsMIBgp4OperEBGPMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 50),
    _FsMIBgp4OperEBGPMaxPaths_Type()
)
fsMIBgp4OperEBGPMaxPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4OperEBGPMaxPaths.setStatus("current")


class _FsMIBgp4OperEIBGPMaxPaths_Type(Integer32):
    """Custom type fsMIBgp4OperEIBGPMaxPaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FsMIBgp4OperEIBGPMaxPaths_Type.__name__ = "Integer32"
_FsMIBgp4OperEIBGPMaxPaths_Object = MibTableColumn
fsMIBgp4OperEIBGPMaxPaths = _FsMIBgp4OperEIBGPMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 51),
    _FsMIBgp4OperEIBGPMaxPaths_Type()
)
fsMIBgp4OperEIBGPMaxPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4OperEIBGPMaxPaths.setStatus("current")


class _FsMIBgp4FourByteASNSupportStatus_Type(Integer32):
    """Custom type fsMIBgp4FourByteASNSupportStatus based on Integer32"""
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


_FsMIBgp4FourByteASNSupportStatus_Type.__name__ = "Integer32"
_FsMIBgp4FourByteASNSupportStatus_Object = MibTableColumn
fsMIBgp4FourByteASNSupportStatus = _FsMIBgp4FourByteASNSupportStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 52),
    _FsMIBgp4FourByteASNSupportStatus_Type()
)
fsMIBgp4FourByteASNSupportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4FourByteASNSupportStatus.setStatus("current")


class _FsMIBgp4FourByteASNotationType_Type(Integer32):
    """Custom type fsMIBgp4FourByteASNotationType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asplain", 1),
          ("asdot", 2))
    )


_FsMIBgp4FourByteASNotationType_Type.__name__ = "Integer32"
_FsMIBgp4FourByteASNotationType_Object = MibTableColumn
fsMIBgp4FourByteASNotationType = _FsMIBgp4FourByteASNotationType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 53),
    _FsMIBgp4FourByteASNotationType_Type()
)
fsMIBgp4FourByteASNotationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4FourByteASNotationType.setStatus("current")


class _FsMIBgp4LocalAsNo_Type(Unsigned32):
    """Custom type fsMIBgp4LocalAsNo based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIBgp4LocalAsNo_Type.__name__ = "Unsigned32"
_FsMIBgp4LocalAsNo_Object = MibTableColumn
fsMIBgp4LocalAsNo = _FsMIBgp4LocalAsNo_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 54),
    _FsMIBgp4LocalAsNo_Type()
)
fsMIBgp4LocalAsNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4LocalAsNo.setStatus("current")
_FsMIBgp4RIBRoutes_Type = Counter32
_FsMIBgp4RIBRoutes_Object = MibTableColumn
fsMIBgp4RIBRoutes = _FsMIBgp4RIBRoutes_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 55),
    _FsMIBgp4RIBRoutes_Type()
)
fsMIBgp4RIBRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4RIBRoutes.setStatus("current")


class _FsMIBgp4Ipv4AddrFamily_Type(Integer32):
    """Custom type fsMIBgp4Ipv4AddrFamily based on Integer32"""
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


_FsMIBgp4Ipv4AddrFamily_Type.__name__ = "Integer32"
_FsMIBgp4Ipv4AddrFamily_Object = MibTableColumn
fsMIBgp4Ipv4AddrFamily = _FsMIBgp4Ipv4AddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 56),
    _FsMIBgp4Ipv4AddrFamily_Type()
)
fsMIBgp4Ipv4AddrFamily.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4Ipv4AddrFamily.setStatus("current")


class _FsMIBgp4Ipv6AddrFamily_Type(Integer32):
    """Custom type fsMIBgp4Ipv6AddrFamily based on Integer32"""
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


_FsMIBgp4Ipv6AddrFamily_Type.__name__ = "Integer32"
_FsMIBgp4Ipv6AddrFamily_Object = MibTableColumn
fsMIBgp4Ipv6AddrFamily = _FsMIBgp4Ipv6AddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 57),
    _FsMIBgp4Ipv6AddrFamily_Type()
)
fsMIBgp4Ipv6AddrFamily.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4Ipv6AddrFamily.setStatus("current")


class _FsMIBgp4VpnLabelAllocPolicy_Type(Integer32):
    """Custom type fsMIBgp4VpnLabelAllocPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pervrf", 1),
          ("perroute", 2))
    )


_FsMIBgp4VpnLabelAllocPolicy_Type.__name__ = "Integer32"
_FsMIBgp4VpnLabelAllocPolicy_Object = MibTableColumn
fsMIBgp4VpnLabelAllocPolicy = _FsMIBgp4VpnLabelAllocPolicy_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 58),
    _FsMIBgp4VpnLabelAllocPolicy_Type()
)
fsMIBgp4VpnLabelAllocPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4VpnLabelAllocPolicy.setStatus("current")


class _FsMIBgp4VPNV4AddrFamily_Type(Integer32):
    """Custom type fsMIBgp4VPNV4AddrFamily based on Integer32"""
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


_FsMIBgp4VPNV4AddrFamily_Type.__name__ = "Integer32"
_FsMIBgp4VPNV4AddrFamily_Object = MibTableColumn
fsMIBgp4VPNV4AddrFamily = _FsMIBgp4VPNV4AddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 59),
    _FsMIBgp4VPNV4AddrFamily_Type()
)
fsMIBgp4VPNV4AddrFamily.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4VPNV4AddrFamily.setStatus("current")


class _FsMIBgp4L2vpnAddrFamily_Type(Integer32):
    """Custom type fsMIBgp4L2vpnAddrFamily based on Integer32"""
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


_FsMIBgp4L2vpnAddrFamily_Type.__name__ = "Integer32"
_FsMIBgp4L2vpnAddrFamily_Object = MibTableColumn
fsMIBgp4L2vpnAddrFamily = _FsMIBgp4L2vpnAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 60),
    _FsMIBgp4L2vpnAddrFamily_Type()
)
fsMIBgp4L2vpnAddrFamily.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4L2vpnAddrFamily.setStatus("current")


class _FsMIBgp4EvpnAddrFamily_Type(Integer32):
    """Custom type fsMIBgp4EvpnAddrFamily based on Integer32"""
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


_FsMIBgp4EvpnAddrFamily_Type.__name__ = "Integer32"
_FsMIBgp4EvpnAddrFamily_Object = MibTableColumn
fsMIBgp4EvpnAddrFamily = _FsMIBgp4EvpnAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 14, 1, 61),
    _FsMIBgp4EvpnAddrFamily_Type()
)
fsMIBgp4EvpnAddrFamily.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4EvpnAddrFamily.setStatus("current")
_FsMIBgp4RRDMetricTable_Object = MibTable
fsMIBgp4RRDMetricTable = _FsMIBgp4RRDMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 15)
)
if mibBuilder.loadTexts:
    fsMIBgp4RRDMetricTable.setStatus("current")
_FsMIBgp4RRDMetricEntry_Object = MibTableRow
fsMIBgp4RRDMetricEntry = _FsMIBgp4RRDMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 15, 1)
)
fsMIBgp4RRDMetricEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4RRDMetricProtocolId"),
)
if mibBuilder.loadTexts:
    fsMIBgp4RRDMetricEntry.setStatus("current")


class _FsMIBgp4RRDMetricProtocolId_Type(Integer32):
    """Custom type fsMIBgp4RRDMetricProtocolId based on Integer32"""
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
        *(("ospf", 1),
          ("rip", 2),
          ("connected", 3),
          ("static", 4))
    )


_FsMIBgp4RRDMetricProtocolId_Type.__name__ = "Integer32"
_FsMIBgp4RRDMetricProtocolId_Object = MibTableColumn
fsMIBgp4RRDMetricProtocolId = _FsMIBgp4RRDMetricProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 15, 1, 1),
    _FsMIBgp4RRDMetricProtocolId_Type()
)
fsMIBgp4RRDMetricProtocolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4RRDMetricProtocolId.setStatus("current")
_FsMIBgp4RRDMetricValue_Type = Integer32
_FsMIBgp4RRDMetricValue_Object = MibTableColumn
fsMIBgp4RRDMetricValue = _FsMIBgp4RRDMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 15, 1, 2),
    _FsMIBgp4RRDMetricValue_Type()
)
fsMIBgp4RRDMetricValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RRDMetricValue.setStatus("current")
_FsMIBgpComm_ObjectIdentity = ObjectIdentity
fsMIBgpComm = _FsMIBgpComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 16)
)
_FsMIBgp4CommInFilterTable_Object = MibTable
fsMIBgp4CommInFilterTable = _FsMIBgp4CommInFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 16, 1)
)
if mibBuilder.loadTexts:
    fsMIBgp4CommInFilterTable.setStatus("current")
_FsMIBgp4CommInFilterEntry_Object = MibTableRow
fsMIBgp4CommInFilterEntry = _FsMIBgp4CommInFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 16, 1, 1)
)
fsMIBgp4CommInFilterEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4InFilterCommVal"),
)
if mibBuilder.loadTexts:
    fsMIBgp4CommInFilterEntry.setStatus("current")


class _FsMIBgp4InFilterCommVal_Type(Unsigned32):
    """Custom type fsMIBgp4InFilterCommVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65536, 4294901759),
        ValueRangeConstraint(4294967041, 4294967043),
    )


_FsMIBgp4InFilterCommVal_Type.__name__ = "Unsigned32"
_FsMIBgp4InFilterCommVal_Object = MibTableColumn
fsMIBgp4InFilterCommVal = _FsMIBgp4InFilterCommVal_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 16, 1, 1, 1),
    _FsMIBgp4InFilterCommVal_Type()
)
fsMIBgp4InFilterCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4InFilterCommVal.setStatus("current")


class _FsMIBgp4CommIncomingFilterStatus_Type(Integer32):
    """Custom type fsMIBgp4CommIncomingFilterStatus based on Integer32"""
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
        *(("none", 1),
          ("accept", 2),
          ("deny", 3))
    )


_FsMIBgp4CommIncomingFilterStatus_Type.__name__ = "Integer32"
_FsMIBgp4CommIncomingFilterStatus_Object = MibTableColumn
fsMIBgp4CommIncomingFilterStatus = _FsMIBgp4CommIncomingFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 16, 1, 1, 2),
    _FsMIBgp4CommIncomingFilterStatus_Type()
)
fsMIBgp4CommIncomingFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4CommIncomingFilterStatus.setStatus("current")
_FsMIBgp4InFilterRowStatus_Type = RowStatus
_FsMIBgp4InFilterRowStatus_Object = MibTableColumn
fsMIBgp4InFilterRowStatus = _FsMIBgp4InFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 16, 1, 1, 3),
    _FsMIBgp4InFilterRowStatus_Type()
)
fsMIBgp4InFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4InFilterRowStatus.setStatus("current")
_FsMIBgp4CommOutFilterTable_Object = MibTable
fsMIBgp4CommOutFilterTable = _FsMIBgp4CommOutFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 16, 2)
)
if mibBuilder.loadTexts:
    fsMIBgp4CommOutFilterTable.setStatus("current")
_FsMIBgp4CommOutFilterEntry_Object = MibTableRow
fsMIBgp4CommOutFilterEntry = _FsMIBgp4CommOutFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 16, 2, 1)
)
fsMIBgp4CommOutFilterEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4OutFilterCommVal"),
)
if mibBuilder.loadTexts:
    fsMIBgp4CommOutFilterEntry.setStatus("current")


class _FsMIBgp4OutFilterCommVal_Type(Unsigned32):
    """Custom type fsMIBgp4OutFilterCommVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65536, 4294901759),
        ValueRangeConstraint(4294967041, 4294967043),
    )


_FsMIBgp4OutFilterCommVal_Type.__name__ = "Unsigned32"
_FsMIBgp4OutFilterCommVal_Object = MibTableColumn
fsMIBgp4OutFilterCommVal = _FsMIBgp4OutFilterCommVal_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 16, 2, 1, 1),
    _FsMIBgp4OutFilterCommVal_Type()
)
fsMIBgp4OutFilterCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4OutFilterCommVal.setStatus("current")


class _FsMIBgp4CommOutgoingFilterStatus_Type(Integer32):
    """Custom type fsMIBgp4CommOutgoingFilterStatus based on Integer32"""
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
        *(("none", 1),
          ("advertise", 2),
          ("filter", 3))
    )


_FsMIBgp4CommOutgoingFilterStatus_Type.__name__ = "Integer32"
_FsMIBgp4CommOutgoingFilterStatus_Object = MibTableColumn
fsMIBgp4CommOutgoingFilterStatus = _FsMIBgp4CommOutgoingFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 16, 2, 1, 2),
    _FsMIBgp4CommOutgoingFilterStatus_Type()
)
fsMIBgp4CommOutgoingFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4CommOutgoingFilterStatus.setStatus("current")
_FsMIBgp4OutFilterRowStatus_Type = RowStatus
_FsMIBgp4OutFilterRowStatus_Object = MibTableColumn
fsMIBgp4OutFilterRowStatus = _FsMIBgp4OutFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 16, 2, 1, 3),
    _FsMIBgp4OutFilterRowStatus_Type()
)
fsMIBgp4OutFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4OutFilterRowStatus.setStatus("current")
_FsMIBgpExtComm_ObjectIdentity = ObjectIdentity
fsMIBgpExtComm = _FsMIBgpExtComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 17)
)
_FsMIBgp4ExtCommInFilterTable_Object = MibTable
fsMIBgp4ExtCommInFilterTable = _FsMIBgp4ExtCommInFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 17, 1)
)
if mibBuilder.loadTexts:
    fsMIBgp4ExtCommInFilterTable.setStatus("current")
_FsMIBgp4ExtCommInFilterEntry_Object = MibTableRow
fsMIBgp4ExtCommInFilterEntry = _FsMIBgp4ExtCommInFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 17, 1, 1)
)
fsMIBgp4ExtCommInFilterEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ExtCommInFilterCommVal"),
)
if mibBuilder.loadTexts:
    fsMIBgp4ExtCommInFilterEntry.setStatus("current")


class _FsMIBgp4ExtCommInFilterCommVal_Type(OctetString):
    """Custom type fsMIBgp4ExtCommInFilterCommVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsMIBgp4ExtCommInFilterCommVal_Type.__name__ = "OctetString"
_FsMIBgp4ExtCommInFilterCommVal_Object = MibTableColumn
fsMIBgp4ExtCommInFilterCommVal = _FsMIBgp4ExtCommInFilterCommVal_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 17, 1, 1, 1),
    _FsMIBgp4ExtCommInFilterCommVal_Type()
)
fsMIBgp4ExtCommInFilterCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4ExtCommInFilterCommVal.setStatus("current")


class _FsMIBgp4ExtCommIncomingFilterStatus_Type(Integer32):
    """Custom type fsMIBgp4ExtCommIncomingFilterStatus based on Integer32"""
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
        *(("none", 1),
          ("accept", 2),
          ("deny", 3))
    )


_FsMIBgp4ExtCommIncomingFilterStatus_Type.__name__ = "Integer32"
_FsMIBgp4ExtCommIncomingFilterStatus_Object = MibTableColumn
fsMIBgp4ExtCommIncomingFilterStatus = _FsMIBgp4ExtCommIncomingFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 17, 1, 1, 2),
    _FsMIBgp4ExtCommIncomingFilterStatus_Type()
)
fsMIBgp4ExtCommIncomingFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4ExtCommIncomingFilterStatus.setStatus("current")
_FsMIBgp4ExtCommInFilterRowStatus_Type = RowStatus
_FsMIBgp4ExtCommInFilterRowStatus_Object = MibTableColumn
fsMIBgp4ExtCommInFilterRowStatus = _FsMIBgp4ExtCommInFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 17, 1, 1, 3),
    _FsMIBgp4ExtCommInFilterRowStatus_Type()
)
fsMIBgp4ExtCommInFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4ExtCommInFilterRowStatus.setStatus("current")
_FsMIBgp4ExtCommOutFilterTable_Object = MibTable
fsMIBgp4ExtCommOutFilterTable = _FsMIBgp4ExtCommOutFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 17, 2)
)
if mibBuilder.loadTexts:
    fsMIBgp4ExtCommOutFilterTable.setStatus("current")
_FsMIBgp4ExtCommOutFilterEntry_Object = MibTableRow
fsMIBgp4ExtCommOutFilterEntry = _FsMIBgp4ExtCommOutFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 17, 2, 1)
)
fsMIBgp4ExtCommOutFilterEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ExtCommOutFilterCommVal"),
)
if mibBuilder.loadTexts:
    fsMIBgp4ExtCommOutFilterEntry.setStatus("current")


class _FsMIBgp4ExtCommOutFilterCommVal_Type(OctetString):
    """Custom type fsMIBgp4ExtCommOutFilterCommVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsMIBgp4ExtCommOutFilterCommVal_Type.__name__ = "OctetString"
_FsMIBgp4ExtCommOutFilterCommVal_Object = MibTableColumn
fsMIBgp4ExtCommOutFilterCommVal = _FsMIBgp4ExtCommOutFilterCommVal_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 17, 2, 1, 1),
    _FsMIBgp4ExtCommOutFilterCommVal_Type()
)
fsMIBgp4ExtCommOutFilterCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4ExtCommOutFilterCommVal.setStatus("current")


class _FsMIBgp4ExtCommOutgoingFilterStatus_Type(Integer32):
    """Custom type fsMIBgp4ExtCommOutgoingFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("advertise", 2),
          ("noadvertise", 3))
    )


_FsMIBgp4ExtCommOutgoingFilterStatus_Type.__name__ = "Integer32"
_FsMIBgp4ExtCommOutgoingFilterStatus_Object = MibTableColumn
fsMIBgp4ExtCommOutgoingFilterStatus = _FsMIBgp4ExtCommOutgoingFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 17, 2, 1, 2),
    _FsMIBgp4ExtCommOutgoingFilterStatus_Type()
)
fsMIBgp4ExtCommOutgoingFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4ExtCommOutgoingFilterStatus.setStatus("current")
_FsMIBgp4ExtCommOutFilterRowStatus_Type = RowStatus
_FsMIBgp4ExtCommOutFilterRowStatus_Object = MibTableColumn
fsMIBgp4ExtCommOutFilterRowStatus = _FsMIBgp4ExtCommOutFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 17, 2, 1, 3),
    _FsMIBgp4ExtCommOutFilterRowStatus_Type()
)
fsMIBgp4ExtCommOutFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4ExtCommOutFilterRowStatus.setStatus("current")
_FsMIBgp4TCPMD5Auth_ObjectIdentity = ObjectIdentity
fsMIBgp4TCPMD5Auth = _FsMIBgp4TCPMD5Auth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 18)
)
_FsMIBgp4TCPMD5AuthTable_Object = MibTable
fsMIBgp4TCPMD5AuthTable = _FsMIBgp4TCPMD5AuthTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 18, 1)
)
if mibBuilder.loadTexts:
    fsMIBgp4TCPMD5AuthTable.setStatus("current")
_FsMIBgp4TCPMD5AuthEntry_Object = MibTableRow
fsMIBgp4TCPMD5AuthEntry = _FsMIBgp4TCPMD5AuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 18, 1, 1)
)
fsMIBgp4TCPMD5AuthEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4TCPMD5AuthPeerType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4TCPMD5AuthPeerAddr"),
)
if mibBuilder.loadTexts:
    fsMIBgp4TCPMD5AuthEntry.setStatus("current")
_FsMIBgp4TCPMD5AuthPeerType_Type = InetAddressType
_FsMIBgp4TCPMD5AuthPeerType_Object = MibTableColumn
fsMIBgp4TCPMD5AuthPeerType = _FsMIBgp4TCPMD5AuthPeerType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 18, 1, 1, 1),
    _FsMIBgp4TCPMD5AuthPeerType_Type()
)
fsMIBgp4TCPMD5AuthPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4TCPMD5AuthPeerType.setStatus("current")


class _FsMIBgp4TCPMD5AuthPeerAddr_Type(OctetString):
    """Custom type fsMIBgp4TCPMD5AuthPeerAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_FsMIBgp4TCPMD5AuthPeerAddr_Type.__name__ = "OctetString"
_FsMIBgp4TCPMD5AuthPeerAddr_Object = MibTableColumn
fsMIBgp4TCPMD5AuthPeerAddr = _FsMIBgp4TCPMD5AuthPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 18, 1, 1, 2),
    _FsMIBgp4TCPMD5AuthPeerAddr_Type()
)
fsMIBgp4TCPMD5AuthPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4TCPMD5AuthPeerAddr.setStatus("current")


class _FsMIBgp4TCPMD5AuthPassword_Type(OctetString):
    """Custom type fsMIBgp4TCPMD5AuthPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_FsMIBgp4TCPMD5AuthPassword_Type.__name__ = "OctetString"
_FsMIBgp4TCPMD5AuthPassword_Object = MibTableColumn
fsMIBgp4TCPMD5AuthPassword = _FsMIBgp4TCPMD5AuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 18, 1, 1, 3),
    _FsMIBgp4TCPMD5AuthPassword_Type()
)
fsMIBgp4TCPMD5AuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4TCPMD5AuthPassword.setStatus("current")


class _FsMIBgp4TCPMD5AuthPwdSet_Type(Integer32):
    """Custom type fsMIBgp4TCPMD5AuthPwdSet based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("clear", 2))
    )


_FsMIBgp4TCPMD5AuthPwdSet_Type.__name__ = "Integer32"
_FsMIBgp4TCPMD5AuthPwdSet_Object = MibTableColumn
fsMIBgp4TCPMD5AuthPwdSet = _FsMIBgp4TCPMD5AuthPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 18, 1, 1, 4),
    _FsMIBgp4TCPMD5AuthPwdSet_Type()
)
fsMIBgp4TCPMD5AuthPwdSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4TCPMD5AuthPwdSet.setStatus("current")
_FsMIBgpAsc_ObjectIdentity = ObjectIdentity
fsMIBgpAsc = _FsMIBgpAsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 19)
)
_FsMIBgpAscConfedPeerTable_Object = MibTable
fsMIBgpAscConfedPeerTable = _FsMIBgpAscConfedPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 19, 1)
)
if mibBuilder.loadTexts:
    fsMIBgpAscConfedPeerTable.setStatus("current")
_FsMIBgpAscConfedPeerEntry_Object = MibTableRow
fsMIBgpAscConfedPeerEntry = _FsMIBgpAscConfedPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 19, 1, 1)
)
fsMIBgpAscConfedPeerEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgpAscConfedPeerASNo"),
)
if mibBuilder.loadTexts:
    fsMIBgpAscConfedPeerEntry.setStatus("current")


class _FsMIBgpAscConfedPeerASNo_Type(Unsigned32):
    """Custom type fsMIBgpAscConfedPeerASNo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsMIBgpAscConfedPeerASNo_Type.__name__ = "Unsigned32"
_FsMIBgpAscConfedPeerASNo_Object = MibTableColumn
fsMIBgpAscConfedPeerASNo = _FsMIBgpAscConfedPeerASNo_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 19, 1, 1, 1),
    _FsMIBgpAscConfedPeerASNo_Type()
)
fsMIBgpAscConfedPeerASNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgpAscConfedPeerASNo.setStatus("current")


class _FsMIBgpAscConfedPeerStatus_Type(Integer32):
    """Custom type fsMIBgpAscConfedPeerStatus based on Integer32"""
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


_FsMIBgpAscConfedPeerStatus_Type.__name__ = "Integer32"
_FsMIBgpAscConfedPeerStatus_Object = MibTableColumn
fsMIBgpAscConfedPeerStatus = _FsMIBgpAscConfedPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 19, 1, 1, 2),
    _FsMIBgpAscConfedPeerStatus_Type()
)
fsMIBgpAscConfedPeerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgpAscConfedPeerStatus.setStatus("current")
_FsMIBgp4MpeBgpPeerTable_Object = MibTable
fsMIBgp4MpeBgpPeerTable = _FsMIBgp4MpeBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeBgpPeerTable.setStatus("current")
_FsMIBgp4MpeBgpPeerEntry_Object = MibTableRow
fsMIBgp4MpeBgpPeerEntry = _FsMIBgp4MpeBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1)
)
fsMIBgp4MpeBgpPeerEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpebgpPeerRemoteAddrType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpebgpPeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeBgpPeerEntry.setStatus("current")
_FsMIBgp4mpebgpPeerIdentifier_Type = InetAddress
_FsMIBgp4mpebgpPeerIdentifier_Object = MibTableColumn
fsMIBgp4mpebgpPeerIdentifier = _FsMIBgp4mpebgpPeerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 1),
    _FsMIBgp4mpebgpPeerIdentifier_Type()
)
fsMIBgp4mpebgpPeerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerIdentifier.setStatus("current")
_FsMIBgp4mpebgpPeerRemoteAddrType_Type = InetAddressType
_FsMIBgp4mpebgpPeerRemoteAddrType_Object = MibTableColumn
fsMIBgp4mpebgpPeerRemoteAddrType = _FsMIBgp4mpebgpPeerRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 2),
    _FsMIBgp4mpebgpPeerRemoteAddrType_Type()
)
fsMIBgp4mpebgpPeerRemoteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerRemoteAddrType.setStatus("current")


class _FsMIBgp4mpebgpPeerLocalAs_Type(Unsigned32):
    """Custom type fsMIBgp4mpebgpPeerLocalAs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIBgp4mpebgpPeerLocalAs_Type.__name__ = "Unsigned32"
_FsMIBgp4mpebgpPeerLocalAs_Object = MibTableColumn
fsMIBgp4mpebgpPeerLocalAs = _FsMIBgp4mpebgpPeerLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 3),
    _FsMIBgp4mpebgpPeerLocalAs_Type()
)
fsMIBgp4mpebgpPeerLocalAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerLocalAs.setStatus("current")


class _FsMIBgp4mpebgpPeerState_Type(Integer32):
    """Custom type fsMIBgp4mpebgpPeerState based on Integer32"""
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
        *(("idle", 1),
          ("connect", 2),
          ("active", 3),
          ("opensent", 4),
          ("openconfirm", 5),
          ("established", 6))
    )


_FsMIBgp4mpebgpPeerState_Type.__name__ = "Integer32"
_FsMIBgp4mpebgpPeerState_Object = MibTableColumn
fsMIBgp4mpebgpPeerState = _FsMIBgp4mpebgpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 4),
    _FsMIBgp4mpebgpPeerState_Type()
)
fsMIBgp4mpebgpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerState.setStatus("current")


class _FsMIBgp4mpebgpPeerAdminStatus_Type(Integer32):
    """Custom type fsMIBgp4mpebgpPeerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stop", 1),
          ("start", 2),
          ("autostart", 3))
    )


_FsMIBgp4mpebgpPeerAdminStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpebgpPeerAdminStatus_Object = MibTableColumn
fsMIBgp4mpebgpPeerAdminStatus = _FsMIBgp4mpebgpPeerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 5),
    _FsMIBgp4mpebgpPeerAdminStatus_Type()
)
fsMIBgp4mpebgpPeerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerAdminStatus.setStatus("current")
_FsMIBgp4mpebgpPeerNegotiatedVersion_Type = Integer32
_FsMIBgp4mpebgpPeerNegotiatedVersion_Object = MibTableColumn
fsMIBgp4mpebgpPeerNegotiatedVersion = _FsMIBgp4mpebgpPeerNegotiatedVersion_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 6),
    _FsMIBgp4mpebgpPeerNegotiatedVersion_Type()
)
fsMIBgp4mpebgpPeerNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerNegotiatedVersion.setStatus("current")
_FsMIBgp4mpebgpPeerLocalAddr_Type = InetAddress
_FsMIBgp4mpebgpPeerLocalAddr_Object = MibTableColumn
fsMIBgp4mpebgpPeerLocalAddr = _FsMIBgp4mpebgpPeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 7),
    _FsMIBgp4mpebgpPeerLocalAddr_Type()
)
fsMIBgp4mpebgpPeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerLocalAddr.setStatus("current")


class _FsMIBgp4mpebgpPeerLocalPort_Type(Integer32):
    """Custom type fsMIBgp4mpebgpPeerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIBgp4mpebgpPeerLocalPort_Type.__name__ = "Integer32"
_FsMIBgp4mpebgpPeerLocalPort_Object = MibTableColumn
fsMIBgp4mpebgpPeerLocalPort = _FsMIBgp4mpebgpPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 8),
    _FsMIBgp4mpebgpPeerLocalPort_Type()
)
fsMIBgp4mpebgpPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerLocalPort.setStatus("current")
_FsMIBgp4mpebgpPeerRemoteAddr_Type = InetAddress
_FsMIBgp4mpebgpPeerRemoteAddr_Object = MibTableColumn
fsMIBgp4mpebgpPeerRemoteAddr = _FsMIBgp4mpebgpPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 9),
    _FsMIBgp4mpebgpPeerRemoteAddr_Type()
)
fsMIBgp4mpebgpPeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerRemoteAddr.setStatus("current")


class _FsMIBgp4mpebgpPeerRemotePort_Type(Integer32):
    """Custom type fsMIBgp4mpebgpPeerRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIBgp4mpebgpPeerRemotePort_Type.__name__ = "Integer32"
_FsMIBgp4mpebgpPeerRemotePort_Object = MibTableColumn
fsMIBgp4mpebgpPeerRemotePort = _FsMIBgp4mpebgpPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 10),
    _FsMIBgp4mpebgpPeerRemotePort_Type()
)
fsMIBgp4mpebgpPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerRemotePort.setStatus("current")


class _FsMIBgp4mpebgpPeerRemoteAs_Type(Unsigned32):
    """Custom type fsMIBgp4mpebgpPeerRemoteAs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIBgp4mpebgpPeerRemoteAs_Type.__name__ = "Unsigned32"
_FsMIBgp4mpebgpPeerRemoteAs_Object = MibTableColumn
fsMIBgp4mpebgpPeerRemoteAs = _FsMIBgp4mpebgpPeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 11),
    _FsMIBgp4mpebgpPeerRemoteAs_Type()
)
fsMIBgp4mpebgpPeerRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerRemoteAs.setStatus("current")
_FsMIBgp4mpebgpPeerInUpdates_Type = Counter32
_FsMIBgp4mpebgpPeerInUpdates_Object = MibTableColumn
fsMIBgp4mpebgpPeerInUpdates = _FsMIBgp4mpebgpPeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 12),
    _FsMIBgp4mpebgpPeerInUpdates_Type()
)
fsMIBgp4mpebgpPeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerInUpdates.setStatus("current")
_FsMIBgp4mpebgpPeerOutUpdates_Type = Counter32
_FsMIBgp4mpebgpPeerOutUpdates_Object = MibTableColumn
fsMIBgp4mpebgpPeerOutUpdates = _FsMIBgp4mpebgpPeerOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 13),
    _FsMIBgp4mpebgpPeerOutUpdates_Type()
)
fsMIBgp4mpebgpPeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerOutUpdates.setStatus("current")
_FsMIBgp4mpebgpPeerInTotalMessages_Type = Counter32
_FsMIBgp4mpebgpPeerInTotalMessages_Object = MibTableColumn
fsMIBgp4mpebgpPeerInTotalMessages = _FsMIBgp4mpebgpPeerInTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 14),
    _FsMIBgp4mpebgpPeerInTotalMessages_Type()
)
fsMIBgp4mpebgpPeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerInTotalMessages.setStatus("current")
_FsMIBgp4mpebgpPeerOutTotalMessages_Type = Counter32
_FsMIBgp4mpebgpPeerOutTotalMessages_Object = MibTableColumn
fsMIBgp4mpebgpPeerOutTotalMessages = _FsMIBgp4mpebgpPeerOutTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 15),
    _FsMIBgp4mpebgpPeerOutTotalMessages_Type()
)
fsMIBgp4mpebgpPeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerOutTotalMessages.setStatus("current")


class _FsMIBgp4mpebgpPeerLastError_Type(OctetString):
    """Custom type fsMIBgp4mpebgpPeerLastError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_FsMIBgp4mpebgpPeerLastError_Type.__name__ = "OctetString"
_FsMIBgp4mpebgpPeerLastError_Object = MibTableColumn
fsMIBgp4mpebgpPeerLastError = _FsMIBgp4mpebgpPeerLastError_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 16),
    _FsMIBgp4mpebgpPeerLastError_Type()
)
fsMIBgp4mpebgpPeerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerLastError.setStatus("current")
_FsMIBgp4mpebgpPeerFsmEstablishedTransitions_Type = Counter32
_FsMIBgp4mpebgpPeerFsmEstablishedTransitions_Object = MibTableColumn
fsMIBgp4mpebgpPeerFsmEstablishedTransitions = _FsMIBgp4mpebgpPeerFsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 17),
    _FsMIBgp4mpebgpPeerFsmEstablishedTransitions_Type()
)
fsMIBgp4mpebgpPeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerFsmEstablishedTransitions.setStatus("current")
_FsMIBgp4mpebgpPeerFsmEstablishedTime_Type = Gauge32
_FsMIBgp4mpebgpPeerFsmEstablishedTime_Object = MibTableColumn
fsMIBgp4mpebgpPeerFsmEstablishedTime = _FsMIBgp4mpebgpPeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 18),
    _FsMIBgp4mpebgpPeerFsmEstablishedTime_Type()
)
fsMIBgp4mpebgpPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerFsmEstablishedTime.setStatus("current")


class _FsMIBgp4mpebgpPeerConnectRetryInterval_Type(Integer32):
    """Custom type fsMIBgp4mpebgpPeerConnectRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIBgp4mpebgpPeerConnectRetryInterval_Type.__name__ = "Integer32"
_FsMIBgp4mpebgpPeerConnectRetryInterval_Object = MibTableColumn
fsMIBgp4mpebgpPeerConnectRetryInterval = _FsMIBgp4mpebgpPeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 19),
    _FsMIBgp4mpebgpPeerConnectRetryInterval_Type()
)
fsMIBgp4mpebgpPeerConnectRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerConnectRetryInterval.setStatus("current")


class _FsMIBgp4mpebgpPeerHoldTime_Type(Integer32):
    """Custom type fsMIBgp4mpebgpPeerHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_FsMIBgp4mpebgpPeerHoldTime_Type.__name__ = "Integer32"
_FsMIBgp4mpebgpPeerHoldTime_Object = MibTableColumn
fsMIBgp4mpebgpPeerHoldTime = _FsMIBgp4mpebgpPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 20),
    _FsMIBgp4mpebgpPeerHoldTime_Type()
)
fsMIBgp4mpebgpPeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerHoldTime.setStatus("current")


class _FsMIBgp4mpebgpPeerKeepAlive_Type(Integer32):
    """Custom type fsMIBgp4mpebgpPeerKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_FsMIBgp4mpebgpPeerKeepAlive_Type.__name__ = "Integer32"
_FsMIBgp4mpebgpPeerKeepAlive_Object = MibTableColumn
fsMIBgp4mpebgpPeerKeepAlive = _FsMIBgp4mpebgpPeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 21),
    _FsMIBgp4mpebgpPeerKeepAlive_Type()
)
fsMIBgp4mpebgpPeerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerKeepAlive.setStatus("current")


class _FsMIBgp4mpebgpPeerHoldTimeConfigured_Type(Integer32):
    """Custom type fsMIBgp4mpebgpPeerHoldTimeConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_FsMIBgp4mpebgpPeerHoldTimeConfigured_Type.__name__ = "Integer32"
_FsMIBgp4mpebgpPeerHoldTimeConfigured_Object = MibTableColumn
fsMIBgp4mpebgpPeerHoldTimeConfigured = _FsMIBgp4mpebgpPeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 22),
    _FsMIBgp4mpebgpPeerHoldTimeConfigured_Type()
)
fsMIBgp4mpebgpPeerHoldTimeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerHoldTimeConfigured.setStatus("current")


class _FsMIBgp4mpebgpPeerKeepAliveConfigured_Type(Integer32):
    """Custom type fsMIBgp4mpebgpPeerKeepAliveConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_FsMIBgp4mpebgpPeerKeepAliveConfigured_Type.__name__ = "Integer32"
_FsMIBgp4mpebgpPeerKeepAliveConfigured_Object = MibTableColumn
fsMIBgp4mpebgpPeerKeepAliveConfigured = _FsMIBgp4mpebgpPeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 23),
    _FsMIBgp4mpebgpPeerKeepAliveConfigured_Type()
)
fsMIBgp4mpebgpPeerKeepAliveConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerKeepAliveConfigured.setStatus("current")


class _FsMIBgp4mpebgpPeerMinASOriginationInterval_Type(Integer32):
    """Custom type fsMIBgp4mpebgpPeerMinASOriginationInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIBgp4mpebgpPeerMinASOriginationInterval_Type.__name__ = "Integer32"
_FsMIBgp4mpebgpPeerMinASOriginationInterval_Object = MibTableColumn
fsMIBgp4mpebgpPeerMinASOriginationInterval = _FsMIBgp4mpebgpPeerMinASOriginationInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 24),
    _FsMIBgp4mpebgpPeerMinASOriginationInterval_Type()
)
fsMIBgp4mpebgpPeerMinASOriginationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerMinASOriginationInterval.setStatus("current")


class _FsMIBgp4mpebgpPeerMinRouteAdvertisementInterval_Type(Integer32):
    """Custom type fsMIBgp4mpebgpPeerMinRouteAdvertisementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIBgp4mpebgpPeerMinRouteAdvertisementInterval_Type.__name__ = "Integer32"
_FsMIBgp4mpebgpPeerMinRouteAdvertisementInterval_Object = MibTableColumn
fsMIBgp4mpebgpPeerMinRouteAdvertisementInterval = _FsMIBgp4mpebgpPeerMinRouteAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 25),
    _FsMIBgp4mpebgpPeerMinRouteAdvertisementInterval_Type()
)
fsMIBgp4mpebgpPeerMinRouteAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerMinRouteAdvertisementInterval.setStatus("current")
_FsMIBgp4mpebgpPeerInUpdateElapsedTime_Type = Gauge32
_FsMIBgp4mpebgpPeerInUpdateElapsedTime_Object = MibTableColumn
fsMIBgp4mpebgpPeerInUpdateElapsedTime = _FsMIBgp4mpebgpPeerInUpdateElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 26),
    _FsMIBgp4mpebgpPeerInUpdateElapsedTime_Type()
)
fsMIBgp4mpebgpPeerInUpdateElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerInUpdateElapsedTime.setStatus("current")


class _FsMIBgp4mpebgpPeerEndOfRIBMarkerSentStatus_Type(Integer32):
    """Custom type fsMIBgp4mpebgpPeerEndOfRIBMarkerSentStatus based on Integer32"""
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
          ("true", 1),
          ("false", 2))
    )


_FsMIBgp4mpebgpPeerEndOfRIBMarkerSentStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpebgpPeerEndOfRIBMarkerSentStatus_Object = MibTableColumn
fsMIBgp4mpebgpPeerEndOfRIBMarkerSentStatus = _FsMIBgp4mpebgpPeerEndOfRIBMarkerSentStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 27),
    _FsMIBgp4mpebgpPeerEndOfRIBMarkerSentStatus_Type()
)
fsMIBgp4mpebgpPeerEndOfRIBMarkerSentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerEndOfRIBMarkerSentStatus.setStatus("current")


class _FsMIBgp4mpebgpPeerEndOfRIBMarkerReceivedStatus_Type(Integer32):
    """Custom type fsMIBgp4mpebgpPeerEndOfRIBMarkerReceivedStatus based on Integer32"""
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
          ("true", 1),
          ("false", 2))
    )


_FsMIBgp4mpebgpPeerEndOfRIBMarkerReceivedStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpebgpPeerEndOfRIBMarkerReceivedStatus_Object = MibTableColumn
fsMIBgp4mpebgpPeerEndOfRIBMarkerReceivedStatus = _FsMIBgp4mpebgpPeerEndOfRIBMarkerReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 28),
    _FsMIBgp4mpebgpPeerEndOfRIBMarkerReceivedStatus_Type()
)
fsMIBgp4mpebgpPeerEndOfRIBMarkerReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerEndOfRIBMarkerReceivedStatus.setStatus("current")


class _FsMIBgp4mpebgpPeerRestartMode_Type(Integer32):
    """Custom type fsMIBgp4mpebgpPeerRestartMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("restarting", 1),
          ("receiving", 2),
          ("none", 3))
    )


_FsMIBgp4mpebgpPeerRestartMode_Type.__name__ = "Integer32"
_FsMIBgp4mpebgpPeerRestartMode_Object = MibTableColumn
fsMIBgp4mpebgpPeerRestartMode = _FsMIBgp4mpebgpPeerRestartMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 29),
    _FsMIBgp4mpebgpPeerRestartMode_Type()
)
fsMIBgp4mpebgpPeerRestartMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerRestartMode.setStatus("current")


class _FsMIBgp4mpePeerRestartTimeInterval_Type(Integer32):
    """Custom type fsMIBgp4mpePeerRestartTimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FsMIBgp4mpePeerRestartTimeInterval_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerRestartTimeInterval_Object = MibTableColumn
fsMIBgp4mpePeerRestartTimeInterval = _FsMIBgp4mpePeerRestartTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 30),
    _FsMIBgp4mpePeerRestartTimeInterval_Type()
)
fsMIBgp4mpePeerRestartTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerRestartTimeInterval.setStatus("current")


class _FsMIBgp4mpePeerAllowAutomaticStart_Type(Integer32):
    """Custom type fsMIBgp4mpePeerAllowAutomaticStart based on Integer32"""
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


_FsMIBgp4mpePeerAllowAutomaticStart_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerAllowAutomaticStart_Object = MibTableColumn
fsMIBgp4mpePeerAllowAutomaticStart = _FsMIBgp4mpePeerAllowAutomaticStart_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 31),
    _FsMIBgp4mpePeerAllowAutomaticStart_Type()
)
fsMIBgp4mpePeerAllowAutomaticStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerAllowAutomaticStart.setStatus("current")


class _FsMIBgp4mpePeerAllowAutomaticStop_Type(Integer32):
    """Custom type fsMIBgp4mpePeerAllowAutomaticStop based on Integer32"""
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


_FsMIBgp4mpePeerAllowAutomaticStop_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerAllowAutomaticStop_Object = MibTableColumn
fsMIBgp4mpePeerAllowAutomaticStop = _FsMIBgp4mpePeerAllowAutomaticStop_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 32),
    _FsMIBgp4mpePeerAllowAutomaticStop_Type()
)
fsMIBgp4mpePeerAllowAutomaticStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerAllowAutomaticStop.setStatus("current")


class _FsMIBgp4mpebgpPeerIdleHoldTimeConfigured_Type(Integer32):
    """Custom type fsMIBgp4mpebgpPeerIdleHoldTimeConfigured based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIBgp4mpebgpPeerIdleHoldTimeConfigured_Type.__name__ = "Integer32"
_FsMIBgp4mpebgpPeerIdleHoldTimeConfigured_Object = MibTableColumn
fsMIBgp4mpebgpPeerIdleHoldTimeConfigured = _FsMIBgp4mpebgpPeerIdleHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 33),
    _FsMIBgp4mpebgpPeerIdleHoldTimeConfigured_Type()
)
fsMIBgp4mpebgpPeerIdleHoldTimeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerIdleHoldTimeConfigured.setStatus("current")


class _FsMIBgp4mpeDampPeerOscillations_Type(Integer32):
    """Custom type fsMIBgp4mpeDampPeerOscillations based on Integer32"""
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


_FsMIBgp4mpeDampPeerOscillations_Type.__name__ = "Integer32"
_FsMIBgp4mpeDampPeerOscillations_Object = MibTableColumn
fsMIBgp4mpeDampPeerOscillations = _FsMIBgp4mpeDampPeerOscillations_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 34),
    _FsMIBgp4mpeDampPeerOscillations_Type()
)
fsMIBgp4mpeDampPeerOscillations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeDampPeerOscillations.setStatus("current")


class _FsMIBgp4mpePeerDelayOpen_Type(Integer32):
    """Custom type fsMIBgp4mpePeerDelayOpen based on Integer32"""
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


_FsMIBgp4mpePeerDelayOpen_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerDelayOpen_Object = MibTableColumn
fsMIBgp4mpePeerDelayOpen = _FsMIBgp4mpePeerDelayOpen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 35),
    _FsMIBgp4mpePeerDelayOpen_Type()
)
fsMIBgp4mpePeerDelayOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerDelayOpen.setStatus("current")


class _FsMIBgp4mpebgpPeerDelayOpenTimeConfigured_Type(Integer32):
    """Custom type fsMIBgp4mpebgpPeerDelayOpenTimeConfigured based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIBgp4mpebgpPeerDelayOpenTimeConfigured_Type.__name__ = "Integer32"
_FsMIBgp4mpebgpPeerDelayOpenTimeConfigured_Object = MibTableColumn
fsMIBgp4mpebgpPeerDelayOpenTimeConfigured = _FsMIBgp4mpebgpPeerDelayOpenTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 36),
    _FsMIBgp4mpebgpPeerDelayOpenTimeConfigured_Type()
)
fsMIBgp4mpebgpPeerDelayOpenTimeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgpPeerDelayOpenTimeConfigured.setStatus("current")


class _FsMIBgp4mpePeerPrefixUpperLimit_Type(Integer32):
    """Custom type fsMIBgp4mpePeerPrefixUpperLimit based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsMIBgp4mpePeerPrefixUpperLimit_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerPrefixUpperLimit_Object = MibTableColumn
fsMIBgp4mpePeerPrefixUpperLimit = _FsMIBgp4mpePeerPrefixUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 37),
    _FsMIBgp4mpePeerPrefixUpperLimit_Type()
)
fsMIBgp4mpePeerPrefixUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerPrefixUpperLimit.setStatus("current")


class _FsMIBgp4mpePeerTcpConnectRetryCnt_Type(Integer32):
    """Custom type fsMIBgp4mpePeerTcpConnectRetryCnt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_FsMIBgp4mpePeerTcpConnectRetryCnt_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerTcpConnectRetryCnt_Object = MibTableColumn
fsMIBgp4mpePeerTcpConnectRetryCnt = _FsMIBgp4mpePeerTcpConnectRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 38),
    _FsMIBgp4mpePeerTcpConnectRetryCnt_Type()
)
fsMIBgp4mpePeerTcpConnectRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerTcpConnectRetryCnt.setStatus("current")


class _FsMIBgp4mpePeerTcpCurrentConnectRetryCnt_Type(Integer32):
    """Custom type fsMIBgp4mpePeerTcpCurrentConnectRetryCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_FsMIBgp4mpePeerTcpCurrentConnectRetryCnt_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerTcpCurrentConnectRetryCnt_Object = MibTableColumn
fsMIBgp4mpePeerTcpCurrentConnectRetryCnt = _FsMIBgp4mpePeerTcpCurrentConnectRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 39),
    _FsMIBgp4mpePeerTcpCurrentConnectRetryCnt_Type()
)
fsMIBgp4mpePeerTcpCurrentConnectRetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerTcpCurrentConnectRetryCnt.setStatus("current")


class _FsMIBgp4mpeIsPeerDamped_Type(Integer32):
    """Custom type fsMIBgp4mpeIsPeerDamped based on Integer32"""
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


_FsMIBgp4mpeIsPeerDamped_Type.__name__ = "Integer32"
_FsMIBgp4mpeIsPeerDamped_Object = MibTableColumn
fsMIBgp4mpeIsPeerDamped = _FsMIBgp4mpeIsPeerDamped_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 40),
    _FsMIBgp4mpeIsPeerDamped_Type()
)
fsMIBgp4mpeIsPeerDamped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeIsPeerDamped.setStatus("current")


class _FsMIBgp4mpePeerSessionAuthStatus_Type(Integer32):
    """Custom type fsMIBgp4mpePeerSessionAuthStatus based on Integer32"""
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
        *(("nosession", 1),
          ("authenticatedMd5", 2),
          ("unauthenticated", 3),
          ("authenticatedTcpAo", 4))
    )


_FsMIBgp4mpePeerSessionAuthStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerSessionAuthStatus_Object = MibTableColumn
fsMIBgp4mpePeerSessionAuthStatus = _FsMIBgp4mpePeerSessionAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 41),
    _FsMIBgp4mpePeerSessionAuthStatus_Type()
)
fsMIBgp4mpePeerSessionAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerSessionAuthStatus.setStatus("current")


class _FsMIBgp4mpePeerTCPAOKeyIdInUse_Type(Integer32):
    """Custom type fsMIBgp4mpePeerTCPAOKeyIdInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIBgp4mpePeerTCPAOKeyIdInUse_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerTCPAOKeyIdInUse_Object = MibTableColumn
fsMIBgp4mpePeerTCPAOKeyIdInUse = _FsMIBgp4mpePeerTCPAOKeyIdInUse_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 42),
    _FsMIBgp4mpePeerTCPAOKeyIdInUse_Type()
)
fsMIBgp4mpePeerTCPAOKeyIdInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerTCPAOKeyIdInUse.setStatus("current")


class _FsMIBgp4mpePeerTCPAOAuthNoMKTDiscard_Type(Integer32):
    """Custom type fsMIBgp4mpePeerTCPAOAuthNoMKTDiscard based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("discard", 2))
    )


_FsMIBgp4mpePeerTCPAOAuthNoMKTDiscard_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerTCPAOAuthNoMKTDiscard_Object = MibTableColumn
fsMIBgp4mpePeerTCPAOAuthNoMKTDiscard = _FsMIBgp4mpePeerTCPAOAuthNoMKTDiscard_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 43),
    _FsMIBgp4mpePeerTCPAOAuthNoMKTDiscard_Type()
)
fsMIBgp4mpePeerTCPAOAuthNoMKTDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerTCPAOAuthNoMKTDiscard.setStatus("current")


class _FsMIBgp4mpePeerTCPAOAuthICMPAccept_Type(Integer32):
    """Custom type fsMIBgp4mpePeerTCPAOAuthICMPAccept based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("ignore", 2))
    )


_FsMIBgp4mpePeerTCPAOAuthICMPAccept_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerTCPAOAuthICMPAccept_Object = MibTableColumn
fsMIBgp4mpePeerTCPAOAuthICMPAccept = _FsMIBgp4mpePeerTCPAOAuthICMPAccept_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 44),
    _FsMIBgp4mpePeerTCPAOAuthICMPAccept_Type()
)
fsMIBgp4mpePeerTCPAOAuthICMPAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerTCPAOAuthICMPAccept.setStatus("current")
_FsMIBgp4mpePeerIpPrefixNameIn_Type = DisplayString
_FsMIBgp4mpePeerIpPrefixNameIn_Object = MibTableColumn
fsMIBgp4mpePeerIpPrefixNameIn = _FsMIBgp4mpePeerIpPrefixNameIn_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 45),
    _FsMIBgp4mpePeerIpPrefixNameIn_Type()
)
fsMIBgp4mpePeerIpPrefixNameIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerIpPrefixNameIn.setStatus("current")
_FsMIBgp4mpePeerIpPrefixNameOut_Type = DisplayString
_FsMIBgp4mpePeerIpPrefixNameOut_Object = MibTableColumn
fsMIBgp4mpePeerIpPrefixNameOut = _FsMIBgp4mpePeerIpPrefixNameOut_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 46),
    _FsMIBgp4mpePeerIpPrefixNameOut_Type()
)
fsMIBgp4mpePeerIpPrefixNameOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerIpPrefixNameOut.setStatus("current")


class _FsMIBgp4mpePeerBfdStatus_Type(Integer32):
    """Custom type fsMIBgp4mpePeerBfdStatus based on Integer32"""
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


_FsMIBgp4mpePeerBfdStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerBfdStatus_Object = MibTableColumn
fsMIBgp4mpePeerBfdStatus = _FsMIBgp4mpePeerBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 47),
    _FsMIBgp4mpePeerBfdStatus_Type()
)
fsMIBgp4mpePeerBfdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerBfdStatus.setStatus("current")


class _FsMIBgp4mpePeerHoldAdvtRoutes_Type(Integer32):
    """Custom type fsMIBgp4mpePeerHoldAdvtRoutes based on Integer32"""
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


_FsMIBgp4mpePeerHoldAdvtRoutes_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerHoldAdvtRoutes_Object = MibTableColumn
fsMIBgp4mpePeerHoldAdvtRoutes = _FsMIBgp4mpePeerHoldAdvtRoutes_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 20, 1, 48),
    _FsMIBgp4mpePeerHoldAdvtRoutes_Type()
)
fsMIBgp4mpePeerHoldAdvtRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerHoldAdvtRoutes.setStatus("current")
_FsMIBgp4MpeBgp4PathAttrTable_Object = MibTable
fsMIBgp4MpeBgp4PathAttrTable = _FsMIBgp4MpeBgp4PathAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeBgp4PathAttrTable.setStatus("current")
_FsMIBgp4MpeBgp4PathAttrEntry_Object = MibTableRow
fsMIBgp4MpeBgp4PathAttrEntry = _FsMIBgp4MpeBgp4PathAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1)
)
fsMIBgp4MpeBgp4PathAttrEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpebgp4PathAttrRouteAfi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpebgp4PathAttrRouteSafi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpebgp4PathAttrIpAddrPrefix"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpebgp4PathAttrIpAddrPrefixLen"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpebgp4PathAttrPeerType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpebgp4PathAttrPeer"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeBgp4PathAttrEntry.setStatus("current")
_FsMIBgp4mpebgp4PathAttrRouteAfi_Type = InetAddressType
_FsMIBgp4mpebgp4PathAttrRouteAfi_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrRouteAfi = _FsMIBgp4mpebgp4PathAttrRouteAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 1),
    _FsMIBgp4mpebgp4PathAttrRouteAfi_Type()
)
fsMIBgp4mpebgp4PathAttrRouteAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrRouteAfi.setStatus("current")
_FsMIBgp4mpebgp4PathAttrRouteSafi_Type = BgpSafi
_FsMIBgp4mpebgp4PathAttrRouteSafi_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrRouteSafi = _FsMIBgp4mpebgp4PathAttrRouteSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 2),
    _FsMIBgp4mpebgp4PathAttrRouteSafi_Type()
)
fsMIBgp4mpebgp4PathAttrRouteSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrRouteSafi.setStatus("current")
_FsMIBgp4mpebgp4PathAttrPeerType_Type = InetAddressType
_FsMIBgp4mpebgp4PathAttrPeerType_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrPeerType = _FsMIBgp4mpebgp4PathAttrPeerType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 3),
    _FsMIBgp4mpebgp4PathAttrPeerType_Type()
)
fsMIBgp4mpebgp4PathAttrPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrPeerType.setStatus("current")
_FsMIBgp4mpebgp4PathAttrPeer_Type = InetAddress
_FsMIBgp4mpebgp4PathAttrPeer_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrPeer = _FsMIBgp4mpebgp4PathAttrPeer_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 4),
    _FsMIBgp4mpebgp4PathAttrPeer_Type()
)
fsMIBgp4mpebgp4PathAttrPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrPeer.setStatus("current")


class _FsMIBgp4mpebgp4PathAttrIpAddrPrefixLen_Type(Integer32):
    """Custom type fsMIBgp4mpebgp4PathAttrIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FsMIBgp4mpebgp4PathAttrIpAddrPrefixLen_Type.__name__ = "Integer32"
_FsMIBgp4mpebgp4PathAttrIpAddrPrefixLen_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrIpAddrPrefixLen = _FsMIBgp4mpebgp4PathAttrIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 5),
    _FsMIBgp4mpebgp4PathAttrIpAddrPrefixLen_Type()
)
fsMIBgp4mpebgp4PathAttrIpAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrIpAddrPrefixLen.setStatus("current")
_FsMIBgp4mpebgp4PathAttrIpAddrPrefix_Type = InetAddress
_FsMIBgp4mpebgp4PathAttrIpAddrPrefix_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrIpAddrPrefix = _FsMIBgp4mpebgp4PathAttrIpAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 6),
    _FsMIBgp4mpebgp4PathAttrIpAddrPrefix_Type()
)
fsMIBgp4mpebgp4PathAttrIpAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrIpAddrPrefix.setStatus("current")


class _FsMIBgp4mpebgp4PathAttrOrigin_Type(Integer32):
    """Custom type fsMIBgp4mpebgp4PathAttrOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igp", 1),
          ("egp", 2),
          ("incomplete", 3))
    )


_FsMIBgp4mpebgp4PathAttrOrigin_Type.__name__ = "Integer32"
_FsMIBgp4mpebgp4PathAttrOrigin_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrOrigin = _FsMIBgp4mpebgp4PathAttrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 7),
    _FsMIBgp4mpebgp4PathAttrOrigin_Type()
)
fsMIBgp4mpebgp4PathAttrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrOrigin.setStatus("current")


class _FsMIBgp4mpebgp4PathAttrASPathSegment_Type(OctetString):
    """Custom type fsMIBgp4mpebgp4PathAttrASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_FsMIBgp4mpebgp4PathAttrASPathSegment_Type.__name__ = "OctetString"
_FsMIBgp4mpebgp4PathAttrASPathSegment_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrASPathSegment = _FsMIBgp4mpebgp4PathAttrASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 8),
    _FsMIBgp4mpebgp4PathAttrASPathSegment_Type()
)
fsMIBgp4mpebgp4PathAttrASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrASPathSegment.setStatus("current")
_FsMIBgp4mpebgp4PathAttrNextHop_Type = InetAddress
_FsMIBgp4mpebgp4PathAttrNextHop_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrNextHop = _FsMIBgp4mpebgp4PathAttrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 9),
    _FsMIBgp4mpebgp4PathAttrNextHop_Type()
)
fsMIBgp4mpebgp4PathAttrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrNextHop.setStatus("current")


class _FsMIBgp4mpebgp4PathAttrMultiExitDisc_Type(Integer32):
    """Custom type fsMIBgp4mpebgp4PathAttrMultiExitDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_FsMIBgp4mpebgp4PathAttrMultiExitDisc_Type.__name__ = "Integer32"
_FsMIBgp4mpebgp4PathAttrMultiExitDisc_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrMultiExitDisc = _FsMIBgp4mpebgp4PathAttrMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 10),
    _FsMIBgp4mpebgp4PathAttrMultiExitDisc_Type()
)
fsMIBgp4mpebgp4PathAttrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrMultiExitDisc.setStatus("current")


class _FsMIBgp4mpebgp4PathAttrLocalPref_Type(Integer32):
    """Custom type fsMIBgp4mpebgp4PathAttrLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_FsMIBgp4mpebgp4PathAttrLocalPref_Type.__name__ = "Integer32"
_FsMIBgp4mpebgp4PathAttrLocalPref_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrLocalPref = _FsMIBgp4mpebgp4PathAttrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 11),
    _FsMIBgp4mpebgp4PathAttrLocalPref_Type()
)
fsMIBgp4mpebgp4PathAttrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrLocalPref.setStatus("current")


class _FsMIBgp4mpebgp4PathAttrAtomicAggregate_Type(Integer32):
    """Custom type fsMIBgp4mpebgp4PathAttrAtomicAggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lessSpecificRrouteNotSelected", 1),
          ("lessSpecificRouteSelected", 2))
    )


_FsMIBgp4mpebgp4PathAttrAtomicAggregate_Type.__name__ = "Integer32"
_FsMIBgp4mpebgp4PathAttrAtomicAggregate_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrAtomicAggregate = _FsMIBgp4mpebgp4PathAttrAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 12),
    _FsMIBgp4mpebgp4PathAttrAtomicAggregate_Type()
)
fsMIBgp4mpebgp4PathAttrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrAtomicAggregate.setStatus("current")


class _FsMIBgp4mpebgp4PathAttrAggregatorAS_Type(Unsigned32):
    """Custom type fsMIBgp4mpebgp4PathAttrAggregatorAS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIBgp4mpebgp4PathAttrAggregatorAS_Type.__name__ = "Unsigned32"
_FsMIBgp4mpebgp4PathAttrAggregatorAS_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrAggregatorAS = _FsMIBgp4mpebgp4PathAttrAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 13),
    _FsMIBgp4mpebgp4PathAttrAggregatorAS_Type()
)
fsMIBgp4mpebgp4PathAttrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrAggregatorAS.setStatus("current")
_FsMIBgp4mpebgp4PathAttrAggregatorAddr_Type = IpAddress
_FsMIBgp4mpebgp4PathAttrAggregatorAddr_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrAggregatorAddr = _FsMIBgp4mpebgp4PathAttrAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 14),
    _FsMIBgp4mpebgp4PathAttrAggregatorAddr_Type()
)
fsMIBgp4mpebgp4PathAttrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrAggregatorAddr.setStatus("current")


class _FsMIBgp4mpebgp4PathAttrCalcLocalPref_Type(Integer32):
    """Custom type fsMIBgp4mpebgp4PathAttrCalcLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_FsMIBgp4mpebgp4PathAttrCalcLocalPref_Type.__name__ = "Integer32"
_FsMIBgp4mpebgp4PathAttrCalcLocalPref_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrCalcLocalPref = _FsMIBgp4mpebgp4PathAttrCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 15),
    _FsMIBgp4mpebgp4PathAttrCalcLocalPref_Type()
)
fsMIBgp4mpebgp4PathAttrCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrCalcLocalPref.setStatus("current")


class _FsMIBgp4mpebgp4PathAttrBest_Type(Integer32):
    """Custom type fsMIBgp4mpebgp4PathAttrBest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonbest", 1),
          ("best", 2),
          ("stale", 3))
    )


_FsMIBgp4mpebgp4PathAttrBest_Type.__name__ = "Integer32"
_FsMIBgp4mpebgp4PathAttrBest_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrBest = _FsMIBgp4mpebgp4PathAttrBest_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 16),
    _FsMIBgp4mpebgp4PathAttrBest_Type()
)
fsMIBgp4mpebgp4PathAttrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrBest.setStatus("current")


class _FsMIBgp4mpebgp4PathAttrCommunity_Type(OctetString):
    """Custom type fsMIBgp4mpebgp4PathAttrCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 800),
    )


_FsMIBgp4mpebgp4PathAttrCommunity_Type.__name__ = "OctetString"
_FsMIBgp4mpebgp4PathAttrCommunity_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrCommunity = _FsMIBgp4mpebgp4PathAttrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 17),
    _FsMIBgp4mpebgp4PathAttrCommunity_Type()
)
fsMIBgp4mpebgp4PathAttrCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrCommunity.setStatus("current")


class _FsMIBgp4mpebgp4PathAttrOriginatorId_Type(OctetString):
    """Custom type fsMIBgp4mpebgp4PathAttrOriginatorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_FsMIBgp4mpebgp4PathAttrOriginatorId_Type.__name__ = "OctetString"
_FsMIBgp4mpebgp4PathAttrOriginatorId_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrOriginatorId = _FsMIBgp4mpebgp4PathAttrOriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 18),
    _FsMIBgp4mpebgp4PathAttrOriginatorId_Type()
)
fsMIBgp4mpebgp4PathAttrOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrOriginatorId.setStatus("current")


class _FsMIBgp4mpebgp4PathAttrClusterList_Type(OctetString):
    """Custom type fsMIBgp4mpebgp4PathAttrClusterList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_FsMIBgp4mpebgp4PathAttrClusterList_Type.__name__ = "OctetString"
_FsMIBgp4mpebgp4PathAttrClusterList_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrClusterList = _FsMIBgp4mpebgp4PathAttrClusterList_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 19),
    _FsMIBgp4mpebgp4PathAttrClusterList_Type()
)
fsMIBgp4mpebgp4PathAttrClusterList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrClusterList.setStatus("current")


class _FsMIBgp4mpebgp4PathAttrExtCommunity_Type(OctetString):
    """Custom type fsMIBgp4mpebgp4PathAttrExtCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 800),
    )


_FsMIBgp4mpebgp4PathAttrExtCommunity_Type.__name__ = "OctetString"
_FsMIBgp4mpebgp4PathAttrExtCommunity_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrExtCommunity = _FsMIBgp4mpebgp4PathAttrExtCommunity_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 20),
    _FsMIBgp4mpebgp4PathAttrExtCommunity_Type()
)
fsMIBgp4mpebgp4PathAttrExtCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrExtCommunity.setStatus("current")


class _FsMIBgp4mpebgp4PathAttrUnknown_Type(OctetString):
    """Custom type fsMIBgp4mpebgp4PathAttrUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsMIBgp4mpebgp4PathAttrUnknown_Type.__name__ = "OctetString"
_FsMIBgp4mpebgp4PathAttrUnknown_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrUnknown = _FsMIBgp4mpebgp4PathAttrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 21),
    _FsMIBgp4mpebgp4PathAttrUnknown_Type()
)
fsMIBgp4mpebgp4PathAttrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrUnknown.setStatus("current")


class _FsMIBgp4mpebgp4PathAttrLabel_Type(OctetString):
    """Custom type fsMIBgp4mpebgp4PathAttrLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_FsMIBgp4mpebgp4PathAttrLabel_Type.__name__ = "OctetString"
_FsMIBgp4mpebgp4PathAttrLabel_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrLabel = _FsMIBgp4mpebgp4PathAttrLabel_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 22),
    _FsMIBgp4mpebgp4PathAttrLabel_Type()
)
fsMIBgp4mpebgp4PathAttrLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrLabel.setStatus("current")


class _FsMIBgp4mpebgp4PathAttrAS4PathSegment_Type(OctetString):
    """Custom type fsMIBgp4mpebgp4PathAttrAS4PathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_FsMIBgp4mpebgp4PathAttrAS4PathSegment_Type.__name__ = "OctetString"
_FsMIBgp4mpebgp4PathAttrAS4PathSegment_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrAS4PathSegment = _FsMIBgp4mpebgp4PathAttrAS4PathSegment_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 23),
    _FsMIBgp4mpebgp4PathAttrAS4PathSegment_Type()
)
fsMIBgp4mpebgp4PathAttrAS4PathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrAS4PathSegment.setStatus("current")


class _FsMIBgp4mpebgp4PathAttrAggregatorAS4_Type(Unsigned32):
    """Custom type fsMIBgp4mpebgp4PathAttrAggregatorAS4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIBgp4mpebgp4PathAttrAggregatorAS4_Type.__name__ = "Unsigned32"
_FsMIBgp4mpebgp4PathAttrAggregatorAS4_Object = MibTableColumn
fsMIBgp4mpebgp4PathAttrAggregatorAS4 = _FsMIBgp4mpebgp4PathAttrAggregatorAS4_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 21, 1, 24),
    _FsMIBgp4mpebgp4PathAttrAggregatorAS4_Type()
)
fsMIBgp4mpebgp4PathAttrAggregatorAS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpebgp4PathAttrAggregatorAS4.setStatus("current")
_FsMIBgp4MpePeerExtTable_Object = MibTable
fsMIBgp4MpePeerExtTable = _FsMIBgp4MpePeerExtTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpePeerExtTable.setStatus("current")
_FsMIBgp4MpePeerExtEntry_Object = MibTableRow
fsMIBgp4MpePeerExtEntry = _FsMIBgp4MpePeerExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1)
)
fsMIBgp4MpePeerExtEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpePeerExtPeerType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpePeerExtPeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpePeerExtEntry.setStatus("current")
_FsMIBgp4mpePeerExtPeerType_Type = InetAddressType
_FsMIBgp4mpePeerExtPeerType_Object = MibTableColumn
fsMIBgp4mpePeerExtPeerType = _FsMIBgp4mpePeerExtPeerType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1, 1),
    _FsMIBgp4mpePeerExtPeerType_Type()
)
fsMIBgp4mpePeerExtPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerExtPeerType.setStatus("current")
_FsMIBgp4mpePeerExtPeerRemoteAddr_Type = InetAddress
_FsMIBgp4mpePeerExtPeerRemoteAddr_Object = MibTableColumn
fsMIBgp4mpePeerExtPeerRemoteAddr = _FsMIBgp4mpePeerExtPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1, 2),
    _FsMIBgp4mpePeerExtPeerRemoteAddr_Type()
)
fsMIBgp4mpePeerExtPeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerExtPeerRemoteAddr.setStatus("current")


class _FsMIBgp4mpePeerExtConfigurePeer_Type(Integer32):
    """Custom type fsMIBgp4mpePeerExtConfigurePeer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_FsMIBgp4mpePeerExtConfigurePeer_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerExtConfigurePeer_Object = MibTableColumn
fsMIBgp4mpePeerExtConfigurePeer = _FsMIBgp4mpePeerExtConfigurePeer_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1, 3),
    _FsMIBgp4mpePeerExtConfigurePeer_Type()
)
fsMIBgp4mpePeerExtConfigurePeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerExtConfigurePeer.setStatus("current")


class _FsMIBgp4mpePeerExtPeerRemoteAs_Type(Unsigned32):
    """Custom type fsMIBgp4mpePeerExtPeerRemoteAs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsMIBgp4mpePeerExtPeerRemoteAs_Type.__name__ = "Unsigned32"
_FsMIBgp4mpePeerExtPeerRemoteAs_Object = MibTableColumn
fsMIBgp4mpePeerExtPeerRemoteAs = _FsMIBgp4mpePeerExtPeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1, 4),
    _FsMIBgp4mpePeerExtPeerRemoteAs_Type()
)
fsMIBgp4mpePeerExtPeerRemoteAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerExtPeerRemoteAs.setStatus("current")


class _FsMIBgp4mpePeerExtEBGPMultiHop_Type(Integer32):
    """Custom type fsMIBgp4mpePeerExtEBGPMultiHop based on Integer32"""
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


_FsMIBgp4mpePeerExtEBGPMultiHop_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerExtEBGPMultiHop_Object = MibTableColumn
fsMIBgp4mpePeerExtEBGPMultiHop = _FsMIBgp4mpePeerExtEBGPMultiHop_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1, 5),
    _FsMIBgp4mpePeerExtEBGPMultiHop_Type()
)
fsMIBgp4mpePeerExtEBGPMultiHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerExtEBGPMultiHop.setStatus("current")


class _FsMIBgp4mpePeerExtEBGPHopLimit_Type(Integer32):
    """Custom type fsMIBgp4mpePeerExtEBGPHopLimit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsMIBgp4mpePeerExtEBGPHopLimit_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerExtEBGPHopLimit_Object = MibTableColumn
fsMIBgp4mpePeerExtEBGPHopLimit = _FsMIBgp4mpePeerExtEBGPHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1, 6),
    _FsMIBgp4mpePeerExtEBGPHopLimit_Type()
)
fsMIBgp4mpePeerExtEBGPHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerExtEBGPHopLimit.setStatus("current")


class _FsMIBgp4mpePeerExtNextHopSelf_Type(Integer32):
    """Custom type fsMIBgp4mpePeerExtNextHopSelf based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("self", 2))
    )


_FsMIBgp4mpePeerExtNextHopSelf_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerExtNextHopSelf_Object = MibTableColumn
fsMIBgp4mpePeerExtNextHopSelf = _FsMIBgp4mpePeerExtNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1, 7),
    _FsMIBgp4mpePeerExtNextHopSelf_Type()
)
fsMIBgp4mpePeerExtNextHopSelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerExtNextHopSelf.setStatus("current")


class _FsMIBgp4mpePeerExtRflClient_Type(Integer32):
    """Custom type fsMIBgp4mpePeerExtRflClient based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonClient", 1),
          ("client", 2))
    )


_FsMIBgp4mpePeerExtRflClient_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerExtRflClient_Object = MibTableColumn
fsMIBgp4mpePeerExtRflClient = _FsMIBgp4mpePeerExtRflClient_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1, 8),
    _FsMIBgp4mpePeerExtRflClient_Type()
)
fsMIBgp4mpePeerExtRflClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerExtRflClient.setStatus("current")


class _FsMIBgp4mpePeerExtTcpSendBufSize_Type(Integer32):
    """Custom type fsMIBgp4mpePeerExtTcpSendBufSize based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 65536),
    )


_FsMIBgp4mpePeerExtTcpSendBufSize_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerExtTcpSendBufSize_Object = MibTableColumn
fsMIBgp4mpePeerExtTcpSendBufSize = _FsMIBgp4mpePeerExtTcpSendBufSize_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1, 9),
    _FsMIBgp4mpePeerExtTcpSendBufSize_Type()
)
fsMIBgp4mpePeerExtTcpSendBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerExtTcpSendBufSize.setStatus("current")


class _FsMIBgp4mpePeerExtTcpRcvBufSize_Type(Integer32):
    """Custom type fsMIBgp4mpePeerExtTcpRcvBufSize based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 65536),
    )


_FsMIBgp4mpePeerExtTcpRcvBufSize_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerExtTcpRcvBufSize_Object = MibTableColumn
fsMIBgp4mpePeerExtTcpRcvBufSize = _FsMIBgp4mpePeerExtTcpRcvBufSize_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1, 10),
    _FsMIBgp4mpePeerExtTcpRcvBufSize_Type()
)
fsMIBgp4mpePeerExtTcpRcvBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerExtTcpRcvBufSize.setStatus("current")
_FsMIBgp4mpePeerExtLclAddress_Type = InetAddress
_FsMIBgp4mpePeerExtLclAddress_Object = MibTableColumn
fsMIBgp4mpePeerExtLclAddress = _FsMIBgp4mpePeerExtLclAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1, 11),
    _FsMIBgp4mpePeerExtLclAddress_Type()
)
fsMIBgp4mpePeerExtLclAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerExtLclAddress.setStatus("current")
_FsMIBgp4mpePeerExtNetworkAddress_Type = InetAddress
_FsMIBgp4mpePeerExtNetworkAddress_Object = MibTableColumn
fsMIBgp4mpePeerExtNetworkAddress = _FsMIBgp4mpePeerExtNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1, 12),
    _FsMIBgp4mpePeerExtNetworkAddress_Type()
)
fsMIBgp4mpePeerExtNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerExtNetworkAddress.setStatus("current")
_FsMIBgp4mpePeerExtGateway_Type = InetAddress
_FsMIBgp4mpePeerExtGateway_Object = MibTableColumn
fsMIBgp4mpePeerExtGateway = _FsMIBgp4mpePeerExtGateway_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1, 13),
    _FsMIBgp4mpePeerExtGateway_Type()
)
fsMIBgp4mpePeerExtGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerExtGateway.setStatus("current")


class _FsMIBgp4mpePeerExtCommSendStatus_Type(Integer32):
    """Custom type fsMIBgp4mpePeerExtCommSendStatus based on Integer32"""
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
        *(("none", 1),
          ("send", 2),
          ("donotsend", 3))
    )


_FsMIBgp4mpePeerExtCommSendStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerExtCommSendStatus_Object = MibTableColumn
fsMIBgp4mpePeerExtCommSendStatus = _FsMIBgp4mpePeerExtCommSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1, 14),
    _FsMIBgp4mpePeerExtCommSendStatus_Type()
)
fsMIBgp4mpePeerExtCommSendStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerExtCommSendStatus.setStatus("current")


class _FsMIBgp4mpePeerExtECommSendStatus_Type(Integer32):
    """Custom type fsMIBgp4mpePeerExtECommSendStatus based on Integer32"""
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
        *(("none", 1),
          ("send", 2),
          ("donotsend", 3))
    )


_FsMIBgp4mpePeerExtECommSendStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerExtECommSendStatus_Object = MibTableColumn
fsMIBgp4mpePeerExtECommSendStatus = _FsMIBgp4mpePeerExtECommSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1, 15),
    _FsMIBgp4mpePeerExtECommSendStatus_Type()
)
fsMIBgp4mpePeerExtECommSendStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerExtECommSendStatus.setStatus("current")


class _FsMIBgp4mpePeerExtPassive_Type(Integer32):
    """Custom type fsMIBgp4mpePeerExtPassive based on Integer32"""
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


_FsMIBgp4mpePeerExtPassive_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerExtPassive_Object = MibTableColumn
fsMIBgp4mpePeerExtPassive = _FsMIBgp4mpePeerExtPassive_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1, 16),
    _FsMIBgp4mpePeerExtPassive_Type()
)
fsMIBgp4mpePeerExtPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerExtPassive.setStatus("current")


class _FsMIBgp4mpePeerExtDefaultOriginate_Type(Integer32):
    """Custom type fsMIBgp4mpePeerExtDefaultOriginate based on Integer32"""
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


_FsMIBgp4mpePeerExtDefaultOriginate_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerExtDefaultOriginate_Object = MibTableColumn
fsMIBgp4mpePeerExtDefaultOriginate = _FsMIBgp4mpePeerExtDefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1, 17),
    _FsMIBgp4mpePeerExtDefaultOriginate_Type()
)
fsMIBgp4mpePeerExtDefaultOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerExtDefaultOriginate.setStatus("current")


class _FsMIBgp4mpePeerExtOverrideCapability_Type(Integer32):
    """Custom type fsMIBgp4mpePeerExtOverrideCapability based on Integer32"""
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


_FsMIBgp4mpePeerExtOverrideCapability_Type.__name__ = "Integer32"
_FsMIBgp4mpePeerExtOverrideCapability_Object = MibTableColumn
fsMIBgp4mpePeerExtOverrideCapability = _FsMIBgp4mpePeerExtOverrideCapability_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 22, 1, 18),
    _FsMIBgp4mpePeerExtOverrideCapability_Type()
)
fsMIBgp4mpePeerExtOverrideCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerExtOverrideCapability.setStatus("current")
_FsMIBgp4MpeMEDTable_Object = MibTable
fsMIBgp4MpeMEDTable = _FsMIBgp4MpeMEDTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 23)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeMEDTable.setStatus("current")
_FsMIBgp4MpeMEDEntry_Object = MibTableRow
fsMIBgp4MpeMEDEntry = _FsMIBgp4MpeMEDEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 23, 1)
)
fsMIBgp4MpeMEDEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeMEDIndex"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeMEDEntry.setStatus("current")


class _FsMIBgp4mpeMEDIndex_Type(Integer32):
    """Custom type fsMIBgp4mpeMEDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsMIBgp4mpeMEDIndex_Type.__name__ = "Integer32"
_FsMIBgp4mpeMEDIndex_Object = MibTableColumn
fsMIBgp4mpeMEDIndex = _FsMIBgp4mpeMEDIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 23, 1, 1),
    _FsMIBgp4mpeMEDIndex_Type()
)
fsMIBgp4mpeMEDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeMEDIndex.setStatus("current")


class _FsMIBgp4mpeMEDAdminStatus_Type(Integer32):
    """Custom type fsMIBgp4mpeMEDAdminStatus based on Integer32"""
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


_FsMIBgp4mpeMEDAdminStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpeMEDAdminStatus_Object = MibTableColumn
fsMIBgp4mpeMEDAdminStatus = _FsMIBgp4mpeMEDAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 23, 1, 2),
    _FsMIBgp4mpeMEDAdminStatus_Type()
)
fsMIBgp4mpeMEDAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeMEDAdminStatus.setStatus("current")


class _FsMIBgp4mpeMEDRemoteAS_Type(Unsigned32):
    """Custom type fsMIBgp4mpeMEDRemoteAS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIBgp4mpeMEDRemoteAS_Type.__name__ = "Unsigned32"
_FsMIBgp4mpeMEDRemoteAS_Object = MibTableColumn
fsMIBgp4mpeMEDRemoteAS = _FsMIBgp4mpeMEDRemoteAS_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 23, 1, 3),
    _FsMIBgp4mpeMEDRemoteAS_Type()
)
fsMIBgp4mpeMEDRemoteAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeMEDRemoteAS.setStatus("current")
_FsMIBgp4mpeMEDIPAddrAfi_Type = InetAddressType
_FsMIBgp4mpeMEDIPAddrAfi_Object = MibTableColumn
fsMIBgp4mpeMEDIPAddrAfi = _FsMIBgp4mpeMEDIPAddrAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 23, 1, 4),
    _FsMIBgp4mpeMEDIPAddrAfi_Type()
)
fsMIBgp4mpeMEDIPAddrAfi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeMEDIPAddrAfi.setStatus("current")
_FsMIBgp4mpeMEDIPAddrSafi_Type = BgpSafi
_FsMIBgp4mpeMEDIPAddrSafi_Object = MibTableColumn
fsMIBgp4mpeMEDIPAddrSafi = _FsMIBgp4mpeMEDIPAddrSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 23, 1, 5),
    _FsMIBgp4mpeMEDIPAddrSafi_Type()
)
fsMIBgp4mpeMEDIPAddrSafi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeMEDIPAddrSafi.setStatus("current")


class _FsMIBgp4mpeMEDIPAddrPrefix_Type(InetAddress):
    """Custom type fsMIBgp4mpeMEDIPAddrPrefix based on InetAddress"""
    defaultHexValue = "00000000"


_FsMIBgp4mpeMEDIPAddrPrefix_Type.__name__ = "InetAddress"
_FsMIBgp4mpeMEDIPAddrPrefix_Object = MibTableColumn
fsMIBgp4mpeMEDIPAddrPrefix = _FsMIBgp4mpeMEDIPAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 23, 1, 6),
    _FsMIBgp4mpeMEDIPAddrPrefix_Type()
)
fsMIBgp4mpeMEDIPAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeMEDIPAddrPrefix.setStatus("current")


class _FsMIBgp4mpeMEDIPAddrPrefixLen_Type(Integer32):
    """Custom type fsMIBgp4mpeMEDIPAddrPrefixLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FsMIBgp4mpeMEDIPAddrPrefixLen_Type.__name__ = "Integer32"
_FsMIBgp4mpeMEDIPAddrPrefixLen_Object = MibTableColumn
fsMIBgp4mpeMEDIPAddrPrefixLen = _FsMIBgp4mpeMEDIPAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 23, 1, 7),
    _FsMIBgp4mpeMEDIPAddrPrefixLen_Type()
)
fsMIBgp4mpeMEDIPAddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeMEDIPAddrPrefixLen.setStatus("current")
_FsMIBgp4mpeMEDIntermediateAS_Type = DisplayString
_FsMIBgp4mpeMEDIntermediateAS_Object = MibTableColumn
fsMIBgp4mpeMEDIntermediateAS = _FsMIBgp4mpeMEDIntermediateAS_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 23, 1, 8),
    _FsMIBgp4mpeMEDIntermediateAS_Type()
)
fsMIBgp4mpeMEDIntermediateAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeMEDIntermediateAS.setStatus("current")


class _FsMIBgp4mpeMEDDirection_Type(Integer32):
    """Custom type fsMIBgp4mpeMEDDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_FsMIBgp4mpeMEDDirection_Type.__name__ = "Integer32"
_FsMIBgp4mpeMEDDirection_Object = MibTableColumn
fsMIBgp4mpeMEDDirection = _FsMIBgp4mpeMEDDirection_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 23, 1, 9),
    _FsMIBgp4mpeMEDDirection_Type()
)
fsMIBgp4mpeMEDDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeMEDDirection.setStatus("current")


class _FsMIBgp4mpeMEDValue_Type(Unsigned32):
    """Custom type fsMIBgp4mpeMEDValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIBgp4mpeMEDValue_Type.__name__ = "Unsigned32"
_FsMIBgp4mpeMEDValue_Object = MibTableColumn
fsMIBgp4mpeMEDValue = _FsMIBgp4mpeMEDValue_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 23, 1, 10),
    _FsMIBgp4mpeMEDValue_Type()
)
fsMIBgp4mpeMEDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeMEDValue.setStatus("current")


class _FsMIBgp4mpeMEDPreference_Type(Integer32):
    """Custom type fsMIBgp4mpeMEDPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FsMIBgp4mpeMEDPreference_Type.__name__ = "Integer32"
_FsMIBgp4mpeMEDPreference_Object = MibTableColumn
fsMIBgp4mpeMEDPreference = _FsMIBgp4mpeMEDPreference_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 23, 1, 11),
    _FsMIBgp4mpeMEDPreference_Type()
)
fsMIBgp4mpeMEDPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeMEDPreference.setStatus("current")


class _FsMIBgp4mpeMEDVrfName_Type(DisplayString):
    """Custom type fsMIBgp4mpeMEDVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsMIBgp4mpeMEDVrfName_Type.__name__ = "DisplayString"
_FsMIBgp4mpeMEDVrfName_Object = MibTableColumn
fsMIBgp4mpeMEDVrfName = _FsMIBgp4mpeMEDVrfName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 23, 1, 12),
    _FsMIBgp4mpeMEDVrfName_Type()
)
fsMIBgp4mpeMEDVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeMEDVrfName.setStatus("current")
_FsMIBgp4MpeLocalPrefTable_Object = MibTable
fsMIBgp4MpeLocalPrefTable = _FsMIBgp4MpeLocalPrefTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 24)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeLocalPrefTable.setStatus("current")
_FsMIBgp4MpeLocalPrefEntry_Object = MibTableRow
fsMIBgp4MpeLocalPrefEntry = _FsMIBgp4MpeLocalPrefEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 24, 1)
)
fsMIBgp4MpeLocalPrefEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeLocalPrefIndex"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeLocalPrefEntry.setStatus("current")


class _FsMIBgp4mpeLocalPrefIndex_Type(Integer32):
    """Custom type fsMIBgp4mpeLocalPrefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsMIBgp4mpeLocalPrefIndex_Type.__name__ = "Integer32"
_FsMIBgp4mpeLocalPrefIndex_Object = MibTableColumn
fsMIBgp4mpeLocalPrefIndex = _FsMIBgp4mpeLocalPrefIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 24, 1, 1),
    _FsMIBgp4mpeLocalPrefIndex_Type()
)
fsMIBgp4mpeLocalPrefIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeLocalPrefIndex.setStatus("current")


class _FsMIBgp4mpeLocalPrefAdminStatus_Type(Integer32):
    """Custom type fsMIBgp4mpeLocalPrefAdminStatus based on Integer32"""
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


_FsMIBgp4mpeLocalPrefAdminStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpeLocalPrefAdminStatus_Object = MibTableColumn
fsMIBgp4mpeLocalPrefAdminStatus = _FsMIBgp4mpeLocalPrefAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 24, 1, 2),
    _FsMIBgp4mpeLocalPrefAdminStatus_Type()
)
fsMIBgp4mpeLocalPrefAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeLocalPrefAdminStatus.setStatus("current")


class _FsMIBgp4mpeLocalPrefRemoteAS_Type(Unsigned32):
    """Custom type fsMIBgp4mpeLocalPrefRemoteAS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIBgp4mpeLocalPrefRemoteAS_Type.__name__ = "Unsigned32"
_FsMIBgp4mpeLocalPrefRemoteAS_Object = MibTableColumn
fsMIBgp4mpeLocalPrefRemoteAS = _FsMIBgp4mpeLocalPrefRemoteAS_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 24, 1, 3),
    _FsMIBgp4mpeLocalPrefRemoteAS_Type()
)
fsMIBgp4mpeLocalPrefRemoteAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeLocalPrefRemoteAS.setStatus("current")
_FsMIBgp4mpeLocalPrefIPAddrAfi_Type = InetAddressType
_FsMIBgp4mpeLocalPrefIPAddrAfi_Object = MibTableColumn
fsMIBgp4mpeLocalPrefIPAddrAfi = _FsMIBgp4mpeLocalPrefIPAddrAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 24, 1, 4),
    _FsMIBgp4mpeLocalPrefIPAddrAfi_Type()
)
fsMIBgp4mpeLocalPrefIPAddrAfi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeLocalPrefIPAddrAfi.setStatus("current")
_FsMIBgp4mpeLocalPrefIPAddrSafi_Type = BgpSafi
_FsMIBgp4mpeLocalPrefIPAddrSafi_Object = MibTableColumn
fsMIBgp4mpeLocalPrefIPAddrSafi = _FsMIBgp4mpeLocalPrefIPAddrSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 24, 1, 5),
    _FsMIBgp4mpeLocalPrefIPAddrSafi_Type()
)
fsMIBgp4mpeLocalPrefIPAddrSafi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeLocalPrefIPAddrSafi.setStatus("current")


class _FsMIBgp4mpeLocalPrefIPAddrPrefix_Type(InetAddress):
    """Custom type fsMIBgp4mpeLocalPrefIPAddrPrefix based on InetAddress"""
    defaultHexValue = "00000000"


_FsMIBgp4mpeLocalPrefIPAddrPrefix_Type.__name__ = "InetAddress"
_FsMIBgp4mpeLocalPrefIPAddrPrefix_Object = MibTableColumn
fsMIBgp4mpeLocalPrefIPAddrPrefix = _FsMIBgp4mpeLocalPrefIPAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 24, 1, 6),
    _FsMIBgp4mpeLocalPrefIPAddrPrefix_Type()
)
fsMIBgp4mpeLocalPrefIPAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeLocalPrefIPAddrPrefix.setStatus("current")


class _FsMIBgp4mpeLocalPrefIPAddrPrefixLen_Type(Integer32):
    """Custom type fsMIBgp4mpeLocalPrefIPAddrPrefixLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FsMIBgp4mpeLocalPrefIPAddrPrefixLen_Type.__name__ = "Integer32"
_FsMIBgp4mpeLocalPrefIPAddrPrefixLen_Object = MibTableColumn
fsMIBgp4mpeLocalPrefIPAddrPrefixLen = _FsMIBgp4mpeLocalPrefIPAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 24, 1, 7),
    _FsMIBgp4mpeLocalPrefIPAddrPrefixLen_Type()
)
fsMIBgp4mpeLocalPrefIPAddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeLocalPrefIPAddrPrefixLen.setStatus("current")
_FsMIBgp4mpeLocalPrefIntermediateAS_Type = DisplayString
_FsMIBgp4mpeLocalPrefIntermediateAS_Object = MibTableColumn
fsMIBgp4mpeLocalPrefIntermediateAS = _FsMIBgp4mpeLocalPrefIntermediateAS_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 24, 1, 8),
    _FsMIBgp4mpeLocalPrefIntermediateAS_Type()
)
fsMIBgp4mpeLocalPrefIntermediateAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeLocalPrefIntermediateAS.setStatus("current")


class _FsMIBgp4mpeLocalPrefDirection_Type(Integer32):
    """Custom type fsMIBgp4mpeLocalPrefDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_FsMIBgp4mpeLocalPrefDirection_Type.__name__ = "Integer32"
_FsMIBgp4mpeLocalPrefDirection_Object = MibTableColumn
fsMIBgp4mpeLocalPrefDirection = _FsMIBgp4mpeLocalPrefDirection_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 24, 1, 9),
    _FsMIBgp4mpeLocalPrefDirection_Type()
)
fsMIBgp4mpeLocalPrefDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeLocalPrefDirection.setStatus("current")


class _FsMIBgp4mpeLocalPrefValue_Type(Unsigned32):
    """Custom type fsMIBgp4mpeLocalPrefValue based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIBgp4mpeLocalPrefValue_Type.__name__ = "Unsigned32"
_FsMIBgp4mpeLocalPrefValue_Object = MibTableColumn
fsMIBgp4mpeLocalPrefValue = _FsMIBgp4mpeLocalPrefValue_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 24, 1, 10),
    _FsMIBgp4mpeLocalPrefValue_Type()
)
fsMIBgp4mpeLocalPrefValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeLocalPrefValue.setStatus("current")


class _FsMIBgp4mpeLocalPrefPreference_Type(Integer32):
    """Custom type fsMIBgp4mpeLocalPrefPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_FsMIBgp4mpeLocalPrefPreference_Type.__name__ = "Integer32"
_FsMIBgp4mpeLocalPrefPreference_Object = MibTableColumn
fsMIBgp4mpeLocalPrefPreference = _FsMIBgp4mpeLocalPrefPreference_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 24, 1, 11),
    _FsMIBgp4mpeLocalPrefPreference_Type()
)
fsMIBgp4mpeLocalPrefPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeLocalPrefPreference.setStatus("current")


class _FsMIBgp4mpeLocalPrefVrfName_Type(DisplayString):
    """Custom type fsMIBgp4mpeLocalPrefVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsMIBgp4mpeLocalPrefVrfName_Type.__name__ = "DisplayString"
_FsMIBgp4mpeLocalPrefVrfName_Object = MibTableColumn
fsMIBgp4mpeLocalPrefVrfName = _FsMIBgp4mpeLocalPrefVrfName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 24, 1, 12),
    _FsMIBgp4mpeLocalPrefVrfName_Type()
)
fsMIBgp4mpeLocalPrefVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeLocalPrefVrfName.setStatus("current")
_FsMIBgp4MpeUpdateFilterTable_Object = MibTable
fsMIBgp4MpeUpdateFilterTable = _FsMIBgp4MpeUpdateFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 25)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeUpdateFilterTable.setStatus("current")
_FsMIBgp4MpeUpdateFilterEntry_Object = MibTableRow
fsMIBgp4MpeUpdateFilterEntry = _FsMIBgp4MpeUpdateFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 25, 1)
)
fsMIBgp4MpeUpdateFilterEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeUpdateFilterIndex"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeUpdateFilterEntry.setStatus("current")


class _FsMIBgp4mpeUpdateFilterIndex_Type(Integer32):
    """Custom type fsMIBgp4mpeUpdateFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsMIBgp4mpeUpdateFilterIndex_Type.__name__ = "Integer32"
_FsMIBgp4mpeUpdateFilterIndex_Object = MibTableColumn
fsMIBgp4mpeUpdateFilterIndex = _FsMIBgp4mpeUpdateFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 25, 1, 1),
    _FsMIBgp4mpeUpdateFilterIndex_Type()
)
fsMIBgp4mpeUpdateFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeUpdateFilterIndex.setStatus("current")


class _FsMIBgp4mpeUpdateFilterAdminStatus_Type(Integer32):
    """Custom type fsMIBgp4mpeUpdateFilterAdminStatus based on Integer32"""
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


_FsMIBgp4mpeUpdateFilterAdminStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpeUpdateFilterAdminStatus_Object = MibTableColumn
fsMIBgp4mpeUpdateFilterAdminStatus = _FsMIBgp4mpeUpdateFilterAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 25, 1, 2),
    _FsMIBgp4mpeUpdateFilterAdminStatus_Type()
)
fsMIBgp4mpeUpdateFilterAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeUpdateFilterAdminStatus.setStatus("current")


class _FsMIBgp4mpeUpdateFilterRemoteAS_Type(Unsigned32):
    """Custom type fsMIBgp4mpeUpdateFilterRemoteAS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIBgp4mpeUpdateFilterRemoteAS_Type.__name__ = "Unsigned32"
_FsMIBgp4mpeUpdateFilterRemoteAS_Object = MibTableColumn
fsMIBgp4mpeUpdateFilterRemoteAS = _FsMIBgp4mpeUpdateFilterRemoteAS_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 25, 1, 3),
    _FsMIBgp4mpeUpdateFilterRemoteAS_Type()
)
fsMIBgp4mpeUpdateFilterRemoteAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeUpdateFilterRemoteAS.setStatus("current")
_FsMIBgp4mpeUpdateFilterIPAddrAfi_Type = InetAddressType
_FsMIBgp4mpeUpdateFilterIPAddrAfi_Object = MibTableColumn
fsMIBgp4mpeUpdateFilterIPAddrAfi = _FsMIBgp4mpeUpdateFilterIPAddrAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 25, 1, 4),
    _FsMIBgp4mpeUpdateFilterIPAddrAfi_Type()
)
fsMIBgp4mpeUpdateFilterIPAddrAfi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeUpdateFilterIPAddrAfi.setStatus("current")
_FsMIBgp4mpeUpdateFilterIPAddrSafi_Type = BgpSafi
_FsMIBgp4mpeUpdateFilterIPAddrSafi_Object = MibTableColumn
fsMIBgp4mpeUpdateFilterIPAddrSafi = _FsMIBgp4mpeUpdateFilterIPAddrSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 25, 1, 5),
    _FsMIBgp4mpeUpdateFilterIPAddrSafi_Type()
)
fsMIBgp4mpeUpdateFilterIPAddrSafi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeUpdateFilterIPAddrSafi.setStatus("current")


class _FsMIBgp4mpeUpdateFilterIPAddrPrefix_Type(InetAddress):
    """Custom type fsMIBgp4mpeUpdateFilterIPAddrPrefix based on InetAddress"""
    defaultHexValue = "00000000"


_FsMIBgp4mpeUpdateFilterIPAddrPrefix_Type.__name__ = "InetAddress"
_FsMIBgp4mpeUpdateFilterIPAddrPrefix_Object = MibTableColumn
fsMIBgp4mpeUpdateFilterIPAddrPrefix = _FsMIBgp4mpeUpdateFilterIPAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 25, 1, 6),
    _FsMIBgp4mpeUpdateFilterIPAddrPrefix_Type()
)
fsMIBgp4mpeUpdateFilterIPAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeUpdateFilterIPAddrPrefix.setStatus("current")


class _FsMIBgp4mpeUpdateFilterIPAddrPrefixLen_Type(Integer32):
    """Custom type fsMIBgp4mpeUpdateFilterIPAddrPrefixLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FsMIBgp4mpeUpdateFilterIPAddrPrefixLen_Type.__name__ = "Integer32"
_FsMIBgp4mpeUpdateFilterIPAddrPrefixLen_Object = MibTableColumn
fsMIBgp4mpeUpdateFilterIPAddrPrefixLen = _FsMIBgp4mpeUpdateFilterIPAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 25, 1, 7),
    _FsMIBgp4mpeUpdateFilterIPAddrPrefixLen_Type()
)
fsMIBgp4mpeUpdateFilterIPAddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeUpdateFilterIPAddrPrefixLen.setStatus("current")
_FsMIBgp4mpeUpdateFilterIntermediateAS_Type = DisplayString
_FsMIBgp4mpeUpdateFilterIntermediateAS_Object = MibTableColumn
fsMIBgp4mpeUpdateFilterIntermediateAS = _FsMIBgp4mpeUpdateFilterIntermediateAS_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 25, 1, 8),
    _FsMIBgp4mpeUpdateFilterIntermediateAS_Type()
)
fsMIBgp4mpeUpdateFilterIntermediateAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeUpdateFilterIntermediateAS.setStatus("current")


class _FsMIBgp4mpeUpdateFilterDirection_Type(Integer32):
    """Custom type fsMIBgp4mpeUpdateFilterDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_FsMIBgp4mpeUpdateFilterDirection_Type.__name__ = "Integer32"
_FsMIBgp4mpeUpdateFilterDirection_Object = MibTableColumn
fsMIBgp4mpeUpdateFilterDirection = _FsMIBgp4mpeUpdateFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 25, 1, 9),
    _FsMIBgp4mpeUpdateFilterDirection_Type()
)
fsMIBgp4mpeUpdateFilterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeUpdateFilterDirection.setStatus("current")


class _FsMIBgp4mpeUpdateFilterAction_Type(Integer32):
    """Custom type fsMIBgp4mpeUpdateFilterAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("filter", 2))
    )


_FsMIBgp4mpeUpdateFilterAction_Type.__name__ = "Integer32"
_FsMIBgp4mpeUpdateFilterAction_Object = MibTableColumn
fsMIBgp4mpeUpdateFilterAction = _FsMIBgp4mpeUpdateFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 25, 1, 10),
    _FsMIBgp4mpeUpdateFilterAction_Type()
)
fsMIBgp4mpeUpdateFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeUpdateFilterAction.setStatus("current")


class _FsMIBgp4mpeUpdateFilterVrfName_Type(DisplayString):
    """Custom type fsMIBgp4mpeUpdateFilterVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsMIBgp4mpeUpdateFilterVrfName_Type.__name__ = "DisplayString"
_FsMIBgp4mpeUpdateFilterVrfName_Object = MibTableColumn
fsMIBgp4mpeUpdateFilterVrfName = _FsMIBgp4mpeUpdateFilterVrfName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 25, 1, 11),
    _FsMIBgp4mpeUpdateFilterVrfName_Type()
)
fsMIBgp4mpeUpdateFilterVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeUpdateFilterVrfName.setStatus("current")
_FsMIBgp4MpeAggregateTable_Object = MibTable
fsMIBgp4MpeAggregateTable = _FsMIBgp4MpeAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 26)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeAggregateTable.setStatus("current")
_FsMIBgp4MpeAggregateEntry_Object = MibTableRow
fsMIBgp4MpeAggregateEntry = _FsMIBgp4MpeAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 26, 1)
)
fsMIBgp4MpeAggregateEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeAggregateIndex"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeAggregateEntry.setStatus("current")


class _FsMIBgp4mpeAggregateIndex_Type(Integer32):
    """Custom type fsMIBgp4mpeAggregateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIBgp4mpeAggregateIndex_Type.__name__ = "Integer32"
_FsMIBgp4mpeAggregateIndex_Object = MibTableColumn
fsMIBgp4mpeAggregateIndex = _FsMIBgp4mpeAggregateIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 26, 1, 1),
    _FsMIBgp4mpeAggregateIndex_Type()
)
fsMIBgp4mpeAggregateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAggregateIndex.setStatus("current")


class _FsMIBgp4mpeAggregateAdminStatus_Type(Integer32):
    """Custom type fsMIBgp4mpeAggregateAdminStatus based on Integer32"""
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
          ("invalid", 3))
    )


_FsMIBgp4mpeAggregateAdminStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpeAggregateAdminStatus_Object = MibTableColumn
fsMIBgp4mpeAggregateAdminStatus = _FsMIBgp4mpeAggregateAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 26, 1, 2),
    _FsMIBgp4mpeAggregateAdminStatus_Type()
)
fsMIBgp4mpeAggregateAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAggregateAdminStatus.setStatus("current")
_FsMIBgp4mpeAggregateIPAddrAfi_Type = InetAddressType
_FsMIBgp4mpeAggregateIPAddrAfi_Object = MibTableColumn
fsMIBgp4mpeAggregateIPAddrAfi = _FsMIBgp4mpeAggregateIPAddrAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 26, 1, 3),
    _FsMIBgp4mpeAggregateIPAddrAfi_Type()
)
fsMIBgp4mpeAggregateIPAddrAfi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAggregateIPAddrAfi.setStatus("current")
_FsMIBgp4mpeAggregateIPAddrSafi_Type = BgpSafi
_FsMIBgp4mpeAggregateIPAddrSafi_Object = MibTableColumn
fsMIBgp4mpeAggregateIPAddrSafi = _FsMIBgp4mpeAggregateIPAddrSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 26, 1, 4),
    _FsMIBgp4mpeAggregateIPAddrSafi_Type()
)
fsMIBgp4mpeAggregateIPAddrSafi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAggregateIPAddrSafi.setStatus("current")
_FsMIBgp4mpeAggregateIPAddrPrefix_Type = InetAddress
_FsMIBgp4mpeAggregateIPAddrPrefix_Object = MibTableColumn
fsMIBgp4mpeAggregateIPAddrPrefix = _FsMIBgp4mpeAggregateIPAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 26, 1, 5),
    _FsMIBgp4mpeAggregateIPAddrPrefix_Type()
)
fsMIBgp4mpeAggregateIPAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAggregateIPAddrPrefix.setStatus("current")


class _FsMIBgp4mpeAggregateIPAddrPrefixLen_Type(Integer32):
    """Custom type fsMIBgp4mpeAggregateIPAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FsMIBgp4mpeAggregateIPAddrPrefixLen_Type.__name__ = "Integer32"
_FsMIBgp4mpeAggregateIPAddrPrefixLen_Object = MibTableColumn
fsMIBgp4mpeAggregateIPAddrPrefixLen = _FsMIBgp4mpeAggregateIPAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 26, 1, 6),
    _FsMIBgp4mpeAggregateIPAddrPrefixLen_Type()
)
fsMIBgp4mpeAggregateIPAddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAggregateIPAddrPrefixLen.setStatus("current")


class _FsMIBgp4mpeAggregateAdvertise_Type(Integer32):
    """Custom type fsMIBgp4mpeAggregateAdvertise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("summaryOnly", 1),
          ("all", 2))
    )


_FsMIBgp4mpeAggregateAdvertise_Type.__name__ = "Integer32"
_FsMIBgp4mpeAggregateAdvertise_Object = MibTableColumn
fsMIBgp4mpeAggregateAdvertise = _FsMIBgp4mpeAggregateAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 26, 1, 7),
    _FsMIBgp4mpeAggregateAdvertise_Type()
)
fsMIBgp4mpeAggregateAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAggregateAdvertise.setStatus("current")


class _FsMIBgp4mpeAggregateVrfName_Type(DisplayString):
    """Custom type fsMIBgp4mpeAggregateVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsMIBgp4mpeAggregateVrfName_Type.__name__ = "DisplayString"
_FsMIBgp4mpeAggregateVrfName_Object = MibTableColumn
fsMIBgp4mpeAggregateVrfName = _FsMIBgp4mpeAggregateVrfName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 26, 1, 8),
    _FsMIBgp4mpeAggregateVrfName_Type()
)
fsMIBgp4mpeAggregateVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAggregateVrfName.setStatus("current")


class _FsMIBgp4mpeAggregateAsSet_Type(Integer32):
    """Custom type fsMIBgp4mpeAggregateAsSet based on Integer32"""
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


_FsMIBgp4mpeAggregateAsSet_Type.__name__ = "Integer32"
_FsMIBgp4mpeAggregateAsSet_Object = MibTableColumn
fsMIBgp4mpeAggregateAsSet = _FsMIBgp4mpeAggregateAsSet_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 26, 1, 9),
    _FsMIBgp4mpeAggregateAsSet_Type()
)
fsMIBgp4mpeAggregateAsSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAggregateAsSet.setStatus("current")


class _FsMIBgp4mpeAggregateAdvertiseRouteMapName_Type(DisplayString):
    """Custom type fsMIBgp4mpeAggregateAdvertiseRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsMIBgp4mpeAggregateAdvertiseRouteMapName_Type.__name__ = "DisplayString"
_FsMIBgp4mpeAggregateAdvertiseRouteMapName_Object = MibTableColumn
fsMIBgp4mpeAggregateAdvertiseRouteMapName = _FsMIBgp4mpeAggregateAdvertiseRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 26, 1, 10),
    _FsMIBgp4mpeAggregateAdvertiseRouteMapName_Type()
)
fsMIBgp4mpeAggregateAdvertiseRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAggregateAdvertiseRouteMapName.setStatus("current")


class _FsMIBgp4mpeAggregateSuppressRouteMapName_Type(DisplayString):
    """Custom type fsMIBgp4mpeAggregateSuppressRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsMIBgp4mpeAggregateSuppressRouteMapName_Type.__name__ = "DisplayString"
_FsMIBgp4mpeAggregateSuppressRouteMapName_Object = MibTableColumn
fsMIBgp4mpeAggregateSuppressRouteMapName = _FsMIBgp4mpeAggregateSuppressRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 26, 1, 11),
    _FsMIBgp4mpeAggregateSuppressRouteMapName_Type()
)
fsMIBgp4mpeAggregateSuppressRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAggregateSuppressRouteMapName.setStatus("current")


class _FsMIBgp4mpeAggregateAttributeRouteMapName_Type(DisplayString):
    """Custom type fsMIBgp4mpeAggregateAttributeRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsMIBgp4mpeAggregateAttributeRouteMapName_Type.__name__ = "DisplayString"
_FsMIBgp4mpeAggregateAttributeRouteMapName_Object = MibTableColumn
fsMIBgp4mpeAggregateAttributeRouteMapName = _FsMIBgp4mpeAggregateAttributeRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 26, 1, 12),
    _FsMIBgp4mpeAggregateAttributeRouteMapName_Type()
)
fsMIBgp4mpeAggregateAttributeRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAggregateAttributeRouteMapName.setStatus("current")
_FsMIBgp4MpeImportRouteTable_Object = MibTable
fsMIBgp4MpeImportRouteTable = _FsMIBgp4MpeImportRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 27)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeImportRouteTable.setStatus("current")
_FsMIBgp4MpeImportRouteEntry_Object = MibTableRow
fsMIBgp4MpeImportRouteEntry = _FsMIBgp4MpeImportRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 27, 1)
)
fsMIBgp4MpeImportRouteEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeImportRoutePrefixAfi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeImportRoutePrefixSafi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeImportRoutePrefix"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeImportRoutePrefixLen"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeImportRouteProtocol"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeImportRouteNextHop"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeImportRouteIfIndex"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeImportRouteMetric"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeImportRouteVrf"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeImportRouteEntry.setStatus("current")
_FsMIBgp4mpeImportRoutePrefixAfi_Type = InetAddressType
_FsMIBgp4mpeImportRoutePrefixAfi_Object = MibTableColumn
fsMIBgp4mpeImportRoutePrefixAfi = _FsMIBgp4mpeImportRoutePrefixAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 27, 1, 1),
    _FsMIBgp4mpeImportRoutePrefixAfi_Type()
)
fsMIBgp4mpeImportRoutePrefixAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeImportRoutePrefixAfi.setStatus("current")
_FsMIBgp4mpeImportRoutePrefixSafi_Type = BgpSafi
_FsMIBgp4mpeImportRoutePrefixSafi_Object = MibTableColumn
fsMIBgp4mpeImportRoutePrefixSafi = _FsMIBgp4mpeImportRoutePrefixSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 27, 1, 2),
    _FsMIBgp4mpeImportRoutePrefixSafi_Type()
)
fsMIBgp4mpeImportRoutePrefixSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeImportRoutePrefixSafi.setStatus("current")
_FsMIBgp4mpeImportRoutePrefix_Type = InetAddress
_FsMIBgp4mpeImportRoutePrefix_Object = MibTableColumn
fsMIBgp4mpeImportRoutePrefix = _FsMIBgp4mpeImportRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 27, 1, 3),
    _FsMIBgp4mpeImportRoutePrefix_Type()
)
fsMIBgp4mpeImportRoutePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeImportRoutePrefix.setStatus("current")


class _FsMIBgp4mpeImportRoutePrefixLen_Type(Integer32):
    """Custom type fsMIBgp4mpeImportRoutePrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsMIBgp4mpeImportRoutePrefixLen_Type.__name__ = "Integer32"
_FsMIBgp4mpeImportRoutePrefixLen_Object = MibTableColumn
fsMIBgp4mpeImportRoutePrefixLen = _FsMIBgp4mpeImportRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 27, 1, 4),
    _FsMIBgp4mpeImportRoutePrefixLen_Type()
)
fsMIBgp4mpeImportRoutePrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeImportRoutePrefixLen.setStatus("current")


class _FsMIBgp4mpeImportRouteProtocol_Type(Integer32):
    """Custom type fsMIBgp4mpeImportRouteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(13, 13),
    )


_FsMIBgp4mpeImportRouteProtocol_Type.__name__ = "Integer32"
_FsMIBgp4mpeImportRouteProtocol_Object = MibTableColumn
fsMIBgp4mpeImportRouteProtocol = _FsMIBgp4mpeImportRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 27, 1, 5),
    _FsMIBgp4mpeImportRouteProtocol_Type()
)
fsMIBgp4mpeImportRouteProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeImportRouteProtocol.setStatus("current")
_FsMIBgp4mpeImportRouteNextHop_Type = InetAddress
_FsMIBgp4mpeImportRouteNextHop_Object = MibTableColumn
fsMIBgp4mpeImportRouteNextHop = _FsMIBgp4mpeImportRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 27, 1, 6),
    _FsMIBgp4mpeImportRouteNextHop_Type()
)
fsMIBgp4mpeImportRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeImportRouteNextHop.setStatus("current")


class _FsMIBgp4mpeImportRouteIfIndex_Type(Integer32):
    """Custom type fsMIBgp4mpeImportRouteIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsMIBgp4mpeImportRouteIfIndex_Type.__name__ = "Integer32"
_FsMIBgp4mpeImportRouteIfIndex_Object = MibTableColumn
fsMIBgp4mpeImportRouteIfIndex = _FsMIBgp4mpeImportRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 27, 1, 7),
    _FsMIBgp4mpeImportRouteIfIndex_Type()
)
fsMIBgp4mpeImportRouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeImportRouteIfIndex.setStatus("current")


class _FsMIBgp4mpeImportRouteMetric_Type(Integer32):
    """Custom type fsMIBgp4mpeImportRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsMIBgp4mpeImportRouteMetric_Type.__name__ = "Integer32"
_FsMIBgp4mpeImportRouteMetric_Object = MibTableColumn
fsMIBgp4mpeImportRouteMetric = _FsMIBgp4mpeImportRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 27, 1, 8),
    _FsMIBgp4mpeImportRouteMetric_Type()
)
fsMIBgp4mpeImportRouteMetric.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeImportRouteMetric.setStatus("current")


class _FsMIBgp4mpeImportRouteVrf_Type(DisplayString):
    """Custom type fsMIBgp4mpeImportRouteVrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FsMIBgp4mpeImportRouteVrf_Type.__name__ = "DisplayString"
_FsMIBgp4mpeImportRouteVrf_Object = MibTableColumn
fsMIBgp4mpeImportRouteVrf = _FsMIBgp4mpeImportRouteVrf_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 27, 1, 9),
    _FsMIBgp4mpeImportRouteVrf_Type()
)
fsMIBgp4mpeImportRouteVrf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeImportRouteVrf.setStatus("current")


class _FsMIBgp4mpeImportRouteAction_Type(Integer32):
    """Custom type fsMIBgp4mpeImportRouteAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_FsMIBgp4mpeImportRouteAction_Type.__name__ = "Integer32"
_FsMIBgp4mpeImportRouteAction_Object = MibTableColumn
fsMIBgp4mpeImportRouteAction = _FsMIBgp4mpeImportRouteAction_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 27, 1, 10),
    _FsMIBgp4mpeImportRouteAction_Type()
)
fsMIBgp4mpeImportRouteAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeImportRouteAction.setStatus("current")
_FsMIBgp4MpeFsmTransitionHistTable_Object = MibTable
fsMIBgp4MpeFsmTransitionHistTable = _FsMIBgp4MpeFsmTransitionHistTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 28)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeFsmTransitionHistTable.setStatus("current")
_FsMIBgp4MpeFsmTransitionHistEntry_Object = MibTableRow
fsMIBgp4MpeFsmTransitionHistEntry = _FsMIBgp4MpeFsmTransitionHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 28, 1)
)
fsMIBgp4MpeFsmTransitionHistEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpePeerType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpePeer"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeFsmTransitionHistEntry.setStatus("current")
_FsMIBgp4mpePeerType_Type = InetAddressType
_FsMIBgp4mpePeerType_Object = MibTableColumn
fsMIBgp4mpePeerType = _FsMIBgp4mpePeerType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 28, 1, 1),
    _FsMIBgp4mpePeerType_Type()
)
fsMIBgp4mpePeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerType.setStatus("current")
_FsMIBgp4mpePeer_Type = InetAddress
_FsMIBgp4mpePeer_Object = MibTableColumn
fsMIBgp4mpePeer = _FsMIBgp4mpePeer_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 28, 1, 2),
    _FsMIBgp4mpePeer_Type()
)
fsMIBgp4mpePeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeer.setStatus("current")
_FsMIBgp4mpeFsmTransitionHist_Type = DisplayString
_FsMIBgp4mpeFsmTransitionHist_Object = MibTableColumn
fsMIBgp4mpeFsmTransitionHist = _FsMIBgp4mpeFsmTransitionHist_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 28, 1, 3),
    _FsMIBgp4mpeFsmTransitionHist_Type()
)
fsMIBgp4mpeFsmTransitionHist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeFsmTransitionHist.setStatus("current")
_FsMIBgp4MpeRfd_ObjectIdentity = ObjectIdentity
fsMIBgp4MpeRfd = _FsMIBgp4MpeRfd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29)
)
_FsMIBgp4MpeRfdRtDampHistTable_Object = MibTable
fsMIBgp4MpeRfdRtDampHistTable = _FsMIBgp4MpeRfdRtDampHistTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 1)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeRfdRtDampHistTable.setStatus("current")
_FsMIBgp4MpeRfdRtDampHistEntry_Object = MibTableRow
fsMIBgp4MpeRfdRtDampHistEntry = _FsMIBgp4MpeRfdRtDampHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 1, 1)
)
fsMIBgp4MpeRfdRtDampHistEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpePathAttrAddrPrefixAfi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpePathAttrAddrPrefixSafi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpePathAttrAddrPrefix"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpePathAttrAddrPrefixLen"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpePathAttrPeerType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpePathAttrPeer"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeRfdRtDampHistEntry.setStatus("current")
_FsMIBgp4mpePathAttrAddrPrefixAfi_Type = InetAddressType
_FsMIBgp4mpePathAttrAddrPrefixAfi_Object = MibTableColumn
fsMIBgp4mpePathAttrAddrPrefixAfi = _FsMIBgp4mpePathAttrAddrPrefixAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 1, 1, 1),
    _FsMIBgp4mpePathAttrAddrPrefixAfi_Type()
)
fsMIBgp4mpePathAttrAddrPrefixAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpePathAttrAddrPrefixAfi.setStatus("current")
_FsMIBgp4mpePathAttrAddrPrefixSafi_Type = BgpSafi
_FsMIBgp4mpePathAttrAddrPrefixSafi_Object = MibTableColumn
fsMIBgp4mpePathAttrAddrPrefixSafi = _FsMIBgp4mpePathAttrAddrPrefixSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 1, 1, 2),
    _FsMIBgp4mpePathAttrAddrPrefixSafi_Type()
)
fsMIBgp4mpePathAttrAddrPrefixSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpePathAttrAddrPrefixSafi.setStatus("current")
_FsMIBgp4mpePathAttrAddrPrefix_Type = InetAddress
_FsMIBgp4mpePathAttrAddrPrefix_Object = MibTableColumn
fsMIBgp4mpePathAttrAddrPrefix = _FsMIBgp4mpePathAttrAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 1, 1, 3),
    _FsMIBgp4mpePathAttrAddrPrefix_Type()
)
fsMIBgp4mpePathAttrAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpePathAttrAddrPrefix.setStatus("current")


class _FsMIBgp4mpePathAttrAddrPrefixLen_Type(Integer32):
    """Custom type fsMIBgp4mpePathAttrAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FsMIBgp4mpePathAttrAddrPrefixLen_Type.__name__ = "Integer32"
_FsMIBgp4mpePathAttrAddrPrefixLen_Object = MibTableColumn
fsMIBgp4mpePathAttrAddrPrefixLen = _FsMIBgp4mpePathAttrAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 1, 1, 4),
    _FsMIBgp4mpePathAttrAddrPrefixLen_Type()
)
fsMIBgp4mpePathAttrAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpePathAttrAddrPrefixLen.setStatus("current")
_FsMIBgp4mpePathAttrPeerType_Type = InetAddressType
_FsMIBgp4mpePathAttrPeerType_Object = MibTableColumn
fsMIBgp4mpePathAttrPeerType = _FsMIBgp4mpePathAttrPeerType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 1, 1, 5),
    _FsMIBgp4mpePathAttrPeerType_Type()
)
fsMIBgp4mpePathAttrPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpePathAttrPeerType.setStatus("current")
_FsMIBgp4mpePathAttrPeer_Type = InetAddress
_FsMIBgp4mpePathAttrPeer_Object = MibTableColumn
fsMIBgp4mpePathAttrPeer = _FsMIBgp4mpePathAttrPeer_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 1, 1, 6),
    _FsMIBgp4mpePathAttrPeer_Type()
)
fsMIBgp4mpePathAttrPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpePathAttrPeer.setStatus("current")


class _FsMIBgp4mpeRfdRtFom_Type(Integer32):
    """Custom type fsMIBgp4mpeRfdRtFom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIBgp4mpeRfdRtFom_Type.__name__ = "Integer32"
_FsMIBgp4mpeRfdRtFom_Object = MibTableColumn
fsMIBgp4mpeRfdRtFom = _FsMIBgp4mpeRfdRtFom_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 1, 1, 7),
    _FsMIBgp4mpeRfdRtFom_Type()
)
fsMIBgp4mpeRfdRtFom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdRtFom.setStatus("current")


class _FsMIBgp4mpeRfdRtLastUpdtTime_Type(Integer32):
    """Custom type fsMIBgp4mpeRfdRtLastUpdtTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsMIBgp4mpeRfdRtLastUpdtTime_Type.__name__ = "Integer32"
_FsMIBgp4mpeRfdRtLastUpdtTime_Object = MibTableColumn
fsMIBgp4mpeRfdRtLastUpdtTime = _FsMIBgp4mpeRfdRtLastUpdtTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 1, 1, 8),
    _FsMIBgp4mpeRfdRtLastUpdtTime_Type()
)
fsMIBgp4mpeRfdRtLastUpdtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdRtLastUpdtTime.setStatus("current")


class _FsMIBgp4mpeRfdRtState_Type(Integer32):
    """Custom type fsMIBgp4mpeRfdRtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("suppressed", 2),
          ("unsuppressed", 3))
    )


_FsMIBgp4mpeRfdRtState_Type.__name__ = "Integer32"
_FsMIBgp4mpeRfdRtState_Object = MibTableColumn
fsMIBgp4mpeRfdRtState = _FsMIBgp4mpeRfdRtState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 1, 1, 9),
    _FsMIBgp4mpeRfdRtState_Type()
)
fsMIBgp4mpeRfdRtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdRtState.setStatus("current")


class _FsMIBgp4mpeRfdRtStatus_Type(Integer32):
    """Custom type fsMIBgp4mpeRfdRtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("feasibleroute", 2),
          ("unfeasibleroute", 3))
    )


_FsMIBgp4mpeRfdRtStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpeRfdRtStatus_Object = MibTableColumn
fsMIBgp4mpeRfdRtStatus = _FsMIBgp4mpeRfdRtStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 1, 1, 10),
    _FsMIBgp4mpeRfdRtStatus_Type()
)
fsMIBgp4mpeRfdRtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdRtStatus.setStatus("current")
_FsMIBgp4mpeRfdRtFlapCount_Type = Integer32
_FsMIBgp4mpeRfdRtFlapCount_Object = MibTableColumn
fsMIBgp4mpeRfdRtFlapCount = _FsMIBgp4mpeRfdRtFlapCount_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 1, 1, 11),
    _FsMIBgp4mpeRfdRtFlapCount_Type()
)
fsMIBgp4mpeRfdRtFlapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdRtFlapCount.setStatus("current")


class _FsMIBgp4mpeRfdRtFlapTime_Type(Integer32):
    """Custom type fsMIBgp4mpeRfdRtFlapTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsMIBgp4mpeRfdRtFlapTime_Type.__name__ = "Integer32"
_FsMIBgp4mpeRfdRtFlapTime_Object = MibTableColumn
fsMIBgp4mpeRfdRtFlapTime = _FsMIBgp4mpeRfdRtFlapTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 1, 1, 12),
    _FsMIBgp4mpeRfdRtFlapTime_Type()
)
fsMIBgp4mpeRfdRtFlapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdRtFlapTime.setStatus("current")


class _FsMIBgp4mpeRfdRtReuseTime_Type(Integer32):
    """Custom type fsMIBgp4mpeRfdRtReuseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsMIBgp4mpeRfdRtReuseTime_Type.__name__ = "Integer32"
_FsMIBgp4mpeRfdRtReuseTime_Object = MibTableColumn
fsMIBgp4mpeRfdRtReuseTime = _FsMIBgp4mpeRfdRtReuseTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 1, 1, 13),
    _FsMIBgp4mpeRfdRtReuseTime_Type()
)
fsMIBgp4mpeRfdRtReuseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdRtReuseTime.setStatus("current")
_FsMIBgp4MpeRfdPeerDampHistTable_Object = MibTable
fsMIBgp4MpeRfdPeerDampHistTable = _FsMIBgp4MpeRfdPeerDampHistTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 2)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeRfdPeerDampHistTable.setStatus("current")
_FsMIBgp4MpeRfdPeerDampHistEntry_Object = MibTableRow
fsMIBgp4MpeRfdPeerDampHistEntry = _FsMIBgp4MpeRfdPeerDampHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 2, 1)
)
fsMIBgp4MpeRfdPeerDampHistEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpePeerRemoteIpAddrType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpePeerRemoteIpAddr"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeRfdPeerDampHistEntry.setStatus("current")
_FsMIBgp4mpePeerRemoteIpAddrType_Type = InetAddressType
_FsMIBgp4mpePeerRemoteIpAddrType_Object = MibTableColumn
fsMIBgp4mpePeerRemoteIpAddrType = _FsMIBgp4mpePeerRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 2, 1, 1),
    _FsMIBgp4mpePeerRemoteIpAddrType_Type()
)
fsMIBgp4mpePeerRemoteIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerRemoteIpAddrType.setStatus("current")
_FsMIBgp4mpePeerRemoteIpAddr_Type = InetAddress
_FsMIBgp4mpePeerRemoteIpAddr_Object = MibTableColumn
fsMIBgp4mpePeerRemoteIpAddr = _FsMIBgp4mpePeerRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 2, 1, 2),
    _FsMIBgp4mpePeerRemoteIpAddr_Type()
)
fsMIBgp4mpePeerRemoteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerRemoteIpAddr.setStatus("current")


class _FsMIBgp4mpeRfdPeerFom_Type(Integer32):
    """Custom type fsMIBgp4mpeRfdPeerFom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIBgp4mpeRfdPeerFom_Type.__name__ = "Integer32"
_FsMIBgp4mpeRfdPeerFom_Object = MibTableColumn
fsMIBgp4mpeRfdPeerFom = _FsMIBgp4mpeRfdPeerFom_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 2, 1, 3),
    _FsMIBgp4mpeRfdPeerFom_Type()
)
fsMIBgp4mpeRfdPeerFom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdPeerFom.setStatus("current")


class _FsMIBgp4mpeRfdPeerLastUpdtTime_Type(Integer32):
    """Custom type fsMIBgp4mpeRfdPeerLastUpdtTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsMIBgp4mpeRfdPeerLastUpdtTime_Type.__name__ = "Integer32"
_FsMIBgp4mpeRfdPeerLastUpdtTime_Object = MibTableColumn
fsMIBgp4mpeRfdPeerLastUpdtTime = _FsMIBgp4mpeRfdPeerLastUpdtTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 2, 1, 4),
    _FsMIBgp4mpeRfdPeerLastUpdtTime_Type()
)
fsMIBgp4mpeRfdPeerLastUpdtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdPeerLastUpdtTime.setStatus("current")


class _FsMIBgp4mpeRfdPeerState_Type(Integer32):
    """Custom type fsMIBgp4mpeRfdPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("suppressed", 2),
          ("unsuppressed", 3))
    )


_FsMIBgp4mpeRfdPeerState_Type.__name__ = "Integer32"
_FsMIBgp4mpeRfdPeerState_Object = MibTableColumn
fsMIBgp4mpeRfdPeerState = _FsMIBgp4mpeRfdPeerState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 2, 1, 5),
    _FsMIBgp4mpeRfdPeerState_Type()
)
fsMIBgp4mpeRfdPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdPeerState.setStatus("current")


class _FsMIBgp4mpeRfdPeerStatus_Type(Integer32):
    """Custom type fsMIBgp4mpeRfdPeerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("peerup", 2),
          ("peerdown", 3))
    )


_FsMIBgp4mpeRfdPeerStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpeRfdPeerStatus_Object = MibTableColumn
fsMIBgp4mpeRfdPeerStatus = _FsMIBgp4mpeRfdPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 2, 1, 6),
    _FsMIBgp4mpeRfdPeerStatus_Type()
)
fsMIBgp4mpeRfdPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdPeerStatus.setStatus("current")
_FsMIBgp4MpeRfdRtsReuseListTable_Object = MibTable
fsMIBgp4MpeRfdRtsReuseListTable = _FsMIBgp4MpeRfdRtsReuseListTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 3)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeRfdRtsReuseListTable.setStatus("current")
_FsMIBgp4MpeRfdRtsReuseListEntry_Object = MibTableRow
fsMIBgp4MpeRfdRtsReuseListEntry = _FsMIBgp4MpeRfdRtsReuseListEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 3, 1)
)
fsMIBgp4MpeRfdRtsReuseListEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeRtAfi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeRtSafi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeRtIPPrefix"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeRtIPPrefixLen"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeRfdRtsReusePeerType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpePeerRemAddress"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeRfdRtsReuseListEntry.setStatus("current")
_FsMIBgp4mpeRtAfi_Type = InetAddressType
_FsMIBgp4mpeRtAfi_Object = MibTableColumn
fsMIBgp4mpeRtAfi = _FsMIBgp4mpeRtAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 3, 1, 1),
    _FsMIBgp4mpeRtAfi_Type()
)
fsMIBgp4mpeRtAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRtAfi.setStatus("current")
_FsMIBgp4mpeRtSafi_Type = BgpSafi
_FsMIBgp4mpeRtSafi_Object = MibTableColumn
fsMIBgp4mpeRtSafi = _FsMIBgp4mpeRtSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 3, 1, 2),
    _FsMIBgp4mpeRtSafi_Type()
)
fsMIBgp4mpeRtSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRtSafi.setStatus("current")
_FsMIBgp4mpeRtIPPrefix_Type = InetAddress
_FsMIBgp4mpeRtIPPrefix_Object = MibTableColumn
fsMIBgp4mpeRtIPPrefix = _FsMIBgp4mpeRtIPPrefix_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 3, 1, 3),
    _FsMIBgp4mpeRtIPPrefix_Type()
)
fsMIBgp4mpeRtIPPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRtIPPrefix.setStatus("current")


class _FsMIBgp4mpeRtIPPrefixLen_Type(Integer32):
    """Custom type fsMIBgp4mpeRtIPPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_FsMIBgp4mpeRtIPPrefixLen_Type.__name__ = "Integer32"
_FsMIBgp4mpeRtIPPrefixLen_Object = MibTableColumn
fsMIBgp4mpeRtIPPrefixLen = _FsMIBgp4mpeRtIPPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 3, 1, 4),
    _FsMIBgp4mpeRtIPPrefixLen_Type()
)
fsMIBgp4mpeRtIPPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRtIPPrefixLen.setStatus("current")
_FsMIBgp4mpeRfdRtsReusePeerType_Type = InetAddressType
_FsMIBgp4mpeRfdRtsReusePeerType_Object = MibTableColumn
fsMIBgp4mpeRfdRtsReusePeerType = _FsMIBgp4mpeRfdRtsReusePeerType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 3, 1, 5),
    _FsMIBgp4mpeRfdRtsReusePeerType_Type()
)
fsMIBgp4mpeRfdRtsReusePeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdRtsReusePeerType.setStatus("current")
_FsMIBgp4mpePeerRemAddress_Type = InetAddress
_FsMIBgp4mpePeerRemAddress_Object = MibTableColumn
fsMIBgp4mpePeerRemAddress = _FsMIBgp4mpePeerRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 3, 1, 6),
    _FsMIBgp4mpePeerRemAddress_Type()
)
fsMIBgp4mpePeerRemAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerRemAddress.setStatus("current")


class _FsMIBgp4mpeRfdRtReuseListRtFom_Type(Integer32):
    """Custom type fsMIBgp4mpeRfdRtReuseListRtFom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIBgp4mpeRfdRtReuseListRtFom_Type.__name__ = "Integer32"
_FsMIBgp4mpeRfdRtReuseListRtFom_Object = MibTableColumn
fsMIBgp4mpeRfdRtReuseListRtFom = _FsMIBgp4mpeRfdRtReuseListRtFom_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 3, 1, 7),
    _FsMIBgp4mpeRfdRtReuseListRtFom_Type()
)
fsMIBgp4mpeRfdRtReuseListRtFom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdRtReuseListRtFom.setStatus("current")


class _FsMIBgp4mpeRfdRtReuseListRtLastUpdtTime_Type(Integer32):
    """Custom type fsMIBgp4mpeRfdRtReuseListRtLastUpdtTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsMIBgp4mpeRfdRtReuseListRtLastUpdtTime_Type.__name__ = "Integer32"
_FsMIBgp4mpeRfdRtReuseListRtLastUpdtTime_Object = MibTableColumn
fsMIBgp4mpeRfdRtReuseListRtLastUpdtTime = _FsMIBgp4mpeRfdRtReuseListRtLastUpdtTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 3, 1, 8),
    _FsMIBgp4mpeRfdRtReuseListRtLastUpdtTime_Type()
)
fsMIBgp4mpeRfdRtReuseListRtLastUpdtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdRtReuseListRtLastUpdtTime.setStatus("current")


class _FsMIBgp4mpeRfdRtReuseListRtState_Type(Integer32):
    """Custom type fsMIBgp4mpeRfdRtReuseListRtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("suppressed", 2),
          ("unsuppressed", 3))
    )


_FsMIBgp4mpeRfdRtReuseListRtState_Type.__name__ = "Integer32"
_FsMIBgp4mpeRfdRtReuseListRtState_Object = MibTableColumn
fsMIBgp4mpeRfdRtReuseListRtState = _FsMIBgp4mpeRfdRtReuseListRtState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 3, 1, 9),
    _FsMIBgp4mpeRfdRtReuseListRtState_Type()
)
fsMIBgp4mpeRfdRtReuseListRtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdRtReuseListRtState.setStatus("current")


class _FsMIBgp4mpeRfdRtReuseListRtStatus_Type(Integer32):
    """Custom type fsMIBgp4mpeRfdRtReuseListRtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("feasibleroute", 2),
          ("unfeasibleroute", 3))
    )


_FsMIBgp4mpeRfdRtReuseListRtStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpeRfdRtReuseListRtStatus_Object = MibTableColumn
fsMIBgp4mpeRfdRtReuseListRtStatus = _FsMIBgp4mpeRfdRtReuseListRtStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 3, 1, 10),
    _FsMIBgp4mpeRfdRtReuseListRtStatus_Type()
)
fsMIBgp4mpeRfdRtReuseListRtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdRtReuseListRtStatus.setStatus("current")
_FsMIBgp4MpeRfdPeerReuseListTable_Object = MibTable
fsMIBgp4MpeRfdPeerReuseListTable = _FsMIBgp4MpeRfdPeerReuseListTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 4)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeRfdPeerReuseListTable.setStatus("current")
_FsMIBgp4MpeRfdPeerReuseListEntry_Object = MibTableRow
fsMIBgp4MpeRfdPeerReuseListEntry = _FsMIBgp4MpeRfdPeerReuseListEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 4, 1)
)
fsMIBgp4MpeRfdPeerReuseListEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeRfdPeerRemIpAddrType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeRfdPeerRemIpAddr"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeRfdPeerReuseListEntry.setStatus("current")
_FsMIBgp4mpeRfdPeerRemIpAddrType_Type = InetAddressType
_FsMIBgp4mpeRfdPeerRemIpAddrType_Object = MibTableColumn
fsMIBgp4mpeRfdPeerRemIpAddrType = _FsMIBgp4mpeRfdPeerRemIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 4, 1, 1),
    _FsMIBgp4mpeRfdPeerRemIpAddrType_Type()
)
fsMIBgp4mpeRfdPeerRemIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdPeerRemIpAddrType.setStatus("current")
_FsMIBgp4mpeRfdPeerRemIpAddr_Type = InetAddress
_FsMIBgp4mpeRfdPeerRemIpAddr_Object = MibTableColumn
fsMIBgp4mpeRfdPeerRemIpAddr = _FsMIBgp4mpeRfdPeerRemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 4, 1, 2),
    _FsMIBgp4mpeRfdPeerRemIpAddr_Type()
)
fsMIBgp4mpeRfdPeerRemIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdPeerRemIpAddr.setStatus("current")


class _FsMIBgp4mpeRfdPeerReuseListPeerFom_Type(Integer32):
    """Custom type fsMIBgp4mpeRfdPeerReuseListPeerFom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIBgp4mpeRfdPeerReuseListPeerFom_Type.__name__ = "Integer32"
_FsMIBgp4mpeRfdPeerReuseListPeerFom_Object = MibTableColumn
fsMIBgp4mpeRfdPeerReuseListPeerFom = _FsMIBgp4mpeRfdPeerReuseListPeerFom_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 4, 1, 3),
    _FsMIBgp4mpeRfdPeerReuseListPeerFom_Type()
)
fsMIBgp4mpeRfdPeerReuseListPeerFom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdPeerReuseListPeerFom.setStatus("current")


class _FsMIBgp4mpeRfdPeerReuseListLastUpdtTime_Type(Integer32):
    """Custom type fsMIBgp4mpeRfdPeerReuseListLastUpdtTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsMIBgp4mpeRfdPeerReuseListLastUpdtTime_Type.__name__ = "Integer32"
_FsMIBgp4mpeRfdPeerReuseListLastUpdtTime_Object = MibTableColumn
fsMIBgp4mpeRfdPeerReuseListLastUpdtTime = _FsMIBgp4mpeRfdPeerReuseListLastUpdtTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 4, 1, 4),
    _FsMIBgp4mpeRfdPeerReuseListLastUpdtTime_Type()
)
fsMIBgp4mpeRfdPeerReuseListLastUpdtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdPeerReuseListLastUpdtTime.setStatus("current")


class _FsMIBgp4mpeRfdPeerReuseListPeerState_Type(Integer32):
    """Custom type fsMIBgp4mpeRfdPeerReuseListPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("suppressed", 2),
          ("unsuppressed", 3))
    )


_FsMIBgp4mpeRfdPeerReuseListPeerState_Type.__name__ = "Integer32"
_FsMIBgp4mpeRfdPeerReuseListPeerState_Object = MibTableColumn
fsMIBgp4mpeRfdPeerReuseListPeerState = _FsMIBgp4mpeRfdPeerReuseListPeerState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 4, 1, 5),
    _FsMIBgp4mpeRfdPeerReuseListPeerState_Type()
)
fsMIBgp4mpeRfdPeerReuseListPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdPeerReuseListPeerState.setStatus("current")


class _FsMIBgp4mpeRfdPeerReuseListPeerStatus_Type(Integer32):
    """Custom type fsMIBgp4mpeRfdPeerReuseListPeerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("peerup", 2),
          ("peerdown", 3))
    )


_FsMIBgp4mpeRfdPeerReuseListPeerStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpeRfdPeerReuseListPeerStatus_Object = MibTableColumn
fsMIBgp4mpeRfdPeerReuseListPeerStatus = _FsMIBgp4mpeRfdPeerReuseListPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 29, 4, 1, 6),
    _FsMIBgp4mpeRfdPeerReuseListPeerStatus_Type()
)
fsMIBgp4mpeRfdPeerReuseListPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRfdPeerReuseListPeerStatus.setStatus("current")
_FsMIBgp4MpeComm_ObjectIdentity = ObjectIdentity
fsMIBgp4MpeComm = _FsMIBgp4MpeComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30)
)
_FsMIBgp4MpeCommRouteAddCommTable_Object = MibTable
fsMIBgp4MpeCommRouteAddCommTable = _FsMIBgp4MpeCommRouteAddCommTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 1)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeCommRouteAddCommTable.setStatus("current")
_FsMIBgp4MpeCommRouteAddCommEntry_Object = MibTableRow
fsMIBgp4MpeCommRouteAddCommEntry = _FsMIBgp4MpeCommRouteAddCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 1, 1)
)
fsMIBgp4MpeCommRouteAddCommEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeAddCommRtAfi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeAddCommRtSafi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeAddCommIpNetwork"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeAddCommIpPrefixLen"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeAddCommVal"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeCommRouteAddCommEntry.setStatus("current")
_FsMIBgp4mpeAddCommRtAfi_Type = InetAddressType
_FsMIBgp4mpeAddCommRtAfi_Object = MibTableColumn
fsMIBgp4mpeAddCommRtAfi = _FsMIBgp4mpeAddCommRtAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 1, 1, 1),
    _FsMIBgp4mpeAddCommRtAfi_Type()
)
fsMIBgp4mpeAddCommRtAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAddCommRtAfi.setStatus("current")
_FsMIBgp4mpeAddCommRtSafi_Type = BgpSafi
_FsMIBgp4mpeAddCommRtSafi_Object = MibTableColumn
fsMIBgp4mpeAddCommRtSafi = _FsMIBgp4mpeAddCommRtSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 1, 1, 2),
    _FsMIBgp4mpeAddCommRtSafi_Type()
)
fsMIBgp4mpeAddCommRtSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAddCommRtSafi.setStatus("current")
_FsMIBgp4mpeAddCommIpNetwork_Type = InetAddress
_FsMIBgp4mpeAddCommIpNetwork_Object = MibTableColumn
fsMIBgp4mpeAddCommIpNetwork = _FsMIBgp4mpeAddCommIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 1, 1, 3),
    _FsMIBgp4mpeAddCommIpNetwork_Type()
)
fsMIBgp4mpeAddCommIpNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAddCommIpNetwork.setStatus("current")


class _FsMIBgp4mpeAddCommIpPrefixLen_Type(Integer32):
    """Custom type fsMIBgp4mpeAddCommIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsMIBgp4mpeAddCommIpPrefixLen_Type.__name__ = "Integer32"
_FsMIBgp4mpeAddCommIpPrefixLen_Object = MibTableColumn
fsMIBgp4mpeAddCommIpPrefixLen = _FsMIBgp4mpeAddCommIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 1, 1, 4),
    _FsMIBgp4mpeAddCommIpPrefixLen_Type()
)
fsMIBgp4mpeAddCommIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAddCommIpPrefixLen.setStatus("current")


class _FsMIBgp4mpeAddCommVal_Type(Unsigned32):
    """Custom type fsMIBgp4mpeAddCommVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65536, 4294901759),
        ValueRangeConstraint(4294967041, 4294967043),
    )


_FsMIBgp4mpeAddCommVal_Type.__name__ = "Unsigned32"
_FsMIBgp4mpeAddCommVal_Object = MibTableColumn
fsMIBgp4mpeAddCommVal = _FsMIBgp4mpeAddCommVal_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 1, 1, 5),
    _FsMIBgp4mpeAddCommVal_Type()
)
fsMIBgp4mpeAddCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAddCommVal.setStatus("current")
_FsMIBgp4mpeAddCommRowStatus_Type = RowStatus
_FsMIBgp4mpeAddCommRowStatus_Object = MibTableColumn
fsMIBgp4mpeAddCommRowStatus = _FsMIBgp4mpeAddCommRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 1, 1, 6),
    _FsMIBgp4mpeAddCommRowStatus_Type()
)
fsMIBgp4mpeAddCommRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAddCommRowStatus.setStatus("current")
_FsMIBgp4MpeCommRouteDeleteCommTable_Object = MibTable
fsMIBgp4MpeCommRouteDeleteCommTable = _FsMIBgp4MpeCommRouteDeleteCommTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 2)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeCommRouteDeleteCommTable.setStatus("current")
_FsMIBgp4MpeCommRouteDeleteCommEntry_Object = MibTableRow
fsMIBgp4MpeCommRouteDeleteCommEntry = _FsMIBgp4MpeCommRouteDeleteCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 2, 1)
)
fsMIBgp4MpeCommRouteDeleteCommEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeDeleteCommRtAfi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeDeleteCommRtSafi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeDeleteCommIpNetwork"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeDeleteCommIpPrefixLen"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeDeleteCommVal"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeCommRouteDeleteCommEntry.setStatus("current")
_FsMIBgp4mpeDeleteCommRtAfi_Type = InetAddressType
_FsMIBgp4mpeDeleteCommRtAfi_Object = MibTableColumn
fsMIBgp4mpeDeleteCommRtAfi = _FsMIBgp4mpeDeleteCommRtAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 2, 1, 1),
    _FsMIBgp4mpeDeleteCommRtAfi_Type()
)
fsMIBgp4mpeDeleteCommRtAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeDeleteCommRtAfi.setStatus("current")
_FsMIBgp4mpeDeleteCommRtSafi_Type = BgpSafi
_FsMIBgp4mpeDeleteCommRtSafi_Object = MibTableColumn
fsMIBgp4mpeDeleteCommRtSafi = _FsMIBgp4mpeDeleteCommRtSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 2, 1, 2),
    _FsMIBgp4mpeDeleteCommRtSafi_Type()
)
fsMIBgp4mpeDeleteCommRtSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeDeleteCommRtSafi.setStatus("current")
_FsMIBgp4mpeDeleteCommIpNetwork_Type = InetAddress
_FsMIBgp4mpeDeleteCommIpNetwork_Object = MibTableColumn
fsMIBgp4mpeDeleteCommIpNetwork = _FsMIBgp4mpeDeleteCommIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 2, 1, 3),
    _FsMIBgp4mpeDeleteCommIpNetwork_Type()
)
fsMIBgp4mpeDeleteCommIpNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeDeleteCommIpNetwork.setStatus("current")


class _FsMIBgp4mpeDeleteCommIpPrefixLen_Type(Integer32):
    """Custom type fsMIBgp4mpeDeleteCommIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsMIBgp4mpeDeleteCommIpPrefixLen_Type.__name__ = "Integer32"
_FsMIBgp4mpeDeleteCommIpPrefixLen_Object = MibTableColumn
fsMIBgp4mpeDeleteCommIpPrefixLen = _FsMIBgp4mpeDeleteCommIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 2, 1, 4),
    _FsMIBgp4mpeDeleteCommIpPrefixLen_Type()
)
fsMIBgp4mpeDeleteCommIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeDeleteCommIpPrefixLen.setStatus("current")


class _FsMIBgp4mpeDeleteCommVal_Type(Unsigned32):
    """Custom type fsMIBgp4mpeDeleteCommVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65536, 4294901759),
        ValueRangeConstraint(4294967041, 4294967043),
    )


_FsMIBgp4mpeDeleteCommVal_Type.__name__ = "Unsigned32"
_FsMIBgp4mpeDeleteCommVal_Object = MibTableColumn
fsMIBgp4mpeDeleteCommVal = _FsMIBgp4mpeDeleteCommVal_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 2, 1, 5),
    _FsMIBgp4mpeDeleteCommVal_Type()
)
fsMIBgp4mpeDeleteCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeDeleteCommVal.setStatus("current")
_FsMIBgp4mpeDeleteCommRowStatus_Type = RowStatus
_FsMIBgp4mpeDeleteCommRowStatus_Object = MibTableColumn
fsMIBgp4mpeDeleteCommRowStatus = _FsMIBgp4mpeDeleteCommRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 2, 1, 6),
    _FsMIBgp4mpeDeleteCommRowStatus_Type()
)
fsMIBgp4mpeDeleteCommRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4mpeDeleteCommRowStatus.setStatus("current")
_FsMIBgp4MpeCommRouteCommSetStatusTable_Object = MibTable
fsMIBgp4MpeCommRouteCommSetStatusTable = _FsMIBgp4MpeCommRouteCommSetStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 3)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeCommRouteCommSetStatusTable.setStatus("current")
_FsMIBgp4MpeCommRouteCommSetStatusEntry_Object = MibTableRow
fsMIBgp4MpeCommRouteCommSetStatusEntry = _FsMIBgp4MpeCommRouteCommSetStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 3, 1)
)
fsMIBgp4MpeCommRouteCommSetStatusEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeCommSetStatusAfi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeCommSetStatusSafi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeCommSetStatusIpNetwork"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeCommSetStatusIpPrefixLen"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeCommRouteCommSetStatusEntry.setStatus("current")
_FsMIBgp4mpeCommSetStatusAfi_Type = InetAddressType
_FsMIBgp4mpeCommSetStatusAfi_Object = MibTableColumn
fsMIBgp4mpeCommSetStatusAfi = _FsMIBgp4mpeCommSetStatusAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 3, 1, 1),
    _FsMIBgp4mpeCommSetStatusAfi_Type()
)
fsMIBgp4mpeCommSetStatusAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeCommSetStatusAfi.setStatus("current")
_FsMIBgp4mpeCommSetStatusSafi_Type = BgpSafi
_FsMIBgp4mpeCommSetStatusSafi_Object = MibTableColumn
fsMIBgp4mpeCommSetStatusSafi = _FsMIBgp4mpeCommSetStatusSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 3, 1, 2),
    _FsMIBgp4mpeCommSetStatusSafi_Type()
)
fsMIBgp4mpeCommSetStatusSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeCommSetStatusSafi.setStatus("current")
_FsMIBgp4mpeCommSetStatusIpNetwork_Type = InetAddress
_FsMIBgp4mpeCommSetStatusIpNetwork_Object = MibTableColumn
fsMIBgp4mpeCommSetStatusIpNetwork = _FsMIBgp4mpeCommSetStatusIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 3, 1, 3),
    _FsMIBgp4mpeCommSetStatusIpNetwork_Type()
)
fsMIBgp4mpeCommSetStatusIpNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeCommSetStatusIpNetwork.setStatus("current")


class _FsMIBgp4mpeCommSetStatusIpPrefixLen_Type(Integer32):
    """Custom type fsMIBgp4mpeCommSetStatusIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsMIBgp4mpeCommSetStatusIpPrefixLen_Type.__name__ = "Integer32"
_FsMIBgp4mpeCommSetStatusIpPrefixLen_Object = MibTableColumn
fsMIBgp4mpeCommSetStatusIpPrefixLen = _FsMIBgp4mpeCommSetStatusIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 3, 1, 4),
    _FsMIBgp4mpeCommSetStatusIpPrefixLen_Type()
)
fsMIBgp4mpeCommSetStatusIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeCommSetStatusIpPrefixLen.setStatus("current")


class _FsMIBgp4mpeCommSetStatus_Type(Integer32):
    """Custom type fsMIBgp4mpeCommSetStatus based on Integer32"""
    defaultValue = 4

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
          ("set", 2),
          ("setnone", 3),
          ("modify", 4))
    )


_FsMIBgp4mpeCommSetStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpeCommSetStatus_Object = MibTableColumn
fsMIBgp4mpeCommSetStatus = _FsMIBgp4mpeCommSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 3, 1, 5),
    _FsMIBgp4mpeCommSetStatus_Type()
)
fsMIBgp4mpeCommSetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4mpeCommSetStatus.setStatus("current")
_FsMIBgp4mpeCommSetStatusRowStatus_Type = RowStatus
_FsMIBgp4mpeCommSetStatusRowStatus_Object = MibTableColumn
fsMIBgp4mpeCommSetStatusRowStatus = _FsMIBgp4mpeCommSetStatusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 30, 3, 1, 6),
    _FsMIBgp4mpeCommSetStatusRowStatus_Type()
)
fsMIBgp4mpeCommSetStatusRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4mpeCommSetStatusRowStatus.setStatus("current")
_FsMIBgp4MpeExtComm_ObjectIdentity = ObjectIdentity
fsMIBgp4MpeExtComm = _FsMIBgp4MpeExtComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31)
)
_FsMIBgp4MpeExtCommRouteAddExtCommTable_Object = MibTable
fsMIBgp4MpeExtCommRouteAddExtCommTable = _FsMIBgp4MpeExtCommRouteAddExtCommTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 1)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeExtCommRouteAddExtCommTable.setStatus("current")
_FsMIBgp4MpeExtCommRouteAddExtCommEntry_Object = MibTableRow
fsMIBgp4MpeExtCommRouteAddExtCommEntry = _FsMIBgp4MpeExtCommRouteAddExtCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 1, 1)
)
fsMIBgp4MpeExtCommRouteAddExtCommEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeAddExtCommRtAfi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeAddExtCommRtSafi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeAddExtCommIpNetwork"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeAddExtCommIpPrefixLen"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeAddExtCommVal"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeExtCommRouteAddExtCommEntry.setStatus("current")
_FsMIBgp4mpeAddExtCommRtAfi_Type = InetAddressType
_FsMIBgp4mpeAddExtCommRtAfi_Object = MibTableColumn
fsMIBgp4mpeAddExtCommRtAfi = _FsMIBgp4mpeAddExtCommRtAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 1, 1, 1),
    _FsMIBgp4mpeAddExtCommRtAfi_Type()
)
fsMIBgp4mpeAddExtCommRtAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAddExtCommRtAfi.setStatus("current")
_FsMIBgp4mpeAddExtCommRtSafi_Type = BgpSafi
_FsMIBgp4mpeAddExtCommRtSafi_Object = MibTableColumn
fsMIBgp4mpeAddExtCommRtSafi = _FsMIBgp4mpeAddExtCommRtSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 1, 1, 2),
    _FsMIBgp4mpeAddExtCommRtSafi_Type()
)
fsMIBgp4mpeAddExtCommRtSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAddExtCommRtSafi.setStatus("current")
_FsMIBgp4mpeAddExtCommIpNetwork_Type = InetAddress
_FsMIBgp4mpeAddExtCommIpNetwork_Object = MibTableColumn
fsMIBgp4mpeAddExtCommIpNetwork = _FsMIBgp4mpeAddExtCommIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 1, 1, 3),
    _FsMIBgp4mpeAddExtCommIpNetwork_Type()
)
fsMIBgp4mpeAddExtCommIpNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAddExtCommIpNetwork.setStatus("current")


class _FsMIBgp4mpeAddExtCommIpPrefixLen_Type(Integer32):
    """Custom type fsMIBgp4mpeAddExtCommIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsMIBgp4mpeAddExtCommIpPrefixLen_Type.__name__ = "Integer32"
_FsMIBgp4mpeAddExtCommIpPrefixLen_Object = MibTableColumn
fsMIBgp4mpeAddExtCommIpPrefixLen = _FsMIBgp4mpeAddExtCommIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 1, 1, 4),
    _FsMIBgp4mpeAddExtCommIpPrefixLen_Type()
)
fsMIBgp4mpeAddExtCommIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAddExtCommIpPrefixLen.setStatus("current")


class _FsMIBgp4mpeAddExtCommVal_Type(OctetString):
    """Custom type fsMIBgp4mpeAddExtCommVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsMIBgp4mpeAddExtCommVal_Type.__name__ = "OctetString"
_FsMIBgp4mpeAddExtCommVal_Object = MibTableColumn
fsMIBgp4mpeAddExtCommVal = _FsMIBgp4mpeAddExtCommVal_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 1, 1, 5),
    _FsMIBgp4mpeAddExtCommVal_Type()
)
fsMIBgp4mpeAddExtCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAddExtCommVal.setStatus("current")
_FsMIBgp4mpeAddExtCommRowStatus_Type = RowStatus
_FsMIBgp4mpeAddExtCommRowStatus_Object = MibTableColumn
fsMIBgp4mpeAddExtCommRowStatus = _FsMIBgp4mpeAddExtCommRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 1, 1, 6),
    _FsMIBgp4mpeAddExtCommRowStatus_Type()
)
fsMIBgp4mpeAddExtCommRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4mpeAddExtCommRowStatus.setStatus("current")
_FsMIBgp4MpeExtCommRouteDeleteExtCommTable_Object = MibTable
fsMIBgp4MpeExtCommRouteDeleteExtCommTable = _FsMIBgp4MpeExtCommRouteDeleteExtCommTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 2)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeExtCommRouteDeleteExtCommTable.setStatus("current")
_FsMIBgp4MpeExtCommRouteDeleteExtCommEntry_Object = MibTableRow
fsMIBgp4MpeExtCommRouteDeleteExtCommEntry = _FsMIBgp4MpeExtCommRouteDeleteExtCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 2, 1)
)
fsMIBgp4MpeExtCommRouteDeleteExtCommEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeDeleteExtCommRtAfi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeDeleteExtCommRtSafi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeDeleteExtCommIpNetwork"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeDeleteExtCommIpPrefixLen"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeDeleteExtCommVal"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeExtCommRouteDeleteExtCommEntry.setStatus("current")
_FsMIBgp4mpeDeleteExtCommRtAfi_Type = InetAddressType
_FsMIBgp4mpeDeleteExtCommRtAfi_Object = MibTableColumn
fsMIBgp4mpeDeleteExtCommRtAfi = _FsMIBgp4mpeDeleteExtCommRtAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 2, 1, 1),
    _FsMIBgp4mpeDeleteExtCommRtAfi_Type()
)
fsMIBgp4mpeDeleteExtCommRtAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeDeleteExtCommRtAfi.setStatus("current")
_FsMIBgp4mpeDeleteExtCommRtSafi_Type = BgpSafi
_FsMIBgp4mpeDeleteExtCommRtSafi_Object = MibTableColumn
fsMIBgp4mpeDeleteExtCommRtSafi = _FsMIBgp4mpeDeleteExtCommRtSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 2, 1, 2),
    _FsMIBgp4mpeDeleteExtCommRtSafi_Type()
)
fsMIBgp4mpeDeleteExtCommRtSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeDeleteExtCommRtSafi.setStatus("current")
_FsMIBgp4mpeDeleteExtCommIpNetwork_Type = InetAddress
_FsMIBgp4mpeDeleteExtCommIpNetwork_Object = MibTableColumn
fsMIBgp4mpeDeleteExtCommIpNetwork = _FsMIBgp4mpeDeleteExtCommIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 2, 1, 3),
    _FsMIBgp4mpeDeleteExtCommIpNetwork_Type()
)
fsMIBgp4mpeDeleteExtCommIpNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeDeleteExtCommIpNetwork.setStatus("current")


class _FsMIBgp4mpeDeleteExtCommIpPrefixLen_Type(Integer32):
    """Custom type fsMIBgp4mpeDeleteExtCommIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsMIBgp4mpeDeleteExtCommIpPrefixLen_Type.__name__ = "Integer32"
_FsMIBgp4mpeDeleteExtCommIpPrefixLen_Object = MibTableColumn
fsMIBgp4mpeDeleteExtCommIpPrefixLen = _FsMIBgp4mpeDeleteExtCommIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 2, 1, 4),
    _FsMIBgp4mpeDeleteExtCommIpPrefixLen_Type()
)
fsMIBgp4mpeDeleteExtCommIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeDeleteExtCommIpPrefixLen.setStatus("current")


class _FsMIBgp4mpeDeleteExtCommVal_Type(OctetString):
    """Custom type fsMIBgp4mpeDeleteExtCommVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsMIBgp4mpeDeleteExtCommVal_Type.__name__ = "OctetString"
_FsMIBgp4mpeDeleteExtCommVal_Object = MibTableColumn
fsMIBgp4mpeDeleteExtCommVal = _FsMIBgp4mpeDeleteExtCommVal_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 2, 1, 5),
    _FsMIBgp4mpeDeleteExtCommVal_Type()
)
fsMIBgp4mpeDeleteExtCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeDeleteExtCommVal.setStatus("current")
_FsMIBgp4mpeDeleteExtCommRowStatus_Type = RowStatus
_FsMIBgp4mpeDeleteExtCommRowStatus_Object = MibTableColumn
fsMIBgp4mpeDeleteExtCommRowStatus = _FsMIBgp4mpeDeleteExtCommRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 2, 1, 6),
    _FsMIBgp4mpeDeleteExtCommRowStatus_Type()
)
fsMIBgp4mpeDeleteExtCommRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4mpeDeleteExtCommRowStatus.setStatus("current")
_FsMIBgp4MpeExtCommRouteExtCommSetStatusTable_Object = MibTable
fsMIBgp4MpeExtCommRouteExtCommSetStatusTable = _FsMIBgp4MpeExtCommRouteExtCommSetStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 3)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeExtCommRouteExtCommSetStatusTable.setStatus("current")
_FsMIBgp4MpeExtCommRouteExtCommSetStatusEntry_Object = MibTableRow
fsMIBgp4MpeExtCommRouteExtCommSetStatusEntry = _FsMIBgp4MpeExtCommRouteExtCommSetStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 3, 1)
)
fsMIBgp4MpeExtCommRouteExtCommSetStatusEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeExtCommSetStatusRtAfi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeExtCommSetStatusRtSafi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeExtCommSetStatusIpNetwork"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeExtCommSetStatusIpPrefixLen"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeExtCommRouteExtCommSetStatusEntry.setStatus("current")
_FsMIBgp4mpeExtCommSetStatusRtAfi_Type = InetAddressType
_FsMIBgp4mpeExtCommSetStatusRtAfi_Object = MibTableColumn
fsMIBgp4mpeExtCommSetStatusRtAfi = _FsMIBgp4mpeExtCommSetStatusRtAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 3, 1, 1),
    _FsMIBgp4mpeExtCommSetStatusRtAfi_Type()
)
fsMIBgp4mpeExtCommSetStatusRtAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeExtCommSetStatusRtAfi.setStatus("current")
_FsMIBgp4mpeExtCommSetStatusRtSafi_Type = BgpSafi
_FsMIBgp4mpeExtCommSetStatusRtSafi_Object = MibTableColumn
fsMIBgp4mpeExtCommSetStatusRtSafi = _FsMIBgp4mpeExtCommSetStatusRtSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 3, 1, 2),
    _FsMIBgp4mpeExtCommSetStatusRtSafi_Type()
)
fsMIBgp4mpeExtCommSetStatusRtSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeExtCommSetStatusRtSafi.setStatus("current")
_FsMIBgp4mpeExtCommSetStatusIpNetwork_Type = InetAddress
_FsMIBgp4mpeExtCommSetStatusIpNetwork_Object = MibTableColumn
fsMIBgp4mpeExtCommSetStatusIpNetwork = _FsMIBgp4mpeExtCommSetStatusIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 3, 1, 3),
    _FsMIBgp4mpeExtCommSetStatusIpNetwork_Type()
)
fsMIBgp4mpeExtCommSetStatusIpNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeExtCommSetStatusIpNetwork.setStatus("current")


class _FsMIBgp4mpeExtCommSetStatusIpPrefixLen_Type(Integer32):
    """Custom type fsMIBgp4mpeExtCommSetStatusIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsMIBgp4mpeExtCommSetStatusIpPrefixLen_Type.__name__ = "Integer32"
_FsMIBgp4mpeExtCommSetStatusIpPrefixLen_Object = MibTableColumn
fsMIBgp4mpeExtCommSetStatusIpPrefixLen = _FsMIBgp4mpeExtCommSetStatusIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 3, 1, 4),
    _FsMIBgp4mpeExtCommSetStatusIpPrefixLen_Type()
)
fsMIBgp4mpeExtCommSetStatusIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeExtCommSetStatusIpPrefixLen.setStatus("current")


class _FsMIBgp4mpeExtCommSetStatus_Type(Integer32):
    """Custom type fsMIBgp4mpeExtCommSetStatus based on Integer32"""
    defaultValue = 4

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
          ("set", 2),
          ("setnone", 3),
          ("modify", 4))
    )


_FsMIBgp4mpeExtCommSetStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpeExtCommSetStatus_Object = MibTableColumn
fsMIBgp4mpeExtCommSetStatus = _FsMIBgp4mpeExtCommSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 3, 1, 5),
    _FsMIBgp4mpeExtCommSetStatus_Type()
)
fsMIBgp4mpeExtCommSetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4mpeExtCommSetStatus.setStatus("current")
_FsMIBgp4mpeExtCommSetStatusRowStatus_Type = RowStatus
_FsMIBgp4mpeExtCommSetStatusRowStatus_Object = MibTableColumn
fsMIBgp4mpeExtCommSetStatusRowStatus = _FsMIBgp4mpeExtCommSetStatusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 3, 1, 6),
    _FsMIBgp4mpeExtCommSetStatusRowStatus_Type()
)
fsMIBgp4mpeExtCommSetStatusRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4mpeExtCommSetStatusRowStatus.setStatus("current")
_FsMIBgp4MpePeerLinkBwTable_Object = MibTable
fsMIBgp4MpePeerLinkBwTable = _FsMIBgp4MpePeerLinkBwTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 4)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpePeerLinkBwTable.setStatus("current")
_FsMIBgp4MpePeerLinkBwEntry_Object = MibTableRow
fsMIBgp4MpePeerLinkBwEntry = _FsMIBgp4MpePeerLinkBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 4, 1)
)
fsMIBgp4MpePeerLinkBwEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpePeerLinkType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpePeerLinkRemAddr"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpePeerLinkBwEntry.setStatus("current")
_FsMIBgp4mpePeerLinkType_Type = InetAddressType
_FsMIBgp4mpePeerLinkType_Object = MibTableColumn
fsMIBgp4mpePeerLinkType = _FsMIBgp4mpePeerLinkType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 4, 1, 1),
    _FsMIBgp4mpePeerLinkType_Type()
)
fsMIBgp4mpePeerLinkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerLinkType.setStatus("current")
_FsMIBgp4mpePeerLinkRemAddr_Type = InetAddress
_FsMIBgp4mpePeerLinkRemAddr_Object = MibTableColumn
fsMIBgp4mpePeerLinkRemAddr = _FsMIBgp4mpePeerLinkRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 4, 1, 2),
    _FsMIBgp4mpePeerLinkRemAddr_Type()
)
fsMIBgp4mpePeerLinkRemAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerLinkRemAddr.setStatus("current")


class _FsMIBgp4mpeLinkBandWidth_Type(Unsigned32):
    """Custom type fsMIBgp4mpeLinkBandWidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7000, 4294967295),
    )


_FsMIBgp4mpeLinkBandWidth_Type.__name__ = "Unsigned32"
_FsMIBgp4mpeLinkBandWidth_Object = MibTableColumn
fsMIBgp4mpeLinkBandWidth = _FsMIBgp4mpeLinkBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 4, 1, 3),
    _FsMIBgp4mpeLinkBandWidth_Type()
)
fsMIBgp4mpeLinkBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4mpeLinkBandWidth.setStatus("current")
_FsMIBgp4mpePeerLinkBwRowStatus_Type = RowStatus
_FsMIBgp4mpePeerLinkBwRowStatus_Object = MibTableColumn
fsMIBgp4mpePeerLinkBwRowStatus = _FsMIBgp4mpePeerLinkBwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 31, 4, 1, 4),
    _FsMIBgp4mpePeerLinkBwRowStatus_Type()
)
fsMIBgp4mpePeerLinkBwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4mpePeerLinkBwRowStatus.setStatus("current")
_FsMIBgp4MpeCaps_ObjectIdentity = ObjectIdentity
fsMIBgp4MpeCaps = _FsMIBgp4MpeCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 32)
)
_FsMIBgp4MpeCapSupportedCapsTable_Object = MibTable
fsMIBgp4MpeCapSupportedCapsTable = _FsMIBgp4MpeCapSupportedCapsTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 32, 1)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeCapSupportedCapsTable.setStatus("current")
_FsMIBgp4MpeCapSupportedCapsEntry_Object = MibTableRow
fsMIBgp4MpeCapSupportedCapsEntry = _FsMIBgp4MpeCapSupportedCapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 32, 1, 1)
)
fsMIBgp4MpeCapSupportedCapsEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeCapPeerType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeCapPeerRemoteIpAddr"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeSupportedCapabilityCode"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeSupportedCapabilityLength"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeSupportedCapabilityValue"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeCapSupportedCapsEntry.setStatus("current")
_FsMIBgp4mpeCapPeerType_Type = InetAddressType
_FsMIBgp4mpeCapPeerType_Object = MibTableColumn
fsMIBgp4mpeCapPeerType = _FsMIBgp4mpeCapPeerType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 32, 1, 1, 1),
    _FsMIBgp4mpeCapPeerType_Type()
)
fsMIBgp4mpeCapPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeCapPeerType.setStatus("current")


class _FsMIBgp4mpeCapPeerRemoteIpAddr_Type(InetAddress):
    """Custom type fsMIBgp4mpeCapPeerRemoteIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_FsMIBgp4mpeCapPeerRemoteIpAddr_Type.__name__ = "InetAddress"
_FsMIBgp4mpeCapPeerRemoteIpAddr_Object = MibTableColumn
fsMIBgp4mpeCapPeerRemoteIpAddr = _FsMIBgp4mpeCapPeerRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 32, 1, 1, 2),
    _FsMIBgp4mpeCapPeerRemoteIpAddr_Type()
)
fsMIBgp4mpeCapPeerRemoteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeCapPeerRemoteIpAddr.setStatus("current")


class _FsMIBgp4mpeSupportedCapabilityCode_Type(Integer32):
    """Custom type fsMIBgp4mpeSupportedCapabilityCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIBgp4mpeSupportedCapabilityCode_Type.__name__ = "Integer32"
_FsMIBgp4mpeSupportedCapabilityCode_Object = MibTableColumn
fsMIBgp4mpeSupportedCapabilityCode = _FsMIBgp4mpeSupportedCapabilityCode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 32, 1, 1, 3),
    _FsMIBgp4mpeSupportedCapabilityCode_Type()
)
fsMIBgp4mpeSupportedCapabilityCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeSupportedCapabilityCode.setStatus("current")


class _FsMIBgp4mpeSupportedCapabilityLength_Type(Integer32):
    """Custom type fsMIBgp4mpeSupportedCapabilityLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 251),
    )


_FsMIBgp4mpeSupportedCapabilityLength_Type.__name__ = "Integer32"
_FsMIBgp4mpeSupportedCapabilityLength_Object = MibTableColumn
fsMIBgp4mpeSupportedCapabilityLength = _FsMIBgp4mpeSupportedCapabilityLength_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 32, 1, 1, 4),
    _FsMIBgp4mpeSupportedCapabilityLength_Type()
)
fsMIBgp4mpeSupportedCapabilityLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeSupportedCapabilityLength.setStatus("current")


class _FsMIBgp4mpeSupportedCapabilityValue_Type(OctetString):
    """Custom type fsMIBgp4mpeSupportedCapabilityValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FsMIBgp4mpeSupportedCapabilityValue_Type.__name__ = "OctetString"
_FsMIBgp4mpeSupportedCapabilityValue_Object = MibTableColumn
fsMIBgp4mpeSupportedCapabilityValue = _FsMIBgp4mpeSupportedCapabilityValue_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 32, 1, 1, 5),
    _FsMIBgp4mpeSupportedCapabilityValue_Type()
)
fsMIBgp4mpeSupportedCapabilityValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeSupportedCapabilityValue.setStatus("current")
_FsMIBgp4mpeCapSupportedCapsRowStatus_Type = RowStatus
_FsMIBgp4mpeCapSupportedCapsRowStatus_Object = MibTableColumn
fsMIBgp4mpeCapSupportedCapsRowStatus = _FsMIBgp4mpeCapSupportedCapsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 32, 1, 1, 6),
    _FsMIBgp4mpeCapSupportedCapsRowStatus_Type()
)
fsMIBgp4mpeCapSupportedCapsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4mpeCapSupportedCapsRowStatus.setStatus("current")


class _FsMIBgp4mpeCapAnnouncedStatus_Type(Integer32):
    """Custom type fsMIBgp4mpeCapAnnouncedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("announced", 1),
          ("notAnnounced", 2))
    )


_FsMIBgp4mpeCapAnnouncedStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpeCapAnnouncedStatus_Object = MibTableColumn
fsMIBgp4mpeCapAnnouncedStatus = _FsMIBgp4mpeCapAnnouncedStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 32, 1, 1, 7),
    _FsMIBgp4mpeCapAnnouncedStatus_Type()
)
fsMIBgp4mpeCapAnnouncedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeCapAnnouncedStatus.setStatus("current")


class _FsMIBgp4mpeCapReceivedStatus_Type(Integer32):
    """Custom type fsMIBgp4mpeCapReceivedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("received", 1),
          ("notReceived", 2))
    )


_FsMIBgp4mpeCapReceivedStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpeCapReceivedStatus_Object = MibTableColumn
fsMIBgp4mpeCapReceivedStatus = _FsMIBgp4mpeCapReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 32, 1, 1, 8),
    _FsMIBgp4mpeCapReceivedStatus_Type()
)
fsMIBgp4mpeCapReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeCapReceivedStatus.setStatus("current")


class _FsMIBgp4mpeCapNegotiatedStatus_Type(Integer32):
    """Custom type fsMIBgp4mpeCapNegotiatedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negotiated", 1),
          ("notNegotiated", 2))
    )


_FsMIBgp4mpeCapNegotiatedStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpeCapNegotiatedStatus_Object = MibTableColumn
fsMIBgp4mpeCapNegotiatedStatus = _FsMIBgp4mpeCapNegotiatedStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 32, 1, 1, 9),
    _FsMIBgp4mpeCapNegotiatedStatus_Type()
)
fsMIBgp4mpeCapNegotiatedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeCapNegotiatedStatus.setStatus("current")


class _FsMIBgp4mpeCapConfiguredStatus_Type(Integer32):
    """Custom type fsMIBgp4mpeCapConfiguredStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("automatic", 2))
    )


_FsMIBgp4mpeCapConfiguredStatus_Type.__name__ = "Integer32"
_FsMIBgp4mpeCapConfiguredStatus_Object = MibTableColumn
fsMIBgp4mpeCapConfiguredStatus = _FsMIBgp4mpeCapConfiguredStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 32, 1, 1, 10),
    _FsMIBgp4mpeCapConfiguredStatus_Type()
)
fsMIBgp4mpeCapConfiguredStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeCapConfiguredStatus.setStatus("current")
_FsMIBgp4MpeRtRefresh_ObjectIdentity = ObjectIdentity
fsMIBgp4MpeRtRefresh = _FsMIBgp4MpeRtRefresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33)
)
_FsMIBgp4MpeRtRefreshInboundTable_Object = MibTable
fsMIBgp4MpeRtRefreshInboundTable = _FsMIBgp4MpeRtRefreshInboundTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33, 1)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeRtRefreshInboundTable.setStatus("current")
_FsMIBgp4MpeRtRefreshInboundEntry_Object = MibTableRow
fsMIBgp4MpeRtRefreshInboundEntry = _FsMIBgp4MpeRtRefreshInboundEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33, 1, 1)
)
fsMIBgp4MpeRtRefreshInboundEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeRtRefreshInboundPeerType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeRtRefreshInboundPeerAddr"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeRtRefreshInboundAfi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeRtRefreshInboundSafi"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeRtRefreshInboundEntry.setStatus("current")
_FsMIBgp4mpeRtRefreshInboundPeerType_Type = InetAddressType
_FsMIBgp4mpeRtRefreshInboundPeerType_Object = MibTableColumn
fsMIBgp4mpeRtRefreshInboundPeerType = _FsMIBgp4mpeRtRefreshInboundPeerType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33, 1, 1, 1),
    _FsMIBgp4mpeRtRefreshInboundPeerType_Type()
)
fsMIBgp4mpeRtRefreshInboundPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRtRefreshInboundPeerType.setStatus("current")
_FsMIBgp4mpeRtRefreshInboundPeerAddr_Type = InetAddress
_FsMIBgp4mpeRtRefreshInboundPeerAddr_Object = MibTableColumn
fsMIBgp4mpeRtRefreshInboundPeerAddr = _FsMIBgp4mpeRtRefreshInboundPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33, 1, 1, 2),
    _FsMIBgp4mpeRtRefreshInboundPeerAddr_Type()
)
fsMIBgp4mpeRtRefreshInboundPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRtRefreshInboundPeerAddr.setStatus("current")
_FsMIBgp4mpeRtRefreshInboundAfi_Type = InetAddressType
_FsMIBgp4mpeRtRefreshInboundAfi_Object = MibTableColumn
fsMIBgp4mpeRtRefreshInboundAfi = _FsMIBgp4mpeRtRefreshInboundAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33, 1, 1, 3),
    _FsMIBgp4mpeRtRefreshInboundAfi_Type()
)
fsMIBgp4mpeRtRefreshInboundAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRtRefreshInboundAfi.setStatus("current")
_FsMIBgp4mpeRtRefreshInboundSafi_Type = BgpSafi
_FsMIBgp4mpeRtRefreshInboundSafi_Object = MibTableColumn
fsMIBgp4mpeRtRefreshInboundSafi = _FsMIBgp4mpeRtRefreshInboundSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33, 1, 1, 4),
    _FsMIBgp4mpeRtRefreshInboundSafi_Type()
)
fsMIBgp4mpeRtRefreshInboundSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRtRefreshInboundSafi.setStatus("current")


class _FsMIBgp4mpeRtRefreshInboundRequest_Type(Integer32):
    """Custom type fsMIBgp4mpeRtRefreshInboundRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_FsMIBgp4mpeRtRefreshInboundRequest_Type.__name__ = "Integer32"
_FsMIBgp4mpeRtRefreshInboundRequest_Object = MibTableColumn
fsMIBgp4mpeRtRefreshInboundRequest = _FsMIBgp4mpeRtRefreshInboundRequest_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33, 1, 1, 5),
    _FsMIBgp4mpeRtRefreshInboundRequest_Type()
)
fsMIBgp4mpeRtRefreshInboundRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRtRefreshInboundRequest.setStatus("current")


class _FsMIBgp4mpeRtRefreshInboundPrefixFilter_Type(Integer32):
    """Custom type fsMIBgp4mpeRtRefreshInboundPrefixFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_FsMIBgp4mpeRtRefreshInboundPrefixFilter_Type.__name__ = "Integer32"
_FsMIBgp4mpeRtRefreshInboundPrefixFilter_Object = MibTableColumn
fsMIBgp4mpeRtRefreshInboundPrefixFilter = _FsMIBgp4mpeRtRefreshInboundPrefixFilter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33, 1, 1, 6),
    _FsMIBgp4mpeRtRefreshInboundPrefixFilter_Type()
)
fsMIBgp4mpeRtRefreshInboundPrefixFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRtRefreshInboundPrefixFilter.setStatus("current")
_FsMIBgp4MpeRtRefreshStatisticsTable_Object = MibTable
fsMIBgp4MpeRtRefreshStatisticsTable = _FsMIBgp4MpeRtRefreshStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33, 2)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeRtRefreshStatisticsTable.setStatus("current")
_FsMIBgp4MpeRtRefreshStatisticsEntry_Object = MibTableRow
fsMIBgp4MpeRtRefreshStatisticsEntry = _FsMIBgp4MpeRtRefreshStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33, 2, 1)
)
fsMIBgp4MpeRtRefreshStatisticsEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeRtRefreshStatisticsPeerType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeRtRefreshStatisticsPeerAddr"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeRtRefreshStatisticsAfi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeRtRefreshStatisticsSafi"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeRtRefreshStatisticsEntry.setStatus("current")
_FsMIBgp4mpeRtRefreshStatisticsPeerType_Type = InetAddressType
_FsMIBgp4mpeRtRefreshStatisticsPeerType_Object = MibTableColumn
fsMIBgp4mpeRtRefreshStatisticsPeerType = _FsMIBgp4mpeRtRefreshStatisticsPeerType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33, 2, 1, 1),
    _FsMIBgp4mpeRtRefreshStatisticsPeerType_Type()
)
fsMIBgp4mpeRtRefreshStatisticsPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRtRefreshStatisticsPeerType.setStatus("current")
_FsMIBgp4mpeRtRefreshStatisticsPeerAddr_Type = InetAddress
_FsMIBgp4mpeRtRefreshStatisticsPeerAddr_Object = MibTableColumn
fsMIBgp4mpeRtRefreshStatisticsPeerAddr = _FsMIBgp4mpeRtRefreshStatisticsPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33, 2, 1, 2),
    _FsMIBgp4mpeRtRefreshStatisticsPeerAddr_Type()
)
fsMIBgp4mpeRtRefreshStatisticsPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRtRefreshStatisticsPeerAddr.setStatus("current")
_FsMIBgp4mpeRtRefreshStatisticsAfi_Type = InetAddressType
_FsMIBgp4mpeRtRefreshStatisticsAfi_Object = MibTableColumn
fsMIBgp4mpeRtRefreshStatisticsAfi = _FsMIBgp4mpeRtRefreshStatisticsAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33, 2, 1, 3),
    _FsMIBgp4mpeRtRefreshStatisticsAfi_Type()
)
fsMIBgp4mpeRtRefreshStatisticsAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRtRefreshStatisticsAfi.setStatus("current")
_FsMIBgp4mpeRtRefreshStatisticsSafi_Type = BgpSafi
_FsMIBgp4mpeRtRefreshStatisticsSafi_Object = MibTableColumn
fsMIBgp4mpeRtRefreshStatisticsSafi = _FsMIBgp4mpeRtRefreshStatisticsSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33, 2, 1, 4),
    _FsMIBgp4mpeRtRefreshStatisticsSafi_Type()
)
fsMIBgp4mpeRtRefreshStatisticsSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRtRefreshStatisticsSafi.setStatus("current")
_FsMIBgp4mpeRtRefreshStatisticsRtRefMsgSentCntr_Type = Counter32
_FsMIBgp4mpeRtRefreshStatisticsRtRefMsgSentCntr_Object = MibTableColumn
fsMIBgp4mpeRtRefreshStatisticsRtRefMsgSentCntr = _FsMIBgp4mpeRtRefreshStatisticsRtRefMsgSentCntr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33, 2, 1, 5),
    _FsMIBgp4mpeRtRefreshStatisticsRtRefMsgSentCntr_Type()
)
fsMIBgp4mpeRtRefreshStatisticsRtRefMsgSentCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRtRefreshStatisticsRtRefMsgSentCntr.setStatus("current")
_FsMIBgp4mpeRtRefreshStatisticsRtRefMsgTxErrCntr_Type = Counter32
_FsMIBgp4mpeRtRefreshStatisticsRtRefMsgTxErrCntr_Object = MibTableColumn
fsMIBgp4mpeRtRefreshStatisticsRtRefMsgTxErrCntr = _FsMIBgp4mpeRtRefreshStatisticsRtRefMsgTxErrCntr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33, 2, 1, 6),
    _FsMIBgp4mpeRtRefreshStatisticsRtRefMsgTxErrCntr_Type()
)
fsMIBgp4mpeRtRefreshStatisticsRtRefMsgTxErrCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRtRefreshStatisticsRtRefMsgTxErrCntr.setStatus("current")
_FsMIBgp4mpeRtRefreshStatisticsRtRefMsgRcvdCntr_Type = Counter32
_FsMIBgp4mpeRtRefreshStatisticsRtRefMsgRcvdCntr_Object = MibTableColumn
fsMIBgp4mpeRtRefreshStatisticsRtRefMsgRcvdCntr = _FsMIBgp4mpeRtRefreshStatisticsRtRefMsgRcvdCntr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33, 2, 1, 7),
    _FsMIBgp4mpeRtRefreshStatisticsRtRefMsgRcvdCntr_Type()
)
fsMIBgp4mpeRtRefreshStatisticsRtRefMsgRcvdCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRtRefreshStatisticsRtRefMsgRcvdCntr.setStatus("current")
_FsMIBgp4mpeRtRefreshStatisticsRtRefMsgInvalidCntr_Type = Counter32
_FsMIBgp4mpeRtRefreshStatisticsRtRefMsgInvalidCntr_Object = MibTableColumn
fsMIBgp4mpeRtRefreshStatisticsRtRefMsgInvalidCntr = _FsMIBgp4mpeRtRefreshStatisticsRtRefMsgInvalidCntr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 33, 2, 1, 8),
    _FsMIBgp4mpeRtRefreshStatisticsRtRefMsgInvalidCntr_Type()
)
fsMIBgp4mpeRtRefreshStatisticsRtRefMsgInvalidCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4mpeRtRefreshStatisticsRtRefMsgInvalidCntr.setStatus("current")
_FsMIBgp4MpeSoftReconfigOut_ObjectIdentity = ObjectIdentity
fsMIBgp4MpeSoftReconfigOut = _FsMIBgp4MpeSoftReconfigOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 34)
)
_FsMIBgp4MpeSoftReconfigOutboundTable_Object = MibTable
fsMIBgp4MpeSoftReconfigOutboundTable = _FsMIBgp4MpeSoftReconfigOutboundTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 34, 1)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeSoftReconfigOutboundTable.setStatus("current")
_FsMIBgp4MpeSoftReconfigOutboundEntry_Object = MibTableRow
fsMIBgp4MpeSoftReconfigOutboundEntry = _FsMIBgp4MpeSoftReconfigOutboundEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 34, 1, 1)
)
fsMIBgp4MpeSoftReconfigOutboundEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeSoftReconfigOutboundPeerType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeSoftReconfigOutboundPeerAddr"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeSoftReconfigOutboundAfi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4mpeSoftReconfigOutboundSafi"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpeSoftReconfigOutboundEntry.setStatus("current")
_FsMIBgp4mpeSoftReconfigOutboundPeerType_Type = InetAddressType
_FsMIBgp4mpeSoftReconfigOutboundPeerType_Object = MibTableColumn
fsMIBgp4mpeSoftReconfigOutboundPeerType = _FsMIBgp4mpeSoftReconfigOutboundPeerType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 34, 1, 1, 1),
    _FsMIBgp4mpeSoftReconfigOutboundPeerType_Type()
)
fsMIBgp4mpeSoftReconfigOutboundPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeSoftReconfigOutboundPeerType.setStatus("current")
_FsMIBgp4mpeSoftReconfigOutboundPeerAddr_Type = InetAddress
_FsMIBgp4mpeSoftReconfigOutboundPeerAddr_Object = MibTableColumn
fsMIBgp4mpeSoftReconfigOutboundPeerAddr = _FsMIBgp4mpeSoftReconfigOutboundPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 34, 1, 1, 2),
    _FsMIBgp4mpeSoftReconfigOutboundPeerAddr_Type()
)
fsMIBgp4mpeSoftReconfigOutboundPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeSoftReconfigOutboundPeerAddr.setStatus("current")
_FsMIBgp4mpeSoftReconfigOutboundAfi_Type = InetAddressType
_FsMIBgp4mpeSoftReconfigOutboundAfi_Object = MibTableColumn
fsMIBgp4mpeSoftReconfigOutboundAfi = _FsMIBgp4mpeSoftReconfigOutboundAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 34, 1, 1, 3),
    _FsMIBgp4mpeSoftReconfigOutboundAfi_Type()
)
fsMIBgp4mpeSoftReconfigOutboundAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeSoftReconfigOutboundAfi.setStatus("current")
_FsMIBgp4mpeSoftReconfigOutboundSafi_Type = BgpSafi
_FsMIBgp4mpeSoftReconfigOutboundSafi_Object = MibTableColumn
fsMIBgp4mpeSoftReconfigOutboundSafi = _FsMIBgp4mpeSoftReconfigOutboundSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 34, 1, 1, 4),
    _FsMIBgp4mpeSoftReconfigOutboundSafi_Type()
)
fsMIBgp4mpeSoftReconfigOutboundSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4mpeSoftReconfigOutboundSafi.setStatus("current")


class _FsMIBgp4mpeSoftReconfigOutboundRequest_Type(Integer32):
    """Custom type fsMIBgp4mpeSoftReconfigOutboundRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_FsMIBgp4mpeSoftReconfigOutboundRequest_Type.__name__ = "Integer32"
_FsMIBgp4mpeSoftReconfigOutboundRequest_Object = MibTableColumn
fsMIBgp4mpeSoftReconfigOutboundRequest = _FsMIBgp4mpeSoftReconfigOutboundRequest_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 34, 1, 1, 5),
    _FsMIBgp4mpeSoftReconfigOutboundRequest_Type()
)
fsMIBgp4mpeSoftReconfigOutboundRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4mpeSoftReconfigOutboundRequest.setStatus("current")
_FsMIBgp4MpePrefixCountersTable_Object = MibTable
fsMIBgp4MpePrefixCountersTable = _FsMIBgp4MpePrefixCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 35)
)
if mibBuilder.loadTexts:
    fsMIBgp4MpePrefixCountersTable.setStatus("current")
_FsMIBgp4MpePrefixCountersEntry_Object = MibTableRow
fsMIBgp4MpePrefixCountersEntry = _FsMIBgp4MpePrefixCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 35, 1)
)
fsMIBgp4MpePrefixCountersEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4MpePeerRemoteAddrType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4MpePeerRemoteAddr"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4MpePrefixCountersAfi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4MpePrefixCountersSafi"),
)
if mibBuilder.loadTexts:
    fsMIBgp4MpePrefixCountersEntry.setStatus("current")
_FsMIBgp4MpePeerRemoteAddrType_Type = InetAddressType
_FsMIBgp4MpePeerRemoteAddrType_Object = MibTableColumn
fsMIBgp4MpePeerRemoteAddrType = _FsMIBgp4MpePeerRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 35, 1, 1),
    _FsMIBgp4MpePeerRemoteAddrType_Type()
)
fsMIBgp4MpePeerRemoteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4MpePeerRemoteAddrType.setStatus("current")
_FsMIBgp4MpePeerRemoteAddr_Type = InetAddress
_FsMIBgp4MpePeerRemoteAddr_Object = MibTableColumn
fsMIBgp4MpePeerRemoteAddr = _FsMIBgp4MpePeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 35, 1, 2),
    _FsMIBgp4MpePeerRemoteAddr_Type()
)
fsMIBgp4MpePeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4MpePeerRemoteAddr.setStatus("current")
_FsMIBgp4MpePrefixCountersAfi_Type = InetAddressType
_FsMIBgp4MpePrefixCountersAfi_Object = MibTableColumn
fsMIBgp4MpePrefixCountersAfi = _FsMIBgp4MpePrefixCountersAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 35, 1, 3),
    _FsMIBgp4MpePrefixCountersAfi_Type()
)
fsMIBgp4MpePrefixCountersAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4MpePrefixCountersAfi.setStatus("current")
_FsMIBgp4MpePrefixCountersSafi_Type = BgpSafi
_FsMIBgp4MpePrefixCountersSafi_Object = MibTableColumn
fsMIBgp4MpePrefixCountersSafi = _FsMIBgp4MpePrefixCountersSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 35, 1, 4),
    _FsMIBgp4MpePrefixCountersSafi_Type()
)
fsMIBgp4MpePrefixCountersSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4MpePrefixCountersSafi.setStatus("current")
_FsMIBgp4MpePrefixCountersPrefixesReceived_Type = Counter32
_FsMIBgp4MpePrefixCountersPrefixesReceived_Object = MibTableColumn
fsMIBgp4MpePrefixCountersPrefixesReceived = _FsMIBgp4MpePrefixCountersPrefixesReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 35, 1, 5),
    _FsMIBgp4MpePrefixCountersPrefixesReceived_Type()
)
fsMIBgp4MpePrefixCountersPrefixesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4MpePrefixCountersPrefixesReceived.setStatus("current")
_FsMIBgp4MpePrefixCountersPrefixesSent_Type = Counter32
_FsMIBgp4MpePrefixCountersPrefixesSent_Object = MibTableColumn
fsMIBgp4MpePrefixCountersPrefixesSent = _FsMIBgp4MpePrefixCountersPrefixesSent_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 35, 1, 6),
    _FsMIBgp4MpePrefixCountersPrefixesSent_Type()
)
fsMIBgp4MpePrefixCountersPrefixesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4MpePrefixCountersPrefixesSent.setStatus("current")
_FsMIBgp4MpePrefixCountersWithdrawsReceived_Type = Counter32
_FsMIBgp4MpePrefixCountersWithdrawsReceived_Object = MibTableColumn
fsMIBgp4MpePrefixCountersWithdrawsReceived = _FsMIBgp4MpePrefixCountersWithdrawsReceived_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 35, 1, 7),
    _FsMIBgp4MpePrefixCountersWithdrawsReceived_Type()
)
fsMIBgp4MpePrefixCountersWithdrawsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4MpePrefixCountersWithdrawsReceived.setStatus("current")
_FsMIBgp4MpePrefixCountersWithdrawsSent_Type = Counter32
_FsMIBgp4MpePrefixCountersWithdrawsSent_Object = MibTableColumn
fsMIBgp4MpePrefixCountersWithdrawsSent = _FsMIBgp4MpePrefixCountersWithdrawsSent_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 35, 1, 8),
    _FsMIBgp4MpePrefixCountersWithdrawsSent_Type()
)
fsMIBgp4MpePrefixCountersWithdrawsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4MpePrefixCountersWithdrawsSent.setStatus("current")
_FsMIBgp4MpePrefixCountersInPrefixes_Type = Gauge32
_FsMIBgp4MpePrefixCountersInPrefixes_Object = MibTableColumn
fsMIBgp4MpePrefixCountersInPrefixes = _FsMIBgp4MpePrefixCountersInPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 35, 1, 9),
    _FsMIBgp4MpePrefixCountersInPrefixes_Type()
)
fsMIBgp4MpePrefixCountersInPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4MpePrefixCountersInPrefixes.setStatus("current")
_FsMIBgp4MpePrefixCountersInPrefixesAccepted_Type = Gauge32
_FsMIBgp4MpePrefixCountersInPrefixesAccepted_Object = MibTableColumn
fsMIBgp4MpePrefixCountersInPrefixesAccepted = _FsMIBgp4MpePrefixCountersInPrefixesAccepted_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 35, 1, 10),
    _FsMIBgp4MpePrefixCountersInPrefixesAccepted_Type()
)
fsMIBgp4MpePrefixCountersInPrefixesAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4MpePrefixCountersInPrefixesAccepted.setStatus("current")
_FsMIBgp4MpePrefixCountersInPrefixesRejected_Type = Gauge32
_FsMIBgp4MpePrefixCountersInPrefixesRejected_Object = MibTableColumn
fsMIBgp4MpePrefixCountersInPrefixesRejected = _FsMIBgp4MpePrefixCountersInPrefixesRejected_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 35, 1, 11),
    _FsMIBgp4MpePrefixCountersInPrefixesRejected_Type()
)
fsMIBgp4MpePrefixCountersInPrefixesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4MpePrefixCountersInPrefixesRejected.setStatus("current")
_FsMIBgp4MpePrefixCountersOutPrefixes_Type = Gauge32
_FsMIBgp4MpePrefixCountersOutPrefixes_Object = MibTableColumn
fsMIBgp4MpePrefixCountersOutPrefixes = _FsMIBgp4MpePrefixCountersOutPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 35, 1, 12),
    _FsMIBgp4MpePrefixCountersOutPrefixes_Type()
)
fsMIBgp4MpePrefixCountersOutPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4MpePrefixCountersOutPrefixes.setStatus("current")
_FsMIBgp4DistInOutRouteMap_ObjectIdentity = ObjectIdentity
fsMIBgp4DistInOutRouteMap = _FsMIBgp4DistInOutRouteMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 36)
)
_FsMIBgp4DistInOutRouteMapTable_Object = MibTable
fsMIBgp4DistInOutRouteMapTable = _FsMIBgp4DistInOutRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 36, 1)
)
if mibBuilder.loadTexts:
    fsMIBgp4DistInOutRouteMapTable.setStatus("current")
_FsMIBgp4DistInOutRouteMapEntry_Object = MibTableRow
fsMIBgp4DistInOutRouteMapEntry = _FsMIBgp4DistInOutRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 36, 1, 1)
)
fsMIBgp4DistInOutRouteMapEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4DistInOutRouteMapName"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4DistInOutRouteMapType"),
)
if mibBuilder.loadTexts:
    fsMIBgp4DistInOutRouteMapEntry.setStatus("current")


class _FsMIBgp4DistInOutRouteMapName_Type(DisplayString):
    """Custom type fsMIBgp4DistInOutRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsMIBgp4DistInOutRouteMapName_Type.__name__ = "DisplayString"
_FsMIBgp4DistInOutRouteMapName_Object = MibTableColumn
fsMIBgp4DistInOutRouteMapName = _FsMIBgp4DistInOutRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 36, 1, 1, 1),
    _FsMIBgp4DistInOutRouteMapName_Type()
)
fsMIBgp4DistInOutRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4DistInOutRouteMapName.setStatus("current")


class _FsMIBgp4DistInOutRouteMapType_Type(Integer32):
    """Custom type fsMIBgp4DistInOutRouteMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsMIBgp4DistInOutRouteMapType_Type.__name__ = "Integer32"
_FsMIBgp4DistInOutRouteMapType_Object = MibTableColumn
fsMIBgp4DistInOutRouteMapType = _FsMIBgp4DistInOutRouteMapType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 36, 1, 1, 2),
    _FsMIBgp4DistInOutRouteMapType_Type()
)
fsMIBgp4DistInOutRouteMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4DistInOutRouteMapType.setStatus("current")


class _FsMIBgp4DistInOutRouteMapValue_Type(Integer32):
    """Custom type fsMIBgp4DistInOutRouteMapValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsMIBgp4DistInOutRouteMapValue_Type.__name__ = "Integer32"
_FsMIBgp4DistInOutRouteMapValue_Object = MibTableColumn
fsMIBgp4DistInOutRouteMapValue = _FsMIBgp4DistInOutRouteMapValue_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 36, 1, 1, 3),
    _FsMIBgp4DistInOutRouteMapValue_Type()
)
fsMIBgp4DistInOutRouteMapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4DistInOutRouteMapValue.setStatus("current")
_FsMIBgp4DistInOutRouteMapRowStatus_Type = RowStatus
_FsMIBgp4DistInOutRouteMapRowStatus_Object = MibTableColumn
fsMIBgp4DistInOutRouteMapRowStatus = _FsMIBgp4DistInOutRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 36, 1, 1, 4),
    _FsMIBgp4DistInOutRouteMapRowStatus_Type()
)
fsMIBgp4DistInOutRouteMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4DistInOutRouteMapRowStatus.setStatus("current")
_FsMIBgp4Notification_ObjectIdentity = ObjectIdentity
fsMIBgp4Notification = _FsMIBgp4Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 37)
)
_FsMIBgp4Trap_ObjectIdentity = ObjectIdentity
fsMIBgp4Trap = _FsMIBgp4Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 37, 0)
)
_FsMIBgp4Objects_ObjectIdentity = ObjectIdentity
fsMIBgp4Objects = _FsMIBgp4Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 37, 1)
)
_FsMIBgp4TrapContextId_Type = Integer32
_FsMIBgp4TrapContextId_Object = MibScalar
fsMIBgp4TrapContextId = _FsMIBgp4TrapContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 37, 1, 1),
    _FsMIBgp4TrapContextId_Type()
)
fsMIBgp4TrapContextId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMIBgp4TrapContextId.setStatus("current")
_FsMIBgp4TrapRouteAddressType_Type = InetAddressType
_FsMIBgp4TrapRouteAddressType_Object = MibScalar
fsMIBgp4TrapRouteAddressType = _FsMIBgp4TrapRouteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 37, 1, 2),
    _FsMIBgp4TrapRouteAddressType_Type()
)
fsMIBgp4TrapRouteAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMIBgp4TrapRouteAddressType.setStatus("current")
_FsMIBgp4TrapRoutePrefix_Type = InetAddress
_FsMIBgp4TrapRoutePrefix_Object = MibScalar
fsMIBgp4TrapRoutePrefix = _FsMIBgp4TrapRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 37, 1, 3),
    _FsMIBgp4TrapRoutePrefix_Type()
)
fsMIBgp4TrapRoutePrefix.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMIBgp4TrapRoutePrefix.setStatus("current")
_FsMIBgp4NextHop_Type = InetAddress
_FsMIBgp4NextHop_Object = MibScalar
fsMIBgp4NextHop = _FsMIBgp4NextHop_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 37, 1, 4),
    _FsMIBgp4NextHop_Type()
)
fsMIBgp4NextHop.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMIBgp4NextHop.setStatus("current")
_FsMIBgp4TrapPeerAddrType_Type = InetAddressType
_FsMIBgp4TrapPeerAddrType_Object = MibScalar
fsMIBgp4TrapPeerAddrType = _FsMIBgp4TrapPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 37, 1, 5),
    _FsMIBgp4TrapPeerAddrType_Type()
)
fsMIBgp4TrapPeerAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMIBgp4TrapPeerAddrType.setStatus("current")
_FsMIBgp4TrapPeerAddr_Type = InetAddress
_FsMIBgp4TrapPeerAddr_Object = MibScalar
fsMIBgp4TrapPeerAddr = _FsMIBgp4TrapPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 37, 1, 6),
    _FsMIBgp4TrapPeerAddr_Type()
)
fsMIBgp4TrapPeerAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMIBgp4TrapPeerAddr.setStatus("current")
_FsMIBgp4NeighborRouteMap_ObjectIdentity = ObjectIdentity
fsMIBgp4NeighborRouteMap = _FsMIBgp4NeighborRouteMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 38)
)
_FsMIBgp4NeighborRouteMapTable_Object = MibTable
fsMIBgp4NeighborRouteMapTable = _FsMIBgp4NeighborRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 38, 1)
)
if mibBuilder.loadTexts:
    fsMIBgp4NeighborRouteMapTable.setStatus("current")
_FsMIBgp4NeighborRouteMapEntry_Object = MibTableRow
fsMIBgp4NeighborRouteMapEntry = _FsMIBgp4NeighborRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 38, 1, 1)
)
fsMIBgp4NeighborRouteMapEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4NeighborRouteMapPeerAddrType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4NeighborRouteMapPeer"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4NeighborRouteMapDirection"),
)
if mibBuilder.loadTexts:
    fsMIBgp4NeighborRouteMapEntry.setStatus("current")
_FsMIBgp4NeighborRouteMapPeerAddrType_Type = InetAddressType
_FsMIBgp4NeighborRouteMapPeerAddrType_Object = MibTableColumn
fsMIBgp4NeighborRouteMapPeerAddrType = _FsMIBgp4NeighborRouteMapPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 38, 1, 1, 1),
    _FsMIBgp4NeighborRouteMapPeerAddrType_Type()
)
fsMIBgp4NeighborRouteMapPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4NeighborRouteMapPeerAddrType.setStatus("current")
_FsMIBgp4NeighborRouteMapPeer_Type = InetAddress
_FsMIBgp4NeighborRouteMapPeer_Object = MibTableColumn
fsMIBgp4NeighborRouteMapPeer = _FsMIBgp4NeighborRouteMapPeer_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 38, 1, 1, 2),
    _FsMIBgp4NeighborRouteMapPeer_Type()
)
fsMIBgp4NeighborRouteMapPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4NeighborRouteMapPeer.setStatus("current")


class _FsMIBgp4NeighborRouteMapDirection_Type(Integer32):
    """Custom type fsMIBgp4NeighborRouteMapDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_FsMIBgp4NeighborRouteMapDirection_Type.__name__ = "Integer32"
_FsMIBgp4NeighborRouteMapDirection_Object = MibTableColumn
fsMIBgp4NeighborRouteMapDirection = _FsMIBgp4NeighborRouteMapDirection_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 38, 1, 1, 3),
    _FsMIBgp4NeighborRouteMapDirection_Type()
)
fsMIBgp4NeighborRouteMapDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4NeighborRouteMapDirection.setStatus("current")


class _FsMIBgp4NeighborRouteMapName_Type(DisplayString):
    """Custom type fsMIBgp4NeighborRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsMIBgp4NeighborRouteMapName_Type.__name__ = "DisplayString"
_FsMIBgp4NeighborRouteMapName_Object = MibTableColumn
fsMIBgp4NeighborRouteMapName = _FsMIBgp4NeighborRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 38, 1, 1, 4),
    _FsMIBgp4NeighborRouteMapName_Type()
)
fsMIBgp4NeighborRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4NeighborRouteMapName.setStatus("current")
_FsMIBgp4NeighborRouteMapRowStatus_Type = RowStatus
_FsMIBgp4NeighborRouteMapRowStatus_Object = MibTableColumn
fsMIBgp4NeighborRouteMapRowStatus = _FsMIBgp4NeighborRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 38, 1, 1, 5),
    _FsMIBgp4NeighborRouteMapRowStatus_Type()
)
fsMIBgp4NeighborRouteMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4NeighborRouteMapRowStatus.setStatus("current")
_FsMIBgp4PeerGroupTable_Object = MibTable
fsMIBgp4PeerGroupTable = _FsMIBgp4PeerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39)
)
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupTable.setStatus("current")
_FsMIBgp4PeerGroupEntry_Object = MibTableRow
fsMIBgp4PeerGroupEntry = _FsMIBgp4PeerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1)
)
fsMIBgp4PeerGroupEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4PeerGroupName"),
)
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupEntry.setStatus("current")


class _FsMIBgp4PeerGroupName_Type(DisplayString):
    """Custom type fsMIBgp4PeerGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsMIBgp4PeerGroupName_Type.__name__ = "DisplayString"
_FsMIBgp4PeerGroupName_Object = MibTableColumn
fsMIBgp4PeerGroupName = _FsMIBgp4PeerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 1),
    _FsMIBgp4PeerGroupName_Type()
)
fsMIBgp4PeerGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupName.setStatus("current")
_FsMIBgp4PeerGroupAddrType_Type = InetAddressType
_FsMIBgp4PeerGroupAddrType_Object = MibTableColumn
fsMIBgp4PeerGroupAddrType = _FsMIBgp4PeerGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 2),
    _FsMIBgp4PeerGroupAddrType_Type()
)
fsMIBgp4PeerGroupAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupAddrType.setStatus("current")


class _FsMIBgp4PeerGroupRemoteAs_Type(Unsigned32):
    """Custom type fsMIBgp4PeerGroupRemoteAs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIBgp4PeerGroupRemoteAs_Type.__name__ = "Unsigned32"
_FsMIBgp4PeerGroupRemoteAs_Object = MibTableColumn
fsMIBgp4PeerGroupRemoteAs = _FsMIBgp4PeerGroupRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 3),
    _FsMIBgp4PeerGroupRemoteAs_Type()
)
fsMIBgp4PeerGroupRemoteAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupRemoteAs.setStatus("current")


class _FsMIBgp4PeerGroupHoldTimeConfigured_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupHoldTimeConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_FsMIBgp4PeerGroupHoldTimeConfigured_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupHoldTimeConfigured_Object = MibTableColumn
fsMIBgp4PeerGroupHoldTimeConfigured = _FsMIBgp4PeerGroupHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 4),
    _FsMIBgp4PeerGroupHoldTimeConfigured_Type()
)
fsMIBgp4PeerGroupHoldTimeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupHoldTimeConfigured.setStatus("current")


class _FsMIBgp4PeerGroupKeepAliveConfigured_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupKeepAliveConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_FsMIBgp4PeerGroupKeepAliveConfigured_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupKeepAliveConfigured_Object = MibTableColumn
fsMIBgp4PeerGroupKeepAliveConfigured = _FsMIBgp4PeerGroupKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 5),
    _FsMIBgp4PeerGroupKeepAliveConfigured_Type()
)
fsMIBgp4PeerGroupKeepAliveConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupKeepAliveConfigured.setStatus("current")


class _FsMIBgp4PeerGroupConnectRetryInterval_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupConnectRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIBgp4PeerGroupConnectRetryInterval_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupConnectRetryInterval_Object = MibTableColumn
fsMIBgp4PeerGroupConnectRetryInterval = _FsMIBgp4PeerGroupConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 6),
    _FsMIBgp4PeerGroupConnectRetryInterval_Type()
)
fsMIBgp4PeerGroupConnectRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupConnectRetryInterval.setStatus("current")


class _FsMIBgp4PeerGroupMinASOriginInterval_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupMinASOriginInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIBgp4PeerGroupMinASOriginInterval_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupMinASOriginInterval_Object = MibTableColumn
fsMIBgp4PeerGroupMinASOriginInterval = _FsMIBgp4PeerGroupMinASOriginInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 7),
    _FsMIBgp4PeerGroupMinASOriginInterval_Type()
)
fsMIBgp4PeerGroupMinASOriginInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupMinASOriginInterval.setStatus("current")


class _FsMIBgp4PeerGroupMinRouteAdvInterval_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupMinRouteAdvInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIBgp4PeerGroupMinRouteAdvInterval_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupMinRouteAdvInterval_Object = MibTableColumn
fsMIBgp4PeerGroupMinRouteAdvInterval = _FsMIBgp4PeerGroupMinRouteAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 8),
    _FsMIBgp4PeerGroupMinRouteAdvInterval_Type()
)
fsMIBgp4PeerGroupMinRouteAdvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupMinRouteAdvInterval.setStatus("current")


class _FsMIBgp4PeerGroupAllowAutomaticStart_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupAllowAutomaticStart based on Integer32"""
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


_FsMIBgp4PeerGroupAllowAutomaticStart_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupAllowAutomaticStart_Object = MibTableColumn
fsMIBgp4PeerGroupAllowAutomaticStart = _FsMIBgp4PeerGroupAllowAutomaticStart_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 9),
    _FsMIBgp4PeerGroupAllowAutomaticStart_Type()
)
fsMIBgp4PeerGroupAllowAutomaticStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupAllowAutomaticStart.setStatus("current")


class _FsMIBgp4PeerGroupAllowAutomaticStop_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupAllowAutomaticStop based on Integer32"""
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


_FsMIBgp4PeerGroupAllowAutomaticStop_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupAllowAutomaticStop_Object = MibTableColumn
fsMIBgp4PeerGroupAllowAutomaticStop = _FsMIBgp4PeerGroupAllowAutomaticStop_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 10),
    _FsMIBgp4PeerGroupAllowAutomaticStop_Type()
)
fsMIBgp4PeerGroupAllowAutomaticStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupAllowAutomaticStop.setStatus("current")


class _FsMIBgp4PeerGroupIdleHoldTimeConfigured_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupIdleHoldTimeConfigured based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIBgp4PeerGroupIdleHoldTimeConfigured_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupIdleHoldTimeConfigured_Object = MibTableColumn
fsMIBgp4PeerGroupIdleHoldTimeConfigured = _FsMIBgp4PeerGroupIdleHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 11),
    _FsMIBgp4PeerGroupIdleHoldTimeConfigured_Type()
)
fsMIBgp4PeerGroupIdleHoldTimeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupIdleHoldTimeConfigured.setStatus("current")


class _FsMIBgp4PeerGroupDampPeerOscillations_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupDampPeerOscillations based on Integer32"""
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


_FsMIBgp4PeerGroupDampPeerOscillations_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupDampPeerOscillations_Object = MibTableColumn
fsMIBgp4PeerGroupDampPeerOscillations = _FsMIBgp4PeerGroupDampPeerOscillations_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 12),
    _FsMIBgp4PeerGroupDampPeerOscillations_Type()
)
fsMIBgp4PeerGroupDampPeerOscillations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupDampPeerOscillations.setStatus("current")


class _FsMIBgp4PeerGroupDelayOpen_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupDelayOpen based on Integer32"""
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


_FsMIBgp4PeerGroupDelayOpen_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupDelayOpen_Object = MibTableColumn
fsMIBgp4PeerGroupDelayOpen = _FsMIBgp4PeerGroupDelayOpen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 13),
    _FsMIBgp4PeerGroupDelayOpen_Type()
)
fsMIBgp4PeerGroupDelayOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupDelayOpen.setStatus("current")


class _FsMIBgp4PeerGroupDelayOpenTimeConfigured_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupDelayOpenTimeConfigured based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIBgp4PeerGroupDelayOpenTimeConfigured_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupDelayOpenTimeConfigured_Object = MibTableColumn
fsMIBgp4PeerGroupDelayOpenTimeConfigured = _FsMIBgp4PeerGroupDelayOpenTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 14),
    _FsMIBgp4PeerGroupDelayOpenTimeConfigured_Type()
)
fsMIBgp4PeerGroupDelayOpenTimeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupDelayOpenTimeConfigured.setStatus("current")


class _FsMIBgp4PeerGroupPrefixUpperLimit_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupPrefixUpperLimit based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsMIBgp4PeerGroupPrefixUpperLimit_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupPrefixUpperLimit_Object = MibTableColumn
fsMIBgp4PeerGroupPrefixUpperLimit = _FsMIBgp4PeerGroupPrefixUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 15),
    _FsMIBgp4PeerGroupPrefixUpperLimit_Type()
)
fsMIBgp4PeerGroupPrefixUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupPrefixUpperLimit.setStatus("current")


class _FsMIBgp4PeerGroupTcpConnectRetryCnt_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupTcpConnectRetryCnt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_FsMIBgp4PeerGroupTcpConnectRetryCnt_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupTcpConnectRetryCnt_Object = MibTableColumn
fsMIBgp4PeerGroupTcpConnectRetryCnt = _FsMIBgp4PeerGroupTcpConnectRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 16),
    _FsMIBgp4PeerGroupTcpConnectRetryCnt_Type()
)
fsMIBgp4PeerGroupTcpConnectRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupTcpConnectRetryCnt.setStatus("current")


class _FsMIBgp4PeerGroupEBGPMultiHop_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupEBGPMultiHop based on Integer32"""
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


_FsMIBgp4PeerGroupEBGPMultiHop_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupEBGPMultiHop_Object = MibTableColumn
fsMIBgp4PeerGroupEBGPMultiHop = _FsMIBgp4PeerGroupEBGPMultiHop_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 17),
    _FsMIBgp4PeerGroupEBGPMultiHop_Type()
)
fsMIBgp4PeerGroupEBGPMultiHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupEBGPMultiHop.setStatus("current")


class _FsMIBgp4PeerGroupEBGPHopLimit_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupEBGPHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsMIBgp4PeerGroupEBGPHopLimit_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupEBGPHopLimit_Object = MibTableColumn
fsMIBgp4PeerGroupEBGPHopLimit = _FsMIBgp4PeerGroupEBGPHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 18),
    _FsMIBgp4PeerGroupEBGPHopLimit_Type()
)
fsMIBgp4PeerGroupEBGPHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupEBGPHopLimit.setStatus("current")


class _FsMIBgp4PeerGroupNextHopSelf_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupNextHopSelf based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("self", 2))
    )


_FsMIBgp4PeerGroupNextHopSelf_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupNextHopSelf_Object = MibTableColumn
fsMIBgp4PeerGroupNextHopSelf = _FsMIBgp4PeerGroupNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 19),
    _FsMIBgp4PeerGroupNextHopSelf_Type()
)
fsMIBgp4PeerGroupNextHopSelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupNextHopSelf.setStatus("current")


class _FsMIBgp4PeerGroupRflClient_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupRflClient based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonClient", 1),
          ("client", 2))
    )


_FsMIBgp4PeerGroupRflClient_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupRflClient_Object = MibTableColumn
fsMIBgp4PeerGroupRflClient = _FsMIBgp4PeerGroupRflClient_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 20),
    _FsMIBgp4PeerGroupRflClient_Type()
)
fsMIBgp4PeerGroupRflClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupRflClient.setStatus("current")


class _FsMIBgp4PeerGroupTcpSendBufSize_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupTcpSendBufSize based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 65536),
    )


_FsMIBgp4PeerGroupTcpSendBufSize_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupTcpSendBufSize_Object = MibTableColumn
fsMIBgp4PeerGroupTcpSendBufSize = _FsMIBgp4PeerGroupTcpSendBufSize_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 21),
    _FsMIBgp4PeerGroupTcpSendBufSize_Type()
)
fsMIBgp4PeerGroupTcpSendBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupTcpSendBufSize.setStatus("current")


class _FsMIBgp4PeerGroupTcpRcvBufSize_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupTcpRcvBufSize based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 65536),
    )


_FsMIBgp4PeerGroupTcpRcvBufSize_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupTcpRcvBufSize_Object = MibTableColumn
fsMIBgp4PeerGroupTcpRcvBufSize = _FsMIBgp4PeerGroupTcpRcvBufSize_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 22),
    _FsMIBgp4PeerGroupTcpRcvBufSize_Type()
)
fsMIBgp4PeerGroupTcpRcvBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupTcpRcvBufSize.setStatus("current")


class _FsMIBgp4PeerGroupCommSendStatus_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupCommSendStatus based on Integer32"""
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
        *(("none", 1),
          ("send", 2),
          ("donotsend", 3))
    )


_FsMIBgp4PeerGroupCommSendStatus_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupCommSendStatus_Object = MibTableColumn
fsMIBgp4PeerGroupCommSendStatus = _FsMIBgp4PeerGroupCommSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 23),
    _FsMIBgp4PeerGroupCommSendStatus_Type()
)
fsMIBgp4PeerGroupCommSendStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupCommSendStatus.setStatus("current")


class _FsMIBgp4PeerGroupECommSendStatus_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupECommSendStatus based on Integer32"""
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
        *(("none", 1),
          ("send", 2),
          ("donotsend", 3))
    )


_FsMIBgp4PeerGroupECommSendStatus_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupECommSendStatus_Object = MibTableColumn
fsMIBgp4PeerGroupECommSendStatus = _FsMIBgp4PeerGroupECommSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 24),
    _FsMIBgp4PeerGroupECommSendStatus_Type()
)
fsMIBgp4PeerGroupECommSendStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupECommSendStatus.setStatus("current")


class _FsMIBgp4PeerGroupPassive_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupPassive based on Integer32"""
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


_FsMIBgp4PeerGroupPassive_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupPassive_Object = MibTableColumn
fsMIBgp4PeerGroupPassive = _FsMIBgp4PeerGroupPassive_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 25),
    _FsMIBgp4PeerGroupPassive_Type()
)
fsMIBgp4PeerGroupPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupPassive.setStatus("current")


class _FsMIBgp4PeerGroupDefaultOriginate_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupDefaultOriginate based on Integer32"""
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


_FsMIBgp4PeerGroupDefaultOriginate_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupDefaultOriginate_Object = MibTableColumn
fsMIBgp4PeerGroupDefaultOriginate = _FsMIBgp4PeerGroupDefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 26),
    _FsMIBgp4PeerGroupDefaultOriginate_Type()
)
fsMIBgp4PeerGroupDefaultOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupDefaultOriginate.setStatus("current")


class _FsMIBgp4PeerGroupActivateMPCapability_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupActivateMPCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4unicast", 1),
          ("ipv6unicast", 2))
    )


_FsMIBgp4PeerGroupActivateMPCapability_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupActivateMPCapability_Object = MibTableColumn
fsMIBgp4PeerGroupActivateMPCapability = _FsMIBgp4PeerGroupActivateMPCapability_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 27),
    _FsMIBgp4PeerGroupActivateMPCapability_Type()
)
fsMIBgp4PeerGroupActivateMPCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupActivateMPCapability.setStatus("current")


class _FsMIBgp4PeerGroupDeactivateMPCapability_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupDeactivateMPCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4unicast", 1),
          ("ipv6unicast", 2))
    )


_FsMIBgp4PeerGroupDeactivateMPCapability_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupDeactivateMPCapability_Object = MibTableColumn
fsMIBgp4PeerGroupDeactivateMPCapability = _FsMIBgp4PeerGroupDeactivateMPCapability_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 28),
    _FsMIBgp4PeerGroupDeactivateMPCapability_Type()
)
fsMIBgp4PeerGroupDeactivateMPCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupDeactivateMPCapability.setStatus("current")
_FsMIBgp4PeerGroupRouteMapNameIn_Type = DisplayString
_FsMIBgp4PeerGroupRouteMapNameIn_Object = MibTableColumn
fsMIBgp4PeerGroupRouteMapNameIn = _FsMIBgp4PeerGroupRouteMapNameIn_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 29),
    _FsMIBgp4PeerGroupRouteMapNameIn_Type()
)
fsMIBgp4PeerGroupRouteMapNameIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupRouteMapNameIn.setStatus("current")
_FsMIBgp4PeerGroupRouteMapNameOut_Type = DisplayString
_FsMIBgp4PeerGroupRouteMapNameOut_Object = MibTableColumn
fsMIBgp4PeerGroupRouteMapNameOut = _FsMIBgp4PeerGroupRouteMapNameOut_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 30),
    _FsMIBgp4PeerGroupRouteMapNameOut_Type()
)
fsMIBgp4PeerGroupRouteMapNameOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupRouteMapNameOut.setStatus("current")
_FsMIBgp4PeerGroupStatus_Type = RowStatus
_FsMIBgp4PeerGroupStatus_Object = MibTableColumn
fsMIBgp4PeerGroupStatus = _FsMIBgp4PeerGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 31),
    _FsMIBgp4PeerGroupStatus_Type()
)
fsMIBgp4PeerGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupStatus.setStatus("current")
_FsMIBgp4PeerGroupIpPrefixNameIn_Type = DisplayString
_FsMIBgp4PeerGroupIpPrefixNameIn_Object = MibTableColumn
fsMIBgp4PeerGroupIpPrefixNameIn = _FsMIBgp4PeerGroupIpPrefixNameIn_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 32),
    _FsMIBgp4PeerGroupIpPrefixNameIn_Type()
)
fsMIBgp4PeerGroupIpPrefixNameIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupIpPrefixNameIn.setStatus("current")
_FsMIBgp4PeerGroupIpPrefixNameOut_Type = DisplayString
_FsMIBgp4PeerGroupIpPrefixNameOut_Object = MibTableColumn
fsMIBgp4PeerGroupIpPrefixNameOut = _FsMIBgp4PeerGroupIpPrefixNameOut_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 33),
    _FsMIBgp4PeerGroupIpPrefixNameOut_Type()
)
fsMIBgp4PeerGroupIpPrefixNameOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupIpPrefixNameOut.setStatus("current")
_FsMIBgp4PeerGroupOrfType_Type = Unsigned32
_FsMIBgp4PeerGroupOrfType_Object = MibTableColumn
fsMIBgp4PeerGroupOrfType = _FsMIBgp4PeerGroupOrfType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 34),
    _FsMIBgp4PeerGroupOrfType_Type()
)
fsMIBgp4PeerGroupOrfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupOrfType.setStatus("current")


class _FsMIBgp4PeerGroupOrfCapMode_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupOrfCapMode based on Integer32"""
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
        *(("disable", 0),
          ("receive", 1),
          ("send", 2),
          ("both", 3))
    )


_FsMIBgp4PeerGroupOrfCapMode_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupOrfCapMode_Object = MibTableColumn
fsMIBgp4PeerGroupOrfCapMode = _FsMIBgp4PeerGroupOrfCapMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 35),
    _FsMIBgp4PeerGroupOrfCapMode_Type()
)
fsMIBgp4PeerGroupOrfCapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupOrfCapMode.setStatus("current")


class _FsMIBgp4PeerGroupOrfRequest_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupOrfRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_FsMIBgp4PeerGroupOrfRequest_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupOrfRequest_Object = MibTableColumn
fsMIBgp4PeerGroupOrfRequest = _FsMIBgp4PeerGroupOrfRequest_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 36),
    _FsMIBgp4PeerGroupOrfRequest_Type()
)
fsMIBgp4PeerGroupOrfRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupOrfRequest.setStatus("current")


class _FsMIBgp4PeerGroupBfdStatus_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupBfdStatus based on Integer32"""
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


_FsMIBgp4PeerGroupBfdStatus_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupBfdStatus_Object = MibTableColumn
fsMIBgp4PeerGroupBfdStatus = _FsMIBgp4PeerGroupBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 37),
    _FsMIBgp4PeerGroupBfdStatus_Type()
)
fsMIBgp4PeerGroupBfdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupBfdStatus.setStatus("current")


class _FsMIBgp4PeerGroupOverrideCapability_Type(Integer32):
    """Custom type fsMIBgp4PeerGroupOverrideCapability based on Integer32"""
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


_FsMIBgp4PeerGroupOverrideCapability_Type.__name__ = "Integer32"
_FsMIBgp4PeerGroupOverrideCapability_Object = MibTableColumn
fsMIBgp4PeerGroupOverrideCapability = _FsMIBgp4PeerGroupOverrideCapability_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 39, 1, 38),
    _FsMIBgp4PeerGroupOverrideCapability_Type()
)
fsMIBgp4PeerGroupOverrideCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupOverrideCapability.setStatus("current")
_FsMIBgp4PeerGroupListTable_Object = MibTable
fsMIBgp4PeerGroupListTable = _FsMIBgp4PeerGroupListTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 40)
)
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupListTable.setStatus("current")
_FsMIBgp4PeerGroupListEntry_Object = MibTableRow
fsMIBgp4PeerGroupListEntry = _FsMIBgp4PeerGroupListEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 40, 1)
)
fsMIBgp4PeerGroupListEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4PeerGroupName"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4PeerAddrType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4PeerAddress"),
)
if mibBuilder.loadTexts:
    fsMIBgp4PeerGroupListEntry.setStatus("current")
_FsMIBgp4PeerAddrType_Type = InetAddressType
_FsMIBgp4PeerAddrType_Object = MibTableColumn
fsMIBgp4PeerAddrType = _FsMIBgp4PeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 40, 1, 1),
    _FsMIBgp4PeerAddrType_Type()
)
fsMIBgp4PeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4PeerAddrType.setStatus("current")
_FsMIBgp4PeerAddress_Type = InetAddress
_FsMIBgp4PeerAddress_Object = MibTableColumn
fsMIBgp4PeerAddress = _FsMIBgp4PeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 40, 1, 2),
    _FsMIBgp4PeerAddress_Type()
)
fsMIBgp4PeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4PeerAddress.setStatus("current")


class _FsMIBgp4PeerAddStatus_Type(Integer32):
    """Custom type fsMIBgp4PeerAddStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_FsMIBgp4PeerAddStatus_Type.__name__ = "Integer32"
_FsMIBgp4PeerAddStatus_Object = MibTableColumn
fsMIBgp4PeerAddStatus = _FsMIBgp4PeerAddStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 40, 1, 3),
    _FsMIBgp4PeerAddStatus_Type()
)
fsMIBgp4PeerAddStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4PeerAddStatus.setStatus("current")


class _FsMIBgp4RestartReason_Type(Integer32):
    """Custom type fsMIBgp4RestartReason based on Integer32"""
    defaultValue = 1

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
          ("softwareRestart", 1),
          ("swReloadUpgrade", 2))
    )


_FsMIBgp4RestartReason_Type.__name__ = "Integer32"
_FsMIBgp4RestartReason_Object = MibScalar
fsMIBgp4RestartReason = _FsMIBgp4RestartReason_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 41),
    _FsMIBgp4RestartReason_Type()
)
fsMIBgp4RestartReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RestartReason.setStatus("current")
_FsMIBgp4TCPMKTAuth_ObjectIdentity = ObjectIdentity
fsMIBgp4TCPMKTAuth = _FsMIBgp4TCPMKTAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 42)
)
_FsMIBgp4TCPMKTAuthTable_Object = MibTable
fsMIBgp4TCPMKTAuthTable = _FsMIBgp4TCPMKTAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 42, 1)
)
if mibBuilder.loadTexts:
    fsMIBgp4TCPMKTAuthTable.setStatus("current")
_FsMIBgp4TCPMKTAuthEntry_Object = MibTableRow
fsMIBgp4TCPMKTAuthEntry = _FsMIBgp4TCPMKTAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 42, 1, 1)
)
fsMIBgp4TCPMKTAuthEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4TCPMKTAuthKeyId"),
)
if mibBuilder.loadTexts:
    fsMIBgp4TCPMKTAuthEntry.setStatus("current")


class _FsMIBgp4TCPMKTAuthKeyId_Type(Integer32):
    """Custom type fsMIBgp4TCPMKTAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIBgp4TCPMKTAuthKeyId_Type.__name__ = "Integer32"
_FsMIBgp4TCPMKTAuthKeyId_Object = MibTableColumn
fsMIBgp4TCPMKTAuthKeyId = _FsMIBgp4TCPMKTAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 42, 1, 1, 1),
    _FsMIBgp4TCPMKTAuthKeyId_Type()
)
fsMIBgp4TCPMKTAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4TCPMKTAuthKeyId.setStatus("current")


class _FsMIBgp4TCPMKTAuthRecvKeyId_Type(Integer32):
    """Custom type fsMIBgp4TCPMKTAuthRecvKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIBgp4TCPMKTAuthRecvKeyId_Type.__name__ = "Integer32"
_FsMIBgp4TCPMKTAuthRecvKeyId_Object = MibTableColumn
fsMIBgp4TCPMKTAuthRecvKeyId = _FsMIBgp4TCPMKTAuthRecvKeyId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 42, 1, 1, 2),
    _FsMIBgp4TCPMKTAuthRecvKeyId_Type()
)
fsMIBgp4TCPMKTAuthRecvKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4TCPMKTAuthRecvKeyId.setStatus("current")


class _FsMIBgp4TCPMKTAuthMasterKey_Type(OctetString):
    """Custom type fsMIBgp4TCPMKTAuthMasterKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_FsMIBgp4TCPMKTAuthMasterKey_Type.__name__ = "OctetString"
_FsMIBgp4TCPMKTAuthMasterKey_Object = MibTableColumn
fsMIBgp4TCPMKTAuthMasterKey = _FsMIBgp4TCPMKTAuthMasterKey_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 42, 1, 1, 3),
    _FsMIBgp4TCPMKTAuthMasterKey_Type()
)
fsMIBgp4TCPMKTAuthMasterKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4TCPMKTAuthMasterKey.setStatus("current")


class _FsMIBgp4TCPMKTAuthAlgo_Type(Integer32):
    """Custom type fsMIBgp4TCPMKTAuthAlgo based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hmacSha1", 1),
          ("aes128Cmac", 2))
    )


_FsMIBgp4TCPMKTAuthAlgo_Type.__name__ = "Integer32"
_FsMIBgp4TCPMKTAuthAlgo_Object = MibTableColumn
fsMIBgp4TCPMKTAuthAlgo = _FsMIBgp4TCPMKTAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 42, 1, 1, 4),
    _FsMIBgp4TCPMKTAuthAlgo_Type()
)
fsMIBgp4TCPMKTAuthAlgo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4TCPMKTAuthAlgo.setStatus("current")
_FsMIBgp4TCPMKTAuthTcpOptExc_Type = TruthValue
_FsMIBgp4TCPMKTAuthTcpOptExc_Object = MibTableColumn
fsMIBgp4TCPMKTAuthTcpOptExc = _FsMIBgp4TCPMKTAuthTcpOptExc_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 42, 1, 1, 5),
    _FsMIBgp4TCPMKTAuthTcpOptExc_Type()
)
fsMIBgp4TCPMKTAuthTcpOptExc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4TCPMKTAuthTcpOptExc.setStatus("current")
_FsMIBgp4TCPMKTAuthRowStatus_Type = RowStatus
_FsMIBgp4TCPMKTAuthRowStatus_Object = MibTableColumn
fsMIBgp4TCPMKTAuthRowStatus = _FsMIBgp4TCPMKTAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 42, 1, 1, 6),
    _FsMIBgp4TCPMKTAuthRowStatus_Type()
)
fsMIBgp4TCPMKTAuthRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4TCPMKTAuthRowStatus.setStatus("current")
_FsMIBgp4TCPAOAuthPeer_ObjectIdentity = ObjectIdentity
fsMIBgp4TCPAOAuthPeer = _FsMIBgp4TCPAOAuthPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 43)
)
_FsMIBgp4TCPAOAuthPeerTable_Object = MibTable
fsMIBgp4TCPAOAuthPeerTable = _FsMIBgp4TCPAOAuthPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 43, 1)
)
if mibBuilder.loadTexts:
    fsMIBgp4TCPAOAuthPeerTable.setStatus("current")
_FsMIBgp4TCPAOAuthPeerEntry_Object = MibTableRow
fsMIBgp4TCPAOAuthPeerEntry = _FsMIBgp4TCPAOAuthPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 43, 1, 1)
)
fsMIBgp4TCPAOAuthPeerEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4TCPAOAuthPeerType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4TCPAOAuthPeerAddr"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4TCPAOAuthKeyId"),
)
if mibBuilder.loadTexts:
    fsMIBgp4TCPAOAuthPeerEntry.setStatus("current")
_FsMIBgp4TCPAOAuthPeerType_Type = InetAddressType
_FsMIBgp4TCPAOAuthPeerType_Object = MibTableColumn
fsMIBgp4TCPAOAuthPeerType = _FsMIBgp4TCPAOAuthPeerType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 43, 1, 1, 1),
    _FsMIBgp4TCPAOAuthPeerType_Type()
)
fsMIBgp4TCPAOAuthPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4TCPAOAuthPeerType.setStatus("current")
_FsMIBgp4TCPAOAuthPeerAddr_Type = InetAddress
_FsMIBgp4TCPAOAuthPeerAddr_Object = MibTableColumn
fsMIBgp4TCPAOAuthPeerAddr = _FsMIBgp4TCPAOAuthPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 43, 1, 1, 2),
    _FsMIBgp4TCPAOAuthPeerAddr_Type()
)
fsMIBgp4TCPAOAuthPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4TCPAOAuthPeerAddr.setStatus("current")


class _FsMIBgp4TCPAOAuthKeyId_Type(Integer32):
    """Custom type fsMIBgp4TCPAOAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIBgp4TCPAOAuthKeyId_Type.__name__ = "Integer32"
_FsMIBgp4TCPAOAuthKeyId_Object = MibTableColumn
fsMIBgp4TCPAOAuthKeyId = _FsMIBgp4TCPAOAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 43, 1, 1, 3),
    _FsMIBgp4TCPAOAuthKeyId_Type()
)
fsMIBgp4TCPAOAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4TCPAOAuthKeyId.setStatus("current")


class _FsMIBgp4TCPAOAuthKeyStatus_Type(Integer32):
    """Custom type fsMIBgp4TCPAOAuthKeyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("clear", 2))
    )


_FsMIBgp4TCPAOAuthKeyStatus_Type.__name__ = "Integer32"
_FsMIBgp4TCPAOAuthKeyStatus_Object = MibTableColumn
fsMIBgp4TCPAOAuthKeyStatus = _FsMIBgp4TCPAOAuthKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 43, 1, 1, 4),
    _FsMIBgp4TCPAOAuthKeyStatus_Type()
)
fsMIBgp4TCPAOAuthKeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4TCPAOAuthKeyStatus.setStatus("current")
_FsMIBgp4TCPAOAuthKeyStartAccept_Type = DateAndTime
_FsMIBgp4TCPAOAuthKeyStartAccept_Object = MibTableColumn
fsMIBgp4TCPAOAuthKeyStartAccept = _FsMIBgp4TCPAOAuthKeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 43, 1, 1, 5),
    _FsMIBgp4TCPAOAuthKeyStartAccept_Type()
)
fsMIBgp4TCPAOAuthKeyStartAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4TCPAOAuthKeyStartAccept.setStatus("current")
_FsMIBgp4TCPAOAuthKeyStartGenerate_Type = DateAndTime
_FsMIBgp4TCPAOAuthKeyStartGenerate_Object = MibTableColumn
fsMIBgp4TCPAOAuthKeyStartGenerate = _FsMIBgp4TCPAOAuthKeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 43, 1, 1, 6),
    _FsMIBgp4TCPAOAuthKeyStartGenerate_Type()
)
fsMIBgp4TCPAOAuthKeyStartGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4TCPAOAuthKeyStartGenerate.setStatus("current")
_FsMIBgp4TCPAOAuthKeyStopGenerate_Type = DateAndTime
_FsMIBgp4TCPAOAuthKeyStopGenerate_Object = MibTableColumn
fsMIBgp4TCPAOAuthKeyStopGenerate = _FsMIBgp4TCPAOAuthKeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 43, 1, 1, 7),
    _FsMIBgp4TCPAOAuthKeyStopGenerate_Type()
)
fsMIBgp4TCPAOAuthKeyStopGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4TCPAOAuthKeyStopGenerate.setStatus("current")
_FsMIBgp4TCPAOAuthKeyStopAccept_Type = DateAndTime
_FsMIBgp4TCPAOAuthKeyStopAccept_Object = MibTableColumn
fsMIBgp4TCPAOAuthKeyStopAccept = _FsMIBgp4TCPAOAuthKeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 43, 1, 1, 8),
    _FsMIBgp4TCPAOAuthKeyStopAccept_Type()
)
fsMIBgp4TCPAOAuthKeyStopAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4TCPAOAuthKeyStopAccept.setStatus("current")
_FsMIBgp4ORFListTable_Object = MibTable
fsMIBgp4ORFListTable = _FsMIBgp4ORFListTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 44)
)
if mibBuilder.loadTexts:
    fsMIBgp4ORFListTable.setStatus("current")
_FsMIBgp4ORFListEntry_Object = MibTableRow
fsMIBgp4ORFListEntry = _FsMIBgp4ORFListEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 44, 1)
)
fsMIBgp4ORFListEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ORFPeerAddrType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ORFPeerAddr"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ORFAfi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ORFSafi"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ORFType"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ORFSequence"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ORFAddrPrefix"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ORFAddrPrefixLen"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ORFMinLength"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ORFMaxLength"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ORFAction"),
)
if mibBuilder.loadTexts:
    fsMIBgp4ORFListEntry.setStatus("current")
_FsMIBgp4ORFPeerAddrType_Type = InetAddressType
_FsMIBgp4ORFPeerAddrType_Object = MibTableColumn
fsMIBgp4ORFPeerAddrType = _FsMIBgp4ORFPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 44, 1, 1),
    _FsMIBgp4ORFPeerAddrType_Type()
)
fsMIBgp4ORFPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4ORFPeerAddrType.setStatus("current")
_FsMIBgp4ORFPeerAddr_Type = InetAddress
_FsMIBgp4ORFPeerAddr_Object = MibTableColumn
fsMIBgp4ORFPeerAddr = _FsMIBgp4ORFPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 44, 1, 2),
    _FsMIBgp4ORFPeerAddr_Type()
)
fsMIBgp4ORFPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4ORFPeerAddr.setStatus("current")
_FsMIBgp4ORFAfi_Type = InetAddressType
_FsMIBgp4ORFAfi_Object = MibTableColumn
fsMIBgp4ORFAfi = _FsMIBgp4ORFAfi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 44, 1, 3),
    _FsMIBgp4ORFAfi_Type()
)
fsMIBgp4ORFAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4ORFAfi.setStatus("current")
_FsMIBgp4ORFSafi_Type = BgpSafi
_FsMIBgp4ORFSafi_Object = MibTableColumn
fsMIBgp4ORFSafi = _FsMIBgp4ORFSafi_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 44, 1, 4),
    _FsMIBgp4ORFSafi_Type()
)
fsMIBgp4ORFSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4ORFSafi.setStatus("current")
_FsMIBgp4ORFType_Type = Unsigned32
_FsMIBgp4ORFType_Object = MibTableColumn
fsMIBgp4ORFType = _FsMIBgp4ORFType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 44, 1, 5),
    _FsMIBgp4ORFType_Type()
)
fsMIBgp4ORFType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4ORFType.setStatus("current")
_FsMIBgp4ORFSequence_Type = Unsigned32
_FsMIBgp4ORFSequence_Object = MibTableColumn
fsMIBgp4ORFSequence = _FsMIBgp4ORFSequence_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 44, 1, 6),
    _FsMIBgp4ORFSequence_Type()
)
fsMIBgp4ORFSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4ORFSequence.setStatus("current")
_FsMIBgp4ORFAddrPrefix_Type = InetAddress
_FsMIBgp4ORFAddrPrefix_Object = MibTableColumn
fsMIBgp4ORFAddrPrefix = _FsMIBgp4ORFAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 44, 1, 7),
    _FsMIBgp4ORFAddrPrefix_Type()
)
fsMIBgp4ORFAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4ORFAddrPrefix.setStatus("current")


class _FsMIBgp4ORFAddrPrefixLen_Type(Unsigned32):
    """Custom type fsMIBgp4ORFAddrPrefixLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsMIBgp4ORFAddrPrefixLen_Type.__name__ = "Unsigned32"
_FsMIBgp4ORFAddrPrefixLen_Object = MibTableColumn
fsMIBgp4ORFAddrPrefixLen = _FsMIBgp4ORFAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 44, 1, 8),
    _FsMIBgp4ORFAddrPrefixLen_Type()
)
fsMIBgp4ORFAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4ORFAddrPrefixLen.setStatus("current")


class _FsMIBgp4ORFMinLength_Type(Unsigned32):
    """Custom type fsMIBgp4ORFMinLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsMIBgp4ORFMinLength_Type.__name__ = "Unsigned32"
_FsMIBgp4ORFMinLength_Object = MibTableColumn
fsMIBgp4ORFMinLength = _FsMIBgp4ORFMinLength_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 44, 1, 9),
    _FsMIBgp4ORFMinLength_Type()
)
fsMIBgp4ORFMinLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4ORFMinLength.setStatus("current")


class _FsMIBgp4ORFMaxLength_Type(Unsigned32):
    """Custom type fsMIBgp4ORFMaxLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsMIBgp4ORFMaxLength_Type.__name__ = "Unsigned32"
_FsMIBgp4ORFMaxLength_Object = MibTableColumn
fsMIBgp4ORFMaxLength = _FsMIBgp4ORFMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 44, 1, 10),
    _FsMIBgp4ORFMaxLength_Type()
)
fsMIBgp4ORFMaxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4ORFMaxLength.setStatus("current")


class _FsMIBgp4ORFAction_Type(Integer32):
    """Custom type fsMIBgp4ORFAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("permit", 0),
          ("deny", 1))
    )


_FsMIBgp4ORFAction_Type.__name__ = "Integer32"
_FsMIBgp4ORFAction_Object = MibTableColumn
fsMIBgp4ORFAction = _FsMIBgp4ORFAction_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 44, 1, 11),
    _FsMIBgp4ORFAction_Type()
)
fsMIBgp4ORFAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4ORFAction.setStatus("current")
_FsMIBgp4RRDNetworkTable_Object = MibTable
fsMIBgp4RRDNetworkTable = _FsMIBgp4RRDNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 45)
)
if mibBuilder.loadTexts:
    fsMIBgp4RRDNetworkTable.setStatus("current")
_FsMIBgp4RRDNetworkEntry_Object = MibTableRow
fsMIBgp4RRDNetworkEntry = _FsMIBgp4RRDNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 45, 1)
)
fsMIBgp4RRDNetworkEntry.setIndexNames(
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4ContextId"),
    (0, "ARICENT-MI-BGP-MIB", "fsMIBgp4RRDNetworkAddr"),
)
if mibBuilder.loadTexts:
    fsMIBgp4RRDNetworkEntry.setStatus("current")
_FsMIBgp4RRDNetworkAddr_Type = InetAddress
_FsMIBgp4RRDNetworkAddr_Object = MibTableColumn
fsMIBgp4RRDNetworkAddr = _FsMIBgp4RRDNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 45, 1, 1),
    _FsMIBgp4RRDNetworkAddr_Type()
)
fsMIBgp4RRDNetworkAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIBgp4RRDNetworkAddr.setStatus("current")
_FsMIBgp4RRDNetworkAddrType_Type = InetAddressType
_FsMIBgp4RRDNetworkAddrType_Object = MibTableColumn
fsMIBgp4RRDNetworkAddrType = _FsMIBgp4RRDNetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 45, 1, 2),
    _FsMIBgp4RRDNetworkAddrType_Type()
)
fsMIBgp4RRDNetworkAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RRDNetworkAddrType.setStatus("current")


class _FsMIBgp4RRDNetworkPrefixLen_Type(Integer32):
    """Custom type fsMIBgp4RRDNetworkPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsMIBgp4RRDNetworkPrefixLen_Type.__name__ = "Integer32"
_FsMIBgp4RRDNetworkPrefixLen_Object = MibTableColumn
fsMIBgp4RRDNetworkPrefixLen = _FsMIBgp4RRDNetworkPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 45, 1, 3),
    _FsMIBgp4RRDNetworkPrefixLen_Type()
)
fsMIBgp4RRDNetworkPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RRDNetworkPrefixLen.setStatus("current")
_FsMIBgp4RRDNetworkRowStatus_Type = RowStatus
_FsMIBgp4RRDNetworkRowStatus_Object = MibTableColumn
fsMIBgp4RRDNetworkRowStatus = _FsMIBgp4RRDNetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 45, 1, 4),
    _FsMIBgp4RRDNetworkRowStatus_Type()
)
fsMIBgp4RRDNetworkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4RRDNetworkRowStatus.setStatus("current")


class _FsMIBgp4MacMobDuplicationTimeInterval_Type(Integer32):
    """Custom type fsMIBgp4MacMobDuplicationTimeInterval based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 36000),
    )


_FsMIBgp4MacMobDuplicationTimeInterval_Type.__name__ = "Integer32"
_FsMIBgp4MacMobDuplicationTimeInterval_Object = MibScalar
fsMIBgp4MacMobDuplicationTimeInterval = _FsMIBgp4MacMobDuplicationTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 46),
    _FsMIBgp4MacMobDuplicationTimeInterval_Type()
)
fsMIBgp4MacMobDuplicationTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4MacMobDuplicationTimeInterval.setStatus("current")


class _FsMIBgp4MaxMacMoves_Type(Integer32):
    """Custom type fsMIBgp4MaxMacMoves based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FsMIBgp4MaxMacMoves_Type.__name__ = "Integer32"
_FsMIBgp4MaxMacMoves_Object = MibScalar
fsMIBgp4MaxMacMoves = _FsMIBgp4MaxMacMoves_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 47),
    _FsMIBgp4MaxMacMoves_Type()
)
fsMIBgp4MaxMacMoves.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIBgp4MaxMacMoves.setStatus("current")

# Managed Objects groups


# Notification objects

fsMIBgp4RestartStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 37, 0, 1)
)
fsMIBgp4RestartStatusChange.setObjects(
      *(("ARICENT-MI-BGP-MIB", "fsMIBgp4Identifier"),
        ("ARICENT-MI-BGP-MIB", "fsMIBgp4RestartStatus"),
        ("ARICENT-MI-BGP-MIB", "fsMIBgp4GRRestartTimeInterval"),
        ("ARICENT-MI-BGP-MIB", "fsMIBgp4RestartExitReason"))
)
if mibBuilder.loadTexts:
    fsMIBgp4RestartStatusChange.setStatus(
        "current"
    )

fsMIBgp4RouteAddRTMFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 77, 37, 0, 3)
)
fsMIBgp4RouteAddRTMFailure.setObjects(
      *(("ARICENT-MI-BGP-MIB", "fsMIBgp4TrapContextId"),
        ("ARICENT-MI-BGP-MIB", "fsMIBgp4Identifier"),
        ("ARICENT-MI-BGP-MIB", "fsMIBgp4TrapRouteAddressType"),
        ("ARICENT-MI-BGP-MIB", "fsMIBgp4TrapRoutePrefix"),
        ("ARICENT-MI-BGP-MIB", "fsMIBgp4TrapPeerAddrType"),
        ("ARICENT-MI-BGP-MIB", "fsMIBgp4TrapPeerAddr"),
        ("ARICENT-MI-BGP-MIB", "fsMIBgp4mpebgp4PathAttrNextHop"))
)
if mibBuilder.loadTexts:
    fsMIBgp4RouteAddRTMFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-MI-BGP-MIB",
    **{"fsMIBgp": fsMIBgp,
       "fsMIBgp4GlobalTraceDebug": fsMIBgp4GlobalTraceDebug,
       "fsMIBgp4LocalAs": fsMIBgp4LocalAs,
       "fsMIBgp4MaxPeerEntry": fsMIBgp4MaxPeerEntry,
       "fsMIBgp4MaxNoofRoutes": fsMIBgp4MaxNoofRoutes,
       "fsMIBgp4GRAdminStatus": fsMIBgp4GRAdminStatus,
       "fsMIBgp4GRRestartTimeInterval": fsMIBgp4GRRestartTimeInterval,
       "fsMIBgp4RestartExitReason": fsMIBgp4RestartExitReason,
       "fsMIBgp4GRSelectionDeferralTimeInterval": fsMIBgp4GRSelectionDeferralTimeInterval,
       "fsMIBgp4GRStaleTimeInterval": fsMIBgp4GRStaleTimeInterval,
       "fsMIBgp4GRMode": fsMIBgp4GRMode,
       "fsMIBgp4RestartSupport": fsMIBgp4RestartSupport,
       "fsMIBgp4RestartStatus": fsMIBgp4RestartStatus,
       "fsMIBgp4ForwardingPreservation": fsMIBgp4ForwardingPreservation,
       "fsMIBgpContextTable": fsMIBgpContextTable,
       "fsMIBgpContextEntry": fsMIBgpContextEntry,
       "fsMIBgp4ContextId": fsMIBgp4ContextId,
       "fsMIBgp4GlobalAdminStatus": fsMIBgp4GlobalAdminStatus,
       "fsMIBgp4Identifier": fsMIBgp4Identifier,
       "fsMIBgp4Synchronization": fsMIBgp4Synchronization,
       "fsMIBgp4DefaultLocalPref": fsMIBgp4DefaultLocalPref,
       "fsMIBgp4AdvtNonBgpRt": fsMIBgp4AdvtNonBgpRt,
       "fsMIBgp4TraceEnable": fsMIBgp4TraceEnable,
       "fsMIBgp4DebugEnable": fsMIBgp4DebugEnable,
       "fsMIBgp4OverlappingRoute": fsMIBgp4OverlappingRoute,
       "fsMIBgp4AlwaysCompareMED": fsMIBgp4AlwaysCompareMED,
       "fsMIBgp4DefaultOriginate": fsMIBgp4DefaultOriginate,
       "fsMIBgp4DefaultIpv4UniCast": fsMIBgp4DefaultIpv4UniCast,
       "fsMIBgp4IsTrapEnabled": fsMIBgp4IsTrapEnabled,
       "fsMIBgp4NextHopProcessingInterval": fsMIBgp4NextHopProcessingInterval,
       "fsMIBgp4IBGPRedistributionStatus": fsMIBgp4IBGPRedistributionStatus,
       "fsMIBgp4RRDAdminStatus": fsMIBgp4RRDAdminStatus,
       "fsMIBgp4RRDProtoMaskForEnable": fsMIBgp4RRDProtoMaskForEnable,
       "fsMIBgp4RRDSrcProtoMaskForDisable": fsMIBgp4RRDSrcProtoMaskForDisable,
       "fsMIBgp4RRDDefaultMetric": fsMIBgp4RRDDefaultMetric,
       "fsMIBgp4RRDRouteMapName": fsMIBgp4RRDRouteMapName,
       "fsMIBgp4RRDMatchTypeEnable": fsMIBgp4RRDMatchTypeEnable,
       "fsMIBgp4RRDMatchTypeDisable": fsMIBgp4RRDMatchTypeDisable,
       "fsMIBgp4AscConfedId": fsMIBgp4AscConfedId,
       "fsMIBgp4AscConfedBestPathCompareMED": fsMIBgp4AscConfedBestPathCompareMED,
       "fsMIBgp4RflbgpClusterId": fsMIBgp4RflbgpClusterId,
       "fsMIBgp4RflRflSupport": fsMIBgp4RflRflSupport,
       "fsMIBgp4RfdCutOff": fsMIBgp4RfdCutOff,
       "fsMIBgp4RfdReuse": fsMIBgp4RfdReuse,
       "fsMIBgp4RfdCeiling": fsMIBgp4RfdCeiling,
       "fsMIBgp4RfdMaxHoldDownTime": fsMIBgp4RfdMaxHoldDownTime,
       "fsMIBgp4RfdDecayHalfLifeTime": fsMIBgp4RfdDecayHalfLifeTime,
       "fsMIBgp4RfdDecayTimerGranularity": fsMIBgp4RfdDecayTimerGranularity,
       "fsMIBgp4RfdReuseTimerGranularity": fsMIBgp4RfdReuseTimerGranularity,
       "fsMIBgp4RfdReuseIndxArraySize": fsMIBgp4RfdReuseIndxArraySize,
       "fsMIBgp4RfdAdminStatus": fsMIBgp4RfdAdminStatus,
       "fsMIBgp4CommMaxInFTblEntries": fsMIBgp4CommMaxInFTblEntries,
       "fsMIBgp4CommMaxOutFTblEntries": fsMIBgp4CommMaxOutFTblEntries,
       "fsMIBgp4ExtCommMaxInFTblEntries": fsMIBgp4ExtCommMaxInFTblEntries,
       "fsMIBgp4ExtCommMaxOutFTblEntries": fsMIBgp4ExtCommMaxOutFTblEntries,
       "fsMIBgp4CapabilitySupportAvailable": fsMIBgp4CapabilitySupportAvailable,
       "fsMIBgp4MaxCapsPerPeer": fsMIBgp4MaxCapsPerPeer,
       "fsMIBgp4MaxInstancesPerCap": fsMIBgp4MaxInstancesPerCap,
       "fsMIBgp4MaxCapDataSize": fsMIBgp4MaxCapDataSize,
       "fsMIBgp4PreferenceValue": fsMIBgp4PreferenceValue,
       "fsMIBgp4ContextStatus": fsMIBgp4ContextStatus,
       "fsMIBgp4IBGPMaxPaths": fsMIBgp4IBGPMaxPaths,
       "fsMIBgp4EBGPMaxPaths": fsMIBgp4EBGPMaxPaths,
       "fsMIBgp4EIBGPMaxPaths": fsMIBgp4EIBGPMaxPaths,
       "fsMIBgp4OperIBGPMaxPaths": fsMIBgp4OperIBGPMaxPaths,
       "fsMIBgp4OperEBGPMaxPaths": fsMIBgp4OperEBGPMaxPaths,
       "fsMIBgp4OperEIBGPMaxPaths": fsMIBgp4OperEIBGPMaxPaths,
       "fsMIBgp4FourByteASNSupportStatus": fsMIBgp4FourByteASNSupportStatus,
       "fsMIBgp4FourByteASNotationType": fsMIBgp4FourByteASNotationType,
       "fsMIBgp4LocalAsNo": fsMIBgp4LocalAsNo,
       "fsMIBgp4RIBRoutes": fsMIBgp4RIBRoutes,
       "fsMIBgp4Ipv4AddrFamily": fsMIBgp4Ipv4AddrFamily,
       "fsMIBgp4Ipv6AddrFamily": fsMIBgp4Ipv6AddrFamily,
       "fsMIBgp4VpnLabelAllocPolicy": fsMIBgp4VpnLabelAllocPolicy,
       "fsMIBgp4VPNV4AddrFamily": fsMIBgp4VPNV4AddrFamily,
       "fsMIBgp4L2vpnAddrFamily": fsMIBgp4L2vpnAddrFamily,
       "fsMIBgp4EvpnAddrFamily": fsMIBgp4EvpnAddrFamily,
       "fsMIBgp4RRDMetricTable": fsMIBgp4RRDMetricTable,
       "fsMIBgp4RRDMetricEntry": fsMIBgp4RRDMetricEntry,
       "fsMIBgp4RRDMetricProtocolId": fsMIBgp4RRDMetricProtocolId,
       "fsMIBgp4RRDMetricValue": fsMIBgp4RRDMetricValue,
       "fsMIBgpComm": fsMIBgpComm,
       "fsMIBgp4CommInFilterTable": fsMIBgp4CommInFilterTable,
       "fsMIBgp4CommInFilterEntry": fsMIBgp4CommInFilterEntry,
       "fsMIBgp4InFilterCommVal": fsMIBgp4InFilterCommVal,
       "fsMIBgp4CommIncomingFilterStatus": fsMIBgp4CommIncomingFilterStatus,
       "fsMIBgp4InFilterRowStatus": fsMIBgp4InFilterRowStatus,
       "fsMIBgp4CommOutFilterTable": fsMIBgp4CommOutFilterTable,
       "fsMIBgp4CommOutFilterEntry": fsMIBgp4CommOutFilterEntry,
       "fsMIBgp4OutFilterCommVal": fsMIBgp4OutFilterCommVal,
       "fsMIBgp4CommOutgoingFilterStatus": fsMIBgp4CommOutgoingFilterStatus,
       "fsMIBgp4OutFilterRowStatus": fsMIBgp4OutFilterRowStatus,
       "fsMIBgpExtComm": fsMIBgpExtComm,
       "fsMIBgp4ExtCommInFilterTable": fsMIBgp4ExtCommInFilterTable,
       "fsMIBgp4ExtCommInFilterEntry": fsMIBgp4ExtCommInFilterEntry,
       "fsMIBgp4ExtCommInFilterCommVal": fsMIBgp4ExtCommInFilterCommVal,
       "fsMIBgp4ExtCommIncomingFilterStatus": fsMIBgp4ExtCommIncomingFilterStatus,
       "fsMIBgp4ExtCommInFilterRowStatus": fsMIBgp4ExtCommInFilterRowStatus,
       "fsMIBgp4ExtCommOutFilterTable": fsMIBgp4ExtCommOutFilterTable,
       "fsMIBgp4ExtCommOutFilterEntry": fsMIBgp4ExtCommOutFilterEntry,
       "fsMIBgp4ExtCommOutFilterCommVal": fsMIBgp4ExtCommOutFilterCommVal,
       "fsMIBgp4ExtCommOutgoingFilterStatus": fsMIBgp4ExtCommOutgoingFilterStatus,
       "fsMIBgp4ExtCommOutFilterRowStatus": fsMIBgp4ExtCommOutFilterRowStatus,
       "fsMIBgp4TCPMD5Auth": fsMIBgp4TCPMD5Auth,
       "fsMIBgp4TCPMD5AuthTable": fsMIBgp4TCPMD5AuthTable,
       "fsMIBgp4TCPMD5AuthEntry": fsMIBgp4TCPMD5AuthEntry,
       "fsMIBgp4TCPMD5AuthPeerType": fsMIBgp4TCPMD5AuthPeerType,
       "fsMIBgp4TCPMD5AuthPeerAddr": fsMIBgp4TCPMD5AuthPeerAddr,
       "fsMIBgp4TCPMD5AuthPassword": fsMIBgp4TCPMD5AuthPassword,
       "fsMIBgp4TCPMD5AuthPwdSet": fsMIBgp4TCPMD5AuthPwdSet,
       "fsMIBgpAsc": fsMIBgpAsc,
       "fsMIBgpAscConfedPeerTable": fsMIBgpAscConfedPeerTable,
       "fsMIBgpAscConfedPeerEntry": fsMIBgpAscConfedPeerEntry,
       "fsMIBgpAscConfedPeerASNo": fsMIBgpAscConfedPeerASNo,
       "fsMIBgpAscConfedPeerStatus": fsMIBgpAscConfedPeerStatus,
       "fsMIBgp4MpeBgpPeerTable": fsMIBgp4MpeBgpPeerTable,
       "fsMIBgp4MpeBgpPeerEntry": fsMIBgp4MpeBgpPeerEntry,
       "fsMIBgp4mpebgpPeerIdentifier": fsMIBgp4mpebgpPeerIdentifier,
       "fsMIBgp4mpebgpPeerRemoteAddrType": fsMIBgp4mpebgpPeerRemoteAddrType,
       "fsMIBgp4mpebgpPeerLocalAs": fsMIBgp4mpebgpPeerLocalAs,
       "fsMIBgp4mpebgpPeerState": fsMIBgp4mpebgpPeerState,
       "fsMIBgp4mpebgpPeerAdminStatus": fsMIBgp4mpebgpPeerAdminStatus,
       "fsMIBgp4mpebgpPeerNegotiatedVersion": fsMIBgp4mpebgpPeerNegotiatedVersion,
       "fsMIBgp4mpebgpPeerLocalAddr": fsMIBgp4mpebgpPeerLocalAddr,
       "fsMIBgp4mpebgpPeerLocalPort": fsMIBgp4mpebgpPeerLocalPort,
       "fsMIBgp4mpebgpPeerRemoteAddr": fsMIBgp4mpebgpPeerRemoteAddr,
       "fsMIBgp4mpebgpPeerRemotePort": fsMIBgp4mpebgpPeerRemotePort,
       "fsMIBgp4mpebgpPeerRemoteAs": fsMIBgp4mpebgpPeerRemoteAs,
       "fsMIBgp4mpebgpPeerInUpdates": fsMIBgp4mpebgpPeerInUpdates,
       "fsMIBgp4mpebgpPeerOutUpdates": fsMIBgp4mpebgpPeerOutUpdates,
       "fsMIBgp4mpebgpPeerInTotalMessages": fsMIBgp4mpebgpPeerInTotalMessages,
       "fsMIBgp4mpebgpPeerOutTotalMessages": fsMIBgp4mpebgpPeerOutTotalMessages,
       "fsMIBgp4mpebgpPeerLastError": fsMIBgp4mpebgpPeerLastError,
       "fsMIBgp4mpebgpPeerFsmEstablishedTransitions": fsMIBgp4mpebgpPeerFsmEstablishedTransitions,
       "fsMIBgp4mpebgpPeerFsmEstablishedTime": fsMIBgp4mpebgpPeerFsmEstablishedTime,
       "fsMIBgp4mpebgpPeerConnectRetryInterval": fsMIBgp4mpebgpPeerConnectRetryInterval,
       "fsMIBgp4mpebgpPeerHoldTime": fsMIBgp4mpebgpPeerHoldTime,
       "fsMIBgp4mpebgpPeerKeepAlive": fsMIBgp4mpebgpPeerKeepAlive,
       "fsMIBgp4mpebgpPeerHoldTimeConfigured": fsMIBgp4mpebgpPeerHoldTimeConfigured,
       "fsMIBgp4mpebgpPeerKeepAliveConfigured": fsMIBgp4mpebgpPeerKeepAliveConfigured,
       "fsMIBgp4mpebgpPeerMinASOriginationInterval": fsMIBgp4mpebgpPeerMinASOriginationInterval,
       "fsMIBgp4mpebgpPeerMinRouteAdvertisementInterval": fsMIBgp4mpebgpPeerMinRouteAdvertisementInterval,
       "fsMIBgp4mpebgpPeerInUpdateElapsedTime": fsMIBgp4mpebgpPeerInUpdateElapsedTime,
       "fsMIBgp4mpebgpPeerEndOfRIBMarkerSentStatus": fsMIBgp4mpebgpPeerEndOfRIBMarkerSentStatus,
       "fsMIBgp4mpebgpPeerEndOfRIBMarkerReceivedStatus": fsMIBgp4mpebgpPeerEndOfRIBMarkerReceivedStatus,
       "fsMIBgp4mpebgpPeerRestartMode": fsMIBgp4mpebgpPeerRestartMode,
       "fsMIBgp4mpePeerRestartTimeInterval": fsMIBgp4mpePeerRestartTimeInterval,
       "fsMIBgp4mpePeerAllowAutomaticStart": fsMIBgp4mpePeerAllowAutomaticStart,
       "fsMIBgp4mpePeerAllowAutomaticStop": fsMIBgp4mpePeerAllowAutomaticStop,
       "fsMIBgp4mpebgpPeerIdleHoldTimeConfigured": fsMIBgp4mpebgpPeerIdleHoldTimeConfigured,
       "fsMIBgp4mpeDampPeerOscillations": fsMIBgp4mpeDampPeerOscillations,
       "fsMIBgp4mpePeerDelayOpen": fsMIBgp4mpePeerDelayOpen,
       "fsMIBgp4mpebgpPeerDelayOpenTimeConfigured": fsMIBgp4mpebgpPeerDelayOpenTimeConfigured,
       "fsMIBgp4mpePeerPrefixUpperLimit": fsMIBgp4mpePeerPrefixUpperLimit,
       "fsMIBgp4mpePeerTcpConnectRetryCnt": fsMIBgp4mpePeerTcpConnectRetryCnt,
       "fsMIBgp4mpePeerTcpCurrentConnectRetryCnt": fsMIBgp4mpePeerTcpCurrentConnectRetryCnt,
       "fsMIBgp4mpeIsPeerDamped": fsMIBgp4mpeIsPeerDamped,
       "fsMIBgp4mpePeerSessionAuthStatus": fsMIBgp4mpePeerSessionAuthStatus,
       "fsMIBgp4mpePeerTCPAOKeyIdInUse": fsMIBgp4mpePeerTCPAOKeyIdInUse,
       "fsMIBgp4mpePeerTCPAOAuthNoMKTDiscard": fsMIBgp4mpePeerTCPAOAuthNoMKTDiscard,
       "fsMIBgp4mpePeerTCPAOAuthICMPAccept": fsMIBgp4mpePeerTCPAOAuthICMPAccept,
       "fsMIBgp4mpePeerIpPrefixNameIn": fsMIBgp4mpePeerIpPrefixNameIn,
       "fsMIBgp4mpePeerIpPrefixNameOut": fsMIBgp4mpePeerIpPrefixNameOut,
       "fsMIBgp4mpePeerBfdStatus": fsMIBgp4mpePeerBfdStatus,
       "fsMIBgp4mpePeerHoldAdvtRoutes": fsMIBgp4mpePeerHoldAdvtRoutes,
       "fsMIBgp4MpeBgp4PathAttrTable": fsMIBgp4MpeBgp4PathAttrTable,
       "fsMIBgp4MpeBgp4PathAttrEntry": fsMIBgp4MpeBgp4PathAttrEntry,
       "fsMIBgp4mpebgp4PathAttrRouteAfi": fsMIBgp4mpebgp4PathAttrRouteAfi,
       "fsMIBgp4mpebgp4PathAttrRouteSafi": fsMIBgp4mpebgp4PathAttrRouteSafi,
       "fsMIBgp4mpebgp4PathAttrPeerType": fsMIBgp4mpebgp4PathAttrPeerType,
       "fsMIBgp4mpebgp4PathAttrPeer": fsMIBgp4mpebgp4PathAttrPeer,
       "fsMIBgp4mpebgp4PathAttrIpAddrPrefixLen": fsMIBgp4mpebgp4PathAttrIpAddrPrefixLen,
       "fsMIBgp4mpebgp4PathAttrIpAddrPrefix": fsMIBgp4mpebgp4PathAttrIpAddrPrefix,
       "fsMIBgp4mpebgp4PathAttrOrigin": fsMIBgp4mpebgp4PathAttrOrigin,
       "fsMIBgp4mpebgp4PathAttrASPathSegment": fsMIBgp4mpebgp4PathAttrASPathSegment,
       "fsMIBgp4mpebgp4PathAttrNextHop": fsMIBgp4mpebgp4PathAttrNextHop,
       "fsMIBgp4mpebgp4PathAttrMultiExitDisc": fsMIBgp4mpebgp4PathAttrMultiExitDisc,
       "fsMIBgp4mpebgp4PathAttrLocalPref": fsMIBgp4mpebgp4PathAttrLocalPref,
       "fsMIBgp4mpebgp4PathAttrAtomicAggregate": fsMIBgp4mpebgp4PathAttrAtomicAggregate,
       "fsMIBgp4mpebgp4PathAttrAggregatorAS": fsMIBgp4mpebgp4PathAttrAggregatorAS,
       "fsMIBgp4mpebgp4PathAttrAggregatorAddr": fsMIBgp4mpebgp4PathAttrAggregatorAddr,
       "fsMIBgp4mpebgp4PathAttrCalcLocalPref": fsMIBgp4mpebgp4PathAttrCalcLocalPref,
       "fsMIBgp4mpebgp4PathAttrBest": fsMIBgp4mpebgp4PathAttrBest,
       "fsMIBgp4mpebgp4PathAttrCommunity": fsMIBgp4mpebgp4PathAttrCommunity,
       "fsMIBgp4mpebgp4PathAttrOriginatorId": fsMIBgp4mpebgp4PathAttrOriginatorId,
       "fsMIBgp4mpebgp4PathAttrClusterList": fsMIBgp4mpebgp4PathAttrClusterList,
       "fsMIBgp4mpebgp4PathAttrExtCommunity": fsMIBgp4mpebgp4PathAttrExtCommunity,
       "fsMIBgp4mpebgp4PathAttrUnknown": fsMIBgp4mpebgp4PathAttrUnknown,
       "fsMIBgp4mpebgp4PathAttrLabel": fsMIBgp4mpebgp4PathAttrLabel,
       "fsMIBgp4mpebgp4PathAttrAS4PathSegment": fsMIBgp4mpebgp4PathAttrAS4PathSegment,
       "fsMIBgp4mpebgp4PathAttrAggregatorAS4": fsMIBgp4mpebgp4PathAttrAggregatorAS4,
       "fsMIBgp4MpePeerExtTable": fsMIBgp4MpePeerExtTable,
       "fsMIBgp4MpePeerExtEntry": fsMIBgp4MpePeerExtEntry,
       "fsMIBgp4mpePeerExtPeerType": fsMIBgp4mpePeerExtPeerType,
       "fsMIBgp4mpePeerExtPeerRemoteAddr": fsMIBgp4mpePeerExtPeerRemoteAddr,
       "fsMIBgp4mpePeerExtConfigurePeer": fsMIBgp4mpePeerExtConfigurePeer,
       "fsMIBgp4mpePeerExtPeerRemoteAs": fsMIBgp4mpePeerExtPeerRemoteAs,
       "fsMIBgp4mpePeerExtEBGPMultiHop": fsMIBgp4mpePeerExtEBGPMultiHop,
       "fsMIBgp4mpePeerExtEBGPHopLimit": fsMIBgp4mpePeerExtEBGPHopLimit,
       "fsMIBgp4mpePeerExtNextHopSelf": fsMIBgp4mpePeerExtNextHopSelf,
       "fsMIBgp4mpePeerExtRflClient": fsMIBgp4mpePeerExtRflClient,
       "fsMIBgp4mpePeerExtTcpSendBufSize": fsMIBgp4mpePeerExtTcpSendBufSize,
       "fsMIBgp4mpePeerExtTcpRcvBufSize": fsMIBgp4mpePeerExtTcpRcvBufSize,
       "fsMIBgp4mpePeerExtLclAddress": fsMIBgp4mpePeerExtLclAddress,
       "fsMIBgp4mpePeerExtNetworkAddress": fsMIBgp4mpePeerExtNetworkAddress,
       "fsMIBgp4mpePeerExtGateway": fsMIBgp4mpePeerExtGateway,
       "fsMIBgp4mpePeerExtCommSendStatus": fsMIBgp4mpePeerExtCommSendStatus,
       "fsMIBgp4mpePeerExtECommSendStatus": fsMIBgp4mpePeerExtECommSendStatus,
       "fsMIBgp4mpePeerExtPassive": fsMIBgp4mpePeerExtPassive,
       "fsMIBgp4mpePeerExtDefaultOriginate": fsMIBgp4mpePeerExtDefaultOriginate,
       "fsMIBgp4mpePeerExtOverrideCapability": fsMIBgp4mpePeerExtOverrideCapability,
       "fsMIBgp4MpeMEDTable": fsMIBgp4MpeMEDTable,
       "fsMIBgp4MpeMEDEntry": fsMIBgp4MpeMEDEntry,
       "fsMIBgp4mpeMEDIndex": fsMIBgp4mpeMEDIndex,
       "fsMIBgp4mpeMEDAdminStatus": fsMIBgp4mpeMEDAdminStatus,
       "fsMIBgp4mpeMEDRemoteAS": fsMIBgp4mpeMEDRemoteAS,
       "fsMIBgp4mpeMEDIPAddrAfi": fsMIBgp4mpeMEDIPAddrAfi,
       "fsMIBgp4mpeMEDIPAddrSafi": fsMIBgp4mpeMEDIPAddrSafi,
       "fsMIBgp4mpeMEDIPAddrPrefix": fsMIBgp4mpeMEDIPAddrPrefix,
       "fsMIBgp4mpeMEDIPAddrPrefixLen": fsMIBgp4mpeMEDIPAddrPrefixLen,
       "fsMIBgp4mpeMEDIntermediateAS": fsMIBgp4mpeMEDIntermediateAS,
       "fsMIBgp4mpeMEDDirection": fsMIBgp4mpeMEDDirection,
       "fsMIBgp4mpeMEDValue": fsMIBgp4mpeMEDValue,
       "fsMIBgp4mpeMEDPreference": fsMIBgp4mpeMEDPreference,
       "fsMIBgp4mpeMEDVrfName": fsMIBgp4mpeMEDVrfName,
       "fsMIBgp4MpeLocalPrefTable": fsMIBgp4MpeLocalPrefTable,
       "fsMIBgp4MpeLocalPrefEntry": fsMIBgp4MpeLocalPrefEntry,
       "fsMIBgp4mpeLocalPrefIndex": fsMIBgp4mpeLocalPrefIndex,
       "fsMIBgp4mpeLocalPrefAdminStatus": fsMIBgp4mpeLocalPrefAdminStatus,
       "fsMIBgp4mpeLocalPrefRemoteAS": fsMIBgp4mpeLocalPrefRemoteAS,
       "fsMIBgp4mpeLocalPrefIPAddrAfi": fsMIBgp4mpeLocalPrefIPAddrAfi,
       "fsMIBgp4mpeLocalPrefIPAddrSafi": fsMIBgp4mpeLocalPrefIPAddrSafi,
       "fsMIBgp4mpeLocalPrefIPAddrPrefix": fsMIBgp4mpeLocalPrefIPAddrPrefix,
       "fsMIBgp4mpeLocalPrefIPAddrPrefixLen": fsMIBgp4mpeLocalPrefIPAddrPrefixLen,
       "fsMIBgp4mpeLocalPrefIntermediateAS": fsMIBgp4mpeLocalPrefIntermediateAS,
       "fsMIBgp4mpeLocalPrefDirection": fsMIBgp4mpeLocalPrefDirection,
       "fsMIBgp4mpeLocalPrefValue": fsMIBgp4mpeLocalPrefValue,
       "fsMIBgp4mpeLocalPrefPreference": fsMIBgp4mpeLocalPrefPreference,
       "fsMIBgp4mpeLocalPrefVrfName": fsMIBgp4mpeLocalPrefVrfName,
       "fsMIBgp4MpeUpdateFilterTable": fsMIBgp4MpeUpdateFilterTable,
       "fsMIBgp4MpeUpdateFilterEntry": fsMIBgp4MpeUpdateFilterEntry,
       "fsMIBgp4mpeUpdateFilterIndex": fsMIBgp4mpeUpdateFilterIndex,
       "fsMIBgp4mpeUpdateFilterAdminStatus": fsMIBgp4mpeUpdateFilterAdminStatus,
       "fsMIBgp4mpeUpdateFilterRemoteAS": fsMIBgp4mpeUpdateFilterRemoteAS,
       "fsMIBgp4mpeUpdateFilterIPAddrAfi": fsMIBgp4mpeUpdateFilterIPAddrAfi,
       "fsMIBgp4mpeUpdateFilterIPAddrSafi": fsMIBgp4mpeUpdateFilterIPAddrSafi,
       "fsMIBgp4mpeUpdateFilterIPAddrPrefix": fsMIBgp4mpeUpdateFilterIPAddrPrefix,
       "fsMIBgp4mpeUpdateFilterIPAddrPrefixLen": fsMIBgp4mpeUpdateFilterIPAddrPrefixLen,
       "fsMIBgp4mpeUpdateFilterIntermediateAS": fsMIBgp4mpeUpdateFilterIntermediateAS,
       "fsMIBgp4mpeUpdateFilterDirection": fsMIBgp4mpeUpdateFilterDirection,
       "fsMIBgp4mpeUpdateFilterAction": fsMIBgp4mpeUpdateFilterAction,
       "fsMIBgp4mpeUpdateFilterVrfName": fsMIBgp4mpeUpdateFilterVrfName,
       "fsMIBgp4MpeAggregateTable": fsMIBgp4MpeAggregateTable,
       "fsMIBgp4MpeAggregateEntry": fsMIBgp4MpeAggregateEntry,
       "fsMIBgp4mpeAggregateIndex": fsMIBgp4mpeAggregateIndex,
       "fsMIBgp4mpeAggregateAdminStatus": fsMIBgp4mpeAggregateAdminStatus,
       "fsMIBgp4mpeAggregateIPAddrAfi": fsMIBgp4mpeAggregateIPAddrAfi,
       "fsMIBgp4mpeAggregateIPAddrSafi": fsMIBgp4mpeAggregateIPAddrSafi,
       "fsMIBgp4mpeAggregateIPAddrPrefix": fsMIBgp4mpeAggregateIPAddrPrefix,
       "fsMIBgp4mpeAggregateIPAddrPrefixLen": fsMIBgp4mpeAggregateIPAddrPrefixLen,
       "fsMIBgp4mpeAggregateAdvertise": fsMIBgp4mpeAggregateAdvertise,
       "fsMIBgp4mpeAggregateVrfName": fsMIBgp4mpeAggregateVrfName,
       "fsMIBgp4mpeAggregateAsSet": fsMIBgp4mpeAggregateAsSet,
       "fsMIBgp4mpeAggregateAdvertiseRouteMapName": fsMIBgp4mpeAggregateAdvertiseRouteMapName,
       "fsMIBgp4mpeAggregateSuppressRouteMapName": fsMIBgp4mpeAggregateSuppressRouteMapName,
       "fsMIBgp4mpeAggregateAttributeRouteMapName": fsMIBgp4mpeAggregateAttributeRouteMapName,
       "fsMIBgp4MpeImportRouteTable": fsMIBgp4MpeImportRouteTable,
       "fsMIBgp4MpeImportRouteEntry": fsMIBgp4MpeImportRouteEntry,
       "fsMIBgp4mpeImportRoutePrefixAfi": fsMIBgp4mpeImportRoutePrefixAfi,
       "fsMIBgp4mpeImportRoutePrefixSafi": fsMIBgp4mpeImportRoutePrefixSafi,
       "fsMIBgp4mpeImportRoutePrefix": fsMIBgp4mpeImportRoutePrefix,
       "fsMIBgp4mpeImportRoutePrefixLen": fsMIBgp4mpeImportRoutePrefixLen,
       "fsMIBgp4mpeImportRouteProtocol": fsMIBgp4mpeImportRouteProtocol,
       "fsMIBgp4mpeImportRouteNextHop": fsMIBgp4mpeImportRouteNextHop,
       "fsMIBgp4mpeImportRouteIfIndex": fsMIBgp4mpeImportRouteIfIndex,
       "fsMIBgp4mpeImportRouteMetric": fsMIBgp4mpeImportRouteMetric,
       "fsMIBgp4mpeImportRouteVrf": fsMIBgp4mpeImportRouteVrf,
       "fsMIBgp4mpeImportRouteAction": fsMIBgp4mpeImportRouteAction,
       "fsMIBgp4MpeFsmTransitionHistTable": fsMIBgp4MpeFsmTransitionHistTable,
       "fsMIBgp4MpeFsmTransitionHistEntry": fsMIBgp4MpeFsmTransitionHistEntry,
       "fsMIBgp4mpePeerType": fsMIBgp4mpePeerType,
       "fsMIBgp4mpePeer": fsMIBgp4mpePeer,
       "fsMIBgp4mpeFsmTransitionHist": fsMIBgp4mpeFsmTransitionHist,
       "fsMIBgp4MpeRfd": fsMIBgp4MpeRfd,
       "fsMIBgp4MpeRfdRtDampHistTable": fsMIBgp4MpeRfdRtDampHistTable,
       "fsMIBgp4MpeRfdRtDampHistEntry": fsMIBgp4MpeRfdRtDampHistEntry,
       "fsMIBgp4mpePathAttrAddrPrefixAfi": fsMIBgp4mpePathAttrAddrPrefixAfi,
       "fsMIBgp4mpePathAttrAddrPrefixSafi": fsMIBgp4mpePathAttrAddrPrefixSafi,
       "fsMIBgp4mpePathAttrAddrPrefix": fsMIBgp4mpePathAttrAddrPrefix,
       "fsMIBgp4mpePathAttrAddrPrefixLen": fsMIBgp4mpePathAttrAddrPrefixLen,
       "fsMIBgp4mpePathAttrPeerType": fsMIBgp4mpePathAttrPeerType,
       "fsMIBgp4mpePathAttrPeer": fsMIBgp4mpePathAttrPeer,
       "fsMIBgp4mpeRfdRtFom": fsMIBgp4mpeRfdRtFom,
       "fsMIBgp4mpeRfdRtLastUpdtTime": fsMIBgp4mpeRfdRtLastUpdtTime,
       "fsMIBgp4mpeRfdRtState": fsMIBgp4mpeRfdRtState,
       "fsMIBgp4mpeRfdRtStatus": fsMIBgp4mpeRfdRtStatus,
       "fsMIBgp4mpeRfdRtFlapCount": fsMIBgp4mpeRfdRtFlapCount,
       "fsMIBgp4mpeRfdRtFlapTime": fsMIBgp4mpeRfdRtFlapTime,
       "fsMIBgp4mpeRfdRtReuseTime": fsMIBgp4mpeRfdRtReuseTime,
       "fsMIBgp4MpeRfdPeerDampHistTable": fsMIBgp4MpeRfdPeerDampHistTable,
       "fsMIBgp4MpeRfdPeerDampHistEntry": fsMIBgp4MpeRfdPeerDampHistEntry,
       "fsMIBgp4mpePeerRemoteIpAddrType": fsMIBgp4mpePeerRemoteIpAddrType,
       "fsMIBgp4mpePeerRemoteIpAddr": fsMIBgp4mpePeerRemoteIpAddr,
       "fsMIBgp4mpeRfdPeerFom": fsMIBgp4mpeRfdPeerFom,
       "fsMIBgp4mpeRfdPeerLastUpdtTime": fsMIBgp4mpeRfdPeerLastUpdtTime,
       "fsMIBgp4mpeRfdPeerState": fsMIBgp4mpeRfdPeerState,
       "fsMIBgp4mpeRfdPeerStatus": fsMIBgp4mpeRfdPeerStatus,
       "fsMIBgp4MpeRfdRtsReuseListTable": fsMIBgp4MpeRfdRtsReuseListTable,
       "fsMIBgp4MpeRfdRtsReuseListEntry": fsMIBgp4MpeRfdRtsReuseListEntry,
       "fsMIBgp4mpeRtAfi": fsMIBgp4mpeRtAfi,
       "fsMIBgp4mpeRtSafi": fsMIBgp4mpeRtSafi,
       "fsMIBgp4mpeRtIPPrefix": fsMIBgp4mpeRtIPPrefix,
       "fsMIBgp4mpeRtIPPrefixLen": fsMIBgp4mpeRtIPPrefixLen,
       "fsMIBgp4mpeRfdRtsReusePeerType": fsMIBgp4mpeRfdRtsReusePeerType,
       "fsMIBgp4mpePeerRemAddress": fsMIBgp4mpePeerRemAddress,
       "fsMIBgp4mpeRfdRtReuseListRtFom": fsMIBgp4mpeRfdRtReuseListRtFom,
       "fsMIBgp4mpeRfdRtReuseListRtLastUpdtTime": fsMIBgp4mpeRfdRtReuseListRtLastUpdtTime,
       "fsMIBgp4mpeRfdRtReuseListRtState": fsMIBgp4mpeRfdRtReuseListRtState,
       "fsMIBgp4mpeRfdRtReuseListRtStatus": fsMIBgp4mpeRfdRtReuseListRtStatus,
       "fsMIBgp4MpeRfdPeerReuseListTable": fsMIBgp4MpeRfdPeerReuseListTable,
       "fsMIBgp4MpeRfdPeerReuseListEntry": fsMIBgp4MpeRfdPeerReuseListEntry,
       "fsMIBgp4mpeRfdPeerRemIpAddrType": fsMIBgp4mpeRfdPeerRemIpAddrType,
       "fsMIBgp4mpeRfdPeerRemIpAddr": fsMIBgp4mpeRfdPeerRemIpAddr,
       "fsMIBgp4mpeRfdPeerReuseListPeerFom": fsMIBgp4mpeRfdPeerReuseListPeerFom,
       "fsMIBgp4mpeRfdPeerReuseListLastUpdtTime": fsMIBgp4mpeRfdPeerReuseListLastUpdtTime,
       "fsMIBgp4mpeRfdPeerReuseListPeerState": fsMIBgp4mpeRfdPeerReuseListPeerState,
       "fsMIBgp4mpeRfdPeerReuseListPeerStatus": fsMIBgp4mpeRfdPeerReuseListPeerStatus,
       "fsMIBgp4MpeComm": fsMIBgp4MpeComm,
       "fsMIBgp4MpeCommRouteAddCommTable": fsMIBgp4MpeCommRouteAddCommTable,
       "fsMIBgp4MpeCommRouteAddCommEntry": fsMIBgp4MpeCommRouteAddCommEntry,
       "fsMIBgp4mpeAddCommRtAfi": fsMIBgp4mpeAddCommRtAfi,
       "fsMIBgp4mpeAddCommRtSafi": fsMIBgp4mpeAddCommRtSafi,
       "fsMIBgp4mpeAddCommIpNetwork": fsMIBgp4mpeAddCommIpNetwork,
       "fsMIBgp4mpeAddCommIpPrefixLen": fsMIBgp4mpeAddCommIpPrefixLen,
       "fsMIBgp4mpeAddCommVal": fsMIBgp4mpeAddCommVal,
       "fsMIBgp4mpeAddCommRowStatus": fsMIBgp4mpeAddCommRowStatus,
       "fsMIBgp4MpeCommRouteDeleteCommTable": fsMIBgp4MpeCommRouteDeleteCommTable,
       "fsMIBgp4MpeCommRouteDeleteCommEntry": fsMIBgp4MpeCommRouteDeleteCommEntry,
       "fsMIBgp4mpeDeleteCommRtAfi": fsMIBgp4mpeDeleteCommRtAfi,
       "fsMIBgp4mpeDeleteCommRtSafi": fsMIBgp4mpeDeleteCommRtSafi,
       "fsMIBgp4mpeDeleteCommIpNetwork": fsMIBgp4mpeDeleteCommIpNetwork,
       "fsMIBgp4mpeDeleteCommIpPrefixLen": fsMIBgp4mpeDeleteCommIpPrefixLen,
       "fsMIBgp4mpeDeleteCommVal": fsMIBgp4mpeDeleteCommVal,
       "fsMIBgp4mpeDeleteCommRowStatus": fsMIBgp4mpeDeleteCommRowStatus,
       "fsMIBgp4MpeCommRouteCommSetStatusTable": fsMIBgp4MpeCommRouteCommSetStatusTable,
       "fsMIBgp4MpeCommRouteCommSetStatusEntry": fsMIBgp4MpeCommRouteCommSetStatusEntry,
       "fsMIBgp4mpeCommSetStatusAfi": fsMIBgp4mpeCommSetStatusAfi,
       "fsMIBgp4mpeCommSetStatusSafi": fsMIBgp4mpeCommSetStatusSafi,
       "fsMIBgp4mpeCommSetStatusIpNetwork": fsMIBgp4mpeCommSetStatusIpNetwork,
       "fsMIBgp4mpeCommSetStatusIpPrefixLen": fsMIBgp4mpeCommSetStatusIpPrefixLen,
       "fsMIBgp4mpeCommSetStatus": fsMIBgp4mpeCommSetStatus,
       "fsMIBgp4mpeCommSetStatusRowStatus": fsMIBgp4mpeCommSetStatusRowStatus,
       "fsMIBgp4MpeExtComm": fsMIBgp4MpeExtComm,
       "fsMIBgp4MpeExtCommRouteAddExtCommTable": fsMIBgp4MpeExtCommRouteAddExtCommTable,
       "fsMIBgp4MpeExtCommRouteAddExtCommEntry": fsMIBgp4MpeExtCommRouteAddExtCommEntry,
       "fsMIBgp4mpeAddExtCommRtAfi": fsMIBgp4mpeAddExtCommRtAfi,
       "fsMIBgp4mpeAddExtCommRtSafi": fsMIBgp4mpeAddExtCommRtSafi,
       "fsMIBgp4mpeAddExtCommIpNetwork": fsMIBgp4mpeAddExtCommIpNetwork,
       "fsMIBgp4mpeAddExtCommIpPrefixLen": fsMIBgp4mpeAddExtCommIpPrefixLen,
       "fsMIBgp4mpeAddExtCommVal": fsMIBgp4mpeAddExtCommVal,
       "fsMIBgp4mpeAddExtCommRowStatus": fsMIBgp4mpeAddExtCommRowStatus,
       "fsMIBgp4MpeExtCommRouteDeleteExtCommTable": fsMIBgp4MpeExtCommRouteDeleteExtCommTable,
       "fsMIBgp4MpeExtCommRouteDeleteExtCommEntry": fsMIBgp4MpeExtCommRouteDeleteExtCommEntry,
       "fsMIBgp4mpeDeleteExtCommRtAfi": fsMIBgp4mpeDeleteExtCommRtAfi,
       "fsMIBgp4mpeDeleteExtCommRtSafi": fsMIBgp4mpeDeleteExtCommRtSafi,
       "fsMIBgp4mpeDeleteExtCommIpNetwork": fsMIBgp4mpeDeleteExtCommIpNetwork,
       "fsMIBgp4mpeDeleteExtCommIpPrefixLen": fsMIBgp4mpeDeleteExtCommIpPrefixLen,
       "fsMIBgp4mpeDeleteExtCommVal": fsMIBgp4mpeDeleteExtCommVal,
       "fsMIBgp4mpeDeleteExtCommRowStatus": fsMIBgp4mpeDeleteExtCommRowStatus,
       "fsMIBgp4MpeExtCommRouteExtCommSetStatusTable": fsMIBgp4MpeExtCommRouteExtCommSetStatusTable,
       "fsMIBgp4MpeExtCommRouteExtCommSetStatusEntry": fsMIBgp4MpeExtCommRouteExtCommSetStatusEntry,
       "fsMIBgp4mpeExtCommSetStatusRtAfi": fsMIBgp4mpeExtCommSetStatusRtAfi,
       "fsMIBgp4mpeExtCommSetStatusRtSafi": fsMIBgp4mpeExtCommSetStatusRtSafi,
       "fsMIBgp4mpeExtCommSetStatusIpNetwork": fsMIBgp4mpeExtCommSetStatusIpNetwork,
       "fsMIBgp4mpeExtCommSetStatusIpPrefixLen": fsMIBgp4mpeExtCommSetStatusIpPrefixLen,
       "fsMIBgp4mpeExtCommSetStatus": fsMIBgp4mpeExtCommSetStatus,
       "fsMIBgp4mpeExtCommSetStatusRowStatus": fsMIBgp4mpeExtCommSetStatusRowStatus,
       "fsMIBgp4MpePeerLinkBwTable": fsMIBgp4MpePeerLinkBwTable,
       "fsMIBgp4MpePeerLinkBwEntry": fsMIBgp4MpePeerLinkBwEntry,
       "fsMIBgp4mpePeerLinkType": fsMIBgp4mpePeerLinkType,
       "fsMIBgp4mpePeerLinkRemAddr": fsMIBgp4mpePeerLinkRemAddr,
       "fsMIBgp4mpeLinkBandWidth": fsMIBgp4mpeLinkBandWidth,
       "fsMIBgp4mpePeerLinkBwRowStatus": fsMIBgp4mpePeerLinkBwRowStatus,
       "fsMIBgp4MpeCaps": fsMIBgp4MpeCaps,
       "fsMIBgp4MpeCapSupportedCapsTable": fsMIBgp4MpeCapSupportedCapsTable,
       "fsMIBgp4MpeCapSupportedCapsEntry": fsMIBgp4MpeCapSupportedCapsEntry,
       "fsMIBgp4mpeCapPeerType": fsMIBgp4mpeCapPeerType,
       "fsMIBgp4mpeCapPeerRemoteIpAddr": fsMIBgp4mpeCapPeerRemoteIpAddr,
       "fsMIBgp4mpeSupportedCapabilityCode": fsMIBgp4mpeSupportedCapabilityCode,
       "fsMIBgp4mpeSupportedCapabilityLength": fsMIBgp4mpeSupportedCapabilityLength,
       "fsMIBgp4mpeSupportedCapabilityValue": fsMIBgp4mpeSupportedCapabilityValue,
       "fsMIBgp4mpeCapSupportedCapsRowStatus": fsMIBgp4mpeCapSupportedCapsRowStatus,
       "fsMIBgp4mpeCapAnnouncedStatus": fsMIBgp4mpeCapAnnouncedStatus,
       "fsMIBgp4mpeCapReceivedStatus": fsMIBgp4mpeCapReceivedStatus,
       "fsMIBgp4mpeCapNegotiatedStatus": fsMIBgp4mpeCapNegotiatedStatus,
       "fsMIBgp4mpeCapConfiguredStatus": fsMIBgp4mpeCapConfiguredStatus,
       "fsMIBgp4MpeRtRefresh": fsMIBgp4MpeRtRefresh,
       "fsMIBgp4MpeRtRefreshInboundTable": fsMIBgp4MpeRtRefreshInboundTable,
       "fsMIBgp4MpeRtRefreshInboundEntry": fsMIBgp4MpeRtRefreshInboundEntry,
       "fsMIBgp4mpeRtRefreshInboundPeerType": fsMIBgp4mpeRtRefreshInboundPeerType,
       "fsMIBgp4mpeRtRefreshInboundPeerAddr": fsMIBgp4mpeRtRefreshInboundPeerAddr,
       "fsMIBgp4mpeRtRefreshInboundAfi": fsMIBgp4mpeRtRefreshInboundAfi,
       "fsMIBgp4mpeRtRefreshInboundSafi": fsMIBgp4mpeRtRefreshInboundSafi,
       "fsMIBgp4mpeRtRefreshInboundRequest": fsMIBgp4mpeRtRefreshInboundRequest,
       "fsMIBgp4mpeRtRefreshInboundPrefixFilter": fsMIBgp4mpeRtRefreshInboundPrefixFilter,
       "fsMIBgp4MpeRtRefreshStatisticsTable": fsMIBgp4MpeRtRefreshStatisticsTable,
       "fsMIBgp4MpeRtRefreshStatisticsEntry": fsMIBgp4MpeRtRefreshStatisticsEntry,
       "fsMIBgp4mpeRtRefreshStatisticsPeerType": fsMIBgp4mpeRtRefreshStatisticsPeerType,
       "fsMIBgp4mpeRtRefreshStatisticsPeerAddr": fsMIBgp4mpeRtRefreshStatisticsPeerAddr,
       "fsMIBgp4mpeRtRefreshStatisticsAfi": fsMIBgp4mpeRtRefreshStatisticsAfi,
       "fsMIBgp4mpeRtRefreshStatisticsSafi": fsMIBgp4mpeRtRefreshStatisticsSafi,
       "fsMIBgp4mpeRtRefreshStatisticsRtRefMsgSentCntr": fsMIBgp4mpeRtRefreshStatisticsRtRefMsgSentCntr,
       "fsMIBgp4mpeRtRefreshStatisticsRtRefMsgTxErrCntr": fsMIBgp4mpeRtRefreshStatisticsRtRefMsgTxErrCntr,
       "fsMIBgp4mpeRtRefreshStatisticsRtRefMsgRcvdCntr": fsMIBgp4mpeRtRefreshStatisticsRtRefMsgRcvdCntr,
       "fsMIBgp4mpeRtRefreshStatisticsRtRefMsgInvalidCntr": fsMIBgp4mpeRtRefreshStatisticsRtRefMsgInvalidCntr,
       "fsMIBgp4MpeSoftReconfigOut": fsMIBgp4MpeSoftReconfigOut,
       "fsMIBgp4MpeSoftReconfigOutboundTable": fsMIBgp4MpeSoftReconfigOutboundTable,
       "fsMIBgp4MpeSoftReconfigOutboundEntry": fsMIBgp4MpeSoftReconfigOutboundEntry,
       "fsMIBgp4mpeSoftReconfigOutboundPeerType": fsMIBgp4mpeSoftReconfigOutboundPeerType,
       "fsMIBgp4mpeSoftReconfigOutboundPeerAddr": fsMIBgp4mpeSoftReconfigOutboundPeerAddr,
       "fsMIBgp4mpeSoftReconfigOutboundAfi": fsMIBgp4mpeSoftReconfigOutboundAfi,
       "fsMIBgp4mpeSoftReconfigOutboundSafi": fsMIBgp4mpeSoftReconfigOutboundSafi,
       "fsMIBgp4mpeSoftReconfigOutboundRequest": fsMIBgp4mpeSoftReconfigOutboundRequest,
       "fsMIBgp4MpePrefixCountersTable": fsMIBgp4MpePrefixCountersTable,
       "fsMIBgp4MpePrefixCountersEntry": fsMIBgp4MpePrefixCountersEntry,
       "fsMIBgp4MpePeerRemoteAddrType": fsMIBgp4MpePeerRemoteAddrType,
       "fsMIBgp4MpePeerRemoteAddr": fsMIBgp4MpePeerRemoteAddr,
       "fsMIBgp4MpePrefixCountersAfi": fsMIBgp4MpePrefixCountersAfi,
       "fsMIBgp4MpePrefixCountersSafi": fsMIBgp4MpePrefixCountersSafi,
       "fsMIBgp4MpePrefixCountersPrefixesReceived": fsMIBgp4MpePrefixCountersPrefixesReceived,
       "fsMIBgp4MpePrefixCountersPrefixesSent": fsMIBgp4MpePrefixCountersPrefixesSent,
       "fsMIBgp4MpePrefixCountersWithdrawsReceived": fsMIBgp4MpePrefixCountersWithdrawsReceived,
       "fsMIBgp4MpePrefixCountersWithdrawsSent": fsMIBgp4MpePrefixCountersWithdrawsSent,
       "fsMIBgp4MpePrefixCountersInPrefixes": fsMIBgp4MpePrefixCountersInPrefixes,
       "fsMIBgp4MpePrefixCountersInPrefixesAccepted": fsMIBgp4MpePrefixCountersInPrefixesAccepted,
       "fsMIBgp4MpePrefixCountersInPrefixesRejected": fsMIBgp4MpePrefixCountersInPrefixesRejected,
       "fsMIBgp4MpePrefixCountersOutPrefixes": fsMIBgp4MpePrefixCountersOutPrefixes,
       "fsMIBgp4DistInOutRouteMap": fsMIBgp4DistInOutRouteMap,
       "fsMIBgp4DistInOutRouteMapTable": fsMIBgp4DistInOutRouteMapTable,
       "fsMIBgp4DistInOutRouteMapEntry": fsMIBgp4DistInOutRouteMapEntry,
       "fsMIBgp4DistInOutRouteMapName": fsMIBgp4DistInOutRouteMapName,
       "fsMIBgp4DistInOutRouteMapType": fsMIBgp4DistInOutRouteMapType,
       "fsMIBgp4DistInOutRouteMapValue": fsMIBgp4DistInOutRouteMapValue,
       "fsMIBgp4DistInOutRouteMapRowStatus": fsMIBgp4DistInOutRouteMapRowStatus,
       "fsMIBgp4Notification": fsMIBgp4Notification,
       "fsMIBgp4Trap": fsMIBgp4Trap,
       "fsMIBgp4RestartStatusChange": fsMIBgp4RestartStatusChange,
       "fsMIBgp4RouteAddRTMFailure": fsMIBgp4RouteAddRTMFailure,
       "fsMIBgp4Objects": fsMIBgp4Objects,
       "fsMIBgp4TrapContextId": fsMIBgp4TrapContextId,
       "fsMIBgp4TrapRouteAddressType": fsMIBgp4TrapRouteAddressType,
       "fsMIBgp4TrapRoutePrefix": fsMIBgp4TrapRoutePrefix,
       "fsMIBgp4NextHop": fsMIBgp4NextHop,
       "fsMIBgp4TrapPeerAddrType": fsMIBgp4TrapPeerAddrType,
       "fsMIBgp4TrapPeerAddr": fsMIBgp4TrapPeerAddr,
       "fsMIBgp4NeighborRouteMap": fsMIBgp4NeighborRouteMap,
       "fsMIBgp4NeighborRouteMapTable": fsMIBgp4NeighborRouteMapTable,
       "fsMIBgp4NeighborRouteMapEntry": fsMIBgp4NeighborRouteMapEntry,
       "fsMIBgp4NeighborRouteMapPeerAddrType": fsMIBgp4NeighborRouteMapPeerAddrType,
       "fsMIBgp4NeighborRouteMapPeer": fsMIBgp4NeighborRouteMapPeer,
       "fsMIBgp4NeighborRouteMapDirection": fsMIBgp4NeighborRouteMapDirection,
       "fsMIBgp4NeighborRouteMapName": fsMIBgp4NeighborRouteMapName,
       "fsMIBgp4NeighborRouteMapRowStatus": fsMIBgp4NeighborRouteMapRowStatus,
       "fsMIBgp4PeerGroupTable": fsMIBgp4PeerGroupTable,
       "fsMIBgp4PeerGroupEntry": fsMIBgp4PeerGroupEntry,
       "fsMIBgp4PeerGroupName": fsMIBgp4PeerGroupName,
       "fsMIBgp4PeerGroupAddrType": fsMIBgp4PeerGroupAddrType,
       "fsMIBgp4PeerGroupRemoteAs": fsMIBgp4PeerGroupRemoteAs,
       "fsMIBgp4PeerGroupHoldTimeConfigured": fsMIBgp4PeerGroupHoldTimeConfigured,
       "fsMIBgp4PeerGroupKeepAliveConfigured": fsMIBgp4PeerGroupKeepAliveConfigured,
       "fsMIBgp4PeerGroupConnectRetryInterval": fsMIBgp4PeerGroupConnectRetryInterval,
       "fsMIBgp4PeerGroupMinASOriginInterval": fsMIBgp4PeerGroupMinASOriginInterval,
       "fsMIBgp4PeerGroupMinRouteAdvInterval": fsMIBgp4PeerGroupMinRouteAdvInterval,
       "fsMIBgp4PeerGroupAllowAutomaticStart": fsMIBgp4PeerGroupAllowAutomaticStart,
       "fsMIBgp4PeerGroupAllowAutomaticStop": fsMIBgp4PeerGroupAllowAutomaticStop,
       "fsMIBgp4PeerGroupIdleHoldTimeConfigured": fsMIBgp4PeerGroupIdleHoldTimeConfigured,
       "fsMIBgp4PeerGroupDampPeerOscillations": fsMIBgp4PeerGroupDampPeerOscillations,
       "fsMIBgp4PeerGroupDelayOpen": fsMIBgp4PeerGroupDelayOpen,
       "fsMIBgp4PeerGroupDelayOpenTimeConfigured": fsMIBgp4PeerGroupDelayOpenTimeConfigured,
       "fsMIBgp4PeerGroupPrefixUpperLimit": fsMIBgp4PeerGroupPrefixUpperLimit,
       "fsMIBgp4PeerGroupTcpConnectRetryCnt": fsMIBgp4PeerGroupTcpConnectRetryCnt,
       "fsMIBgp4PeerGroupEBGPMultiHop": fsMIBgp4PeerGroupEBGPMultiHop,
       "fsMIBgp4PeerGroupEBGPHopLimit": fsMIBgp4PeerGroupEBGPHopLimit,
       "fsMIBgp4PeerGroupNextHopSelf": fsMIBgp4PeerGroupNextHopSelf,
       "fsMIBgp4PeerGroupRflClient": fsMIBgp4PeerGroupRflClient,
       "fsMIBgp4PeerGroupTcpSendBufSize": fsMIBgp4PeerGroupTcpSendBufSize,
       "fsMIBgp4PeerGroupTcpRcvBufSize": fsMIBgp4PeerGroupTcpRcvBufSize,
       "fsMIBgp4PeerGroupCommSendStatus": fsMIBgp4PeerGroupCommSendStatus,
       "fsMIBgp4PeerGroupECommSendStatus": fsMIBgp4PeerGroupECommSendStatus,
       "fsMIBgp4PeerGroupPassive": fsMIBgp4PeerGroupPassive,
       "fsMIBgp4PeerGroupDefaultOriginate": fsMIBgp4PeerGroupDefaultOriginate,
       "fsMIBgp4PeerGroupActivateMPCapability": fsMIBgp4PeerGroupActivateMPCapability,
       "fsMIBgp4PeerGroupDeactivateMPCapability": fsMIBgp4PeerGroupDeactivateMPCapability,
       "fsMIBgp4PeerGroupRouteMapNameIn": fsMIBgp4PeerGroupRouteMapNameIn,
       "fsMIBgp4PeerGroupRouteMapNameOut": fsMIBgp4PeerGroupRouteMapNameOut,
       "fsMIBgp4PeerGroupStatus": fsMIBgp4PeerGroupStatus,
       "fsMIBgp4PeerGroupIpPrefixNameIn": fsMIBgp4PeerGroupIpPrefixNameIn,
       "fsMIBgp4PeerGroupIpPrefixNameOut": fsMIBgp4PeerGroupIpPrefixNameOut,
       "fsMIBgp4PeerGroupOrfType": fsMIBgp4PeerGroupOrfType,
       "fsMIBgp4PeerGroupOrfCapMode": fsMIBgp4PeerGroupOrfCapMode,
       "fsMIBgp4PeerGroupOrfRequest": fsMIBgp4PeerGroupOrfRequest,
       "fsMIBgp4PeerGroupBfdStatus": fsMIBgp4PeerGroupBfdStatus,
       "fsMIBgp4PeerGroupOverrideCapability": fsMIBgp4PeerGroupOverrideCapability,
       "fsMIBgp4PeerGroupListTable": fsMIBgp4PeerGroupListTable,
       "fsMIBgp4PeerGroupListEntry": fsMIBgp4PeerGroupListEntry,
       "fsMIBgp4PeerAddrType": fsMIBgp4PeerAddrType,
       "fsMIBgp4PeerAddress": fsMIBgp4PeerAddress,
       "fsMIBgp4PeerAddStatus": fsMIBgp4PeerAddStatus,
       "fsMIBgp4RestartReason": fsMIBgp4RestartReason,
       "fsMIBgp4TCPMKTAuth": fsMIBgp4TCPMKTAuth,
       "fsMIBgp4TCPMKTAuthTable": fsMIBgp4TCPMKTAuthTable,
       "fsMIBgp4TCPMKTAuthEntry": fsMIBgp4TCPMKTAuthEntry,
       "fsMIBgp4TCPMKTAuthKeyId": fsMIBgp4TCPMKTAuthKeyId,
       "fsMIBgp4TCPMKTAuthRecvKeyId": fsMIBgp4TCPMKTAuthRecvKeyId,
       "fsMIBgp4TCPMKTAuthMasterKey": fsMIBgp4TCPMKTAuthMasterKey,
       "fsMIBgp4TCPMKTAuthAlgo": fsMIBgp4TCPMKTAuthAlgo,
       "fsMIBgp4TCPMKTAuthTcpOptExc": fsMIBgp4TCPMKTAuthTcpOptExc,
       "fsMIBgp4TCPMKTAuthRowStatus": fsMIBgp4TCPMKTAuthRowStatus,
       "fsMIBgp4TCPAOAuthPeer": fsMIBgp4TCPAOAuthPeer,
       "fsMIBgp4TCPAOAuthPeerTable": fsMIBgp4TCPAOAuthPeerTable,
       "fsMIBgp4TCPAOAuthPeerEntry": fsMIBgp4TCPAOAuthPeerEntry,
       "fsMIBgp4TCPAOAuthPeerType": fsMIBgp4TCPAOAuthPeerType,
       "fsMIBgp4TCPAOAuthPeerAddr": fsMIBgp4TCPAOAuthPeerAddr,
       "fsMIBgp4TCPAOAuthKeyId": fsMIBgp4TCPAOAuthKeyId,
       "fsMIBgp4TCPAOAuthKeyStatus": fsMIBgp4TCPAOAuthKeyStatus,
       "fsMIBgp4TCPAOAuthKeyStartAccept": fsMIBgp4TCPAOAuthKeyStartAccept,
       "fsMIBgp4TCPAOAuthKeyStartGenerate": fsMIBgp4TCPAOAuthKeyStartGenerate,
       "fsMIBgp4TCPAOAuthKeyStopGenerate": fsMIBgp4TCPAOAuthKeyStopGenerate,
       "fsMIBgp4TCPAOAuthKeyStopAccept": fsMIBgp4TCPAOAuthKeyStopAccept,
       "fsMIBgp4ORFListTable": fsMIBgp4ORFListTable,
       "fsMIBgp4ORFListEntry": fsMIBgp4ORFListEntry,
       "fsMIBgp4ORFPeerAddrType": fsMIBgp4ORFPeerAddrType,
       "fsMIBgp4ORFPeerAddr": fsMIBgp4ORFPeerAddr,
       "fsMIBgp4ORFAfi": fsMIBgp4ORFAfi,
       "fsMIBgp4ORFSafi": fsMIBgp4ORFSafi,
       "fsMIBgp4ORFType": fsMIBgp4ORFType,
       "fsMIBgp4ORFSequence": fsMIBgp4ORFSequence,
       "fsMIBgp4ORFAddrPrefix": fsMIBgp4ORFAddrPrefix,
       "fsMIBgp4ORFAddrPrefixLen": fsMIBgp4ORFAddrPrefixLen,
       "fsMIBgp4ORFMinLength": fsMIBgp4ORFMinLength,
       "fsMIBgp4ORFMaxLength": fsMIBgp4ORFMaxLength,
       "fsMIBgp4ORFAction": fsMIBgp4ORFAction,
       "fsMIBgp4RRDNetworkTable": fsMIBgp4RRDNetworkTable,
       "fsMIBgp4RRDNetworkEntry": fsMIBgp4RRDNetworkEntry,
       "fsMIBgp4RRDNetworkAddr": fsMIBgp4RRDNetworkAddr,
       "fsMIBgp4RRDNetworkAddrType": fsMIBgp4RRDNetworkAddrType,
       "fsMIBgp4RRDNetworkPrefixLen": fsMIBgp4RRDNetworkPrefixLen,
       "fsMIBgp4RRDNetworkRowStatus": fsMIBgp4RRDNetworkRowStatus,
       "fsMIBgp4MacMobDuplicationTimeInterval": fsMIBgp4MacMobDuplicationTimeInterval,
       "fsMIBgp4MaxMacMoves": fsMIBgp4MaxMacMoves}
)
