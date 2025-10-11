# SNMP MIB module (ARICENT-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-BGP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:51 2025
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

fsbgp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41)
)
if mibBuilder.loadTexts:
    fsbgp.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class InetAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )



class InetAddressType(TextualConvention, Integer32):
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



class BgpSafi(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              65,
              128)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("unicast", 1),
          ("labelledIpv4", 4),
          ("vpls", 65),
          ("vpnv4", 128))
    )



# MIB Managed Objects in the order of their OIDs

_Fsbgp4Scalars_ObjectIdentity = ObjectIdentity
fsbgp4Scalars = _Fsbgp4Scalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1)
)


class _Fsbgp4GlobalAdminStatus_Type(Integer32):
    """Custom type fsbgp4GlobalAdminStatus based on Integer32"""
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


_Fsbgp4GlobalAdminStatus_Type.__name__ = "Integer32"
_Fsbgp4GlobalAdminStatus_Object = MibScalar
fsbgp4GlobalAdminStatus = _Fsbgp4GlobalAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 1),
    _Fsbgp4GlobalAdminStatus_Type()
)
fsbgp4GlobalAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4GlobalAdminStatus.setStatus("current")


class _Fsbgp4LocalAs_Type(Unsigned32):
    """Custom type fsbgp4LocalAs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Fsbgp4LocalAs_Type.__name__ = "Unsigned32"
_Fsbgp4LocalAs_Object = MibScalar
fsbgp4LocalAs = _Fsbgp4LocalAs_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 2),
    _Fsbgp4LocalAs_Type()
)
fsbgp4LocalAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4LocalAs.setStatus("current")
_Fsbgp4Identifier_Type = IpAddress
_Fsbgp4Identifier_Object = MibScalar
fsbgp4Identifier = _Fsbgp4Identifier_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 3),
    _Fsbgp4Identifier_Type()
)
fsbgp4Identifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4Identifier.setStatus("current")


class _Fsbgp4Synchronization_Type(Integer32):
    """Custom type fsbgp4Synchronization based on Integer32"""
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


_Fsbgp4Synchronization_Type.__name__ = "Integer32"
_Fsbgp4Synchronization_Object = MibScalar
fsbgp4Synchronization = _Fsbgp4Synchronization_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 4),
    _Fsbgp4Synchronization_Type()
)
fsbgp4Synchronization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4Synchronization.setStatus("current")


class _Fsbgp4DefaultLocalPref_Type(Unsigned32):
    """Custom type fsbgp4DefaultLocalPref based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Fsbgp4DefaultLocalPref_Type.__name__ = "Unsigned32"
_Fsbgp4DefaultLocalPref_Object = MibScalar
fsbgp4DefaultLocalPref = _Fsbgp4DefaultLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 5),
    _Fsbgp4DefaultLocalPref_Type()
)
fsbgp4DefaultLocalPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4DefaultLocalPref.setStatus("current")


class _Fsbgp4AdvtNonBgpRt_Type(Integer32):
    """Custom type fsbgp4AdvtNonBgpRt based on Integer32"""
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


_Fsbgp4AdvtNonBgpRt_Type.__name__ = "Integer32"
_Fsbgp4AdvtNonBgpRt_Object = MibScalar
fsbgp4AdvtNonBgpRt = _Fsbgp4AdvtNonBgpRt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 6),
    _Fsbgp4AdvtNonBgpRt_Type()
)
fsbgp4AdvtNonBgpRt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4AdvtNonBgpRt.setStatus("current")


class _Fsbgp4TraceEnable_Type(Unsigned32):
    """Custom type fsbgp4TraceEnable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Fsbgp4TraceEnable_Type.__name__ = "Unsigned32"
_Fsbgp4TraceEnable_Object = MibScalar
fsbgp4TraceEnable = _Fsbgp4TraceEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 7),
    _Fsbgp4TraceEnable_Type()
)
fsbgp4TraceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4TraceEnable.setStatus("current")


class _Fsbgp4DebugEnable_Type(Unsigned32):
    """Custom type fsbgp4DebugEnable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Fsbgp4DebugEnable_Type.__name__ = "Unsigned32"
_Fsbgp4DebugEnable_Object = MibScalar
fsbgp4DebugEnable = _Fsbgp4DebugEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 8),
    _Fsbgp4DebugEnable_Type()
)
fsbgp4DebugEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4DebugEnable.setStatus("current")


class _Fsbgp4OverlappingRoute_Type(Integer32):
    """Custom type fsbgp4OverlappingRoute based on Integer32"""
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


_Fsbgp4OverlappingRoute_Type.__name__ = "Integer32"
_Fsbgp4OverlappingRoute_Object = MibScalar
fsbgp4OverlappingRoute = _Fsbgp4OverlappingRoute_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 9),
    _Fsbgp4OverlappingRoute_Type()
)
fsbgp4OverlappingRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4OverlappingRoute.setStatus("current")


class _Fsbgp4MaxPeerEntry_Type(Integer32):
    """Custom type fsbgp4MaxPeerEntry based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_Fsbgp4MaxPeerEntry_Type.__name__ = "Integer32"
_Fsbgp4MaxPeerEntry_Object = MibScalar
fsbgp4MaxPeerEntry = _Fsbgp4MaxPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 10),
    _Fsbgp4MaxPeerEntry_Type()
)
fsbgp4MaxPeerEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4MaxPeerEntry.setStatus("current")


class _Fsbgp4MaxNoofRoutes_Type(Integer32):
    """Custom type fsbgp4MaxNoofRoutes based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_Fsbgp4MaxNoofRoutes_Type.__name__ = "Integer32"
_Fsbgp4MaxNoofRoutes_Object = MibScalar
fsbgp4MaxNoofRoutes = _Fsbgp4MaxNoofRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 11),
    _Fsbgp4MaxNoofRoutes_Type()
)
fsbgp4MaxNoofRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4MaxNoofRoutes.setStatus("current")


class _Fsbgp4AlwaysCompareMED_Type(Integer32):
    """Custom type fsbgp4AlwaysCompareMED based on Integer32"""
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


_Fsbgp4AlwaysCompareMED_Type.__name__ = "Integer32"
_Fsbgp4AlwaysCompareMED_Object = MibScalar
fsbgp4AlwaysCompareMED = _Fsbgp4AlwaysCompareMED_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 12),
    _Fsbgp4AlwaysCompareMED_Type()
)
fsbgp4AlwaysCompareMED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4AlwaysCompareMED.setStatus("current")


class _Fsbgp4DefaultOriginate_Type(Integer32):
    """Custom type fsbgp4DefaultOriginate based on Integer32"""
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


_Fsbgp4DefaultOriginate_Type.__name__ = "Integer32"
_Fsbgp4DefaultOriginate_Object = MibScalar
fsbgp4DefaultOriginate = _Fsbgp4DefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 13),
    _Fsbgp4DefaultOriginate_Type()
)
fsbgp4DefaultOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4DefaultOriginate.setStatus("current")


class _Fsbgp4DefaultIpv4UniCast_Type(Integer32):
    """Custom type fsbgp4DefaultIpv4UniCast based on Integer32"""
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


_Fsbgp4DefaultIpv4UniCast_Type.__name__ = "Integer32"
_Fsbgp4DefaultIpv4UniCast_Object = MibScalar
fsbgp4DefaultIpv4UniCast = _Fsbgp4DefaultIpv4UniCast_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 14),
    _Fsbgp4DefaultIpv4UniCast_Type()
)
fsbgp4DefaultIpv4UniCast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4DefaultIpv4UniCast.setStatus("current")


class _Fsbgp4GRAdminStatus_Type(Integer32):
    """Custom type fsbgp4GRAdminStatus based on Integer32"""
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


_Fsbgp4GRAdminStatus_Type.__name__ = "Integer32"
_Fsbgp4GRAdminStatus_Object = MibScalar
fsbgp4GRAdminStatus = _Fsbgp4GRAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 15),
    _Fsbgp4GRAdminStatus_Type()
)
fsbgp4GRAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4GRAdminStatus.setStatus("current")


class _Fsbgp4GRRestartTimeInterval_Type(Integer32):
    """Custom type fsbgp4GRRestartTimeInterval based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Fsbgp4GRRestartTimeInterval_Type.__name__ = "Integer32"
_Fsbgp4GRRestartTimeInterval_Object = MibScalar
fsbgp4GRRestartTimeInterval = _Fsbgp4GRRestartTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 16),
    _Fsbgp4GRRestartTimeInterval_Type()
)
fsbgp4GRRestartTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4GRRestartTimeInterval.setStatus("current")


class _Fsbgp4GRSelectionDeferralTimeInterval_Type(Integer32):
    """Custom type fsbgp4GRSelectionDeferralTimeInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1800),
    )


_Fsbgp4GRSelectionDeferralTimeInterval_Type.__name__ = "Integer32"
_Fsbgp4GRSelectionDeferralTimeInterval_Object = MibScalar
fsbgp4GRSelectionDeferralTimeInterval = _Fsbgp4GRSelectionDeferralTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 17),
    _Fsbgp4GRSelectionDeferralTimeInterval_Type()
)
fsbgp4GRSelectionDeferralTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4GRSelectionDeferralTimeInterval.setStatus("current")


class _Fsbgp4GRStaleTimeInterval_Type(Integer32):
    """Custom type fsbgp4GRStaleTimeInterval based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 3600),
    )


_Fsbgp4GRStaleTimeInterval_Type.__name__ = "Integer32"
_Fsbgp4GRStaleTimeInterval_Object = MibScalar
fsbgp4GRStaleTimeInterval = _Fsbgp4GRStaleTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 18),
    _Fsbgp4GRStaleTimeInterval_Type()
)
fsbgp4GRStaleTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4GRStaleTimeInterval.setStatus("current")


class _Fsbgp4GRMode_Type(Integer32):
    """Custom type fsbgp4GRMode based on Integer32"""
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


_Fsbgp4GRMode_Type.__name__ = "Integer32"
_Fsbgp4GRMode_Object = MibScalar
fsbgp4GRMode = _Fsbgp4GRMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 19),
    _Fsbgp4GRMode_Type()
)
fsbgp4GRMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4GRMode.setStatus("current")


class _Fsbgp4RestartSupport_Type(Integer32):
    """Custom type fsbgp4RestartSupport based on Integer32"""
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
          ("plannedOnly", 2),
          ("plannedAndUnplanned", 3))
    )


_Fsbgp4RestartSupport_Type.__name__ = "Integer32"
_Fsbgp4RestartSupport_Object = MibScalar
fsbgp4RestartSupport = _Fsbgp4RestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 20),
    _Fsbgp4RestartSupport_Type()
)
fsbgp4RestartSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RestartSupport.setStatus("current")


class _Fsbgp4RestartStatus_Type(Integer32):
    """Custom type fsbgp4RestartStatus based on Integer32"""
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


_Fsbgp4RestartStatus_Type.__name__ = "Integer32"
_Fsbgp4RestartStatus_Object = MibScalar
fsbgp4RestartStatus = _Fsbgp4RestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 21),
    _Fsbgp4RestartStatus_Type()
)
fsbgp4RestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RestartStatus.setStatus("current")


class _Fsbgp4RestartExitReason_Type(Integer32):
    """Custom type fsbgp4RestartExitReason based on Integer32"""
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


_Fsbgp4RestartExitReason_Type.__name__ = "Integer32"
_Fsbgp4RestartExitReason_Object = MibScalar
fsbgp4RestartExitReason = _Fsbgp4RestartExitReason_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 22),
    _Fsbgp4RestartExitReason_Type()
)
fsbgp4RestartExitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RestartExitReason.setStatus("current")


class _Fsbgp4RestartReason_Type(Integer32):
    """Custom type fsbgp4RestartReason based on Integer32"""
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


_Fsbgp4RestartReason_Type.__name__ = "Integer32"
_Fsbgp4RestartReason_Object = MibScalar
fsbgp4RestartReason = _Fsbgp4RestartReason_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 23),
    _Fsbgp4RestartReason_Type()
)
fsbgp4RestartReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RestartReason.setStatus("current")


class _Fsbgp4ForwardingPreservation_Type(Integer32):
    """Custom type fsbgp4ForwardingPreservation based on Integer32"""
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


_Fsbgp4ForwardingPreservation_Type.__name__ = "Integer32"
_Fsbgp4ForwardingPreservation_Object = MibScalar
fsbgp4ForwardingPreservation = _Fsbgp4ForwardingPreservation_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 24),
    _Fsbgp4ForwardingPreservation_Type()
)
fsbgp4ForwardingPreservation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4ForwardingPreservation.setStatus("current")


class _Fsbgp4IsTrapEnabled_Type(Integer32):
    """Custom type fsbgp4IsTrapEnabled based on Integer32"""
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


_Fsbgp4IsTrapEnabled_Type.__name__ = "Integer32"
_Fsbgp4IsTrapEnabled_Object = MibScalar
fsbgp4IsTrapEnabled = _Fsbgp4IsTrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 25),
    _Fsbgp4IsTrapEnabled_Type()
)
fsbgp4IsTrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4IsTrapEnabled.setStatus("current")


class _Fsbgp4NextHopProcessingInterval_Type(Integer32):
    """Custom type fsbgp4NextHopProcessingInterval based on Integer32"""
    defaultValue = 60


_Fsbgp4NextHopProcessingInterval_Type.__name__ = "Integer32"
_Fsbgp4NextHopProcessingInterval_Object = MibScalar
fsbgp4NextHopProcessingInterval = _Fsbgp4NextHopProcessingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 26),
    _Fsbgp4NextHopProcessingInterval_Type()
)
fsbgp4NextHopProcessingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4NextHopProcessingInterval.setStatus("current")


class _Fsbgp4IBGPRedistributionStatus_Type(Integer32):
    """Custom type fsbgp4IBGPRedistributionStatus based on Integer32"""
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


_Fsbgp4IBGPRedistributionStatus_Type.__name__ = "Integer32"
_Fsbgp4IBGPRedistributionStatus_Object = MibScalar
fsbgp4IBGPRedistributionStatus = _Fsbgp4IBGPRedistributionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 27),
    _Fsbgp4IBGPRedistributionStatus_Type()
)
fsbgp4IBGPRedistributionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4IBGPRedistributionStatus.setStatus("current")


class _Fsbgp4IBGPMaxPaths_Type(Integer32):
    """Custom type fsbgp4IBGPMaxPaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Fsbgp4IBGPMaxPaths_Type.__name__ = "Integer32"
_Fsbgp4IBGPMaxPaths_Object = MibScalar
fsbgp4IBGPMaxPaths = _Fsbgp4IBGPMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 28),
    _Fsbgp4IBGPMaxPaths_Type()
)
fsbgp4IBGPMaxPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4IBGPMaxPaths.setStatus("current")


class _Fsbgp4EBGPMaxPaths_Type(Integer32):
    """Custom type fsbgp4EBGPMaxPaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Fsbgp4EBGPMaxPaths_Type.__name__ = "Integer32"
_Fsbgp4EBGPMaxPaths_Object = MibScalar
fsbgp4EBGPMaxPaths = _Fsbgp4EBGPMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 29),
    _Fsbgp4EBGPMaxPaths_Type()
)
fsbgp4EBGPMaxPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4EBGPMaxPaths.setStatus("current")


class _Fsbgp4EIBGPMaxPaths_Type(Integer32):
    """Custom type fsbgp4EIBGPMaxPaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Fsbgp4EIBGPMaxPaths_Type.__name__ = "Integer32"
_Fsbgp4EIBGPMaxPaths_Object = MibScalar
fsbgp4EIBGPMaxPaths = _Fsbgp4EIBGPMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 30),
    _Fsbgp4EIBGPMaxPaths_Type()
)
fsbgp4EIBGPMaxPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4EIBGPMaxPaths.setStatus("current")


class _Fsbgp4OperIBGPMaxPaths_Type(Integer32):
    """Custom type fsbgp4OperIBGPMaxPaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Fsbgp4OperIBGPMaxPaths_Type.__name__ = "Integer32"
_Fsbgp4OperIBGPMaxPaths_Object = MibScalar
fsbgp4OperIBGPMaxPaths = _Fsbgp4OperIBGPMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 31),
    _Fsbgp4OperIBGPMaxPaths_Type()
)
fsbgp4OperIBGPMaxPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4OperIBGPMaxPaths.setStatus("current")


class _Fsbgp4OperEBGPMaxPaths_Type(Integer32):
    """Custom type fsbgp4OperEBGPMaxPaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Fsbgp4OperEBGPMaxPaths_Type.__name__ = "Integer32"
_Fsbgp4OperEBGPMaxPaths_Object = MibScalar
fsbgp4OperEBGPMaxPaths = _Fsbgp4OperEBGPMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 32),
    _Fsbgp4OperEBGPMaxPaths_Type()
)
fsbgp4OperEBGPMaxPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4OperEBGPMaxPaths.setStatus("current")


class _Fsbgp4OperEIBGPMaxPaths_Type(Integer32):
    """Custom type fsbgp4OperEIBGPMaxPaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Fsbgp4OperEIBGPMaxPaths_Type.__name__ = "Integer32"
_Fsbgp4OperEIBGPMaxPaths_Object = MibScalar
fsbgp4OperEIBGPMaxPaths = _Fsbgp4OperEIBGPMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 33),
    _Fsbgp4OperEIBGPMaxPaths_Type()
)
fsbgp4OperEIBGPMaxPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4OperEIBGPMaxPaths.setStatus("current")


class _Fsbgp4FourByteASNSupportStatus_Type(Integer32):
    """Custom type fsbgp4FourByteASNSupportStatus based on Integer32"""
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


_Fsbgp4FourByteASNSupportStatus_Type.__name__ = "Integer32"
_Fsbgp4FourByteASNSupportStatus_Object = MibScalar
fsbgp4FourByteASNSupportStatus = _Fsbgp4FourByteASNSupportStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 34),
    _Fsbgp4FourByteASNSupportStatus_Type()
)
fsbgp4FourByteASNSupportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4FourByteASNSupportStatus.setStatus("current")


class _Fsbgp4FourByteASNotationType_Type(Integer32):
    """Custom type fsbgp4FourByteASNotationType based on Integer32"""
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


_Fsbgp4FourByteASNotationType_Type.__name__ = "Integer32"
_Fsbgp4FourByteASNotationType_Object = MibScalar
fsbgp4FourByteASNotationType = _Fsbgp4FourByteASNotationType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 35),
    _Fsbgp4FourByteASNotationType_Type()
)
fsbgp4FourByteASNotationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4FourByteASNotationType.setStatus("current")


class _Fsbgp4VpnLabelAllocPolicy_Type(Integer32):
    """Custom type fsbgp4VpnLabelAllocPolicy based on Integer32"""
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


_Fsbgp4VpnLabelAllocPolicy_Type.__name__ = "Integer32"
_Fsbgp4VpnLabelAllocPolicy_Object = MibScalar
fsbgp4VpnLabelAllocPolicy = _Fsbgp4VpnLabelAllocPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 36),
    _Fsbgp4VpnLabelAllocPolicy_Type()
)
fsbgp4VpnLabelAllocPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4VpnLabelAllocPolicy.setStatus("current")


class _Fsbgp4MacMobDuplicationTimeInterval_Type(Integer32):
    """Custom type fsbgp4MacMobDuplicationTimeInterval based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 36000),
    )


_Fsbgp4MacMobDuplicationTimeInterval_Type.__name__ = "Integer32"
_Fsbgp4MacMobDuplicationTimeInterval_Object = MibScalar
fsbgp4MacMobDuplicationTimeInterval = _Fsbgp4MacMobDuplicationTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 37),
    _Fsbgp4MacMobDuplicationTimeInterval_Type()
)
fsbgp4MacMobDuplicationTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4MacMobDuplicationTimeInterval.setStatus("current")


class _Fsbgp4MaxMacMoves_Type(Integer32):
    """Custom type fsbgp4MaxMacMoves based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Fsbgp4MaxMacMoves_Type.__name__ = "Integer32"
_Fsbgp4MaxMacMoves_Object = MibScalar
fsbgp4MaxMacMoves = _Fsbgp4MaxMacMoves_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 38),
    _Fsbgp4MaxMacMoves_Type()
)
fsbgp4MaxMacMoves.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4MaxMacMoves.setStatus("current")


class _Fsbgp4VpnRouteLeakStatus_Type(Integer32):
    """Custom type fsbgp4VpnRouteLeakStatus based on Integer32"""
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


_Fsbgp4VpnRouteLeakStatus_Type.__name__ = "Integer32"
_Fsbgp4VpnRouteLeakStatus_Object = MibScalar
fsbgp4VpnRouteLeakStatus = _Fsbgp4VpnRouteLeakStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 1, 39),
    _Fsbgp4VpnRouteLeakStatus_Type()
)
fsbgp4VpnRouteLeakStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4VpnRouteLeakStatus.setStatus("current")
_Fsbgp4PeerExtTable_Object = MibTable
fsbgp4PeerExtTable = _Fsbgp4PeerExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 2)
)
if mibBuilder.loadTexts:
    fsbgp4PeerExtTable.setStatus("deprecated")
_Fsbgp4PeerExtEntry_Object = MibTableRow
fsbgp4PeerExtEntry = _Fsbgp4PeerExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 2, 1)
)
fsbgp4PeerExtEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4PeerExtPeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    fsbgp4PeerExtEntry.setStatus("deprecated")
_Fsbgp4PeerExtPeerRemoteAddr_Type = IpAddress
_Fsbgp4PeerExtPeerRemoteAddr_Object = MibTableColumn
fsbgp4PeerExtPeerRemoteAddr = _Fsbgp4PeerExtPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 2, 1, 1),
    _Fsbgp4PeerExtPeerRemoteAddr_Type()
)
fsbgp4PeerExtPeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4PeerExtPeerRemoteAddr.setStatus("deprecated")


class _Fsbgp4PeerExtConfigurePeer_Type(Integer32):
    """Custom type fsbgp4PeerExtConfigurePeer based on Integer32"""
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


_Fsbgp4PeerExtConfigurePeer_Type.__name__ = "Integer32"
_Fsbgp4PeerExtConfigurePeer_Object = MibTableColumn
fsbgp4PeerExtConfigurePeer = _Fsbgp4PeerExtConfigurePeer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 2, 1, 2),
    _Fsbgp4PeerExtConfigurePeer_Type()
)
fsbgp4PeerExtConfigurePeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4PeerExtConfigurePeer.setStatus("deprecated")


class _Fsbgp4PeerExtPeerRemoteAs_Type(Unsigned32):
    """Custom type fsbgp4PeerExtPeerRemoteAs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Fsbgp4PeerExtPeerRemoteAs_Type.__name__ = "Unsigned32"
_Fsbgp4PeerExtPeerRemoteAs_Object = MibTableColumn
fsbgp4PeerExtPeerRemoteAs = _Fsbgp4PeerExtPeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 2, 1, 3),
    _Fsbgp4PeerExtPeerRemoteAs_Type()
)
fsbgp4PeerExtPeerRemoteAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4PeerExtPeerRemoteAs.setStatus("deprecated")


class _Fsbgp4PeerExtEBGPMultiHop_Type(Integer32):
    """Custom type fsbgp4PeerExtEBGPMultiHop based on Integer32"""
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


_Fsbgp4PeerExtEBGPMultiHop_Type.__name__ = "Integer32"
_Fsbgp4PeerExtEBGPMultiHop_Object = MibTableColumn
fsbgp4PeerExtEBGPMultiHop = _Fsbgp4PeerExtEBGPMultiHop_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 2, 1, 4),
    _Fsbgp4PeerExtEBGPMultiHop_Type()
)
fsbgp4PeerExtEBGPMultiHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4PeerExtEBGPMultiHop.setStatus("deprecated")


class _Fsbgp4PeerExtNextHopSelf_Type(Integer32):
    """Custom type fsbgp4PeerExtNextHopSelf based on Integer32"""
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


_Fsbgp4PeerExtNextHopSelf_Type.__name__ = "Integer32"
_Fsbgp4PeerExtNextHopSelf_Object = MibTableColumn
fsbgp4PeerExtNextHopSelf = _Fsbgp4PeerExtNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 2, 1, 5),
    _Fsbgp4PeerExtNextHopSelf_Type()
)
fsbgp4PeerExtNextHopSelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4PeerExtNextHopSelf.setStatus("deprecated")


class _Fsbgp4PeerExtConnSrcIfId_Type(Integer32):
    """Custom type fsbgp4PeerExtConnSrcIfId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsbgp4PeerExtConnSrcIfId_Type.__name__ = "Integer32"
_Fsbgp4PeerExtConnSrcIfId_Object = MibTableColumn
fsbgp4PeerExtConnSrcIfId = _Fsbgp4PeerExtConnSrcIfId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 2, 1, 6),
    _Fsbgp4PeerExtConnSrcIfId_Type()
)
fsbgp4PeerExtConnSrcIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4PeerExtConnSrcIfId.setStatus("deprecated")


class _Fsbgp4PeerExtRflClient_Type(Integer32):
    """Custom type fsbgp4PeerExtRflClient based on Integer32"""
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


_Fsbgp4PeerExtRflClient_Type.__name__ = "Integer32"
_Fsbgp4PeerExtRflClient_Object = MibTableColumn
fsbgp4PeerExtRflClient = _Fsbgp4PeerExtRflClient_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 2, 1, 7),
    _Fsbgp4PeerExtRflClient_Type()
)
fsbgp4PeerExtRflClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4PeerExtRflClient.setStatus("deprecated")
_Fsbgp4MEDTable_Object = MibTable
fsbgp4MEDTable = _Fsbgp4MEDTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 3)
)
if mibBuilder.loadTexts:
    fsbgp4MEDTable.setStatus("deprecated")
_Fsbgp4MEDEntry_Object = MibTableRow
fsbgp4MEDEntry = _Fsbgp4MEDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 3, 1)
)
fsbgp4MEDEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4MEDIndex"),
)
if mibBuilder.loadTexts:
    fsbgp4MEDEntry.setStatus("deprecated")


class _Fsbgp4MEDIndex_Type(Integer32):
    """Custom type fsbgp4MEDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Fsbgp4MEDIndex_Type.__name__ = "Integer32"
_Fsbgp4MEDIndex_Object = MibTableColumn
fsbgp4MEDIndex = _Fsbgp4MEDIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 3, 1, 1),
    _Fsbgp4MEDIndex_Type()
)
fsbgp4MEDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4MEDIndex.setStatus("deprecated")


class _Fsbgp4MEDAdminStatus_Type(Integer32):
    """Custom type fsbgp4MEDAdminStatus based on Integer32"""
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


_Fsbgp4MEDAdminStatus_Type.__name__ = "Integer32"
_Fsbgp4MEDAdminStatus_Object = MibTableColumn
fsbgp4MEDAdminStatus = _Fsbgp4MEDAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 3, 1, 2),
    _Fsbgp4MEDAdminStatus_Type()
)
fsbgp4MEDAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4MEDAdminStatus.setStatus("deprecated")


class _Fsbgp4MEDRemoteAS_Type(Unsigned32):
    """Custom type fsbgp4MEDRemoteAS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Fsbgp4MEDRemoteAS_Type.__name__ = "Unsigned32"
_Fsbgp4MEDRemoteAS_Object = MibTableColumn
fsbgp4MEDRemoteAS = _Fsbgp4MEDRemoteAS_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 3, 1, 3),
    _Fsbgp4MEDRemoteAS_Type()
)
fsbgp4MEDRemoteAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4MEDRemoteAS.setStatus("deprecated")


class _Fsbgp4MEDIPAddrPrefix_Type(IpAddress):
    """Custom type fsbgp4MEDIPAddrPrefix based on IpAddress"""
    defaultHexValue = "00000000"


_Fsbgp4MEDIPAddrPrefix_Type.__name__ = "IpAddress"
_Fsbgp4MEDIPAddrPrefix_Object = MibTableColumn
fsbgp4MEDIPAddrPrefix = _Fsbgp4MEDIPAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 3, 1, 4),
    _Fsbgp4MEDIPAddrPrefix_Type()
)
fsbgp4MEDIPAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4MEDIPAddrPrefix.setStatus("deprecated")


class _Fsbgp4MEDIPAddrPrefixLen_Type(Integer32):
    """Custom type fsbgp4MEDIPAddrPrefixLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Fsbgp4MEDIPAddrPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4MEDIPAddrPrefixLen_Object = MibTableColumn
fsbgp4MEDIPAddrPrefixLen = _Fsbgp4MEDIPAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 3, 1, 5),
    _Fsbgp4MEDIPAddrPrefixLen_Type()
)
fsbgp4MEDIPAddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4MEDIPAddrPrefixLen.setStatus("deprecated")
_Fsbgp4MEDIntermediateAS_Type = DisplayString
_Fsbgp4MEDIntermediateAS_Object = MibTableColumn
fsbgp4MEDIntermediateAS = _Fsbgp4MEDIntermediateAS_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 3, 1, 6),
    _Fsbgp4MEDIntermediateAS_Type()
)
fsbgp4MEDIntermediateAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4MEDIntermediateAS.setStatus("deprecated")


class _Fsbgp4MEDDirection_Type(Integer32):
    """Custom type fsbgp4MEDDirection based on Integer32"""
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


_Fsbgp4MEDDirection_Type.__name__ = "Integer32"
_Fsbgp4MEDDirection_Object = MibTableColumn
fsbgp4MEDDirection = _Fsbgp4MEDDirection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 3, 1, 7),
    _Fsbgp4MEDDirection_Type()
)
fsbgp4MEDDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4MEDDirection.setStatus("deprecated")


class _Fsbgp4MEDValue_Type(Unsigned32):
    """Custom type fsbgp4MEDValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Fsbgp4MEDValue_Type.__name__ = "Unsigned32"
_Fsbgp4MEDValue_Object = MibTableColumn
fsbgp4MEDValue = _Fsbgp4MEDValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 3, 1, 8),
    _Fsbgp4MEDValue_Type()
)
fsbgp4MEDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4MEDValue.setStatus("deprecated")


class _Fsbgp4MEDPreference_Type(Integer32):
    """Custom type fsbgp4MEDPreference based on Integer32"""
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


_Fsbgp4MEDPreference_Type.__name__ = "Integer32"
_Fsbgp4MEDPreference_Object = MibTableColumn
fsbgp4MEDPreference = _Fsbgp4MEDPreference_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 3, 1, 9),
    _Fsbgp4MEDPreference_Type()
)
fsbgp4MEDPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4MEDPreference.setStatus("deprecated")
_Fsbgp4LocalPrefTable_Object = MibTable
fsbgp4LocalPrefTable = _Fsbgp4LocalPrefTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 4)
)
if mibBuilder.loadTexts:
    fsbgp4LocalPrefTable.setStatus("deprecated")
_Fsbgp4LocalPrefEntry_Object = MibTableRow
fsbgp4LocalPrefEntry = _Fsbgp4LocalPrefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 4, 1)
)
fsbgp4LocalPrefEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4LocalPrefIndex"),
)
if mibBuilder.loadTexts:
    fsbgp4LocalPrefEntry.setStatus("deprecated")


class _Fsbgp4LocalPrefIndex_Type(Integer32):
    """Custom type fsbgp4LocalPrefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Fsbgp4LocalPrefIndex_Type.__name__ = "Integer32"
_Fsbgp4LocalPrefIndex_Object = MibTableColumn
fsbgp4LocalPrefIndex = _Fsbgp4LocalPrefIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 4, 1, 1),
    _Fsbgp4LocalPrefIndex_Type()
)
fsbgp4LocalPrefIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4LocalPrefIndex.setStatus("deprecated")


class _Fsbgp4LocalPrefAdminStatus_Type(Integer32):
    """Custom type fsbgp4LocalPrefAdminStatus based on Integer32"""
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


_Fsbgp4LocalPrefAdminStatus_Type.__name__ = "Integer32"
_Fsbgp4LocalPrefAdminStatus_Object = MibTableColumn
fsbgp4LocalPrefAdminStatus = _Fsbgp4LocalPrefAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 4, 1, 2),
    _Fsbgp4LocalPrefAdminStatus_Type()
)
fsbgp4LocalPrefAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4LocalPrefAdminStatus.setStatus("deprecated")


class _Fsbgp4LocalPrefRemoteAS_Type(Unsigned32):
    """Custom type fsbgp4LocalPrefRemoteAS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Fsbgp4LocalPrefRemoteAS_Type.__name__ = "Unsigned32"
_Fsbgp4LocalPrefRemoteAS_Object = MibTableColumn
fsbgp4LocalPrefRemoteAS = _Fsbgp4LocalPrefRemoteAS_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 4, 1, 3),
    _Fsbgp4LocalPrefRemoteAS_Type()
)
fsbgp4LocalPrefRemoteAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4LocalPrefRemoteAS.setStatus("deprecated")


class _Fsbgp4LocalPrefIPAddrPrefix_Type(IpAddress):
    """Custom type fsbgp4LocalPrefIPAddrPrefix based on IpAddress"""
    defaultHexValue = "00000000"


_Fsbgp4LocalPrefIPAddrPrefix_Type.__name__ = "IpAddress"
_Fsbgp4LocalPrefIPAddrPrefix_Object = MibTableColumn
fsbgp4LocalPrefIPAddrPrefix = _Fsbgp4LocalPrefIPAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 4, 1, 4),
    _Fsbgp4LocalPrefIPAddrPrefix_Type()
)
fsbgp4LocalPrefIPAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4LocalPrefIPAddrPrefix.setStatus("deprecated")


class _Fsbgp4LocalPrefIPAddrPrefixLen_Type(Integer32):
    """Custom type fsbgp4LocalPrefIPAddrPrefixLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Fsbgp4LocalPrefIPAddrPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4LocalPrefIPAddrPrefixLen_Object = MibTableColumn
fsbgp4LocalPrefIPAddrPrefixLen = _Fsbgp4LocalPrefIPAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 4, 1, 5),
    _Fsbgp4LocalPrefIPAddrPrefixLen_Type()
)
fsbgp4LocalPrefIPAddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4LocalPrefIPAddrPrefixLen.setStatus("deprecated")
_Fsbgp4LocalPrefIntermediateAS_Type = DisplayString
_Fsbgp4LocalPrefIntermediateAS_Object = MibTableColumn
fsbgp4LocalPrefIntermediateAS = _Fsbgp4LocalPrefIntermediateAS_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 4, 1, 6),
    _Fsbgp4LocalPrefIntermediateAS_Type()
)
fsbgp4LocalPrefIntermediateAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4LocalPrefIntermediateAS.setStatus("deprecated")


class _Fsbgp4LocalPrefDirection_Type(Integer32):
    """Custom type fsbgp4LocalPrefDirection based on Integer32"""
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


_Fsbgp4LocalPrefDirection_Type.__name__ = "Integer32"
_Fsbgp4LocalPrefDirection_Object = MibTableColumn
fsbgp4LocalPrefDirection = _Fsbgp4LocalPrefDirection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 4, 1, 7),
    _Fsbgp4LocalPrefDirection_Type()
)
fsbgp4LocalPrefDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4LocalPrefDirection.setStatus("deprecated")


class _Fsbgp4LocalPrefValue_Type(Unsigned32):
    """Custom type fsbgp4LocalPrefValue based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Fsbgp4LocalPrefValue_Type.__name__ = "Unsigned32"
_Fsbgp4LocalPrefValue_Object = MibTableColumn
fsbgp4LocalPrefValue = _Fsbgp4LocalPrefValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 4, 1, 8),
    _Fsbgp4LocalPrefValue_Type()
)
fsbgp4LocalPrefValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4LocalPrefValue.setStatus("deprecated")


class _Fsbgp4LocalPrefPreference_Type(Integer32):
    """Custom type fsbgp4LocalPrefPreference based on Integer32"""
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


_Fsbgp4LocalPrefPreference_Type.__name__ = "Integer32"
_Fsbgp4LocalPrefPreference_Object = MibTableColumn
fsbgp4LocalPrefPreference = _Fsbgp4LocalPrefPreference_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 4, 1, 9),
    _Fsbgp4LocalPrefPreference_Type()
)
fsbgp4LocalPrefPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4LocalPrefPreference.setStatus("deprecated")
_Fsbgp4UpdateFilterTable_Object = MibTable
fsbgp4UpdateFilterTable = _Fsbgp4UpdateFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 5)
)
if mibBuilder.loadTexts:
    fsbgp4UpdateFilterTable.setStatus("deprecated")
_Fsbgp4UpdateFilterEntry_Object = MibTableRow
fsbgp4UpdateFilterEntry = _Fsbgp4UpdateFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 5, 1)
)
fsbgp4UpdateFilterEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4UpdateFilterIndex"),
)
if mibBuilder.loadTexts:
    fsbgp4UpdateFilterEntry.setStatus("deprecated")


class _Fsbgp4UpdateFilterIndex_Type(Integer32):
    """Custom type fsbgp4UpdateFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Fsbgp4UpdateFilterIndex_Type.__name__ = "Integer32"
_Fsbgp4UpdateFilterIndex_Object = MibTableColumn
fsbgp4UpdateFilterIndex = _Fsbgp4UpdateFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 5, 1, 1),
    _Fsbgp4UpdateFilterIndex_Type()
)
fsbgp4UpdateFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4UpdateFilterIndex.setStatus("deprecated")


class _Fsbgp4UpdateFilterAdminStatus_Type(Integer32):
    """Custom type fsbgp4UpdateFilterAdminStatus based on Integer32"""
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


_Fsbgp4UpdateFilterAdminStatus_Type.__name__ = "Integer32"
_Fsbgp4UpdateFilterAdminStatus_Object = MibTableColumn
fsbgp4UpdateFilterAdminStatus = _Fsbgp4UpdateFilterAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 5, 1, 2),
    _Fsbgp4UpdateFilterAdminStatus_Type()
)
fsbgp4UpdateFilterAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4UpdateFilterAdminStatus.setStatus("deprecated")


class _Fsbgp4UpdateFilterRemoteAS_Type(Unsigned32):
    """Custom type fsbgp4UpdateFilterRemoteAS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Fsbgp4UpdateFilterRemoteAS_Type.__name__ = "Unsigned32"
_Fsbgp4UpdateFilterRemoteAS_Object = MibTableColumn
fsbgp4UpdateFilterRemoteAS = _Fsbgp4UpdateFilterRemoteAS_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 5, 1, 3),
    _Fsbgp4UpdateFilterRemoteAS_Type()
)
fsbgp4UpdateFilterRemoteAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4UpdateFilterRemoteAS.setStatus("deprecated")


class _Fsbgp4UpdateFilterIPAddrPrefix_Type(IpAddress):
    """Custom type fsbgp4UpdateFilterIPAddrPrefix based on IpAddress"""
    defaultHexValue = "00000000"


_Fsbgp4UpdateFilterIPAddrPrefix_Type.__name__ = "IpAddress"
_Fsbgp4UpdateFilterIPAddrPrefix_Object = MibTableColumn
fsbgp4UpdateFilterIPAddrPrefix = _Fsbgp4UpdateFilterIPAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 5, 1, 4),
    _Fsbgp4UpdateFilterIPAddrPrefix_Type()
)
fsbgp4UpdateFilterIPAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4UpdateFilterIPAddrPrefix.setStatus("deprecated")


class _Fsbgp4UpdateFilterIPAddrPrefixLen_Type(Integer32):
    """Custom type fsbgp4UpdateFilterIPAddrPrefixLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Fsbgp4UpdateFilterIPAddrPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4UpdateFilterIPAddrPrefixLen_Object = MibTableColumn
fsbgp4UpdateFilterIPAddrPrefixLen = _Fsbgp4UpdateFilterIPAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 5, 1, 5),
    _Fsbgp4UpdateFilterIPAddrPrefixLen_Type()
)
fsbgp4UpdateFilterIPAddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4UpdateFilterIPAddrPrefixLen.setStatus("deprecated")
_Fsbgp4UpdateFilterIntermediateAS_Type = DisplayString
_Fsbgp4UpdateFilterIntermediateAS_Object = MibTableColumn
fsbgp4UpdateFilterIntermediateAS = _Fsbgp4UpdateFilterIntermediateAS_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 5, 1, 6),
    _Fsbgp4UpdateFilterIntermediateAS_Type()
)
fsbgp4UpdateFilterIntermediateAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4UpdateFilterIntermediateAS.setStatus("deprecated")


class _Fsbgp4UpdateFilterDirection_Type(Integer32):
    """Custom type fsbgp4UpdateFilterDirection based on Integer32"""
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


_Fsbgp4UpdateFilterDirection_Type.__name__ = "Integer32"
_Fsbgp4UpdateFilterDirection_Object = MibTableColumn
fsbgp4UpdateFilterDirection = _Fsbgp4UpdateFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 5, 1, 7),
    _Fsbgp4UpdateFilterDirection_Type()
)
fsbgp4UpdateFilterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4UpdateFilterDirection.setStatus("deprecated")


class _Fsbgp4UpdateFilterAction_Type(Integer32):
    """Custom type fsbgp4UpdateFilterAction based on Integer32"""
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


_Fsbgp4UpdateFilterAction_Type.__name__ = "Integer32"
_Fsbgp4UpdateFilterAction_Object = MibTableColumn
fsbgp4UpdateFilterAction = _Fsbgp4UpdateFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 5, 1, 8),
    _Fsbgp4UpdateFilterAction_Type()
)
fsbgp4UpdateFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4UpdateFilterAction.setStatus("deprecated")
_Fsbgp4AggregateTable_Object = MibTable
fsbgp4AggregateTable = _Fsbgp4AggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 6)
)
if mibBuilder.loadTexts:
    fsbgp4AggregateTable.setStatus("deprecated")
_Fsbgp4AggregateEntry_Object = MibTableRow
fsbgp4AggregateEntry = _Fsbgp4AggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 6, 1)
)
fsbgp4AggregateEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4AggregateIndex"),
)
if mibBuilder.loadTexts:
    fsbgp4AggregateEntry.setStatus("deprecated")


class _Fsbgp4AggregateIndex_Type(Integer32):
    """Custom type fsbgp4AggregateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Fsbgp4AggregateIndex_Type.__name__ = "Integer32"
_Fsbgp4AggregateIndex_Object = MibTableColumn
fsbgp4AggregateIndex = _Fsbgp4AggregateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 6, 1, 1),
    _Fsbgp4AggregateIndex_Type()
)
fsbgp4AggregateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4AggregateIndex.setStatus("deprecated")


class _Fsbgp4AggregateAdminStatus_Type(Integer32):
    """Custom type fsbgp4AggregateAdminStatus based on Integer32"""
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


_Fsbgp4AggregateAdminStatus_Type.__name__ = "Integer32"
_Fsbgp4AggregateAdminStatus_Object = MibTableColumn
fsbgp4AggregateAdminStatus = _Fsbgp4AggregateAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 6, 1, 2),
    _Fsbgp4AggregateAdminStatus_Type()
)
fsbgp4AggregateAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4AggregateAdminStatus.setStatus("deprecated")
_Fsbgp4AggregateIPAddrPrefix_Type = IpAddress
_Fsbgp4AggregateIPAddrPrefix_Object = MibTableColumn
fsbgp4AggregateIPAddrPrefix = _Fsbgp4AggregateIPAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 6, 1, 3),
    _Fsbgp4AggregateIPAddrPrefix_Type()
)
fsbgp4AggregateIPAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4AggregateIPAddrPrefix.setStatus("deprecated")


class _Fsbgp4AggregateIPAddrPrefixLen_Type(Integer32):
    """Custom type fsbgp4AggregateIPAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Fsbgp4AggregateIPAddrPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4AggregateIPAddrPrefixLen_Object = MibTableColumn
fsbgp4AggregateIPAddrPrefixLen = _Fsbgp4AggregateIPAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 6, 1, 4),
    _Fsbgp4AggregateIPAddrPrefixLen_Type()
)
fsbgp4AggregateIPAddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4AggregateIPAddrPrefixLen.setStatus("deprecated")


class _Fsbgp4AggregateAdvertise_Type(Integer32):
    """Custom type fsbgp4AggregateAdvertise based on Integer32"""
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


_Fsbgp4AggregateAdvertise_Type.__name__ = "Integer32"
_Fsbgp4AggregateAdvertise_Object = MibTableColumn
fsbgp4AggregateAdvertise = _Fsbgp4AggregateAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 6, 1, 5),
    _Fsbgp4AggregateAdvertise_Type()
)
fsbgp4AggregateAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4AggregateAdvertise.setStatus("deprecated")
_Fsbgp4RRDGroup_ObjectIdentity = ObjectIdentity
fsbgp4RRDGroup = _Fsbgp4RRDGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 7)
)


class _Fsbgp4RRDAdminStatus_Type(Integer32):
    """Custom type fsbgp4RRDAdminStatus based on Integer32"""
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


_Fsbgp4RRDAdminStatus_Type.__name__ = "Integer32"
_Fsbgp4RRDAdminStatus_Object = MibScalar
fsbgp4RRDAdminStatus = _Fsbgp4RRDAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 7, 1),
    _Fsbgp4RRDAdminStatus_Type()
)
fsbgp4RRDAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RRDAdminStatus.setStatus("current")
_Fsbgp4RRDProtoMaskForEnable_Type = Integer32
_Fsbgp4RRDProtoMaskForEnable_Object = MibScalar
fsbgp4RRDProtoMaskForEnable = _Fsbgp4RRDProtoMaskForEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 7, 2),
    _Fsbgp4RRDProtoMaskForEnable_Type()
)
fsbgp4RRDProtoMaskForEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RRDProtoMaskForEnable.setStatus("current")
_Fsbgp4RRDSrcProtoMaskForDisable_Type = Integer32
_Fsbgp4RRDSrcProtoMaskForDisable_Object = MibScalar
fsbgp4RRDSrcProtoMaskForDisable = _Fsbgp4RRDSrcProtoMaskForDisable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 7, 3),
    _Fsbgp4RRDSrcProtoMaskForDisable_Type()
)
fsbgp4RRDSrcProtoMaskForDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RRDSrcProtoMaskForDisable.setStatus("current")


class _Fsbgp4RRDDefaultMetric_Type(Unsigned32):
    """Custom type fsbgp4RRDDefaultMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Fsbgp4RRDDefaultMetric_Type.__name__ = "Unsigned32"
_Fsbgp4RRDDefaultMetric_Object = MibScalar
fsbgp4RRDDefaultMetric = _Fsbgp4RRDDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 7, 4),
    _Fsbgp4RRDDefaultMetric_Type()
)
fsbgp4RRDDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RRDDefaultMetric.setStatus("current")


class _Fsbgp4RRDRouteMapName_Type(DisplayString):
    """Custom type fsbgp4RRDRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Fsbgp4RRDRouteMapName_Type.__name__ = "DisplayString"
_Fsbgp4RRDRouteMapName_Object = MibScalar
fsbgp4RRDRouteMapName = _Fsbgp4RRDRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 7, 5),
    _Fsbgp4RRDRouteMapName_Type()
)
fsbgp4RRDRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RRDRouteMapName.setStatus("current")


class _Fsbgp4RRDMatchTypeEnable_Type(Integer32):
    """Custom type fsbgp4RRDMatchTypeEnable based on Integer32"""
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
          ("nssa-external", 4))
    )


_Fsbgp4RRDMatchTypeEnable_Type.__name__ = "Integer32"
_Fsbgp4RRDMatchTypeEnable_Object = MibScalar
fsbgp4RRDMatchTypeEnable = _Fsbgp4RRDMatchTypeEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 7, 6),
    _Fsbgp4RRDMatchTypeEnable_Type()
)
fsbgp4RRDMatchTypeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RRDMatchTypeEnable.setStatus("current")


class _Fsbgp4RRDMatchTypeDisable_Type(Integer32):
    """Custom type fsbgp4RRDMatchTypeDisable based on Integer32"""
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
          ("nssa-external", 4))
    )


_Fsbgp4RRDMatchTypeDisable_Type.__name__ = "Integer32"
_Fsbgp4RRDMatchTypeDisable_Object = MibScalar
fsbgp4RRDMatchTypeDisable = _Fsbgp4RRDMatchTypeDisable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 7, 7),
    _Fsbgp4RRDMatchTypeDisable_Type()
)
fsbgp4RRDMatchTypeDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RRDMatchTypeDisable.setStatus("current")
_Fsbgp4RRDMetricTable_Object = MibTable
fsbgp4RRDMetricTable = _Fsbgp4RRDMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 7, 8)
)
if mibBuilder.loadTexts:
    fsbgp4RRDMetricTable.setStatus("current")
_Fsbgp4RRDMetricEntry_Object = MibTableRow
fsbgp4RRDMetricEntry = _Fsbgp4RRDMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 7, 8, 1)
)
fsbgp4RRDMetricEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsBgp4RRDMetricProtocolId"),
)
if mibBuilder.loadTexts:
    fsbgp4RRDMetricEntry.setStatus("current")


class _FsBgp4RRDMetricProtocolId_Type(Integer32):
    """Custom type fsBgp4RRDMetricProtocolId based on Integer32"""
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


_FsBgp4RRDMetricProtocolId_Type.__name__ = "Integer32"
_FsBgp4RRDMetricProtocolId_Object = MibTableColumn
fsBgp4RRDMetricProtocolId = _FsBgp4RRDMetricProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 7, 8, 1, 1),
    _FsBgp4RRDMetricProtocolId_Type()
)
fsBgp4RRDMetricProtocolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4RRDMetricProtocolId.setStatus("current")
_FsBgp4RRDMetricValue_Type = Integer32
_FsBgp4RRDMetricValue_Object = MibTableColumn
fsBgp4RRDMetricValue = _FsBgp4RRDMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 7, 8, 1, 2),
    _FsBgp4RRDMetricValue_Type()
)
fsBgp4RRDMetricValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4RRDMetricValue.setStatus("current")
_Fsbgp4ImportRouteTable_Object = MibTable
fsbgp4ImportRouteTable = _Fsbgp4ImportRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 8)
)
if mibBuilder.loadTexts:
    fsbgp4ImportRouteTable.setStatus("deprecated")
_Fsbgp4ImportRouteEntry_Object = MibTableRow
fsbgp4ImportRouteEntry = _Fsbgp4ImportRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 8, 1)
)
fsbgp4ImportRouteEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4ImportRoutePrefix"),
    (0, "ARICENT-BGP-MIB", "fsbgp4ImportRoutePrefixLen"),
    (0, "ARICENT-BGP-MIB", "fsbgp4ImportRouteProtocol"),
    (0, "ARICENT-BGP-MIB", "fsbgp4ImportRouteNextHop"),
    (0, "ARICENT-BGP-MIB", "fsbgp4ImportRouteIfIndex"),
    (0, "ARICENT-BGP-MIB", "fsbgp4ImportRouteMetric"),
)
if mibBuilder.loadTexts:
    fsbgp4ImportRouteEntry.setStatus("deprecated")
_Fsbgp4ImportRoutePrefix_Type = IpAddress
_Fsbgp4ImportRoutePrefix_Object = MibTableColumn
fsbgp4ImportRoutePrefix = _Fsbgp4ImportRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 8, 1, 1),
    _Fsbgp4ImportRoutePrefix_Type()
)
fsbgp4ImportRoutePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4ImportRoutePrefix.setStatus("deprecated")


class _Fsbgp4ImportRoutePrefixLen_Type(Integer32):
    """Custom type fsbgp4ImportRoutePrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fsbgp4ImportRoutePrefixLen_Type.__name__ = "Integer32"
_Fsbgp4ImportRoutePrefixLen_Object = MibTableColumn
fsbgp4ImportRoutePrefixLen = _Fsbgp4ImportRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 8, 1, 2),
    _Fsbgp4ImportRoutePrefixLen_Type()
)
fsbgp4ImportRoutePrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4ImportRoutePrefixLen.setStatus("deprecated")


class _Fsbgp4ImportRouteProtocol_Type(Integer32):
    """Custom type fsbgp4ImportRouteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(13, 13),
    )


_Fsbgp4ImportRouteProtocol_Type.__name__ = "Integer32"
_Fsbgp4ImportRouteProtocol_Object = MibTableColumn
fsbgp4ImportRouteProtocol = _Fsbgp4ImportRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 8, 1, 3),
    _Fsbgp4ImportRouteProtocol_Type()
)
fsbgp4ImportRouteProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4ImportRouteProtocol.setStatus("deprecated")
_Fsbgp4ImportRouteNextHop_Type = IpAddress
_Fsbgp4ImportRouteNextHop_Object = MibTableColumn
fsbgp4ImportRouteNextHop = _Fsbgp4ImportRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 8, 1, 4),
    _Fsbgp4ImportRouteNextHop_Type()
)
fsbgp4ImportRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4ImportRouteNextHop.setStatus("deprecated")


class _Fsbgp4ImportRouteIfIndex_Type(Integer32):
    """Custom type fsbgp4ImportRouteIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsbgp4ImportRouteIfIndex_Type.__name__ = "Integer32"
_Fsbgp4ImportRouteIfIndex_Object = MibTableColumn
fsbgp4ImportRouteIfIndex = _Fsbgp4ImportRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 8, 1, 5),
    _Fsbgp4ImportRouteIfIndex_Type()
)
fsbgp4ImportRouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4ImportRouteIfIndex.setStatus("deprecated")


class _Fsbgp4ImportRouteMetric_Type(Integer32):
    """Custom type fsbgp4ImportRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsbgp4ImportRouteMetric_Type.__name__ = "Integer32"
_Fsbgp4ImportRouteMetric_Object = MibTableColumn
fsbgp4ImportRouteMetric = _Fsbgp4ImportRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 8, 1, 6),
    _Fsbgp4ImportRouteMetric_Type()
)
fsbgp4ImportRouteMetric.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4ImportRouteMetric.setStatus("deprecated")


class _Fsbgp4ImportRouteAction_Type(Integer32):
    """Custom type fsbgp4ImportRouteAction based on Integer32"""
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


_Fsbgp4ImportRouteAction_Type.__name__ = "Integer32"
_Fsbgp4ImportRouteAction_Object = MibTableColumn
fsbgp4ImportRouteAction = _Fsbgp4ImportRouteAction_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 8, 1, 7),
    _Fsbgp4ImportRouteAction_Type()
)
fsbgp4ImportRouteAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4ImportRouteAction.setStatus("deprecated")
_Fsbgp4FsmTransitionHistTable_Object = MibTable
fsbgp4FsmTransitionHistTable = _Fsbgp4FsmTransitionHistTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 9)
)
if mibBuilder.loadTexts:
    fsbgp4FsmTransitionHistTable.setStatus("deprecated")
_Fsbgp4FsmTransitionHistEntry_Object = MibTableRow
fsbgp4FsmTransitionHistEntry = _Fsbgp4FsmTransitionHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 9, 1)
)
fsbgp4FsmTransitionHistEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4Peer"),
)
if mibBuilder.loadTexts:
    fsbgp4FsmTransitionHistEntry.setStatus("deprecated")
_Fsbgp4Peer_Type = IpAddress
_Fsbgp4Peer_Object = MibTableColumn
fsbgp4Peer = _Fsbgp4Peer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 9, 1, 1),
    _Fsbgp4Peer_Type()
)
fsbgp4Peer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4Peer.setStatus("deprecated")
_Fsbgp4FsmTransitionHist_Type = DisplayString
_Fsbgp4FsmTransitionHist_Object = MibTableColumn
fsbgp4FsmTransitionHist = _Fsbgp4FsmTransitionHist_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 9, 1, 2),
    _Fsbgp4FsmTransitionHist_Type()
)
fsbgp4FsmTransitionHist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4FsmTransitionHist.setStatus("deprecated")
_FsbgpRfl_ObjectIdentity = ObjectIdentity
fsbgpRfl = _FsbgpRfl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 10)
)
_Fsbgp4RflScalars_ObjectIdentity = ObjectIdentity
fsbgp4RflScalars = _Fsbgp4RflScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 10, 1)
)


class _Fsbgp4RflbgpClusterId_Type(OctetString):
    """Custom type fsbgp4RflbgpClusterId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Fsbgp4RflbgpClusterId_Type.__name__ = "OctetString"
_Fsbgp4RflbgpClusterId_Object = MibScalar
fsbgp4RflbgpClusterId = _Fsbgp4RflbgpClusterId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 10, 1, 1),
    _Fsbgp4RflbgpClusterId_Type()
)
fsbgp4RflbgpClusterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RflbgpClusterId.setStatus("current")


class _Fsbgp4RflRflSupport_Type(Integer32):
    """Custom type fsbgp4RflRflSupport based on Integer32"""
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


_Fsbgp4RflRflSupport_Type.__name__ = "Integer32"
_Fsbgp4RflRflSupport_Object = MibScalar
fsbgp4RflRflSupport = _Fsbgp4RflRflSupport_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 10, 1, 2),
    _Fsbgp4RflRflSupport_Type()
)
fsbgp4RflRflSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RflRflSupport.setStatus("current")
_Fsbgp4RflRouteReflectorTable_Object = MibTable
fsbgp4RflRouteReflectorTable = _Fsbgp4RflRouteReflectorTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 10, 2)
)
if mibBuilder.loadTexts:
    fsbgp4RflRouteReflectorTable.setStatus("deprecated")
_Fsbgp4RflRouteReflectorEntry_Object = MibTableRow
fsbgp4RflRouteReflectorEntry = _Fsbgp4RflRouteReflectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 10, 2, 1)
)
fsbgp4RflRouteReflectorEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4RflPathAttrAddrPrefix"),
    (0, "ARICENT-BGP-MIB", "fsbgp4RflPathAttrAddrPrefixLen"),
    (0, "ARICENT-BGP-MIB", "fsbgp4RflPathAttrPeer"),
)
if mibBuilder.loadTexts:
    fsbgp4RflRouteReflectorEntry.setStatus("deprecated")
_Fsbgp4RflPathAttrAddrPrefix_Type = IpAddress
_Fsbgp4RflPathAttrAddrPrefix_Object = MibTableColumn
fsbgp4RflPathAttrAddrPrefix = _Fsbgp4RflPathAttrAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 10, 2, 1, 1),
    _Fsbgp4RflPathAttrAddrPrefix_Type()
)
fsbgp4RflPathAttrAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4RflPathAttrAddrPrefix.setStatus("deprecated")


class _Fsbgp4RflPathAttrAddrPrefixLen_Type(Integer32):
    """Custom type fsbgp4RflPathAttrAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Fsbgp4RflPathAttrAddrPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4RflPathAttrAddrPrefixLen_Object = MibTableColumn
fsbgp4RflPathAttrAddrPrefixLen = _Fsbgp4RflPathAttrAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 10, 2, 1, 2),
    _Fsbgp4RflPathAttrAddrPrefixLen_Type()
)
fsbgp4RflPathAttrAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4RflPathAttrAddrPrefixLen.setStatus("deprecated")
_Fsbgp4RflPathAttrPeer_Type = IpAddress
_Fsbgp4RflPathAttrPeer_Object = MibTableColumn
fsbgp4RflPathAttrPeer = _Fsbgp4RflPathAttrPeer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 10, 2, 1, 3),
    _Fsbgp4RflPathAttrPeer_Type()
)
fsbgp4RflPathAttrPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4RflPathAttrPeer.setStatus("deprecated")


class _Fsbgp4RflPathAttrOriginatorId_Type(OctetString):
    """Custom type fsbgp4RflPathAttrOriginatorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Fsbgp4RflPathAttrOriginatorId_Type.__name__ = "OctetString"
_Fsbgp4RflPathAttrOriginatorId_Object = MibTableColumn
fsbgp4RflPathAttrOriginatorId = _Fsbgp4RflPathAttrOriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 10, 2, 1, 4),
    _Fsbgp4RflPathAttrOriginatorId_Type()
)
fsbgp4RflPathAttrOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RflPathAttrOriginatorId.setStatus("deprecated")


class _Fsbgp4RflPathAttrClusterList_Type(OctetString):
    """Custom type fsbgp4RflPathAttrClusterList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_Fsbgp4RflPathAttrClusterList_Type.__name__ = "OctetString"
_Fsbgp4RflPathAttrClusterList_Object = MibTableColumn
fsbgp4RflPathAttrClusterList = _Fsbgp4RflPathAttrClusterList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 10, 2, 1, 5),
    _Fsbgp4RflPathAttrClusterList_Type()
)
fsbgp4RflPathAttrClusterList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RflPathAttrClusterList.setStatus("deprecated")
_Fsbgp4Rfd_ObjectIdentity = ObjectIdentity
fsbgp4Rfd = _Fsbgp4Rfd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11)
)
_Fsbgp4RfdScalars_ObjectIdentity = ObjectIdentity
fsbgp4RfdScalars = _Fsbgp4RfdScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 1)
)


class _Fsbgp4RfdCutOff_Type(Integer32):
    """Custom type fsbgp4RfdCutOff based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 3999),
    )


_Fsbgp4RfdCutOff_Type.__name__ = "Integer32"
_Fsbgp4RfdCutOff_Object = MibScalar
fsbgp4RfdCutOff = _Fsbgp4RfdCutOff_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 1, 1),
    _Fsbgp4RfdCutOff_Type()
)
fsbgp4RfdCutOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RfdCutOff.setStatus("current")


class _Fsbgp4RfdReuse_Type(Integer32):
    """Custom type fsbgp4RfdReuse based on Integer32"""
    defaultValue = 750

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1999),
    )


_Fsbgp4RfdReuse_Type.__name__ = "Integer32"
_Fsbgp4RfdReuse_Object = MibScalar
fsbgp4RfdReuse = _Fsbgp4RfdReuse_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 1, 2),
    _Fsbgp4RfdReuse_Type()
)
fsbgp4RfdReuse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RfdReuse.setStatus("current")


class _Fsbgp4RfdCeiling_Type(Integer32):
    """Custom type fsbgp4RfdCeiling based on Integer32"""
    defaultValue = 8000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 10000),
    )


_Fsbgp4RfdCeiling_Type.__name__ = "Integer32"
_Fsbgp4RfdCeiling_Object = MibScalar
fsbgp4RfdCeiling = _Fsbgp4RfdCeiling_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 1, 3),
    _Fsbgp4RfdCeiling_Type()
)
fsbgp4RfdCeiling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RfdCeiling.setStatus("current")


class _Fsbgp4RfdMaxHoldDownTime_Type(Integer32):
    """Custom type fsbgp4RfdMaxHoldDownTime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 10800),
    )


_Fsbgp4RfdMaxHoldDownTime_Type.__name__ = "Integer32"
_Fsbgp4RfdMaxHoldDownTime_Object = MibScalar
fsbgp4RfdMaxHoldDownTime = _Fsbgp4RfdMaxHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 1, 4),
    _Fsbgp4RfdMaxHoldDownTime_Type()
)
fsbgp4RfdMaxHoldDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RfdMaxHoldDownTime.setStatus("current")


class _Fsbgp4RfdDecayHalfLifeTime_Type(Integer32):
    """Custom type fsbgp4RfdDecayHalfLifeTime based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 2700),
    )


_Fsbgp4RfdDecayHalfLifeTime_Type.__name__ = "Integer32"
_Fsbgp4RfdDecayHalfLifeTime_Object = MibScalar
fsbgp4RfdDecayHalfLifeTime = _Fsbgp4RfdDecayHalfLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 1, 5),
    _Fsbgp4RfdDecayHalfLifeTime_Type()
)
fsbgp4RfdDecayHalfLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RfdDecayHalfLifeTime.setStatus("current")


class _Fsbgp4RfdDecayTimerGranularity_Type(Integer32):
    """Custom type fsbgp4RfdDecayTimerGranularity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10800),
    )


_Fsbgp4RfdDecayTimerGranularity_Type.__name__ = "Integer32"
_Fsbgp4RfdDecayTimerGranularity_Object = MibScalar
fsbgp4RfdDecayTimerGranularity = _Fsbgp4RfdDecayTimerGranularity_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 1, 6),
    _Fsbgp4RfdDecayTimerGranularity_Type()
)
fsbgp4RfdDecayTimerGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RfdDecayTimerGranularity.setStatus("current")


class _Fsbgp4RfdReuseTimerGranularity_Type(Integer32):
    """Custom type fsbgp4RfdReuseTimerGranularity based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 10800),
    )


_Fsbgp4RfdReuseTimerGranularity_Type.__name__ = "Integer32"
_Fsbgp4RfdReuseTimerGranularity_Object = MibScalar
fsbgp4RfdReuseTimerGranularity = _Fsbgp4RfdReuseTimerGranularity_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 1, 7),
    _Fsbgp4RfdReuseTimerGranularity_Type()
)
fsbgp4RfdReuseTimerGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RfdReuseTimerGranularity.setStatus("current")


class _Fsbgp4RfdReuseIndxArraySize_Type(Integer32):
    """Custom type fsbgp4RfdReuseIndxArraySize based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 65535),
    )


_Fsbgp4RfdReuseIndxArraySize_Type.__name__ = "Integer32"
_Fsbgp4RfdReuseIndxArraySize_Object = MibScalar
fsbgp4RfdReuseIndxArraySize = _Fsbgp4RfdReuseIndxArraySize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 1, 8),
    _Fsbgp4RfdReuseIndxArraySize_Type()
)
fsbgp4RfdReuseIndxArraySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RfdReuseIndxArraySize.setStatus("current")


class _Fsbgp4RfdAdminStatus_Type(Integer32):
    """Custom type fsbgp4RfdAdminStatus based on Integer32"""
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


_Fsbgp4RfdAdminStatus_Type.__name__ = "Integer32"
_Fsbgp4RfdAdminStatus_Object = MibScalar
fsbgp4RfdAdminStatus = _Fsbgp4RfdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 1, 9),
    _Fsbgp4RfdAdminStatus_Type()
)
fsbgp4RfdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RfdAdminStatus.setStatus("current")
_Fsbgp4RfdRtDampHistTable_Object = MibTable
fsbgp4RfdRtDampHistTable = _Fsbgp4RfdRtDampHistTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 2)
)
if mibBuilder.loadTexts:
    fsbgp4RfdRtDampHistTable.setStatus("deprecated")
_Fsbgp4RfdRtDampHistEntry_Object = MibTableRow
fsbgp4RfdRtDampHistEntry = _Fsbgp4RfdRtDampHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 2, 1)
)
fsbgp4RfdRtDampHistEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4PathAttrAddrPrefix"),
    (0, "ARICENT-BGP-MIB", "fsbgp4PathAttrAddrPrefixLen"),
    (0, "ARICENT-BGP-MIB", "fsbgp4PathAttrPeer"),
    (0, "ARICENT-BGP-MIB", "fsbgp4RtDampHistInstance"),
)
if mibBuilder.loadTexts:
    fsbgp4RfdRtDampHistEntry.setStatus("deprecated")
_Fsbgp4PathAttrAddrPrefix_Type = IpAddress
_Fsbgp4PathAttrAddrPrefix_Object = MibTableColumn
fsbgp4PathAttrAddrPrefix = _Fsbgp4PathAttrAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 2, 1, 1),
    _Fsbgp4PathAttrAddrPrefix_Type()
)
fsbgp4PathAttrAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4PathAttrAddrPrefix.setStatus("deprecated")


class _Fsbgp4PathAttrAddrPrefixLen_Type(Integer32):
    """Custom type fsbgp4PathAttrAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Fsbgp4PathAttrAddrPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4PathAttrAddrPrefixLen_Object = MibTableColumn
fsbgp4PathAttrAddrPrefixLen = _Fsbgp4PathAttrAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 2, 1, 2),
    _Fsbgp4PathAttrAddrPrefixLen_Type()
)
fsbgp4PathAttrAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4PathAttrAddrPrefixLen.setStatus("deprecated")
_Fsbgp4PathAttrPeer_Type = IpAddress
_Fsbgp4PathAttrPeer_Object = MibTableColumn
fsbgp4PathAttrPeer = _Fsbgp4PathAttrPeer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 2, 1, 3),
    _Fsbgp4PathAttrPeer_Type()
)
fsbgp4PathAttrPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4PathAttrPeer.setStatus("deprecated")


class _Fsbgp4RtDampHistInstance_Type(Integer32):
    """Custom type fsbgp4RtDampHistInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Fsbgp4RtDampHistInstance_Type.__name__ = "Integer32"
_Fsbgp4RtDampHistInstance_Object = MibTableColumn
fsbgp4RtDampHistInstance = _Fsbgp4RtDampHistInstance_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 2, 1, 4),
    _Fsbgp4RtDampHistInstance_Type()
)
fsbgp4RtDampHistInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4RtDampHistInstance.setStatus("deprecated")


class _Fsbgp4RfdRtFom_Type(Integer32):
    """Custom type fsbgp4RfdRtFom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsbgp4RfdRtFom_Type.__name__ = "Integer32"
_Fsbgp4RfdRtFom_Object = MibTableColumn
fsbgp4RfdRtFom = _Fsbgp4RfdRtFom_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 2, 1, 5),
    _Fsbgp4RfdRtFom_Type()
)
fsbgp4RfdRtFom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RfdRtFom.setStatus("deprecated")


class _Fsbgp4RfdRtLastUpdtTime_Type(Integer32):
    """Custom type fsbgp4RfdRtLastUpdtTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsbgp4RfdRtLastUpdtTime_Type.__name__ = "Integer32"
_Fsbgp4RfdRtLastUpdtTime_Object = MibTableColumn
fsbgp4RfdRtLastUpdtTime = _Fsbgp4RfdRtLastUpdtTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 2, 1, 6),
    _Fsbgp4RfdRtLastUpdtTime_Type()
)
fsbgp4RfdRtLastUpdtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RfdRtLastUpdtTime.setStatus("deprecated")


class _Fsbgp4RfdRtState_Type(Integer32):
    """Custom type fsbgp4RfdRtState based on Integer32"""
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


_Fsbgp4RfdRtState_Type.__name__ = "Integer32"
_Fsbgp4RfdRtState_Object = MibTableColumn
fsbgp4RfdRtState = _Fsbgp4RfdRtState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 2, 1, 7),
    _Fsbgp4RfdRtState_Type()
)
fsbgp4RfdRtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RfdRtState.setStatus("deprecated")


class _Fsbgp4RfdRtStatus_Type(Integer32):
    """Custom type fsbgp4RfdRtStatus based on Integer32"""
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


_Fsbgp4RfdRtStatus_Type.__name__ = "Integer32"
_Fsbgp4RfdRtStatus_Object = MibTableColumn
fsbgp4RfdRtStatus = _Fsbgp4RfdRtStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 2, 1, 8),
    _Fsbgp4RfdRtStatus_Type()
)
fsbgp4RfdRtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RfdRtStatus.setStatus("deprecated")
_Fsbgp4RfdPeerDampHistTable_Object = MibTable
fsbgp4RfdPeerDampHistTable = _Fsbgp4RfdPeerDampHistTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 3)
)
if mibBuilder.loadTexts:
    fsbgp4RfdPeerDampHistTable.setStatus("deprecated")
_Fsbgp4RfdPeerDampHistEntry_Object = MibTableRow
fsbgp4RfdPeerDampHistEntry = _Fsbgp4RfdPeerDampHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 3, 1)
)
fsbgp4RfdPeerDampHistEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4PeerRemoteIpAddr"),
)
if mibBuilder.loadTexts:
    fsbgp4RfdPeerDampHistEntry.setStatus("deprecated")
_Fsbgp4PeerRemoteIpAddr_Type = IpAddress
_Fsbgp4PeerRemoteIpAddr_Object = MibTableColumn
fsbgp4PeerRemoteIpAddr = _Fsbgp4PeerRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 3, 1, 1),
    _Fsbgp4PeerRemoteIpAddr_Type()
)
fsbgp4PeerRemoteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4PeerRemoteIpAddr.setStatus("deprecated")


class _Fsbgp4RfdPeerFom_Type(Integer32):
    """Custom type fsbgp4RfdPeerFom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsbgp4RfdPeerFom_Type.__name__ = "Integer32"
_Fsbgp4RfdPeerFom_Object = MibTableColumn
fsbgp4RfdPeerFom = _Fsbgp4RfdPeerFom_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 3, 1, 2),
    _Fsbgp4RfdPeerFom_Type()
)
fsbgp4RfdPeerFom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RfdPeerFom.setStatus("deprecated")


class _Fsbgp4RfdPeerLastUpdtTime_Type(Integer32):
    """Custom type fsbgp4RfdPeerLastUpdtTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsbgp4RfdPeerLastUpdtTime_Type.__name__ = "Integer32"
_Fsbgp4RfdPeerLastUpdtTime_Object = MibTableColumn
fsbgp4RfdPeerLastUpdtTime = _Fsbgp4RfdPeerLastUpdtTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 3, 1, 3),
    _Fsbgp4RfdPeerLastUpdtTime_Type()
)
fsbgp4RfdPeerLastUpdtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RfdPeerLastUpdtTime.setStatus("deprecated")


class _Fsbgp4RfdPeerState_Type(Integer32):
    """Custom type fsbgp4RfdPeerState based on Integer32"""
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


_Fsbgp4RfdPeerState_Type.__name__ = "Integer32"
_Fsbgp4RfdPeerState_Object = MibTableColumn
fsbgp4RfdPeerState = _Fsbgp4RfdPeerState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 3, 1, 4),
    _Fsbgp4RfdPeerState_Type()
)
fsbgp4RfdPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RfdPeerState.setStatus("deprecated")


class _Fsbgp4RfdPeerStatus_Type(Integer32):
    """Custom type fsbgp4RfdPeerStatus based on Integer32"""
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


_Fsbgp4RfdPeerStatus_Type.__name__ = "Integer32"
_Fsbgp4RfdPeerStatus_Object = MibTableColumn
fsbgp4RfdPeerStatus = _Fsbgp4RfdPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 3, 1, 5),
    _Fsbgp4RfdPeerStatus_Type()
)
fsbgp4RfdPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RfdPeerStatus.setStatus("deprecated")
_Fsbgp4RfdRtsReuseListTable_Object = MibTable
fsbgp4RfdRtsReuseListTable = _Fsbgp4RfdRtsReuseListTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 4)
)
if mibBuilder.loadTexts:
    fsbgp4RfdRtsReuseListTable.setStatus("deprecated")
_Fsbgp4RfdRtsReuseListEntry_Object = MibTableRow
fsbgp4RfdRtsReuseListEntry = _Fsbgp4RfdRtsReuseListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 4, 1)
)
fsbgp4RfdRtsReuseListEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4RtIPPrefix"),
    (0, "ARICENT-BGP-MIB", "fsbgp4RtIPPrefixLen"),
    (0, "ARICENT-BGP-MIB", "fsbgp4PeerRemAddress"),
    (0, "ARICENT-BGP-MIB", "fsbgp4RfdRtReuseListInstance"),
)
if mibBuilder.loadTexts:
    fsbgp4RfdRtsReuseListEntry.setStatus("deprecated")
_Fsbgp4RtIPPrefix_Type = IpAddress
_Fsbgp4RtIPPrefix_Object = MibTableColumn
fsbgp4RtIPPrefix = _Fsbgp4RtIPPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 4, 1, 1),
    _Fsbgp4RtIPPrefix_Type()
)
fsbgp4RtIPPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4RtIPPrefix.setStatus("deprecated")


class _Fsbgp4RtIPPrefixLen_Type(Integer32):
    """Custom type fsbgp4RtIPPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Fsbgp4RtIPPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4RtIPPrefixLen_Object = MibTableColumn
fsbgp4RtIPPrefixLen = _Fsbgp4RtIPPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 4, 1, 2),
    _Fsbgp4RtIPPrefixLen_Type()
)
fsbgp4RtIPPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4RtIPPrefixLen.setStatus("deprecated")
_Fsbgp4PeerRemAddress_Type = IpAddress
_Fsbgp4PeerRemAddress_Object = MibTableColumn
fsbgp4PeerRemAddress = _Fsbgp4PeerRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 4, 1, 3),
    _Fsbgp4PeerRemAddress_Type()
)
fsbgp4PeerRemAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4PeerRemAddress.setStatus("deprecated")


class _Fsbgp4RfdRtReuseListInstance_Type(Integer32):
    """Custom type fsbgp4RfdRtReuseListInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Fsbgp4RfdRtReuseListInstance_Type.__name__ = "Integer32"
_Fsbgp4RfdRtReuseListInstance_Object = MibTableColumn
fsbgp4RfdRtReuseListInstance = _Fsbgp4RfdRtReuseListInstance_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 4, 1, 4),
    _Fsbgp4RfdRtReuseListInstance_Type()
)
fsbgp4RfdRtReuseListInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4RfdRtReuseListInstance.setStatus("deprecated")


class _Fsbgp4RfdRtReuseListRtFom_Type(Integer32):
    """Custom type fsbgp4RfdRtReuseListRtFom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsbgp4RfdRtReuseListRtFom_Type.__name__ = "Integer32"
_Fsbgp4RfdRtReuseListRtFom_Object = MibTableColumn
fsbgp4RfdRtReuseListRtFom = _Fsbgp4RfdRtReuseListRtFom_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 4, 1, 5),
    _Fsbgp4RfdRtReuseListRtFom_Type()
)
fsbgp4RfdRtReuseListRtFom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RfdRtReuseListRtFom.setStatus("deprecated")


class _Fsbgp4RfdRtReuseListRtLastUpdtTime_Type(Integer32):
    """Custom type fsbgp4RfdRtReuseListRtLastUpdtTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsbgp4RfdRtReuseListRtLastUpdtTime_Type.__name__ = "Integer32"
_Fsbgp4RfdRtReuseListRtLastUpdtTime_Object = MibTableColumn
fsbgp4RfdRtReuseListRtLastUpdtTime = _Fsbgp4RfdRtReuseListRtLastUpdtTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 4, 1, 6),
    _Fsbgp4RfdRtReuseListRtLastUpdtTime_Type()
)
fsbgp4RfdRtReuseListRtLastUpdtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RfdRtReuseListRtLastUpdtTime.setStatus("deprecated")


class _Fsbgp4RfdRtReuseListRtState_Type(Integer32):
    """Custom type fsbgp4RfdRtReuseListRtState based on Integer32"""
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


_Fsbgp4RfdRtReuseListRtState_Type.__name__ = "Integer32"
_Fsbgp4RfdRtReuseListRtState_Object = MibTableColumn
fsbgp4RfdRtReuseListRtState = _Fsbgp4RfdRtReuseListRtState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 4, 1, 7),
    _Fsbgp4RfdRtReuseListRtState_Type()
)
fsbgp4RfdRtReuseListRtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RfdRtReuseListRtState.setStatus("deprecated")


class _Fsbgp4RfdRtReuseListRtStatus_Type(Integer32):
    """Custom type fsbgp4RfdRtReuseListRtStatus based on Integer32"""
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


_Fsbgp4RfdRtReuseListRtStatus_Type.__name__ = "Integer32"
_Fsbgp4RfdRtReuseListRtStatus_Object = MibTableColumn
fsbgp4RfdRtReuseListRtStatus = _Fsbgp4RfdRtReuseListRtStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 4, 1, 8),
    _Fsbgp4RfdRtReuseListRtStatus_Type()
)
fsbgp4RfdRtReuseListRtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RfdRtReuseListRtStatus.setStatus("deprecated")
_Fsbgp4RfdPeerReuseListTable_Object = MibTable
fsbgp4RfdPeerReuseListTable = _Fsbgp4RfdPeerReuseListTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 5)
)
if mibBuilder.loadTexts:
    fsbgp4RfdPeerReuseListTable.setStatus("deprecated")
_Fsbgp4RfdPeerReuseListEntry_Object = MibTableRow
fsbgp4RfdPeerReuseListEntry = _Fsbgp4RfdPeerReuseListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 5, 1)
)
fsbgp4RfdPeerReuseListEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4RfdPeerRemIpAddr"),
)
if mibBuilder.loadTexts:
    fsbgp4RfdPeerReuseListEntry.setStatus("deprecated")
_Fsbgp4RfdPeerRemIpAddr_Type = IpAddress
_Fsbgp4RfdPeerRemIpAddr_Object = MibTableColumn
fsbgp4RfdPeerRemIpAddr = _Fsbgp4RfdPeerRemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 5, 1, 1),
    _Fsbgp4RfdPeerRemIpAddr_Type()
)
fsbgp4RfdPeerRemIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4RfdPeerRemIpAddr.setStatus("deprecated")


class _Fsbgp4RfdPeerReuseListPeerFom_Type(Integer32):
    """Custom type fsbgp4RfdPeerReuseListPeerFom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsbgp4RfdPeerReuseListPeerFom_Type.__name__ = "Integer32"
_Fsbgp4RfdPeerReuseListPeerFom_Object = MibTableColumn
fsbgp4RfdPeerReuseListPeerFom = _Fsbgp4RfdPeerReuseListPeerFom_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 5, 1, 2),
    _Fsbgp4RfdPeerReuseListPeerFom_Type()
)
fsbgp4RfdPeerReuseListPeerFom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RfdPeerReuseListPeerFom.setStatus("deprecated")


class _Fsbgp4RfdPeerReuseListLastUpdtTime_Type(Integer32):
    """Custom type fsbgp4RfdPeerReuseListLastUpdtTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsbgp4RfdPeerReuseListLastUpdtTime_Type.__name__ = "Integer32"
_Fsbgp4RfdPeerReuseListLastUpdtTime_Object = MibTableColumn
fsbgp4RfdPeerReuseListLastUpdtTime = _Fsbgp4RfdPeerReuseListLastUpdtTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 5, 1, 3),
    _Fsbgp4RfdPeerReuseListLastUpdtTime_Type()
)
fsbgp4RfdPeerReuseListLastUpdtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RfdPeerReuseListLastUpdtTime.setStatus("deprecated")


class _Fsbgp4RfdPeerReuseListPeerState_Type(Integer32):
    """Custom type fsbgp4RfdPeerReuseListPeerState based on Integer32"""
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


_Fsbgp4RfdPeerReuseListPeerState_Type.__name__ = "Integer32"
_Fsbgp4RfdPeerReuseListPeerState_Object = MibTableColumn
fsbgp4RfdPeerReuseListPeerState = _Fsbgp4RfdPeerReuseListPeerState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 5, 1, 4),
    _Fsbgp4RfdPeerReuseListPeerState_Type()
)
fsbgp4RfdPeerReuseListPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RfdPeerReuseListPeerState.setStatus("deprecated")


class _Fsbgp4RfdPeerReuseListPeerStatus_Type(Integer32):
    """Custom type fsbgp4RfdPeerReuseListPeerStatus based on Integer32"""
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


_Fsbgp4RfdPeerReuseListPeerStatus_Type.__name__ = "Integer32"
_Fsbgp4RfdPeerReuseListPeerStatus_Object = MibTableColumn
fsbgp4RfdPeerReuseListPeerStatus = _Fsbgp4RfdPeerReuseListPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 11, 5, 1, 5),
    _Fsbgp4RfdPeerReuseListPeerStatus_Type()
)
fsbgp4RfdPeerReuseListPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RfdPeerReuseListPeerStatus.setStatus("deprecated")
_FsbgpComm_ObjectIdentity = ObjectIdentity
fsbgpComm = _FsbgpComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12)
)
_Fsbgp4CommScalars_ObjectIdentity = ObjectIdentity
fsbgp4CommScalars = _Fsbgp4CommScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 1)
)


class _Fsbgp4CommMaxInFTblEntries_Type(Integer32):
    """Custom type fsbgp4CommMaxInFTblEntries based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50000),
    )


_Fsbgp4CommMaxInFTblEntries_Type.__name__ = "Integer32"
_Fsbgp4CommMaxInFTblEntries_Object = MibScalar
fsbgp4CommMaxInFTblEntries = _Fsbgp4CommMaxInFTblEntries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 1, 1),
    _Fsbgp4CommMaxInFTblEntries_Type()
)
fsbgp4CommMaxInFTblEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4CommMaxInFTblEntries.setStatus("current")


class _Fsbgp4CommMaxOutFTblEntries_Type(Integer32):
    """Custom type fsbgp4CommMaxOutFTblEntries based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50000),
    )


_Fsbgp4CommMaxOutFTblEntries_Type.__name__ = "Integer32"
_Fsbgp4CommMaxOutFTblEntries_Object = MibScalar
fsbgp4CommMaxOutFTblEntries = _Fsbgp4CommMaxOutFTblEntries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 1, 2),
    _Fsbgp4CommMaxOutFTblEntries_Type()
)
fsbgp4CommMaxOutFTblEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4CommMaxOutFTblEntries.setStatus("current")
_Fsbgp4CommRouteAddCommTable_Object = MibTable
fsbgp4CommRouteAddCommTable = _Fsbgp4CommRouteAddCommTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 2)
)
if mibBuilder.loadTexts:
    fsbgp4CommRouteAddCommTable.setStatus("deprecated")
_Fsbgp4CommRouteAddCommEntry_Object = MibTableRow
fsbgp4CommRouteAddCommEntry = _Fsbgp4CommRouteAddCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 2, 1)
)
fsbgp4CommRouteAddCommEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4AddCommIpNetwork"),
    (0, "ARICENT-BGP-MIB", "fsbgp4AddCommIpPrefixLen"),
    (0, "ARICENT-BGP-MIB", "fsbgp4AddCommVal"),
)
if mibBuilder.loadTexts:
    fsbgp4CommRouteAddCommEntry.setStatus("deprecated")
_Fsbgp4AddCommIpNetwork_Type = IpAddress
_Fsbgp4AddCommIpNetwork_Object = MibTableColumn
fsbgp4AddCommIpNetwork = _Fsbgp4AddCommIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 2, 1, 1),
    _Fsbgp4AddCommIpNetwork_Type()
)
fsbgp4AddCommIpNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4AddCommIpNetwork.setStatus("deprecated")


class _Fsbgp4AddCommIpPrefixLen_Type(Integer32):
    """Custom type fsbgp4AddCommIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fsbgp4AddCommIpPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4AddCommIpPrefixLen_Object = MibTableColumn
fsbgp4AddCommIpPrefixLen = _Fsbgp4AddCommIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 2, 1, 2),
    _Fsbgp4AddCommIpPrefixLen_Type()
)
fsbgp4AddCommIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4AddCommIpPrefixLen.setStatus("deprecated")


class _Fsbgp4AddCommVal_Type(Unsigned32):
    """Custom type fsbgp4AddCommVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65536, 4294901759),
        ValueRangeConstraint(4294967041, 4294967043),
    )


_Fsbgp4AddCommVal_Type.__name__ = "Unsigned32"
_Fsbgp4AddCommVal_Object = MibTableColumn
fsbgp4AddCommVal = _Fsbgp4AddCommVal_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 2, 1, 3),
    _Fsbgp4AddCommVal_Type()
)
fsbgp4AddCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4AddCommVal.setStatus("deprecated")
_Fsbgp4AddCommRowStatus_Type = RowStatus
_Fsbgp4AddCommRowStatus_Object = MibTableColumn
fsbgp4AddCommRowStatus = _Fsbgp4AddCommRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 2, 1, 4),
    _Fsbgp4AddCommRowStatus_Type()
)
fsbgp4AddCommRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4AddCommRowStatus.setStatus("deprecated")
_Fsbgp4CommRouteDeleteCommTable_Object = MibTable
fsbgp4CommRouteDeleteCommTable = _Fsbgp4CommRouteDeleteCommTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 3)
)
if mibBuilder.loadTexts:
    fsbgp4CommRouteDeleteCommTable.setStatus("deprecated")
_Fsbgp4CommRouteDeleteCommEntry_Object = MibTableRow
fsbgp4CommRouteDeleteCommEntry = _Fsbgp4CommRouteDeleteCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 3, 1)
)
fsbgp4CommRouteDeleteCommEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4DeleteCommIpNetwork"),
    (0, "ARICENT-BGP-MIB", "fsbgp4DeleteCommIpPrefixLen"),
    (0, "ARICENT-BGP-MIB", "fsbgp4DeleteCommVal"),
)
if mibBuilder.loadTexts:
    fsbgp4CommRouteDeleteCommEntry.setStatus("deprecated")
_Fsbgp4DeleteCommIpNetwork_Type = IpAddress
_Fsbgp4DeleteCommIpNetwork_Object = MibTableColumn
fsbgp4DeleteCommIpNetwork = _Fsbgp4DeleteCommIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 3, 1, 1),
    _Fsbgp4DeleteCommIpNetwork_Type()
)
fsbgp4DeleteCommIpNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4DeleteCommIpNetwork.setStatus("deprecated")


class _Fsbgp4DeleteCommIpPrefixLen_Type(Integer32):
    """Custom type fsbgp4DeleteCommIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fsbgp4DeleteCommIpPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4DeleteCommIpPrefixLen_Object = MibTableColumn
fsbgp4DeleteCommIpPrefixLen = _Fsbgp4DeleteCommIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 3, 1, 2),
    _Fsbgp4DeleteCommIpPrefixLen_Type()
)
fsbgp4DeleteCommIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4DeleteCommIpPrefixLen.setStatus("deprecated")


class _Fsbgp4DeleteCommVal_Type(Unsigned32):
    """Custom type fsbgp4DeleteCommVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65536, 4294901759),
        ValueRangeConstraint(4294967041, 4294967043),
    )


_Fsbgp4DeleteCommVal_Type.__name__ = "Unsigned32"
_Fsbgp4DeleteCommVal_Object = MibTableColumn
fsbgp4DeleteCommVal = _Fsbgp4DeleteCommVal_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 3, 1, 3),
    _Fsbgp4DeleteCommVal_Type()
)
fsbgp4DeleteCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4DeleteCommVal.setStatus("deprecated")
_Fsbgp4DeleteCommRowStatus_Type = RowStatus
_Fsbgp4DeleteCommRowStatus_Object = MibTableColumn
fsbgp4DeleteCommRowStatus = _Fsbgp4DeleteCommRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 3, 1, 4),
    _Fsbgp4DeleteCommRowStatus_Type()
)
fsbgp4DeleteCommRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4DeleteCommRowStatus.setStatus("deprecated")
_Fsbgp4CommRouteCommSetStatusTable_Object = MibTable
fsbgp4CommRouteCommSetStatusTable = _Fsbgp4CommRouteCommSetStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 4)
)
if mibBuilder.loadTexts:
    fsbgp4CommRouteCommSetStatusTable.setStatus("deprecated")
_Fsbgp4CommRouteCommSetStatusEntry_Object = MibTableRow
fsbgp4CommRouteCommSetStatusEntry = _Fsbgp4CommRouteCommSetStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 4, 1)
)
fsbgp4CommRouteCommSetStatusEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4CommSetStatusIpNetwork"),
    (0, "ARICENT-BGP-MIB", "fsbgp4CommSetStatusIpPrefixLen"),
)
if mibBuilder.loadTexts:
    fsbgp4CommRouteCommSetStatusEntry.setStatus("deprecated")
_Fsbgp4CommSetStatusIpNetwork_Type = IpAddress
_Fsbgp4CommSetStatusIpNetwork_Object = MibTableColumn
fsbgp4CommSetStatusIpNetwork = _Fsbgp4CommSetStatusIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 4, 1, 1),
    _Fsbgp4CommSetStatusIpNetwork_Type()
)
fsbgp4CommSetStatusIpNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4CommSetStatusIpNetwork.setStatus("deprecated")


class _Fsbgp4CommSetStatusIpPrefixLen_Type(Integer32):
    """Custom type fsbgp4CommSetStatusIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fsbgp4CommSetStatusIpPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4CommSetStatusIpPrefixLen_Object = MibTableColumn
fsbgp4CommSetStatusIpPrefixLen = _Fsbgp4CommSetStatusIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 4, 1, 2),
    _Fsbgp4CommSetStatusIpPrefixLen_Type()
)
fsbgp4CommSetStatusIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4CommSetStatusIpPrefixLen.setStatus("deprecated")


class _Fsbgp4CommSetStatus_Type(Integer32):
    """Custom type fsbgp4CommSetStatus based on Integer32"""
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


_Fsbgp4CommSetStatus_Type.__name__ = "Integer32"
_Fsbgp4CommSetStatus_Object = MibTableColumn
fsbgp4CommSetStatus = _Fsbgp4CommSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 4, 1, 3),
    _Fsbgp4CommSetStatus_Type()
)
fsbgp4CommSetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4CommSetStatus.setStatus("deprecated")
_Fsbgp4CommSetStatusRowStatus_Type = RowStatus
_Fsbgp4CommSetStatusRowStatus_Object = MibTableColumn
fsbgp4CommSetStatusRowStatus = _Fsbgp4CommSetStatusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 4, 1, 4),
    _Fsbgp4CommSetStatusRowStatus_Type()
)
fsbgp4CommSetStatusRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4CommSetStatusRowStatus.setStatus("deprecated")
_Fsbgp4CommPeerSendStatusTable_Object = MibTable
fsbgp4CommPeerSendStatusTable = _Fsbgp4CommPeerSendStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 5)
)
if mibBuilder.loadTexts:
    fsbgp4CommPeerSendStatusTable.setStatus("deprecated")
_Fsbgp4CommPeerSendStatusEntry_Object = MibTableRow
fsbgp4CommPeerSendStatusEntry = _Fsbgp4CommPeerSendStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 5, 1)
)
fsbgp4CommPeerSendStatusEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4PeerAddress"),
)
if mibBuilder.loadTexts:
    fsbgp4CommPeerSendStatusEntry.setStatus("deprecated")
_Fsbgp4PeerAddress_Type = IpAddress
_Fsbgp4PeerAddress_Object = MibTableColumn
fsbgp4PeerAddress = _Fsbgp4PeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 5, 1, 1),
    _Fsbgp4PeerAddress_Type()
)
fsbgp4PeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4PeerAddress.setStatus("deprecated")


class _Fsbgp4CommSendStatus_Type(Integer32):
    """Custom type fsbgp4CommSendStatus based on Integer32"""
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
        *(("none", 1),
          ("send", 2),
          ("donotsend", 3))
    )


_Fsbgp4CommSendStatus_Type.__name__ = "Integer32"
_Fsbgp4CommSendStatus_Object = MibTableColumn
fsbgp4CommSendStatus = _Fsbgp4CommSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 5, 1, 2),
    _Fsbgp4CommSendStatus_Type()
)
fsbgp4CommSendStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4CommSendStatus.setStatus("deprecated")
_Fsbgp4CommPeerSendRowStatus_Type = RowStatus
_Fsbgp4CommPeerSendRowStatus_Object = MibTableColumn
fsbgp4CommPeerSendRowStatus = _Fsbgp4CommPeerSendRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 5, 1, 3),
    _Fsbgp4CommPeerSendRowStatus_Type()
)
fsbgp4CommPeerSendRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4CommPeerSendRowStatus.setStatus("deprecated")
_Fsbgp4CommInFilterTable_Object = MibTable
fsbgp4CommInFilterTable = _Fsbgp4CommInFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 6)
)
if mibBuilder.loadTexts:
    fsbgp4CommInFilterTable.setStatus("current")
_Fsbgp4CommInFilterEntry_Object = MibTableRow
fsbgp4CommInFilterEntry = _Fsbgp4CommInFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 6, 1)
)
fsbgp4CommInFilterEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4InFilterCommVal"),
)
if mibBuilder.loadTexts:
    fsbgp4CommInFilterEntry.setStatus("current")


class _Fsbgp4InFilterCommVal_Type(Unsigned32):
    """Custom type fsbgp4InFilterCommVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65536, 4294901759),
        ValueRangeConstraint(4294967041, 4294967043),
    )


_Fsbgp4InFilterCommVal_Type.__name__ = "Unsigned32"
_Fsbgp4InFilterCommVal_Object = MibTableColumn
fsbgp4InFilterCommVal = _Fsbgp4InFilterCommVal_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 6, 1, 1),
    _Fsbgp4InFilterCommVal_Type()
)
fsbgp4InFilterCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4InFilterCommVal.setStatus("current")


class _Fsbgp4CommIncomingFilterStatus_Type(Integer32):
    """Custom type fsbgp4CommIncomingFilterStatus based on Integer32"""
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


_Fsbgp4CommIncomingFilterStatus_Type.__name__ = "Integer32"
_Fsbgp4CommIncomingFilterStatus_Object = MibTableColumn
fsbgp4CommIncomingFilterStatus = _Fsbgp4CommIncomingFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 6, 1, 2),
    _Fsbgp4CommIncomingFilterStatus_Type()
)
fsbgp4CommIncomingFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4CommIncomingFilterStatus.setStatus("current")
_Fsbgp4InFilterRowStatus_Type = RowStatus
_Fsbgp4InFilterRowStatus_Object = MibTableColumn
fsbgp4InFilterRowStatus = _Fsbgp4InFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 6, 1, 3),
    _Fsbgp4InFilterRowStatus_Type()
)
fsbgp4InFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4InFilterRowStatus.setStatus("current")
_Fsbgp4CommOutFilterTable_Object = MibTable
fsbgp4CommOutFilterTable = _Fsbgp4CommOutFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 7)
)
if mibBuilder.loadTexts:
    fsbgp4CommOutFilterTable.setStatus("current")
_Fsbgp4CommOutFilterEntry_Object = MibTableRow
fsbgp4CommOutFilterEntry = _Fsbgp4CommOutFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 7, 1)
)
fsbgp4CommOutFilterEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4OutFilterCommVal"),
)
if mibBuilder.loadTexts:
    fsbgp4CommOutFilterEntry.setStatus("current")


class _Fsbgp4OutFilterCommVal_Type(Unsigned32):
    """Custom type fsbgp4OutFilterCommVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65536, 4294901759),
        ValueRangeConstraint(4294967041, 4294967043),
    )


_Fsbgp4OutFilterCommVal_Type.__name__ = "Unsigned32"
_Fsbgp4OutFilterCommVal_Object = MibTableColumn
fsbgp4OutFilterCommVal = _Fsbgp4OutFilterCommVal_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 7, 1, 1),
    _Fsbgp4OutFilterCommVal_Type()
)
fsbgp4OutFilterCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4OutFilterCommVal.setStatus("current")


class _Fsbgp4CommOutgoingFilterStatus_Type(Integer32):
    """Custom type fsbgp4CommOutgoingFilterStatus based on Integer32"""
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


_Fsbgp4CommOutgoingFilterStatus_Type.__name__ = "Integer32"
_Fsbgp4CommOutgoingFilterStatus_Object = MibTableColumn
fsbgp4CommOutgoingFilterStatus = _Fsbgp4CommOutgoingFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 7, 1, 2),
    _Fsbgp4CommOutgoingFilterStatus_Type()
)
fsbgp4CommOutgoingFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4CommOutgoingFilterStatus.setStatus("current")
_Fsbgp4OutFilterRowStatus_Type = RowStatus
_Fsbgp4OutFilterRowStatus_Object = MibTableColumn
fsbgp4OutFilterRowStatus = _Fsbgp4OutFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 7, 1, 3),
    _Fsbgp4OutFilterRowStatus_Type()
)
fsbgp4OutFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4OutFilterRowStatus.setStatus("current")
_Fsbgp4CommReceivedRouteCommTable_Object = MibTable
fsbgp4CommReceivedRouteCommTable = _Fsbgp4CommReceivedRouteCommTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 8)
)
if mibBuilder.loadTexts:
    fsbgp4CommReceivedRouteCommTable.setStatus("deprecated")
_Fsbgp4CommReceivedRouteCommEntry_Object = MibTableRow
fsbgp4CommReceivedRouteCommEntry = _Fsbgp4CommReceivedRouteCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 8, 1)
)
fsbgp4CommReceivedRouteCommEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4IpNet"),
    (0, "ARICENT-BGP-MIB", "fsbgp4IPPrefixLength"),
    (0, "ARICENT-BGP-MIB", "fsbgp4PeerRemAddr"),
)
if mibBuilder.loadTexts:
    fsbgp4CommReceivedRouteCommEntry.setStatus("deprecated")
_Fsbgp4IpNet_Type = IpAddress
_Fsbgp4IpNet_Object = MibTableColumn
fsbgp4IpNet = _Fsbgp4IpNet_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 8, 1, 1),
    _Fsbgp4IpNet_Type()
)
fsbgp4IpNet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4IpNet.setStatus("deprecated")


class _Fsbgp4IPPrefixLength_Type(Integer32):
    """Custom type fsbgp4IPPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fsbgp4IPPrefixLength_Type.__name__ = "Integer32"
_Fsbgp4IPPrefixLength_Object = MibTableColumn
fsbgp4IPPrefixLength = _Fsbgp4IPPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 8, 1, 2),
    _Fsbgp4IPPrefixLength_Type()
)
fsbgp4IPPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4IPPrefixLength.setStatus("deprecated")
_Fsbgp4PeerRemAddr_Type = IpAddress
_Fsbgp4PeerRemAddr_Object = MibTableColumn
fsbgp4PeerRemAddr = _Fsbgp4PeerRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 8, 1, 3),
    _Fsbgp4PeerRemAddr_Type()
)
fsbgp4PeerRemAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4PeerRemAddr.setStatus("deprecated")


class _Fsbgp4ReceivedRouteCommPath_Type(OctetString):
    """Custom type fsbgp4ReceivedRouteCommPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 800),
    )


_Fsbgp4ReceivedRouteCommPath_Type.__name__ = "OctetString"
_Fsbgp4ReceivedRouteCommPath_Object = MibTableColumn
fsbgp4ReceivedRouteCommPath = _Fsbgp4ReceivedRouteCommPath_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 12, 8, 1, 4),
    _Fsbgp4ReceivedRouteCommPath_Type()
)
fsbgp4ReceivedRouteCommPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4ReceivedRouteCommPath.setStatus("deprecated")
_FsbgpExtComm_ObjectIdentity = ObjectIdentity
fsbgpExtComm = _FsbgpExtComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13)
)
_Fsbgp4ExtCommScalars_ObjectIdentity = ObjectIdentity
fsbgp4ExtCommScalars = _Fsbgp4ExtCommScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 1)
)


class _Fsbgp4ExtCommMaxInFTblEntries_Type(Integer32):
    """Custom type fsbgp4ExtCommMaxInFTblEntries based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_Fsbgp4ExtCommMaxInFTblEntries_Type.__name__ = "Integer32"
_Fsbgp4ExtCommMaxInFTblEntries_Object = MibScalar
fsbgp4ExtCommMaxInFTblEntries = _Fsbgp4ExtCommMaxInFTblEntries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 1, 1),
    _Fsbgp4ExtCommMaxInFTblEntries_Type()
)
fsbgp4ExtCommMaxInFTblEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4ExtCommMaxInFTblEntries.setStatus("current")


class _Fsbgp4ExtCommMaxOutFTblEntries_Type(Integer32):
    """Custom type fsbgp4ExtCommMaxOutFTblEntries based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_Fsbgp4ExtCommMaxOutFTblEntries_Type.__name__ = "Integer32"
_Fsbgp4ExtCommMaxOutFTblEntries_Object = MibScalar
fsbgp4ExtCommMaxOutFTblEntries = _Fsbgp4ExtCommMaxOutFTblEntries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 1, 2),
    _Fsbgp4ExtCommMaxOutFTblEntries_Type()
)
fsbgp4ExtCommMaxOutFTblEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4ExtCommMaxOutFTblEntries.setStatus("current")
_Fsbgp4ExtCommRouteAddExtCommTable_Object = MibTable
fsbgp4ExtCommRouteAddExtCommTable = _Fsbgp4ExtCommRouteAddExtCommTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 2)
)
if mibBuilder.loadTexts:
    fsbgp4ExtCommRouteAddExtCommTable.setStatus("deprecated")
_Fsbgp4ExtCommRouteAddExtCommEntry_Object = MibTableRow
fsbgp4ExtCommRouteAddExtCommEntry = _Fsbgp4ExtCommRouteAddExtCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 2, 1)
)
fsbgp4ExtCommRouteAddExtCommEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4AddExtCommIpNetwork"),
    (0, "ARICENT-BGP-MIB", "fsbgp4AddExtCommIpPrefixLen"),
    (0, "ARICENT-BGP-MIB", "fsbgp4AddExtCommVal"),
)
if mibBuilder.loadTexts:
    fsbgp4ExtCommRouteAddExtCommEntry.setStatus("deprecated")
_Fsbgp4AddExtCommIpNetwork_Type = IpAddress
_Fsbgp4AddExtCommIpNetwork_Object = MibTableColumn
fsbgp4AddExtCommIpNetwork = _Fsbgp4AddExtCommIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 2, 1, 1),
    _Fsbgp4AddExtCommIpNetwork_Type()
)
fsbgp4AddExtCommIpNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4AddExtCommIpNetwork.setStatus("deprecated")


class _Fsbgp4AddExtCommIpPrefixLen_Type(Integer32):
    """Custom type fsbgp4AddExtCommIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fsbgp4AddExtCommIpPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4AddExtCommIpPrefixLen_Object = MibTableColumn
fsbgp4AddExtCommIpPrefixLen = _Fsbgp4AddExtCommIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 2, 1, 2),
    _Fsbgp4AddExtCommIpPrefixLen_Type()
)
fsbgp4AddExtCommIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4AddExtCommIpPrefixLen.setStatus("deprecated")


class _Fsbgp4AddExtCommVal_Type(OctetString):
    """Custom type fsbgp4AddExtCommVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Fsbgp4AddExtCommVal_Type.__name__ = "OctetString"
_Fsbgp4AddExtCommVal_Object = MibTableColumn
fsbgp4AddExtCommVal = _Fsbgp4AddExtCommVal_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 2, 1, 3),
    _Fsbgp4AddExtCommVal_Type()
)
fsbgp4AddExtCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4AddExtCommVal.setStatus("deprecated")
_Fsbgp4AddExtCommRowStatus_Type = RowStatus
_Fsbgp4AddExtCommRowStatus_Object = MibTableColumn
fsbgp4AddExtCommRowStatus = _Fsbgp4AddExtCommRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 2, 1, 4),
    _Fsbgp4AddExtCommRowStatus_Type()
)
fsbgp4AddExtCommRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4AddExtCommRowStatus.setStatus("deprecated")
_Fsbgp4ExtCommRouteDeleteExtCommTable_Object = MibTable
fsbgp4ExtCommRouteDeleteExtCommTable = _Fsbgp4ExtCommRouteDeleteExtCommTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 3)
)
if mibBuilder.loadTexts:
    fsbgp4ExtCommRouteDeleteExtCommTable.setStatus("deprecated")
_Fsbgp4ExtCommRouteDeleteExtCommEntry_Object = MibTableRow
fsbgp4ExtCommRouteDeleteExtCommEntry = _Fsbgp4ExtCommRouteDeleteExtCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 3, 1)
)
fsbgp4ExtCommRouteDeleteExtCommEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4DeleteExtCommIpNetwork"),
    (0, "ARICENT-BGP-MIB", "fsbgp4DeleteExtCommIpPrefixLen"),
    (0, "ARICENT-BGP-MIB", "fsbgp4DeleteExtCommVal"),
)
if mibBuilder.loadTexts:
    fsbgp4ExtCommRouteDeleteExtCommEntry.setStatus("deprecated")
_Fsbgp4DeleteExtCommIpNetwork_Type = IpAddress
_Fsbgp4DeleteExtCommIpNetwork_Object = MibTableColumn
fsbgp4DeleteExtCommIpNetwork = _Fsbgp4DeleteExtCommIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 3, 1, 1),
    _Fsbgp4DeleteExtCommIpNetwork_Type()
)
fsbgp4DeleteExtCommIpNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4DeleteExtCommIpNetwork.setStatus("deprecated")


class _Fsbgp4DeleteExtCommIpPrefixLen_Type(Integer32):
    """Custom type fsbgp4DeleteExtCommIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fsbgp4DeleteExtCommIpPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4DeleteExtCommIpPrefixLen_Object = MibTableColumn
fsbgp4DeleteExtCommIpPrefixLen = _Fsbgp4DeleteExtCommIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 3, 1, 2),
    _Fsbgp4DeleteExtCommIpPrefixLen_Type()
)
fsbgp4DeleteExtCommIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4DeleteExtCommIpPrefixLen.setStatus("deprecated")


class _Fsbgp4DeleteExtCommVal_Type(OctetString):
    """Custom type fsbgp4DeleteExtCommVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Fsbgp4DeleteExtCommVal_Type.__name__ = "OctetString"
_Fsbgp4DeleteExtCommVal_Object = MibTableColumn
fsbgp4DeleteExtCommVal = _Fsbgp4DeleteExtCommVal_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 3, 1, 3),
    _Fsbgp4DeleteExtCommVal_Type()
)
fsbgp4DeleteExtCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4DeleteExtCommVal.setStatus("deprecated")
_Fsbgp4DeleteExtCommRowStatus_Type = RowStatus
_Fsbgp4DeleteExtCommRowStatus_Object = MibTableColumn
fsbgp4DeleteExtCommRowStatus = _Fsbgp4DeleteExtCommRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 3, 1, 4),
    _Fsbgp4DeleteExtCommRowStatus_Type()
)
fsbgp4DeleteExtCommRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4DeleteExtCommRowStatus.setStatus("deprecated")
_Fsbgp4ExtCommRouteExtCommSetStatusTable_Object = MibTable
fsbgp4ExtCommRouteExtCommSetStatusTable = _Fsbgp4ExtCommRouteExtCommSetStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 4)
)
if mibBuilder.loadTexts:
    fsbgp4ExtCommRouteExtCommSetStatusTable.setStatus("deprecated")
_Fsbgp4ExtCommRouteExtCommSetStatusEntry_Object = MibTableRow
fsbgp4ExtCommRouteExtCommSetStatusEntry = _Fsbgp4ExtCommRouteExtCommSetStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 4, 1)
)
fsbgp4ExtCommRouteExtCommSetStatusEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4ExtCommSetStatusIpNetwork"),
    (0, "ARICENT-BGP-MIB", "fsbgp4ExtCommSetStatusIpPrefixLen"),
)
if mibBuilder.loadTexts:
    fsbgp4ExtCommRouteExtCommSetStatusEntry.setStatus("deprecated")
_Fsbgp4ExtCommSetStatusIpNetwork_Type = IpAddress
_Fsbgp4ExtCommSetStatusIpNetwork_Object = MibTableColumn
fsbgp4ExtCommSetStatusIpNetwork = _Fsbgp4ExtCommSetStatusIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 4, 1, 1),
    _Fsbgp4ExtCommSetStatusIpNetwork_Type()
)
fsbgp4ExtCommSetStatusIpNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4ExtCommSetStatusIpNetwork.setStatus("deprecated")


class _Fsbgp4ExtCommSetStatusIpPrefixLen_Type(Integer32):
    """Custom type fsbgp4ExtCommSetStatusIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fsbgp4ExtCommSetStatusIpPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4ExtCommSetStatusIpPrefixLen_Object = MibTableColumn
fsbgp4ExtCommSetStatusIpPrefixLen = _Fsbgp4ExtCommSetStatusIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 4, 1, 2),
    _Fsbgp4ExtCommSetStatusIpPrefixLen_Type()
)
fsbgp4ExtCommSetStatusIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4ExtCommSetStatusIpPrefixLen.setStatus("deprecated")


class _Fsbgp4ExtCommSetStatus_Type(Integer32):
    """Custom type fsbgp4ExtCommSetStatus based on Integer32"""
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


_Fsbgp4ExtCommSetStatus_Type.__name__ = "Integer32"
_Fsbgp4ExtCommSetStatus_Object = MibTableColumn
fsbgp4ExtCommSetStatus = _Fsbgp4ExtCommSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 4, 1, 3),
    _Fsbgp4ExtCommSetStatus_Type()
)
fsbgp4ExtCommSetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4ExtCommSetStatus.setStatus("deprecated")
_Fsbgp4ExtCommSetStatusRowStatus_Type = RowStatus
_Fsbgp4ExtCommSetStatusRowStatus_Object = MibTableColumn
fsbgp4ExtCommSetStatusRowStatus = _Fsbgp4ExtCommSetStatusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 4, 1, 4),
    _Fsbgp4ExtCommSetStatusRowStatus_Type()
)
fsbgp4ExtCommSetStatusRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4ExtCommSetStatusRowStatus.setStatus("deprecated")
_Fsbgp4ExtCommPeerSendStatusTable_Object = MibTable
fsbgp4ExtCommPeerSendStatusTable = _Fsbgp4ExtCommPeerSendStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 5)
)
if mibBuilder.loadTexts:
    fsbgp4ExtCommPeerSendStatusTable.setStatus("deprecated")
_Fsbgp4ExtCommPeerSendStatusEntry_Object = MibTableRow
fsbgp4ExtCommPeerSendStatusEntry = _Fsbgp4ExtCommPeerSendStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 5, 1)
)
fsbgp4ExtCommPeerSendStatusEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4ExtCommPeerAddress"),
)
if mibBuilder.loadTexts:
    fsbgp4ExtCommPeerSendStatusEntry.setStatus("deprecated")
_Fsbgp4ExtCommPeerAddress_Type = IpAddress
_Fsbgp4ExtCommPeerAddress_Object = MibTableColumn
fsbgp4ExtCommPeerAddress = _Fsbgp4ExtCommPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 5, 1, 1),
    _Fsbgp4ExtCommPeerAddress_Type()
)
fsbgp4ExtCommPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4ExtCommPeerAddress.setStatus("deprecated")


class _Fsbgp4ExtCommPeerSendStatus_Type(Integer32):
    """Custom type fsbgp4ExtCommPeerSendStatus based on Integer32"""
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
        *(("none", 1),
          ("send", 2),
          ("donotsend", 3))
    )


_Fsbgp4ExtCommPeerSendStatus_Type.__name__ = "Integer32"
_Fsbgp4ExtCommPeerSendStatus_Object = MibTableColumn
fsbgp4ExtCommPeerSendStatus = _Fsbgp4ExtCommPeerSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 5, 1, 2),
    _Fsbgp4ExtCommPeerSendStatus_Type()
)
fsbgp4ExtCommPeerSendStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4ExtCommPeerSendStatus.setStatus("deprecated")
_Fsbgp4ExtCommPeerSendStatusRowStatus_Type = RowStatus
_Fsbgp4ExtCommPeerSendStatusRowStatus_Object = MibTableColumn
fsbgp4ExtCommPeerSendStatusRowStatus = _Fsbgp4ExtCommPeerSendStatusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 5, 1, 3),
    _Fsbgp4ExtCommPeerSendStatusRowStatus_Type()
)
fsbgp4ExtCommPeerSendStatusRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4ExtCommPeerSendStatusRowStatus.setStatus("deprecated")
_Fsbgp4ExtCommInFilterTable_Object = MibTable
fsbgp4ExtCommInFilterTable = _Fsbgp4ExtCommInFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 6)
)
if mibBuilder.loadTexts:
    fsbgp4ExtCommInFilterTable.setStatus("current")
_Fsbgp4ExtCommInFilterEntry_Object = MibTableRow
fsbgp4ExtCommInFilterEntry = _Fsbgp4ExtCommInFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 6, 1)
)
fsbgp4ExtCommInFilterEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4ExtCommInFilterCommVal"),
)
if mibBuilder.loadTexts:
    fsbgp4ExtCommInFilterEntry.setStatus("current")


class _Fsbgp4ExtCommInFilterCommVal_Type(OctetString):
    """Custom type fsbgp4ExtCommInFilterCommVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Fsbgp4ExtCommInFilterCommVal_Type.__name__ = "OctetString"
_Fsbgp4ExtCommInFilterCommVal_Object = MibTableColumn
fsbgp4ExtCommInFilterCommVal = _Fsbgp4ExtCommInFilterCommVal_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 6, 1, 1),
    _Fsbgp4ExtCommInFilterCommVal_Type()
)
fsbgp4ExtCommInFilterCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4ExtCommInFilterCommVal.setStatus("current")


class _Fsbgp4ExtCommIncomingFilterStatus_Type(Integer32):
    """Custom type fsbgp4ExtCommIncomingFilterStatus based on Integer32"""
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


_Fsbgp4ExtCommIncomingFilterStatus_Type.__name__ = "Integer32"
_Fsbgp4ExtCommIncomingFilterStatus_Object = MibTableColumn
fsbgp4ExtCommIncomingFilterStatus = _Fsbgp4ExtCommIncomingFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 6, 1, 2),
    _Fsbgp4ExtCommIncomingFilterStatus_Type()
)
fsbgp4ExtCommIncomingFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4ExtCommIncomingFilterStatus.setStatus("current")
_Fsbgp4ExtCommInFilterRowStatus_Type = RowStatus
_Fsbgp4ExtCommInFilterRowStatus_Object = MibTableColumn
fsbgp4ExtCommInFilterRowStatus = _Fsbgp4ExtCommInFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 6, 1, 3),
    _Fsbgp4ExtCommInFilterRowStatus_Type()
)
fsbgp4ExtCommInFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4ExtCommInFilterRowStatus.setStatus("current")
_Fsbgp4ExtCommOutFilterTable_Object = MibTable
fsbgp4ExtCommOutFilterTable = _Fsbgp4ExtCommOutFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 7)
)
if mibBuilder.loadTexts:
    fsbgp4ExtCommOutFilterTable.setStatus("current")
_Fsbgp4ExtCommOutFilterEntry_Object = MibTableRow
fsbgp4ExtCommOutFilterEntry = _Fsbgp4ExtCommOutFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 7, 1)
)
fsbgp4ExtCommOutFilterEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4ExtCommOutFilterCommVal"),
)
if mibBuilder.loadTexts:
    fsbgp4ExtCommOutFilterEntry.setStatus("current")


class _Fsbgp4ExtCommOutFilterCommVal_Type(OctetString):
    """Custom type fsbgp4ExtCommOutFilterCommVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Fsbgp4ExtCommOutFilterCommVal_Type.__name__ = "OctetString"
_Fsbgp4ExtCommOutFilterCommVal_Object = MibTableColumn
fsbgp4ExtCommOutFilterCommVal = _Fsbgp4ExtCommOutFilterCommVal_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 7, 1, 1),
    _Fsbgp4ExtCommOutFilterCommVal_Type()
)
fsbgp4ExtCommOutFilterCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4ExtCommOutFilterCommVal.setStatus("current")


class _Fsbgp4ExtCommOutgoingFilterStatus_Type(Integer32):
    """Custom type fsbgp4ExtCommOutgoingFilterStatus based on Integer32"""
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


_Fsbgp4ExtCommOutgoingFilterStatus_Type.__name__ = "Integer32"
_Fsbgp4ExtCommOutgoingFilterStatus_Object = MibTableColumn
fsbgp4ExtCommOutgoingFilterStatus = _Fsbgp4ExtCommOutgoingFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 7, 1, 2),
    _Fsbgp4ExtCommOutgoingFilterStatus_Type()
)
fsbgp4ExtCommOutgoingFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4ExtCommOutgoingFilterStatus.setStatus("current")
_Fsbgp4ExtCommOutFilterRowStatus_Type = RowStatus
_Fsbgp4ExtCommOutFilterRowStatus_Object = MibTableColumn
fsbgp4ExtCommOutFilterRowStatus = _Fsbgp4ExtCommOutFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 7, 1, 3),
    _Fsbgp4ExtCommOutFilterRowStatus_Type()
)
fsbgp4ExtCommOutFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4ExtCommOutFilterRowStatus.setStatus("current")
_Fsbgp4PeerLinkBwTable_Object = MibTable
fsbgp4PeerLinkBwTable = _Fsbgp4PeerLinkBwTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 8)
)
if mibBuilder.loadTexts:
    fsbgp4PeerLinkBwTable.setStatus("deprecated")
_Fsbgp4PeerLinkBwEntry_Object = MibTableRow
fsbgp4PeerLinkBwEntry = _Fsbgp4PeerLinkBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 8, 1)
)
fsbgp4PeerLinkBwEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4PeerLinkRemAddr"),
)
if mibBuilder.loadTexts:
    fsbgp4PeerLinkBwEntry.setStatus("deprecated")
_Fsbgp4PeerLinkRemAddr_Type = IpAddress
_Fsbgp4PeerLinkRemAddr_Object = MibTableColumn
fsbgp4PeerLinkRemAddr = _Fsbgp4PeerLinkRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 8, 1, 1),
    _Fsbgp4PeerLinkRemAddr_Type()
)
fsbgp4PeerLinkRemAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4PeerLinkRemAddr.setStatus("deprecated")


class _Fsbgp4LinkBandWidth_Type(Unsigned32):
    """Custom type fsbgp4LinkBandWidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7000, 4294967295),
    )


_Fsbgp4LinkBandWidth_Type.__name__ = "Unsigned32"
_Fsbgp4LinkBandWidth_Object = MibTableColumn
fsbgp4LinkBandWidth = _Fsbgp4LinkBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 8, 1, 2),
    _Fsbgp4LinkBandWidth_Type()
)
fsbgp4LinkBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4LinkBandWidth.setStatus("deprecated")
_Fsbgp4PeerLinkBwRowStatus_Type = RowStatus
_Fsbgp4PeerLinkBwRowStatus_Object = MibTableColumn
fsbgp4PeerLinkBwRowStatus = _Fsbgp4PeerLinkBwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 8, 1, 3),
    _Fsbgp4PeerLinkBwRowStatus_Type()
)
fsbgp4PeerLinkBwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4PeerLinkBwRowStatus.setStatus("deprecated")
_Fsbgp4ExtCommReceivedRouteExtCommTable_Object = MibTable
fsbgp4ExtCommReceivedRouteExtCommTable = _Fsbgp4ExtCommReceivedRouteExtCommTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 9)
)
if mibBuilder.loadTexts:
    fsbgp4ExtCommReceivedRouteExtCommTable.setStatus("deprecated")
_Fsbgp4ExtCommReceivedRouteExtCommEntry_Object = MibTableRow
fsbgp4ExtCommReceivedRouteExtCommEntry = _Fsbgp4ExtCommReceivedRouteExtCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 9, 1)
)
fsbgp4ExtCommReceivedRouteExtCommEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4ExtCommIpNet"),
    (0, "ARICENT-BGP-MIB", "fsbgp4ExtCommIPPrefixLength"),
    (0, "ARICENT-BGP-MIB", "fsbgp4ExtCommPeerRemAddr"),
)
if mibBuilder.loadTexts:
    fsbgp4ExtCommReceivedRouteExtCommEntry.setStatus("deprecated")
_Fsbgp4ExtCommIpNet_Type = IpAddress
_Fsbgp4ExtCommIpNet_Object = MibTableColumn
fsbgp4ExtCommIpNet = _Fsbgp4ExtCommIpNet_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 9, 1, 1),
    _Fsbgp4ExtCommIpNet_Type()
)
fsbgp4ExtCommIpNet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4ExtCommIpNet.setStatus("deprecated")


class _Fsbgp4ExtCommIPPrefixLength_Type(Integer32):
    """Custom type fsbgp4ExtCommIPPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fsbgp4ExtCommIPPrefixLength_Type.__name__ = "Integer32"
_Fsbgp4ExtCommIPPrefixLength_Object = MibTableColumn
fsbgp4ExtCommIPPrefixLength = _Fsbgp4ExtCommIPPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 9, 1, 2),
    _Fsbgp4ExtCommIPPrefixLength_Type()
)
fsbgp4ExtCommIPPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4ExtCommIPPrefixLength.setStatus("deprecated")
_Fsbgp4ExtCommPeerRemAddr_Type = IpAddress
_Fsbgp4ExtCommPeerRemAddr_Object = MibTableColumn
fsbgp4ExtCommPeerRemAddr = _Fsbgp4ExtCommPeerRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 9, 1, 3),
    _Fsbgp4ExtCommPeerRemAddr_Type()
)
fsbgp4ExtCommPeerRemAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4ExtCommPeerRemAddr.setStatus("deprecated")


class _Fsbgp4ReceivedRouteExtCommPath_Type(OctetString):
    """Custom type fsbgp4ReceivedRouteExtCommPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 800),
    )


_Fsbgp4ReceivedRouteExtCommPath_Type.__name__ = "OctetString"
_Fsbgp4ReceivedRouteExtCommPath_Object = MibTableColumn
fsbgp4ReceivedRouteExtCommPath = _Fsbgp4ReceivedRouteExtCommPath_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 13, 9, 1, 4),
    _Fsbgp4ReceivedRouteExtCommPath_Type()
)
fsbgp4ReceivedRouteExtCommPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4ReceivedRouteExtCommPath.setStatus("deprecated")
_FsbgpCaps_ObjectIdentity = ObjectIdentity
fsbgpCaps = _FsbgpCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14)
)
_FsbgpCapScalars_ObjectIdentity = ObjectIdentity
fsbgpCapScalars = _FsbgpCapScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 1)
)


class _Fsbgp4CapabilitySupportAvailable_Type(TruthValue):
    """Custom type fsbgp4CapabilitySupportAvailable based on TruthValue"""
    defaultValue = 1


_Fsbgp4CapabilitySupportAvailable_Type.__name__ = "TruthValue"
_Fsbgp4CapabilitySupportAvailable_Object = MibScalar
fsbgp4CapabilitySupportAvailable = _Fsbgp4CapabilitySupportAvailable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 1, 1),
    _Fsbgp4CapabilitySupportAvailable_Type()
)
fsbgp4CapabilitySupportAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4CapabilitySupportAvailable.setStatus("current")


class _Fsbgp4MaxCapsPerPeer_Type(Integer32):
    """Custom type fsbgp4MaxCapsPerPeer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Fsbgp4MaxCapsPerPeer_Type.__name__ = "Integer32"
_Fsbgp4MaxCapsPerPeer_Object = MibScalar
fsbgp4MaxCapsPerPeer = _Fsbgp4MaxCapsPerPeer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 1, 2),
    _Fsbgp4MaxCapsPerPeer_Type()
)
fsbgp4MaxCapsPerPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4MaxCapsPerPeer.setStatus("current")


class _Fsbgp4MaxInstancesPerCap_Type(Integer32):
    """Custom type fsbgp4MaxInstancesPerCap based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Fsbgp4MaxInstancesPerCap_Type.__name__ = "Integer32"
_Fsbgp4MaxInstancesPerCap_Object = MibScalar
fsbgp4MaxInstancesPerCap = _Fsbgp4MaxInstancesPerCap_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 1, 3),
    _Fsbgp4MaxInstancesPerCap_Type()
)
fsbgp4MaxInstancesPerCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4MaxInstancesPerCap.setStatus("current")


class _Fsbgp4MaxCapDataSize_Type(Integer32):
    """Custom type fsbgp4MaxCapDataSize based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 252),
    )


_Fsbgp4MaxCapDataSize_Type.__name__ = "Integer32"
_Fsbgp4MaxCapDataSize_Object = MibScalar
fsbgp4MaxCapDataSize = _Fsbgp4MaxCapDataSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 1, 4),
    _Fsbgp4MaxCapDataSize_Type()
)
fsbgp4MaxCapDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4MaxCapDataSize.setStatus("current")
_Fsbgp4CapSupportedCapsTable_Object = MibTable
fsbgp4CapSupportedCapsTable = _Fsbgp4CapSupportedCapsTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 2)
)
if mibBuilder.loadTexts:
    fsbgp4CapSupportedCapsTable.setStatus("deprecated")
_Fsbgp4CapSupportedCapsEntry_Object = MibTableRow
fsbgp4CapSupportedCapsEntry = _Fsbgp4CapSupportedCapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 2, 1)
)
fsbgp4CapSupportedCapsEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4CapPeerRemoteIpAddr"),
    (0, "ARICENT-BGP-MIB", "fsbgp4SupportedCapabilityCode"),
    (0, "ARICENT-BGP-MIB", "fsbgp4SupportedCapabilityInstance"),
)
if mibBuilder.loadTexts:
    fsbgp4CapSupportedCapsEntry.setStatus("deprecated")
_Fsbgp4CapPeerRemoteIpAddr_Type = IpAddress
_Fsbgp4CapPeerRemoteIpAddr_Object = MibTableColumn
fsbgp4CapPeerRemoteIpAddr = _Fsbgp4CapPeerRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 2, 1, 1),
    _Fsbgp4CapPeerRemoteIpAddr_Type()
)
fsbgp4CapPeerRemoteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4CapPeerRemoteIpAddr.setStatus("deprecated")


class _Fsbgp4SupportedCapabilityCode_Type(Integer32):
    """Custom type fsbgp4SupportedCapabilityCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fsbgp4SupportedCapabilityCode_Type.__name__ = "Integer32"
_Fsbgp4SupportedCapabilityCode_Object = MibTableColumn
fsbgp4SupportedCapabilityCode = _Fsbgp4SupportedCapabilityCode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 2, 1, 2),
    _Fsbgp4SupportedCapabilityCode_Type()
)
fsbgp4SupportedCapabilityCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4SupportedCapabilityCode.setStatus("deprecated")


class _Fsbgp4SupportedCapabilityInstance_Type(Integer32):
    """Custom type fsbgp4SupportedCapabilityInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Fsbgp4SupportedCapabilityInstance_Type.__name__ = "Integer32"
_Fsbgp4SupportedCapabilityInstance_Object = MibTableColumn
fsbgp4SupportedCapabilityInstance = _Fsbgp4SupportedCapabilityInstance_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 2, 1, 3),
    _Fsbgp4SupportedCapabilityInstance_Type()
)
fsbgp4SupportedCapabilityInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4SupportedCapabilityInstance.setStatus("deprecated")


class _Fsbgp4SupportedCapabilityLength_Type(Integer32):
    """Custom type fsbgp4SupportedCapabilityLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 251),
    )


_Fsbgp4SupportedCapabilityLength_Type.__name__ = "Integer32"
_Fsbgp4SupportedCapabilityLength_Object = MibTableColumn
fsbgp4SupportedCapabilityLength = _Fsbgp4SupportedCapabilityLength_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 2, 1, 4),
    _Fsbgp4SupportedCapabilityLength_Type()
)
fsbgp4SupportedCapabilityLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4SupportedCapabilityLength.setStatus("deprecated")


class _Fsbgp4SupportedCapabilityValue_Type(OctetString):
    """Custom type fsbgp4SupportedCapabilityValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 251),
    )


_Fsbgp4SupportedCapabilityValue_Type.__name__ = "OctetString"
_Fsbgp4SupportedCapabilityValue_Object = MibTableColumn
fsbgp4SupportedCapabilityValue = _Fsbgp4SupportedCapabilityValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 2, 1, 5),
    _Fsbgp4SupportedCapabilityValue_Type()
)
fsbgp4SupportedCapabilityValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4SupportedCapabilityValue.setStatus("deprecated")
_Fsbgp4CapSupportedCapsRowStatus_Type = RowStatus
_Fsbgp4CapSupportedCapsRowStatus_Object = MibTableColumn
fsbgp4CapSupportedCapsRowStatus = _Fsbgp4CapSupportedCapsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 2, 1, 6),
    _Fsbgp4CapSupportedCapsRowStatus_Type()
)
fsbgp4CapSupportedCapsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4CapSupportedCapsRowStatus.setStatus("deprecated")
_Fsbgp4StrictCapabilityMatchTable_Object = MibTable
fsbgp4StrictCapabilityMatchTable = _Fsbgp4StrictCapabilityMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 3)
)
if mibBuilder.loadTexts:
    fsbgp4StrictCapabilityMatchTable.setStatus("deprecated")
_Fsbgp4StrictCapabilityMatchEntry_Object = MibTableRow
fsbgp4StrictCapabilityMatchEntry = _Fsbgp4StrictCapabilityMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 3, 1)
)
fsbgp4StrictCapabilityMatchEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4PeerRemIpAddr"),
)
if mibBuilder.loadTexts:
    fsbgp4StrictCapabilityMatchEntry.setStatus("deprecated")
_Fsbgp4PeerRemIpAddr_Type = IpAddress
_Fsbgp4PeerRemIpAddr_Object = MibTableColumn
fsbgp4PeerRemIpAddr = _Fsbgp4PeerRemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 3, 1, 1),
    _Fsbgp4PeerRemIpAddr_Type()
)
fsbgp4PeerRemIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4PeerRemIpAddr.setStatus("deprecated")


class _Fsbgp4StrictCapabilityMatch_Type(Integer32):
    """Custom type fsbgp4StrictCapabilityMatch based on Integer32"""
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


_Fsbgp4StrictCapabilityMatch_Type.__name__ = "Integer32"
_Fsbgp4StrictCapabilityMatch_Object = MibTableColumn
fsbgp4StrictCapabilityMatch = _Fsbgp4StrictCapabilityMatch_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 3, 1, 2),
    _Fsbgp4StrictCapabilityMatch_Type()
)
fsbgp4StrictCapabilityMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4StrictCapabilityMatch.setStatus("deprecated")
_Fsbgp4CapsAnnouncedTable_Object = MibTable
fsbgp4CapsAnnouncedTable = _Fsbgp4CapsAnnouncedTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 4)
)
if mibBuilder.loadTexts:
    fsbgp4CapsAnnouncedTable.setStatus("deprecated")
_Fsbgp4CapsAnnouncedEntry_Object = MibTableRow
fsbgp4CapsAnnouncedEntry = _Fsbgp4CapsAnnouncedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 4, 1)
)
fsbgp4CapsAnnouncedEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4PeerIpAddr"),
    (0, "ARICENT-BGP-MIB", "fsbgp4PeerCapAnnouncedCode"),
    (0, "ARICENT-BGP-MIB", "fsbgp4PeerCapAnnouncedInstance"),
)
if mibBuilder.loadTexts:
    fsbgp4CapsAnnouncedEntry.setStatus("deprecated")
_Fsbgp4PeerIpAddr_Type = IpAddress
_Fsbgp4PeerIpAddr_Object = MibTableColumn
fsbgp4PeerIpAddr = _Fsbgp4PeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 4, 1, 1),
    _Fsbgp4PeerIpAddr_Type()
)
fsbgp4PeerIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4PeerIpAddr.setStatus("deprecated")


class _Fsbgp4PeerCapAnnouncedCode_Type(Integer32):
    """Custom type fsbgp4PeerCapAnnouncedCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fsbgp4PeerCapAnnouncedCode_Type.__name__ = "Integer32"
_Fsbgp4PeerCapAnnouncedCode_Object = MibTableColumn
fsbgp4PeerCapAnnouncedCode = _Fsbgp4PeerCapAnnouncedCode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 4, 1, 2),
    _Fsbgp4PeerCapAnnouncedCode_Type()
)
fsbgp4PeerCapAnnouncedCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4PeerCapAnnouncedCode.setStatus("deprecated")


class _Fsbgp4PeerCapAnnouncedInstance_Type(Integer32):
    """Custom type fsbgp4PeerCapAnnouncedInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Fsbgp4PeerCapAnnouncedInstance_Type.__name__ = "Integer32"
_Fsbgp4PeerCapAnnouncedInstance_Object = MibTableColumn
fsbgp4PeerCapAnnouncedInstance = _Fsbgp4PeerCapAnnouncedInstance_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 4, 1, 3),
    _Fsbgp4PeerCapAnnouncedInstance_Type()
)
fsbgp4PeerCapAnnouncedInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4PeerCapAnnouncedInstance.setStatus("deprecated")


class _Fsbgp4PeerCapAnnouncedLength_Type(Integer32):
    """Custom type fsbgp4PeerCapAnnouncedLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 251),
    )


_Fsbgp4PeerCapAnnouncedLength_Type.__name__ = "Integer32"
_Fsbgp4PeerCapAnnouncedLength_Object = MibTableColumn
fsbgp4PeerCapAnnouncedLength = _Fsbgp4PeerCapAnnouncedLength_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 4, 1, 4),
    _Fsbgp4PeerCapAnnouncedLength_Type()
)
fsbgp4PeerCapAnnouncedLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4PeerCapAnnouncedLength.setStatus("deprecated")


class _Fsbgp4PeerCapAnnouncedValue_Type(OctetString):
    """Custom type fsbgp4PeerCapAnnouncedValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 251),
    )


_Fsbgp4PeerCapAnnouncedValue_Type.__name__ = "OctetString"
_Fsbgp4PeerCapAnnouncedValue_Object = MibTableColumn
fsbgp4PeerCapAnnouncedValue = _Fsbgp4PeerCapAnnouncedValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 4, 1, 5),
    _Fsbgp4PeerCapAnnouncedValue_Type()
)
fsbgp4PeerCapAnnouncedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4PeerCapAnnouncedValue.setStatus("deprecated")
_Fsbgp4CapReceivedCapsTable_Object = MibTable
fsbgp4CapReceivedCapsTable = _Fsbgp4CapReceivedCapsTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 5)
)
if mibBuilder.loadTexts:
    fsbgp4CapReceivedCapsTable.setStatus("deprecated")
_Fsbgp4CapReceivedCapsEntry_Object = MibTableRow
fsbgp4CapReceivedCapsEntry = _Fsbgp4CapReceivedCapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 5, 1)
)
fsbgp4CapReceivedCapsEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4PeerRemoteAddress"),
    (0, "ARICENT-BGP-MIB", "fsbgp4PeerCapReceivedCode"),
    (0, "ARICENT-BGP-MIB", "fsbgp4PeerCapReceivedInstance"),
)
if mibBuilder.loadTexts:
    fsbgp4CapReceivedCapsEntry.setStatus("deprecated")
_Fsbgp4PeerRemoteAddress_Type = IpAddress
_Fsbgp4PeerRemoteAddress_Object = MibTableColumn
fsbgp4PeerRemoteAddress = _Fsbgp4PeerRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 5, 1, 1),
    _Fsbgp4PeerRemoteAddress_Type()
)
fsbgp4PeerRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4PeerRemoteAddress.setStatus("deprecated")


class _Fsbgp4PeerCapReceivedCode_Type(Integer32):
    """Custom type fsbgp4PeerCapReceivedCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fsbgp4PeerCapReceivedCode_Type.__name__ = "Integer32"
_Fsbgp4PeerCapReceivedCode_Object = MibTableColumn
fsbgp4PeerCapReceivedCode = _Fsbgp4PeerCapReceivedCode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 5, 1, 2),
    _Fsbgp4PeerCapReceivedCode_Type()
)
fsbgp4PeerCapReceivedCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4PeerCapReceivedCode.setStatus("deprecated")


class _Fsbgp4PeerCapReceivedInstance_Type(Integer32):
    """Custom type fsbgp4PeerCapReceivedInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Fsbgp4PeerCapReceivedInstance_Type.__name__ = "Integer32"
_Fsbgp4PeerCapReceivedInstance_Object = MibTableColumn
fsbgp4PeerCapReceivedInstance = _Fsbgp4PeerCapReceivedInstance_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 5, 1, 3),
    _Fsbgp4PeerCapReceivedInstance_Type()
)
fsbgp4PeerCapReceivedInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4PeerCapReceivedInstance.setStatus("deprecated")


class _Fsbgp4PeerCapReceivedLength_Type(Integer32):
    """Custom type fsbgp4PeerCapReceivedLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 251),
    )


_Fsbgp4PeerCapReceivedLength_Type.__name__ = "Integer32"
_Fsbgp4PeerCapReceivedLength_Object = MibTableColumn
fsbgp4PeerCapReceivedLength = _Fsbgp4PeerCapReceivedLength_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 5, 1, 4),
    _Fsbgp4PeerCapReceivedLength_Type()
)
fsbgp4PeerCapReceivedLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4PeerCapReceivedLength.setStatus("deprecated")


class _Fsbgp4PeerCapReceivedValue_Type(OctetString):
    """Custom type fsbgp4PeerCapReceivedValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 251),
    )


_Fsbgp4PeerCapReceivedValue_Type.__name__ = "OctetString"
_Fsbgp4PeerCapReceivedValue_Object = MibTableColumn
fsbgp4PeerCapReceivedValue = _Fsbgp4PeerCapReceivedValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 5, 1, 5),
    _Fsbgp4PeerCapReceivedValue_Type()
)
fsbgp4PeerCapReceivedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4PeerCapReceivedValue.setStatus("deprecated")
_Fsbgp4CapAcceptedCapsTable_Object = MibTable
fsbgp4CapAcceptedCapsTable = _Fsbgp4CapAcceptedCapsTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 6)
)
if mibBuilder.loadTexts:
    fsbgp4CapAcceptedCapsTable.setStatus("deprecated")
_Fsbgp4CapAcceptedCapsEntry_Object = MibTableRow
fsbgp4CapAcceptedCapsEntry = _Fsbgp4CapAcceptedCapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 6, 1)
)
fsbgp4CapAcceptedCapsEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4CapAcceptedPeerRemAddr"),
    (0, "ARICENT-BGP-MIB", "fsbgp4PeerCapAcceptedCode"),
    (0, "ARICENT-BGP-MIB", "fsbgp4PeerCapAcceptedInstance"),
)
if mibBuilder.loadTexts:
    fsbgp4CapAcceptedCapsEntry.setStatus("deprecated")
_Fsbgp4CapAcceptedPeerRemAddr_Type = IpAddress
_Fsbgp4CapAcceptedPeerRemAddr_Object = MibTableColumn
fsbgp4CapAcceptedPeerRemAddr = _Fsbgp4CapAcceptedPeerRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 6, 1, 1),
    _Fsbgp4CapAcceptedPeerRemAddr_Type()
)
fsbgp4CapAcceptedPeerRemAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4CapAcceptedPeerRemAddr.setStatus("deprecated")


class _Fsbgp4PeerCapAcceptedCode_Type(Integer32):
    """Custom type fsbgp4PeerCapAcceptedCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fsbgp4PeerCapAcceptedCode_Type.__name__ = "Integer32"
_Fsbgp4PeerCapAcceptedCode_Object = MibTableColumn
fsbgp4PeerCapAcceptedCode = _Fsbgp4PeerCapAcceptedCode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 6, 1, 2),
    _Fsbgp4PeerCapAcceptedCode_Type()
)
fsbgp4PeerCapAcceptedCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4PeerCapAcceptedCode.setStatus("deprecated")


class _Fsbgp4PeerCapAcceptedInstance_Type(Integer32):
    """Custom type fsbgp4PeerCapAcceptedInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Fsbgp4PeerCapAcceptedInstance_Type.__name__ = "Integer32"
_Fsbgp4PeerCapAcceptedInstance_Object = MibTableColumn
fsbgp4PeerCapAcceptedInstance = _Fsbgp4PeerCapAcceptedInstance_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 6, 1, 3),
    _Fsbgp4PeerCapAcceptedInstance_Type()
)
fsbgp4PeerCapAcceptedInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4PeerCapAcceptedInstance.setStatus("deprecated")


class _Fsbgp4PeerCapAcceptedLength_Type(Integer32):
    """Custom type fsbgp4PeerCapAcceptedLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 251),
    )


_Fsbgp4PeerCapAcceptedLength_Type.__name__ = "Integer32"
_Fsbgp4PeerCapAcceptedLength_Object = MibTableColumn
fsbgp4PeerCapAcceptedLength = _Fsbgp4PeerCapAcceptedLength_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 6, 1, 4),
    _Fsbgp4PeerCapAcceptedLength_Type()
)
fsbgp4PeerCapAcceptedLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4PeerCapAcceptedLength.setStatus("deprecated")


class _Fsbgp4PeerCapAcceptedValue_Type(OctetString):
    """Custom type fsbgp4PeerCapAcceptedValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 251),
    )


_Fsbgp4PeerCapAcceptedValue_Type.__name__ = "OctetString"
_Fsbgp4PeerCapAcceptedValue_Object = MibTableColumn
fsbgp4PeerCapAcceptedValue = _Fsbgp4PeerCapAcceptedValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 14, 6, 1, 5),
    _Fsbgp4PeerCapAcceptedValue_Type()
)
fsbgp4PeerCapAcceptedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4PeerCapAcceptedValue.setStatus("deprecated")
_FsbgpAsc_ObjectIdentity = ObjectIdentity
fsbgpAsc = _FsbgpAsc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 15)
)
_FsbgpAscScalars_ObjectIdentity = ObjectIdentity
fsbgpAscScalars = _FsbgpAscScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 15, 1)
)


class _FsbgpAscConfedId_Type(Unsigned32):
    """Custom type fsbgpAscConfedId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsbgpAscConfedId_Type.__name__ = "Unsigned32"
_FsbgpAscConfedId_Object = MibScalar
fsbgpAscConfedId = _FsbgpAscConfedId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 15, 1, 1),
    _FsbgpAscConfedId_Type()
)
fsbgpAscConfedId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgpAscConfedId.setStatus("current")


class _FsbgpAscConfedBestPathCompareMED_Type(Integer32):
    """Custom type fsbgpAscConfedBestPathCompareMED based on Integer32"""
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


_FsbgpAscConfedBestPathCompareMED_Type.__name__ = "Integer32"
_FsbgpAscConfedBestPathCompareMED_Object = MibScalar
fsbgpAscConfedBestPathCompareMED = _FsbgpAscConfedBestPathCompareMED_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 15, 1, 2),
    _FsbgpAscConfedBestPathCompareMED_Type()
)
fsbgpAscConfedBestPathCompareMED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgpAscConfedBestPathCompareMED.setStatus("current")
_FsbgpAscConfedPeerTable_Object = MibTable
fsbgpAscConfedPeerTable = _FsbgpAscConfedPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 15, 2)
)
if mibBuilder.loadTexts:
    fsbgpAscConfedPeerTable.setStatus("current")
_FsbgpAscConfedPeerEntry_Object = MibTableRow
fsbgpAscConfedPeerEntry = _FsbgpAscConfedPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 15, 2, 1)
)
fsbgpAscConfedPeerEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgpAscConfedPeerASNo"),
)
if mibBuilder.loadTexts:
    fsbgpAscConfedPeerEntry.setStatus("current")


class _FsbgpAscConfedPeerASNo_Type(Unsigned32):
    """Custom type fsbgpAscConfedPeerASNo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsbgpAscConfedPeerASNo_Type.__name__ = "Unsigned32"
_FsbgpAscConfedPeerASNo_Object = MibTableColumn
fsbgpAscConfedPeerASNo = _FsbgpAscConfedPeerASNo_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 15, 2, 1, 1),
    _FsbgpAscConfedPeerASNo_Type()
)
fsbgpAscConfedPeerASNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgpAscConfedPeerASNo.setStatus("current")


class _FsbgpAscConfedPeerStatus_Type(Integer32):
    """Custom type fsbgpAscConfedPeerStatus based on Integer32"""
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


_FsbgpAscConfedPeerStatus_Type.__name__ = "Integer32"
_FsbgpAscConfedPeerStatus_Object = MibTableColumn
fsbgpAscConfedPeerStatus = _FsbgpAscConfedPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 15, 2, 1, 2),
    _FsbgpAscConfedPeerStatus_Type()
)
fsbgpAscConfedPeerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgpAscConfedPeerStatus.setStatus("current")
_Fsbgp4RtRefresh_ObjectIdentity = ObjectIdentity
fsbgp4RtRefresh = _Fsbgp4RtRefresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 16)
)


class _Fsbgp4RtRefreshAllPeerInboundRequest_Type(TruthValue):
    """Custom type fsbgp4RtRefreshAllPeerInboundRequest based on TruthValue"""
    defaultValue = 2


_Fsbgp4RtRefreshAllPeerInboundRequest_Type.__name__ = "TruthValue"
_Fsbgp4RtRefreshAllPeerInboundRequest_Object = MibScalar
fsbgp4RtRefreshAllPeerInboundRequest = _Fsbgp4RtRefreshAllPeerInboundRequest_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 16, 1),
    _Fsbgp4RtRefreshAllPeerInboundRequest_Type()
)
fsbgp4RtRefreshAllPeerInboundRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RtRefreshAllPeerInboundRequest.setStatus("deprecated")
_Fsbgp4RtRefreshInboundTable_Object = MibTable
fsbgp4RtRefreshInboundTable = _Fsbgp4RtRefreshInboundTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 16, 2)
)
if mibBuilder.loadTexts:
    fsbgp4RtRefreshInboundTable.setStatus("deprecated")
_Fsbgp4RtRefreshInboundEntry_Object = MibTableRow
fsbgp4RtRefreshInboundEntry = _Fsbgp4RtRefreshInboundEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 16, 2, 1)
)
fsbgp4RtRefreshInboundEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4RtRefreshInboundPeerType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4RtRefreshInboundPeerAddr"),
)
if mibBuilder.loadTexts:
    fsbgp4RtRefreshInboundEntry.setStatus("deprecated")
_Fsbgp4RtRefreshInboundPeerType_Type = InetAddressType
_Fsbgp4RtRefreshInboundPeerType_Object = MibTableColumn
fsbgp4RtRefreshInboundPeerType = _Fsbgp4RtRefreshInboundPeerType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 16, 2, 1, 1),
    _Fsbgp4RtRefreshInboundPeerType_Type()
)
fsbgp4RtRefreshInboundPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4RtRefreshInboundPeerType.setStatus("deprecated")


class _Fsbgp4RtRefreshInboundPeerAddr_Type(OctetString):
    """Custom type fsbgp4RtRefreshInboundPeerAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Fsbgp4RtRefreshInboundPeerAddr_Type.__name__ = "OctetString"
_Fsbgp4RtRefreshInboundPeerAddr_Object = MibTableColumn
fsbgp4RtRefreshInboundPeerAddr = _Fsbgp4RtRefreshInboundPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 16, 2, 1, 2),
    _Fsbgp4RtRefreshInboundPeerAddr_Type()
)
fsbgp4RtRefreshInboundPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4RtRefreshInboundPeerAddr.setStatus("deprecated")
_Fsbgp4RtRefreshInboundRequest_Type = TruthValue
_Fsbgp4RtRefreshInboundRequest_Object = MibTableColumn
fsbgp4RtRefreshInboundRequest = _Fsbgp4RtRefreshInboundRequest_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 16, 2, 1, 3),
    _Fsbgp4RtRefreshInboundRequest_Type()
)
fsbgp4RtRefreshInboundRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4RtRefreshInboundRequest.setStatus("deprecated")
_Fsbgp4RtRefreshStatisticsTable_Object = MibTable
fsbgp4RtRefreshStatisticsTable = _Fsbgp4RtRefreshStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 16, 3)
)
if mibBuilder.loadTexts:
    fsbgp4RtRefreshStatisticsTable.setStatus("deprecated")
_Fsbgp4RtRefreshStatisticsEntry_Object = MibTableRow
fsbgp4RtRefreshStatisticsEntry = _Fsbgp4RtRefreshStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 16, 3, 1)
)
fsbgp4RtRefreshStatisticsEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4RtRefreshStatisticsPeerType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4RtRefreshStatisticsPeerAddr"),
)
if mibBuilder.loadTexts:
    fsbgp4RtRefreshStatisticsEntry.setStatus("deprecated")
_Fsbgp4RtRefreshStatisticsPeerType_Type = InetAddressType
_Fsbgp4RtRefreshStatisticsPeerType_Object = MibTableColumn
fsbgp4RtRefreshStatisticsPeerType = _Fsbgp4RtRefreshStatisticsPeerType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 16, 3, 1, 1),
    _Fsbgp4RtRefreshStatisticsPeerType_Type()
)
fsbgp4RtRefreshStatisticsPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4RtRefreshStatisticsPeerType.setStatus("deprecated")


class _Fsbgp4RtRefreshStatisticsPeerAddr_Type(OctetString):
    """Custom type fsbgp4RtRefreshStatisticsPeerAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Fsbgp4RtRefreshStatisticsPeerAddr_Type.__name__ = "OctetString"
_Fsbgp4RtRefreshStatisticsPeerAddr_Object = MibTableColumn
fsbgp4RtRefreshStatisticsPeerAddr = _Fsbgp4RtRefreshStatisticsPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 16, 3, 1, 2),
    _Fsbgp4RtRefreshStatisticsPeerAddr_Type()
)
fsbgp4RtRefreshStatisticsPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4RtRefreshStatisticsPeerAddr.setStatus("deprecated")
_Fsbgp4RtRefreshStatisticsRtRefMsgSentCntr_Type = Counter32
_Fsbgp4RtRefreshStatisticsRtRefMsgSentCntr_Object = MibTableColumn
fsbgp4RtRefreshStatisticsRtRefMsgSentCntr = _Fsbgp4RtRefreshStatisticsRtRefMsgSentCntr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 16, 3, 1, 3),
    _Fsbgp4RtRefreshStatisticsRtRefMsgSentCntr_Type()
)
fsbgp4RtRefreshStatisticsRtRefMsgSentCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RtRefreshStatisticsRtRefMsgSentCntr.setStatus("deprecated")
_Fsbgp4RtRefreshStatisticsRtRefMsgTxErrCntr_Type = Counter32
_Fsbgp4RtRefreshStatisticsRtRefMsgTxErrCntr_Object = MibTableColumn
fsbgp4RtRefreshStatisticsRtRefMsgTxErrCntr = _Fsbgp4RtRefreshStatisticsRtRefMsgTxErrCntr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 16, 3, 1, 4),
    _Fsbgp4RtRefreshStatisticsRtRefMsgTxErrCntr_Type()
)
fsbgp4RtRefreshStatisticsRtRefMsgTxErrCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RtRefreshStatisticsRtRefMsgTxErrCntr.setStatus("deprecated")
_Fsbgp4RtRefreshStatisticsRtRefMsgRcvdCntr_Type = Counter32
_Fsbgp4RtRefreshStatisticsRtRefMsgRcvdCntr_Object = MibTableColumn
fsbgp4RtRefreshStatisticsRtRefMsgRcvdCntr = _Fsbgp4RtRefreshStatisticsRtRefMsgRcvdCntr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 16, 3, 1, 5),
    _Fsbgp4RtRefreshStatisticsRtRefMsgRcvdCntr_Type()
)
fsbgp4RtRefreshStatisticsRtRefMsgRcvdCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RtRefreshStatisticsRtRefMsgRcvdCntr.setStatus("deprecated")
_Fsbgp4RtRefreshStatisticsRtRefMsgInvalidCntr_Type = Counter32
_Fsbgp4RtRefreshStatisticsRtRefMsgInvalidCntr_Object = MibTableColumn
fsbgp4RtRefreshStatisticsRtRefMsgInvalidCntr = _Fsbgp4RtRefreshStatisticsRtRefMsgInvalidCntr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 16, 3, 1, 6),
    _Fsbgp4RtRefreshStatisticsRtRefMsgInvalidCntr_Type()
)
fsbgp4RtRefreshStatisticsRtRefMsgInvalidCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4RtRefreshStatisticsRtRefMsgInvalidCntr.setStatus("deprecated")
_Fsbgp4TCPMD5Auth_ObjectIdentity = ObjectIdentity
fsbgp4TCPMD5Auth = _Fsbgp4TCPMD5Auth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 17)
)
_Fsbgp4TCPMD5AuthTable_Object = MibTable
fsbgp4TCPMD5AuthTable = _Fsbgp4TCPMD5AuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 17, 1)
)
if mibBuilder.loadTexts:
    fsbgp4TCPMD5AuthTable.setStatus("current")
_Fsbgp4TCPMD5AuthEntry_Object = MibTableRow
fsbgp4TCPMD5AuthEntry = _Fsbgp4TCPMD5AuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 17, 1, 1)
)
fsbgp4TCPMD5AuthEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4TCPMD5AuthPeerType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4TCPMD5AuthPeerAddr"),
)
if mibBuilder.loadTexts:
    fsbgp4TCPMD5AuthEntry.setStatus("current")
_Fsbgp4TCPMD5AuthPeerType_Type = InetAddressType
_Fsbgp4TCPMD5AuthPeerType_Object = MibTableColumn
fsbgp4TCPMD5AuthPeerType = _Fsbgp4TCPMD5AuthPeerType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 17, 1, 1, 1),
    _Fsbgp4TCPMD5AuthPeerType_Type()
)
fsbgp4TCPMD5AuthPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4TCPMD5AuthPeerType.setStatus("current")


class _Fsbgp4TCPMD5AuthPeerAddr_Type(OctetString):
    """Custom type fsbgp4TCPMD5AuthPeerAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Fsbgp4TCPMD5AuthPeerAddr_Type.__name__ = "OctetString"
_Fsbgp4TCPMD5AuthPeerAddr_Object = MibTableColumn
fsbgp4TCPMD5AuthPeerAddr = _Fsbgp4TCPMD5AuthPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 17, 1, 1, 2),
    _Fsbgp4TCPMD5AuthPeerAddr_Type()
)
fsbgp4TCPMD5AuthPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4TCPMD5AuthPeerAddr.setStatus("current")


class _Fsbgp4TCPMD5AuthPassword_Type(OctetString):
    """Custom type fsbgp4TCPMD5AuthPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Fsbgp4TCPMD5AuthPassword_Type.__name__ = "OctetString"
_Fsbgp4TCPMD5AuthPassword_Object = MibTableColumn
fsbgp4TCPMD5AuthPassword = _Fsbgp4TCPMD5AuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 17, 1, 1, 3),
    _Fsbgp4TCPMD5AuthPassword_Type()
)
fsbgp4TCPMD5AuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4TCPMD5AuthPassword.setStatus("current")


class _Fsbgp4TCPMD5AuthPwdSet_Type(Integer32):
    """Custom type fsbgp4TCPMD5AuthPwdSet based on Integer32"""
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


_Fsbgp4TCPMD5AuthPwdSet_Type.__name__ = "Integer32"
_Fsbgp4TCPMD5AuthPwdSet_Object = MibTableColumn
fsbgp4TCPMD5AuthPwdSet = _Fsbgp4TCPMD5AuthPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 17, 1, 1, 4),
    _Fsbgp4TCPMD5AuthPwdSet_Type()
)
fsbgp4TCPMD5AuthPwdSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4TCPMD5AuthPwdSet.setStatus("current")
_Fsbgp4SoftReconfigOut_ObjectIdentity = ObjectIdentity
fsbgp4SoftReconfigOut = _Fsbgp4SoftReconfigOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 18)
)


class _Fsbgp4SoftReconfigAllPeerOutboundRequest_Type(TruthValue):
    """Custom type fsbgp4SoftReconfigAllPeerOutboundRequest based on TruthValue"""
    defaultValue = 2


_Fsbgp4SoftReconfigAllPeerOutboundRequest_Type.__name__ = "TruthValue"
_Fsbgp4SoftReconfigAllPeerOutboundRequest_Object = MibScalar
fsbgp4SoftReconfigAllPeerOutboundRequest = _Fsbgp4SoftReconfigAllPeerOutboundRequest_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 18, 1),
    _Fsbgp4SoftReconfigAllPeerOutboundRequest_Type()
)
fsbgp4SoftReconfigAllPeerOutboundRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4SoftReconfigAllPeerOutboundRequest.setStatus("deprecated")
_Fsbgp4SoftReconfigOutboundTable_Object = MibTable
fsbgp4SoftReconfigOutboundTable = _Fsbgp4SoftReconfigOutboundTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 18, 2)
)
if mibBuilder.loadTexts:
    fsbgp4SoftReconfigOutboundTable.setStatus("deprecated")
_Fsbgp4SoftReconfigOutboundEntry_Object = MibTableRow
fsbgp4SoftReconfigOutboundEntry = _Fsbgp4SoftReconfigOutboundEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 18, 2, 1)
)
fsbgp4SoftReconfigOutboundEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4SoftReconfigOutboundPeerType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4SoftReconfigOutboundPeerAddr"),
)
if mibBuilder.loadTexts:
    fsbgp4SoftReconfigOutboundEntry.setStatus("deprecated")
_Fsbgp4SoftReconfigOutboundPeerType_Type = InetAddressType
_Fsbgp4SoftReconfigOutboundPeerType_Object = MibTableColumn
fsbgp4SoftReconfigOutboundPeerType = _Fsbgp4SoftReconfigOutboundPeerType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 18, 2, 1, 1),
    _Fsbgp4SoftReconfigOutboundPeerType_Type()
)
fsbgp4SoftReconfigOutboundPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4SoftReconfigOutboundPeerType.setStatus("deprecated")


class _Fsbgp4SoftReconfigOutboundPeerAddr_Type(OctetString):
    """Custom type fsbgp4SoftReconfigOutboundPeerAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Fsbgp4SoftReconfigOutboundPeerAddr_Type.__name__ = "OctetString"
_Fsbgp4SoftReconfigOutboundPeerAddr_Object = MibTableColumn
fsbgp4SoftReconfigOutboundPeerAddr = _Fsbgp4SoftReconfigOutboundPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 18, 2, 1, 2),
    _Fsbgp4SoftReconfigOutboundPeerAddr_Type()
)
fsbgp4SoftReconfigOutboundPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4SoftReconfigOutboundPeerAddr.setStatus("deprecated")
_Fsbgp4SoftReconfigOutboundRequest_Type = TruthValue
_Fsbgp4SoftReconfigOutboundRequest_Object = MibTableColumn
fsbgp4SoftReconfigOutboundRequest = _Fsbgp4SoftReconfigOutboundRequest_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 18, 2, 1, 3),
    _Fsbgp4SoftReconfigOutboundRequest_Type()
)
fsbgp4SoftReconfigOutboundRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4SoftReconfigOutboundRequest.setStatus("deprecated")
_Fsbgp4MpeBgpPeerTable_Object = MibTable
fsbgp4MpeBgpPeerTable = _Fsbgp4MpeBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19)
)
if mibBuilder.loadTexts:
    fsbgp4MpeBgpPeerTable.setStatus("current")
_Fsbgp4MpeBgpPeerEntry_Object = MibTableRow
fsbgp4MpeBgpPeerEntry = _Fsbgp4MpeBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1)
)
fsbgp4MpeBgpPeerEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpebgpPeerRemoteAddrType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpebgpPeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeBgpPeerEntry.setStatus("current")
_Fsbgp4mpebgpPeerRemoteAddrType_Type = InetAddressType
_Fsbgp4mpebgpPeerRemoteAddrType_Object = MibTableColumn
fsbgp4mpebgpPeerRemoteAddrType = _Fsbgp4mpebgpPeerRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 1),
    _Fsbgp4mpebgpPeerRemoteAddrType_Type()
)
fsbgp4mpebgpPeerRemoteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerRemoteAddrType.setStatus("current")
_Fsbgp4mpebgpPeerIdentifier_Type = InetAddress
_Fsbgp4mpebgpPeerIdentifier_Object = MibTableColumn
fsbgp4mpebgpPeerIdentifier = _Fsbgp4mpebgpPeerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 2),
    _Fsbgp4mpebgpPeerIdentifier_Type()
)
fsbgp4mpebgpPeerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerIdentifier.setStatus("current")


class _Fsbgp4mpebgpPeerState_Type(Integer32):
    """Custom type fsbgp4mpebgpPeerState based on Integer32"""
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


_Fsbgp4mpebgpPeerState_Type.__name__ = "Integer32"
_Fsbgp4mpebgpPeerState_Object = MibTableColumn
fsbgp4mpebgpPeerState = _Fsbgp4mpebgpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 3),
    _Fsbgp4mpebgpPeerState_Type()
)
fsbgp4mpebgpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerState.setStatus("current")


class _Fsbgp4mpebgpPeerAdminStatus_Type(Integer32):
    """Custom type fsbgp4mpebgpPeerAdminStatus based on Integer32"""
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
          ("auto-start", 3))
    )


_Fsbgp4mpebgpPeerAdminStatus_Type.__name__ = "Integer32"
_Fsbgp4mpebgpPeerAdminStatus_Object = MibTableColumn
fsbgp4mpebgpPeerAdminStatus = _Fsbgp4mpebgpPeerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 4),
    _Fsbgp4mpebgpPeerAdminStatus_Type()
)
fsbgp4mpebgpPeerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerAdminStatus.setStatus("current")
_Fsbgp4mpebgpPeerNegotiatedVersion_Type = Integer32
_Fsbgp4mpebgpPeerNegotiatedVersion_Object = MibTableColumn
fsbgp4mpebgpPeerNegotiatedVersion = _Fsbgp4mpebgpPeerNegotiatedVersion_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 5),
    _Fsbgp4mpebgpPeerNegotiatedVersion_Type()
)
fsbgp4mpebgpPeerNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerNegotiatedVersion.setStatus("current")
_Fsbgp4mpebgpPeerLocalAddr_Type = InetAddress
_Fsbgp4mpebgpPeerLocalAddr_Object = MibTableColumn
fsbgp4mpebgpPeerLocalAddr = _Fsbgp4mpebgpPeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 6),
    _Fsbgp4mpebgpPeerLocalAddr_Type()
)
fsbgp4mpebgpPeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerLocalAddr.setStatus("current")


class _Fsbgp4mpebgpPeerLocalPort_Type(Integer32):
    """Custom type fsbgp4mpebgpPeerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsbgp4mpebgpPeerLocalPort_Type.__name__ = "Integer32"
_Fsbgp4mpebgpPeerLocalPort_Object = MibTableColumn
fsbgp4mpebgpPeerLocalPort = _Fsbgp4mpebgpPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 7),
    _Fsbgp4mpebgpPeerLocalPort_Type()
)
fsbgp4mpebgpPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerLocalPort.setStatus("current")
_Fsbgp4mpebgpPeerRemoteAddr_Type = InetAddress
_Fsbgp4mpebgpPeerRemoteAddr_Object = MibTableColumn
fsbgp4mpebgpPeerRemoteAddr = _Fsbgp4mpebgpPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 8),
    _Fsbgp4mpebgpPeerRemoteAddr_Type()
)
fsbgp4mpebgpPeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerRemoteAddr.setStatus("current")


class _Fsbgp4mpebgpPeerRemotePort_Type(Integer32):
    """Custom type fsbgp4mpebgpPeerRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsbgp4mpebgpPeerRemotePort_Type.__name__ = "Integer32"
_Fsbgp4mpebgpPeerRemotePort_Object = MibTableColumn
fsbgp4mpebgpPeerRemotePort = _Fsbgp4mpebgpPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 9),
    _Fsbgp4mpebgpPeerRemotePort_Type()
)
fsbgp4mpebgpPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerRemotePort.setStatus("current")


class _Fsbgp4mpebgpPeerRemoteAs_Type(Unsigned32):
    """Custom type fsbgp4mpebgpPeerRemoteAs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Fsbgp4mpebgpPeerRemoteAs_Type.__name__ = "Unsigned32"
_Fsbgp4mpebgpPeerRemoteAs_Object = MibTableColumn
fsbgp4mpebgpPeerRemoteAs = _Fsbgp4mpebgpPeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 10),
    _Fsbgp4mpebgpPeerRemoteAs_Type()
)
fsbgp4mpebgpPeerRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerRemoteAs.setStatus("current")
_Fsbgp4mpebgpPeerInUpdates_Type = Counter32
_Fsbgp4mpebgpPeerInUpdates_Object = MibTableColumn
fsbgp4mpebgpPeerInUpdates = _Fsbgp4mpebgpPeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 11),
    _Fsbgp4mpebgpPeerInUpdates_Type()
)
fsbgp4mpebgpPeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerInUpdates.setStatus("current")
_Fsbgp4mpebgpPeerOutUpdates_Type = Counter32
_Fsbgp4mpebgpPeerOutUpdates_Object = MibTableColumn
fsbgp4mpebgpPeerOutUpdates = _Fsbgp4mpebgpPeerOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 12),
    _Fsbgp4mpebgpPeerOutUpdates_Type()
)
fsbgp4mpebgpPeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerOutUpdates.setStatus("current")
_Fsbgp4mpebgpPeerInTotalMessages_Type = Counter32
_Fsbgp4mpebgpPeerInTotalMessages_Object = MibTableColumn
fsbgp4mpebgpPeerInTotalMessages = _Fsbgp4mpebgpPeerInTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 13),
    _Fsbgp4mpebgpPeerInTotalMessages_Type()
)
fsbgp4mpebgpPeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerInTotalMessages.setStatus("current")
_Fsbgp4mpebgpPeerOutTotalMessages_Type = Counter32
_Fsbgp4mpebgpPeerOutTotalMessages_Object = MibTableColumn
fsbgp4mpebgpPeerOutTotalMessages = _Fsbgp4mpebgpPeerOutTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 14),
    _Fsbgp4mpebgpPeerOutTotalMessages_Type()
)
fsbgp4mpebgpPeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerOutTotalMessages.setStatus("current")


class _Fsbgp4mpebgpPeerLastError_Type(OctetString):
    """Custom type fsbgp4mpebgpPeerLastError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_Fsbgp4mpebgpPeerLastError_Type.__name__ = "OctetString"
_Fsbgp4mpebgpPeerLastError_Object = MibTableColumn
fsbgp4mpebgpPeerLastError = _Fsbgp4mpebgpPeerLastError_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 15),
    _Fsbgp4mpebgpPeerLastError_Type()
)
fsbgp4mpebgpPeerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerLastError.setStatus("current")
_Fsbgp4mpebgpPeerFsmEstablishedTransitions_Type = Counter32
_Fsbgp4mpebgpPeerFsmEstablishedTransitions_Object = MibTableColumn
fsbgp4mpebgpPeerFsmEstablishedTransitions = _Fsbgp4mpebgpPeerFsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 16),
    _Fsbgp4mpebgpPeerFsmEstablishedTransitions_Type()
)
fsbgp4mpebgpPeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerFsmEstablishedTransitions.setStatus("current")
_Fsbgp4mpebgpPeerFsmEstablishedTime_Type = Gauge32
_Fsbgp4mpebgpPeerFsmEstablishedTime_Object = MibTableColumn
fsbgp4mpebgpPeerFsmEstablishedTime = _Fsbgp4mpebgpPeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 17),
    _Fsbgp4mpebgpPeerFsmEstablishedTime_Type()
)
fsbgp4mpebgpPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerFsmEstablishedTime.setStatus("current")


class _Fsbgp4mpebgpPeerConnectRetryInterval_Type(Integer32):
    """Custom type fsbgp4mpebgpPeerConnectRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Fsbgp4mpebgpPeerConnectRetryInterval_Type.__name__ = "Integer32"
_Fsbgp4mpebgpPeerConnectRetryInterval_Object = MibTableColumn
fsbgp4mpebgpPeerConnectRetryInterval = _Fsbgp4mpebgpPeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 18),
    _Fsbgp4mpebgpPeerConnectRetryInterval_Type()
)
fsbgp4mpebgpPeerConnectRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerConnectRetryInterval.setStatus("current")


class _Fsbgp4mpebgpPeerHoldTime_Type(Integer32):
    """Custom type fsbgp4mpebgpPeerHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_Fsbgp4mpebgpPeerHoldTime_Type.__name__ = "Integer32"
_Fsbgp4mpebgpPeerHoldTime_Object = MibTableColumn
fsbgp4mpebgpPeerHoldTime = _Fsbgp4mpebgpPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 19),
    _Fsbgp4mpebgpPeerHoldTime_Type()
)
fsbgp4mpebgpPeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerHoldTime.setStatus("current")


class _Fsbgp4mpebgpPeerKeepAlive_Type(Integer32):
    """Custom type fsbgp4mpebgpPeerKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_Fsbgp4mpebgpPeerKeepAlive_Type.__name__ = "Integer32"
_Fsbgp4mpebgpPeerKeepAlive_Object = MibTableColumn
fsbgp4mpebgpPeerKeepAlive = _Fsbgp4mpebgpPeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 20),
    _Fsbgp4mpebgpPeerKeepAlive_Type()
)
fsbgp4mpebgpPeerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerKeepAlive.setStatus("current")


class _Fsbgp4mpebgpPeerHoldTimeConfigured_Type(Integer32):
    """Custom type fsbgp4mpebgpPeerHoldTimeConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_Fsbgp4mpebgpPeerHoldTimeConfigured_Type.__name__ = "Integer32"
_Fsbgp4mpebgpPeerHoldTimeConfigured_Object = MibTableColumn
fsbgp4mpebgpPeerHoldTimeConfigured = _Fsbgp4mpebgpPeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 21),
    _Fsbgp4mpebgpPeerHoldTimeConfigured_Type()
)
fsbgp4mpebgpPeerHoldTimeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerHoldTimeConfigured.setStatus("current")


class _Fsbgp4mpebgpPeerKeepAliveConfigured_Type(Integer32):
    """Custom type fsbgp4mpebgpPeerKeepAliveConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_Fsbgp4mpebgpPeerKeepAliveConfigured_Type.__name__ = "Integer32"
_Fsbgp4mpebgpPeerKeepAliveConfigured_Object = MibTableColumn
fsbgp4mpebgpPeerKeepAliveConfigured = _Fsbgp4mpebgpPeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 22),
    _Fsbgp4mpebgpPeerKeepAliveConfigured_Type()
)
fsbgp4mpebgpPeerKeepAliveConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerKeepAliveConfigured.setStatus("current")


class _Fsbgp4mpebgpPeerMinASOriginationInterval_Type(Integer32):
    """Custom type fsbgp4mpebgpPeerMinASOriginationInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Fsbgp4mpebgpPeerMinASOriginationInterval_Type.__name__ = "Integer32"
_Fsbgp4mpebgpPeerMinASOriginationInterval_Object = MibTableColumn
fsbgp4mpebgpPeerMinASOriginationInterval = _Fsbgp4mpebgpPeerMinASOriginationInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 23),
    _Fsbgp4mpebgpPeerMinASOriginationInterval_Type()
)
fsbgp4mpebgpPeerMinASOriginationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerMinASOriginationInterval.setStatus("current")


class _Fsbgp4mpebgpPeerMinRouteAdvertisementInterval_Type(Integer32):
    """Custom type fsbgp4mpebgpPeerMinRouteAdvertisementInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Fsbgp4mpebgpPeerMinRouteAdvertisementInterval_Type.__name__ = "Integer32"
_Fsbgp4mpebgpPeerMinRouteAdvertisementInterval_Object = MibTableColumn
fsbgp4mpebgpPeerMinRouteAdvertisementInterval = _Fsbgp4mpebgpPeerMinRouteAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 24),
    _Fsbgp4mpebgpPeerMinRouteAdvertisementInterval_Type()
)
fsbgp4mpebgpPeerMinRouteAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerMinRouteAdvertisementInterval.setStatus("current")
_Fsbgp4mpebgpPeerInUpdateElapsedTime_Type = Gauge32
_Fsbgp4mpebgpPeerInUpdateElapsedTime_Object = MibTableColumn
fsbgp4mpebgpPeerInUpdateElapsedTime = _Fsbgp4mpebgpPeerInUpdateElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 25),
    _Fsbgp4mpebgpPeerInUpdateElapsedTime_Type()
)
fsbgp4mpebgpPeerInUpdateElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerInUpdateElapsedTime.setStatus("current")


class _Fsbgp4mpebgpPeerEndOfRIBMarkerSentStatus_Type(Integer32):
    """Custom type fsbgp4mpebgpPeerEndOfRIBMarkerSentStatus based on Integer32"""
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


_Fsbgp4mpebgpPeerEndOfRIBMarkerSentStatus_Type.__name__ = "Integer32"
_Fsbgp4mpebgpPeerEndOfRIBMarkerSentStatus_Object = MibTableColumn
fsbgp4mpebgpPeerEndOfRIBMarkerSentStatus = _Fsbgp4mpebgpPeerEndOfRIBMarkerSentStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 26),
    _Fsbgp4mpebgpPeerEndOfRIBMarkerSentStatus_Type()
)
fsbgp4mpebgpPeerEndOfRIBMarkerSentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerEndOfRIBMarkerSentStatus.setStatus("current")


class _Fsbgp4mpebgpPeerEndOfRIBMarkerReceivedStatus_Type(Integer32):
    """Custom type fsbgp4mpebgpPeerEndOfRIBMarkerReceivedStatus based on Integer32"""
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


_Fsbgp4mpebgpPeerEndOfRIBMarkerReceivedStatus_Type.__name__ = "Integer32"
_Fsbgp4mpebgpPeerEndOfRIBMarkerReceivedStatus_Object = MibTableColumn
fsbgp4mpebgpPeerEndOfRIBMarkerReceivedStatus = _Fsbgp4mpebgpPeerEndOfRIBMarkerReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 27),
    _Fsbgp4mpebgpPeerEndOfRIBMarkerReceivedStatus_Type()
)
fsbgp4mpebgpPeerEndOfRIBMarkerReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerEndOfRIBMarkerReceivedStatus.setStatus("current")


class _Fsbgp4mpebgpPeerRestartMode_Type(Integer32):
    """Custom type fsbgp4mpebgpPeerRestartMode based on Integer32"""
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


_Fsbgp4mpebgpPeerRestartMode_Type.__name__ = "Integer32"
_Fsbgp4mpebgpPeerRestartMode_Object = MibTableColumn
fsbgp4mpebgpPeerRestartMode = _Fsbgp4mpebgpPeerRestartMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 28),
    _Fsbgp4mpebgpPeerRestartMode_Type()
)
fsbgp4mpebgpPeerRestartMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerRestartMode.setStatus("current")


class _Fsbgp4mpePeerRestartTimeInterval_Type(Integer32):
    """Custom type fsbgp4mpePeerRestartTimeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Fsbgp4mpePeerRestartTimeInterval_Type.__name__ = "Integer32"
_Fsbgp4mpePeerRestartTimeInterval_Object = MibTableColumn
fsbgp4mpePeerRestartTimeInterval = _Fsbgp4mpePeerRestartTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 29),
    _Fsbgp4mpePeerRestartTimeInterval_Type()
)
fsbgp4mpePeerRestartTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpePeerRestartTimeInterval.setStatus("current")


class _Fsbgp4mpePeerAllowAutomaticStart_Type(Integer32):
    """Custom type fsbgp4mpePeerAllowAutomaticStart based on Integer32"""
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


_Fsbgp4mpePeerAllowAutomaticStart_Type.__name__ = "Integer32"
_Fsbgp4mpePeerAllowAutomaticStart_Object = MibTableColumn
fsbgp4mpePeerAllowAutomaticStart = _Fsbgp4mpePeerAllowAutomaticStart_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 30),
    _Fsbgp4mpePeerAllowAutomaticStart_Type()
)
fsbgp4mpePeerAllowAutomaticStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerAllowAutomaticStart.setStatus("current")


class _Fsbgp4mpePeerAllowAutomaticStop_Type(Integer32):
    """Custom type fsbgp4mpePeerAllowAutomaticStop based on Integer32"""
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


_Fsbgp4mpePeerAllowAutomaticStop_Type.__name__ = "Integer32"
_Fsbgp4mpePeerAllowAutomaticStop_Object = MibTableColumn
fsbgp4mpePeerAllowAutomaticStop = _Fsbgp4mpePeerAllowAutomaticStop_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 31),
    _Fsbgp4mpePeerAllowAutomaticStop_Type()
)
fsbgp4mpePeerAllowAutomaticStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerAllowAutomaticStop.setStatus("current")


class _Fsbgp4mpebgpPeerIdleHoldTimeConfigured_Type(Integer32):
    """Custom type fsbgp4mpebgpPeerIdleHoldTimeConfigured based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Fsbgp4mpebgpPeerIdleHoldTimeConfigured_Type.__name__ = "Integer32"
_Fsbgp4mpebgpPeerIdleHoldTimeConfigured_Object = MibTableColumn
fsbgp4mpebgpPeerIdleHoldTimeConfigured = _Fsbgp4mpebgpPeerIdleHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 32),
    _Fsbgp4mpebgpPeerIdleHoldTimeConfigured_Type()
)
fsbgp4mpebgpPeerIdleHoldTimeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerIdleHoldTimeConfigured.setStatus("current")


class _Fsbgp4mpeDampPeerOscillations_Type(Integer32):
    """Custom type fsbgp4mpeDampPeerOscillations based on Integer32"""
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


_Fsbgp4mpeDampPeerOscillations_Type.__name__ = "Integer32"
_Fsbgp4mpeDampPeerOscillations_Object = MibTableColumn
fsbgp4mpeDampPeerOscillations = _Fsbgp4mpeDampPeerOscillations_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 33),
    _Fsbgp4mpeDampPeerOscillations_Type()
)
fsbgp4mpeDampPeerOscillations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeDampPeerOscillations.setStatus("current")


class _Fsbgp4mpePeerDelayOpen_Type(Integer32):
    """Custom type fsbgp4mpePeerDelayOpen based on Integer32"""
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


_Fsbgp4mpePeerDelayOpen_Type.__name__ = "Integer32"
_Fsbgp4mpePeerDelayOpen_Object = MibTableColumn
fsbgp4mpePeerDelayOpen = _Fsbgp4mpePeerDelayOpen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 34),
    _Fsbgp4mpePeerDelayOpen_Type()
)
fsbgp4mpePeerDelayOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerDelayOpen.setStatus("current")


class _Fsbgp4mpebgpPeerDelayOpenTimeConfigured_Type(Integer32):
    """Custom type fsbgp4mpebgpPeerDelayOpenTimeConfigured based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsbgp4mpebgpPeerDelayOpenTimeConfigured_Type.__name__ = "Integer32"
_Fsbgp4mpebgpPeerDelayOpenTimeConfigured_Object = MibTableColumn
fsbgp4mpebgpPeerDelayOpenTimeConfigured = _Fsbgp4mpebgpPeerDelayOpenTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 35),
    _Fsbgp4mpebgpPeerDelayOpenTimeConfigured_Type()
)
fsbgp4mpebgpPeerDelayOpenTimeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerDelayOpenTimeConfigured.setStatus("current")


class _Fsbgp4mpePeerPrefixUpperLimit_Type(Integer32):
    """Custom type fsbgp4mpePeerPrefixUpperLimit based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsbgp4mpePeerPrefixUpperLimit_Type.__name__ = "Integer32"
_Fsbgp4mpePeerPrefixUpperLimit_Object = MibTableColumn
fsbgp4mpePeerPrefixUpperLimit = _Fsbgp4mpePeerPrefixUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 36),
    _Fsbgp4mpePeerPrefixUpperLimit_Type()
)
fsbgp4mpePeerPrefixUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerPrefixUpperLimit.setStatus("current")


class _Fsbgp4mpePeerTcpConnectRetryCnt_Type(Integer32):
    """Custom type fsbgp4mpePeerTcpConnectRetryCnt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_Fsbgp4mpePeerTcpConnectRetryCnt_Type.__name__ = "Integer32"
_Fsbgp4mpePeerTcpConnectRetryCnt_Object = MibTableColumn
fsbgp4mpePeerTcpConnectRetryCnt = _Fsbgp4mpePeerTcpConnectRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 37),
    _Fsbgp4mpePeerTcpConnectRetryCnt_Type()
)
fsbgp4mpePeerTcpConnectRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerTcpConnectRetryCnt.setStatus("current")


class _Fsbgp4mpePeerTcpCurrentConnectRetryCnt_Type(Integer32):
    """Custom type fsbgp4mpePeerTcpCurrentConnectRetryCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_Fsbgp4mpePeerTcpCurrentConnectRetryCnt_Type.__name__ = "Integer32"
_Fsbgp4mpePeerTcpCurrentConnectRetryCnt_Object = MibTableColumn
fsbgp4mpePeerTcpCurrentConnectRetryCnt = _Fsbgp4mpePeerTcpCurrentConnectRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 38),
    _Fsbgp4mpePeerTcpCurrentConnectRetryCnt_Type()
)
fsbgp4mpePeerTcpCurrentConnectRetryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpePeerTcpCurrentConnectRetryCnt.setStatus("current")


class _Fsbgp4mpeIsPeerDamped_Type(Integer32):
    """Custom type fsbgp4mpeIsPeerDamped based on Integer32"""
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


_Fsbgp4mpeIsPeerDamped_Type.__name__ = "Integer32"
_Fsbgp4mpeIsPeerDamped_Object = MibTableColumn
fsbgp4mpeIsPeerDamped = _Fsbgp4mpeIsPeerDamped_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 39),
    _Fsbgp4mpeIsPeerDamped_Type()
)
fsbgp4mpeIsPeerDamped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeIsPeerDamped.setStatus("current")


class _Fsbgp4mpePeerSessionAuthStatus_Type(Integer32):
    """Custom type fsbgp4mpePeerSessionAuthStatus based on Integer32"""
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
        *(("no-session", 1),
          ("authenticatedMd5", 2),
          ("unauthenticated", 3),
          ("authenticatedTcpAo", 4))
    )


_Fsbgp4mpePeerSessionAuthStatus_Type.__name__ = "Integer32"
_Fsbgp4mpePeerSessionAuthStatus_Object = MibTableColumn
fsbgp4mpePeerSessionAuthStatus = _Fsbgp4mpePeerSessionAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 40),
    _Fsbgp4mpePeerSessionAuthStatus_Type()
)
fsbgp4mpePeerSessionAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpePeerSessionAuthStatus.setStatus("current")


class _Fsbgp4mpePeerTCPAOKeyIdInUse_Type(Integer32):
    """Custom type fsbgp4mpePeerTCPAOKeyIdInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fsbgp4mpePeerTCPAOKeyIdInUse_Type.__name__ = "Integer32"
_Fsbgp4mpePeerTCPAOKeyIdInUse_Object = MibTableColumn
fsbgp4mpePeerTCPAOKeyIdInUse = _Fsbgp4mpePeerTCPAOKeyIdInUse_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 41),
    _Fsbgp4mpePeerTCPAOKeyIdInUse_Type()
)
fsbgp4mpePeerTCPAOKeyIdInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpePeerTCPAOKeyIdInUse.setStatus("current")


class _Fsbgp4mpePeerTCPAOAuthNoMKTDiscard_Type(Integer32):
    """Custom type fsbgp4mpePeerTCPAOAuthNoMKTDiscard based on Integer32"""
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


_Fsbgp4mpePeerTCPAOAuthNoMKTDiscard_Type.__name__ = "Integer32"
_Fsbgp4mpePeerTCPAOAuthNoMKTDiscard_Object = MibTableColumn
fsbgp4mpePeerTCPAOAuthNoMKTDiscard = _Fsbgp4mpePeerTCPAOAuthNoMKTDiscard_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 42),
    _Fsbgp4mpePeerTCPAOAuthNoMKTDiscard_Type()
)
fsbgp4mpePeerTCPAOAuthNoMKTDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerTCPAOAuthNoMKTDiscard.setStatus("current")


class _Fsbgp4mpePeerTCPAOAuthICMPAccept_Type(Integer32):
    """Custom type fsbgp4mpePeerTCPAOAuthICMPAccept based on Integer32"""
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


_Fsbgp4mpePeerTCPAOAuthICMPAccept_Type.__name__ = "Integer32"
_Fsbgp4mpePeerTCPAOAuthICMPAccept_Object = MibTableColumn
fsbgp4mpePeerTCPAOAuthICMPAccept = _Fsbgp4mpePeerTCPAOAuthICMPAccept_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 43),
    _Fsbgp4mpePeerTCPAOAuthICMPAccept_Type()
)
fsbgp4mpePeerTCPAOAuthICMPAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerTCPAOAuthICMPAccept.setStatus("current")
_Fsbgp4mpePeerIpPrefixNameIn_Type = DisplayString
_Fsbgp4mpePeerIpPrefixNameIn_Object = MibTableColumn
fsbgp4mpePeerIpPrefixNameIn = _Fsbgp4mpePeerIpPrefixNameIn_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 44),
    _Fsbgp4mpePeerIpPrefixNameIn_Type()
)
fsbgp4mpePeerIpPrefixNameIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerIpPrefixNameIn.setStatus("current")
_Fsbgp4mpePeerIpPrefixNameOut_Type = DisplayString
_Fsbgp4mpePeerIpPrefixNameOut_Object = MibTableColumn
fsbgp4mpePeerIpPrefixNameOut = _Fsbgp4mpePeerIpPrefixNameOut_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 45),
    _Fsbgp4mpePeerIpPrefixNameOut_Type()
)
fsbgp4mpePeerIpPrefixNameOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerIpPrefixNameOut.setStatus("current")


class _Fsbgp4mpePeerBfdStatus_Type(Integer32):
    """Custom type fsbgp4mpePeerBfdStatus based on Integer32"""
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


_Fsbgp4mpePeerBfdStatus_Type.__name__ = "Integer32"
_Fsbgp4mpePeerBfdStatus_Object = MibTableColumn
fsbgp4mpePeerBfdStatus = _Fsbgp4mpePeerBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 46),
    _Fsbgp4mpePeerBfdStatus_Type()
)
fsbgp4mpePeerBfdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerBfdStatus.setStatus("current")


class _Fsbgp4mpebgpPeerHoldAdvtRoutes_Type(Integer32):
    """Custom type fsbgp4mpebgpPeerHoldAdvtRoutes based on Integer32"""
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


_Fsbgp4mpebgpPeerHoldAdvtRoutes_Type.__name__ = "Integer32"
_Fsbgp4mpebgpPeerHoldAdvtRoutes_Object = MibTableColumn
fsbgp4mpebgpPeerHoldAdvtRoutes = _Fsbgp4mpebgpPeerHoldAdvtRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 19, 1, 47),
    _Fsbgp4mpebgpPeerHoldAdvtRoutes_Type()
)
fsbgp4mpebgpPeerHoldAdvtRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpebgpPeerHoldAdvtRoutes.setStatus("current")
_Fsbgp4MpeBgp4PathAttrTable_Object = MibTable
fsbgp4MpeBgp4PathAttrTable = _Fsbgp4MpeBgp4PathAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20)
)
if mibBuilder.loadTexts:
    fsbgp4MpeBgp4PathAttrTable.setStatus("current")
_Fsbgp4MpeBgp4PathAttrEntry_Object = MibTableRow
fsbgp4MpeBgp4PathAttrEntry = _Fsbgp4MpeBgp4PathAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1)
)
fsbgp4MpeBgp4PathAttrEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpebgp4PathAttrRouteAfi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpebgp4PathAttrRouteSafi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpebgp4PathAttrIpAddrPrefix"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpebgp4PathAttrIpAddrPrefixLen"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpebgp4PathAttrPeerType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpebgp4PathAttrPeer"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeBgp4PathAttrEntry.setStatus("current")
_Fsbgp4mpebgp4PathAttrRouteAfi_Type = InetAddressType
_Fsbgp4mpebgp4PathAttrRouteAfi_Object = MibTableColumn
fsbgp4mpebgp4PathAttrRouteAfi = _Fsbgp4mpebgp4PathAttrRouteAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 1),
    _Fsbgp4mpebgp4PathAttrRouteAfi_Type()
)
fsbgp4mpebgp4PathAttrRouteAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrRouteAfi.setStatus("current")
_Fsbgp4mpebgp4PathAttrRouteSafi_Type = BgpSafi
_Fsbgp4mpebgp4PathAttrRouteSafi_Object = MibTableColumn
fsbgp4mpebgp4PathAttrRouteSafi = _Fsbgp4mpebgp4PathAttrRouteSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 2),
    _Fsbgp4mpebgp4PathAttrRouteSafi_Type()
)
fsbgp4mpebgp4PathAttrRouteSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrRouteSafi.setStatus("current")
_Fsbgp4mpebgp4PathAttrPeerType_Type = InetAddressType
_Fsbgp4mpebgp4PathAttrPeerType_Object = MibTableColumn
fsbgp4mpebgp4PathAttrPeerType = _Fsbgp4mpebgp4PathAttrPeerType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 3),
    _Fsbgp4mpebgp4PathAttrPeerType_Type()
)
fsbgp4mpebgp4PathAttrPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrPeerType.setStatus("current")
_Fsbgp4mpebgp4PathAttrPeer_Type = InetAddress
_Fsbgp4mpebgp4PathAttrPeer_Object = MibTableColumn
fsbgp4mpebgp4PathAttrPeer = _Fsbgp4mpebgp4PathAttrPeer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 4),
    _Fsbgp4mpebgp4PathAttrPeer_Type()
)
fsbgp4mpebgp4PathAttrPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrPeer.setStatus("current")


class _Fsbgp4mpebgp4PathAttrIpAddrPrefixLen_Type(Integer32):
    """Custom type fsbgp4mpebgp4PathAttrIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Fsbgp4mpebgp4PathAttrIpAddrPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4mpebgp4PathAttrIpAddrPrefixLen_Object = MibTableColumn
fsbgp4mpebgp4PathAttrIpAddrPrefixLen = _Fsbgp4mpebgp4PathAttrIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 5),
    _Fsbgp4mpebgp4PathAttrIpAddrPrefixLen_Type()
)
fsbgp4mpebgp4PathAttrIpAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrIpAddrPrefixLen.setStatus("current")
_Fsbgp4mpebgp4PathAttrIpAddrPrefix_Type = InetAddress
_Fsbgp4mpebgp4PathAttrIpAddrPrefix_Object = MibTableColumn
fsbgp4mpebgp4PathAttrIpAddrPrefix = _Fsbgp4mpebgp4PathAttrIpAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 6),
    _Fsbgp4mpebgp4PathAttrIpAddrPrefix_Type()
)
fsbgp4mpebgp4PathAttrIpAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrIpAddrPrefix.setStatus("current")


class _Fsbgp4mpebgp4PathAttrOrigin_Type(Integer32):
    """Custom type fsbgp4mpebgp4PathAttrOrigin based on Integer32"""
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


_Fsbgp4mpebgp4PathAttrOrigin_Type.__name__ = "Integer32"
_Fsbgp4mpebgp4PathAttrOrigin_Object = MibTableColumn
fsbgp4mpebgp4PathAttrOrigin = _Fsbgp4mpebgp4PathAttrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 7),
    _Fsbgp4mpebgp4PathAttrOrigin_Type()
)
fsbgp4mpebgp4PathAttrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrOrigin.setStatus("current")


class _Fsbgp4mpebgp4PathAttrASPathSegment_Type(OctetString):
    """Custom type fsbgp4mpebgp4PathAttrASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_Fsbgp4mpebgp4PathAttrASPathSegment_Type.__name__ = "OctetString"
_Fsbgp4mpebgp4PathAttrASPathSegment_Object = MibTableColumn
fsbgp4mpebgp4PathAttrASPathSegment = _Fsbgp4mpebgp4PathAttrASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 8),
    _Fsbgp4mpebgp4PathAttrASPathSegment_Type()
)
fsbgp4mpebgp4PathAttrASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrASPathSegment.setStatus("current")
_Fsbgp4mpebgp4PathAttrNextHop_Type = InetAddress
_Fsbgp4mpebgp4PathAttrNextHop_Object = MibTableColumn
fsbgp4mpebgp4PathAttrNextHop = _Fsbgp4mpebgp4PathAttrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 9),
    _Fsbgp4mpebgp4PathAttrNextHop_Type()
)
fsbgp4mpebgp4PathAttrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrNextHop.setStatus("current")


class _Fsbgp4mpebgp4PathAttrMultiExitDisc_Type(Integer32):
    """Custom type fsbgp4mpebgp4PathAttrMultiExitDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Fsbgp4mpebgp4PathAttrMultiExitDisc_Type.__name__ = "Integer32"
_Fsbgp4mpebgp4PathAttrMultiExitDisc_Object = MibTableColumn
fsbgp4mpebgp4PathAttrMultiExitDisc = _Fsbgp4mpebgp4PathAttrMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 10),
    _Fsbgp4mpebgp4PathAttrMultiExitDisc_Type()
)
fsbgp4mpebgp4PathAttrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrMultiExitDisc.setStatus("current")


class _Fsbgp4mpebgp4PathAttrLocalPref_Type(Integer32):
    """Custom type fsbgp4mpebgp4PathAttrLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Fsbgp4mpebgp4PathAttrLocalPref_Type.__name__ = "Integer32"
_Fsbgp4mpebgp4PathAttrLocalPref_Object = MibTableColumn
fsbgp4mpebgp4PathAttrLocalPref = _Fsbgp4mpebgp4PathAttrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 11),
    _Fsbgp4mpebgp4PathAttrLocalPref_Type()
)
fsbgp4mpebgp4PathAttrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrLocalPref.setStatus("current")


class _Fsbgp4mpebgp4PathAttrAtomicAggregate_Type(Integer32):
    """Custom type fsbgp4mpebgp4PathAttrAtomicAggregate based on Integer32"""
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


_Fsbgp4mpebgp4PathAttrAtomicAggregate_Type.__name__ = "Integer32"
_Fsbgp4mpebgp4PathAttrAtomicAggregate_Object = MibTableColumn
fsbgp4mpebgp4PathAttrAtomicAggregate = _Fsbgp4mpebgp4PathAttrAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 12),
    _Fsbgp4mpebgp4PathAttrAtomicAggregate_Type()
)
fsbgp4mpebgp4PathAttrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrAtomicAggregate.setStatus("current")


class _Fsbgp4mpebgp4PathAttrAggregatorAS_Type(Unsigned32):
    """Custom type fsbgp4mpebgp4PathAttrAggregatorAS based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Fsbgp4mpebgp4PathAttrAggregatorAS_Type.__name__ = "Unsigned32"
_Fsbgp4mpebgp4PathAttrAggregatorAS_Object = MibTableColumn
fsbgp4mpebgp4PathAttrAggregatorAS = _Fsbgp4mpebgp4PathAttrAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 13),
    _Fsbgp4mpebgp4PathAttrAggregatorAS_Type()
)
fsbgp4mpebgp4PathAttrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrAggregatorAS.setStatus("current")
_Fsbgp4mpebgp4PathAttrAggregatorAddr_Type = IpAddress
_Fsbgp4mpebgp4PathAttrAggregatorAddr_Object = MibTableColumn
fsbgp4mpebgp4PathAttrAggregatorAddr = _Fsbgp4mpebgp4PathAttrAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 14),
    _Fsbgp4mpebgp4PathAttrAggregatorAddr_Type()
)
fsbgp4mpebgp4PathAttrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrAggregatorAddr.setStatus("current")


class _Fsbgp4mpebgp4PathAttrCalcLocalPref_Type(Integer32):
    """Custom type fsbgp4mpebgp4PathAttrCalcLocalPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Fsbgp4mpebgp4PathAttrCalcLocalPref_Type.__name__ = "Integer32"
_Fsbgp4mpebgp4PathAttrCalcLocalPref_Object = MibTableColumn
fsbgp4mpebgp4PathAttrCalcLocalPref = _Fsbgp4mpebgp4PathAttrCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 15),
    _Fsbgp4mpebgp4PathAttrCalcLocalPref_Type()
)
fsbgp4mpebgp4PathAttrCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrCalcLocalPref.setStatus("current")


class _Fsbgp4mpebgp4PathAttrBest_Type(Integer32):
    """Custom type fsbgp4mpebgp4PathAttrBest based on Integer32"""
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


_Fsbgp4mpebgp4PathAttrBest_Type.__name__ = "Integer32"
_Fsbgp4mpebgp4PathAttrBest_Object = MibTableColumn
fsbgp4mpebgp4PathAttrBest = _Fsbgp4mpebgp4PathAttrBest_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 16),
    _Fsbgp4mpebgp4PathAttrBest_Type()
)
fsbgp4mpebgp4PathAttrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrBest.setStatus("current")


class _Fsbgp4mpebgp4PathAttrCommunity_Type(OctetString):
    """Custom type fsbgp4mpebgp4PathAttrCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 800),
    )


_Fsbgp4mpebgp4PathAttrCommunity_Type.__name__ = "OctetString"
_Fsbgp4mpebgp4PathAttrCommunity_Object = MibTableColumn
fsbgp4mpebgp4PathAttrCommunity = _Fsbgp4mpebgp4PathAttrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 17),
    _Fsbgp4mpebgp4PathAttrCommunity_Type()
)
fsbgp4mpebgp4PathAttrCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrCommunity.setStatus("current")


class _Fsbgp4mpebgp4PathAttrOriginatorId_Type(OctetString):
    """Custom type fsbgp4mpebgp4PathAttrOriginatorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Fsbgp4mpebgp4PathAttrOriginatorId_Type.__name__ = "OctetString"
_Fsbgp4mpebgp4PathAttrOriginatorId_Object = MibTableColumn
fsbgp4mpebgp4PathAttrOriginatorId = _Fsbgp4mpebgp4PathAttrOriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 18),
    _Fsbgp4mpebgp4PathAttrOriginatorId_Type()
)
fsbgp4mpebgp4PathAttrOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrOriginatorId.setStatus("current")


class _Fsbgp4mpebgp4PathAttrClusterList_Type(OctetString):
    """Custom type fsbgp4mpebgp4PathAttrClusterList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_Fsbgp4mpebgp4PathAttrClusterList_Type.__name__ = "OctetString"
_Fsbgp4mpebgp4PathAttrClusterList_Object = MibTableColumn
fsbgp4mpebgp4PathAttrClusterList = _Fsbgp4mpebgp4PathAttrClusterList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 19),
    _Fsbgp4mpebgp4PathAttrClusterList_Type()
)
fsbgp4mpebgp4PathAttrClusterList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrClusterList.setStatus("current")


class _Fsbgp4mpebgp4PathAttrExtCommunity_Type(OctetString):
    """Custom type fsbgp4mpebgp4PathAttrExtCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 800),
    )


_Fsbgp4mpebgp4PathAttrExtCommunity_Type.__name__ = "OctetString"
_Fsbgp4mpebgp4PathAttrExtCommunity_Object = MibTableColumn
fsbgp4mpebgp4PathAttrExtCommunity = _Fsbgp4mpebgp4PathAttrExtCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 20),
    _Fsbgp4mpebgp4PathAttrExtCommunity_Type()
)
fsbgp4mpebgp4PathAttrExtCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrExtCommunity.setStatus("current")


class _Fsbgp4mpebgp4PathAttrUnknown_Type(OctetString):
    """Custom type fsbgp4mpebgp4PathAttrUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Fsbgp4mpebgp4PathAttrUnknown_Type.__name__ = "OctetString"
_Fsbgp4mpebgp4PathAttrUnknown_Object = MibTableColumn
fsbgp4mpebgp4PathAttrUnknown = _Fsbgp4mpebgp4PathAttrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 21),
    _Fsbgp4mpebgp4PathAttrUnknown_Type()
)
fsbgp4mpebgp4PathAttrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrUnknown.setStatus("current")


class _Fsbgp4mpebgp4PathAttrLabel_Type(OctetString):
    """Custom type fsbgp4mpebgp4PathAttrLabel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Fsbgp4mpebgp4PathAttrLabel_Type.__name__ = "OctetString"
_Fsbgp4mpebgp4PathAttrLabel_Object = MibTableColumn
fsbgp4mpebgp4PathAttrLabel = _Fsbgp4mpebgp4PathAttrLabel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 22),
    _Fsbgp4mpebgp4PathAttrLabel_Type()
)
fsbgp4mpebgp4PathAttrLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrLabel.setStatus("current")


class _Fsbgp4mpebgp4PathAttrAS4PathSegment_Type(OctetString):
    """Custom type fsbgp4mpebgp4PathAttrAS4PathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_Fsbgp4mpebgp4PathAttrAS4PathSegment_Type.__name__ = "OctetString"
_Fsbgp4mpebgp4PathAttrAS4PathSegment_Object = MibTableColumn
fsbgp4mpebgp4PathAttrAS4PathSegment = _Fsbgp4mpebgp4PathAttrAS4PathSegment_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 23),
    _Fsbgp4mpebgp4PathAttrAS4PathSegment_Type()
)
fsbgp4mpebgp4PathAttrAS4PathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrAS4PathSegment.setStatus("current")


class _Fsbgp4mpebgp4PathAttrAggregatorAS4_Type(Unsigned32):
    """Custom type fsbgp4mpebgp4PathAttrAggregatorAS4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Fsbgp4mpebgp4PathAttrAggregatorAS4_Type.__name__ = "Unsigned32"
_Fsbgp4mpebgp4PathAttrAggregatorAS4_Object = MibTableColumn
fsbgp4mpebgp4PathAttrAggregatorAS4 = _Fsbgp4mpebgp4PathAttrAggregatorAS4_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 20, 1, 24),
    _Fsbgp4mpebgp4PathAttrAggregatorAS4_Type()
)
fsbgp4mpebgp4PathAttrAggregatorAS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpebgp4PathAttrAggregatorAS4.setStatus("current")
_Fsbgp4MpePeerExtTable_Object = MibTable
fsbgp4MpePeerExtTable = _Fsbgp4MpePeerExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21)
)
if mibBuilder.loadTexts:
    fsbgp4MpePeerExtTable.setStatus("current")
_Fsbgp4MpePeerExtEntry_Object = MibTableRow
fsbgp4MpePeerExtEntry = _Fsbgp4MpePeerExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1)
)
fsbgp4MpePeerExtEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpePeerExtPeerType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpePeerExtPeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    fsbgp4MpePeerExtEntry.setStatus("current")
_Fsbgp4mpePeerExtPeerType_Type = InetAddressType
_Fsbgp4mpePeerExtPeerType_Object = MibTableColumn
fsbgp4mpePeerExtPeerType = _Fsbgp4mpePeerExtPeerType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 1),
    _Fsbgp4mpePeerExtPeerType_Type()
)
fsbgp4mpePeerExtPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtPeerType.setStatus("current")
_Fsbgp4mpePeerExtPeerRemoteAddr_Type = InetAddress
_Fsbgp4mpePeerExtPeerRemoteAddr_Object = MibTableColumn
fsbgp4mpePeerExtPeerRemoteAddr = _Fsbgp4mpePeerExtPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 2),
    _Fsbgp4mpePeerExtPeerRemoteAddr_Type()
)
fsbgp4mpePeerExtPeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtPeerRemoteAddr.setStatus("current")


class _Fsbgp4mpePeerExtConfigurePeer_Type(Integer32):
    """Custom type fsbgp4mpePeerExtConfigurePeer based on Integer32"""
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


_Fsbgp4mpePeerExtConfigurePeer_Type.__name__ = "Integer32"
_Fsbgp4mpePeerExtConfigurePeer_Object = MibTableColumn
fsbgp4mpePeerExtConfigurePeer = _Fsbgp4mpePeerExtConfigurePeer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 3),
    _Fsbgp4mpePeerExtConfigurePeer_Type()
)
fsbgp4mpePeerExtConfigurePeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtConfigurePeer.setStatus("current")


class _Fsbgp4mpePeerExtPeerRemoteAs_Type(Unsigned32):
    """Custom type fsbgp4mpePeerExtPeerRemoteAs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Fsbgp4mpePeerExtPeerRemoteAs_Type.__name__ = "Unsigned32"
_Fsbgp4mpePeerExtPeerRemoteAs_Object = MibTableColumn
fsbgp4mpePeerExtPeerRemoteAs = _Fsbgp4mpePeerExtPeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 4),
    _Fsbgp4mpePeerExtPeerRemoteAs_Type()
)
fsbgp4mpePeerExtPeerRemoteAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtPeerRemoteAs.setStatus("current")


class _Fsbgp4mpePeerExtEBGPMultiHop_Type(Integer32):
    """Custom type fsbgp4mpePeerExtEBGPMultiHop based on Integer32"""
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


_Fsbgp4mpePeerExtEBGPMultiHop_Type.__name__ = "Integer32"
_Fsbgp4mpePeerExtEBGPMultiHop_Object = MibTableColumn
fsbgp4mpePeerExtEBGPMultiHop = _Fsbgp4mpePeerExtEBGPMultiHop_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 5),
    _Fsbgp4mpePeerExtEBGPMultiHop_Type()
)
fsbgp4mpePeerExtEBGPMultiHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtEBGPMultiHop.setStatus("current")


class _Fsbgp4mpePeerExtEBGPHopLimit_Type(Integer32):
    """Custom type fsbgp4mpePeerExtEBGPHopLimit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Fsbgp4mpePeerExtEBGPHopLimit_Type.__name__ = "Integer32"
_Fsbgp4mpePeerExtEBGPHopLimit_Object = MibTableColumn
fsbgp4mpePeerExtEBGPHopLimit = _Fsbgp4mpePeerExtEBGPHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 6),
    _Fsbgp4mpePeerExtEBGPHopLimit_Type()
)
fsbgp4mpePeerExtEBGPHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtEBGPHopLimit.setStatus("current")


class _Fsbgp4mpePeerExtNextHopSelf_Type(Integer32):
    """Custom type fsbgp4mpePeerExtNextHopSelf based on Integer32"""
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


_Fsbgp4mpePeerExtNextHopSelf_Type.__name__ = "Integer32"
_Fsbgp4mpePeerExtNextHopSelf_Object = MibTableColumn
fsbgp4mpePeerExtNextHopSelf = _Fsbgp4mpePeerExtNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 7),
    _Fsbgp4mpePeerExtNextHopSelf_Type()
)
fsbgp4mpePeerExtNextHopSelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtNextHopSelf.setStatus("current")


class _Fsbgp4mpePeerExtRflClient_Type(Integer32):
    """Custom type fsbgp4mpePeerExtRflClient based on Integer32"""
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


_Fsbgp4mpePeerExtRflClient_Type.__name__ = "Integer32"
_Fsbgp4mpePeerExtRflClient_Object = MibTableColumn
fsbgp4mpePeerExtRflClient = _Fsbgp4mpePeerExtRflClient_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 8),
    _Fsbgp4mpePeerExtRflClient_Type()
)
fsbgp4mpePeerExtRflClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtRflClient.setStatus("current")


class _Fsbgp4mpePeerExtTcpSendBufSize_Type(Integer32):
    """Custom type fsbgp4mpePeerExtTcpSendBufSize based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 65536),
    )


_Fsbgp4mpePeerExtTcpSendBufSize_Type.__name__ = "Integer32"
_Fsbgp4mpePeerExtTcpSendBufSize_Object = MibTableColumn
fsbgp4mpePeerExtTcpSendBufSize = _Fsbgp4mpePeerExtTcpSendBufSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 9),
    _Fsbgp4mpePeerExtTcpSendBufSize_Type()
)
fsbgp4mpePeerExtTcpSendBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtTcpSendBufSize.setStatus("current")


class _Fsbgp4mpePeerExtTcpRcvBufSize_Type(Integer32):
    """Custom type fsbgp4mpePeerExtTcpRcvBufSize based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 65536),
    )


_Fsbgp4mpePeerExtTcpRcvBufSize_Type.__name__ = "Integer32"
_Fsbgp4mpePeerExtTcpRcvBufSize_Object = MibTableColumn
fsbgp4mpePeerExtTcpRcvBufSize = _Fsbgp4mpePeerExtTcpRcvBufSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 10),
    _Fsbgp4mpePeerExtTcpRcvBufSize_Type()
)
fsbgp4mpePeerExtTcpRcvBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtTcpRcvBufSize.setStatus("current")
_Fsbgp4mpePeerExtLclAddress_Type = InetAddress
_Fsbgp4mpePeerExtLclAddress_Object = MibTableColumn
fsbgp4mpePeerExtLclAddress = _Fsbgp4mpePeerExtLclAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 11),
    _Fsbgp4mpePeerExtLclAddress_Type()
)
fsbgp4mpePeerExtLclAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtLclAddress.setStatus("current")
_Fsbgp4mpePeerExtNetworkAddress_Type = InetAddress
_Fsbgp4mpePeerExtNetworkAddress_Object = MibTableColumn
fsbgp4mpePeerExtNetworkAddress = _Fsbgp4mpePeerExtNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 12),
    _Fsbgp4mpePeerExtNetworkAddress_Type()
)
fsbgp4mpePeerExtNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtNetworkAddress.setStatus("current")
_Fsbgp4mpePeerExtGateway_Type = InetAddress
_Fsbgp4mpePeerExtGateway_Object = MibTableColumn
fsbgp4mpePeerExtGateway = _Fsbgp4mpePeerExtGateway_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 13),
    _Fsbgp4mpePeerExtGateway_Type()
)
fsbgp4mpePeerExtGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtGateway.setStatus("current")


class _Fsbgp4mpePeerExtCommSendStatus_Type(Integer32):
    """Custom type fsbgp4mpePeerExtCommSendStatus based on Integer32"""
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


_Fsbgp4mpePeerExtCommSendStatus_Type.__name__ = "Integer32"
_Fsbgp4mpePeerExtCommSendStatus_Object = MibTableColumn
fsbgp4mpePeerExtCommSendStatus = _Fsbgp4mpePeerExtCommSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 14),
    _Fsbgp4mpePeerExtCommSendStatus_Type()
)
fsbgp4mpePeerExtCommSendStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtCommSendStatus.setStatus("current")


class _Fsbgp4mpePeerExtECommSendStatus_Type(Integer32):
    """Custom type fsbgp4mpePeerExtECommSendStatus based on Integer32"""
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


_Fsbgp4mpePeerExtECommSendStatus_Type.__name__ = "Integer32"
_Fsbgp4mpePeerExtECommSendStatus_Object = MibTableColumn
fsbgp4mpePeerExtECommSendStatus = _Fsbgp4mpePeerExtECommSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 15),
    _Fsbgp4mpePeerExtECommSendStatus_Type()
)
fsbgp4mpePeerExtECommSendStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtECommSendStatus.setStatus("current")


class _Fsbgp4mpePeerExtPassive_Type(Integer32):
    """Custom type fsbgp4mpePeerExtPassive based on Integer32"""
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


_Fsbgp4mpePeerExtPassive_Type.__name__ = "Integer32"
_Fsbgp4mpePeerExtPassive_Object = MibTableColumn
fsbgp4mpePeerExtPassive = _Fsbgp4mpePeerExtPassive_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 16),
    _Fsbgp4mpePeerExtPassive_Type()
)
fsbgp4mpePeerExtPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtPassive.setStatus("current")


class _Fsbgp4mpePeerExtDefaultOriginate_Type(Integer32):
    """Custom type fsbgp4mpePeerExtDefaultOriginate based on Integer32"""
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


_Fsbgp4mpePeerExtDefaultOriginate_Type.__name__ = "Integer32"
_Fsbgp4mpePeerExtDefaultOriginate_Object = MibTableColumn
fsbgp4mpePeerExtDefaultOriginate = _Fsbgp4mpePeerExtDefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 17),
    _Fsbgp4mpePeerExtDefaultOriginate_Type()
)
fsbgp4mpePeerExtDefaultOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtDefaultOriginate.setStatus("current")


class _Fsbgp4mpePeerExtActivateMPCapability_Type(Integer32):
    """Custom type fsbgp4mpePeerExtActivateMPCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ipv4unicast", 1),
          ("ipv6unicast", 2),
          ("vpnv4unicast", 8),
          ("l2vpnvpls", 16))
    )


_Fsbgp4mpePeerExtActivateMPCapability_Type.__name__ = "Integer32"
_Fsbgp4mpePeerExtActivateMPCapability_Object = MibTableColumn
fsbgp4mpePeerExtActivateMPCapability = _Fsbgp4mpePeerExtActivateMPCapability_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 18),
    _Fsbgp4mpePeerExtActivateMPCapability_Type()
)
fsbgp4mpePeerExtActivateMPCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtActivateMPCapability.setStatus("current")


class _Fsbgp4mpePeerExtDeactivateMPCapability_Type(Integer32):
    """Custom type fsbgp4mpePeerExtDeactivateMPCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ipv4unicast", 1),
          ("ipv6unicast", 2),
          ("vpnv4unicast", 8),
          ("l2vpnvpls", 16))
    )


_Fsbgp4mpePeerExtDeactivateMPCapability_Type.__name__ = "Integer32"
_Fsbgp4mpePeerExtDeactivateMPCapability_Object = MibTableColumn
fsbgp4mpePeerExtDeactivateMPCapability = _Fsbgp4mpePeerExtDeactivateMPCapability_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 19),
    _Fsbgp4mpePeerExtDeactivateMPCapability_Type()
)
fsbgp4mpePeerExtDeactivateMPCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtDeactivateMPCapability.setStatus("current")


class _Fsbgp4mpePeerExtMplsVpnVrfAssociated_Type(DisplayString):
    """Custom type fsbgp4mpePeerExtMplsVpnVrfAssociated based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fsbgp4mpePeerExtMplsVpnVrfAssociated_Type.__name__ = "DisplayString"
_Fsbgp4mpePeerExtMplsVpnVrfAssociated_Object = MibTableColumn
fsbgp4mpePeerExtMplsVpnVrfAssociated = _Fsbgp4mpePeerExtMplsVpnVrfAssociated_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 20),
    _Fsbgp4mpePeerExtMplsVpnVrfAssociated_Type()
)
fsbgp4mpePeerExtMplsVpnVrfAssociated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtMplsVpnVrfAssociated.setStatus("current")


class _Fsbgp4mpePeerExtMplsVpnCERouteTargetAdvt_Type(Integer32):
    """Custom type fsbgp4mpePeerExtMplsVpnCERouteTargetAdvt based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("send", 1),
          ("donotsend", 2))
    )


_Fsbgp4mpePeerExtMplsVpnCERouteTargetAdvt_Type.__name__ = "Integer32"
_Fsbgp4mpePeerExtMplsVpnCERouteTargetAdvt_Object = MibTableColumn
fsbgp4mpePeerExtMplsVpnCERouteTargetAdvt = _Fsbgp4mpePeerExtMplsVpnCERouteTargetAdvt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 21),
    _Fsbgp4mpePeerExtMplsVpnCERouteTargetAdvt_Type()
)
fsbgp4mpePeerExtMplsVpnCERouteTargetAdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtMplsVpnCERouteTargetAdvt.setStatus("current")


class _Fsbgp4mpePeerExtMplsVpnCESiteOfOrigin_Type(DisplayString):
    """Custom type fsbgp4mpePeerExtMplsVpnCESiteOfOrigin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Fsbgp4mpePeerExtMplsVpnCESiteOfOrigin_Type.__name__ = "DisplayString"
_Fsbgp4mpePeerExtMplsVpnCESiteOfOrigin_Object = MibTableColumn
fsbgp4mpePeerExtMplsVpnCESiteOfOrigin = _Fsbgp4mpePeerExtMplsVpnCESiteOfOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 22),
    _Fsbgp4mpePeerExtMplsVpnCESiteOfOrigin_Type()
)
fsbgp4mpePeerExtMplsVpnCESiteOfOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtMplsVpnCESiteOfOrigin.setStatus("current")


class _Fsbgp4mpePeerExtOverrideCapability_Type(Integer32):
    """Custom type fsbgp4mpePeerExtOverrideCapability based on Integer32"""
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


_Fsbgp4mpePeerExtOverrideCapability_Type.__name__ = "Integer32"
_Fsbgp4mpePeerExtOverrideCapability_Object = MibTableColumn
fsbgp4mpePeerExtOverrideCapability = _Fsbgp4mpePeerExtOverrideCapability_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 21, 1, 24),
    _Fsbgp4mpePeerExtOverrideCapability_Type()
)
fsbgp4mpePeerExtOverrideCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpePeerExtOverrideCapability.setStatus("current")
_Fsbgp4MpeMEDTable_Object = MibTable
fsbgp4MpeMEDTable = _Fsbgp4MpeMEDTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 22)
)
if mibBuilder.loadTexts:
    fsbgp4MpeMEDTable.setStatus("current")
_Fsbgp4MpeMEDEntry_Object = MibTableRow
fsbgp4MpeMEDEntry = _Fsbgp4MpeMEDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 22, 1)
)
fsbgp4MpeMEDEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeMEDIndex"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeMEDEntry.setStatus("current")


class _Fsbgp4mpeMEDIndex_Type(Integer32):
    """Custom type fsbgp4mpeMEDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Fsbgp4mpeMEDIndex_Type.__name__ = "Integer32"
_Fsbgp4mpeMEDIndex_Object = MibTableColumn
fsbgp4mpeMEDIndex = _Fsbgp4mpeMEDIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 22, 1, 1),
    _Fsbgp4mpeMEDIndex_Type()
)
fsbgp4mpeMEDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeMEDIndex.setStatus("current")


class _Fsbgp4mpeMEDAdminStatus_Type(Integer32):
    """Custom type fsbgp4mpeMEDAdminStatus based on Integer32"""
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


_Fsbgp4mpeMEDAdminStatus_Type.__name__ = "Integer32"
_Fsbgp4mpeMEDAdminStatus_Object = MibTableColumn
fsbgp4mpeMEDAdminStatus = _Fsbgp4mpeMEDAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 22, 1, 2),
    _Fsbgp4mpeMEDAdminStatus_Type()
)
fsbgp4mpeMEDAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeMEDAdminStatus.setStatus("current")


class _Fsbgp4mpeMEDRemoteAS_Type(Unsigned32):
    """Custom type fsbgp4mpeMEDRemoteAS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Fsbgp4mpeMEDRemoteAS_Type.__name__ = "Unsigned32"
_Fsbgp4mpeMEDRemoteAS_Object = MibTableColumn
fsbgp4mpeMEDRemoteAS = _Fsbgp4mpeMEDRemoteAS_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 22, 1, 3),
    _Fsbgp4mpeMEDRemoteAS_Type()
)
fsbgp4mpeMEDRemoteAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeMEDRemoteAS.setStatus("current")
_Fsbgp4mpeMEDIPAddrAfi_Type = InetAddressType
_Fsbgp4mpeMEDIPAddrAfi_Object = MibTableColumn
fsbgp4mpeMEDIPAddrAfi = _Fsbgp4mpeMEDIPAddrAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 22, 1, 4),
    _Fsbgp4mpeMEDIPAddrAfi_Type()
)
fsbgp4mpeMEDIPAddrAfi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeMEDIPAddrAfi.setStatus("current")
_Fsbgp4mpeMEDIPAddrSafi_Type = BgpSafi
_Fsbgp4mpeMEDIPAddrSafi_Object = MibTableColumn
fsbgp4mpeMEDIPAddrSafi = _Fsbgp4mpeMEDIPAddrSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 22, 1, 5),
    _Fsbgp4mpeMEDIPAddrSafi_Type()
)
fsbgp4mpeMEDIPAddrSafi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeMEDIPAddrSafi.setStatus("current")


class _Fsbgp4mpeMEDIPAddrPrefix_Type(InetAddress):
    """Custom type fsbgp4mpeMEDIPAddrPrefix based on InetAddress"""
    defaultHexValue = "00000000"


_Fsbgp4mpeMEDIPAddrPrefix_Type.__name__ = "InetAddress"
_Fsbgp4mpeMEDIPAddrPrefix_Object = MibTableColumn
fsbgp4mpeMEDIPAddrPrefix = _Fsbgp4mpeMEDIPAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 22, 1, 6),
    _Fsbgp4mpeMEDIPAddrPrefix_Type()
)
fsbgp4mpeMEDIPAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeMEDIPAddrPrefix.setStatus("current")


class _Fsbgp4mpeMEDIPAddrPrefixLen_Type(Integer32):
    """Custom type fsbgp4mpeMEDIPAddrPrefixLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Fsbgp4mpeMEDIPAddrPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4mpeMEDIPAddrPrefixLen_Object = MibTableColumn
fsbgp4mpeMEDIPAddrPrefixLen = _Fsbgp4mpeMEDIPAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 22, 1, 7),
    _Fsbgp4mpeMEDIPAddrPrefixLen_Type()
)
fsbgp4mpeMEDIPAddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeMEDIPAddrPrefixLen.setStatus("current")
_Fsbgp4mpeMEDIntermediateAS_Type = DisplayString
_Fsbgp4mpeMEDIntermediateAS_Object = MibTableColumn
fsbgp4mpeMEDIntermediateAS = _Fsbgp4mpeMEDIntermediateAS_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 22, 1, 8),
    _Fsbgp4mpeMEDIntermediateAS_Type()
)
fsbgp4mpeMEDIntermediateAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeMEDIntermediateAS.setStatus("current")


class _Fsbgp4mpeMEDDirection_Type(Integer32):
    """Custom type fsbgp4mpeMEDDirection based on Integer32"""
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


_Fsbgp4mpeMEDDirection_Type.__name__ = "Integer32"
_Fsbgp4mpeMEDDirection_Object = MibTableColumn
fsbgp4mpeMEDDirection = _Fsbgp4mpeMEDDirection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 22, 1, 9),
    _Fsbgp4mpeMEDDirection_Type()
)
fsbgp4mpeMEDDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeMEDDirection.setStatus("current")


class _Fsbgp4mpeMEDValue_Type(Unsigned32):
    """Custom type fsbgp4mpeMEDValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Fsbgp4mpeMEDValue_Type.__name__ = "Unsigned32"
_Fsbgp4mpeMEDValue_Object = MibTableColumn
fsbgp4mpeMEDValue = _Fsbgp4mpeMEDValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 22, 1, 10),
    _Fsbgp4mpeMEDValue_Type()
)
fsbgp4mpeMEDValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeMEDValue.setStatus("current")


class _Fsbgp4mpeMEDPreference_Type(Integer32):
    """Custom type fsbgp4mpeMEDPreference based on Integer32"""
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


_Fsbgp4mpeMEDPreference_Type.__name__ = "Integer32"
_Fsbgp4mpeMEDPreference_Object = MibTableColumn
fsbgp4mpeMEDPreference = _Fsbgp4mpeMEDPreference_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 22, 1, 11),
    _Fsbgp4mpeMEDPreference_Type()
)
fsbgp4mpeMEDPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeMEDPreference.setStatus("current")


class _Fsbgp4mpeMEDVrfName_Type(DisplayString):
    """Custom type fsbgp4mpeMEDVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fsbgp4mpeMEDVrfName_Type.__name__ = "DisplayString"
_Fsbgp4mpeMEDVrfName_Object = MibTableColumn
fsbgp4mpeMEDVrfName = _Fsbgp4mpeMEDVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 22, 1, 12),
    _Fsbgp4mpeMEDVrfName_Type()
)
fsbgp4mpeMEDVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeMEDVrfName.setStatus("current")
_Fsbgp4MpeLocalPrefTable_Object = MibTable
fsbgp4MpeLocalPrefTable = _Fsbgp4MpeLocalPrefTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 23)
)
if mibBuilder.loadTexts:
    fsbgp4MpeLocalPrefTable.setStatus("current")
_Fsbgp4MpeLocalPrefEntry_Object = MibTableRow
fsbgp4MpeLocalPrefEntry = _Fsbgp4MpeLocalPrefEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 23, 1)
)
fsbgp4MpeLocalPrefEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeLocalPrefIndex"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeLocalPrefEntry.setStatus("current")


class _Fsbgp4mpeLocalPrefIndex_Type(Integer32):
    """Custom type fsbgp4mpeLocalPrefIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Fsbgp4mpeLocalPrefIndex_Type.__name__ = "Integer32"
_Fsbgp4mpeLocalPrefIndex_Object = MibTableColumn
fsbgp4mpeLocalPrefIndex = _Fsbgp4mpeLocalPrefIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 23, 1, 1),
    _Fsbgp4mpeLocalPrefIndex_Type()
)
fsbgp4mpeLocalPrefIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeLocalPrefIndex.setStatus("current")


class _Fsbgp4mpeLocalPrefAdminStatus_Type(Integer32):
    """Custom type fsbgp4mpeLocalPrefAdminStatus based on Integer32"""
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


_Fsbgp4mpeLocalPrefAdminStatus_Type.__name__ = "Integer32"
_Fsbgp4mpeLocalPrefAdminStatus_Object = MibTableColumn
fsbgp4mpeLocalPrefAdminStatus = _Fsbgp4mpeLocalPrefAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 23, 1, 2),
    _Fsbgp4mpeLocalPrefAdminStatus_Type()
)
fsbgp4mpeLocalPrefAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeLocalPrefAdminStatus.setStatus("current")


class _Fsbgp4mpeLocalPrefRemoteAS_Type(Unsigned32):
    """Custom type fsbgp4mpeLocalPrefRemoteAS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Fsbgp4mpeLocalPrefRemoteAS_Type.__name__ = "Unsigned32"
_Fsbgp4mpeLocalPrefRemoteAS_Object = MibTableColumn
fsbgp4mpeLocalPrefRemoteAS = _Fsbgp4mpeLocalPrefRemoteAS_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 23, 1, 3),
    _Fsbgp4mpeLocalPrefRemoteAS_Type()
)
fsbgp4mpeLocalPrefRemoteAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeLocalPrefRemoteAS.setStatus("current")
_Fsbgp4mpeLocalPrefIPAddrAfi_Type = InetAddressType
_Fsbgp4mpeLocalPrefIPAddrAfi_Object = MibTableColumn
fsbgp4mpeLocalPrefIPAddrAfi = _Fsbgp4mpeLocalPrefIPAddrAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 23, 1, 4),
    _Fsbgp4mpeLocalPrefIPAddrAfi_Type()
)
fsbgp4mpeLocalPrefIPAddrAfi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeLocalPrefIPAddrAfi.setStatus("current")
_Fsbgp4mpeLocalPrefIPAddrSafi_Type = BgpSafi
_Fsbgp4mpeLocalPrefIPAddrSafi_Object = MibTableColumn
fsbgp4mpeLocalPrefIPAddrSafi = _Fsbgp4mpeLocalPrefIPAddrSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 23, 1, 5),
    _Fsbgp4mpeLocalPrefIPAddrSafi_Type()
)
fsbgp4mpeLocalPrefIPAddrSafi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeLocalPrefIPAddrSafi.setStatus("current")


class _Fsbgp4mpeLocalPrefIPAddrPrefix_Type(InetAddress):
    """Custom type fsbgp4mpeLocalPrefIPAddrPrefix based on InetAddress"""
    defaultHexValue = "00000000"


_Fsbgp4mpeLocalPrefIPAddrPrefix_Type.__name__ = "InetAddress"
_Fsbgp4mpeLocalPrefIPAddrPrefix_Object = MibTableColumn
fsbgp4mpeLocalPrefIPAddrPrefix = _Fsbgp4mpeLocalPrefIPAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 23, 1, 6),
    _Fsbgp4mpeLocalPrefIPAddrPrefix_Type()
)
fsbgp4mpeLocalPrefIPAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeLocalPrefIPAddrPrefix.setStatus("current")


class _Fsbgp4mpeLocalPrefIPAddrPrefixLen_Type(Integer32):
    """Custom type fsbgp4mpeLocalPrefIPAddrPrefixLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Fsbgp4mpeLocalPrefIPAddrPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4mpeLocalPrefIPAddrPrefixLen_Object = MibTableColumn
fsbgp4mpeLocalPrefIPAddrPrefixLen = _Fsbgp4mpeLocalPrefIPAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 23, 1, 7),
    _Fsbgp4mpeLocalPrefIPAddrPrefixLen_Type()
)
fsbgp4mpeLocalPrefIPAddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeLocalPrefIPAddrPrefixLen.setStatus("current")
_Fsbgp4mpeLocalPrefIntermediateAS_Type = DisplayString
_Fsbgp4mpeLocalPrefIntermediateAS_Object = MibTableColumn
fsbgp4mpeLocalPrefIntermediateAS = _Fsbgp4mpeLocalPrefIntermediateAS_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 23, 1, 8),
    _Fsbgp4mpeLocalPrefIntermediateAS_Type()
)
fsbgp4mpeLocalPrefIntermediateAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeLocalPrefIntermediateAS.setStatus("current")


class _Fsbgp4mpeLocalPrefDirection_Type(Integer32):
    """Custom type fsbgp4mpeLocalPrefDirection based on Integer32"""
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


_Fsbgp4mpeLocalPrefDirection_Type.__name__ = "Integer32"
_Fsbgp4mpeLocalPrefDirection_Object = MibTableColumn
fsbgp4mpeLocalPrefDirection = _Fsbgp4mpeLocalPrefDirection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 23, 1, 9),
    _Fsbgp4mpeLocalPrefDirection_Type()
)
fsbgp4mpeLocalPrefDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeLocalPrefDirection.setStatus("current")


class _Fsbgp4mpeLocalPrefValue_Type(Unsigned32):
    """Custom type fsbgp4mpeLocalPrefValue based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Fsbgp4mpeLocalPrefValue_Type.__name__ = "Unsigned32"
_Fsbgp4mpeLocalPrefValue_Object = MibTableColumn
fsbgp4mpeLocalPrefValue = _Fsbgp4mpeLocalPrefValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 23, 1, 10),
    _Fsbgp4mpeLocalPrefValue_Type()
)
fsbgp4mpeLocalPrefValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeLocalPrefValue.setStatus("current")


class _Fsbgp4mpeLocalPrefPreference_Type(Integer32):
    """Custom type fsbgp4mpeLocalPrefPreference based on Integer32"""
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


_Fsbgp4mpeLocalPrefPreference_Type.__name__ = "Integer32"
_Fsbgp4mpeLocalPrefPreference_Object = MibTableColumn
fsbgp4mpeLocalPrefPreference = _Fsbgp4mpeLocalPrefPreference_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 23, 1, 11),
    _Fsbgp4mpeLocalPrefPreference_Type()
)
fsbgp4mpeLocalPrefPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeLocalPrefPreference.setStatus("current")


class _Fsbgp4mpeLocalPrefVrfName_Type(DisplayString):
    """Custom type fsbgp4mpeLocalPrefVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fsbgp4mpeLocalPrefVrfName_Type.__name__ = "DisplayString"
_Fsbgp4mpeLocalPrefVrfName_Object = MibTableColumn
fsbgp4mpeLocalPrefVrfName = _Fsbgp4mpeLocalPrefVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 23, 1, 12),
    _Fsbgp4mpeLocalPrefVrfName_Type()
)
fsbgp4mpeLocalPrefVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeLocalPrefVrfName.setStatus("current")
_Fsbgp4MpeUpdateFilterTable_Object = MibTable
fsbgp4MpeUpdateFilterTable = _Fsbgp4MpeUpdateFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 24)
)
if mibBuilder.loadTexts:
    fsbgp4MpeUpdateFilterTable.setStatus("current")
_Fsbgp4MpeUpdateFilterEntry_Object = MibTableRow
fsbgp4MpeUpdateFilterEntry = _Fsbgp4MpeUpdateFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 24, 1)
)
fsbgp4MpeUpdateFilterEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeUpdateFilterIndex"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeUpdateFilterEntry.setStatus("current")


class _Fsbgp4mpeUpdateFilterIndex_Type(Integer32):
    """Custom type fsbgp4mpeUpdateFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Fsbgp4mpeUpdateFilterIndex_Type.__name__ = "Integer32"
_Fsbgp4mpeUpdateFilterIndex_Object = MibTableColumn
fsbgp4mpeUpdateFilterIndex = _Fsbgp4mpeUpdateFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 24, 1, 1),
    _Fsbgp4mpeUpdateFilterIndex_Type()
)
fsbgp4mpeUpdateFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeUpdateFilterIndex.setStatus("current")


class _Fsbgp4mpeUpdateFilterAdminStatus_Type(Integer32):
    """Custom type fsbgp4mpeUpdateFilterAdminStatus based on Integer32"""
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


_Fsbgp4mpeUpdateFilterAdminStatus_Type.__name__ = "Integer32"
_Fsbgp4mpeUpdateFilterAdminStatus_Object = MibTableColumn
fsbgp4mpeUpdateFilterAdminStatus = _Fsbgp4mpeUpdateFilterAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 24, 1, 2),
    _Fsbgp4mpeUpdateFilterAdminStatus_Type()
)
fsbgp4mpeUpdateFilterAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeUpdateFilterAdminStatus.setStatus("current")


class _Fsbgp4mpeUpdateFilterRemoteAS_Type(Unsigned32):
    """Custom type fsbgp4mpeUpdateFilterRemoteAS based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Fsbgp4mpeUpdateFilterRemoteAS_Type.__name__ = "Unsigned32"
_Fsbgp4mpeUpdateFilterRemoteAS_Object = MibTableColumn
fsbgp4mpeUpdateFilterRemoteAS = _Fsbgp4mpeUpdateFilterRemoteAS_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 24, 1, 3),
    _Fsbgp4mpeUpdateFilterRemoteAS_Type()
)
fsbgp4mpeUpdateFilterRemoteAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeUpdateFilterRemoteAS.setStatus("current")
_Fsbgp4mpeUpdateFilterIPAddrAfi_Type = InetAddressType
_Fsbgp4mpeUpdateFilterIPAddrAfi_Object = MibTableColumn
fsbgp4mpeUpdateFilterIPAddrAfi = _Fsbgp4mpeUpdateFilterIPAddrAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 24, 1, 4),
    _Fsbgp4mpeUpdateFilterIPAddrAfi_Type()
)
fsbgp4mpeUpdateFilterIPAddrAfi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeUpdateFilterIPAddrAfi.setStatus("current")
_Fsbgp4mpeUpdateFilterIPAddrSafi_Type = BgpSafi
_Fsbgp4mpeUpdateFilterIPAddrSafi_Object = MibTableColumn
fsbgp4mpeUpdateFilterIPAddrSafi = _Fsbgp4mpeUpdateFilterIPAddrSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 24, 1, 5),
    _Fsbgp4mpeUpdateFilterIPAddrSafi_Type()
)
fsbgp4mpeUpdateFilterIPAddrSafi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeUpdateFilterIPAddrSafi.setStatus("current")


class _Fsbgp4mpeUpdateFilterIPAddrPrefix_Type(InetAddress):
    """Custom type fsbgp4mpeUpdateFilterIPAddrPrefix based on InetAddress"""
    defaultHexValue = "00000000"


_Fsbgp4mpeUpdateFilterIPAddrPrefix_Type.__name__ = "InetAddress"
_Fsbgp4mpeUpdateFilterIPAddrPrefix_Object = MibTableColumn
fsbgp4mpeUpdateFilterIPAddrPrefix = _Fsbgp4mpeUpdateFilterIPAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 24, 1, 6),
    _Fsbgp4mpeUpdateFilterIPAddrPrefix_Type()
)
fsbgp4mpeUpdateFilterIPAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeUpdateFilterIPAddrPrefix.setStatus("current")


class _Fsbgp4mpeUpdateFilterIPAddrPrefixLen_Type(Integer32):
    """Custom type fsbgp4mpeUpdateFilterIPAddrPrefixLen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Fsbgp4mpeUpdateFilterIPAddrPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4mpeUpdateFilterIPAddrPrefixLen_Object = MibTableColumn
fsbgp4mpeUpdateFilterIPAddrPrefixLen = _Fsbgp4mpeUpdateFilterIPAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 24, 1, 7),
    _Fsbgp4mpeUpdateFilterIPAddrPrefixLen_Type()
)
fsbgp4mpeUpdateFilterIPAddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeUpdateFilterIPAddrPrefixLen.setStatus("current")
_Fsbgp4mpeUpdateFilterIntermediateAS_Type = DisplayString
_Fsbgp4mpeUpdateFilterIntermediateAS_Object = MibTableColumn
fsbgp4mpeUpdateFilterIntermediateAS = _Fsbgp4mpeUpdateFilterIntermediateAS_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 24, 1, 8),
    _Fsbgp4mpeUpdateFilterIntermediateAS_Type()
)
fsbgp4mpeUpdateFilterIntermediateAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeUpdateFilterIntermediateAS.setStatus("current")


class _Fsbgp4mpeUpdateFilterDirection_Type(Integer32):
    """Custom type fsbgp4mpeUpdateFilterDirection based on Integer32"""
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


_Fsbgp4mpeUpdateFilterDirection_Type.__name__ = "Integer32"
_Fsbgp4mpeUpdateFilterDirection_Object = MibTableColumn
fsbgp4mpeUpdateFilterDirection = _Fsbgp4mpeUpdateFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 24, 1, 9),
    _Fsbgp4mpeUpdateFilterDirection_Type()
)
fsbgp4mpeUpdateFilterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeUpdateFilterDirection.setStatus("current")


class _Fsbgp4mpeUpdateFilterAction_Type(Integer32):
    """Custom type fsbgp4mpeUpdateFilterAction based on Integer32"""
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


_Fsbgp4mpeUpdateFilterAction_Type.__name__ = "Integer32"
_Fsbgp4mpeUpdateFilterAction_Object = MibTableColumn
fsbgp4mpeUpdateFilterAction = _Fsbgp4mpeUpdateFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 24, 1, 10),
    _Fsbgp4mpeUpdateFilterAction_Type()
)
fsbgp4mpeUpdateFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeUpdateFilterAction.setStatus("current")


class _Fsbgp4mpeUpdateFilterVrfName_Type(DisplayString):
    """Custom type fsbgp4mpeUpdateFilterVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fsbgp4mpeUpdateFilterVrfName_Type.__name__ = "DisplayString"
_Fsbgp4mpeUpdateFilterVrfName_Object = MibTableColumn
fsbgp4mpeUpdateFilterVrfName = _Fsbgp4mpeUpdateFilterVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 24, 1, 11),
    _Fsbgp4mpeUpdateFilterVrfName_Type()
)
fsbgp4mpeUpdateFilterVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeUpdateFilterVrfName.setStatus("current")
_Fsbgp4MpeAggregateTable_Object = MibTable
fsbgp4MpeAggregateTable = _Fsbgp4MpeAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 25)
)
if mibBuilder.loadTexts:
    fsbgp4MpeAggregateTable.setStatus("current")
_Fsbgp4MpeAggregateEntry_Object = MibTableRow
fsbgp4MpeAggregateEntry = _Fsbgp4MpeAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 25, 1)
)
fsbgp4MpeAggregateEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeAggregateIndex"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeAggregateEntry.setStatus("current")
_Fsbgp4mpeAggregateIndex_Type = Integer32
_Fsbgp4mpeAggregateIndex_Object = MibTableColumn
fsbgp4mpeAggregateIndex = _Fsbgp4mpeAggregateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 25, 1, 1),
    _Fsbgp4mpeAggregateIndex_Type()
)
fsbgp4mpeAggregateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeAggregateIndex.setStatus("current")


class _Fsbgp4mpeAggregateAdminStatus_Type(Integer32):
    """Custom type fsbgp4mpeAggregateAdminStatus based on Integer32"""
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


_Fsbgp4mpeAggregateAdminStatus_Type.__name__ = "Integer32"
_Fsbgp4mpeAggregateAdminStatus_Object = MibTableColumn
fsbgp4mpeAggregateAdminStatus = _Fsbgp4mpeAggregateAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 25, 1, 2),
    _Fsbgp4mpeAggregateAdminStatus_Type()
)
fsbgp4mpeAggregateAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeAggregateAdminStatus.setStatus("current")
_Fsbgp4mpeAggregateIPAddrAfi_Type = InetAddressType
_Fsbgp4mpeAggregateIPAddrAfi_Object = MibTableColumn
fsbgp4mpeAggregateIPAddrAfi = _Fsbgp4mpeAggregateIPAddrAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 25, 1, 3),
    _Fsbgp4mpeAggregateIPAddrAfi_Type()
)
fsbgp4mpeAggregateIPAddrAfi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeAggregateIPAddrAfi.setStatus("current")
_Fsbgp4mpeAggregateIPAddrSafi_Type = BgpSafi
_Fsbgp4mpeAggregateIPAddrSafi_Object = MibTableColumn
fsbgp4mpeAggregateIPAddrSafi = _Fsbgp4mpeAggregateIPAddrSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 25, 1, 4),
    _Fsbgp4mpeAggregateIPAddrSafi_Type()
)
fsbgp4mpeAggregateIPAddrSafi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeAggregateIPAddrSafi.setStatus("current")
_Fsbgp4mpeAggregateIPAddrPrefix_Type = InetAddress
_Fsbgp4mpeAggregateIPAddrPrefix_Object = MibTableColumn
fsbgp4mpeAggregateIPAddrPrefix = _Fsbgp4mpeAggregateIPAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 25, 1, 5),
    _Fsbgp4mpeAggregateIPAddrPrefix_Type()
)
fsbgp4mpeAggregateIPAddrPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeAggregateIPAddrPrefix.setStatus("current")


class _Fsbgp4mpeAggregateIPAddrPrefixLen_Type(Integer32):
    """Custom type fsbgp4mpeAggregateIPAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Fsbgp4mpeAggregateIPAddrPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4mpeAggregateIPAddrPrefixLen_Object = MibTableColumn
fsbgp4mpeAggregateIPAddrPrefixLen = _Fsbgp4mpeAggregateIPAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 25, 1, 6),
    _Fsbgp4mpeAggregateIPAddrPrefixLen_Type()
)
fsbgp4mpeAggregateIPAddrPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeAggregateIPAddrPrefixLen.setStatus("current")


class _Fsbgp4mpeAggregateAdvertise_Type(Integer32):
    """Custom type fsbgp4mpeAggregateAdvertise based on Integer32"""
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


_Fsbgp4mpeAggregateAdvertise_Type.__name__ = "Integer32"
_Fsbgp4mpeAggregateAdvertise_Object = MibTableColumn
fsbgp4mpeAggregateAdvertise = _Fsbgp4mpeAggregateAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 25, 1, 7),
    _Fsbgp4mpeAggregateAdvertise_Type()
)
fsbgp4mpeAggregateAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeAggregateAdvertise.setStatus("current")


class _Fsbgp4mpeAggregateVrfName_Type(DisplayString):
    """Custom type fsbgp4mpeAggregateVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fsbgp4mpeAggregateVrfName_Type.__name__ = "DisplayString"
_Fsbgp4mpeAggregateVrfName_Object = MibTableColumn
fsbgp4mpeAggregateVrfName = _Fsbgp4mpeAggregateVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 25, 1, 8),
    _Fsbgp4mpeAggregateVrfName_Type()
)
fsbgp4mpeAggregateVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeAggregateVrfName.setStatus("current")


class _Fsbgp4mpeAggregateAsSet_Type(Integer32):
    """Custom type fsbgp4mpeAggregateAsSet based on Integer32"""
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


_Fsbgp4mpeAggregateAsSet_Type.__name__ = "Integer32"
_Fsbgp4mpeAggregateAsSet_Object = MibTableColumn
fsbgp4mpeAggregateAsSet = _Fsbgp4mpeAggregateAsSet_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 25, 1, 9),
    _Fsbgp4mpeAggregateAsSet_Type()
)
fsbgp4mpeAggregateAsSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeAggregateAsSet.setStatus("current")


class _Fsbgp4mpeAggregateAdvertiseRouteMapName_Type(DisplayString):
    """Custom type fsbgp4mpeAggregateAdvertiseRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Fsbgp4mpeAggregateAdvertiseRouteMapName_Type.__name__ = "DisplayString"
_Fsbgp4mpeAggregateAdvertiseRouteMapName_Object = MibTableColumn
fsbgp4mpeAggregateAdvertiseRouteMapName = _Fsbgp4mpeAggregateAdvertiseRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 25, 1, 10),
    _Fsbgp4mpeAggregateAdvertiseRouteMapName_Type()
)
fsbgp4mpeAggregateAdvertiseRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeAggregateAdvertiseRouteMapName.setStatus("current")


class _Fsbgp4mpeAggregateSuppressRouteMapName_Type(DisplayString):
    """Custom type fsbgp4mpeAggregateSuppressRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Fsbgp4mpeAggregateSuppressRouteMapName_Type.__name__ = "DisplayString"
_Fsbgp4mpeAggregateSuppressRouteMapName_Object = MibTableColumn
fsbgp4mpeAggregateSuppressRouteMapName = _Fsbgp4mpeAggregateSuppressRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 25, 1, 11),
    _Fsbgp4mpeAggregateSuppressRouteMapName_Type()
)
fsbgp4mpeAggregateSuppressRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeAggregateSuppressRouteMapName.setStatus("current")


class _Fsbgp4mpeAggregateAttributeRouteMapName_Type(DisplayString):
    """Custom type fsbgp4mpeAggregateAttributeRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Fsbgp4mpeAggregateAttributeRouteMapName_Type.__name__ = "DisplayString"
_Fsbgp4mpeAggregateAttributeRouteMapName_Object = MibTableColumn
fsbgp4mpeAggregateAttributeRouteMapName = _Fsbgp4mpeAggregateAttributeRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 25, 1, 12),
    _Fsbgp4mpeAggregateAttributeRouteMapName_Type()
)
fsbgp4mpeAggregateAttributeRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeAggregateAttributeRouteMapName.setStatus("current")
_Fsbgp4MpeImportRouteTable_Object = MibTable
fsbgp4MpeImportRouteTable = _Fsbgp4MpeImportRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 26)
)
if mibBuilder.loadTexts:
    fsbgp4MpeImportRouteTable.setStatus("current")
_Fsbgp4MpeImportRouteEntry_Object = MibTableRow
fsbgp4MpeImportRouteEntry = _Fsbgp4MpeImportRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 26, 1)
)
fsbgp4MpeImportRouteEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeImportRoutePrefixAfi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeImportRoutePrefixSafi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeImportRoutePrefix"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeImportRoutePrefixLen"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeImportRouteProtocol"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeImportRouteNextHop"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeImportRouteIfIndex"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeImportRouteMetric"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeImportRouteVrf"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeImportRouteEntry.setStatus("current")
_Fsbgp4mpeImportRoutePrefixAfi_Type = InetAddressType
_Fsbgp4mpeImportRoutePrefixAfi_Object = MibTableColumn
fsbgp4mpeImportRoutePrefixAfi = _Fsbgp4mpeImportRoutePrefixAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 26, 1, 1),
    _Fsbgp4mpeImportRoutePrefixAfi_Type()
)
fsbgp4mpeImportRoutePrefixAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeImportRoutePrefixAfi.setStatus("current")
_Fsbgp4mpeImportRoutePrefixSafi_Type = BgpSafi
_Fsbgp4mpeImportRoutePrefixSafi_Object = MibTableColumn
fsbgp4mpeImportRoutePrefixSafi = _Fsbgp4mpeImportRoutePrefixSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 26, 1, 2),
    _Fsbgp4mpeImportRoutePrefixSafi_Type()
)
fsbgp4mpeImportRoutePrefixSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeImportRoutePrefixSafi.setStatus("current")
_Fsbgp4mpeImportRoutePrefix_Type = InetAddress
_Fsbgp4mpeImportRoutePrefix_Object = MibTableColumn
fsbgp4mpeImportRoutePrefix = _Fsbgp4mpeImportRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 26, 1, 3),
    _Fsbgp4mpeImportRoutePrefix_Type()
)
fsbgp4mpeImportRoutePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeImportRoutePrefix.setStatus("current")


class _Fsbgp4mpeImportRoutePrefixLen_Type(Integer32):
    """Custom type fsbgp4mpeImportRoutePrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fsbgp4mpeImportRoutePrefixLen_Type.__name__ = "Integer32"
_Fsbgp4mpeImportRoutePrefixLen_Object = MibTableColumn
fsbgp4mpeImportRoutePrefixLen = _Fsbgp4mpeImportRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 26, 1, 4),
    _Fsbgp4mpeImportRoutePrefixLen_Type()
)
fsbgp4mpeImportRoutePrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeImportRoutePrefixLen.setStatus("current")


class _Fsbgp4mpeImportRouteProtocol_Type(Integer32):
    """Custom type fsbgp4mpeImportRouteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(13, 13),
    )


_Fsbgp4mpeImportRouteProtocol_Type.__name__ = "Integer32"
_Fsbgp4mpeImportRouteProtocol_Object = MibTableColumn
fsbgp4mpeImportRouteProtocol = _Fsbgp4mpeImportRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 26, 1, 5),
    _Fsbgp4mpeImportRouteProtocol_Type()
)
fsbgp4mpeImportRouteProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeImportRouteProtocol.setStatus("current")
_Fsbgp4mpeImportRouteNextHop_Type = InetAddress
_Fsbgp4mpeImportRouteNextHop_Object = MibTableColumn
fsbgp4mpeImportRouteNextHop = _Fsbgp4mpeImportRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 26, 1, 6),
    _Fsbgp4mpeImportRouteNextHop_Type()
)
fsbgp4mpeImportRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeImportRouteNextHop.setStatus("current")


class _Fsbgp4mpeImportRouteIfIndex_Type(Integer32):
    """Custom type fsbgp4mpeImportRouteIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsbgp4mpeImportRouteIfIndex_Type.__name__ = "Integer32"
_Fsbgp4mpeImportRouteIfIndex_Object = MibTableColumn
fsbgp4mpeImportRouteIfIndex = _Fsbgp4mpeImportRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 26, 1, 7),
    _Fsbgp4mpeImportRouteIfIndex_Type()
)
fsbgp4mpeImportRouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeImportRouteIfIndex.setStatus("current")


class _Fsbgp4mpeImportRouteMetric_Type(Integer32):
    """Custom type fsbgp4mpeImportRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsbgp4mpeImportRouteMetric_Type.__name__ = "Integer32"
_Fsbgp4mpeImportRouteMetric_Object = MibTableColumn
fsbgp4mpeImportRouteMetric = _Fsbgp4mpeImportRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 26, 1, 8),
    _Fsbgp4mpeImportRouteMetric_Type()
)
fsbgp4mpeImportRouteMetric.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeImportRouteMetric.setStatus("current")


class _Fsbgp4mpeImportRouteVrf_Type(DisplayString):
    """Custom type fsbgp4mpeImportRouteVrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fsbgp4mpeImportRouteVrf_Type.__name__ = "DisplayString"
_Fsbgp4mpeImportRouteVrf_Object = MibTableColumn
fsbgp4mpeImportRouteVrf = _Fsbgp4mpeImportRouteVrf_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 26, 1, 9),
    _Fsbgp4mpeImportRouteVrf_Type()
)
fsbgp4mpeImportRouteVrf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeImportRouteVrf.setStatus("current")


class _Fsbgp4mpeImportRouteAction_Type(Integer32):
    """Custom type fsbgp4mpeImportRouteAction based on Integer32"""
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


_Fsbgp4mpeImportRouteAction_Type.__name__ = "Integer32"
_Fsbgp4mpeImportRouteAction_Object = MibTableColumn
fsbgp4mpeImportRouteAction = _Fsbgp4mpeImportRouteAction_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 26, 1, 10),
    _Fsbgp4mpeImportRouteAction_Type()
)
fsbgp4mpeImportRouteAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeImportRouteAction.setStatus("current")
_Fsbgp4MpeFsmTransitionHistTable_Object = MibTable
fsbgp4MpeFsmTransitionHistTable = _Fsbgp4MpeFsmTransitionHistTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 27)
)
if mibBuilder.loadTexts:
    fsbgp4MpeFsmTransitionHistTable.setStatus("current")
_Fsbgp4MpeFsmTransitionHistEntry_Object = MibTableRow
fsbgp4MpeFsmTransitionHistEntry = _Fsbgp4MpeFsmTransitionHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 27, 1)
)
fsbgp4MpeFsmTransitionHistEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpePeerType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpePeer"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeFsmTransitionHistEntry.setStatus("current")
_Fsbgp4mpePeerType_Type = InetAddressType
_Fsbgp4mpePeerType_Object = MibTableColumn
fsbgp4mpePeerType = _Fsbgp4mpePeerType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 27, 1, 1),
    _Fsbgp4mpePeerType_Type()
)
fsbgp4mpePeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpePeerType.setStatus("current")
_Fsbgp4mpePeer_Type = InetAddress
_Fsbgp4mpePeer_Object = MibTableColumn
fsbgp4mpePeer = _Fsbgp4mpePeer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 27, 1, 2),
    _Fsbgp4mpePeer_Type()
)
fsbgp4mpePeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpePeer.setStatus("current")
_Fsbgp4mpeFsmTransitionHist_Type = DisplayString
_Fsbgp4mpeFsmTransitionHist_Object = MibTableColumn
fsbgp4mpeFsmTransitionHist = _Fsbgp4mpeFsmTransitionHist_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 27, 1, 3),
    _Fsbgp4mpeFsmTransitionHist_Type()
)
fsbgp4mpeFsmTransitionHist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeFsmTransitionHist.setStatus("current")
_Fsbgp4MpeRfd_ObjectIdentity = ObjectIdentity
fsbgp4MpeRfd = _Fsbgp4MpeRfd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28)
)
_Fsbgp4MpeRfdRtDampHistTable_Object = MibTable
fsbgp4MpeRfdRtDampHistTable = _Fsbgp4MpeRfdRtDampHistTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 1)
)
if mibBuilder.loadTexts:
    fsbgp4MpeRfdRtDampHistTable.setStatus("current")
_Fsbgp4MpeRfdRtDampHistEntry_Object = MibTableRow
fsbgp4MpeRfdRtDampHistEntry = _Fsbgp4MpeRfdRtDampHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 1, 1)
)
fsbgp4MpeRfdRtDampHistEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpePathAttrAddrPrefixAfi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpePathAttrAddrPrefixSafi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpePathAttrAddrPrefix"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpePathAttrAddrPrefixLen"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpePathAttrPeerType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpePathAttrPeer"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeRfdRtDampHistEntry.setStatus("current")
_Fsbgp4mpePathAttrAddrPrefixAfi_Type = InetAddressType
_Fsbgp4mpePathAttrAddrPrefixAfi_Object = MibTableColumn
fsbgp4mpePathAttrAddrPrefixAfi = _Fsbgp4mpePathAttrAddrPrefixAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 1, 1, 1),
    _Fsbgp4mpePathAttrAddrPrefixAfi_Type()
)
fsbgp4mpePathAttrAddrPrefixAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpePathAttrAddrPrefixAfi.setStatus("current")
_Fsbgp4mpePathAttrAddrPrefixSafi_Type = BgpSafi
_Fsbgp4mpePathAttrAddrPrefixSafi_Object = MibTableColumn
fsbgp4mpePathAttrAddrPrefixSafi = _Fsbgp4mpePathAttrAddrPrefixSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 1, 1, 2),
    _Fsbgp4mpePathAttrAddrPrefixSafi_Type()
)
fsbgp4mpePathAttrAddrPrefixSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpePathAttrAddrPrefixSafi.setStatus("current")
_Fsbgp4mpePathAttrAddrPrefix_Type = InetAddress
_Fsbgp4mpePathAttrAddrPrefix_Object = MibTableColumn
fsbgp4mpePathAttrAddrPrefix = _Fsbgp4mpePathAttrAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 1, 1, 3),
    _Fsbgp4mpePathAttrAddrPrefix_Type()
)
fsbgp4mpePathAttrAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpePathAttrAddrPrefix.setStatus("current")


class _Fsbgp4mpePathAttrAddrPrefixLen_Type(Integer32):
    """Custom type fsbgp4mpePathAttrAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Fsbgp4mpePathAttrAddrPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4mpePathAttrAddrPrefixLen_Object = MibTableColumn
fsbgp4mpePathAttrAddrPrefixLen = _Fsbgp4mpePathAttrAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 1, 1, 4),
    _Fsbgp4mpePathAttrAddrPrefixLen_Type()
)
fsbgp4mpePathAttrAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpePathAttrAddrPrefixLen.setStatus("current")
_Fsbgp4mpePathAttrPeerType_Type = InetAddressType
_Fsbgp4mpePathAttrPeerType_Object = MibTableColumn
fsbgp4mpePathAttrPeerType = _Fsbgp4mpePathAttrPeerType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 1, 1, 5),
    _Fsbgp4mpePathAttrPeerType_Type()
)
fsbgp4mpePathAttrPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpePathAttrPeerType.setStatus("current")
_Fsbgp4mpePathAttrPeer_Type = InetAddress
_Fsbgp4mpePathAttrPeer_Object = MibTableColumn
fsbgp4mpePathAttrPeer = _Fsbgp4mpePathAttrPeer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 1, 1, 6),
    _Fsbgp4mpePathAttrPeer_Type()
)
fsbgp4mpePathAttrPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpePathAttrPeer.setStatus("current")


class _Fsbgp4mpeRfdRtFom_Type(Integer32):
    """Custom type fsbgp4mpeRfdRtFom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsbgp4mpeRfdRtFom_Type.__name__ = "Integer32"
_Fsbgp4mpeRfdRtFom_Object = MibTableColumn
fsbgp4mpeRfdRtFom = _Fsbgp4mpeRfdRtFom_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 1, 1, 7),
    _Fsbgp4mpeRfdRtFom_Type()
)
fsbgp4mpeRfdRtFom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdRtFom.setStatus("current")


class _Fsbgp4mpeRfdRtLastUpdtTime_Type(Integer32):
    """Custom type fsbgp4mpeRfdRtLastUpdtTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsbgp4mpeRfdRtLastUpdtTime_Type.__name__ = "Integer32"
_Fsbgp4mpeRfdRtLastUpdtTime_Object = MibTableColumn
fsbgp4mpeRfdRtLastUpdtTime = _Fsbgp4mpeRfdRtLastUpdtTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 1, 1, 8),
    _Fsbgp4mpeRfdRtLastUpdtTime_Type()
)
fsbgp4mpeRfdRtLastUpdtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdRtLastUpdtTime.setStatus("current")


class _Fsbgp4mpeRfdRtState_Type(Integer32):
    """Custom type fsbgp4mpeRfdRtState based on Integer32"""
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


_Fsbgp4mpeRfdRtState_Type.__name__ = "Integer32"
_Fsbgp4mpeRfdRtState_Object = MibTableColumn
fsbgp4mpeRfdRtState = _Fsbgp4mpeRfdRtState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 1, 1, 9),
    _Fsbgp4mpeRfdRtState_Type()
)
fsbgp4mpeRfdRtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdRtState.setStatus("current")


class _Fsbgp4mpeRfdRtStatus_Type(Integer32):
    """Custom type fsbgp4mpeRfdRtStatus based on Integer32"""
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


_Fsbgp4mpeRfdRtStatus_Type.__name__ = "Integer32"
_Fsbgp4mpeRfdRtStatus_Object = MibTableColumn
fsbgp4mpeRfdRtStatus = _Fsbgp4mpeRfdRtStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 1, 1, 10),
    _Fsbgp4mpeRfdRtStatus_Type()
)
fsbgp4mpeRfdRtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdRtStatus.setStatus("current")
_Fsbgp4mpeRfdRtFlapCount_Type = Integer32
_Fsbgp4mpeRfdRtFlapCount_Object = MibTableColumn
fsbgp4mpeRfdRtFlapCount = _Fsbgp4mpeRfdRtFlapCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 1, 1, 11),
    _Fsbgp4mpeRfdRtFlapCount_Type()
)
fsbgp4mpeRfdRtFlapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdRtFlapCount.setStatus("current")


class _Fsbgp4mpeRfdRtFlapTime_Type(Integer32):
    """Custom type fsbgp4mpeRfdRtFlapTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsbgp4mpeRfdRtFlapTime_Type.__name__ = "Integer32"
_Fsbgp4mpeRfdRtFlapTime_Object = MibTableColumn
fsbgp4mpeRfdRtFlapTime = _Fsbgp4mpeRfdRtFlapTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 1, 1, 12),
    _Fsbgp4mpeRfdRtFlapTime_Type()
)
fsbgp4mpeRfdRtFlapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdRtFlapTime.setStatus("current")


class _Fsbgp4mpeRfdRtReuseTime_Type(Integer32):
    """Custom type fsbgp4mpeRfdRtReuseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsbgp4mpeRfdRtReuseTime_Type.__name__ = "Integer32"
_Fsbgp4mpeRfdRtReuseTime_Object = MibTableColumn
fsbgp4mpeRfdRtReuseTime = _Fsbgp4mpeRfdRtReuseTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 1, 1, 13),
    _Fsbgp4mpeRfdRtReuseTime_Type()
)
fsbgp4mpeRfdRtReuseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdRtReuseTime.setStatus("current")
_Fsbgp4MpeRfdPeerDampHistTable_Object = MibTable
fsbgp4MpeRfdPeerDampHistTable = _Fsbgp4MpeRfdPeerDampHistTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 2)
)
if mibBuilder.loadTexts:
    fsbgp4MpeRfdPeerDampHistTable.setStatus("current")
_Fsbgp4MpeRfdPeerDampHistEntry_Object = MibTableRow
fsbgp4MpeRfdPeerDampHistEntry = _Fsbgp4MpeRfdPeerDampHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 2, 1)
)
fsbgp4MpeRfdPeerDampHistEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpePeerRemoteIpAddrType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpePeerRemoteIpAddr"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeRfdPeerDampHistEntry.setStatus("current")
_Fsbgp4mpePeerRemoteIpAddrType_Type = InetAddressType
_Fsbgp4mpePeerRemoteIpAddrType_Object = MibTableColumn
fsbgp4mpePeerRemoteIpAddrType = _Fsbgp4mpePeerRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 2, 1, 1),
    _Fsbgp4mpePeerRemoteIpAddrType_Type()
)
fsbgp4mpePeerRemoteIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpePeerRemoteIpAddrType.setStatus("current")
_Fsbgp4mpePeerRemoteIpAddr_Type = InetAddress
_Fsbgp4mpePeerRemoteIpAddr_Object = MibTableColumn
fsbgp4mpePeerRemoteIpAddr = _Fsbgp4mpePeerRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 2, 1, 2),
    _Fsbgp4mpePeerRemoteIpAddr_Type()
)
fsbgp4mpePeerRemoteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpePeerRemoteIpAddr.setStatus("current")


class _Fsbgp4mpeRfdPeerFom_Type(Integer32):
    """Custom type fsbgp4mpeRfdPeerFom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsbgp4mpeRfdPeerFom_Type.__name__ = "Integer32"
_Fsbgp4mpeRfdPeerFom_Object = MibTableColumn
fsbgp4mpeRfdPeerFom = _Fsbgp4mpeRfdPeerFom_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 2, 1, 3),
    _Fsbgp4mpeRfdPeerFom_Type()
)
fsbgp4mpeRfdPeerFom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdPeerFom.setStatus("current")


class _Fsbgp4mpeRfdPeerLastUpdtTime_Type(Integer32):
    """Custom type fsbgp4mpeRfdPeerLastUpdtTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsbgp4mpeRfdPeerLastUpdtTime_Type.__name__ = "Integer32"
_Fsbgp4mpeRfdPeerLastUpdtTime_Object = MibTableColumn
fsbgp4mpeRfdPeerLastUpdtTime = _Fsbgp4mpeRfdPeerLastUpdtTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 2, 1, 4),
    _Fsbgp4mpeRfdPeerLastUpdtTime_Type()
)
fsbgp4mpeRfdPeerLastUpdtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdPeerLastUpdtTime.setStatus("current")


class _Fsbgp4mpeRfdPeerState_Type(Integer32):
    """Custom type fsbgp4mpeRfdPeerState based on Integer32"""
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


_Fsbgp4mpeRfdPeerState_Type.__name__ = "Integer32"
_Fsbgp4mpeRfdPeerState_Object = MibTableColumn
fsbgp4mpeRfdPeerState = _Fsbgp4mpeRfdPeerState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 2, 1, 5),
    _Fsbgp4mpeRfdPeerState_Type()
)
fsbgp4mpeRfdPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdPeerState.setStatus("current")


class _Fsbgp4mpeRfdPeerStatus_Type(Integer32):
    """Custom type fsbgp4mpeRfdPeerStatus based on Integer32"""
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


_Fsbgp4mpeRfdPeerStatus_Type.__name__ = "Integer32"
_Fsbgp4mpeRfdPeerStatus_Object = MibTableColumn
fsbgp4mpeRfdPeerStatus = _Fsbgp4mpeRfdPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 2, 1, 6),
    _Fsbgp4mpeRfdPeerStatus_Type()
)
fsbgp4mpeRfdPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdPeerStatus.setStatus("current")
_Fsbgp4MpeRfdRtsReuseListTable_Object = MibTable
fsbgp4MpeRfdRtsReuseListTable = _Fsbgp4MpeRfdRtsReuseListTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 3)
)
if mibBuilder.loadTexts:
    fsbgp4MpeRfdRtsReuseListTable.setStatus("current")
_Fsbgp4MpeRfdRtsReuseListEntry_Object = MibTableRow
fsbgp4MpeRfdRtsReuseListEntry = _Fsbgp4MpeRfdRtsReuseListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 3, 1)
)
fsbgp4MpeRfdRtsReuseListEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeRtAfi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeRtSafi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeRtIPPrefix"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeRtIPPrefixLen"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeRfdRtsReusePeerType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpePeerRemAddress"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeRfdRtsReuseListEntry.setStatus("current")
_Fsbgp4mpeRtAfi_Type = InetAddressType
_Fsbgp4mpeRtAfi_Object = MibTableColumn
fsbgp4mpeRtAfi = _Fsbgp4mpeRtAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 3, 1, 1),
    _Fsbgp4mpeRtAfi_Type()
)
fsbgp4mpeRtAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeRtAfi.setStatus("current")
_Fsbgp4mpeRtSafi_Type = BgpSafi
_Fsbgp4mpeRtSafi_Object = MibTableColumn
fsbgp4mpeRtSafi = _Fsbgp4mpeRtSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 3, 1, 2),
    _Fsbgp4mpeRtSafi_Type()
)
fsbgp4mpeRtSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeRtSafi.setStatus("current")
_Fsbgp4mpeRtIPPrefix_Type = InetAddress
_Fsbgp4mpeRtIPPrefix_Object = MibTableColumn
fsbgp4mpeRtIPPrefix = _Fsbgp4mpeRtIPPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 3, 1, 3),
    _Fsbgp4mpeRtIPPrefix_Type()
)
fsbgp4mpeRtIPPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeRtIPPrefix.setStatus("current")


class _Fsbgp4mpeRtIPPrefixLen_Type(Integer32):
    """Custom type fsbgp4mpeRtIPPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Fsbgp4mpeRtIPPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4mpeRtIPPrefixLen_Object = MibTableColumn
fsbgp4mpeRtIPPrefixLen = _Fsbgp4mpeRtIPPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 3, 1, 4),
    _Fsbgp4mpeRtIPPrefixLen_Type()
)
fsbgp4mpeRtIPPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeRtIPPrefixLen.setStatus("current")
_Fsbgp4mpeRfdRtsReusePeerType_Type = InetAddressType
_Fsbgp4mpeRfdRtsReusePeerType_Object = MibTableColumn
fsbgp4mpeRfdRtsReusePeerType = _Fsbgp4mpeRfdRtsReusePeerType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 3, 1, 5),
    _Fsbgp4mpeRfdRtsReusePeerType_Type()
)
fsbgp4mpeRfdRtsReusePeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdRtsReusePeerType.setStatus("current")
_Fsbgp4mpePeerRemAddress_Type = InetAddress
_Fsbgp4mpePeerRemAddress_Object = MibTableColumn
fsbgp4mpePeerRemAddress = _Fsbgp4mpePeerRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 3, 1, 6),
    _Fsbgp4mpePeerRemAddress_Type()
)
fsbgp4mpePeerRemAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpePeerRemAddress.setStatus("current")


class _Fsbgp4mpeRfdRtReuseListRtFom_Type(Integer32):
    """Custom type fsbgp4mpeRfdRtReuseListRtFom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsbgp4mpeRfdRtReuseListRtFom_Type.__name__ = "Integer32"
_Fsbgp4mpeRfdRtReuseListRtFom_Object = MibTableColumn
fsbgp4mpeRfdRtReuseListRtFom = _Fsbgp4mpeRfdRtReuseListRtFom_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 3, 1, 7),
    _Fsbgp4mpeRfdRtReuseListRtFom_Type()
)
fsbgp4mpeRfdRtReuseListRtFom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdRtReuseListRtFom.setStatus("current")


class _Fsbgp4mpeRfdRtReuseListRtLastUpdtTime_Type(Integer32):
    """Custom type fsbgp4mpeRfdRtReuseListRtLastUpdtTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsbgp4mpeRfdRtReuseListRtLastUpdtTime_Type.__name__ = "Integer32"
_Fsbgp4mpeRfdRtReuseListRtLastUpdtTime_Object = MibTableColumn
fsbgp4mpeRfdRtReuseListRtLastUpdtTime = _Fsbgp4mpeRfdRtReuseListRtLastUpdtTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 3, 1, 8),
    _Fsbgp4mpeRfdRtReuseListRtLastUpdtTime_Type()
)
fsbgp4mpeRfdRtReuseListRtLastUpdtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdRtReuseListRtLastUpdtTime.setStatus("current")


class _Fsbgp4mpeRfdRtReuseListRtState_Type(Integer32):
    """Custom type fsbgp4mpeRfdRtReuseListRtState based on Integer32"""
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


_Fsbgp4mpeRfdRtReuseListRtState_Type.__name__ = "Integer32"
_Fsbgp4mpeRfdRtReuseListRtState_Object = MibTableColumn
fsbgp4mpeRfdRtReuseListRtState = _Fsbgp4mpeRfdRtReuseListRtState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 3, 1, 9),
    _Fsbgp4mpeRfdRtReuseListRtState_Type()
)
fsbgp4mpeRfdRtReuseListRtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdRtReuseListRtState.setStatus("current")


class _Fsbgp4mpeRfdRtReuseListRtStatus_Type(Integer32):
    """Custom type fsbgp4mpeRfdRtReuseListRtStatus based on Integer32"""
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


_Fsbgp4mpeRfdRtReuseListRtStatus_Type.__name__ = "Integer32"
_Fsbgp4mpeRfdRtReuseListRtStatus_Object = MibTableColumn
fsbgp4mpeRfdRtReuseListRtStatus = _Fsbgp4mpeRfdRtReuseListRtStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 3, 1, 10),
    _Fsbgp4mpeRfdRtReuseListRtStatus_Type()
)
fsbgp4mpeRfdRtReuseListRtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdRtReuseListRtStatus.setStatus("current")
_Fsbgp4MpeRfdPeerReuseListTable_Object = MibTable
fsbgp4MpeRfdPeerReuseListTable = _Fsbgp4MpeRfdPeerReuseListTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 4)
)
if mibBuilder.loadTexts:
    fsbgp4MpeRfdPeerReuseListTable.setStatus("current")
_Fsbgp4MpeRfdPeerReuseListEntry_Object = MibTableRow
fsbgp4MpeRfdPeerReuseListEntry = _Fsbgp4MpeRfdPeerReuseListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 4, 1)
)
fsbgp4MpeRfdPeerReuseListEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeRfdPeerRemIpAddrType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeRfdPeerRemIpAddr"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeRfdPeerReuseListEntry.setStatus("current")
_Fsbgp4mpeRfdPeerRemIpAddrType_Type = InetAddressType
_Fsbgp4mpeRfdPeerRemIpAddrType_Object = MibTableColumn
fsbgp4mpeRfdPeerRemIpAddrType = _Fsbgp4mpeRfdPeerRemIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 4, 1, 1),
    _Fsbgp4mpeRfdPeerRemIpAddrType_Type()
)
fsbgp4mpeRfdPeerRemIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdPeerRemIpAddrType.setStatus("current")
_Fsbgp4mpeRfdPeerRemIpAddr_Type = InetAddress
_Fsbgp4mpeRfdPeerRemIpAddr_Object = MibTableColumn
fsbgp4mpeRfdPeerRemIpAddr = _Fsbgp4mpeRfdPeerRemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 4, 1, 2),
    _Fsbgp4mpeRfdPeerRemIpAddr_Type()
)
fsbgp4mpeRfdPeerRemIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdPeerRemIpAddr.setStatus("current")


class _Fsbgp4mpeRfdPeerReuseListPeerFom_Type(Integer32):
    """Custom type fsbgp4mpeRfdPeerReuseListPeerFom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsbgp4mpeRfdPeerReuseListPeerFom_Type.__name__ = "Integer32"
_Fsbgp4mpeRfdPeerReuseListPeerFom_Object = MibTableColumn
fsbgp4mpeRfdPeerReuseListPeerFom = _Fsbgp4mpeRfdPeerReuseListPeerFom_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 4, 1, 3),
    _Fsbgp4mpeRfdPeerReuseListPeerFom_Type()
)
fsbgp4mpeRfdPeerReuseListPeerFom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdPeerReuseListPeerFom.setStatus("current")


class _Fsbgp4mpeRfdPeerReuseListLastUpdtTime_Type(Integer32):
    """Custom type fsbgp4mpeRfdPeerReuseListLastUpdtTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Fsbgp4mpeRfdPeerReuseListLastUpdtTime_Type.__name__ = "Integer32"
_Fsbgp4mpeRfdPeerReuseListLastUpdtTime_Object = MibTableColumn
fsbgp4mpeRfdPeerReuseListLastUpdtTime = _Fsbgp4mpeRfdPeerReuseListLastUpdtTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 4, 1, 4),
    _Fsbgp4mpeRfdPeerReuseListLastUpdtTime_Type()
)
fsbgp4mpeRfdPeerReuseListLastUpdtTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdPeerReuseListLastUpdtTime.setStatus("current")


class _Fsbgp4mpeRfdPeerReuseListPeerState_Type(Integer32):
    """Custom type fsbgp4mpeRfdPeerReuseListPeerState based on Integer32"""
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


_Fsbgp4mpeRfdPeerReuseListPeerState_Type.__name__ = "Integer32"
_Fsbgp4mpeRfdPeerReuseListPeerState_Object = MibTableColumn
fsbgp4mpeRfdPeerReuseListPeerState = _Fsbgp4mpeRfdPeerReuseListPeerState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 4, 1, 5),
    _Fsbgp4mpeRfdPeerReuseListPeerState_Type()
)
fsbgp4mpeRfdPeerReuseListPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdPeerReuseListPeerState.setStatus("current")


class _Fsbgp4mpeRfdPeerReuseListPeerStatus_Type(Integer32):
    """Custom type fsbgp4mpeRfdPeerReuseListPeerStatus based on Integer32"""
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


_Fsbgp4mpeRfdPeerReuseListPeerStatus_Type.__name__ = "Integer32"
_Fsbgp4mpeRfdPeerReuseListPeerStatus_Object = MibTableColumn
fsbgp4mpeRfdPeerReuseListPeerStatus = _Fsbgp4mpeRfdPeerReuseListPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 28, 4, 1, 6),
    _Fsbgp4mpeRfdPeerReuseListPeerStatus_Type()
)
fsbgp4mpeRfdPeerReuseListPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRfdPeerReuseListPeerStatus.setStatus("current")
_FsbgpMpeComm_ObjectIdentity = ObjectIdentity
fsbgpMpeComm = _FsbgpMpeComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29)
)
_Fsbgp4MpeCommRouteAddCommTable_Object = MibTable
fsbgp4MpeCommRouteAddCommTable = _Fsbgp4MpeCommRouteAddCommTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 1)
)
if mibBuilder.loadTexts:
    fsbgp4MpeCommRouteAddCommTable.setStatus("current")
_Fsbgp4MpeCommRouteAddCommEntry_Object = MibTableRow
fsbgp4MpeCommRouteAddCommEntry = _Fsbgp4MpeCommRouteAddCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 1, 1)
)
fsbgp4MpeCommRouteAddCommEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeAddCommRtAfi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeAddCommRtSafi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeAddCommIpNetwork"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeAddCommIpPrefixLen"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeAddCommVal"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeCommRouteAddCommEntry.setStatus("current")
_Fsbgp4mpeAddCommRtAfi_Type = InetAddressType
_Fsbgp4mpeAddCommRtAfi_Object = MibTableColumn
fsbgp4mpeAddCommRtAfi = _Fsbgp4mpeAddCommRtAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 1, 1, 1),
    _Fsbgp4mpeAddCommRtAfi_Type()
)
fsbgp4mpeAddCommRtAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeAddCommRtAfi.setStatus("current")
_Fsbgp4mpeAddCommRtSafi_Type = BgpSafi
_Fsbgp4mpeAddCommRtSafi_Object = MibTableColumn
fsbgp4mpeAddCommRtSafi = _Fsbgp4mpeAddCommRtSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 1, 1, 2),
    _Fsbgp4mpeAddCommRtSafi_Type()
)
fsbgp4mpeAddCommRtSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeAddCommRtSafi.setStatus("current")
_Fsbgp4mpeAddCommIpNetwork_Type = InetAddress
_Fsbgp4mpeAddCommIpNetwork_Object = MibTableColumn
fsbgp4mpeAddCommIpNetwork = _Fsbgp4mpeAddCommIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 1, 1, 3),
    _Fsbgp4mpeAddCommIpNetwork_Type()
)
fsbgp4mpeAddCommIpNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeAddCommIpNetwork.setStatus("current")


class _Fsbgp4mpeAddCommIpPrefixLen_Type(Integer32):
    """Custom type fsbgp4mpeAddCommIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fsbgp4mpeAddCommIpPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4mpeAddCommIpPrefixLen_Object = MibTableColumn
fsbgp4mpeAddCommIpPrefixLen = _Fsbgp4mpeAddCommIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 1, 1, 4),
    _Fsbgp4mpeAddCommIpPrefixLen_Type()
)
fsbgp4mpeAddCommIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeAddCommIpPrefixLen.setStatus("current")


class _Fsbgp4mpeAddCommVal_Type(Unsigned32):
    """Custom type fsbgp4mpeAddCommVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65536, 4294901759),
        ValueRangeConstraint(4294967041, 4294967043),
    )


_Fsbgp4mpeAddCommVal_Type.__name__ = "Unsigned32"
_Fsbgp4mpeAddCommVal_Object = MibTableColumn
fsbgp4mpeAddCommVal = _Fsbgp4mpeAddCommVal_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 1, 1, 5),
    _Fsbgp4mpeAddCommVal_Type()
)
fsbgp4mpeAddCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeAddCommVal.setStatus("current")
_Fsbgp4mpeAddCommRowStatus_Type = RowStatus
_Fsbgp4mpeAddCommRowStatus_Object = MibTableColumn
fsbgp4mpeAddCommRowStatus = _Fsbgp4mpeAddCommRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 1, 1, 6),
    _Fsbgp4mpeAddCommRowStatus_Type()
)
fsbgp4mpeAddCommRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4mpeAddCommRowStatus.setStatus("current")
_Fsbgp4MpeCommRouteDeleteCommTable_Object = MibTable
fsbgp4MpeCommRouteDeleteCommTable = _Fsbgp4MpeCommRouteDeleteCommTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 2)
)
if mibBuilder.loadTexts:
    fsbgp4MpeCommRouteDeleteCommTable.setStatus("current")
_Fsbgp4MpeCommRouteDeleteCommEntry_Object = MibTableRow
fsbgp4MpeCommRouteDeleteCommEntry = _Fsbgp4MpeCommRouteDeleteCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 2, 1)
)
fsbgp4MpeCommRouteDeleteCommEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeDeleteCommRtAfi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeDeleteCommRtSafi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeDeleteCommIpNetwork"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeDeleteCommIpPrefixLen"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeDeleteCommVal"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeCommRouteDeleteCommEntry.setStatus("current")
_Fsbgp4mpeDeleteCommRtAfi_Type = InetAddressType
_Fsbgp4mpeDeleteCommRtAfi_Object = MibTableColumn
fsbgp4mpeDeleteCommRtAfi = _Fsbgp4mpeDeleteCommRtAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 2, 1, 1),
    _Fsbgp4mpeDeleteCommRtAfi_Type()
)
fsbgp4mpeDeleteCommRtAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeDeleteCommRtAfi.setStatus("current")
_Fsbgp4mpeDeleteCommRtSafi_Type = BgpSafi
_Fsbgp4mpeDeleteCommRtSafi_Object = MibTableColumn
fsbgp4mpeDeleteCommRtSafi = _Fsbgp4mpeDeleteCommRtSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 2, 1, 2),
    _Fsbgp4mpeDeleteCommRtSafi_Type()
)
fsbgp4mpeDeleteCommRtSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeDeleteCommRtSafi.setStatus("current")
_Fsbgp4mpeDeleteCommIpNetwork_Type = InetAddress
_Fsbgp4mpeDeleteCommIpNetwork_Object = MibTableColumn
fsbgp4mpeDeleteCommIpNetwork = _Fsbgp4mpeDeleteCommIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 2, 1, 3),
    _Fsbgp4mpeDeleteCommIpNetwork_Type()
)
fsbgp4mpeDeleteCommIpNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeDeleteCommIpNetwork.setStatus("current")


class _Fsbgp4mpeDeleteCommIpPrefixLen_Type(Integer32):
    """Custom type fsbgp4mpeDeleteCommIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fsbgp4mpeDeleteCommIpPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4mpeDeleteCommIpPrefixLen_Object = MibTableColumn
fsbgp4mpeDeleteCommIpPrefixLen = _Fsbgp4mpeDeleteCommIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 2, 1, 4),
    _Fsbgp4mpeDeleteCommIpPrefixLen_Type()
)
fsbgp4mpeDeleteCommIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeDeleteCommIpPrefixLen.setStatus("current")


class _Fsbgp4mpeDeleteCommVal_Type(Unsigned32):
    """Custom type fsbgp4mpeDeleteCommVal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65536, 4294901759),
        ValueRangeConstraint(4294967041, 4294967043),
    )


_Fsbgp4mpeDeleteCommVal_Type.__name__ = "Unsigned32"
_Fsbgp4mpeDeleteCommVal_Object = MibTableColumn
fsbgp4mpeDeleteCommVal = _Fsbgp4mpeDeleteCommVal_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 2, 1, 5),
    _Fsbgp4mpeDeleteCommVal_Type()
)
fsbgp4mpeDeleteCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeDeleteCommVal.setStatus("current")
_Fsbgp4mpeDeleteCommRowStatus_Type = RowStatus
_Fsbgp4mpeDeleteCommRowStatus_Object = MibTableColumn
fsbgp4mpeDeleteCommRowStatus = _Fsbgp4mpeDeleteCommRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 2, 1, 6),
    _Fsbgp4mpeDeleteCommRowStatus_Type()
)
fsbgp4mpeDeleteCommRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4mpeDeleteCommRowStatus.setStatus("current")
_Fsbgp4MpeCommRouteCommSetStatusTable_Object = MibTable
fsbgp4MpeCommRouteCommSetStatusTable = _Fsbgp4MpeCommRouteCommSetStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 3)
)
if mibBuilder.loadTexts:
    fsbgp4MpeCommRouteCommSetStatusTable.setStatus("current")
_Fsbgp4MpeCommRouteCommSetStatusEntry_Object = MibTableRow
fsbgp4MpeCommRouteCommSetStatusEntry = _Fsbgp4MpeCommRouteCommSetStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 3, 1)
)
fsbgp4MpeCommRouteCommSetStatusEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeCommSetStatusAfi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeCommSetStatusSafi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeCommSetStatusIpNetwork"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeCommSetStatusIpPrefixLen"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeCommRouteCommSetStatusEntry.setStatus("current")
_Fsbgp4mpeCommSetStatusAfi_Type = InetAddressType
_Fsbgp4mpeCommSetStatusAfi_Object = MibTableColumn
fsbgp4mpeCommSetStatusAfi = _Fsbgp4mpeCommSetStatusAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 3, 1, 1),
    _Fsbgp4mpeCommSetStatusAfi_Type()
)
fsbgp4mpeCommSetStatusAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeCommSetStatusAfi.setStatus("current")
_Fsbgp4mpeCommSetStatusSafi_Type = BgpSafi
_Fsbgp4mpeCommSetStatusSafi_Object = MibTableColumn
fsbgp4mpeCommSetStatusSafi = _Fsbgp4mpeCommSetStatusSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 3, 1, 2),
    _Fsbgp4mpeCommSetStatusSafi_Type()
)
fsbgp4mpeCommSetStatusSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeCommSetStatusSafi.setStatus("current")
_Fsbgp4mpeCommSetStatusIpNetwork_Type = InetAddress
_Fsbgp4mpeCommSetStatusIpNetwork_Object = MibTableColumn
fsbgp4mpeCommSetStatusIpNetwork = _Fsbgp4mpeCommSetStatusIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 3, 1, 3),
    _Fsbgp4mpeCommSetStatusIpNetwork_Type()
)
fsbgp4mpeCommSetStatusIpNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeCommSetStatusIpNetwork.setStatus("current")


class _Fsbgp4mpeCommSetStatusIpPrefixLen_Type(Integer32):
    """Custom type fsbgp4mpeCommSetStatusIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fsbgp4mpeCommSetStatusIpPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4mpeCommSetStatusIpPrefixLen_Object = MibTableColumn
fsbgp4mpeCommSetStatusIpPrefixLen = _Fsbgp4mpeCommSetStatusIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 3, 1, 4),
    _Fsbgp4mpeCommSetStatusIpPrefixLen_Type()
)
fsbgp4mpeCommSetStatusIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeCommSetStatusIpPrefixLen.setStatus("current")


class _Fsbgp4mpeCommSetStatus_Type(Integer32):
    """Custom type fsbgp4mpeCommSetStatus based on Integer32"""
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


_Fsbgp4mpeCommSetStatus_Type.__name__ = "Integer32"
_Fsbgp4mpeCommSetStatus_Object = MibTableColumn
fsbgp4mpeCommSetStatus = _Fsbgp4mpeCommSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 3, 1, 5),
    _Fsbgp4mpeCommSetStatus_Type()
)
fsbgp4mpeCommSetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4mpeCommSetStatus.setStatus("current")
_Fsbgp4mpeCommSetStatusRowStatus_Type = RowStatus
_Fsbgp4mpeCommSetStatusRowStatus_Object = MibTableColumn
fsbgp4mpeCommSetStatusRowStatus = _Fsbgp4mpeCommSetStatusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 29, 3, 1, 6),
    _Fsbgp4mpeCommSetStatusRowStatus_Type()
)
fsbgp4mpeCommSetStatusRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4mpeCommSetStatusRowStatus.setStatus("current")
_FsbgpMpeExtComm_ObjectIdentity = ObjectIdentity
fsbgpMpeExtComm = _FsbgpMpeExtComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30)
)
_Fsbgp4MpeExtCommRouteAddExtCommTable_Object = MibTable
fsbgp4MpeExtCommRouteAddExtCommTable = _Fsbgp4MpeExtCommRouteAddExtCommTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 1)
)
if mibBuilder.loadTexts:
    fsbgp4MpeExtCommRouteAddExtCommTable.setStatus("current")
_Fsbgp4MpeExtCommRouteAddExtCommEntry_Object = MibTableRow
fsbgp4MpeExtCommRouteAddExtCommEntry = _Fsbgp4MpeExtCommRouteAddExtCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 1, 1)
)
fsbgp4MpeExtCommRouteAddExtCommEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeAddExtCommRtAfi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeAddExtCommRtSafi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeAddExtCommIpNetwork"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeAddExtCommIpPrefixLen"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeAddExtCommVal"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeExtCommRouteAddExtCommEntry.setStatus("current")
_Fsbgp4mpeAddExtCommRtAfi_Type = InetAddressType
_Fsbgp4mpeAddExtCommRtAfi_Object = MibTableColumn
fsbgp4mpeAddExtCommRtAfi = _Fsbgp4mpeAddExtCommRtAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 1, 1, 1),
    _Fsbgp4mpeAddExtCommRtAfi_Type()
)
fsbgp4mpeAddExtCommRtAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeAddExtCommRtAfi.setStatus("current")
_Fsbgp4mpeAddExtCommRtSafi_Type = BgpSafi
_Fsbgp4mpeAddExtCommRtSafi_Object = MibTableColumn
fsbgp4mpeAddExtCommRtSafi = _Fsbgp4mpeAddExtCommRtSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 1, 1, 2),
    _Fsbgp4mpeAddExtCommRtSafi_Type()
)
fsbgp4mpeAddExtCommRtSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeAddExtCommRtSafi.setStatus("current")
_Fsbgp4mpeAddExtCommIpNetwork_Type = InetAddress
_Fsbgp4mpeAddExtCommIpNetwork_Object = MibTableColumn
fsbgp4mpeAddExtCommIpNetwork = _Fsbgp4mpeAddExtCommIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 1, 1, 3),
    _Fsbgp4mpeAddExtCommIpNetwork_Type()
)
fsbgp4mpeAddExtCommIpNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeAddExtCommIpNetwork.setStatus("current")


class _Fsbgp4mpeAddExtCommIpPrefixLen_Type(Integer32):
    """Custom type fsbgp4mpeAddExtCommIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fsbgp4mpeAddExtCommIpPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4mpeAddExtCommIpPrefixLen_Object = MibTableColumn
fsbgp4mpeAddExtCommIpPrefixLen = _Fsbgp4mpeAddExtCommIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 1, 1, 4),
    _Fsbgp4mpeAddExtCommIpPrefixLen_Type()
)
fsbgp4mpeAddExtCommIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeAddExtCommIpPrefixLen.setStatus("current")


class _Fsbgp4mpeAddExtCommVal_Type(OctetString):
    """Custom type fsbgp4mpeAddExtCommVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Fsbgp4mpeAddExtCommVal_Type.__name__ = "OctetString"
_Fsbgp4mpeAddExtCommVal_Object = MibTableColumn
fsbgp4mpeAddExtCommVal = _Fsbgp4mpeAddExtCommVal_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 1, 1, 5),
    _Fsbgp4mpeAddExtCommVal_Type()
)
fsbgp4mpeAddExtCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeAddExtCommVal.setStatus("current")
_Fsbgp4mpeAddExtCommRowStatus_Type = RowStatus
_Fsbgp4mpeAddExtCommRowStatus_Object = MibTableColumn
fsbgp4mpeAddExtCommRowStatus = _Fsbgp4mpeAddExtCommRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 1, 1, 6),
    _Fsbgp4mpeAddExtCommRowStatus_Type()
)
fsbgp4mpeAddExtCommRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4mpeAddExtCommRowStatus.setStatus("current")
_Fsbgp4MpeExtCommRouteDeleteExtCommTable_Object = MibTable
fsbgp4MpeExtCommRouteDeleteExtCommTable = _Fsbgp4MpeExtCommRouteDeleteExtCommTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 2)
)
if mibBuilder.loadTexts:
    fsbgp4MpeExtCommRouteDeleteExtCommTable.setStatus("current")
_Fsbgp4MpeExtCommRouteDeleteExtCommEntry_Object = MibTableRow
fsbgp4MpeExtCommRouteDeleteExtCommEntry = _Fsbgp4MpeExtCommRouteDeleteExtCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 2, 1)
)
fsbgp4MpeExtCommRouteDeleteExtCommEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeDeleteExtCommRtAfi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeDeleteExtCommRtSafi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeDeleteExtCommIpNetwork"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeDeleteExtCommIpPrefixLen"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeDeleteExtCommVal"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeExtCommRouteDeleteExtCommEntry.setStatus("current")
_Fsbgp4mpeDeleteExtCommRtAfi_Type = InetAddressType
_Fsbgp4mpeDeleteExtCommRtAfi_Object = MibTableColumn
fsbgp4mpeDeleteExtCommRtAfi = _Fsbgp4mpeDeleteExtCommRtAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 2, 1, 1),
    _Fsbgp4mpeDeleteExtCommRtAfi_Type()
)
fsbgp4mpeDeleteExtCommRtAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeDeleteExtCommRtAfi.setStatus("current")
_Fsbgp4mpeDeleteExtCommRtSafi_Type = BgpSafi
_Fsbgp4mpeDeleteExtCommRtSafi_Object = MibTableColumn
fsbgp4mpeDeleteExtCommRtSafi = _Fsbgp4mpeDeleteExtCommRtSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 2, 1, 2),
    _Fsbgp4mpeDeleteExtCommRtSafi_Type()
)
fsbgp4mpeDeleteExtCommRtSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeDeleteExtCommRtSafi.setStatus("current")
_Fsbgp4mpeDeleteExtCommIpNetwork_Type = InetAddress
_Fsbgp4mpeDeleteExtCommIpNetwork_Object = MibTableColumn
fsbgp4mpeDeleteExtCommIpNetwork = _Fsbgp4mpeDeleteExtCommIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 2, 1, 3),
    _Fsbgp4mpeDeleteExtCommIpNetwork_Type()
)
fsbgp4mpeDeleteExtCommIpNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeDeleteExtCommIpNetwork.setStatus("current")


class _Fsbgp4mpeDeleteExtCommIpPrefixLen_Type(Integer32):
    """Custom type fsbgp4mpeDeleteExtCommIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fsbgp4mpeDeleteExtCommIpPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4mpeDeleteExtCommIpPrefixLen_Object = MibTableColumn
fsbgp4mpeDeleteExtCommIpPrefixLen = _Fsbgp4mpeDeleteExtCommIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 2, 1, 4),
    _Fsbgp4mpeDeleteExtCommIpPrefixLen_Type()
)
fsbgp4mpeDeleteExtCommIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeDeleteExtCommIpPrefixLen.setStatus("current")


class _Fsbgp4mpeDeleteExtCommVal_Type(OctetString):
    """Custom type fsbgp4mpeDeleteExtCommVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Fsbgp4mpeDeleteExtCommVal_Type.__name__ = "OctetString"
_Fsbgp4mpeDeleteExtCommVal_Object = MibTableColumn
fsbgp4mpeDeleteExtCommVal = _Fsbgp4mpeDeleteExtCommVal_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 2, 1, 5),
    _Fsbgp4mpeDeleteExtCommVal_Type()
)
fsbgp4mpeDeleteExtCommVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeDeleteExtCommVal.setStatus("current")
_Fsbgp4mpeDeleteExtCommRowStatus_Type = RowStatus
_Fsbgp4mpeDeleteExtCommRowStatus_Object = MibTableColumn
fsbgp4mpeDeleteExtCommRowStatus = _Fsbgp4mpeDeleteExtCommRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 2, 1, 6),
    _Fsbgp4mpeDeleteExtCommRowStatus_Type()
)
fsbgp4mpeDeleteExtCommRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4mpeDeleteExtCommRowStatus.setStatus("current")
_Fsbgp4MpeExtCommRouteExtCommSetStatusTable_Object = MibTable
fsbgp4MpeExtCommRouteExtCommSetStatusTable = _Fsbgp4MpeExtCommRouteExtCommSetStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 3)
)
if mibBuilder.loadTexts:
    fsbgp4MpeExtCommRouteExtCommSetStatusTable.setStatus("current")
_Fsbgp4MpeExtCommRouteExtCommSetStatusEntry_Object = MibTableRow
fsbgp4MpeExtCommRouteExtCommSetStatusEntry = _Fsbgp4MpeExtCommRouteExtCommSetStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 3, 1)
)
fsbgp4MpeExtCommRouteExtCommSetStatusEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeExtCommSetStatusRtAfi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeExtCommSetStatusRtSafi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeExtCommSetStatusIpNetwork"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeExtCommSetStatusIpPrefixLen"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeExtCommRouteExtCommSetStatusEntry.setStatus("current")
_Fsbgp4mpeExtCommSetStatusRtAfi_Type = InetAddressType
_Fsbgp4mpeExtCommSetStatusRtAfi_Object = MibTableColumn
fsbgp4mpeExtCommSetStatusRtAfi = _Fsbgp4mpeExtCommSetStatusRtAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 3, 1, 1),
    _Fsbgp4mpeExtCommSetStatusRtAfi_Type()
)
fsbgp4mpeExtCommSetStatusRtAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeExtCommSetStatusRtAfi.setStatus("current")
_Fsbgp4mpeExtCommSetStatusRtSafi_Type = BgpSafi
_Fsbgp4mpeExtCommSetStatusRtSafi_Object = MibTableColumn
fsbgp4mpeExtCommSetStatusRtSafi = _Fsbgp4mpeExtCommSetStatusRtSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 3, 1, 2),
    _Fsbgp4mpeExtCommSetStatusRtSafi_Type()
)
fsbgp4mpeExtCommSetStatusRtSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeExtCommSetStatusRtSafi.setStatus("current")
_Fsbgp4mpeExtCommSetStatusIpNetwork_Type = InetAddress
_Fsbgp4mpeExtCommSetStatusIpNetwork_Object = MibTableColumn
fsbgp4mpeExtCommSetStatusIpNetwork = _Fsbgp4mpeExtCommSetStatusIpNetwork_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 3, 1, 3),
    _Fsbgp4mpeExtCommSetStatusIpNetwork_Type()
)
fsbgp4mpeExtCommSetStatusIpNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeExtCommSetStatusIpNetwork.setStatus("current")


class _Fsbgp4mpeExtCommSetStatusIpPrefixLen_Type(Integer32):
    """Custom type fsbgp4mpeExtCommSetStatusIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Fsbgp4mpeExtCommSetStatusIpPrefixLen_Type.__name__ = "Integer32"
_Fsbgp4mpeExtCommSetStatusIpPrefixLen_Object = MibTableColumn
fsbgp4mpeExtCommSetStatusIpPrefixLen = _Fsbgp4mpeExtCommSetStatusIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 3, 1, 4),
    _Fsbgp4mpeExtCommSetStatusIpPrefixLen_Type()
)
fsbgp4mpeExtCommSetStatusIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeExtCommSetStatusIpPrefixLen.setStatus("current")


class _Fsbgp4mpeExtCommSetStatus_Type(Integer32):
    """Custom type fsbgp4mpeExtCommSetStatus based on Integer32"""
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


_Fsbgp4mpeExtCommSetStatus_Type.__name__ = "Integer32"
_Fsbgp4mpeExtCommSetStatus_Object = MibTableColumn
fsbgp4mpeExtCommSetStatus = _Fsbgp4mpeExtCommSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 3, 1, 5),
    _Fsbgp4mpeExtCommSetStatus_Type()
)
fsbgp4mpeExtCommSetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4mpeExtCommSetStatus.setStatus("current")
_Fsbgp4mpeExtCommSetStatusRowStatus_Type = RowStatus
_Fsbgp4mpeExtCommSetStatusRowStatus_Object = MibTableColumn
fsbgp4mpeExtCommSetStatusRowStatus = _Fsbgp4mpeExtCommSetStatusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 3, 1, 6),
    _Fsbgp4mpeExtCommSetStatusRowStatus_Type()
)
fsbgp4mpeExtCommSetStatusRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4mpeExtCommSetStatusRowStatus.setStatus("current")
_Fsbgp4MpePeerLinkBwTable_Object = MibTable
fsbgp4MpePeerLinkBwTable = _Fsbgp4MpePeerLinkBwTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 4)
)
if mibBuilder.loadTexts:
    fsbgp4MpePeerLinkBwTable.setStatus("current")
_Fsbgp4MpePeerLinkBwEntry_Object = MibTableRow
fsbgp4MpePeerLinkBwEntry = _Fsbgp4MpePeerLinkBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 4, 1)
)
fsbgp4MpePeerLinkBwEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpePeerLinkType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpePeerLinkRemAddr"),
)
if mibBuilder.loadTexts:
    fsbgp4MpePeerLinkBwEntry.setStatus("current")
_Fsbgp4mpePeerLinkType_Type = InetAddressType
_Fsbgp4mpePeerLinkType_Object = MibTableColumn
fsbgp4mpePeerLinkType = _Fsbgp4mpePeerLinkType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 4, 1, 1),
    _Fsbgp4mpePeerLinkType_Type()
)
fsbgp4mpePeerLinkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpePeerLinkType.setStatus("current")
_Fsbgp4mpePeerLinkRemAddr_Type = InetAddress
_Fsbgp4mpePeerLinkRemAddr_Object = MibTableColumn
fsbgp4mpePeerLinkRemAddr = _Fsbgp4mpePeerLinkRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 4, 1, 2),
    _Fsbgp4mpePeerLinkRemAddr_Type()
)
fsbgp4mpePeerLinkRemAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpePeerLinkRemAddr.setStatus("current")


class _Fsbgp4mpeLinkBandWidth_Type(Unsigned32):
    """Custom type fsbgp4mpeLinkBandWidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7000, 4294967295),
    )


_Fsbgp4mpeLinkBandWidth_Type.__name__ = "Unsigned32"
_Fsbgp4mpeLinkBandWidth_Object = MibTableColumn
fsbgp4mpeLinkBandWidth = _Fsbgp4mpeLinkBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 4, 1, 3),
    _Fsbgp4mpeLinkBandWidth_Type()
)
fsbgp4mpeLinkBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4mpeLinkBandWidth.setStatus("current")
_Fsbgp4mpePeerLinkBwRowStatus_Type = RowStatus
_Fsbgp4mpePeerLinkBwRowStatus_Object = MibTableColumn
fsbgp4mpePeerLinkBwRowStatus = _Fsbgp4mpePeerLinkBwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 30, 4, 1, 4),
    _Fsbgp4mpePeerLinkBwRowStatus_Type()
)
fsbgp4mpePeerLinkBwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4mpePeerLinkBwRowStatus.setStatus("current")
_FsbgpMpeCaps_ObjectIdentity = ObjectIdentity
fsbgpMpeCaps = _FsbgpMpeCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 31)
)
_Fsbgp4MpeCapSupportedCapsTable_Object = MibTable
fsbgp4MpeCapSupportedCapsTable = _Fsbgp4MpeCapSupportedCapsTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 31, 1)
)
if mibBuilder.loadTexts:
    fsbgp4MpeCapSupportedCapsTable.setStatus("current")
_Fsbgp4MpeCapSupportedCapsEntry_Object = MibTableRow
fsbgp4MpeCapSupportedCapsEntry = _Fsbgp4MpeCapSupportedCapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 31, 1, 1)
)
fsbgp4MpeCapSupportedCapsEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeCapPeerType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeCapPeerRemoteIpAddr"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeSupportedCapabilityCode"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeSupportedCapabilityLength"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeSupportedCapabilityValue"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeCapSupportedCapsEntry.setStatus("current")
_Fsbgp4mpeCapPeerType_Type = InetAddressType
_Fsbgp4mpeCapPeerType_Object = MibTableColumn
fsbgp4mpeCapPeerType = _Fsbgp4mpeCapPeerType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 31, 1, 1, 1),
    _Fsbgp4mpeCapPeerType_Type()
)
fsbgp4mpeCapPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeCapPeerType.setStatus("current")


class _Fsbgp4mpeCapPeerRemoteIpAddr_Type(InetAddress):
    """Custom type fsbgp4mpeCapPeerRemoteIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_Fsbgp4mpeCapPeerRemoteIpAddr_Type.__name__ = "InetAddress"
_Fsbgp4mpeCapPeerRemoteIpAddr_Object = MibTableColumn
fsbgp4mpeCapPeerRemoteIpAddr = _Fsbgp4mpeCapPeerRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 31, 1, 1, 2),
    _Fsbgp4mpeCapPeerRemoteIpAddr_Type()
)
fsbgp4mpeCapPeerRemoteIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeCapPeerRemoteIpAddr.setStatus("current")


class _Fsbgp4mpeSupportedCapabilityCode_Type(Integer32):
    """Custom type fsbgp4mpeSupportedCapabilityCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fsbgp4mpeSupportedCapabilityCode_Type.__name__ = "Integer32"
_Fsbgp4mpeSupportedCapabilityCode_Object = MibTableColumn
fsbgp4mpeSupportedCapabilityCode = _Fsbgp4mpeSupportedCapabilityCode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 31, 1, 1, 3),
    _Fsbgp4mpeSupportedCapabilityCode_Type()
)
fsbgp4mpeSupportedCapabilityCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeSupportedCapabilityCode.setStatus("current")


class _Fsbgp4mpeSupportedCapabilityLength_Type(Integer32):
    """Custom type fsbgp4mpeSupportedCapabilityLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 251),
    )


_Fsbgp4mpeSupportedCapabilityLength_Type.__name__ = "Integer32"
_Fsbgp4mpeSupportedCapabilityLength_Object = MibTableColumn
fsbgp4mpeSupportedCapabilityLength = _Fsbgp4mpeSupportedCapabilityLength_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 31, 1, 1, 5),
    _Fsbgp4mpeSupportedCapabilityLength_Type()
)
fsbgp4mpeSupportedCapabilityLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeSupportedCapabilityLength.setStatus("current")


class _Fsbgp4mpeSupportedCapabilityValue_Type(OctetString):
    """Custom type fsbgp4mpeSupportedCapabilityValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Fsbgp4mpeSupportedCapabilityValue_Type.__name__ = "OctetString"
_Fsbgp4mpeSupportedCapabilityValue_Object = MibTableColumn
fsbgp4mpeSupportedCapabilityValue = _Fsbgp4mpeSupportedCapabilityValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 31, 1, 1, 6),
    _Fsbgp4mpeSupportedCapabilityValue_Type()
)
fsbgp4mpeSupportedCapabilityValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeSupportedCapabilityValue.setStatus("current")
_Fsbgp4mpeCapSupportedCapsRowStatus_Type = RowStatus
_Fsbgp4mpeCapSupportedCapsRowStatus_Object = MibTableColumn
fsbgp4mpeCapSupportedCapsRowStatus = _Fsbgp4mpeCapSupportedCapsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 31, 1, 1, 7),
    _Fsbgp4mpeCapSupportedCapsRowStatus_Type()
)
fsbgp4mpeCapSupportedCapsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4mpeCapSupportedCapsRowStatus.setStatus("current")


class _Fsbgp4mpeCapAnnouncedStatus_Type(Integer32):
    """Custom type fsbgp4mpeCapAnnouncedStatus based on Integer32"""
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


_Fsbgp4mpeCapAnnouncedStatus_Type.__name__ = "Integer32"
_Fsbgp4mpeCapAnnouncedStatus_Object = MibTableColumn
fsbgp4mpeCapAnnouncedStatus = _Fsbgp4mpeCapAnnouncedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 31, 1, 1, 8),
    _Fsbgp4mpeCapAnnouncedStatus_Type()
)
fsbgp4mpeCapAnnouncedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeCapAnnouncedStatus.setStatus("current")


class _Fsbgp4mpeCapReceivedStatus_Type(Integer32):
    """Custom type fsbgp4mpeCapReceivedStatus based on Integer32"""
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


_Fsbgp4mpeCapReceivedStatus_Type.__name__ = "Integer32"
_Fsbgp4mpeCapReceivedStatus_Object = MibTableColumn
fsbgp4mpeCapReceivedStatus = _Fsbgp4mpeCapReceivedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 31, 1, 1, 9),
    _Fsbgp4mpeCapReceivedStatus_Type()
)
fsbgp4mpeCapReceivedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeCapReceivedStatus.setStatus("current")


class _Fsbgp4mpeCapNegotiatedStatus_Type(Integer32):
    """Custom type fsbgp4mpeCapNegotiatedStatus based on Integer32"""
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


_Fsbgp4mpeCapNegotiatedStatus_Type.__name__ = "Integer32"
_Fsbgp4mpeCapNegotiatedStatus_Object = MibTableColumn
fsbgp4mpeCapNegotiatedStatus = _Fsbgp4mpeCapNegotiatedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 31, 1, 1, 10),
    _Fsbgp4mpeCapNegotiatedStatus_Type()
)
fsbgp4mpeCapNegotiatedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeCapNegotiatedStatus.setStatus("current")


class _Fsbgp4mpeCapConfiguredStatus_Type(Integer32):
    """Custom type fsbgp4mpeCapConfiguredStatus based on Integer32"""
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


_Fsbgp4mpeCapConfiguredStatus_Type.__name__ = "Integer32"
_Fsbgp4mpeCapConfiguredStatus_Object = MibTableColumn
fsbgp4mpeCapConfiguredStatus = _Fsbgp4mpeCapConfiguredStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 31, 1, 1, 11),
    _Fsbgp4mpeCapConfiguredStatus_Type()
)
fsbgp4mpeCapConfiguredStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeCapConfiguredStatus.setStatus("current")
_Fsbgp4MpeRtRefresh_ObjectIdentity = ObjectIdentity
fsbgp4MpeRtRefresh = _Fsbgp4MpeRtRefresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32)
)
_Fsbgp4MpeRtRefreshInboundTable_Object = MibTable
fsbgp4MpeRtRefreshInboundTable = _Fsbgp4MpeRtRefreshInboundTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32, 1)
)
if mibBuilder.loadTexts:
    fsbgp4MpeRtRefreshInboundTable.setStatus("current")
_Fsbgp4MpeRtRefreshInboundEntry_Object = MibTableRow
fsbgp4MpeRtRefreshInboundEntry = _Fsbgp4MpeRtRefreshInboundEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32, 1, 1)
)
fsbgp4MpeRtRefreshInboundEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeRtRefreshInboundPeerType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeRtRefreshInboundPeerAddr"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeRtRefreshInboundAfi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeRtRefreshInboundSafi"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeRtRefreshInboundEntry.setStatus("current")
_Fsbgp4mpeRtRefreshInboundPeerType_Type = InetAddressType
_Fsbgp4mpeRtRefreshInboundPeerType_Object = MibTableColumn
fsbgp4mpeRtRefreshInboundPeerType = _Fsbgp4mpeRtRefreshInboundPeerType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32, 1, 1, 1),
    _Fsbgp4mpeRtRefreshInboundPeerType_Type()
)
fsbgp4mpeRtRefreshInboundPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeRtRefreshInboundPeerType.setStatus("current")
_Fsbgp4mpeRtRefreshInboundPeerAddr_Type = InetAddress
_Fsbgp4mpeRtRefreshInboundPeerAddr_Object = MibTableColumn
fsbgp4mpeRtRefreshInboundPeerAddr = _Fsbgp4mpeRtRefreshInboundPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32, 1, 1, 2),
    _Fsbgp4mpeRtRefreshInboundPeerAddr_Type()
)
fsbgp4mpeRtRefreshInboundPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeRtRefreshInboundPeerAddr.setStatus("current")
_Fsbgp4mpeRtRefreshInboundAfi_Type = InetAddressType
_Fsbgp4mpeRtRefreshInboundAfi_Object = MibTableColumn
fsbgp4mpeRtRefreshInboundAfi = _Fsbgp4mpeRtRefreshInboundAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32, 1, 1, 3),
    _Fsbgp4mpeRtRefreshInboundAfi_Type()
)
fsbgp4mpeRtRefreshInboundAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeRtRefreshInboundAfi.setStatus("current")
_Fsbgp4mpeRtRefreshInboundSafi_Type = BgpSafi
_Fsbgp4mpeRtRefreshInboundSafi_Object = MibTableColumn
fsbgp4mpeRtRefreshInboundSafi = _Fsbgp4mpeRtRefreshInboundSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32, 1, 1, 4),
    _Fsbgp4mpeRtRefreshInboundSafi_Type()
)
fsbgp4mpeRtRefreshInboundSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeRtRefreshInboundSafi.setStatus("current")


class _Fsbgp4mpeRtRefreshInboundRequest_Type(Integer32):
    """Custom type fsbgp4mpeRtRefreshInboundRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_Fsbgp4mpeRtRefreshInboundRequest_Type.__name__ = "Integer32"
_Fsbgp4mpeRtRefreshInboundRequest_Object = MibTableColumn
fsbgp4mpeRtRefreshInboundRequest = _Fsbgp4mpeRtRefreshInboundRequest_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32, 1, 1, 5),
    _Fsbgp4mpeRtRefreshInboundRequest_Type()
)
fsbgp4mpeRtRefreshInboundRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeRtRefreshInboundRequest.setStatus("current")


class _Fsbgp4mpeRtRefreshInboundPrefixFilter_Type(Integer32):
    """Custom type fsbgp4mpeRtRefreshInboundPrefixFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_Fsbgp4mpeRtRefreshInboundPrefixFilter_Type.__name__ = "Integer32"
_Fsbgp4mpeRtRefreshInboundPrefixFilter_Object = MibTableColumn
fsbgp4mpeRtRefreshInboundPrefixFilter = _Fsbgp4mpeRtRefreshInboundPrefixFilter_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32, 1, 1, 6),
    _Fsbgp4mpeRtRefreshInboundPrefixFilter_Type()
)
fsbgp4mpeRtRefreshInboundPrefixFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeRtRefreshInboundPrefixFilter.setStatus("current")
_Fsbgp4MpeRtRefreshStatisticsTable_Object = MibTable
fsbgp4MpeRtRefreshStatisticsTable = _Fsbgp4MpeRtRefreshStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32, 2)
)
if mibBuilder.loadTexts:
    fsbgp4MpeRtRefreshStatisticsTable.setStatus("current")
_Fsbgp4MpeRtRefreshStatisticsEntry_Object = MibTableRow
fsbgp4MpeRtRefreshStatisticsEntry = _Fsbgp4MpeRtRefreshStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32, 2, 1)
)
fsbgp4MpeRtRefreshStatisticsEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeRtRefreshStatisticsPeerType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeRtRefreshStatisticsPeerAddr"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeRtRefreshStatisticsAfi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeRtRefreshStatisticsSafi"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeRtRefreshStatisticsEntry.setStatus("current")
_Fsbgp4mpeRtRefreshStatisticsPeerType_Type = InetAddressType
_Fsbgp4mpeRtRefreshStatisticsPeerType_Object = MibTableColumn
fsbgp4mpeRtRefreshStatisticsPeerType = _Fsbgp4mpeRtRefreshStatisticsPeerType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32, 2, 1, 1),
    _Fsbgp4mpeRtRefreshStatisticsPeerType_Type()
)
fsbgp4mpeRtRefreshStatisticsPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeRtRefreshStatisticsPeerType.setStatus("current")
_Fsbgp4mpeRtRefreshStatisticsPeerAddr_Type = InetAddress
_Fsbgp4mpeRtRefreshStatisticsPeerAddr_Object = MibTableColumn
fsbgp4mpeRtRefreshStatisticsPeerAddr = _Fsbgp4mpeRtRefreshStatisticsPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32, 2, 1, 2),
    _Fsbgp4mpeRtRefreshStatisticsPeerAddr_Type()
)
fsbgp4mpeRtRefreshStatisticsPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeRtRefreshStatisticsPeerAddr.setStatus("current")
_Fsbgp4mpeRtRefreshStatisticsAfi_Type = InetAddressType
_Fsbgp4mpeRtRefreshStatisticsAfi_Object = MibTableColumn
fsbgp4mpeRtRefreshStatisticsAfi = _Fsbgp4mpeRtRefreshStatisticsAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32, 2, 1, 3),
    _Fsbgp4mpeRtRefreshStatisticsAfi_Type()
)
fsbgp4mpeRtRefreshStatisticsAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeRtRefreshStatisticsAfi.setStatus("current")
_Fsbgp4mpeRtRefreshStatisticsSafi_Type = BgpSafi
_Fsbgp4mpeRtRefreshStatisticsSafi_Object = MibTableColumn
fsbgp4mpeRtRefreshStatisticsSafi = _Fsbgp4mpeRtRefreshStatisticsSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32, 2, 1, 4),
    _Fsbgp4mpeRtRefreshStatisticsSafi_Type()
)
fsbgp4mpeRtRefreshStatisticsSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeRtRefreshStatisticsSafi.setStatus("current")
_Fsbgp4mpeRtRefreshStatisticsRtRefMsgSentCntr_Type = Counter32
_Fsbgp4mpeRtRefreshStatisticsRtRefMsgSentCntr_Object = MibTableColumn
fsbgp4mpeRtRefreshStatisticsRtRefMsgSentCntr = _Fsbgp4mpeRtRefreshStatisticsRtRefMsgSentCntr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32, 2, 1, 5),
    _Fsbgp4mpeRtRefreshStatisticsRtRefMsgSentCntr_Type()
)
fsbgp4mpeRtRefreshStatisticsRtRefMsgSentCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRtRefreshStatisticsRtRefMsgSentCntr.setStatus("current")
_Fsbgp4mpeRtRefreshStatisticsRtRefMsgTxErrCntr_Type = Counter32
_Fsbgp4mpeRtRefreshStatisticsRtRefMsgTxErrCntr_Object = MibTableColumn
fsbgp4mpeRtRefreshStatisticsRtRefMsgTxErrCntr = _Fsbgp4mpeRtRefreshStatisticsRtRefMsgTxErrCntr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32, 2, 1, 6),
    _Fsbgp4mpeRtRefreshStatisticsRtRefMsgTxErrCntr_Type()
)
fsbgp4mpeRtRefreshStatisticsRtRefMsgTxErrCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRtRefreshStatisticsRtRefMsgTxErrCntr.setStatus("current")
_Fsbgp4mpeRtRefreshStatisticsRtRefMsgRcvdCntr_Type = Counter32
_Fsbgp4mpeRtRefreshStatisticsRtRefMsgRcvdCntr_Object = MibTableColumn
fsbgp4mpeRtRefreshStatisticsRtRefMsgRcvdCntr = _Fsbgp4mpeRtRefreshStatisticsRtRefMsgRcvdCntr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32, 2, 1, 7),
    _Fsbgp4mpeRtRefreshStatisticsRtRefMsgRcvdCntr_Type()
)
fsbgp4mpeRtRefreshStatisticsRtRefMsgRcvdCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRtRefreshStatisticsRtRefMsgRcvdCntr.setStatus("current")
_Fsbgp4mpeRtRefreshStatisticsRtRefMsgInvalidCntr_Type = Counter32
_Fsbgp4mpeRtRefreshStatisticsRtRefMsgInvalidCntr_Object = MibTableColumn
fsbgp4mpeRtRefreshStatisticsRtRefMsgInvalidCntr = _Fsbgp4mpeRtRefreshStatisticsRtRefMsgInvalidCntr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 32, 2, 1, 8),
    _Fsbgp4mpeRtRefreshStatisticsRtRefMsgInvalidCntr_Type()
)
fsbgp4mpeRtRefreshStatisticsRtRefMsgInvalidCntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4mpeRtRefreshStatisticsRtRefMsgInvalidCntr.setStatus("current")
_Fsbgp4MpeSoftReconfigOut_ObjectIdentity = ObjectIdentity
fsbgp4MpeSoftReconfigOut = _Fsbgp4MpeSoftReconfigOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 33)
)
_Fsbgp4MpeSoftReconfigOutboundTable_Object = MibTable
fsbgp4MpeSoftReconfigOutboundTable = _Fsbgp4MpeSoftReconfigOutboundTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 33, 1)
)
if mibBuilder.loadTexts:
    fsbgp4MpeSoftReconfigOutboundTable.setStatus("current")
_Fsbgp4MpeSoftReconfigOutboundEntry_Object = MibTableRow
fsbgp4MpeSoftReconfigOutboundEntry = _Fsbgp4MpeSoftReconfigOutboundEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 33, 1, 1)
)
fsbgp4MpeSoftReconfigOutboundEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeSoftReconfigOutboundPeerType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeSoftReconfigOutboundPeerAddr"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeSoftReconfigOutboundAfi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4mpeSoftReconfigOutboundSafi"),
)
if mibBuilder.loadTexts:
    fsbgp4MpeSoftReconfigOutboundEntry.setStatus("current")
_Fsbgp4mpeSoftReconfigOutboundPeerType_Type = InetAddressType
_Fsbgp4mpeSoftReconfigOutboundPeerType_Object = MibTableColumn
fsbgp4mpeSoftReconfigOutboundPeerType = _Fsbgp4mpeSoftReconfigOutboundPeerType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 33, 1, 1, 1),
    _Fsbgp4mpeSoftReconfigOutboundPeerType_Type()
)
fsbgp4mpeSoftReconfigOutboundPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeSoftReconfigOutboundPeerType.setStatus("current")
_Fsbgp4mpeSoftReconfigOutboundPeerAddr_Type = InetAddress
_Fsbgp4mpeSoftReconfigOutboundPeerAddr_Object = MibTableColumn
fsbgp4mpeSoftReconfigOutboundPeerAddr = _Fsbgp4mpeSoftReconfigOutboundPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 33, 1, 1, 2),
    _Fsbgp4mpeSoftReconfigOutboundPeerAddr_Type()
)
fsbgp4mpeSoftReconfigOutboundPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeSoftReconfigOutboundPeerAddr.setStatus("current")
_Fsbgp4mpeSoftReconfigOutboundAfi_Type = InetAddressType
_Fsbgp4mpeSoftReconfigOutboundAfi_Object = MibTableColumn
fsbgp4mpeSoftReconfigOutboundAfi = _Fsbgp4mpeSoftReconfigOutboundAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 33, 1, 1, 3),
    _Fsbgp4mpeSoftReconfigOutboundAfi_Type()
)
fsbgp4mpeSoftReconfigOutboundAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeSoftReconfigOutboundAfi.setStatus("current")
_Fsbgp4mpeSoftReconfigOutboundSafi_Type = BgpSafi
_Fsbgp4mpeSoftReconfigOutboundSafi_Object = MibTableColumn
fsbgp4mpeSoftReconfigOutboundSafi = _Fsbgp4mpeSoftReconfigOutboundSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 33, 1, 1, 4),
    _Fsbgp4mpeSoftReconfigOutboundSafi_Type()
)
fsbgp4mpeSoftReconfigOutboundSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4mpeSoftReconfigOutboundSafi.setStatus("current")


class _Fsbgp4mpeSoftReconfigOutboundRequest_Type(Integer32):
    """Custom type fsbgp4mpeSoftReconfigOutboundRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_Fsbgp4mpeSoftReconfigOutboundRequest_Type.__name__ = "Integer32"
_Fsbgp4mpeSoftReconfigOutboundRequest_Object = MibTableColumn
fsbgp4mpeSoftReconfigOutboundRequest = _Fsbgp4mpeSoftReconfigOutboundRequest_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 33, 1, 1, 5),
    _Fsbgp4mpeSoftReconfigOutboundRequest_Type()
)
fsbgp4mpeSoftReconfigOutboundRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4mpeSoftReconfigOutboundRequest.setStatus("current")
_Fsbgp4MpePrefixCountersTable_Object = MibTable
fsbgp4MpePrefixCountersTable = _Fsbgp4MpePrefixCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 34)
)
if mibBuilder.loadTexts:
    fsbgp4MpePrefixCountersTable.setStatus("current")
_Fsbgp4MpePrefixCountersEntry_Object = MibTableRow
fsbgp4MpePrefixCountersEntry = _Fsbgp4MpePrefixCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 34, 1)
)
fsbgp4MpePrefixCountersEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4MpePeerRemoteAddrType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4MpePeerRemoteAddr"),
    (0, "ARICENT-BGP-MIB", "fsbgp4MpePrefixCountersAfi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4MpePrefixCountersSafi"),
)
if mibBuilder.loadTexts:
    fsbgp4MpePrefixCountersEntry.setStatus("current")
_Fsbgp4MpePeerRemoteAddrType_Type = InetAddressType
_Fsbgp4MpePeerRemoteAddrType_Object = MibTableColumn
fsbgp4MpePeerRemoteAddrType = _Fsbgp4MpePeerRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 34, 1, 1),
    _Fsbgp4MpePeerRemoteAddrType_Type()
)
fsbgp4MpePeerRemoteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4MpePeerRemoteAddrType.setStatus("current")
_Fsbgp4MpePeerRemoteAddr_Type = InetAddress
_Fsbgp4MpePeerRemoteAddr_Object = MibTableColumn
fsbgp4MpePeerRemoteAddr = _Fsbgp4MpePeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 34, 1, 2),
    _Fsbgp4MpePeerRemoteAddr_Type()
)
fsbgp4MpePeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4MpePeerRemoteAddr.setStatus("current")
_Fsbgp4MpePrefixCountersAfi_Type = InetAddressType
_Fsbgp4MpePrefixCountersAfi_Object = MibTableColumn
fsbgp4MpePrefixCountersAfi = _Fsbgp4MpePrefixCountersAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 34, 1, 3),
    _Fsbgp4MpePrefixCountersAfi_Type()
)
fsbgp4MpePrefixCountersAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4MpePrefixCountersAfi.setStatus("current")
_Fsbgp4MpePrefixCountersSafi_Type = BgpSafi
_Fsbgp4MpePrefixCountersSafi_Object = MibTableColumn
fsbgp4MpePrefixCountersSafi = _Fsbgp4MpePrefixCountersSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 34, 1, 4),
    _Fsbgp4MpePrefixCountersSafi_Type()
)
fsbgp4MpePrefixCountersSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4MpePrefixCountersSafi.setStatus("current")
_Fsbgp4MpePrefixCountersPrefixesReceived_Type = Counter32
_Fsbgp4MpePrefixCountersPrefixesReceived_Object = MibTableColumn
fsbgp4MpePrefixCountersPrefixesReceived = _Fsbgp4MpePrefixCountersPrefixesReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 34, 1, 5),
    _Fsbgp4MpePrefixCountersPrefixesReceived_Type()
)
fsbgp4MpePrefixCountersPrefixesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4MpePrefixCountersPrefixesReceived.setStatus("current")
_Fsbgp4MpePrefixCountersPrefixesSent_Type = Counter32
_Fsbgp4MpePrefixCountersPrefixesSent_Object = MibTableColumn
fsbgp4MpePrefixCountersPrefixesSent = _Fsbgp4MpePrefixCountersPrefixesSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 34, 1, 6),
    _Fsbgp4MpePrefixCountersPrefixesSent_Type()
)
fsbgp4MpePrefixCountersPrefixesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4MpePrefixCountersPrefixesSent.setStatus("current")
_Fsbgp4MpePrefixCountersWithdrawsReceived_Type = Counter32
_Fsbgp4MpePrefixCountersWithdrawsReceived_Object = MibTableColumn
fsbgp4MpePrefixCountersWithdrawsReceived = _Fsbgp4MpePrefixCountersWithdrawsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 34, 1, 7),
    _Fsbgp4MpePrefixCountersWithdrawsReceived_Type()
)
fsbgp4MpePrefixCountersWithdrawsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4MpePrefixCountersWithdrawsReceived.setStatus("current")
_Fsbgp4MpePrefixCountersWithdrawsSent_Type = Counter32
_Fsbgp4MpePrefixCountersWithdrawsSent_Object = MibTableColumn
fsbgp4MpePrefixCountersWithdrawsSent = _Fsbgp4MpePrefixCountersWithdrawsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 34, 1, 8),
    _Fsbgp4MpePrefixCountersWithdrawsSent_Type()
)
fsbgp4MpePrefixCountersWithdrawsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4MpePrefixCountersWithdrawsSent.setStatus("current")
_Fsbgp4MpePrefixCountersInPrefixes_Type = Gauge32
_Fsbgp4MpePrefixCountersInPrefixes_Object = MibTableColumn
fsbgp4MpePrefixCountersInPrefixes = _Fsbgp4MpePrefixCountersInPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 34, 1, 9),
    _Fsbgp4MpePrefixCountersInPrefixes_Type()
)
fsbgp4MpePrefixCountersInPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4MpePrefixCountersInPrefixes.setStatus("current")
_Fsbgp4MpePrefixCountersInPrefixesAccepted_Type = Gauge32
_Fsbgp4MpePrefixCountersInPrefixesAccepted_Object = MibTableColumn
fsbgp4MpePrefixCountersInPrefixesAccepted = _Fsbgp4MpePrefixCountersInPrefixesAccepted_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 34, 1, 10),
    _Fsbgp4MpePrefixCountersInPrefixesAccepted_Type()
)
fsbgp4MpePrefixCountersInPrefixesAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4MpePrefixCountersInPrefixesAccepted.setStatus("current")
_Fsbgp4MpePrefixCountersInPrefixesRejected_Type = Gauge32
_Fsbgp4MpePrefixCountersInPrefixesRejected_Object = MibTableColumn
fsbgp4MpePrefixCountersInPrefixesRejected = _Fsbgp4MpePrefixCountersInPrefixesRejected_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 34, 1, 11),
    _Fsbgp4MpePrefixCountersInPrefixesRejected_Type()
)
fsbgp4MpePrefixCountersInPrefixesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4MpePrefixCountersInPrefixesRejected.setStatus("current")
_Fsbgp4MpePrefixCountersOutPrefixes_Type = Gauge32
_Fsbgp4MpePrefixCountersOutPrefixes_Object = MibTableColumn
fsbgp4MpePrefixCountersOutPrefixes = _Fsbgp4MpePrefixCountersOutPrefixes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 34, 1, 12),
    _Fsbgp4MpePrefixCountersOutPrefixes_Type()
)
fsbgp4MpePrefixCountersOutPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4MpePrefixCountersOutPrefixes.setStatus("current")
_Fsbgp4MplsVpn_ObjectIdentity = ObjectIdentity
fsbgp4MplsVpn = _Fsbgp4MplsVpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 35)
)
_Fsbgp4MplsVpnVrfRouteTargetTable_Object = MibTable
fsbgp4MplsVpnVrfRouteTargetTable = _Fsbgp4MplsVpnVrfRouteTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 35, 1)
)
if mibBuilder.loadTexts:
    fsbgp4MplsVpnVrfRouteTargetTable.setStatus("current")
_Fsbgp4MplsVpnVrfRouteTargetEntry_Object = MibTableRow
fsbgp4MplsVpnVrfRouteTargetEntry = _Fsbgp4MplsVpnVrfRouteTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 35, 1, 1)
)
fsbgp4MplsVpnVrfRouteTargetEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4MplsVpnVrfName"),
    (0, "ARICENT-BGP-MIB", "fsbgp4MplsVpnVrfRouteTargetType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4MplsVpnVrfRouteTarget"),
)
if mibBuilder.loadTexts:
    fsbgp4MplsVpnVrfRouteTargetEntry.setStatus("current")


class _Fsbgp4MplsVpnVrfName_Type(DisplayString):
    """Custom type fsbgp4MplsVpnVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Fsbgp4MplsVpnVrfName_Type.__name__ = "DisplayString"
_Fsbgp4MplsVpnVrfName_Object = MibTableColumn
fsbgp4MplsVpnVrfName = _Fsbgp4MplsVpnVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 35, 1, 1, 1),
    _Fsbgp4MplsVpnVrfName_Type()
)
fsbgp4MplsVpnVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4MplsVpnVrfName.setStatus("current")


class _Fsbgp4MplsVpnVrfRouteTargetType_Type(Integer32):
    """Custom type fsbgp4MplsVpnVrfRouteTargetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("import", 1),
          ("export", 2),
          ("both", 3))
    )


_Fsbgp4MplsVpnVrfRouteTargetType_Type.__name__ = "Integer32"
_Fsbgp4MplsVpnVrfRouteTargetType_Object = MibTableColumn
fsbgp4MplsVpnVrfRouteTargetType = _Fsbgp4MplsVpnVrfRouteTargetType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 35, 1, 1, 2),
    _Fsbgp4MplsVpnVrfRouteTargetType_Type()
)
fsbgp4MplsVpnVrfRouteTargetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4MplsVpnVrfRouteTargetType.setStatus("current")


class _Fsbgp4MplsVpnVrfRouteTarget_Type(DisplayString):
    """Custom type fsbgp4MplsVpnVrfRouteTarget based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Fsbgp4MplsVpnVrfRouteTarget_Type.__name__ = "DisplayString"
_Fsbgp4MplsVpnVrfRouteTarget_Object = MibTableColumn
fsbgp4MplsVpnVrfRouteTarget = _Fsbgp4MplsVpnVrfRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 35, 1, 1, 3),
    _Fsbgp4MplsVpnVrfRouteTarget_Type()
)
fsbgp4MplsVpnVrfRouteTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4MplsVpnVrfRouteTarget.setStatus("current")
_Fsbgp4MplsVpnVrfRouteTargetRowStatus_Type = RowStatus
_Fsbgp4MplsVpnVrfRouteTargetRowStatus_Object = MibTableColumn
fsbgp4MplsVpnVrfRouteTargetRowStatus = _Fsbgp4MplsVpnVrfRouteTargetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 35, 1, 1, 4),
    _Fsbgp4MplsVpnVrfRouteTargetRowStatus_Type()
)
fsbgp4MplsVpnVrfRouteTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsbgp4MplsVpnVrfRouteTargetRowStatus.setStatus("current")
_Fsbgp4MplsVpnVrfRedistributeTable_Object = MibTable
fsbgp4MplsVpnVrfRedistributeTable = _Fsbgp4MplsVpnVrfRedistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 35, 2)
)
if mibBuilder.loadTexts:
    fsbgp4MplsVpnVrfRedistributeTable.setStatus("current")
_Fsbgp4MplsVpnVrfRedistributeEntry_Object = MibTableRow
fsbgp4MplsVpnVrfRedistributeEntry = _Fsbgp4MplsVpnVrfRedistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 35, 2, 1)
)
fsbgp4MplsVpnVrfRedistributeEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4MplsVpnVrfRedisAfi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4MplsVpnVrfRedisSafi"),
    (0, "ARICENT-BGP-MIB", "fsbgp4MplsVpnVrfName"),
)
if mibBuilder.loadTexts:
    fsbgp4MplsVpnVrfRedistributeEntry.setStatus("current")
_Fsbgp4MplsVpnVrfRedisAfi_Type = InetAddressType
_Fsbgp4MplsVpnVrfRedisAfi_Object = MibTableColumn
fsbgp4MplsVpnVrfRedisAfi = _Fsbgp4MplsVpnVrfRedisAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 35, 2, 1, 1),
    _Fsbgp4MplsVpnVrfRedisAfi_Type()
)
fsbgp4MplsVpnVrfRedisAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4MplsVpnVrfRedisAfi.setStatus("current")
_Fsbgp4MplsVpnVrfRedisSafi_Type = BgpSafi
_Fsbgp4MplsVpnVrfRedisSafi_Object = MibTableColumn
fsbgp4MplsVpnVrfRedisSafi = _Fsbgp4MplsVpnVrfRedisSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 35, 2, 1, 2),
    _Fsbgp4MplsVpnVrfRedisSafi_Type()
)
fsbgp4MplsVpnVrfRedisSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4MplsVpnVrfRedisSafi.setStatus("current")
_Fsbgp4MplsVpnVrfRedisProtoMask_Type = Integer32
_Fsbgp4MplsVpnVrfRedisProtoMask_Object = MibTableColumn
fsbgp4MplsVpnVrfRedisProtoMask = _Fsbgp4MplsVpnVrfRedisProtoMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 35, 2, 1, 3),
    _Fsbgp4MplsVpnVrfRedisProtoMask_Type()
)
fsbgp4MplsVpnVrfRedisProtoMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4MplsVpnVrfRedisProtoMask.setStatus("current")
_Fsbgp4MplsVpnRRRouteTargetTable_Object = MibTable
fsbgp4MplsVpnRRRouteTargetTable = _Fsbgp4MplsVpnRRRouteTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 35, 3)
)
if mibBuilder.loadTexts:
    fsbgp4MplsVpnRRRouteTargetTable.setStatus("current")
_Fsbgp4MplsVpnRRRouteTargetEntry_Object = MibTableRow
fsbgp4MplsVpnRRRouteTargetEntry = _Fsbgp4MplsVpnRRRouteTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 35, 3, 1)
)
fsbgp4MplsVpnRRRouteTargetEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4MplsVpnRRRouteTarget"),
)
if mibBuilder.loadTexts:
    fsbgp4MplsVpnRRRouteTargetEntry.setStatus("current")


class _Fsbgp4MplsVpnRRRouteTarget_Type(DisplayString):
    """Custom type fsbgp4MplsVpnRRRouteTarget based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Fsbgp4MplsVpnRRRouteTarget_Type.__name__ = "DisplayString"
_Fsbgp4MplsVpnRRRouteTarget_Object = MibTableColumn
fsbgp4MplsVpnRRRouteTarget = _Fsbgp4MplsVpnRRRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 35, 3, 1, 1),
    _Fsbgp4MplsVpnRRRouteTarget_Type()
)
fsbgp4MplsVpnRRRouteTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4MplsVpnRRRouteTarget.setStatus("current")
_Fsbgp4MplsVpnRRRouteTargetRtCnt_Type = Integer32
_Fsbgp4MplsVpnRRRouteTargetRtCnt_Object = MibTableColumn
fsbgp4MplsVpnRRRouteTargetRtCnt = _Fsbgp4MplsVpnRRRouteTargetRtCnt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 35, 3, 1, 2),
    _Fsbgp4MplsVpnRRRouteTargetRtCnt_Type()
)
fsbgp4MplsVpnRRRouteTargetRtCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4MplsVpnRRRouteTargetRtCnt.setStatus("current")
_Fsbgp4MplsVpnRRRouteTargetTimeStamp_Type = Integer32
_Fsbgp4MplsVpnRRRouteTargetTimeStamp_Object = MibTableColumn
fsbgp4MplsVpnRRRouteTargetTimeStamp = _Fsbgp4MplsVpnRRRouteTargetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 35, 3, 1, 3),
    _Fsbgp4MplsVpnRRRouteTargetTimeStamp_Type()
)
fsbgp4MplsVpnRRRouteTargetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsbgp4MplsVpnRRRouteTargetTimeStamp.setStatus("current")
_Fsbgp4DistInOutRouteMap_ObjectIdentity = ObjectIdentity
fsbgp4DistInOutRouteMap = _Fsbgp4DistInOutRouteMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 36)
)
_FsBgp4DistInOutRouteMapTable_Object = MibTable
fsBgp4DistInOutRouteMapTable = _FsBgp4DistInOutRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 36, 1)
)
if mibBuilder.loadTexts:
    fsBgp4DistInOutRouteMapTable.setStatus("current")
_FsBgp4DistInOutRouteMapEntry_Object = MibTableRow
fsBgp4DistInOutRouteMapEntry = _FsBgp4DistInOutRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 36, 1, 1)
)
fsBgp4DistInOutRouteMapEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsBgp4DistInOutRouteMapName"),
    (0, "ARICENT-BGP-MIB", "fsBgp4DistInOutRouteMapType"),
)
if mibBuilder.loadTexts:
    fsBgp4DistInOutRouteMapEntry.setStatus("current")


class _FsBgp4DistInOutRouteMapName_Type(DisplayString):
    """Custom type fsBgp4DistInOutRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsBgp4DistInOutRouteMapName_Type.__name__ = "DisplayString"
_FsBgp4DistInOutRouteMapName_Object = MibTableColumn
fsBgp4DistInOutRouteMapName = _FsBgp4DistInOutRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 36, 1, 1, 1),
    _FsBgp4DistInOutRouteMapName_Type()
)
fsBgp4DistInOutRouteMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4DistInOutRouteMapName.setStatus("current")


class _FsBgp4DistInOutRouteMapType_Type(Integer32):
    """Custom type fsBgp4DistInOutRouteMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsBgp4DistInOutRouteMapType_Type.__name__ = "Integer32"
_FsBgp4DistInOutRouteMapType_Object = MibTableColumn
fsBgp4DistInOutRouteMapType = _FsBgp4DistInOutRouteMapType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 36, 1, 1, 2),
    _FsBgp4DistInOutRouteMapType_Type()
)
fsBgp4DistInOutRouteMapType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4DistInOutRouteMapType.setStatus("current")


class _FsBgp4DistInOutRouteMapValue_Type(Integer32):
    """Custom type fsBgp4DistInOutRouteMapValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsBgp4DistInOutRouteMapValue_Type.__name__ = "Integer32"
_FsBgp4DistInOutRouteMapValue_Object = MibTableColumn
fsBgp4DistInOutRouteMapValue = _FsBgp4DistInOutRouteMapValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 36, 1, 1, 3),
    _FsBgp4DistInOutRouteMapValue_Type()
)
fsBgp4DistInOutRouteMapValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4DistInOutRouteMapValue.setStatus("current")
_FsBgp4DistInOutRouteMapRowStatus_Type = RowStatus
_FsBgp4DistInOutRouteMapRowStatus_Object = MibTableColumn
fsBgp4DistInOutRouteMapRowStatus = _FsBgp4DistInOutRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 36, 1, 1, 4),
    _FsBgp4DistInOutRouteMapRowStatus_Type()
)
fsBgp4DistInOutRouteMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4DistInOutRouteMapRowStatus.setStatus("current")
_Fsbgp4PreferenceGroup_ObjectIdentity = ObjectIdentity
fsbgp4PreferenceGroup = _Fsbgp4PreferenceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 37)
)


class _FsBgp4PreferenceValue_Type(Integer32):
    """Custom type fsBgp4PreferenceValue based on Integer32"""
    defaultValue = 122

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsBgp4PreferenceValue_Type.__name__ = "Integer32"
_FsBgp4PreferenceValue_Object = MibScalar
fsBgp4PreferenceValue = _FsBgp4PreferenceValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 37, 1),
    _FsBgp4PreferenceValue_Type()
)
fsBgp4PreferenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PreferenceValue.setStatus("current")
_Fsbgp4Notification_ObjectIdentity = ObjectIdentity
fsbgp4Notification = _Fsbgp4Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 38)
)
_Fsbgp4Trap_ObjectIdentity = ObjectIdentity
fsbgp4Trap = _Fsbgp4Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 38, 0)
)
_Fsbgp4NeighborRouteMap_ObjectIdentity = ObjectIdentity
fsbgp4NeighborRouteMap = _Fsbgp4NeighborRouteMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 39)
)
_FsBgp4NeighborRouteMapTable_Object = MibTable
fsBgp4NeighborRouteMapTable = _FsBgp4NeighborRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 39, 1)
)
if mibBuilder.loadTexts:
    fsBgp4NeighborRouteMapTable.setStatus("current")
_FsBgp4NeighborRouteMapEntry_Object = MibTableRow
fsBgp4NeighborRouteMapEntry = _FsBgp4NeighborRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 39, 1, 1)
)
fsBgp4NeighborRouteMapEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsBgp4NeighborRouteMapPeerAddrType"),
    (0, "ARICENT-BGP-MIB", "fsBgp4NeighborRouteMapPeer"),
    (0, "ARICENT-BGP-MIB", "fsBgp4NeighborRouteMapDirection"),
)
if mibBuilder.loadTexts:
    fsBgp4NeighborRouteMapEntry.setStatus("current")
_FsBgp4NeighborRouteMapPeerAddrType_Type = InetAddressType
_FsBgp4NeighborRouteMapPeerAddrType_Object = MibTableColumn
fsBgp4NeighborRouteMapPeerAddrType = _FsBgp4NeighborRouteMapPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 39, 1, 1, 1),
    _FsBgp4NeighborRouteMapPeerAddrType_Type()
)
fsBgp4NeighborRouteMapPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4NeighborRouteMapPeerAddrType.setStatus("current")
_FsBgp4NeighborRouteMapPeer_Type = InetAddress
_FsBgp4NeighborRouteMapPeer_Object = MibTableColumn
fsBgp4NeighborRouteMapPeer = _FsBgp4NeighborRouteMapPeer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 39, 1, 1, 2),
    _FsBgp4NeighborRouteMapPeer_Type()
)
fsBgp4NeighborRouteMapPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4NeighborRouteMapPeer.setStatus("current")


class _FsBgp4NeighborRouteMapDirection_Type(Integer32):
    """Custom type fsBgp4NeighborRouteMapDirection based on Integer32"""
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


_FsBgp4NeighborRouteMapDirection_Type.__name__ = "Integer32"
_FsBgp4NeighborRouteMapDirection_Object = MibTableColumn
fsBgp4NeighborRouteMapDirection = _FsBgp4NeighborRouteMapDirection_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 39, 1, 1, 3),
    _FsBgp4NeighborRouteMapDirection_Type()
)
fsBgp4NeighborRouteMapDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4NeighborRouteMapDirection.setStatus("current")


class _FsBgp4NeighborRouteMapName_Type(DisplayString):
    """Custom type fsBgp4NeighborRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsBgp4NeighborRouteMapName_Type.__name__ = "DisplayString"
_FsBgp4NeighborRouteMapName_Object = MibTableColumn
fsBgp4NeighborRouteMapName = _FsBgp4NeighborRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 39, 1, 1, 4),
    _FsBgp4NeighborRouteMapName_Type()
)
fsBgp4NeighborRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4NeighborRouteMapName.setStatus("current")
_FsBgp4NeighborRouteMapRowStatus_Type = RowStatus
_FsBgp4NeighborRouteMapRowStatus_Object = MibTableColumn
fsBgp4NeighborRouteMapRowStatus = _FsBgp4NeighborRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 39, 1, 1, 5),
    _FsBgp4NeighborRouteMapRowStatus_Type()
)
fsBgp4NeighborRouteMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4NeighborRouteMapRowStatus.setStatus("current")
_FsBgp4PeerGroupTable_Object = MibTable
fsBgp4PeerGroupTable = _FsBgp4PeerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40)
)
if mibBuilder.loadTexts:
    fsBgp4PeerGroupTable.setStatus("current")
_FsBgp4PeerGroupEntry_Object = MibTableRow
fsBgp4PeerGroupEntry = _FsBgp4PeerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1)
)
fsBgp4PeerGroupEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsBgp4PeerGroupName"),
)
if mibBuilder.loadTexts:
    fsBgp4PeerGroupEntry.setStatus("current")


class _FsBgp4PeerGroupName_Type(DisplayString):
    """Custom type fsBgp4PeerGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsBgp4PeerGroupName_Type.__name__ = "DisplayString"
_FsBgp4PeerGroupName_Object = MibTableColumn
fsBgp4PeerGroupName = _FsBgp4PeerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 1),
    _FsBgp4PeerGroupName_Type()
)
fsBgp4PeerGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupName.setStatus("current")
_FsBgp4PeerGroupAddrType_Type = InetAddressType
_FsBgp4PeerGroupAddrType_Object = MibTableColumn
fsBgp4PeerGroupAddrType = _FsBgp4PeerGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 2),
    _FsBgp4PeerGroupAddrType_Type()
)
fsBgp4PeerGroupAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupAddrType.setStatus("current")


class _FsBgp4PeerGroupRemoteAs_Type(Unsigned32):
    """Custom type fsBgp4PeerGroupRemoteAs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsBgp4PeerGroupRemoteAs_Type.__name__ = "Unsigned32"
_FsBgp4PeerGroupRemoteAs_Object = MibTableColumn
fsBgp4PeerGroupRemoteAs = _FsBgp4PeerGroupRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 3),
    _FsBgp4PeerGroupRemoteAs_Type()
)
fsBgp4PeerGroupRemoteAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupRemoteAs.setStatus("current")


class _FsBgp4PeerGroupHoldTimeConfigured_Type(Integer32):
    """Custom type fsBgp4PeerGroupHoldTimeConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_FsBgp4PeerGroupHoldTimeConfigured_Type.__name__ = "Integer32"
_FsBgp4PeerGroupHoldTimeConfigured_Object = MibTableColumn
fsBgp4PeerGroupHoldTimeConfigured = _FsBgp4PeerGroupHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 4),
    _FsBgp4PeerGroupHoldTimeConfigured_Type()
)
fsBgp4PeerGroupHoldTimeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupHoldTimeConfigured.setStatus("current")


class _FsBgp4PeerGroupKeepAliveConfigured_Type(Integer32):
    """Custom type fsBgp4PeerGroupKeepAliveConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_FsBgp4PeerGroupKeepAliveConfigured_Type.__name__ = "Integer32"
_FsBgp4PeerGroupKeepAliveConfigured_Object = MibTableColumn
fsBgp4PeerGroupKeepAliveConfigured = _FsBgp4PeerGroupKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 5),
    _FsBgp4PeerGroupKeepAliveConfigured_Type()
)
fsBgp4PeerGroupKeepAliveConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupKeepAliveConfigured.setStatus("current")


class _FsBgp4PeerGroupConnectRetryInterval_Type(Integer32):
    """Custom type fsBgp4PeerGroupConnectRetryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsBgp4PeerGroupConnectRetryInterval_Type.__name__ = "Integer32"
_FsBgp4PeerGroupConnectRetryInterval_Object = MibTableColumn
fsBgp4PeerGroupConnectRetryInterval = _FsBgp4PeerGroupConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 6),
    _FsBgp4PeerGroupConnectRetryInterval_Type()
)
fsBgp4PeerGroupConnectRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupConnectRetryInterval.setStatus("current")


class _FsBgp4PeerGroupMinASOriginInterval_Type(Integer32):
    """Custom type fsBgp4PeerGroupMinASOriginInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsBgp4PeerGroupMinASOriginInterval_Type.__name__ = "Integer32"
_FsBgp4PeerGroupMinASOriginInterval_Object = MibTableColumn
fsBgp4PeerGroupMinASOriginInterval = _FsBgp4PeerGroupMinASOriginInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 7),
    _FsBgp4PeerGroupMinASOriginInterval_Type()
)
fsBgp4PeerGroupMinASOriginInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupMinASOriginInterval.setStatus("current")


class _FsBgp4PeerGroupMinRouteAdvInterval_Type(Integer32):
    """Custom type fsBgp4PeerGroupMinRouteAdvInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsBgp4PeerGroupMinRouteAdvInterval_Type.__name__ = "Integer32"
_FsBgp4PeerGroupMinRouteAdvInterval_Object = MibTableColumn
fsBgp4PeerGroupMinRouteAdvInterval = _FsBgp4PeerGroupMinRouteAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 8),
    _FsBgp4PeerGroupMinRouteAdvInterval_Type()
)
fsBgp4PeerGroupMinRouteAdvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupMinRouteAdvInterval.setStatus("current")


class _FsBgp4PeerGroupAllowAutomaticStart_Type(Integer32):
    """Custom type fsBgp4PeerGroupAllowAutomaticStart based on Integer32"""
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


_FsBgp4PeerGroupAllowAutomaticStart_Type.__name__ = "Integer32"
_FsBgp4PeerGroupAllowAutomaticStart_Object = MibTableColumn
fsBgp4PeerGroupAllowAutomaticStart = _FsBgp4PeerGroupAllowAutomaticStart_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 9),
    _FsBgp4PeerGroupAllowAutomaticStart_Type()
)
fsBgp4PeerGroupAllowAutomaticStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupAllowAutomaticStart.setStatus("current")


class _FsBgp4PeerGroupAllowAutomaticStop_Type(Integer32):
    """Custom type fsBgp4PeerGroupAllowAutomaticStop based on Integer32"""
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


_FsBgp4PeerGroupAllowAutomaticStop_Type.__name__ = "Integer32"
_FsBgp4PeerGroupAllowAutomaticStop_Object = MibTableColumn
fsBgp4PeerGroupAllowAutomaticStop = _FsBgp4PeerGroupAllowAutomaticStop_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 10),
    _FsBgp4PeerGroupAllowAutomaticStop_Type()
)
fsBgp4PeerGroupAllowAutomaticStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupAllowAutomaticStop.setStatus("current")


class _FsBgp4PeerGroupIdleHoldTimeConfigured_Type(Integer32):
    """Custom type fsBgp4PeerGroupIdleHoldTimeConfigured based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsBgp4PeerGroupIdleHoldTimeConfigured_Type.__name__ = "Integer32"
_FsBgp4PeerGroupIdleHoldTimeConfigured_Object = MibTableColumn
fsBgp4PeerGroupIdleHoldTimeConfigured = _FsBgp4PeerGroupIdleHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 11),
    _FsBgp4PeerGroupIdleHoldTimeConfigured_Type()
)
fsBgp4PeerGroupIdleHoldTimeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupIdleHoldTimeConfigured.setStatus("current")


class _FsBgp4PeerGroupDampPeerOscillations_Type(Integer32):
    """Custom type fsBgp4PeerGroupDampPeerOscillations based on Integer32"""
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


_FsBgp4PeerGroupDampPeerOscillations_Type.__name__ = "Integer32"
_FsBgp4PeerGroupDampPeerOscillations_Object = MibTableColumn
fsBgp4PeerGroupDampPeerOscillations = _FsBgp4PeerGroupDampPeerOscillations_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 12),
    _FsBgp4PeerGroupDampPeerOscillations_Type()
)
fsBgp4PeerGroupDampPeerOscillations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupDampPeerOscillations.setStatus("current")


class _FsBgp4PeerGroupDelayOpen_Type(Integer32):
    """Custom type fsBgp4PeerGroupDelayOpen based on Integer32"""
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


_FsBgp4PeerGroupDelayOpen_Type.__name__ = "Integer32"
_FsBgp4PeerGroupDelayOpen_Object = MibTableColumn
fsBgp4PeerGroupDelayOpen = _FsBgp4PeerGroupDelayOpen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 13),
    _FsBgp4PeerGroupDelayOpen_Type()
)
fsBgp4PeerGroupDelayOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupDelayOpen.setStatus("current")


class _FsBgp4PeerGroupDelayOpenTimeConfigured_Type(Integer32):
    """Custom type fsBgp4PeerGroupDelayOpenTimeConfigured based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsBgp4PeerGroupDelayOpenTimeConfigured_Type.__name__ = "Integer32"
_FsBgp4PeerGroupDelayOpenTimeConfigured_Object = MibTableColumn
fsBgp4PeerGroupDelayOpenTimeConfigured = _FsBgp4PeerGroupDelayOpenTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 14),
    _FsBgp4PeerGroupDelayOpenTimeConfigured_Type()
)
fsBgp4PeerGroupDelayOpenTimeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupDelayOpenTimeConfigured.setStatus("current")


class _FsBgp4PeerGroupPrefixUpperLimit_Type(Integer32):
    """Custom type fsBgp4PeerGroupPrefixUpperLimit based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsBgp4PeerGroupPrefixUpperLimit_Type.__name__ = "Integer32"
_FsBgp4PeerGroupPrefixUpperLimit_Object = MibTableColumn
fsBgp4PeerGroupPrefixUpperLimit = _FsBgp4PeerGroupPrefixUpperLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 15),
    _FsBgp4PeerGroupPrefixUpperLimit_Type()
)
fsBgp4PeerGroupPrefixUpperLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupPrefixUpperLimit.setStatus("current")


class _FsBgp4PeerGroupTcpConnectRetryCnt_Type(Integer32):
    """Custom type fsBgp4PeerGroupTcpConnectRetryCnt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_FsBgp4PeerGroupTcpConnectRetryCnt_Type.__name__ = "Integer32"
_FsBgp4PeerGroupTcpConnectRetryCnt_Object = MibTableColumn
fsBgp4PeerGroupTcpConnectRetryCnt = _FsBgp4PeerGroupTcpConnectRetryCnt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 16),
    _FsBgp4PeerGroupTcpConnectRetryCnt_Type()
)
fsBgp4PeerGroupTcpConnectRetryCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupTcpConnectRetryCnt.setStatus("current")


class _FsBgp4PeerGroupEBGPMultiHop_Type(Integer32):
    """Custom type fsBgp4PeerGroupEBGPMultiHop based on Integer32"""
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


_FsBgp4PeerGroupEBGPMultiHop_Type.__name__ = "Integer32"
_FsBgp4PeerGroupEBGPMultiHop_Object = MibTableColumn
fsBgp4PeerGroupEBGPMultiHop = _FsBgp4PeerGroupEBGPMultiHop_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 17),
    _FsBgp4PeerGroupEBGPMultiHop_Type()
)
fsBgp4PeerGroupEBGPMultiHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupEBGPMultiHop.setStatus("current")


class _FsBgp4PeerGroupEBGPHopLimit_Type(Integer32):
    """Custom type fsBgp4PeerGroupEBGPHopLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsBgp4PeerGroupEBGPHopLimit_Type.__name__ = "Integer32"
_FsBgp4PeerGroupEBGPHopLimit_Object = MibTableColumn
fsBgp4PeerGroupEBGPHopLimit = _FsBgp4PeerGroupEBGPHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 18),
    _FsBgp4PeerGroupEBGPHopLimit_Type()
)
fsBgp4PeerGroupEBGPHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupEBGPHopLimit.setStatus("current")


class _FsBgp4PeerGroupNextHopSelf_Type(Integer32):
    """Custom type fsBgp4PeerGroupNextHopSelf based on Integer32"""
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


_FsBgp4PeerGroupNextHopSelf_Type.__name__ = "Integer32"
_FsBgp4PeerGroupNextHopSelf_Object = MibTableColumn
fsBgp4PeerGroupNextHopSelf = _FsBgp4PeerGroupNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 19),
    _FsBgp4PeerGroupNextHopSelf_Type()
)
fsBgp4PeerGroupNextHopSelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupNextHopSelf.setStatus("current")


class _FsBgp4PeerGroupRflClient_Type(Integer32):
    """Custom type fsBgp4PeerGroupRflClient based on Integer32"""
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


_FsBgp4PeerGroupRflClient_Type.__name__ = "Integer32"
_FsBgp4PeerGroupRflClient_Object = MibTableColumn
fsBgp4PeerGroupRflClient = _FsBgp4PeerGroupRflClient_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 20),
    _FsBgp4PeerGroupRflClient_Type()
)
fsBgp4PeerGroupRflClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupRflClient.setStatus("current")


class _FsBgp4PeerGroupTcpSendBufSize_Type(Integer32):
    """Custom type fsBgp4PeerGroupTcpSendBufSize based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 65536),
    )


_FsBgp4PeerGroupTcpSendBufSize_Type.__name__ = "Integer32"
_FsBgp4PeerGroupTcpSendBufSize_Object = MibTableColumn
fsBgp4PeerGroupTcpSendBufSize = _FsBgp4PeerGroupTcpSendBufSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 21),
    _FsBgp4PeerGroupTcpSendBufSize_Type()
)
fsBgp4PeerGroupTcpSendBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupTcpSendBufSize.setStatus("current")


class _FsBgp4PeerGroupTcpRcvBufSize_Type(Integer32):
    """Custom type fsBgp4PeerGroupTcpRcvBufSize based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 65536),
    )


_FsBgp4PeerGroupTcpRcvBufSize_Type.__name__ = "Integer32"
_FsBgp4PeerGroupTcpRcvBufSize_Object = MibTableColumn
fsBgp4PeerGroupTcpRcvBufSize = _FsBgp4PeerGroupTcpRcvBufSize_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 22),
    _FsBgp4PeerGroupTcpRcvBufSize_Type()
)
fsBgp4PeerGroupTcpRcvBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupTcpRcvBufSize.setStatus("current")


class _FsBgp4PeerGroupCommSendStatus_Type(Integer32):
    """Custom type fsBgp4PeerGroupCommSendStatus based on Integer32"""
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


_FsBgp4PeerGroupCommSendStatus_Type.__name__ = "Integer32"
_FsBgp4PeerGroupCommSendStatus_Object = MibTableColumn
fsBgp4PeerGroupCommSendStatus = _FsBgp4PeerGroupCommSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 23),
    _FsBgp4PeerGroupCommSendStatus_Type()
)
fsBgp4PeerGroupCommSendStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupCommSendStatus.setStatus("current")


class _FsBgp4PeerGroupECommSendStatus_Type(Integer32):
    """Custom type fsBgp4PeerGroupECommSendStatus based on Integer32"""
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


_FsBgp4PeerGroupECommSendStatus_Type.__name__ = "Integer32"
_FsBgp4PeerGroupECommSendStatus_Object = MibTableColumn
fsBgp4PeerGroupECommSendStatus = _FsBgp4PeerGroupECommSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 24),
    _FsBgp4PeerGroupECommSendStatus_Type()
)
fsBgp4PeerGroupECommSendStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupECommSendStatus.setStatus("current")


class _FsBgp4PeerGroupPassive_Type(Integer32):
    """Custom type fsBgp4PeerGroupPassive based on Integer32"""
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


_FsBgp4PeerGroupPassive_Type.__name__ = "Integer32"
_FsBgp4PeerGroupPassive_Object = MibTableColumn
fsBgp4PeerGroupPassive = _FsBgp4PeerGroupPassive_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 25),
    _FsBgp4PeerGroupPassive_Type()
)
fsBgp4PeerGroupPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupPassive.setStatus("current")


class _FsBgp4PeerGroupDefaultOriginate_Type(Integer32):
    """Custom type fsBgp4PeerGroupDefaultOriginate based on Integer32"""
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


_FsBgp4PeerGroupDefaultOriginate_Type.__name__ = "Integer32"
_FsBgp4PeerGroupDefaultOriginate_Object = MibTableColumn
fsBgp4PeerGroupDefaultOriginate = _FsBgp4PeerGroupDefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 26),
    _FsBgp4PeerGroupDefaultOriginate_Type()
)
fsBgp4PeerGroupDefaultOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupDefaultOriginate.setStatus("current")


class _FsBgp4PeerGroupActivateMPCapability_Type(Integer32):
    """Custom type fsBgp4PeerGroupActivateMPCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ipv4unicast", 1),
          ("ipv6unicast", 2),
          ("l2vpnvpls", 16))
    )


_FsBgp4PeerGroupActivateMPCapability_Type.__name__ = "Integer32"
_FsBgp4PeerGroupActivateMPCapability_Object = MibTableColumn
fsBgp4PeerGroupActivateMPCapability = _FsBgp4PeerGroupActivateMPCapability_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 27),
    _FsBgp4PeerGroupActivateMPCapability_Type()
)
fsBgp4PeerGroupActivateMPCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupActivateMPCapability.setStatus("current")


class _FsBgp4PeerGroupDeactivateMPCapability_Type(Integer32):
    """Custom type fsBgp4PeerGroupDeactivateMPCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ipv4unicast", 1),
          ("ipv6unicast", 2),
          ("l2vpnvpls", 16))
    )


_FsBgp4PeerGroupDeactivateMPCapability_Type.__name__ = "Integer32"
_FsBgp4PeerGroupDeactivateMPCapability_Object = MibTableColumn
fsBgp4PeerGroupDeactivateMPCapability = _FsBgp4PeerGroupDeactivateMPCapability_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 28),
    _FsBgp4PeerGroupDeactivateMPCapability_Type()
)
fsBgp4PeerGroupDeactivateMPCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupDeactivateMPCapability.setStatus("current")
_FsBgp4PeerGroupRouteMapNameIn_Type = DisplayString
_FsBgp4PeerGroupRouteMapNameIn_Object = MibTableColumn
fsBgp4PeerGroupRouteMapNameIn = _FsBgp4PeerGroupRouteMapNameIn_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 29),
    _FsBgp4PeerGroupRouteMapNameIn_Type()
)
fsBgp4PeerGroupRouteMapNameIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupRouteMapNameIn.setStatus("current")
_FsBgp4PeerGroupRouteMapNameOut_Type = DisplayString
_FsBgp4PeerGroupRouteMapNameOut_Object = MibTableColumn
fsBgp4PeerGroupRouteMapNameOut = _FsBgp4PeerGroupRouteMapNameOut_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 30),
    _FsBgp4PeerGroupRouteMapNameOut_Type()
)
fsBgp4PeerGroupRouteMapNameOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupRouteMapNameOut.setStatus("current")
_FsBgp4PeerGroupStatus_Type = RowStatus
_FsBgp4PeerGroupStatus_Object = MibTableColumn
fsBgp4PeerGroupStatus = _FsBgp4PeerGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 31),
    _FsBgp4PeerGroupStatus_Type()
)
fsBgp4PeerGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupStatus.setStatus("current")
_FsBgp4PeerGroupIpPrefixNameIn_Type = DisplayString
_FsBgp4PeerGroupIpPrefixNameIn_Object = MibTableColumn
fsBgp4PeerGroupIpPrefixNameIn = _FsBgp4PeerGroupIpPrefixNameIn_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 32),
    _FsBgp4PeerGroupIpPrefixNameIn_Type()
)
fsBgp4PeerGroupIpPrefixNameIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupIpPrefixNameIn.setStatus("current")
_FsBgp4PeerGroupIpPrefixNameOut_Type = DisplayString
_FsBgp4PeerGroupIpPrefixNameOut_Object = MibTableColumn
fsBgp4PeerGroupIpPrefixNameOut = _FsBgp4PeerGroupIpPrefixNameOut_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 33),
    _FsBgp4PeerGroupIpPrefixNameOut_Type()
)
fsBgp4PeerGroupIpPrefixNameOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupIpPrefixNameOut.setStatus("current")
_FsBgp4PeerGroupOrfType_Type = Unsigned32
_FsBgp4PeerGroupOrfType_Object = MibTableColumn
fsBgp4PeerGroupOrfType = _FsBgp4PeerGroupOrfType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 34),
    _FsBgp4PeerGroupOrfType_Type()
)
fsBgp4PeerGroupOrfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupOrfType.setStatus("current")


class _FsBgp4PeerGroupOrfCapMode_Type(Integer32):
    """Custom type fsBgp4PeerGroupOrfCapMode based on Integer32"""
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


_FsBgp4PeerGroupOrfCapMode_Type.__name__ = "Integer32"
_FsBgp4PeerGroupOrfCapMode_Object = MibTableColumn
fsBgp4PeerGroupOrfCapMode = _FsBgp4PeerGroupOrfCapMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 35),
    _FsBgp4PeerGroupOrfCapMode_Type()
)
fsBgp4PeerGroupOrfCapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupOrfCapMode.setStatus("current")


class _FsBgp4PeerGroupOrfRequest_Type(Integer32):
    """Custom type fsBgp4PeerGroupOrfRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_FsBgp4PeerGroupOrfRequest_Type.__name__ = "Integer32"
_FsBgp4PeerGroupOrfRequest_Object = MibTableColumn
fsBgp4PeerGroupOrfRequest = _FsBgp4PeerGroupOrfRequest_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 36),
    _FsBgp4PeerGroupOrfRequest_Type()
)
fsBgp4PeerGroupOrfRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupOrfRequest.setStatus("current")


class _FsBgp4PeerGroupBfdStatus_Type(Integer32):
    """Custom type fsBgp4PeerGroupBfdStatus based on Integer32"""
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


_FsBgp4PeerGroupBfdStatus_Type.__name__ = "Integer32"
_FsBgp4PeerGroupBfdStatus_Object = MibTableColumn
fsBgp4PeerGroupBfdStatus = _FsBgp4PeerGroupBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 37),
    _FsBgp4PeerGroupBfdStatus_Type()
)
fsBgp4PeerGroupBfdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupBfdStatus.setStatus("current")


class _FsBgp4PeerGroupOverrideCapability_Type(Integer32):
    """Custom type fsBgp4PeerGroupOverrideCapability based on Integer32"""
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


_FsBgp4PeerGroupOverrideCapability_Type.__name__ = "Integer32"
_FsBgp4PeerGroupOverrideCapability_Object = MibTableColumn
fsBgp4PeerGroupOverrideCapability = _FsBgp4PeerGroupOverrideCapability_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 40, 1, 38),
    _FsBgp4PeerGroupOverrideCapability_Type()
)
fsBgp4PeerGroupOverrideCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerGroupOverrideCapability.setStatus("current")
_FsBgp4PeerGroupListTable_Object = MibTable
fsBgp4PeerGroupListTable = _FsBgp4PeerGroupListTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 41)
)
if mibBuilder.loadTexts:
    fsBgp4PeerGroupListTable.setStatus("current")
_FsBgp4PeerGroupListEntry_Object = MibTableRow
fsBgp4PeerGroupListEntry = _FsBgp4PeerGroupListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 41, 1)
)
fsBgp4PeerGroupListEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsBgp4PeerGroupName"),
    (0, "ARICENT-BGP-MIB", "fsBgp4PeerAddrType"),
    (0, "ARICENT-BGP-MIB", "fsBgp4PeerAddress"),
)
if mibBuilder.loadTexts:
    fsBgp4PeerGroupListEntry.setStatus("current")
_FsBgp4PeerAddrType_Type = InetAddressType
_FsBgp4PeerAddrType_Object = MibTableColumn
fsBgp4PeerAddrType = _FsBgp4PeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 41, 1, 1),
    _FsBgp4PeerAddrType_Type()
)
fsBgp4PeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4PeerAddrType.setStatus("current")
_FsBgp4PeerAddress_Type = InetAddress
_FsBgp4PeerAddress_Object = MibTableColumn
fsBgp4PeerAddress = _FsBgp4PeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 41, 1, 2),
    _FsBgp4PeerAddress_Type()
)
fsBgp4PeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4PeerAddress.setStatus("current")


class _FsBgp4PeerAddStatus_Type(Integer32):
    """Custom type fsBgp4PeerAddStatus based on Integer32"""
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


_FsBgp4PeerAddStatus_Type.__name__ = "Integer32"
_FsBgp4PeerAddStatus_Object = MibTableColumn
fsBgp4PeerAddStatus = _FsBgp4PeerAddStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 41, 1, 3),
    _FsBgp4PeerAddStatus_Type()
)
fsBgp4PeerAddStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4PeerAddStatus.setStatus("current")
_Fsbgp4TCPMKTAuth_ObjectIdentity = ObjectIdentity
fsbgp4TCPMKTAuth = _Fsbgp4TCPMKTAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 42)
)
_Fsbgp4TCPMKTAuthTable_Object = MibTable
fsbgp4TCPMKTAuthTable = _Fsbgp4TCPMKTAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 42, 1)
)
if mibBuilder.loadTexts:
    fsbgp4TCPMKTAuthTable.setStatus("current")
_Fsbgp4TCPMKTAuthEntry_Object = MibTableRow
fsbgp4TCPMKTAuthEntry = _Fsbgp4TCPMKTAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 42, 1, 1)
)
fsbgp4TCPMKTAuthEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4TCPMKTAuthKeyId"),
)
if mibBuilder.loadTexts:
    fsbgp4TCPMKTAuthEntry.setStatus("current")


class _Fsbgp4TCPMKTAuthKeyId_Type(Integer32):
    """Custom type fsbgp4TCPMKTAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fsbgp4TCPMKTAuthKeyId_Type.__name__ = "Integer32"
_Fsbgp4TCPMKTAuthKeyId_Object = MibTableColumn
fsbgp4TCPMKTAuthKeyId = _Fsbgp4TCPMKTAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 42, 1, 1, 1),
    _Fsbgp4TCPMKTAuthKeyId_Type()
)
fsbgp4TCPMKTAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4TCPMKTAuthKeyId.setStatus("current")


class _Fsbgp4TCPMKTAuthRecvKeyId_Type(Integer32):
    """Custom type fsbgp4TCPMKTAuthRecvKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fsbgp4TCPMKTAuthRecvKeyId_Type.__name__ = "Integer32"
_Fsbgp4TCPMKTAuthRecvKeyId_Object = MibTableColumn
fsbgp4TCPMKTAuthRecvKeyId = _Fsbgp4TCPMKTAuthRecvKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 42, 1, 1, 2),
    _Fsbgp4TCPMKTAuthRecvKeyId_Type()
)
fsbgp4TCPMKTAuthRecvKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4TCPMKTAuthRecvKeyId.setStatus("current")


class _Fsbgp4TCPMKTAuthMasterKey_Type(OctetString):
    """Custom type fsbgp4TCPMKTAuthMasterKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_Fsbgp4TCPMKTAuthMasterKey_Type.__name__ = "OctetString"
_Fsbgp4TCPMKTAuthMasterKey_Object = MibTableColumn
fsbgp4TCPMKTAuthMasterKey = _Fsbgp4TCPMKTAuthMasterKey_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 42, 1, 1, 3),
    _Fsbgp4TCPMKTAuthMasterKey_Type()
)
fsbgp4TCPMKTAuthMasterKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4TCPMKTAuthMasterKey.setStatus("current")


class _Fsbgp4TCPMKTAuthAlgo_Type(Integer32):
    """Custom type fsbgp4TCPMKTAuthAlgo based on Integer32"""
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


_Fsbgp4TCPMKTAuthAlgo_Type.__name__ = "Integer32"
_Fsbgp4TCPMKTAuthAlgo_Object = MibTableColumn
fsbgp4TCPMKTAuthAlgo = _Fsbgp4TCPMKTAuthAlgo_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 42, 1, 1, 4),
    _Fsbgp4TCPMKTAuthAlgo_Type()
)
fsbgp4TCPMKTAuthAlgo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4TCPMKTAuthAlgo.setStatus("current")
_Fsbgp4TCPMKTAuthTcpOptExc_Type = TruthValue
_Fsbgp4TCPMKTAuthTcpOptExc_Object = MibTableColumn
fsbgp4TCPMKTAuthTcpOptExc = _Fsbgp4TCPMKTAuthTcpOptExc_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 42, 1, 1, 5),
    _Fsbgp4TCPMKTAuthTcpOptExc_Type()
)
fsbgp4TCPMKTAuthTcpOptExc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4TCPMKTAuthTcpOptExc.setStatus("current")
_Fsbgp4TCPMKTAuthRowStatus_Type = RowStatus
_Fsbgp4TCPMKTAuthRowStatus_Object = MibTableColumn
fsbgp4TCPMKTAuthRowStatus = _Fsbgp4TCPMKTAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 42, 1, 1, 6),
    _Fsbgp4TCPMKTAuthRowStatus_Type()
)
fsbgp4TCPMKTAuthRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4TCPMKTAuthRowStatus.setStatus("current")
_Fsbgp4TCPAOAuthPeer_ObjectIdentity = ObjectIdentity
fsbgp4TCPAOAuthPeer = _Fsbgp4TCPAOAuthPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 43)
)
_Fsbgp4TCPAOAuthPeerTable_Object = MibTable
fsbgp4TCPAOAuthPeerTable = _Fsbgp4TCPAOAuthPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 43, 1)
)
if mibBuilder.loadTexts:
    fsbgp4TCPAOAuthPeerTable.setStatus("current")
_Fsbgp4TCPAOAuthPeerEntry_Object = MibTableRow
fsbgp4TCPAOAuthPeerEntry = _Fsbgp4TCPAOAuthPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 43, 1, 1)
)
fsbgp4TCPAOAuthPeerEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsbgp4TCPAOAuthPeerType"),
    (0, "ARICENT-BGP-MIB", "fsbgp4TCPAOAuthPeerAddr"),
    (0, "ARICENT-BGP-MIB", "fsbgp4TCPAOAuthKeyId"),
)
if mibBuilder.loadTexts:
    fsbgp4TCPAOAuthPeerEntry.setStatus("current")
_Fsbgp4TCPAOAuthPeerType_Type = InetAddressType
_Fsbgp4TCPAOAuthPeerType_Object = MibTableColumn
fsbgp4TCPAOAuthPeerType = _Fsbgp4TCPAOAuthPeerType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 43, 1, 1, 1),
    _Fsbgp4TCPAOAuthPeerType_Type()
)
fsbgp4TCPAOAuthPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4TCPAOAuthPeerType.setStatus("current")


class _Fsbgp4TCPAOAuthPeerAddr_Type(InetAddress):
    """Custom type fsbgp4TCPAOAuthPeerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Fsbgp4TCPAOAuthPeerAddr_Type.__name__ = "InetAddress"
_Fsbgp4TCPAOAuthPeerAddr_Object = MibTableColumn
fsbgp4TCPAOAuthPeerAddr = _Fsbgp4TCPAOAuthPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 43, 1, 1, 2),
    _Fsbgp4TCPAOAuthPeerAddr_Type()
)
fsbgp4TCPAOAuthPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4TCPAOAuthPeerAddr.setStatus("current")


class _Fsbgp4TCPAOAuthKeyId_Type(Integer32):
    """Custom type fsbgp4TCPAOAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Fsbgp4TCPAOAuthKeyId_Type.__name__ = "Integer32"
_Fsbgp4TCPAOAuthKeyId_Object = MibTableColumn
fsbgp4TCPAOAuthKeyId = _Fsbgp4TCPAOAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 43, 1, 1, 3),
    _Fsbgp4TCPAOAuthKeyId_Type()
)
fsbgp4TCPAOAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsbgp4TCPAOAuthKeyId.setStatus("current")


class _Fsbgp4TCPAOAuthKeyStatus_Type(Integer32):
    """Custom type fsbgp4TCPAOAuthKeyStatus based on Integer32"""
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


_Fsbgp4TCPAOAuthKeyStatus_Type.__name__ = "Integer32"
_Fsbgp4TCPAOAuthKeyStatus_Object = MibTableColumn
fsbgp4TCPAOAuthKeyStatus = _Fsbgp4TCPAOAuthKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 43, 1, 1, 4),
    _Fsbgp4TCPAOAuthKeyStatus_Type()
)
fsbgp4TCPAOAuthKeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4TCPAOAuthKeyStatus.setStatus("current")
_Fsbgp4TCPAOAuthKeyStartAccept_Type = DateAndTime
_Fsbgp4TCPAOAuthKeyStartAccept_Object = MibTableColumn
fsbgp4TCPAOAuthKeyStartAccept = _Fsbgp4TCPAOAuthKeyStartAccept_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 43, 1, 1, 5),
    _Fsbgp4TCPAOAuthKeyStartAccept_Type()
)
fsbgp4TCPAOAuthKeyStartAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4TCPAOAuthKeyStartAccept.setStatus("current")
_Fsbgp4TCPAOAuthKeyStartGenerate_Type = DateAndTime
_Fsbgp4TCPAOAuthKeyStartGenerate_Object = MibTableColumn
fsbgp4TCPAOAuthKeyStartGenerate = _Fsbgp4TCPAOAuthKeyStartGenerate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 43, 1, 1, 6),
    _Fsbgp4TCPAOAuthKeyStartGenerate_Type()
)
fsbgp4TCPAOAuthKeyStartGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4TCPAOAuthKeyStartGenerate.setStatus("current")
_Fsbgp4TCPAOAuthKeyStopGenerate_Type = DateAndTime
_Fsbgp4TCPAOAuthKeyStopGenerate_Object = MibTableColumn
fsbgp4TCPAOAuthKeyStopGenerate = _Fsbgp4TCPAOAuthKeyStopGenerate_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 43, 1, 1, 7),
    _Fsbgp4TCPAOAuthKeyStopGenerate_Type()
)
fsbgp4TCPAOAuthKeyStopGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4TCPAOAuthKeyStopGenerate.setStatus("current")
_Fsbgp4TCPAOAuthKeyStopAccept_Type = DateAndTime
_Fsbgp4TCPAOAuthKeyStopAccept_Object = MibTableColumn
fsbgp4TCPAOAuthKeyStopAccept = _Fsbgp4TCPAOAuthKeyStopAccept_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 43, 1, 1, 8),
    _Fsbgp4TCPAOAuthKeyStopAccept_Type()
)
fsbgp4TCPAOAuthKeyStopAccept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsbgp4TCPAOAuthKeyStopAccept.setStatus("current")
_FsBgp4ORFListTable_Object = MibTable
fsBgp4ORFListTable = _FsBgp4ORFListTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 44)
)
if mibBuilder.loadTexts:
    fsBgp4ORFListTable.setStatus("current")
_FsBgp4ORFListEntry_Object = MibTableRow
fsBgp4ORFListEntry = _FsBgp4ORFListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 44, 1)
)
fsBgp4ORFListEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsBgp4ORFPeerAddrType"),
    (0, "ARICENT-BGP-MIB", "fsBgp4ORFPeerAddr"),
    (0, "ARICENT-BGP-MIB", "fsBgp4ORFAfi"),
    (0, "ARICENT-BGP-MIB", "fsBgp4ORFSafi"),
    (0, "ARICENT-BGP-MIB", "fsBgp4ORFType"),
    (0, "ARICENT-BGP-MIB", "fsBgp4ORFSequence"),
    (0, "ARICENT-BGP-MIB", "fsBgp4ORFAddrPrefix"),
    (0, "ARICENT-BGP-MIB", "fsBgp4ORFAddrPrefixLen"),
    (0, "ARICENT-BGP-MIB", "fsBgp4ORFMinLength"),
    (0, "ARICENT-BGP-MIB", "fsBgp4ORFMaxLength"),
    (0, "ARICENT-BGP-MIB", "fsBgp4ORFAction"),
)
if mibBuilder.loadTexts:
    fsBgp4ORFListEntry.setStatus("current")
_FsBgp4ORFPeerAddrType_Type = InetAddressType
_FsBgp4ORFPeerAddrType_Object = MibTableColumn
fsBgp4ORFPeerAddrType = _FsBgp4ORFPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 44, 1, 1),
    _FsBgp4ORFPeerAddrType_Type()
)
fsBgp4ORFPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4ORFPeerAddrType.setStatus("current")
_FsBgp4ORFPeerAddr_Type = InetAddress
_FsBgp4ORFPeerAddr_Object = MibTableColumn
fsBgp4ORFPeerAddr = _FsBgp4ORFPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 44, 1, 2),
    _FsBgp4ORFPeerAddr_Type()
)
fsBgp4ORFPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4ORFPeerAddr.setStatus("current")
_FsBgp4ORFAfi_Type = InetAddressType
_FsBgp4ORFAfi_Object = MibTableColumn
fsBgp4ORFAfi = _FsBgp4ORFAfi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 44, 1, 3),
    _FsBgp4ORFAfi_Type()
)
fsBgp4ORFAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4ORFAfi.setStatus("current")
_FsBgp4ORFSafi_Type = BgpSafi
_FsBgp4ORFSafi_Object = MibTableColumn
fsBgp4ORFSafi = _FsBgp4ORFSafi_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 44, 1, 4),
    _FsBgp4ORFSafi_Type()
)
fsBgp4ORFSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4ORFSafi.setStatus("current")
_FsBgp4ORFType_Type = Unsigned32
_FsBgp4ORFType_Object = MibTableColumn
fsBgp4ORFType = _FsBgp4ORFType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 44, 1, 5),
    _FsBgp4ORFType_Type()
)
fsBgp4ORFType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4ORFType.setStatus("current")
_FsBgp4ORFSequence_Type = Unsigned32
_FsBgp4ORFSequence_Object = MibTableColumn
fsBgp4ORFSequence = _FsBgp4ORFSequence_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 44, 1, 6),
    _FsBgp4ORFSequence_Type()
)
fsBgp4ORFSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4ORFSequence.setStatus("current")
_FsBgp4ORFAddrPrefix_Type = InetAddress
_FsBgp4ORFAddrPrefix_Object = MibTableColumn
fsBgp4ORFAddrPrefix = _FsBgp4ORFAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 44, 1, 7),
    _FsBgp4ORFAddrPrefix_Type()
)
fsBgp4ORFAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4ORFAddrPrefix.setStatus("current")


class _FsBgp4ORFAddrPrefixLen_Type(Unsigned32):
    """Custom type fsBgp4ORFAddrPrefixLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsBgp4ORFAddrPrefixLen_Type.__name__ = "Unsigned32"
_FsBgp4ORFAddrPrefixLen_Object = MibTableColumn
fsBgp4ORFAddrPrefixLen = _FsBgp4ORFAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 44, 1, 8),
    _FsBgp4ORFAddrPrefixLen_Type()
)
fsBgp4ORFAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4ORFAddrPrefixLen.setStatus("current")


class _FsBgp4ORFMinLength_Type(Unsigned32):
    """Custom type fsBgp4ORFMinLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsBgp4ORFMinLength_Type.__name__ = "Unsigned32"
_FsBgp4ORFMinLength_Object = MibTableColumn
fsBgp4ORFMinLength = _FsBgp4ORFMinLength_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 44, 1, 9),
    _FsBgp4ORFMinLength_Type()
)
fsBgp4ORFMinLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4ORFMinLength.setStatus("current")


class _FsBgp4ORFMaxLength_Type(Unsigned32):
    """Custom type fsBgp4ORFMaxLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsBgp4ORFMaxLength_Type.__name__ = "Unsigned32"
_FsBgp4ORFMaxLength_Object = MibTableColumn
fsBgp4ORFMaxLength = _FsBgp4ORFMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 44, 1, 10),
    _FsBgp4ORFMaxLength_Type()
)
fsBgp4ORFMaxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4ORFMaxLength.setStatus("current")


class _FsBgp4ORFAction_Type(Integer32):
    """Custom type fsBgp4ORFAction based on Integer32"""
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


_FsBgp4ORFAction_Type.__name__ = "Integer32"
_FsBgp4ORFAction_Object = MibTableColumn
fsBgp4ORFAction = _FsBgp4ORFAction_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 44, 1, 11),
    _FsBgp4ORFAction_Type()
)
fsBgp4ORFAction.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4ORFAction.setStatus("current")
_FsBgp4TestGroup_ObjectIdentity = ObjectIdentity
fsBgp4TestGroup = _FsBgp4TestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 41, 45)
)
_FsBgp4RmTestObject_Type = Integer32
_FsBgp4RmTestObject_Object = MibScalar
fsBgp4RmTestObject = _FsBgp4RmTestObject_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 45, 1),
    _FsBgp4RmTestObject_Type()
)
fsBgp4RmTestObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4RmTestObject.setStatus("current")
_FsBgp4RRDNetworkTable_Object = MibTable
fsBgp4RRDNetworkTable = _FsBgp4RRDNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 46)
)
if mibBuilder.loadTexts:
    fsBgp4RRDNetworkTable.setStatus("current")
_FsBgp4RRDNetworkEntry_Object = MibTableRow
fsBgp4RRDNetworkEntry = _FsBgp4RRDNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 46, 1)
)
fsBgp4RRDNetworkEntry.setIndexNames(
    (0, "ARICENT-BGP-MIB", "fsBgp4RRDNetworkAddr"),
)
if mibBuilder.loadTexts:
    fsBgp4RRDNetworkEntry.setStatus("current")
_FsBgp4RRDNetworkAddr_Type = InetAddress
_FsBgp4RRDNetworkAddr_Object = MibTableColumn
fsBgp4RRDNetworkAddr = _FsBgp4RRDNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 46, 1, 1),
    _FsBgp4RRDNetworkAddr_Type()
)
fsBgp4RRDNetworkAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBgp4RRDNetworkAddr.setStatus("current")
_FsBgp4RRDNetworkAddrType_Type = InetAddressType
_FsBgp4RRDNetworkAddrType_Object = MibTableColumn
fsBgp4RRDNetworkAddrType = _FsBgp4RRDNetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 46, 1, 2),
    _FsBgp4RRDNetworkAddrType_Type()
)
fsBgp4RRDNetworkAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4RRDNetworkAddrType.setStatus("current")


class _FsBgp4RRDNetworkPrefixLen_Type(Integer32):
    """Custom type fsBgp4RRDNetworkPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsBgp4RRDNetworkPrefixLen_Type.__name__ = "Integer32"
_FsBgp4RRDNetworkPrefixLen_Object = MibTableColumn
fsBgp4RRDNetworkPrefixLen = _FsBgp4RRDNetworkPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 46, 1, 3),
    _FsBgp4RRDNetworkPrefixLen_Type()
)
fsBgp4RRDNetworkPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4RRDNetworkPrefixLen.setStatus("current")
_FsBgp4RRDNetworkRowStatus_Type = RowStatus
_FsBgp4RRDNetworkRowStatus_Object = MibTableColumn
fsBgp4RRDNetworkRowStatus = _FsBgp4RRDNetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 41, 46, 1, 4),
    _FsBgp4RRDNetworkRowStatus_Type()
)
fsBgp4RRDNetworkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsBgp4RRDNetworkRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

fsbgp4RestartStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 41, 38, 0, 1)
)
fsbgp4RestartStatusChange.setObjects(
      *(("ARICENT-BGP-MIB", "fsbgp4Identifier"),
        ("ARICENT-BGP-MIB", "fsbgp4RestartStatus"),
        ("ARICENT-BGP-MIB", "fsbgp4GRRestartTimeInterval"),
        ("ARICENT-BGP-MIB", "fsbgp4RestartExitReason"))
)
if mibBuilder.loadTexts:
    fsbgp4RestartStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-BGP-MIB",
    **{"InetAddress": InetAddress,
       "InetAddressType": InetAddressType,
       "BgpSafi": BgpSafi,
       "fsbgp": fsbgp,
       "fsbgp4Scalars": fsbgp4Scalars,
       "fsbgp4GlobalAdminStatus": fsbgp4GlobalAdminStatus,
       "fsbgp4LocalAs": fsbgp4LocalAs,
       "fsbgp4Identifier": fsbgp4Identifier,
       "fsbgp4Synchronization": fsbgp4Synchronization,
       "fsbgp4DefaultLocalPref": fsbgp4DefaultLocalPref,
       "fsbgp4AdvtNonBgpRt": fsbgp4AdvtNonBgpRt,
       "fsbgp4TraceEnable": fsbgp4TraceEnable,
       "fsbgp4DebugEnable": fsbgp4DebugEnable,
       "fsbgp4OverlappingRoute": fsbgp4OverlappingRoute,
       "fsbgp4MaxPeerEntry": fsbgp4MaxPeerEntry,
       "fsbgp4MaxNoofRoutes": fsbgp4MaxNoofRoutes,
       "fsbgp4AlwaysCompareMED": fsbgp4AlwaysCompareMED,
       "fsbgp4DefaultOriginate": fsbgp4DefaultOriginate,
       "fsbgp4DefaultIpv4UniCast": fsbgp4DefaultIpv4UniCast,
       "fsbgp4GRAdminStatus": fsbgp4GRAdminStatus,
       "fsbgp4GRRestartTimeInterval": fsbgp4GRRestartTimeInterval,
       "fsbgp4GRSelectionDeferralTimeInterval": fsbgp4GRSelectionDeferralTimeInterval,
       "fsbgp4GRStaleTimeInterval": fsbgp4GRStaleTimeInterval,
       "fsbgp4GRMode": fsbgp4GRMode,
       "fsbgp4RestartSupport": fsbgp4RestartSupport,
       "fsbgp4RestartStatus": fsbgp4RestartStatus,
       "fsbgp4RestartExitReason": fsbgp4RestartExitReason,
       "fsbgp4RestartReason": fsbgp4RestartReason,
       "fsbgp4ForwardingPreservation": fsbgp4ForwardingPreservation,
       "fsbgp4IsTrapEnabled": fsbgp4IsTrapEnabled,
       "fsbgp4NextHopProcessingInterval": fsbgp4NextHopProcessingInterval,
       "fsbgp4IBGPRedistributionStatus": fsbgp4IBGPRedistributionStatus,
       "fsbgp4IBGPMaxPaths": fsbgp4IBGPMaxPaths,
       "fsbgp4EBGPMaxPaths": fsbgp4EBGPMaxPaths,
       "fsbgp4EIBGPMaxPaths": fsbgp4EIBGPMaxPaths,
       "fsbgp4OperIBGPMaxPaths": fsbgp4OperIBGPMaxPaths,
       "fsbgp4OperEBGPMaxPaths": fsbgp4OperEBGPMaxPaths,
       "fsbgp4OperEIBGPMaxPaths": fsbgp4OperEIBGPMaxPaths,
       "fsbgp4FourByteASNSupportStatus": fsbgp4FourByteASNSupportStatus,
       "fsbgp4FourByteASNotationType": fsbgp4FourByteASNotationType,
       "fsbgp4VpnLabelAllocPolicy": fsbgp4VpnLabelAllocPolicy,
       "fsbgp4MacMobDuplicationTimeInterval": fsbgp4MacMobDuplicationTimeInterval,
       "fsbgp4MaxMacMoves": fsbgp4MaxMacMoves,
       "fsbgp4VpnRouteLeakStatus": fsbgp4VpnRouteLeakStatus,
       "fsbgp4PeerExtTable": fsbgp4PeerExtTable,
       "fsbgp4PeerExtEntry": fsbgp4PeerExtEntry,
       "fsbgp4PeerExtPeerRemoteAddr": fsbgp4PeerExtPeerRemoteAddr,
       "fsbgp4PeerExtConfigurePeer": fsbgp4PeerExtConfigurePeer,
       "fsbgp4PeerExtPeerRemoteAs": fsbgp4PeerExtPeerRemoteAs,
       "fsbgp4PeerExtEBGPMultiHop": fsbgp4PeerExtEBGPMultiHop,
       "fsbgp4PeerExtNextHopSelf": fsbgp4PeerExtNextHopSelf,
       "fsbgp4PeerExtConnSrcIfId": fsbgp4PeerExtConnSrcIfId,
       "fsbgp4PeerExtRflClient": fsbgp4PeerExtRflClient,
       "fsbgp4MEDTable": fsbgp4MEDTable,
       "fsbgp4MEDEntry": fsbgp4MEDEntry,
       "fsbgp4MEDIndex": fsbgp4MEDIndex,
       "fsbgp4MEDAdminStatus": fsbgp4MEDAdminStatus,
       "fsbgp4MEDRemoteAS": fsbgp4MEDRemoteAS,
       "fsbgp4MEDIPAddrPrefix": fsbgp4MEDIPAddrPrefix,
       "fsbgp4MEDIPAddrPrefixLen": fsbgp4MEDIPAddrPrefixLen,
       "fsbgp4MEDIntermediateAS": fsbgp4MEDIntermediateAS,
       "fsbgp4MEDDirection": fsbgp4MEDDirection,
       "fsbgp4MEDValue": fsbgp4MEDValue,
       "fsbgp4MEDPreference": fsbgp4MEDPreference,
       "fsbgp4LocalPrefTable": fsbgp4LocalPrefTable,
       "fsbgp4LocalPrefEntry": fsbgp4LocalPrefEntry,
       "fsbgp4LocalPrefIndex": fsbgp4LocalPrefIndex,
       "fsbgp4LocalPrefAdminStatus": fsbgp4LocalPrefAdminStatus,
       "fsbgp4LocalPrefRemoteAS": fsbgp4LocalPrefRemoteAS,
       "fsbgp4LocalPrefIPAddrPrefix": fsbgp4LocalPrefIPAddrPrefix,
       "fsbgp4LocalPrefIPAddrPrefixLen": fsbgp4LocalPrefIPAddrPrefixLen,
       "fsbgp4LocalPrefIntermediateAS": fsbgp4LocalPrefIntermediateAS,
       "fsbgp4LocalPrefDirection": fsbgp4LocalPrefDirection,
       "fsbgp4LocalPrefValue": fsbgp4LocalPrefValue,
       "fsbgp4LocalPrefPreference": fsbgp4LocalPrefPreference,
       "fsbgp4UpdateFilterTable": fsbgp4UpdateFilterTable,
       "fsbgp4UpdateFilterEntry": fsbgp4UpdateFilterEntry,
       "fsbgp4UpdateFilterIndex": fsbgp4UpdateFilterIndex,
       "fsbgp4UpdateFilterAdminStatus": fsbgp4UpdateFilterAdminStatus,
       "fsbgp4UpdateFilterRemoteAS": fsbgp4UpdateFilterRemoteAS,
       "fsbgp4UpdateFilterIPAddrPrefix": fsbgp4UpdateFilterIPAddrPrefix,
       "fsbgp4UpdateFilterIPAddrPrefixLen": fsbgp4UpdateFilterIPAddrPrefixLen,
       "fsbgp4UpdateFilterIntermediateAS": fsbgp4UpdateFilterIntermediateAS,
       "fsbgp4UpdateFilterDirection": fsbgp4UpdateFilterDirection,
       "fsbgp4UpdateFilterAction": fsbgp4UpdateFilterAction,
       "fsbgp4AggregateTable": fsbgp4AggregateTable,
       "fsbgp4AggregateEntry": fsbgp4AggregateEntry,
       "fsbgp4AggregateIndex": fsbgp4AggregateIndex,
       "fsbgp4AggregateAdminStatus": fsbgp4AggregateAdminStatus,
       "fsbgp4AggregateIPAddrPrefix": fsbgp4AggregateIPAddrPrefix,
       "fsbgp4AggregateIPAddrPrefixLen": fsbgp4AggregateIPAddrPrefixLen,
       "fsbgp4AggregateAdvertise": fsbgp4AggregateAdvertise,
       "fsbgp4RRDGroup": fsbgp4RRDGroup,
       "fsbgp4RRDAdminStatus": fsbgp4RRDAdminStatus,
       "fsbgp4RRDProtoMaskForEnable": fsbgp4RRDProtoMaskForEnable,
       "fsbgp4RRDSrcProtoMaskForDisable": fsbgp4RRDSrcProtoMaskForDisable,
       "fsbgp4RRDDefaultMetric": fsbgp4RRDDefaultMetric,
       "fsbgp4RRDRouteMapName": fsbgp4RRDRouteMapName,
       "fsbgp4RRDMatchTypeEnable": fsbgp4RRDMatchTypeEnable,
       "fsbgp4RRDMatchTypeDisable": fsbgp4RRDMatchTypeDisable,
       "fsbgp4RRDMetricTable": fsbgp4RRDMetricTable,
       "fsbgp4RRDMetricEntry": fsbgp4RRDMetricEntry,
       "fsBgp4RRDMetricProtocolId": fsBgp4RRDMetricProtocolId,
       "fsBgp4RRDMetricValue": fsBgp4RRDMetricValue,
       "fsbgp4ImportRouteTable": fsbgp4ImportRouteTable,
       "fsbgp4ImportRouteEntry": fsbgp4ImportRouteEntry,
       "fsbgp4ImportRoutePrefix": fsbgp4ImportRoutePrefix,
       "fsbgp4ImportRoutePrefixLen": fsbgp4ImportRoutePrefixLen,
       "fsbgp4ImportRouteProtocol": fsbgp4ImportRouteProtocol,
       "fsbgp4ImportRouteNextHop": fsbgp4ImportRouteNextHop,
       "fsbgp4ImportRouteIfIndex": fsbgp4ImportRouteIfIndex,
       "fsbgp4ImportRouteMetric": fsbgp4ImportRouteMetric,
       "fsbgp4ImportRouteAction": fsbgp4ImportRouteAction,
       "fsbgp4FsmTransitionHistTable": fsbgp4FsmTransitionHistTable,
       "fsbgp4FsmTransitionHistEntry": fsbgp4FsmTransitionHistEntry,
       "fsbgp4Peer": fsbgp4Peer,
       "fsbgp4FsmTransitionHist": fsbgp4FsmTransitionHist,
       "fsbgpRfl": fsbgpRfl,
       "fsbgp4RflScalars": fsbgp4RflScalars,
       "fsbgp4RflbgpClusterId": fsbgp4RflbgpClusterId,
       "fsbgp4RflRflSupport": fsbgp4RflRflSupport,
       "fsbgp4RflRouteReflectorTable": fsbgp4RflRouteReflectorTable,
       "fsbgp4RflRouteReflectorEntry": fsbgp4RflRouteReflectorEntry,
       "fsbgp4RflPathAttrAddrPrefix": fsbgp4RflPathAttrAddrPrefix,
       "fsbgp4RflPathAttrAddrPrefixLen": fsbgp4RflPathAttrAddrPrefixLen,
       "fsbgp4RflPathAttrPeer": fsbgp4RflPathAttrPeer,
       "fsbgp4RflPathAttrOriginatorId": fsbgp4RflPathAttrOriginatorId,
       "fsbgp4RflPathAttrClusterList": fsbgp4RflPathAttrClusterList,
       "fsbgp4Rfd": fsbgp4Rfd,
       "fsbgp4RfdScalars": fsbgp4RfdScalars,
       "fsbgp4RfdCutOff": fsbgp4RfdCutOff,
       "fsbgp4RfdReuse": fsbgp4RfdReuse,
       "fsbgp4RfdCeiling": fsbgp4RfdCeiling,
       "fsbgp4RfdMaxHoldDownTime": fsbgp4RfdMaxHoldDownTime,
       "fsbgp4RfdDecayHalfLifeTime": fsbgp4RfdDecayHalfLifeTime,
       "fsbgp4RfdDecayTimerGranularity": fsbgp4RfdDecayTimerGranularity,
       "fsbgp4RfdReuseTimerGranularity": fsbgp4RfdReuseTimerGranularity,
       "fsbgp4RfdReuseIndxArraySize": fsbgp4RfdReuseIndxArraySize,
       "fsbgp4RfdAdminStatus": fsbgp4RfdAdminStatus,
       "fsbgp4RfdRtDampHistTable": fsbgp4RfdRtDampHistTable,
       "fsbgp4RfdRtDampHistEntry": fsbgp4RfdRtDampHistEntry,
       "fsbgp4PathAttrAddrPrefix": fsbgp4PathAttrAddrPrefix,
       "fsbgp4PathAttrAddrPrefixLen": fsbgp4PathAttrAddrPrefixLen,
       "fsbgp4PathAttrPeer": fsbgp4PathAttrPeer,
       "fsbgp4RtDampHistInstance": fsbgp4RtDampHistInstance,
       "fsbgp4RfdRtFom": fsbgp4RfdRtFom,
       "fsbgp4RfdRtLastUpdtTime": fsbgp4RfdRtLastUpdtTime,
       "fsbgp4RfdRtState": fsbgp4RfdRtState,
       "fsbgp4RfdRtStatus": fsbgp4RfdRtStatus,
       "fsbgp4RfdPeerDampHistTable": fsbgp4RfdPeerDampHistTable,
       "fsbgp4RfdPeerDampHistEntry": fsbgp4RfdPeerDampHistEntry,
       "fsbgp4PeerRemoteIpAddr": fsbgp4PeerRemoteIpAddr,
       "fsbgp4RfdPeerFom": fsbgp4RfdPeerFom,
       "fsbgp4RfdPeerLastUpdtTime": fsbgp4RfdPeerLastUpdtTime,
       "fsbgp4RfdPeerState": fsbgp4RfdPeerState,
       "fsbgp4RfdPeerStatus": fsbgp4RfdPeerStatus,
       "fsbgp4RfdRtsReuseListTable": fsbgp4RfdRtsReuseListTable,
       "fsbgp4RfdRtsReuseListEntry": fsbgp4RfdRtsReuseListEntry,
       "fsbgp4RtIPPrefix": fsbgp4RtIPPrefix,
       "fsbgp4RtIPPrefixLen": fsbgp4RtIPPrefixLen,
       "fsbgp4PeerRemAddress": fsbgp4PeerRemAddress,
       "fsbgp4RfdRtReuseListInstance": fsbgp4RfdRtReuseListInstance,
       "fsbgp4RfdRtReuseListRtFom": fsbgp4RfdRtReuseListRtFom,
       "fsbgp4RfdRtReuseListRtLastUpdtTime": fsbgp4RfdRtReuseListRtLastUpdtTime,
       "fsbgp4RfdRtReuseListRtState": fsbgp4RfdRtReuseListRtState,
       "fsbgp4RfdRtReuseListRtStatus": fsbgp4RfdRtReuseListRtStatus,
       "fsbgp4RfdPeerReuseListTable": fsbgp4RfdPeerReuseListTable,
       "fsbgp4RfdPeerReuseListEntry": fsbgp4RfdPeerReuseListEntry,
       "fsbgp4RfdPeerRemIpAddr": fsbgp4RfdPeerRemIpAddr,
       "fsbgp4RfdPeerReuseListPeerFom": fsbgp4RfdPeerReuseListPeerFom,
       "fsbgp4RfdPeerReuseListLastUpdtTime": fsbgp4RfdPeerReuseListLastUpdtTime,
       "fsbgp4RfdPeerReuseListPeerState": fsbgp4RfdPeerReuseListPeerState,
       "fsbgp4RfdPeerReuseListPeerStatus": fsbgp4RfdPeerReuseListPeerStatus,
       "fsbgpComm": fsbgpComm,
       "fsbgp4CommScalars": fsbgp4CommScalars,
       "fsbgp4CommMaxInFTblEntries": fsbgp4CommMaxInFTblEntries,
       "fsbgp4CommMaxOutFTblEntries": fsbgp4CommMaxOutFTblEntries,
       "fsbgp4CommRouteAddCommTable": fsbgp4CommRouteAddCommTable,
       "fsbgp4CommRouteAddCommEntry": fsbgp4CommRouteAddCommEntry,
       "fsbgp4AddCommIpNetwork": fsbgp4AddCommIpNetwork,
       "fsbgp4AddCommIpPrefixLen": fsbgp4AddCommIpPrefixLen,
       "fsbgp4AddCommVal": fsbgp4AddCommVal,
       "fsbgp4AddCommRowStatus": fsbgp4AddCommRowStatus,
       "fsbgp4CommRouteDeleteCommTable": fsbgp4CommRouteDeleteCommTable,
       "fsbgp4CommRouteDeleteCommEntry": fsbgp4CommRouteDeleteCommEntry,
       "fsbgp4DeleteCommIpNetwork": fsbgp4DeleteCommIpNetwork,
       "fsbgp4DeleteCommIpPrefixLen": fsbgp4DeleteCommIpPrefixLen,
       "fsbgp4DeleteCommVal": fsbgp4DeleteCommVal,
       "fsbgp4DeleteCommRowStatus": fsbgp4DeleteCommRowStatus,
       "fsbgp4CommRouteCommSetStatusTable": fsbgp4CommRouteCommSetStatusTable,
       "fsbgp4CommRouteCommSetStatusEntry": fsbgp4CommRouteCommSetStatusEntry,
       "fsbgp4CommSetStatusIpNetwork": fsbgp4CommSetStatusIpNetwork,
       "fsbgp4CommSetStatusIpPrefixLen": fsbgp4CommSetStatusIpPrefixLen,
       "fsbgp4CommSetStatus": fsbgp4CommSetStatus,
       "fsbgp4CommSetStatusRowStatus": fsbgp4CommSetStatusRowStatus,
       "fsbgp4CommPeerSendStatusTable": fsbgp4CommPeerSendStatusTable,
       "fsbgp4CommPeerSendStatusEntry": fsbgp4CommPeerSendStatusEntry,
       "fsbgp4PeerAddress": fsbgp4PeerAddress,
       "fsbgp4CommSendStatus": fsbgp4CommSendStatus,
       "fsbgp4CommPeerSendRowStatus": fsbgp4CommPeerSendRowStatus,
       "fsbgp4CommInFilterTable": fsbgp4CommInFilterTable,
       "fsbgp4CommInFilterEntry": fsbgp4CommInFilterEntry,
       "fsbgp4InFilterCommVal": fsbgp4InFilterCommVal,
       "fsbgp4CommIncomingFilterStatus": fsbgp4CommIncomingFilterStatus,
       "fsbgp4InFilterRowStatus": fsbgp4InFilterRowStatus,
       "fsbgp4CommOutFilterTable": fsbgp4CommOutFilterTable,
       "fsbgp4CommOutFilterEntry": fsbgp4CommOutFilterEntry,
       "fsbgp4OutFilterCommVal": fsbgp4OutFilterCommVal,
       "fsbgp4CommOutgoingFilterStatus": fsbgp4CommOutgoingFilterStatus,
       "fsbgp4OutFilterRowStatus": fsbgp4OutFilterRowStatus,
       "fsbgp4CommReceivedRouteCommTable": fsbgp4CommReceivedRouteCommTable,
       "fsbgp4CommReceivedRouteCommEntry": fsbgp4CommReceivedRouteCommEntry,
       "fsbgp4IpNet": fsbgp4IpNet,
       "fsbgp4IPPrefixLength": fsbgp4IPPrefixLength,
       "fsbgp4PeerRemAddr": fsbgp4PeerRemAddr,
       "fsbgp4ReceivedRouteCommPath": fsbgp4ReceivedRouteCommPath,
       "fsbgpExtComm": fsbgpExtComm,
       "fsbgp4ExtCommScalars": fsbgp4ExtCommScalars,
       "fsbgp4ExtCommMaxInFTblEntries": fsbgp4ExtCommMaxInFTblEntries,
       "fsbgp4ExtCommMaxOutFTblEntries": fsbgp4ExtCommMaxOutFTblEntries,
       "fsbgp4ExtCommRouteAddExtCommTable": fsbgp4ExtCommRouteAddExtCommTable,
       "fsbgp4ExtCommRouteAddExtCommEntry": fsbgp4ExtCommRouteAddExtCommEntry,
       "fsbgp4AddExtCommIpNetwork": fsbgp4AddExtCommIpNetwork,
       "fsbgp4AddExtCommIpPrefixLen": fsbgp4AddExtCommIpPrefixLen,
       "fsbgp4AddExtCommVal": fsbgp4AddExtCommVal,
       "fsbgp4AddExtCommRowStatus": fsbgp4AddExtCommRowStatus,
       "fsbgp4ExtCommRouteDeleteExtCommTable": fsbgp4ExtCommRouteDeleteExtCommTable,
       "fsbgp4ExtCommRouteDeleteExtCommEntry": fsbgp4ExtCommRouteDeleteExtCommEntry,
       "fsbgp4DeleteExtCommIpNetwork": fsbgp4DeleteExtCommIpNetwork,
       "fsbgp4DeleteExtCommIpPrefixLen": fsbgp4DeleteExtCommIpPrefixLen,
       "fsbgp4DeleteExtCommVal": fsbgp4DeleteExtCommVal,
       "fsbgp4DeleteExtCommRowStatus": fsbgp4DeleteExtCommRowStatus,
       "fsbgp4ExtCommRouteExtCommSetStatusTable": fsbgp4ExtCommRouteExtCommSetStatusTable,
       "fsbgp4ExtCommRouteExtCommSetStatusEntry": fsbgp4ExtCommRouteExtCommSetStatusEntry,
       "fsbgp4ExtCommSetStatusIpNetwork": fsbgp4ExtCommSetStatusIpNetwork,
       "fsbgp4ExtCommSetStatusIpPrefixLen": fsbgp4ExtCommSetStatusIpPrefixLen,
       "fsbgp4ExtCommSetStatus": fsbgp4ExtCommSetStatus,
       "fsbgp4ExtCommSetStatusRowStatus": fsbgp4ExtCommSetStatusRowStatus,
       "fsbgp4ExtCommPeerSendStatusTable": fsbgp4ExtCommPeerSendStatusTable,
       "fsbgp4ExtCommPeerSendStatusEntry": fsbgp4ExtCommPeerSendStatusEntry,
       "fsbgp4ExtCommPeerAddress": fsbgp4ExtCommPeerAddress,
       "fsbgp4ExtCommPeerSendStatus": fsbgp4ExtCommPeerSendStatus,
       "fsbgp4ExtCommPeerSendStatusRowStatus": fsbgp4ExtCommPeerSendStatusRowStatus,
       "fsbgp4ExtCommInFilterTable": fsbgp4ExtCommInFilterTable,
       "fsbgp4ExtCommInFilterEntry": fsbgp4ExtCommInFilterEntry,
       "fsbgp4ExtCommInFilterCommVal": fsbgp4ExtCommInFilterCommVal,
       "fsbgp4ExtCommIncomingFilterStatus": fsbgp4ExtCommIncomingFilterStatus,
       "fsbgp4ExtCommInFilterRowStatus": fsbgp4ExtCommInFilterRowStatus,
       "fsbgp4ExtCommOutFilterTable": fsbgp4ExtCommOutFilterTable,
       "fsbgp4ExtCommOutFilterEntry": fsbgp4ExtCommOutFilterEntry,
       "fsbgp4ExtCommOutFilterCommVal": fsbgp4ExtCommOutFilterCommVal,
       "fsbgp4ExtCommOutgoingFilterStatus": fsbgp4ExtCommOutgoingFilterStatus,
       "fsbgp4ExtCommOutFilterRowStatus": fsbgp4ExtCommOutFilterRowStatus,
       "fsbgp4PeerLinkBwTable": fsbgp4PeerLinkBwTable,
       "fsbgp4PeerLinkBwEntry": fsbgp4PeerLinkBwEntry,
       "fsbgp4PeerLinkRemAddr": fsbgp4PeerLinkRemAddr,
       "fsbgp4LinkBandWidth": fsbgp4LinkBandWidth,
       "fsbgp4PeerLinkBwRowStatus": fsbgp4PeerLinkBwRowStatus,
       "fsbgp4ExtCommReceivedRouteExtCommTable": fsbgp4ExtCommReceivedRouteExtCommTable,
       "fsbgp4ExtCommReceivedRouteExtCommEntry": fsbgp4ExtCommReceivedRouteExtCommEntry,
       "fsbgp4ExtCommIpNet": fsbgp4ExtCommIpNet,
       "fsbgp4ExtCommIPPrefixLength": fsbgp4ExtCommIPPrefixLength,
       "fsbgp4ExtCommPeerRemAddr": fsbgp4ExtCommPeerRemAddr,
       "fsbgp4ReceivedRouteExtCommPath": fsbgp4ReceivedRouteExtCommPath,
       "fsbgpCaps": fsbgpCaps,
       "fsbgpCapScalars": fsbgpCapScalars,
       "fsbgp4CapabilitySupportAvailable": fsbgp4CapabilitySupportAvailable,
       "fsbgp4MaxCapsPerPeer": fsbgp4MaxCapsPerPeer,
       "fsbgp4MaxInstancesPerCap": fsbgp4MaxInstancesPerCap,
       "fsbgp4MaxCapDataSize": fsbgp4MaxCapDataSize,
       "fsbgp4CapSupportedCapsTable": fsbgp4CapSupportedCapsTable,
       "fsbgp4CapSupportedCapsEntry": fsbgp4CapSupportedCapsEntry,
       "fsbgp4CapPeerRemoteIpAddr": fsbgp4CapPeerRemoteIpAddr,
       "fsbgp4SupportedCapabilityCode": fsbgp4SupportedCapabilityCode,
       "fsbgp4SupportedCapabilityInstance": fsbgp4SupportedCapabilityInstance,
       "fsbgp4SupportedCapabilityLength": fsbgp4SupportedCapabilityLength,
       "fsbgp4SupportedCapabilityValue": fsbgp4SupportedCapabilityValue,
       "fsbgp4CapSupportedCapsRowStatus": fsbgp4CapSupportedCapsRowStatus,
       "fsbgp4StrictCapabilityMatchTable": fsbgp4StrictCapabilityMatchTable,
       "fsbgp4StrictCapabilityMatchEntry": fsbgp4StrictCapabilityMatchEntry,
       "fsbgp4PeerRemIpAddr": fsbgp4PeerRemIpAddr,
       "fsbgp4StrictCapabilityMatch": fsbgp4StrictCapabilityMatch,
       "fsbgp4CapsAnnouncedTable": fsbgp4CapsAnnouncedTable,
       "fsbgp4CapsAnnouncedEntry": fsbgp4CapsAnnouncedEntry,
       "fsbgp4PeerIpAddr": fsbgp4PeerIpAddr,
       "fsbgp4PeerCapAnnouncedCode": fsbgp4PeerCapAnnouncedCode,
       "fsbgp4PeerCapAnnouncedInstance": fsbgp4PeerCapAnnouncedInstance,
       "fsbgp4PeerCapAnnouncedLength": fsbgp4PeerCapAnnouncedLength,
       "fsbgp4PeerCapAnnouncedValue": fsbgp4PeerCapAnnouncedValue,
       "fsbgp4CapReceivedCapsTable": fsbgp4CapReceivedCapsTable,
       "fsbgp4CapReceivedCapsEntry": fsbgp4CapReceivedCapsEntry,
       "fsbgp4PeerRemoteAddress": fsbgp4PeerRemoteAddress,
       "fsbgp4PeerCapReceivedCode": fsbgp4PeerCapReceivedCode,
       "fsbgp4PeerCapReceivedInstance": fsbgp4PeerCapReceivedInstance,
       "fsbgp4PeerCapReceivedLength": fsbgp4PeerCapReceivedLength,
       "fsbgp4PeerCapReceivedValue": fsbgp4PeerCapReceivedValue,
       "fsbgp4CapAcceptedCapsTable": fsbgp4CapAcceptedCapsTable,
       "fsbgp4CapAcceptedCapsEntry": fsbgp4CapAcceptedCapsEntry,
       "fsbgp4CapAcceptedPeerRemAddr": fsbgp4CapAcceptedPeerRemAddr,
       "fsbgp4PeerCapAcceptedCode": fsbgp4PeerCapAcceptedCode,
       "fsbgp4PeerCapAcceptedInstance": fsbgp4PeerCapAcceptedInstance,
       "fsbgp4PeerCapAcceptedLength": fsbgp4PeerCapAcceptedLength,
       "fsbgp4PeerCapAcceptedValue": fsbgp4PeerCapAcceptedValue,
       "fsbgpAsc": fsbgpAsc,
       "fsbgpAscScalars": fsbgpAscScalars,
       "fsbgpAscConfedId": fsbgpAscConfedId,
       "fsbgpAscConfedBestPathCompareMED": fsbgpAscConfedBestPathCompareMED,
       "fsbgpAscConfedPeerTable": fsbgpAscConfedPeerTable,
       "fsbgpAscConfedPeerEntry": fsbgpAscConfedPeerEntry,
       "fsbgpAscConfedPeerASNo": fsbgpAscConfedPeerASNo,
       "fsbgpAscConfedPeerStatus": fsbgpAscConfedPeerStatus,
       "fsbgp4RtRefresh": fsbgp4RtRefresh,
       "fsbgp4RtRefreshAllPeerInboundRequest": fsbgp4RtRefreshAllPeerInboundRequest,
       "fsbgp4RtRefreshInboundTable": fsbgp4RtRefreshInboundTable,
       "fsbgp4RtRefreshInboundEntry": fsbgp4RtRefreshInboundEntry,
       "fsbgp4RtRefreshInboundPeerType": fsbgp4RtRefreshInboundPeerType,
       "fsbgp4RtRefreshInboundPeerAddr": fsbgp4RtRefreshInboundPeerAddr,
       "fsbgp4RtRefreshInboundRequest": fsbgp4RtRefreshInboundRequest,
       "fsbgp4RtRefreshStatisticsTable": fsbgp4RtRefreshStatisticsTable,
       "fsbgp4RtRefreshStatisticsEntry": fsbgp4RtRefreshStatisticsEntry,
       "fsbgp4RtRefreshStatisticsPeerType": fsbgp4RtRefreshStatisticsPeerType,
       "fsbgp4RtRefreshStatisticsPeerAddr": fsbgp4RtRefreshStatisticsPeerAddr,
       "fsbgp4RtRefreshStatisticsRtRefMsgSentCntr": fsbgp4RtRefreshStatisticsRtRefMsgSentCntr,
       "fsbgp4RtRefreshStatisticsRtRefMsgTxErrCntr": fsbgp4RtRefreshStatisticsRtRefMsgTxErrCntr,
       "fsbgp4RtRefreshStatisticsRtRefMsgRcvdCntr": fsbgp4RtRefreshStatisticsRtRefMsgRcvdCntr,
       "fsbgp4RtRefreshStatisticsRtRefMsgInvalidCntr": fsbgp4RtRefreshStatisticsRtRefMsgInvalidCntr,
       "fsbgp4TCPMD5Auth": fsbgp4TCPMD5Auth,
       "fsbgp4TCPMD5AuthTable": fsbgp4TCPMD5AuthTable,
       "fsbgp4TCPMD5AuthEntry": fsbgp4TCPMD5AuthEntry,
       "fsbgp4TCPMD5AuthPeerType": fsbgp4TCPMD5AuthPeerType,
       "fsbgp4TCPMD5AuthPeerAddr": fsbgp4TCPMD5AuthPeerAddr,
       "fsbgp4TCPMD5AuthPassword": fsbgp4TCPMD5AuthPassword,
       "fsbgp4TCPMD5AuthPwdSet": fsbgp4TCPMD5AuthPwdSet,
       "fsbgp4SoftReconfigOut": fsbgp4SoftReconfigOut,
       "fsbgp4SoftReconfigAllPeerOutboundRequest": fsbgp4SoftReconfigAllPeerOutboundRequest,
       "fsbgp4SoftReconfigOutboundTable": fsbgp4SoftReconfigOutboundTable,
       "fsbgp4SoftReconfigOutboundEntry": fsbgp4SoftReconfigOutboundEntry,
       "fsbgp4SoftReconfigOutboundPeerType": fsbgp4SoftReconfigOutboundPeerType,
       "fsbgp4SoftReconfigOutboundPeerAddr": fsbgp4SoftReconfigOutboundPeerAddr,
       "fsbgp4SoftReconfigOutboundRequest": fsbgp4SoftReconfigOutboundRequest,
       "fsbgp4MpeBgpPeerTable": fsbgp4MpeBgpPeerTable,
       "fsbgp4MpeBgpPeerEntry": fsbgp4MpeBgpPeerEntry,
       "fsbgp4mpebgpPeerRemoteAddrType": fsbgp4mpebgpPeerRemoteAddrType,
       "fsbgp4mpebgpPeerIdentifier": fsbgp4mpebgpPeerIdentifier,
       "fsbgp4mpebgpPeerState": fsbgp4mpebgpPeerState,
       "fsbgp4mpebgpPeerAdminStatus": fsbgp4mpebgpPeerAdminStatus,
       "fsbgp4mpebgpPeerNegotiatedVersion": fsbgp4mpebgpPeerNegotiatedVersion,
       "fsbgp4mpebgpPeerLocalAddr": fsbgp4mpebgpPeerLocalAddr,
       "fsbgp4mpebgpPeerLocalPort": fsbgp4mpebgpPeerLocalPort,
       "fsbgp4mpebgpPeerRemoteAddr": fsbgp4mpebgpPeerRemoteAddr,
       "fsbgp4mpebgpPeerRemotePort": fsbgp4mpebgpPeerRemotePort,
       "fsbgp4mpebgpPeerRemoteAs": fsbgp4mpebgpPeerRemoteAs,
       "fsbgp4mpebgpPeerInUpdates": fsbgp4mpebgpPeerInUpdates,
       "fsbgp4mpebgpPeerOutUpdates": fsbgp4mpebgpPeerOutUpdates,
       "fsbgp4mpebgpPeerInTotalMessages": fsbgp4mpebgpPeerInTotalMessages,
       "fsbgp4mpebgpPeerOutTotalMessages": fsbgp4mpebgpPeerOutTotalMessages,
       "fsbgp4mpebgpPeerLastError": fsbgp4mpebgpPeerLastError,
       "fsbgp4mpebgpPeerFsmEstablishedTransitions": fsbgp4mpebgpPeerFsmEstablishedTransitions,
       "fsbgp4mpebgpPeerFsmEstablishedTime": fsbgp4mpebgpPeerFsmEstablishedTime,
       "fsbgp4mpebgpPeerConnectRetryInterval": fsbgp4mpebgpPeerConnectRetryInterval,
       "fsbgp4mpebgpPeerHoldTime": fsbgp4mpebgpPeerHoldTime,
       "fsbgp4mpebgpPeerKeepAlive": fsbgp4mpebgpPeerKeepAlive,
       "fsbgp4mpebgpPeerHoldTimeConfigured": fsbgp4mpebgpPeerHoldTimeConfigured,
       "fsbgp4mpebgpPeerKeepAliveConfigured": fsbgp4mpebgpPeerKeepAliveConfigured,
       "fsbgp4mpebgpPeerMinASOriginationInterval": fsbgp4mpebgpPeerMinASOriginationInterval,
       "fsbgp4mpebgpPeerMinRouteAdvertisementInterval": fsbgp4mpebgpPeerMinRouteAdvertisementInterval,
       "fsbgp4mpebgpPeerInUpdateElapsedTime": fsbgp4mpebgpPeerInUpdateElapsedTime,
       "fsbgp4mpebgpPeerEndOfRIBMarkerSentStatus": fsbgp4mpebgpPeerEndOfRIBMarkerSentStatus,
       "fsbgp4mpebgpPeerEndOfRIBMarkerReceivedStatus": fsbgp4mpebgpPeerEndOfRIBMarkerReceivedStatus,
       "fsbgp4mpebgpPeerRestartMode": fsbgp4mpebgpPeerRestartMode,
       "fsbgp4mpePeerRestartTimeInterval": fsbgp4mpePeerRestartTimeInterval,
       "fsbgp4mpePeerAllowAutomaticStart": fsbgp4mpePeerAllowAutomaticStart,
       "fsbgp4mpePeerAllowAutomaticStop": fsbgp4mpePeerAllowAutomaticStop,
       "fsbgp4mpebgpPeerIdleHoldTimeConfigured": fsbgp4mpebgpPeerIdleHoldTimeConfigured,
       "fsbgp4mpeDampPeerOscillations": fsbgp4mpeDampPeerOscillations,
       "fsbgp4mpePeerDelayOpen": fsbgp4mpePeerDelayOpen,
       "fsbgp4mpebgpPeerDelayOpenTimeConfigured": fsbgp4mpebgpPeerDelayOpenTimeConfigured,
       "fsbgp4mpePeerPrefixUpperLimit": fsbgp4mpePeerPrefixUpperLimit,
       "fsbgp4mpePeerTcpConnectRetryCnt": fsbgp4mpePeerTcpConnectRetryCnt,
       "fsbgp4mpePeerTcpCurrentConnectRetryCnt": fsbgp4mpePeerTcpCurrentConnectRetryCnt,
       "fsbgp4mpeIsPeerDamped": fsbgp4mpeIsPeerDamped,
       "fsbgp4mpePeerSessionAuthStatus": fsbgp4mpePeerSessionAuthStatus,
       "fsbgp4mpePeerTCPAOKeyIdInUse": fsbgp4mpePeerTCPAOKeyIdInUse,
       "fsbgp4mpePeerTCPAOAuthNoMKTDiscard": fsbgp4mpePeerTCPAOAuthNoMKTDiscard,
       "fsbgp4mpePeerTCPAOAuthICMPAccept": fsbgp4mpePeerTCPAOAuthICMPAccept,
       "fsbgp4mpePeerIpPrefixNameIn": fsbgp4mpePeerIpPrefixNameIn,
       "fsbgp4mpePeerIpPrefixNameOut": fsbgp4mpePeerIpPrefixNameOut,
       "fsbgp4mpePeerBfdStatus": fsbgp4mpePeerBfdStatus,
       "fsbgp4mpebgpPeerHoldAdvtRoutes": fsbgp4mpebgpPeerHoldAdvtRoutes,
       "fsbgp4MpeBgp4PathAttrTable": fsbgp4MpeBgp4PathAttrTable,
       "fsbgp4MpeBgp4PathAttrEntry": fsbgp4MpeBgp4PathAttrEntry,
       "fsbgp4mpebgp4PathAttrRouteAfi": fsbgp4mpebgp4PathAttrRouteAfi,
       "fsbgp4mpebgp4PathAttrRouteSafi": fsbgp4mpebgp4PathAttrRouteSafi,
       "fsbgp4mpebgp4PathAttrPeerType": fsbgp4mpebgp4PathAttrPeerType,
       "fsbgp4mpebgp4PathAttrPeer": fsbgp4mpebgp4PathAttrPeer,
       "fsbgp4mpebgp4PathAttrIpAddrPrefixLen": fsbgp4mpebgp4PathAttrIpAddrPrefixLen,
       "fsbgp4mpebgp4PathAttrIpAddrPrefix": fsbgp4mpebgp4PathAttrIpAddrPrefix,
       "fsbgp4mpebgp4PathAttrOrigin": fsbgp4mpebgp4PathAttrOrigin,
       "fsbgp4mpebgp4PathAttrASPathSegment": fsbgp4mpebgp4PathAttrASPathSegment,
       "fsbgp4mpebgp4PathAttrNextHop": fsbgp4mpebgp4PathAttrNextHop,
       "fsbgp4mpebgp4PathAttrMultiExitDisc": fsbgp4mpebgp4PathAttrMultiExitDisc,
       "fsbgp4mpebgp4PathAttrLocalPref": fsbgp4mpebgp4PathAttrLocalPref,
       "fsbgp4mpebgp4PathAttrAtomicAggregate": fsbgp4mpebgp4PathAttrAtomicAggregate,
       "fsbgp4mpebgp4PathAttrAggregatorAS": fsbgp4mpebgp4PathAttrAggregatorAS,
       "fsbgp4mpebgp4PathAttrAggregatorAddr": fsbgp4mpebgp4PathAttrAggregatorAddr,
       "fsbgp4mpebgp4PathAttrCalcLocalPref": fsbgp4mpebgp4PathAttrCalcLocalPref,
       "fsbgp4mpebgp4PathAttrBest": fsbgp4mpebgp4PathAttrBest,
       "fsbgp4mpebgp4PathAttrCommunity": fsbgp4mpebgp4PathAttrCommunity,
       "fsbgp4mpebgp4PathAttrOriginatorId": fsbgp4mpebgp4PathAttrOriginatorId,
       "fsbgp4mpebgp4PathAttrClusterList": fsbgp4mpebgp4PathAttrClusterList,
       "fsbgp4mpebgp4PathAttrExtCommunity": fsbgp4mpebgp4PathAttrExtCommunity,
       "fsbgp4mpebgp4PathAttrUnknown": fsbgp4mpebgp4PathAttrUnknown,
       "fsbgp4mpebgp4PathAttrLabel": fsbgp4mpebgp4PathAttrLabel,
       "fsbgp4mpebgp4PathAttrAS4PathSegment": fsbgp4mpebgp4PathAttrAS4PathSegment,
       "fsbgp4mpebgp4PathAttrAggregatorAS4": fsbgp4mpebgp4PathAttrAggregatorAS4,
       "fsbgp4MpePeerExtTable": fsbgp4MpePeerExtTable,
       "fsbgp4MpePeerExtEntry": fsbgp4MpePeerExtEntry,
       "fsbgp4mpePeerExtPeerType": fsbgp4mpePeerExtPeerType,
       "fsbgp4mpePeerExtPeerRemoteAddr": fsbgp4mpePeerExtPeerRemoteAddr,
       "fsbgp4mpePeerExtConfigurePeer": fsbgp4mpePeerExtConfigurePeer,
       "fsbgp4mpePeerExtPeerRemoteAs": fsbgp4mpePeerExtPeerRemoteAs,
       "fsbgp4mpePeerExtEBGPMultiHop": fsbgp4mpePeerExtEBGPMultiHop,
       "fsbgp4mpePeerExtEBGPHopLimit": fsbgp4mpePeerExtEBGPHopLimit,
       "fsbgp4mpePeerExtNextHopSelf": fsbgp4mpePeerExtNextHopSelf,
       "fsbgp4mpePeerExtRflClient": fsbgp4mpePeerExtRflClient,
       "fsbgp4mpePeerExtTcpSendBufSize": fsbgp4mpePeerExtTcpSendBufSize,
       "fsbgp4mpePeerExtTcpRcvBufSize": fsbgp4mpePeerExtTcpRcvBufSize,
       "fsbgp4mpePeerExtLclAddress": fsbgp4mpePeerExtLclAddress,
       "fsbgp4mpePeerExtNetworkAddress": fsbgp4mpePeerExtNetworkAddress,
       "fsbgp4mpePeerExtGateway": fsbgp4mpePeerExtGateway,
       "fsbgp4mpePeerExtCommSendStatus": fsbgp4mpePeerExtCommSendStatus,
       "fsbgp4mpePeerExtECommSendStatus": fsbgp4mpePeerExtECommSendStatus,
       "fsbgp4mpePeerExtPassive": fsbgp4mpePeerExtPassive,
       "fsbgp4mpePeerExtDefaultOriginate": fsbgp4mpePeerExtDefaultOriginate,
       "fsbgp4mpePeerExtActivateMPCapability": fsbgp4mpePeerExtActivateMPCapability,
       "fsbgp4mpePeerExtDeactivateMPCapability": fsbgp4mpePeerExtDeactivateMPCapability,
       "fsbgp4mpePeerExtMplsVpnVrfAssociated": fsbgp4mpePeerExtMplsVpnVrfAssociated,
       "fsbgp4mpePeerExtMplsVpnCERouteTargetAdvt": fsbgp4mpePeerExtMplsVpnCERouteTargetAdvt,
       "fsbgp4mpePeerExtMplsVpnCESiteOfOrigin": fsbgp4mpePeerExtMplsVpnCESiteOfOrigin,
       "fsbgp4mpePeerExtOverrideCapability": fsbgp4mpePeerExtOverrideCapability,
       "fsbgp4MpeMEDTable": fsbgp4MpeMEDTable,
       "fsbgp4MpeMEDEntry": fsbgp4MpeMEDEntry,
       "fsbgp4mpeMEDIndex": fsbgp4mpeMEDIndex,
       "fsbgp4mpeMEDAdminStatus": fsbgp4mpeMEDAdminStatus,
       "fsbgp4mpeMEDRemoteAS": fsbgp4mpeMEDRemoteAS,
       "fsbgp4mpeMEDIPAddrAfi": fsbgp4mpeMEDIPAddrAfi,
       "fsbgp4mpeMEDIPAddrSafi": fsbgp4mpeMEDIPAddrSafi,
       "fsbgp4mpeMEDIPAddrPrefix": fsbgp4mpeMEDIPAddrPrefix,
       "fsbgp4mpeMEDIPAddrPrefixLen": fsbgp4mpeMEDIPAddrPrefixLen,
       "fsbgp4mpeMEDIntermediateAS": fsbgp4mpeMEDIntermediateAS,
       "fsbgp4mpeMEDDirection": fsbgp4mpeMEDDirection,
       "fsbgp4mpeMEDValue": fsbgp4mpeMEDValue,
       "fsbgp4mpeMEDPreference": fsbgp4mpeMEDPreference,
       "fsbgp4mpeMEDVrfName": fsbgp4mpeMEDVrfName,
       "fsbgp4MpeLocalPrefTable": fsbgp4MpeLocalPrefTable,
       "fsbgp4MpeLocalPrefEntry": fsbgp4MpeLocalPrefEntry,
       "fsbgp4mpeLocalPrefIndex": fsbgp4mpeLocalPrefIndex,
       "fsbgp4mpeLocalPrefAdminStatus": fsbgp4mpeLocalPrefAdminStatus,
       "fsbgp4mpeLocalPrefRemoteAS": fsbgp4mpeLocalPrefRemoteAS,
       "fsbgp4mpeLocalPrefIPAddrAfi": fsbgp4mpeLocalPrefIPAddrAfi,
       "fsbgp4mpeLocalPrefIPAddrSafi": fsbgp4mpeLocalPrefIPAddrSafi,
       "fsbgp4mpeLocalPrefIPAddrPrefix": fsbgp4mpeLocalPrefIPAddrPrefix,
       "fsbgp4mpeLocalPrefIPAddrPrefixLen": fsbgp4mpeLocalPrefIPAddrPrefixLen,
       "fsbgp4mpeLocalPrefIntermediateAS": fsbgp4mpeLocalPrefIntermediateAS,
       "fsbgp4mpeLocalPrefDirection": fsbgp4mpeLocalPrefDirection,
       "fsbgp4mpeLocalPrefValue": fsbgp4mpeLocalPrefValue,
       "fsbgp4mpeLocalPrefPreference": fsbgp4mpeLocalPrefPreference,
       "fsbgp4mpeLocalPrefVrfName": fsbgp4mpeLocalPrefVrfName,
       "fsbgp4MpeUpdateFilterTable": fsbgp4MpeUpdateFilterTable,
       "fsbgp4MpeUpdateFilterEntry": fsbgp4MpeUpdateFilterEntry,
       "fsbgp4mpeUpdateFilterIndex": fsbgp4mpeUpdateFilterIndex,
       "fsbgp4mpeUpdateFilterAdminStatus": fsbgp4mpeUpdateFilterAdminStatus,
       "fsbgp4mpeUpdateFilterRemoteAS": fsbgp4mpeUpdateFilterRemoteAS,
       "fsbgp4mpeUpdateFilterIPAddrAfi": fsbgp4mpeUpdateFilterIPAddrAfi,
       "fsbgp4mpeUpdateFilterIPAddrSafi": fsbgp4mpeUpdateFilterIPAddrSafi,
       "fsbgp4mpeUpdateFilterIPAddrPrefix": fsbgp4mpeUpdateFilterIPAddrPrefix,
       "fsbgp4mpeUpdateFilterIPAddrPrefixLen": fsbgp4mpeUpdateFilterIPAddrPrefixLen,
       "fsbgp4mpeUpdateFilterIntermediateAS": fsbgp4mpeUpdateFilterIntermediateAS,
       "fsbgp4mpeUpdateFilterDirection": fsbgp4mpeUpdateFilterDirection,
       "fsbgp4mpeUpdateFilterAction": fsbgp4mpeUpdateFilterAction,
       "fsbgp4mpeUpdateFilterVrfName": fsbgp4mpeUpdateFilterVrfName,
       "fsbgp4MpeAggregateTable": fsbgp4MpeAggregateTable,
       "fsbgp4MpeAggregateEntry": fsbgp4MpeAggregateEntry,
       "fsbgp4mpeAggregateIndex": fsbgp4mpeAggregateIndex,
       "fsbgp4mpeAggregateAdminStatus": fsbgp4mpeAggregateAdminStatus,
       "fsbgp4mpeAggregateIPAddrAfi": fsbgp4mpeAggregateIPAddrAfi,
       "fsbgp4mpeAggregateIPAddrSafi": fsbgp4mpeAggregateIPAddrSafi,
       "fsbgp4mpeAggregateIPAddrPrefix": fsbgp4mpeAggregateIPAddrPrefix,
       "fsbgp4mpeAggregateIPAddrPrefixLen": fsbgp4mpeAggregateIPAddrPrefixLen,
       "fsbgp4mpeAggregateAdvertise": fsbgp4mpeAggregateAdvertise,
       "fsbgp4mpeAggregateVrfName": fsbgp4mpeAggregateVrfName,
       "fsbgp4mpeAggregateAsSet": fsbgp4mpeAggregateAsSet,
       "fsbgp4mpeAggregateAdvertiseRouteMapName": fsbgp4mpeAggregateAdvertiseRouteMapName,
       "fsbgp4mpeAggregateSuppressRouteMapName": fsbgp4mpeAggregateSuppressRouteMapName,
       "fsbgp4mpeAggregateAttributeRouteMapName": fsbgp4mpeAggregateAttributeRouteMapName,
       "fsbgp4MpeImportRouteTable": fsbgp4MpeImportRouteTable,
       "fsbgp4MpeImportRouteEntry": fsbgp4MpeImportRouteEntry,
       "fsbgp4mpeImportRoutePrefixAfi": fsbgp4mpeImportRoutePrefixAfi,
       "fsbgp4mpeImportRoutePrefixSafi": fsbgp4mpeImportRoutePrefixSafi,
       "fsbgp4mpeImportRoutePrefix": fsbgp4mpeImportRoutePrefix,
       "fsbgp4mpeImportRoutePrefixLen": fsbgp4mpeImportRoutePrefixLen,
       "fsbgp4mpeImportRouteProtocol": fsbgp4mpeImportRouteProtocol,
       "fsbgp4mpeImportRouteNextHop": fsbgp4mpeImportRouteNextHop,
       "fsbgp4mpeImportRouteIfIndex": fsbgp4mpeImportRouteIfIndex,
       "fsbgp4mpeImportRouteMetric": fsbgp4mpeImportRouteMetric,
       "fsbgp4mpeImportRouteVrf": fsbgp4mpeImportRouteVrf,
       "fsbgp4mpeImportRouteAction": fsbgp4mpeImportRouteAction,
       "fsbgp4MpeFsmTransitionHistTable": fsbgp4MpeFsmTransitionHistTable,
       "fsbgp4MpeFsmTransitionHistEntry": fsbgp4MpeFsmTransitionHistEntry,
       "fsbgp4mpePeerType": fsbgp4mpePeerType,
       "fsbgp4mpePeer": fsbgp4mpePeer,
       "fsbgp4mpeFsmTransitionHist": fsbgp4mpeFsmTransitionHist,
       "fsbgp4MpeRfd": fsbgp4MpeRfd,
       "fsbgp4MpeRfdRtDampHistTable": fsbgp4MpeRfdRtDampHistTable,
       "fsbgp4MpeRfdRtDampHistEntry": fsbgp4MpeRfdRtDampHistEntry,
       "fsbgp4mpePathAttrAddrPrefixAfi": fsbgp4mpePathAttrAddrPrefixAfi,
       "fsbgp4mpePathAttrAddrPrefixSafi": fsbgp4mpePathAttrAddrPrefixSafi,
       "fsbgp4mpePathAttrAddrPrefix": fsbgp4mpePathAttrAddrPrefix,
       "fsbgp4mpePathAttrAddrPrefixLen": fsbgp4mpePathAttrAddrPrefixLen,
       "fsbgp4mpePathAttrPeerType": fsbgp4mpePathAttrPeerType,
       "fsbgp4mpePathAttrPeer": fsbgp4mpePathAttrPeer,
       "fsbgp4mpeRfdRtFom": fsbgp4mpeRfdRtFom,
       "fsbgp4mpeRfdRtLastUpdtTime": fsbgp4mpeRfdRtLastUpdtTime,
       "fsbgp4mpeRfdRtState": fsbgp4mpeRfdRtState,
       "fsbgp4mpeRfdRtStatus": fsbgp4mpeRfdRtStatus,
       "fsbgp4mpeRfdRtFlapCount": fsbgp4mpeRfdRtFlapCount,
       "fsbgp4mpeRfdRtFlapTime": fsbgp4mpeRfdRtFlapTime,
       "fsbgp4mpeRfdRtReuseTime": fsbgp4mpeRfdRtReuseTime,
       "fsbgp4MpeRfdPeerDampHistTable": fsbgp4MpeRfdPeerDampHistTable,
       "fsbgp4MpeRfdPeerDampHistEntry": fsbgp4MpeRfdPeerDampHistEntry,
       "fsbgp4mpePeerRemoteIpAddrType": fsbgp4mpePeerRemoteIpAddrType,
       "fsbgp4mpePeerRemoteIpAddr": fsbgp4mpePeerRemoteIpAddr,
       "fsbgp4mpeRfdPeerFom": fsbgp4mpeRfdPeerFom,
       "fsbgp4mpeRfdPeerLastUpdtTime": fsbgp4mpeRfdPeerLastUpdtTime,
       "fsbgp4mpeRfdPeerState": fsbgp4mpeRfdPeerState,
       "fsbgp4mpeRfdPeerStatus": fsbgp4mpeRfdPeerStatus,
       "fsbgp4MpeRfdRtsReuseListTable": fsbgp4MpeRfdRtsReuseListTable,
       "fsbgp4MpeRfdRtsReuseListEntry": fsbgp4MpeRfdRtsReuseListEntry,
       "fsbgp4mpeRtAfi": fsbgp4mpeRtAfi,
       "fsbgp4mpeRtSafi": fsbgp4mpeRtSafi,
       "fsbgp4mpeRtIPPrefix": fsbgp4mpeRtIPPrefix,
       "fsbgp4mpeRtIPPrefixLen": fsbgp4mpeRtIPPrefixLen,
       "fsbgp4mpeRfdRtsReusePeerType": fsbgp4mpeRfdRtsReusePeerType,
       "fsbgp4mpePeerRemAddress": fsbgp4mpePeerRemAddress,
       "fsbgp4mpeRfdRtReuseListRtFom": fsbgp4mpeRfdRtReuseListRtFom,
       "fsbgp4mpeRfdRtReuseListRtLastUpdtTime": fsbgp4mpeRfdRtReuseListRtLastUpdtTime,
       "fsbgp4mpeRfdRtReuseListRtState": fsbgp4mpeRfdRtReuseListRtState,
       "fsbgp4mpeRfdRtReuseListRtStatus": fsbgp4mpeRfdRtReuseListRtStatus,
       "fsbgp4MpeRfdPeerReuseListTable": fsbgp4MpeRfdPeerReuseListTable,
       "fsbgp4MpeRfdPeerReuseListEntry": fsbgp4MpeRfdPeerReuseListEntry,
       "fsbgp4mpeRfdPeerRemIpAddrType": fsbgp4mpeRfdPeerRemIpAddrType,
       "fsbgp4mpeRfdPeerRemIpAddr": fsbgp4mpeRfdPeerRemIpAddr,
       "fsbgp4mpeRfdPeerReuseListPeerFom": fsbgp4mpeRfdPeerReuseListPeerFom,
       "fsbgp4mpeRfdPeerReuseListLastUpdtTime": fsbgp4mpeRfdPeerReuseListLastUpdtTime,
       "fsbgp4mpeRfdPeerReuseListPeerState": fsbgp4mpeRfdPeerReuseListPeerState,
       "fsbgp4mpeRfdPeerReuseListPeerStatus": fsbgp4mpeRfdPeerReuseListPeerStatus,
       "fsbgpMpeComm": fsbgpMpeComm,
       "fsbgp4MpeCommRouteAddCommTable": fsbgp4MpeCommRouteAddCommTable,
       "fsbgp4MpeCommRouteAddCommEntry": fsbgp4MpeCommRouteAddCommEntry,
       "fsbgp4mpeAddCommRtAfi": fsbgp4mpeAddCommRtAfi,
       "fsbgp4mpeAddCommRtSafi": fsbgp4mpeAddCommRtSafi,
       "fsbgp4mpeAddCommIpNetwork": fsbgp4mpeAddCommIpNetwork,
       "fsbgp4mpeAddCommIpPrefixLen": fsbgp4mpeAddCommIpPrefixLen,
       "fsbgp4mpeAddCommVal": fsbgp4mpeAddCommVal,
       "fsbgp4mpeAddCommRowStatus": fsbgp4mpeAddCommRowStatus,
       "fsbgp4MpeCommRouteDeleteCommTable": fsbgp4MpeCommRouteDeleteCommTable,
       "fsbgp4MpeCommRouteDeleteCommEntry": fsbgp4MpeCommRouteDeleteCommEntry,
       "fsbgp4mpeDeleteCommRtAfi": fsbgp4mpeDeleteCommRtAfi,
       "fsbgp4mpeDeleteCommRtSafi": fsbgp4mpeDeleteCommRtSafi,
       "fsbgp4mpeDeleteCommIpNetwork": fsbgp4mpeDeleteCommIpNetwork,
       "fsbgp4mpeDeleteCommIpPrefixLen": fsbgp4mpeDeleteCommIpPrefixLen,
       "fsbgp4mpeDeleteCommVal": fsbgp4mpeDeleteCommVal,
       "fsbgp4mpeDeleteCommRowStatus": fsbgp4mpeDeleteCommRowStatus,
       "fsbgp4MpeCommRouteCommSetStatusTable": fsbgp4MpeCommRouteCommSetStatusTable,
       "fsbgp4MpeCommRouteCommSetStatusEntry": fsbgp4MpeCommRouteCommSetStatusEntry,
       "fsbgp4mpeCommSetStatusAfi": fsbgp4mpeCommSetStatusAfi,
       "fsbgp4mpeCommSetStatusSafi": fsbgp4mpeCommSetStatusSafi,
       "fsbgp4mpeCommSetStatusIpNetwork": fsbgp4mpeCommSetStatusIpNetwork,
       "fsbgp4mpeCommSetStatusIpPrefixLen": fsbgp4mpeCommSetStatusIpPrefixLen,
       "fsbgp4mpeCommSetStatus": fsbgp4mpeCommSetStatus,
       "fsbgp4mpeCommSetStatusRowStatus": fsbgp4mpeCommSetStatusRowStatus,
       "fsbgpMpeExtComm": fsbgpMpeExtComm,
       "fsbgp4MpeExtCommRouteAddExtCommTable": fsbgp4MpeExtCommRouteAddExtCommTable,
       "fsbgp4MpeExtCommRouteAddExtCommEntry": fsbgp4MpeExtCommRouteAddExtCommEntry,
       "fsbgp4mpeAddExtCommRtAfi": fsbgp4mpeAddExtCommRtAfi,
       "fsbgp4mpeAddExtCommRtSafi": fsbgp4mpeAddExtCommRtSafi,
       "fsbgp4mpeAddExtCommIpNetwork": fsbgp4mpeAddExtCommIpNetwork,
       "fsbgp4mpeAddExtCommIpPrefixLen": fsbgp4mpeAddExtCommIpPrefixLen,
       "fsbgp4mpeAddExtCommVal": fsbgp4mpeAddExtCommVal,
       "fsbgp4mpeAddExtCommRowStatus": fsbgp4mpeAddExtCommRowStatus,
       "fsbgp4MpeExtCommRouteDeleteExtCommTable": fsbgp4MpeExtCommRouteDeleteExtCommTable,
       "fsbgp4MpeExtCommRouteDeleteExtCommEntry": fsbgp4MpeExtCommRouteDeleteExtCommEntry,
       "fsbgp4mpeDeleteExtCommRtAfi": fsbgp4mpeDeleteExtCommRtAfi,
       "fsbgp4mpeDeleteExtCommRtSafi": fsbgp4mpeDeleteExtCommRtSafi,
       "fsbgp4mpeDeleteExtCommIpNetwork": fsbgp4mpeDeleteExtCommIpNetwork,
       "fsbgp4mpeDeleteExtCommIpPrefixLen": fsbgp4mpeDeleteExtCommIpPrefixLen,
       "fsbgp4mpeDeleteExtCommVal": fsbgp4mpeDeleteExtCommVal,
       "fsbgp4mpeDeleteExtCommRowStatus": fsbgp4mpeDeleteExtCommRowStatus,
       "fsbgp4MpeExtCommRouteExtCommSetStatusTable": fsbgp4MpeExtCommRouteExtCommSetStatusTable,
       "fsbgp4MpeExtCommRouteExtCommSetStatusEntry": fsbgp4MpeExtCommRouteExtCommSetStatusEntry,
       "fsbgp4mpeExtCommSetStatusRtAfi": fsbgp4mpeExtCommSetStatusRtAfi,
       "fsbgp4mpeExtCommSetStatusRtSafi": fsbgp4mpeExtCommSetStatusRtSafi,
       "fsbgp4mpeExtCommSetStatusIpNetwork": fsbgp4mpeExtCommSetStatusIpNetwork,
       "fsbgp4mpeExtCommSetStatusIpPrefixLen": fsbgp4mpeExtCommSetStatusIpPrefixLen,
       "fsbgp4mpeExtCommSetStatus": fsbgp4mpeExtCommSetStatus,
       "fsbgp4mpeExtCommSetStatusRowStatus": fsbgp4mpeExtCommSetStatusRowStatus,
       "fsbgp4MpePeerLinkBwTable": fsbgp4MpePeerLinkBwTable,
       "fsbgp4MpePeerLinkBwEntry": fsbgp4MpePeerLinkBwEntry,
       "fsbgp4mpePeerLinkType": fsbgp4mpePeerLinkType,
       "fsbgp4mpePeerLinkRemAddr": fsbgp4mpePeerLinkRemAddr,
       "fsbgp4mpeLinkBandWidth": fsbgp4mpeLinkBandWidth,
       "fsbgp4mpePeerLinkBwRowStatus": fsbgp4mpePeerLinkBwRowStatus,
       "fsbgpMpeCaps": fsbgpMpeCaps,
       "fsbgp4MpeCapSupportedCapsTable": fsbgp4MpeCapSupportedCapsTable,
       "fsbgp4MpeCapSupportedCapsEntry": fsbgp4MpeCapSupportedCapsEntry,
       "fsbgp4mpeCapPeerType": fsbgp4mpeCapPeerType,
       "fsbgp4mpeCapPeerRemoteIpAddr": fsbgp4mpeCapPeerRemoteIpAddr,
       "fsbgp4mpeSupportedCapabilityCode": fsbgp4mpeSupportedCapabilityCode,
       "fsbgp4mpeSupportedCapabilityLength": fsbgp4mpeSupportedCapabilityLength,
       "fsbgp4mpeSupportedCapabilityValue": fsbgp4mpeSupportedCapabilityValue,
       "fsbgp4mpeCapSupportedCapsRowStatus": fsbgp4mpeCapSupportedCapsRowStatus,
       "fsbgp4mpeCapAnnouncedStatus": fsbgp4mpeCapAnnouncedStatus,
       "fsbgp4mpeCapReceivedStatus": fsbgp4mpeCapReceivedStatus,
       "fsbgp4mpeCapNegotiatedStatus": fsbgp4mpeCapNegotiatedStatus,
       "fsbgp4mpeCapConfiguredStatus": fsbgp4mpeCapConfiguredStatus,
       "fsbgp4MpeRtRefresh": fsbgp4MpeRtRefresh,
       "fsbgp4MpeRtRefreshInboundTable": fsbgp4MpeRtRefreshInboundTable,
       "fsbgp4MpeRtRefreshInboundEntry": fsbgp4MpeRtRefreshInboundEntry,
       "fsbgp4mpeRtRefreshInboundPeerType": fsbgp4mpeRtRefreshInboundPeerType,
       "fsbgp4mpeRtRefreshInboundPeerAddr": fsbgp4mpeRtRefreshInboundPeerAddr,
       "fsbgp4mpeRtRefreshInboundAfi": fsbgp4mpeRtRefreshInboundAfi,
       "fsbgp4mpeRtRefreshInboundSafi": fsbgp4mpeRtRefreshInboundSafi,
       "fsbgp4mpeRtRefreshInboundRequest": fsbgp4mpeRtRefreshInboundRequest,
       "fsbgp4mpeRtRefreshInboundPrefixFilter": fsbgp4mpeRtRefreshInboundPrefixFilter,
       "fsbgp4MpeRtRefreshStatisticsTable": fsbgp4MpeRtRefreshStatisticsTable,
       "fsbgp4MpeRtRefreshStatisticsEntry": fsbgp4MpeRtRefreshStatisticsEntry,
       "fsbgp4mpeRtRefreshStatisticsPeerType": fsbgp4mpeRtRefreshStatisticsPeerType,
       "fsbgp4mpeRtRefreshStatisticsPeerAddr": fsbgp4mpeRtRefreshStatisticsPeerAddr,
       "fsbgp4mpeRtRefreshStatisticsAfi": fsbgp4mpeRtRefreshStatisticsAfi,
       "fsbgp4mpeRtRefreshStatisticsSafi": fsbgp4mpeRtRefreshStatisticsSafi,
       "fsbgp4mpeRtRefreshStatisticsRtRefMsgSentCntr": fsbgp4mpeRtRefreshStatisticsRtRefMsgSentCntr,
       "fsbgp4mpeRtRefreshStatisticsRtRefMsgTxErrCntr": fsbgp4mpeRtRefreshStatisticsRtRefMsgTxErrCntr,
       "fsbgp4mpeRtRefreshStatisticsRtRefMsgRcvdCntr": fsbgp4mpeRtRefreshStatisticsRtRefMsgRcvdCntr,
       "fsbgp4mpeRtRefreshStatisticsRtRefMsgInvalidCntr": fsbgp4mpeRtRefreshStatisticsRtRefMsgInvalidCntr,
       "fsbgp4MpeSoftReconfigOut": fsbgp4MpeSoftReconfigOut,
       "fsbgp4MpeSoftReconfigOutboundTable": fsbgp4MpeSoftReconfigOutboundTable,
       "fsbgp4MpeSoftReconfigOutboundEntry": fsbgp4MpeSoftReconfigOutboundEntry,
       "fsbgp4mpeSoftReconfigOutboundPeerType": fsbgp4mpeSoftReconfigOutboundPeerType,
       "fsbgp4mpeSoftReconfigOutboundPeerAddr": fsbgp4mpeSoftReconfigOutboundPeerAddr,
       "fsbgp4mpeSoftReconfigOutboundAfi": fsbgp4mpeSoftReconfigOutboundAfi,
       "fsbgp4mpeSoftReconfigOutboundSafi": fsbgp4mpeSoftReconfigOutboundSafi,
       "fsbgp4mpeSoftReconfigOutboundRequest": fsbgp4mpeSoftReconfigOutboundRequest,
       "fsbgp4MpePrefixCountersTable": fsbgp4MpePrefixCountersTable,
       "fsbgp4MpePrefixCountersEntry": fsbgp4MpePrefixCountersEntry,
       "fsbgp4MpePeerRemoteAddrType": fsbgp4MpePeerRemoteAddrType,
       "fsbgp4MpePeerRemoteAddr": fsbgp4MpePeerRemoteAddr,
       "fsbgp4MpePrefixCountersAfi": fsbgp4MpePrefixCountersAfi,
       "fsbgp4MpePrefixCountersSafi": fsbgp4MpePrefixCountersSafi,
       "fsbgp4MpePrefixCountersPrefixesReceived": fsbgp4MpePrefixCountersPrefixesReceived,
       "fsbgp4MpePrefixCountersPrefixesSent": fsbgp4MpePrefixCountersPrefixesSent,
       "fsbgp4MpePrefixCountersWithdrawsReceived": fsbgp4MpePrefixCountersWithdrawsReceived,
       "fsbgp4MpePrefixCountersWithdrawsSent": fsbgp4MpePrefixCountersWithdrawsSent,
       "fsbgp4MpePrefixCountersInPrefixes": fsbgp4MpePrefixCountersInPrefixes,
       "fsbgp4MpePrefixCountersInPrefixesAccepted": fsbgp4MpePrefixCountersInPrefixesAccepted,
       "fsbgp4MpePrefixCountersInPrefixesRejected": fsbgp4MpePrefixCountersInPrefixesRejected,
       "fsbgp4MpePrefixCountersOutPrefixes": fsbgp4MpePrefixCountersOutPrefixes,
       "fsbgp4MplsVpn": fsbgp4MplsVpn,
       "fsbgp4MplsVpnVrfRouteTargetTable": fsbgp4MplsVpnVrfRouteTargetTable,
       "fsbgp4MplsVpnVrfRouteTargetEntry": fsbgp4MplsVpnVrfRouteTargetEntry,
       "fsbgp4MplsVpnVrfName": fsbgp4MplsVpnVrfName,
       "fsbgp4MplsVpnVrfRouteTargetType": fsbgp4MplsVpnVrfRouteTargetType,
       "fsbgp4MplsVpnVrfRouteTarget": fsbgp4MplsVpnVrfRouteTarget,
       "fsbgp4MplsVpnVrfRouteTargetRowStatus": fsbgp4MplsVpnVrfRouteTargetRowStatus,
       "fsbgp4MplsVpnVrfRedistributeTable": fsbgp4MplsVpnVrfRedistributeTable,
       "fsbgp4MplsVpnVrfRedistributeEntry": fsbgp4MplsVpnVrfRedistributeEntry,
       "fsbgp4MplsVpnVrfRedisAfi": fsbgp4MplsVpnVrfRedisAfi,
       "fsbgp4MplsVpnVrfRedisSafi": fsbgp4MplsVpnVrfRedisSafi,
       "fsbgp4MplsVpnVrfRedisProtoMask": fsbgp4MplsVpnVrfRedisProtoMask,
       "fsbgp4MplsVpnRRRouteTargetTable": fsbgp4MplsVpnRRRouteTargetTable,
       "fsbgp4MplsVpnRRRouteTargetEntry": fsbgp4MplsVpnRRRouteTargetEntry,
       "fsbgp4MplsVpnRRRouteTarget": fsbgp4MplsVpnRRRouteTarget,
       "fsbgp4MplsVpnRRRouteTargetRtCnt": fsbgp4MplsVpnRRRouteTargetRtCnt,
       "fsbgp4MplsVpnRRRouteTargetTimeStamp": fsbgp4MplsVpnRRRouteTargetTimeStamp,
       "fsbgp4DistInOutRouteMap": fsbgp4DistInOutRouteMap,
       "fsBgp4DistInOutRouteMapTable": fsBgp4DistInOutRouteMapTable,
       "fsBgp4DistInOutRouteMapEntry": fsBgp4DistInOutRouteMapEntry,
       "fsBgp4DistInOutRouteMapName": fsBgp4DistInOutRouteMapName,
       "fsBgp4DistInOutRouteMapType": fsBgp4DistInOutRouteMapType,
       "fsBgp4DistInOutRouteMapValue": fsBgp4DistInOutRouteMapValue,
       "fsBgp4DistInOutRouteMapRowStatus": fsBgp4DistInOutRouteMapRowStatus,
       "fsbgp4PreferenceGroup": fsbgp4PreferenceGroup,
       "fsBgp4PreferenceValue": fsBgp4PreferenceValue,
       "fsbgp4Notification": fsbgp4Notification,
       "fsbgp4Trap": fsbgp4Trap,
       "fsbgp4RestartStatusChange": fsbgp4RestartStatusChange,
       "fsbgp4NeighborRouteMap": fsbgp4NeighborRouteMap,
       "fsBgp4NeighborRouteMapTable": fsBgp4NeighborRouteMapTable,
       "fsBgp4NeighborRouteMapEntry": fsBgp4NeighborRouteMapEntry,
       "fsBgp4NeighborRouteMapPeerAddrType": fsBgp4NeighborRouteMapPeerAddrType,
       "fsBgp4NeighborRouteMapPeer": fsBgp4NeighborRouteMapPeer,
       "fsBgp4NeighborRouteMapDirection": fsBgp4NeighborRouteMapDirection,
       "fsBgp4NeighborRouteMapName": fsBgp4NeighborRouteMapName,
       "fsBgp4NeighborRouteMapRowStatus": fsBgp4NeighborRouteMapRowStatus,
       "fsBgp4PeerGroupTable": fsBgp4PeerGroupTable,
       "fsBgp4PeerGroupEntry": fsBgp4PeerGroupEntry,
       "fsBgp4PeerGroupName": fsBgp4PeerGroupName,
       "fsBgp4PeerGroupAddrType": fsBgp4PeerGroupAddrType,
       "fsBgp4PeerGroupRemoteAs": fsBgp4PeerGroupRemoteAs,
       "fsBgp4PeerGroupHoldTimeConfigured": fsBgp4PeerGroupHoldTimeConfigured,
       "fsBgp4PeerGroupKeepAliveConfigured": fsBgp4PeerGroupKeepAliveConfigured,
       "fsBgp4PeerGroupConnectRetryInterval": fsBgp4PeerGroupConnectRetryInterval,
       "fsBgp4PeerGroupMinASOriginInterval": fsBgp4PeerGroupMinASOriginInterval,
       "fsBgp4PeerGroupMinRouteAdvInterval": fsBgp4PeerGroupMinRouteAdvInterval,
       "fsBgp4PeerGroupAllowAutomaticStart": fsBgp4PeerGroupAllowAutomaticStart,
       "fsBgp4PeerGroupAllowAutomaticStop": fsBgp4PeerGroupAllowAutomaticStop,
       "fsBgp4PeerGroupIdleHoldTimeConfigured": fsBgp4PeerGroupIdleHoldTimeConfigured,
       "fsBgp4PeerGroupDampPeerOscillations": fsBgp4PeerGroupDampPeerOscillations,
       "fsBgp4PeerGroupDelayOpen": fsBgp4PeerGroupDelayOpen,
       "fsBgp4PeerGroupDelayOpenTimeConfigured": fsBgp4PeerGroupDelayOpenTimeConfigured,
       "fsBgp4PeerGroupPrefixUpperLimit": fsBgp4PeerGroupPrefixUpperLimit,
       "fsBgp4PeerGroupTcpConnectRetryCnt": fsBgp4PeerGroupTcpConnectRetryCnt,
       "fsBgp4PeerGroupEBGPMultiHop": fsBgp4PeerGroupEBGPMultiHop,
       "fsBgp4PeerGroupEBGPHopLimit": fsBgp4PeerGroupEBGPHopLimit,
       "fsBgp4PeerGroupNextHopSelf": fsBgp4PeerGroupNextHopSelf,
       "fsBgp4PeerGroupRflClient": fsBgp4PeerGroupRflClient,
       "fsBgp4PeerGroupTcpSendBufSize": fsBgp4PeerGroupTcpSendBufSize,
       "fsBgp4PeerGroupTcpRcvBufSize": fsBgp4PeerGroupTcpRcvBufSize,
       "fsBgp4PeerGroupCommSendStatus": fsBgp4PeerGroupCommSendStatus,
       "fsBgp4PeerGroupECommSendStatus": fsBgp4PeerGroupECommSendStatus,
       "fsBgp4PeerGroupPassive": fsBgp4PeerGroupPassive,
       "fsBgp4PeerGroupDefaultOriginate": fsBgp4PeerGroupDefaultOriginate,
       "fsBgp4PeerGroupActivateMPCapability": fsBgp4PeerGroupActivateMPCapability,
       "fsBgp4PeerGroupDeactivateMPCapability": fsBgp4PeerGroupDeactivateMPCapability,
       "fsBgp4PeerGroupRouteMapNameIn": fsBgp4PeerGroupRouteMapNameIn,
       "fsBgp4PeerGroupRouteMapNameOut": fsBgp4PeerGroupRouteMapNameOut,
       "fsBgp4PeerGroupStatus": fsBgp4PeerGroupStatus,
       "fsBgp4PeerGroupIpPrefixNameIn": fsBgp4PeerGroupIpPrefixNameIn,
       "fsBgp4PeerGroupIpPrefixNameOut": fsBgp4PeerGroupIpPrefixNameOut,
       "fsBgp4PeerGroupOrfType": fsBgp4PeerGroupOrfType,
       "fsBgp4PeerGroupOrfCapMode": fsBgp4PeerGroupOrfCapMode,
       "fsBgp4PeerGroupOrfRequest": fsBgp4PeerGroupOrfRequest,
       "fsBgp4PeerGroupBfdStatus": fsBgp4PeerGroupBfdStatus,
       "fsBgp4PeerGroupOverrideCapability": fsBgp4PeerGroupOverrideCapability,
       "fsBgp4PeerGroupListTable": fsBgp4PeerGroupListTable,
       "fsBgp4PeerGroupListEntry": fsBgp4PeerGroupListEntry,
       "fsBgp4PeerAddrType": fsBgp4PeerAddrType,
       "fsBgp4PeerAddress": fsBgp4PeerAddress,
       "fsBgp4PeerAddStatus": fsBgp4PeerAddStatus,
       "fsbgp4TCPMKTAuth": fsbgp4TCPMKTAuth,
       "fsbgp4TCPMKTAuthTable": fsbgp4TCPMKTAuthTable,
       "fsbgp4TCPMKTAuthEntry": fsbgp4TCPMKTAuthEntry,
       "fsbgp4TCPMKTAuthKeyId": fsbgp4TCPMKTAuthKeyId,
       "fsbgp4TCPMKTAuthRecvKeyId": fsbgp4TCPMKTAuthRecvKeyId,
       "fsbgp4TCPMKTAuthMasterKey": fsbgp4TCPMKTAuthMasterKey,
       "fsbgp4TCPMKTAuthAlgo": fsbgp4TCPMKTAuthAlgo,
       "fsbgp4TCPMKTAuthTcpOptExc": fsbgp4TCPMKTAuthTcpOptExc,
       "fsbgp4TCPMKTAuthRowStatus": fsbgp4TCPMKTAuthRowStatus,
       "fsbgp4TCPAOAuthPeer": fsbgp4TCPAOAuthPeer,
       "fsbgp4TCPAOAuthPeerTable": fsbgp4TCPAOAuthPeerTable,
       "fsbgp4TCPAOAuthPeerEntry": fsbgp4TCPAOAuthPeerEntry,
       "fsbgp4TCPAOAuthPeerType": fsbgp4TCPAOAuthPeerType,
       "fsbgp4TCPAOAuthPeerAddr": fsbgp4TCPAOAuthPeerAddr,
       "fsbgp4TCPAOAuthKeyId": fsbgp4TCPAOAuthKeyId,
       "fsbgp4TCPAOAuthKeyStatus": fsbgp4TCPAOAuthKeyStatus,
       "fsbgp4TCPAOAuthKeyStartAccept": fsbgp4TCPAOAuthKeyStartAccept,
       "fsbgp4TCPAOAuthKeyStartGenerate": fsbgp4TCPAOAuthKeyStartGenerate,
       "fsbgp4TCPAOAuthKeyStopGenerate": fsbgp4TCPAOAuthKeyStopGenerate,
       "fsbgp4TCPAOAuthKeyStopAccept": fsbgp4TCPAOAuthKeyStopAccept,
       "fsBgp4ORFListTable": fsBgp4ORFListTable,
       "fsBgp4ORFListEntry": fsBgp4ORFListEntry,
       "fsBgp4ORFPeerAddrType": fsBgp4ORFPeerAddrType,
       "fsBgp4ORFPeerAddr": fsBgp4ORFPeerAddr,
       "fsBgp4ORFAfi": fsBgp4ORFAfi,
       "fsBgp4ORFSafi": fsBgp4ORFSafi,
       "fsBgp4ORFType": fsBgp4ORFType,
       "fsBgp4ORFSequence": fsBgp4ORFSequence,
       "fsBgp4ORFAddrPrefix": fsBgp4ORFAddrPrefix,
       "fsBgp4ORFAddrPrefixLen": fsBgp4ORFAddrPrefixLen,
       "fsBgp4ORFMinLength": fsBgp4ORFMinLength,
       "fsBgp4ORFMaxLength": fsBgp4ORFMaxLength,
       "fsBgp4ORFAction": fsBgp4ORFAction,
       "fsBgp4TestGroup": fsBgp4TestGroup,
       "fsBgp4RmTestObject": fsBgp4RmTestObject,
       "fsBgp4RRDNetworkTable": fsBgp4RRDNetworkTable,
       "fsBgp4RRDNetworkEntry": fsBgp4RRDNetworkEntry,
       "fsBgp4RRDNetworkAddr": fsBgp4RRDNetworkAddr,
       "fsBgp4RRDNetworkAddrType": fsBgp4RRDNetworkAddrType,
       "fsBgp4RRDNetworkPrefixLen": fsBgp4RRDNetworkPrefixLen,
       "fsBgp4RRDNetworkRowStatus": fsBgp4RRDNetworkRowStatus}
)
