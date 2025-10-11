# SNMP MIB module (ARICENT-PIMCMN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-PIMCMN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:18 2025
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

(IANAipMRouteProtocol,
 IANAipRouteProtocol) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipMRouteProtocol",
    "IANAipRouteProtocol")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsPimCmnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 111)
)
if mibBuilder.loadTexts:
    fsPimCmnMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Status(TextualConvention, Integer32):
    status = "current"
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



class CompList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_FsPimCmnMIBObjects_ObjectIdentity = ObjectIdentity
fsPimCmnMIBObjects = _FsPimCmnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1)
)
_FuturePimCmnScalars_ObjectIdentity = ObjectIdentity
futurePimCmnScalars = _FuturePimCmnScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1)
)
_FsPimCmnVersionString_Type = DisplayString
_FsPimCmnVersionString_Object = MibScalar
fsPimCmnVersionString = _FsPimCmnVersionString_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 1),
    _FsPimCmnVersionString_Type()
)
fsPimCmnVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnVersionString.setStatus("current")


class _FsPimCmnSPTGroupThreshold_Type(Integer32):
    """Custom type fsPimCmnSPTGroupThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsPimCmnSPTGroupThreshold_Type.__name__ = "Integer32"
_FsPimCmnSPTGroupThreshold_Object = MibScalar
fsPimCmnSPTGroupThreshold = _FsPimCmnSPTGroupThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 2),
    _FsPimCmnSPTGroupThreshold_Type()
)
fsPimCmnSPTGroupThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnSPTGroupThreshold.setStatus("current")


class _FsPimCmnSPTSourceThreshold_Type(Integer32):
    """Custom type fsPimCmnSPTSourceThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsPimCmnSPTSourceThreshold_Type.__name__ = "Integer32"
_FsPimCmnSPTSourceThreshold_Object = MibScalar
fsPimCmnSPTSourceThreshold = _FsPimCmnSPTSourceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 3),
    _FsPimCmnSPTSourceThreshold_Type()
)
fsPimCmnSPTSourceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnSPTSourceThreshold.setStatus("current")


class _FsPimCmnSPTSwitchingPeriod_Type(Integer32):
    """Custom type fsPimCmnSPTSwitchingPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsPimCmnSPTSwitchingPeriod_Type.__name__ = "Integer32"
_FsPimCmnSPTSwitchingPeriod_Object = MibScalar
fsPimCmnSPTSwitchingPeriod = _FsPimCmnSPTSwitchingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 4),
    _FsPimCmnSPTSwitchingPeriod_Type()
)
fsPimCmnSPTSwitchingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnSPTSwitchingPeriod.setStatus("current")


class _FsPimCmnSPTRpThreshold_Type(Integer32):
    """Custom type fsPimCmnSPTRpThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsPimCmnSPTRpThreshold_Type.__name__ = "Integer32"
_FsPimCmnSPTRpThreshold_Object = MibScalar
fsPimCmnSPTRpThreshold = _FsPimCmnSPTRpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 5),
    _FsPimCmnSPTRpThreshold_Type()
)
fsPimCmnSPTRpThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnSPTRpThreshold.setStatus("current")


class _FsPimCmnSPTRpSwitchingPeriod_Type(Integer32):
    """Custom type fsPimCmnSPTRpSwitchingPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsPimCmnSPTRpSwitchingPeriod_Type.__name__ = "Integer32"
_FsPimCmnSPTRpSwitchingPeriod_Object = MibScalar
fsPimCmnSPTRpSwitchingPeriod = _FsPimCmnSPTRpSwitchingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 6),
    _FsPimCmnSPTRpSwitchingPeriod_Type()
)
fsPimCmnSPTRpSwitchingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnSPTRpSwitchingPeriod.setStatus("current")


class _FsPimCmnRegStopRateLimitingPeriod_Type(Integer32):
    """Custom type fsPimCmnRegStopRateLimitingPeriod based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsPimCmnRegStopRateLimitingPeriod_Type.__name__ = "Integer32"
_FsPimCmnRegStopRateLimitingPeriod_Object = MibScalar
fsPimCmnRegStopRateLimitingPeriod = _FsPimCmnRegStopRateLimitingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 7),
    _FsPimCmnRegStopRateLimitingPeriod_Type()
)
fsPimCmnRegStopRateLimitingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnRegStopRateLimitingPeriod.setStatus("current")
_FsPimCmnMemoryAllocFailCount_Type = Integer32
_FsPimCmnMemoryAllocFailCount_Object = MibScalar
fsPimCmnMemoryAllocFailCount = _FsPimCmnMemoryAllocFailCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 8),
    _FsPimCmnMemoryAllocFailCount_Type()
)
fsPimCmnMemoryAllocFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnMemoryAllocFailCount.setStatus("current")


class _FsPimCmnGlobalTrace_Type(Integer32):
    """Custom type fsPimCmnGlobalTrace based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPimCmnGlobalTrace_Type.__name__ = "Integer32"
_FsPimCmnGlobalTrace_Object = MibScalar
fsPimCmnGlobalTrace = _FsPimCmnGlobalTrace_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 9),
    _FsPimCmnGlobalTrace_Type()
)
fsPimCmnGlobalTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnGlobalTrace.setStatus("current")


class _FsPimCmnGlobalDebug_Type(Integer32):
    """Custom type fsPimCmnGlobalDebug based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPimCmnGlobalDebug_Type.__name__ = "Integer32"
_FsPimCmnGlobalDebug_Object = MibScalar
fsPimCmnGlobalDebug = _FsPimCmnGlobalDebug_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 10),
    _FsPimCmnGlobalDebug_Type()
)
fsPimCmnGlobalDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnGlobalDebug.setStatus("current")


class _FsPimCmnPmbrStatus_Type(Integer32):
    """Custom type fsPimCmnPmbrStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FsPimCmnPmbrStatus_Type.__name__ = "Integer32"
_FsPimCmnPmbrStatus_Object = MibScalar
fsPimCmnPmbrStatus = _FsPimCmnPmbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 11),
    _FsPimCmnPmbrStatus_Type()
)
fsPimCmnPmbrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnPmbrStatus.setStatus("current")


class _FsPimCmnRouterMode_Type(Integer32):
    """Custom type fsPimCmnRouterMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ssmonly", 1),
          ("smssm", 2))
    )


_FsPimCmnRouterMode_Type.__name__ = "Integer32"
_FsPimCmnRouterMode_Object = MibScalar
fsPimCmnRouterMode = _FsPimCmnRouterMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 12),
    _FsPimCmnRouterMode_Type()
)
fsPimCmnRouterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnRouterMode.setStatus("current")


class _FsPimCmnStaticRpEnabled_Type(Integer32):
    """Custom type fsPimCmnStaticRpEnabled based on Integer32"""
    defaultValue = 0

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


_FsPimCmnStaticRpEnabled_Type.__name__ = "Integer32"
_FsPimCmnStaticRpEnabled_Object = MibScalar
fsPimCmnStaticRpEnabled = _FsPimCmnStaticRpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 13),
    _FsPimCmnStaticRpEnabled_Type()
)
fsPimCmnStaticRpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnStaticRpEnabled.setStatus("current")


class _FsPimCmnIpStatus_Type(Integer32):
    """Custom type fsPimCmnIpStatus based on Integer32"""
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


_FsPimCmnIpStatus_Type.__name__ = "Integer32"
_FsPimCmnIpStatus_Object = MibScalar
fsPimCmnIpStatus = _FsPimCmnIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 14),
    _FsPimCmnIpStatus_Type()
)
fsPimCmnIpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnIpStatus.setStatus("current")


class _FsPimCmnIpv6Status_Type(Integer32):
    """Custom type fsPimCmnIpv6Status based on Integer32"""
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


_FsPimCmnIpv6Status_Type.__name__ = "Integer32"
_FsPimCmnIpv6Status_Object = MibScalar
fsPimCmnIpv6Status = _FsPimCmnIpv6Status_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 15),
    _FsPimCmnIpv6Status_Type()
)
fsPimCmnIpv6Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnIpv6Status.setStatus("current")


class _FsPimCmnSRProcessingStatus_Type(Integer32):
    """Custom type fsPimCmnSRProcessingStatus based on Integer32"""
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


_FsPimCmnSRProcessingStatus_Type.__name__ = "Integer32"
_FsPimCmnSRProcessingStatus_Object = MibScalar
fsPimCmnSRProcessingStatus = _FsPimCmnSRProcessingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 16),
    _FsPimCmnSRProcessingStatus_Type()
)
fsPimCmnSRProcessingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnSRProcessingStatus.setStatus("current")


class _FsPimCmnRefreshInterval_Type(Integer32):
    """Custom type fsPimCmnRefreshInterval based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(4, 100),
    )


_FsPimCmnRefreshInterval_Type.__name__ = "Integer32"
_FsPimCmnRefreshInterval_Object = MibScalar
fsPimCmnRefreshInterval = _FsPimCmnRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 17),
    _FsPimCmnRefreshInterval_Type()
)
fsPimCmnRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsPimCmnRefreshInterval.setUnits("seconds")


class _FsPimCmnSourceActiveInterval_Type(Unsigned32):
    """Custom type fsPimCmnSourceActiveInterval based on Unsigned32"""
    defaultValue = 210

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 210),
    )


_FsPimCmnSourceActiveInterval_Type.__name__ = "Unsigned32"
_FsPimCmnSourceActiveInterval_Object = MibScalar
fsPimCmnSourceActiveInterval = _FsPimCmnSourceActiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 18),
    _FsPimCmnSourceActiveInterval_Type()
)
fsPimCmnSourceActiveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnSourceActiveInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsPimCmnSourceActiveInterval.setUnits("seconds")


class _FsPimCmnHAAdminStatus_Type(Integer32):
    """Custom type fsPimCmnHAAdminStatus based on Integer32"""
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


_FsPimCmnHAAdminStatus_Type.__name__ = "Integer32"
_FsPimCmnHAAdminStatus_Object = MibScalar
fsPimCmnHAAdminStatus = _FsPimCmnHAAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 19),
    _FsPimCmnHAAdminStatus_Type()
)
fsPimCmnHAAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnHAAdminStatus.setStatus("current")


class _FsPimCmnHAState_Type(Integer32):
    """Custom type fsPimCmnHAState based on Integer32"""
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
        *(("init", 1),
          ("activeStandbyUp", 2),
          ("activeStandbyDown", 3),
          ("standby", 4))
    )


_FsPimCmnHAState_Type.__name__ = "Integer32"
_FsPimCmnHAState_Object = MibScalar
fsPimCmnHAState = _FsPimCmnHAState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 20),
    _FsPimCmnHAState_Type()
)
fsPimCmnHAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnHAState.setStatus("current")


class _FsPimCmnHADynamicBulkUpdStatus_Type(Integer32):
    """Custom type fsPimCmnHADynamicBulkUpdStatus based on Integer32"""
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
        *(("notStarted", 1),
          ("inProgress", 2),
          ("completed", 3),
          ("aborted", 4))
    )


_FsPimCmnHADynamicBulkUpdStatus_Type.__name__ = "Integer32"
_FsPimCmnHADynamicBulkUpdStatus_Object = MibScalar
fsPimCmnHADynamicBulkUpdStatus = _FsPimCmnHADynamicBulkUpdStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 21),
    _FsPimCmnHADynamicBulkUpdStatus_Type()
)
fsPimCmnHADynamicBulkUpdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnHADynamicBulkUpdStatus.setStatus("current")


class _FsPimCmnHAForwardingTblEntryCnt_Type(Integer32):
    """Custom type fsPimCmnHAForwardingTblEntryCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPimCmnHAForwardingTblEntryCnt_Type.__name__ = "Integer32"
_FsPimCmnHAForwardingTblEntryCnt_Object = MibScalar
fsPimCmnHAForwardingTblEntryCnt = _FsPimCmnHAForwardingTblEntryCnt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 22),
    _FsPimCmnHAForwardingTblEntryCnt_Type()
)
fsPimCmnHAForwardingTblEntryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnHAForwardingTblEntryCnt.setStatus("current")


class _FsPimCmnIpRpfVector_Type(Integer32):
    """Custom type fsPimCmnIpRpfVector based on Integer32"""
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


_FsPimCmnIpRpfVector_Type.__name__ = "Integer32"
_FsPimCmnIpRpfVector_Object = MibScalar
fsPimCmnIpRpfVector = _FsPimCmnIpRpfVector_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 23),
    _FsPimCmnIpRpfVector_Type()
)
fsPimCmnIpRpfVector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnIpRpfVector.setStatus("current")


class _FsPimCmnIpBidirPIMStatus_Type(Integer32):
    """Custom type fsPimCmnIpBidirPIMStatus based on Integer32"""
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


_FsPimCmnIpBidirPIMStatus_Type.__name__ = "Integer32"
_FsPimCmnIpBidirPIMStatus_Object = MibScalar
fsPimCmnIpBidirPIMStatus = _FsPimCmnIpBidirPIMStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 24),
    _FsPimCmnIpBidirPIMStatus_Type()
)
fsPimCmnIpBidirPIMStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnIpBidirPIMStatus.setStatus("current")


class _FsPimCmnIpBidirOfferInterval_Type(Integer32):
    """Custom type fsPimCmnIpBidirOfferInterval based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000000),
    )


_FsPimCmnIpBidirOfferInterval_Type.__name__ = "Integer32"
_FsPimCmnIpBidirOfferInterval_Object = MibScalar
fsPimCmnIpBidirOfferInterval = _FsPimCmnIpBidirOfferInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 25),
    _FsPimCmnIpBidirOfferInterval_Type()
)
fsPimCmnIpBidirOfferInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnIpBidirOfferInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsPimCmnIpBidirOfferInterval.setUnits("milliseconds")


class _FsPimCmnIpBidirOfferLimit_Type(Integer32):
    """Custom type fsPimCmnIpBidirOfferLimit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 100),
    )


_FsPimCmnIpBidirOfferLimit_Type.__name__ = "Integer32"
_FsPimCmnIpBidirOfferLimit_Object = MibScalar
fsPimCmnIpBidirOfferLimit = _FsPimCmnIpBidirOfferLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 1, 26),
    _FsPimCmnIpBidirOfferLimit_Type()
)
fsPimCmnIpBidirOfferLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnIpBidirOfferLimit.setStatus("current")
_FuturePimCmnTables_ObjectIdentity = ObjectIdentity
futurePimCmnTables = _FuturePimCmnTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2)
)
_FsPimCmnInterfaceTable_Object = MibTable
fsPimCmnInterfaceTable = _FsPimCmnInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsPimCmnInterfaceTable.setStatus("current")
_FsPimCmnInterfaceEntry_Object = MibTableRow
fsPimCmnInterfaceEntry = _FsPimCmnInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1)
)
fsPimCmnInterfaceEntry.setIndexNames(
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnInterfaceIfIndex"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnInterfaceAddrType"),
)
if mibBuilder.loadTexts:
    fsPimCmnInterfaceEntry.setStatus("current")


class _FsPimCmnInterfaceIfIndex_Type(Integer32):
    """Custom type fsPimCmnInterfaceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPimCmnInterfaceIfIndex_Type.__name__ = "Integer32"
_FsPimCmnInterfaceIfIndex_Object = MibTableColumn
fsPimCmnInterfaceIfIndex = _FsPimCmnInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 1),
    _FsPimCmnInterfaceIfIndex_Type()
)
fsPimCmnInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceIfIndex.setStatus("current")
_FsPimCmnInterfaceAddrType_Type = InetAddressType
_FsPimCmnInterfaceAddrType_Object = MibTableColumn
fsPimCmnInterfaceAddrType = _FsPimCmnInterfaceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 2),
    _FsPimCmnInterfaceAddrType_Type()
)
fsPimCmnInterfaceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceAddrType.setStatus("current")


class _FsPimCmnInterfaceCompId_Type(Integer32):
    """Custom type fsPimCmnInterfaceCompId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimCmnInterfaceCompId_Type.__name__ = "Integer32"
_FsPimCmnInterfaceCompId_Object = MibTableColumn
fsPimCmnInterfaceCompId = _FsPimCmnInterfaceCompId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 3),
    _FsPimCmnInterfaceCompId_Type()
)
fsPimCmnInterfaceCompId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceCompId.setStatus("current")


class _FsPimCmnInterfaceDRPriority_Type(Unsigned32):
    """Custom type fsPimCmnInterfaceDRPriority based on Unsigned32"""
    defaultValue = 1


_FsPimCmnInterfaceDRPriority_Type.__name__ = "Unsigned32"
_FsPimCmnInterfaceDRPriority_Object = MibTableColumn
fsPimCmnInterfaceDRPriority = _FsPimCmnInterfaceDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 4),
    _FsPimCmnInterfaceDRPriority_Type()
)
fsPimCmnInterfaceDRPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceDRPriority.setStatus("current")


class _FsPimCmnInterfaceHelloHoldTime_Type(Integer32):
    """Custom type fsPimCmnInterfaceHelloHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPimCmnInterfaceHelloHoldTime_Type.__name__ = "Integer32"
_FsPimCmnInterfaceHelloHoldTime_Object = MibTableColumn
fsPimCmnInterfaceHelloHoldTime = _FsPimCmnInterfaceHelloHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 5),
    _FsPimCmnInterfaceHelloHoldTime_Type()
)
fsPimCmnInterfaceHelloHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceHelloHoldTime.setStatus("current")


class _FsPimCmnInterfaceLanPruneDelayPresent_Type(Integer32):
    """Custom type fsPimCmnInterfaceLanPruneDelayPresent based on Integer32"""
    defaultValue = 0

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


_FsPimCmnInterfaceLanPruneDelayPresent_Type.__name__ = "Integer32"
_FsPimCmnInterfaceLanPruneDelayPresent_Object = MibTableColumn
fsPimCmnInterfaceLanPruneDelayPresent = _FsPimCmnInterfaceLanPruneDelayPresent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 6),
    _FsPimCmnInterfaceLanPruneDelayPresent_Type()
)
fsPimCmnInterfaceLanPruneDelayPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceLanPruneDelayPresent.setStatus("current")


class _FsPimCmnInterfaceLanDelay_Type(Integer32):
    """Custom type fsPimCmnInterfaceLanDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPimCmnInterfaceLanDelay_Type.__name__ = "Integer32"
_FsPimCmnInterfaceLanDelay_Object = MibTableColumn
fsPimCmnInterfaceLanDelay = _FsPimCmnInterfaceLanDelay_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 7),
    _FsPimCmnInterfaceLanDelay_Type()
)
fsPimCmnInterfaceLanDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceLanDelay.setStatus("current")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceLanDelay.setUnits("milliseconds")


class _FsPimCmnInterfaceOverrideInterval_Type(Integer32):
    """Custom type fsPimCmnInterfaceOverrideInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPimCmnInterfaceOverrideInterval_Type.__name__ = "Integer32"
_FsPimCmnInterfaceOverrideInterval_Object = MibTableColumn
fsPimCmnInterfaceOverrideInterval = _FsPimCmnInterfaceOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 8),
    _FsPimCmnInterfaceOverrideInterval_Type()
)
fsPimCmnInterfaceOverrideInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceOverrideInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceOverrideInterval.setUnits("milliseconds")
_FsPimCmnInterfaceGenerationId_Type = Integer32
_FsPimCmnInterfaceGenerationId_Object = MibTableColumn
fsPimCmnInterfaceGenerationId = _FsPimCmnInterfaceGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 9),
    _FsPimCmnInterfaceGenerationId_Type()
)
fsPimCmnInterfaceGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceGenerationId.setStatus("current")
_FsPimCmnInterfaceSuppressionInterval_Type = Integer32
_FsPimCmnInterfaceSuppressionInterval_Object = MibTableColumn
fsPimCmnInterfaceSuppressionInterval = _FsPimCmnInterfaceSuppressionInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 10),
    _FsPimCmnInterfaceSuppressionInterval_Type()
)
fsPimCmnInterfaceSuppressionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceSuppressionInterval.setStatus("current")
_FsPimCmnInterfaceAdminStatus_Type = Integer32
_FsPimCmnInterfaceAdminStatus_Object = MibTableColumn
fsPimCmnInterfaceAdminStatus = _FsPimCmnInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 11),
    _FsPimCmnInterfaceAdminStatus_Type()
)
fsPimCmnInterfaceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceAdminStatus.setStatus("current")
_FsPimCmnInterfaceBorderBit_Type = Integer32
_FsPimCmnInterfaceBorderBit_Object = MibTableColumn
fsPimCmnInterfaceBorderBit = _FsPimCmnInterfaceBorderBit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 12),
    _FsPimCmnInterfaceBorderBit_Type()
)
fsPimCmnInterfaceBorderBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceBorderBit.setStatus("current")


class _FsPimCmnInterfaceGraftRetryInterval_Type(Unsigned32):
    """Custom type fsPimCmnInterfaceGraftRetryInterval based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsPimCmnInterfaceGraftRetryInterval_Type.__name__ = "Unsigned32"
_FsPimCmnInterfaceGraftRetryInterval_Object = MibTableColumn
fsPimCmnInterfaceGraftRetryInterval = _FsPimCmnInterfaceGraftRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 13),
    _FsPimCmnInterfaceGraftRetryInterval_Type()
)
fsPimCmnInterfaceGraftRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceGraftRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceGraftRetryInterval.setUnits("seconds")
_FsPimCmnInterfaceSRPriorityEnabled_Type = TruthValue
_FsPimCmnInterfaceSRPriorityEnabled_Object = MibTableColumn
fsPimCmnInterfaceSRPriorityEnabled = _FsPimCmnInterfaceSRPriorityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 14),
    _FsPimCmnInterfaceSRPriorityEnabled_Type()
)
fsPimCmnInterfaceSRPriorityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceSRPriorityEnabled.setStatus("current")


class _FsPimCmnInterfaceTtl_Type(Integer32):
    """Custom type fsPimCmnInterfaceTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPimCmnInterfaceTtl_Type.__name__ = "Integer32"
_FsPimCmnInterfaceTtl_Object = MibTableColumn
fsPimCmnInterfaceTtl = _FsPimCmnInterfaceTtl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 15),
    _FsPimCmnInterfaceTtl_Type()
)
fsPimCmnInterfaceTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceTtl.setStatus("current")
_FsPimCmnInterfaceProtocol_Type = IANAipMRouteProtocol
_FsPimCmnInterfaceProtocol_Object = MibTableColumn
fsPimCmnInterfaceProtocol = _FsPimCmnInterfaceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 16),
    _FsPimCmnInterfaceProtocol_Type()
)
fsPimCmnInterfaceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceProtocol.setStatus("current")


class _FsPimCmnInterfaceRateLimit_Type(Integer32):
    """Custom type fsPimCmnInterfaceRateLimit based on Integer32"""
    defaultValue = 0


_FsPimCmnInterfaceRateLimit_Type.__name__ = "Integer32"
_FsPimCmnInterfaceRateLimit_Object = MibTableColumn
fsPimCmnInterfaceRateLimit = _FsPimCmnInterfaceRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 17),
    _FsPimCmnInterfaceRateLimit_Type()
)
fsPimCmnInterfaceRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceRateLimit.setStatus("current")
_FsPimCmnInterfaceInMcastOctets_Type = Counter32
_FsPimCmnInterfaceInMcastOctets_Object = MibTableColumn
fsPimCmnInterfaceInMcastOctets = _FsPimCmnInterfaceInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 18),
    _FsPimCmnInterfaceInMcastOctets_Type()
)
fsPimCmnInterfaceInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceInMcastOctets.setStatus("current")
_FsPimCmnInterfaceOutMcastOctets_Type = Counter32
_FsPimCmnInterfaceOutMcastOctets_Object = MibTableColumn
fsPimCmnInterfaceOutMcastOctets = _FsPimCmnInterfaceOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 19),
    _FsPimCmnInterfaceOutMcastOctets_Type()
)
fsPimCmnInterfaceOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceOutMcastOctets.setStatus("current")
_FsPimCmnInterfaceHCInMcastOctets_Type = Counter64
_FsPimCmnInterfaceHCInMcastOctets_Object = MibTableColumn
fsPimCmnInterfaceHCInMcastOctets = _FsPimCmnInterfaceHCInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 20),
    _FsPimCmnInterfaceHCInMcastOctets_Type()
)
fsPimCmnInterfaceHCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceHCInMcastOctets.setStatus("current")
_FsPimCmnInterfaceHCOutMcastOctets_Type = Counter64
_FsPimCmnInterfaceHCOutMcastOctets_Object = MibTableColumn
fsPimCmnInterfaceHCOutMcastOctets = _FsPimCmnInterfaceHCOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 21),
    _FsPimCmnInterfaceHCOutMcastOctets_Type()
)
fsPimCmnInterfaceHCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceHCOutMcastOctets.setStatus("current")
_FsPimCmnInterfaceCompIdList_Type = CompList
_FsPimCmnInterfaceCompIdList_Object = MibTableColumn
fsPimCmnInterfaceCompIdList = _FsPimCmnInterfaceCompIdList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 22),
    _FsPimCmnInterfaceCompIdList_Type()
)
fsPimCmnInterfaceCompIdList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceCompIdList.setStatus("current")
_FsPimCmnInterfaceDFOfferSentPkts_Type = Counter32
_FsPimCmnInterfaceDFOfferSentPkts_Object = MibTableColumn
fsPimCmnInterfaceDFOfferSentPkts = _FsPimCmnInterfaceDFOfferSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 23),
    _FsPimCmnInterfaceDFOfferSentPkts_Type()
)
fsPimCmnInterfaceDFOfferSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceDFOfferSentPkts.setStatus("current")
_FsPimCmnInterfaceDFOfferRcvdPkts_Type = Counter32
_FsPimCmnInterfaceDFOfferRcvdPkts_Object = MibTableColumn
fsPimCmnInterfaceDFOfferRcvdPkts = _FsPimCmnInterfaceDFOfferRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 24),
    _FsPimCmnInterfaceDFOfferRcvdPkts_Type()
)
fsPimCmnInterfaceDFOfferRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceDFOfferRcvdPkts.setStatus("current")
_FsPimCmnInterfaceDFWinnerSentPkts_Type = Counter32
_FsPimCmnInterfaceDFWinnerSentPkts_Object = MibTableColumn
fsPimCmnInterfaceDFWinnerSentPkts = _FsPimCmnInterfaceDFWinnerSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 25),
    _FsPimCmnInterfaceDFWinnerSentPkts_Type()
)
fsPimCmnInterfaceDFWinnerSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceDFWinnerSentPkts.setStatus("current")
_FsPimCmnInterfaceDFWinnerRcvdPkts_Type = Counter32
_FsPimCmnInterfaceDFWinnerRcvdPkts_Object = MibTableColumn
fsPimCmnInterfaceDFWinnerRcvdPkts = _FsPimCmnInterfaceDFWinnerRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 26),
    _FsPimCmnInterfaceDFWinnerRcvdPkts_Type()
)
fsPimCmnInterfaceDFWinnerRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceDFWinnerRcvdPkts.setStatus("current")
_FsPimCmnInterfaceDFBackoffSentPkts_Type = Counter32
_FsPimCmnInterfaceDFBackoffSentPkts_Object = MibTableColumn
fsPimCmnInterfaceDFBackoffSentPkts = _FsPimCmnInterfaceDFBackoffSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 27),
    _FsPimCmnInterfaceDFBackoffSentPkts_Type()
)
fsPimCmnInterfaceDFBackoffSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceDFBackoffSentPkts.setStatus("current")
_FsPimCmnInterfaceDFBackoffRcvdPkts_Type = Counter32
_FsPimCmnInterfaceDFBackoffRcvdPkts_Object = MibTableColumn
fsPimCmnInterfaceDFBackoffRcvdPkts = _FsPimCmnInterfaceDFBackoffRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 28),
    _FsPimCmnInterfaceDFBackoffRcvdPkts_Type()
)
fsPimCmnInterfaceDFBackoffRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceDFBackoffRcvdPkts.setStatus("current")
_FsPimCmnInterfaceDFPassSentPkts_Type = Counter32
_FsPimCmnInterfaceDFPassSentPkts_Object = MibTableColumn
fsPimCmnInterfaceDFPassSentPkts = _FsPimCmnInterfaceDFPassSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 29),
    _FsPimCmnInterfaceDFPassSentPkts_Type()
)
fsPimCmnInterfaceDFPassSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceDFPassSentPkts.setStatus("current")
_FsPimCmnInterfaceDFPassRcvdPkts_Type = Counter32
_FsPimCmnInterfaceDFPassRcvdPkts_Object = MibTableColumn
fsPimCmnInterfaceDFPassRcvdPkts = _FsPimCmnInterfaceDFPassRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 30),
    _FsPimCmnInterfaceDFPassRcvdPkts_Type()
)
fsPimCmnInterfaceDFPassRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceDFPassRcvdPkts.setStatus("current")
_FsPimCmnInterfaceCKSumErrorPkts_Type = Counter32
_FsPimCmnInterfaceCKSumErrorPkts_Object = MibTableColumn
fsPimCmnInterfaceCKSumErrorPkts = _FsPimCmnInterfaceCKSumErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 31),
    _FsPimCmnInterfaceCKSumErrorPkts_Type()
)
fsPimCmnInterfaceCKSumErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceCKSumErrorPkts.setStatus("current")
_FsPimCmnInterfaceInvalidTypePkts_Type = Counter32
_FsPimCmnInterfaceInvalidTypePkts_Object = MibTableColumn
fsPimCmnInterfaceInvalidTypePkts = _FsPimCmnInterfaceInvalidTypePkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 32),
    _FsPimCmnInterfaceInvalidTypePkts_Type()
)
fsPimCmnInterfaceInvalidTypePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceInvalidTypePkts.setStatus("current")
_FsPimCmnInterfaceInvalidDFSubTypePkts_Type = Counter32
_FsPimCmnInterfaceInvalidDFSubTypePkts_Object = MibTableColumn
fsPimCmnInterfaceInvalidDFSubTypePkts = _FsPimCmnInterfaceInvalidDFSubTypePkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 33),
    _FsPimCmnInterfaceInvalidDFSubTypePkts_Type()
)
fsPimCmnInterfaceInvalidDFSubTypePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceInvalidDFSubTypePkts.setStatus("current")
_FsPimCmnInterfaceAuthFailPkts_Type = Counter32
_FsPimCmnInterfaceAuthFailPkts_Object = MibTableColumn
fsPimCmnInterfaceAuthFailPkts = _FsPimCmnInterfaceAuthFailPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 34),
    _FsPimCmnInterfaceAuthFailPkts_Type()
)
fsPimCmnInterfaceAuthFailPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceAuthFailPkts.setStatus("current")
_FsPimCmnInterfaceFromNonNbrsPkts_Type = Counter32
_FsPimCmnInterfaceFromNonNbrsPkts_Object = MibTableColumn
fsPimCmnInterfaceFromNonNbrsPkts = _FsPimCmnInterfaceFromNonNbrsPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 35),
    _FsPimCmnInterfaceFromNonNbrsPkts_Type()
)
fsPimCmnInterfaceFromNonNbrsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceFromNonNbrsPkts.setStatus("current")
_FsPimCmnInterfaceJPRcvdOnRPFPkts_Type = Counter32
_FsPimCmnInterfaceJPRcvdOnRPFPkts_Object = MibTableColumn
fsPimCmnInterfaceJPRcvdOnRPFPkts = _FsPimCmnInterfaceJPRcvdOnRPFPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 36),
    _FsPimCmnInterfaceJPRcvdOnRPFPkts_Type()
)
fsPimCmnInterfaceJPRcvdOnRPFPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceJPRcvdOnRPFPkts.setStatus("current")
_FsPimCmnInterfaceJPRcvdNoRPPkts_Type = Counter32
_FsPimCmnInterfaceJPRcvdNoRPPkts_Object = MibTableColumn
fsPimCmnInterfaceJPRcvdNoRPPkts = _FsPimCmnInterfaceJPRcvdNoRPPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 37),
    _FsPimCmnInterfaceJPRcvdNoRPPkts_Type()
)
fsPimCmnInterfaceJPRcvdNoRPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceJPRcvdNoRPPkts.setStatus("current")
_FsPimCmnInterfaceJPRcvdWrongRPPkts_Type = Counter32
_FsPimCmnInterfaceJPRcvdWrongRPPkts_Object = MibTableColumn
fsPimCmnInterfaceJPRcvdWrongRPPkts = _FsPimCmnInterfaceJPRcvdWrongRPPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 38),
    _FsPimCmnInterfaceJPRcvdWrongRPPkts_Type()
)
fsPimCmnInterfaceJPRcvdWrongRPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceJPRcvdWrongRPPkts.setStatus("current")
_FsPimCmnInterfaceJoinSSMGrpPkts_Type = Counter32
_FsPimCmnInterfaceJoinSSMGrpPkts_Object = MibTableColumn
fsPimCmnInterfaceJoinSSMGrpPkts = _FsPimCmnInterfaceJoinSSMGrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 39),
    _FsPimCmnInterfaceJoinSSMGrpPkts_Type()
)
fsPimCmnInterfaceJoinSSMGrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceJoinSSMGrpPkts.setStatus("current")
_FsPimCmnInterfaceJoinBidirGrpPkts_Type = Counter32
_FsPimCmnInterfaceJoinBidirGrpPkts_Object = MibTableColumn
fsPimCmnInterfaceJoinBidirGrpPkts = _FsPimCmnInterfaceJoinBidirGrpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 40),
    _FsPimCmnInterfaceJoinBidirGrpPkts_Type()
)
fsPimCmnInterfaceJoinBidirGrpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceJoinBidirGrpPkts.setStatus("current")
_FsPimCmnInterfaceHelloRcvdPkts_Type = Counter32
_FsPimCmnInterfaceHelloRcvdPkts_Object = MibTableColumn
fsPimCmnInterfaceHelloRcvdPkts = _FsPimCmnInterfaceHelloRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 41),
    _FsPimCmnInterfaceHelloRcvdPkts_Type()
)
fsPimCmnInterfaceHelloRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceHelloRcvdPkts.setStatus("current")
_FsPimCmnInterfaceHelloSentPkts_Type = Counter32
_FsPimCmnInterfaceHelloSentPkts_Object = MibTableColumn
fsPimCmnInterfaceHelloSentPkts = _FsPimCmnInterfaceHelloSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 42),
    _FsPimCmnInterfaceHelloSentPkts_Type()
)
fsPimCmnInterfaceHelloSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceHelloSentPkts.setStatus("current")
_FsPimCmnInterfaceJPRcvdPkts_Type = Counter32
_FsPimCmnInterfaceJPRcvdPkts_Object = MibTableColumn
fsPimCmnInterfaceJPRcvdPkts = _FsPimCmnInterfaceJPRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 43),
    _FsPimCmnInterfaceJPRcvdPkts_Type()
)
fsPimCmnInterfaceJPRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceJPRcvdPkts.setStatus("current")
_FsPimCmnInterfaceJPSentPkts_Type = Counter32
_FsPimCmnInterfaceJPSentPkts_Object = MibTableColumn
fsPimCmnInterfaceJPSentPkts = _FsPimCmnInterfaceJPSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 44),
    _FsPimCmnInterfaceJPSentPkts_Type()
)
fsPimCmnInterfaceJPSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceJPSentPkts.setStatus("current")
_FsPimCmnInterfaceAssertRcvdPkts_Type = Counter32
_FsPimCmnInterfaceAssertRcvdPkts_Object = MibTableColumn
fsPimCmnInterfaceAssertRcvdPkts = _FsPimCmnInterfaceAssertRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 45),
    _FsPimCmnInterfaceAssertRcvdPkts_Type()
)
fsPimCmnInterfaceAssertRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceAssertRcvdPkts.setStatus("current")
_FsPimCmnInterfaceAssertSentPkts_Type = Counter32
_FsPimCmnInterfaceAssertSentPkts_Object = MibTableColumn
fsPimCmnInterfaceAssertSentPkts = _FsPimCmnInterfaceAssertSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 46),
    _FsPimCmnInterfaceAssertSentPkts_Type()
)
fsPimCmnInterfaceAssertSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceAssertSentPkts.setStatus("current")
_FsPimCmnInterfaceGraftRcvdPkts_Type = Counter32
_FsPimCmnInterfaceGraftRcvdPkts_Object = MibTableColumn
fsPimCmnInterfaceGraftRcvdPkts = _FsPimCmnInterfaceGraftRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 47),
    _FsPimCmnInterfaceGraftRcvdPkts_Type()
)
fsPimCmnInterfaceGraftRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceGraftRcvdPkts.setStatus("current")
_FsPimCmnInterfaceGraftSentPkts_Type = Counter32
_FsPimCmnInterfaceGraftSentPkts_Object = MibTableColumn
fsPimCmnInterfaceGraftSentPkts = _FsPimCmnInterfaceGraftSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 48),
    _FsPimCmnInterfaceGraftSentPkts_Type()
)
fsPimCmnInterfaceGraftSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceGraftSentPkts.setStatus("current")
_FsPimCmnInterfaceGraftAckRcvdPkts_Type = Counter32
_FsPimCmnInterfaceGraftAckRcvdPkts_Object = MibTableColumn
fsPimCmnInterfaceGraftAckRcvdPkts = _FsPimCmnInterfaceGraftAckRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 49),
    _FsPimCmnInterfaceGraftAckRcvdPkts_Type()
)
fsPimCmnInterfaceGraftAckRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceGraftAckRcvdPkts.setStatus("current")
_FsPimCmnInterfaceGraftAckSentPkts_Type = Counter32
_FsPimCmnInterfaceGraftAckSentPkts_Object = MibTableColumn
fsPimCmnInterfaceGraftAckSentPkts = _FsPimCmnInterfaceGraftAckSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 50),
    _FsPimCmnInterfaceGraftAckSentPkts_Type()
)
fsPimCmnInterfaceGraftAckSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceGraftAckSentPkts.setStatus("current")
_FsPimCmnInterfacePackLenErrorPkts_Type = Counter32
_FsPimCmnInterfacePackLenErrorPkts_Object = MibTableColumn
fsPimCmnInterfacePackLenErrorPkts = _FsPimCmnInterfacePackLenErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 51),
    _FsPimCmnInterfacePackLenErrorPkts_Type()
)
fsPimCmnInterfacePackLenErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfacePackLenErrorPkts.setStatus("current")
_FsPimCmnInterfaceBadVersionPkts_Type = Counter32
_FsPimCmnInterfaceBadVersionPkts_Object = MibTableColumn
fsPimCmnInterfaceBadVersionPkts = _FsPimCmnInterfaceBadVersionPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 53),
    _FsPimCmnInterfaceBadVersionPkts_Type()
)
fsPimCmnInterfaceBadVersionPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceBadVersionPkts.setStatus("current")
_FsPimCmnInterfacePktsfromSelf_Type = Counter32
_FsPimCmnInterfacePktsfromSelf_Object = MibTableColumn
fsPimCmnInterfacePktsfromSelf = _FsPimCmnInterfacePktsfromSelf_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 54),
    _FsPimCmnInterfacePktsfromSelf_Type()
)
fsPimCmnInterfacePktsfromSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfacePktsfromSelf.setStatus("current")
_FsPimCmnInterfaceExtBorderBit_Type = Integer32
_FsPimCmnInterfaceExtBorderBit_Object = MibTableColumn
fsPimCmnInterfaceExtBorderBit = _FsPimCmnInterfaceExtBorderBit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 55),
    _FsPimCmnInterfaceExtBorderBit_Type()
)
fsPimCmnInterfaceExtBorderBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceExtBorderBit.setStatus("current")
_FsPimCmnInterfaceJoinSSMBadPkts_Type = Counter32
_FsPimCmnInterfaceJoinSSMBadPkts_Object = MibTableColumn
fsPimCmnInterfaceJoinSSMBadPkts = _FsPimCmnInterfaceJoinSSMBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 1, 1, 56),
    _FsPimCmnInterfaceJoinSSMBadPkts_Type()
)
fsPimCmnInterfaceJoinSSMBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnInterfaceJoinSSMBadPkts.setStatus("current")
_FsPimCmnNeighborTable_Object = MibTable
fsPimCmnNeighborTable = _FsPimCmnNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fsPimCmnNeighborTable.setStatus("deprecated")
_FsPimCmnNeighborEntry_Object = MibTableRow
fsPimCmnNeighborEntry = _FsPimCmnNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 2, 1)
)
fsPimCmnNeighborEntry.setIndexNames(
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnNeighborCompId"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnNeighborAddrType"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnNeighborAddress"),
)
if mibBuilder.loadTexts:
    fsPimCmnNeighborEntry.setStatus("deprecated")


class _FsPimCmnNeighborCompId_Type(Integer32):
    """Custom type fsPimCmnNeighborCompId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimCmnNeighborCompId_Type.__name__ = "Integer32"
_FsPimCmnNeighborCompId_Object = MibTableColumn
fsPimCmnNeighborCompId = _FsPimCmnNeighborCompId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 2, 1, 1),
    _FsPimCmnNeighborCompId_Type()
)
fsPimCmnNeighborCompId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnNeighborCompId.setStatus("deprecated")
_FsPimCmnNeighborAddrType_Type = InetAddressType
_FsPimCmnNeighborAddrType_Object = MibTableColumn
fsPimCmnNeighborAddrType = _FsPimCmnNeighborAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 2, 1, 2),
    _FsPimCmnNeighborAddrType_Type()
)
fsPimCmnNeighborAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnNeighborAddrType.setStatus("deprecated")
_FsPimCmnNeighborAddress_Type = InetAddress
_FsPimCmnNeighborAddress_Object = MibTableColumn
fsPimCmnNeighborAddress = _FsPimCmnNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 2, 1, 3),
    _FsPimCmnNeighborAddress_Type()
)
fsPimCmnNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnNeighborAddress.setStatus("deprecated")
_FsPimCmnNeighborIfIndex_Type = Integer32
_FsPimCmnNeighborIfIndex_Object = MibTableColumn
fsPimCmnNeighborIfIndex = _FsPimCmnNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 2, 1, 4),
    _FsPimCmnNeighborIfIndex_Type()
)
fsPimCmnNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborIfIndex.setStatus("deprecated")
_FsPimCmnNeighborUpTime_Type = TimeTicks
_FsPimCmnNeighborUpTime_Object = MibTableColumn
fsPimCmnNeighborUpTime = _FsPimCmnNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 2, 1, 5),
    _FsPimCmnNeighborUpTime_Type()
)
fsPimCmnNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborUpTime.setStatus("deprecated")
_FsPimCmnNeighborExpiryTime_Type = TimeTicks
_FsPimCmnNeighborExpiryTime_Object = MibTableColumn
fsPimCmnNeighborExpiryTime = _FsPimCmnNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 2, 1, 6),
    _FsPimCmnNeighborExpiryTime_Type()
)
fsPimCmnNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborExpiryTime.setStatus("deprecated")
_FsPimCmnNeighborGenerationId_Type = Integer32
_FsPimCmnNeighborGenerationId_Object = MibTableColumn
fsPimCmnNeighborGenerationId = _FsPimCmnNeighborGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 2, 1, 7),
    _FsPimCmnNeighborGenerationId_Type()
)
fsPimCmnNeighborGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborGenerationId.setStatus("deprecated")
_FsPimCmnNeighborLanDelay_Type = Integer32
_FsPimCmnNeighborLanDelay_Object = MibTableColumn
fsPimCmnNeighborLanDelay = _FsPimCmnNeighborLanDelay_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 2, 1, 8),
    _FsPimCmnNeighborLanDelay_Type()
)
fsPimCmnNeighborLanDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborLanDelay.setStatus("deprecated")
_FsPimCmnNeighborDRPriority_Type = Unsigned32
_FsPimCmnNeighborDRPriority_Object = MibTableColumn
fsPimCmnNeighborDRPriority = _FsPimCmnNeighborDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 2, 1, 9),
    _FsPimCmnNeighborDRPriority_Type()
)
fsPimCmnNeighborDRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborDRPriority.setStatus("deprecated")
_FsPimCmnNeighborOverrideInterval_Type = Integer32
_FsPimCmnNeighborOverrideInterval_Object = MibTableColumn
fsPimCmnNeighborOverrideInterval = _FsPimCmnNeighborOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 2, 1, 10),
    _FsPimCmnNeighborOverrideInterval_Type()
)
fsPimCmnNeighborOverrideInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborOverrideInterval.setStatus("deprecated")
_FsPimCmnNeighborSRCapable_Type = TruthValue
_FsPimCmnNeighborSRCapable_Object = MibTableColumn
fsPimCmnNeighborSRCapable = _FsPimCmnNeighborSRCapable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 2, 1, 11),
    _FsPimCmnNeighborSRCapable_Type()
)
fsPimCmnNeighborSRCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborSRCapable.setStatus("deprecated")
_FsPimCmnNeighborRPFCapable_Type = TruthValue
_FsPimCmnNeighborRPFCapable_Object = MibTableColumn
fsPimCmnNeighborRPFCapable = _FsPimCmnNeighborRPFCapable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 2, 1, 12),
    _FsPimCmnNeighborRPFCapable_Type()
)
fsPimCmnNeighborRPFCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborRPFCapable.setStatus("deprecated")
_FsPimCmnNeighborBidirCapable_Type = TruthValue
_FsPimCmnNeighborBidirCapable_Object = MibTableColumn
fsPimCmnNeighborBidirCapable = _FsPimCmnNeighborBidirCapable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 2, 1, 13),
    _FsPimCmnNeighborBidirCapable_Type()
)
fsPimCmnNeighborBidirCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborBidirCapable.setStatus("deprecated")
_FsPimCmnIpMRouteTable_Object = MibTable
fsPimCmnIpMRouteTable = _FsPimCmnIpMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteTable.setStatus("current")
_FsPimCmnIpMRouteEntry_Object = MibTableRow
fsPimCmnIpMRouteEntry = _FsPimCmnIpMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1)
)
fsPimCmnIpMRouteEntry.setIndexNames(
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpMRouteCompId"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpMRouteAddrType"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpMRouteGroup"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpMRouteSource"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpMRouteSourceMasklen"),
)
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteEntry.setStatus("current")


class _FsPimCmnIpMRouteCompId_Type(Integer32):
    """Custom type fsPimCmnIpMRouteCompId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimCmnIpMRouteCompId_Type.__name__ = "Integer32"
_FsPimCmnIpMRouteCompId_Object = MibTableColumn
fsPimCmnIpMRouteCompId = _FsPimCmnIpMRouteCompId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 1),
    _FsPimCmnIpMRouteCompId_Type()
)
fsPimCmnIpMRouteCompId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteCompId.setStatus("current")
_FsPimCmnIpMRouteAddrType_Type = InetAddressType
_FsPimCmnIpMRouteAddrType_Object = MibTableColumn
fsPimCmnIpMRouteAddrType = _FsPimCmnIpMRouteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 2),
    _FsPimCmnIpMRouteAddrType_Type()
)
fsPimCmnIpMRouteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteAddrType.setStatus("current")
_FsPimCmnIpMRouteGroup_Type = InetAddress
_FsPimCmnIpMRouteGroup_Object = MibTableColumn
fsPimCmnIpMRouteGroup = _FsPimCmnIpMRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 3),
    _FsPimCmnIpMRouteGroup_Type()
)
fsPimCmnIpMRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteGroup.setStatus("current")
_FsPimCmnIpMRouteSource_Type = InetAddress
_FsPimCmnIpMRouteSource_Object = MibTableColumn
fsPimCmnIpMRouteSource = _FsPimCmnIpMRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 4),
    _FsPimCmnIpMRouteSource_Type()
)
fsPimCmnIpMRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteSource.setStatus("current")


class _FsPimCmnIpMRouteSourceMasklen_Type(Integer32):
    """Custom type fsPimCmnIpMRouteSourceMasklen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsPimCmnIpMRouteSourceMasklen_Type.__name__ = "Integer32"
_FsPimCmnIpMRouteSourceMasklen_Object = MibTableColumn
fsPimCmnIpMRouteSourceMasklen = _FsPimCmnIpMRouteSourceMasklen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 5),
    _FsPimCmnIpMRouteSourceMasklen_Type()
)
fsPimCmnIpMRouteSourceMasklen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteSourceMasklen.setStatus("current")
_FsPimCmnIpMRouteUpstreamNeighbor_Type = InetAddress
_FsPimCmnIpMRouteUpstreamNeighbor_Object = MibTableColumn
fsPimCmnIpMRouteUpstreamNeighbor = _FsPimCmnIpMRouteUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 6),
    _FsPimCmnIpMRouteUpstreamNeighbor_Type()
)
fsPimCmnIpMRouteUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteUpstreamNeighbor.setStatus("current")
_FsPimCmnIpMRouteInIfIndex_Type = Integer32
_FsPimCmnIpMRouteInIfIndex_Object = MibTableColumn
fsPimCmnIpMRouteInIfIndex = _FsPimCmnIpMRouteInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 7),
    _FsPimCmnIpMRouteInIfIndex_Type()
)
fsPimCmnIpMRouteInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteInIfIndex.setStatus("current")
_FsPimCmnIpMRouteUpTime_Type = TimeTicks
_FsPimCmnIpMRouteUpTime_Object = MibTableColumn
fsPimCmnIpMRouteUpTime = _FsPimCmnIpMRouteUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 8),
    _FsPimCmnIpMRouteUpTime_Type()
)
fsPimCmnIpMRouteUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteUpTime.setStatus("current")
_FsPimCmnIpMRoutePkts_Type = Counter32
_FsPimCmnIpMRoutePkts_Object = MibTableColumn
fsPimCmnIpMRoutePkts = _FsPimCmnIpMRoutePkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 9),
    _FsPimCmnIpMRoutePkts_Type()
)
fsPimCmnIpMRoutePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRoutePkts.setStatus("current")
_FsPimCmnIpMRouteUpstreamAssertTimer_Type = TimeTicks
_FsPimCmnIpMRouteUpstreamAssertTimer_Object = MibTableColumn
fsPimCmnIpMRouteUpstreamAssertTimer = _FsPimCmnIpMRouteUpstreamAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 10),
    _FsPimCmnIpMRouteUpstreamAssertTimer_Type()
)
fsPimCmnIpMRouteUpstreamAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteUpstreamAssertTimer.setStatus("current")
_FsPimCmnIpMRouteAssertMetric_Type = Integer32
_FsPimCmnIpMRouteAssertMetric_Object = MibTableColumn
fsPimCmnIpMRouteAssertMetric = _FsPimCmnIpMRouteAssertMetric_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 11),
    _FsPimCmnIpMRouteAssertMetric_Type()
)
fsPimCmnIpMRouteAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteAssertMetric.setStatus("current")
_FsPimCmnIpMRouteAssertMetricPref_Type = Integer32
_FsPimCmnIpMRouteAssertMetricPref_Object = MibTableColumn
fsPimCmnIpMRouteAssertMetricPref = _FsPimCmnIpMRouteAssertMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 12),
    _FsPimCmnIpMRouteAssertMetricPref_Type()
)
fsPimCmnIpMRouteAssertMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteAssertMetricPref.setStatus("current")
_FsPimCmnIpMRouteAssertRPTBit_Type = TruthValue
_FsPimCmnIpMRouteAssertRPTBit_Object = MibTableColumn
fsPimCmnIpMRouteAssertRPTBit = _FsPimCmnIpMRouteAssertRPTBit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 13),
    _FsPimCmnIpMRouteAssertRPTBit_Type()
)
fsPimCmnIpMRouteAssertRPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteAssertRPTBit.setStatus("current")
_FsPimCmnIpMRouteTimerFlags_Type = Integer32
_FsPimCmnIpMRouteTimerFlags_Object = MibTableColumn
fsPimCmnIpMRouteTimerFlags = _FsPimCmnIpMRouteTimerFlags_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 14),
    _FsPimCmnIpMRouteTimerFlags_Type()
)
fsPimCmnIpMRouteTimerFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteTimerFlags.setStatus("current")
_FsPimCmnIpMRouteFlags_Type = Integer32
_FsPimCmnIpMRouteFlags_Object = MibTableColumn
fsPimCmnIpMRouteFlags = _FsPimCmnIpMRouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 15),
    _FsPimCmnIpMRouteFlags_Type()
)
fsPimCmnIpMRouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteFlags.setStatus("current")


class _FsPimCmnIpMRouteUpstreamPruneState_Type(Integer32):
    """Custom type fsPimCmnIpMRouteUpstreamPruneState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("ackpending", 2),
          ("pruned", 3))
    )


_FsPimCmnIpMRouteUpstreamPruneState_Type.__name__ = "Integer32"
_FsPimCmnIpMRouteUpstreamPruneState_Object = MibTableColumn
fsPimCmnIpMRouteUpstreamPruneState = _FsPimCmnIpMRouteUpstreamPruneState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 16),
    _FsPimCmnIpMRouteUpstreamPruneState_Type()
)
fsPimCmnIpMRouteUpstreamPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteUpstreamPruneState.setStatus("current")
_FsPimCmnIpMRouteUpstreamPruneLimitTimer_Type = TimeTicks
_FsPimCmnIpMRouteUpstreamPruneLimitTimer_Object = MibTableColumn
fsPimCmnIpMRouteUpstreamPruneLimitTimer = _FsPimCmnIpMRouteUpstreamPruneLimitTimer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 17),
    _FsPimCmnIpMRouteUpstreamPruneLimitTimer_Type()
)
fsPimCmnIpMRouteUpstreamPruneLimitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteUpstreamPruneLimitTimer.setStatus("current")


class _FsPimCmnIpMRouteOriginatorState_Type(Integer32):
    """Custom type fsPimCmnIpMRouteOriginatorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOriginator", 1),
          ("originator", 2))
    )


_FsPimCmnIpMRouteOriginatorState_Type.__name__ = "Integer32"
_FsPimCmnIpMRouteOriginatorState_Object = MibTableColumn
fsPimCmnIpMRouteOriginatorState = _FsPimCmnIpMRouteOriginatorState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 18),
    _FsPimCmnIpMRouteOriginatorState_Type()
)
fsPimCmnIpMRouteOriginatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteOriginatorState.setStatus("current")
_FsPimCmnIpMRouteSourceActiveTimer_Type = TimeTicks
_FsPimCmnIpMRouteSourceActiveTimer_Object = MibTableColumn
fsPimCmnIpMRouteSourceActiveTimer = _FsPimCmnIpMRouteSourceActiveTimer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 19),
    _FsPimCmnIpMRouteSourceActiveTimer_Type()
)
fsPimCmnIpMRouteSourceActiveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteSourceActiveTimer.setStatus("current")
_FsPimCmnIpMRouteStateRefreshTimer_Type = TimeTicks
_FsPimCmnIpMRouteStateRefreshTimer_Object = MibTableColumn
fsPimCmnIpMRouteStateRefreshTimer = _FsPimCmnIpMRouteStateRefreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 20),
    _FsPimCmnIpMRouteStateRefreshTimer_Type()
)
fsPimCmnIpMRouteStateRefreshTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteStateRefreshTimer.setStatus("current")
_FsPimCmnIpMRouteExpiryTime_Type = TimeTicks
_FsPimCmnIpMRouteExpiryTime_Object = MibTableColumn
fsPimCmnIpMRouteExpiryTime = _FsPimCmnIpMRouteExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 21),
    _FsPimCmnIpMRouteExpiryTime_Type()
)
fsPimCmnIpMRouteExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteExpiryTime.setStatus("current")
_FsPimCmnIpMRouteDifferentInIfPackets_Type = Counter32
_FsPimCmnIpMRouteDifferentInIfPackets_Object = MibTableColumn
fsPimCmnIpMRouteDifferentInIfPackets = _FsPimCmnIpMRouteDifferentInIfPackets_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 22),
    _FsPimCmnIpMRouteDifferentInIfPackets_Type()
)
fsPimCmnIpMRouteDifferentInIfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteDifferentInIfPackets.setStatus("current")
_FsPimCmnIpMRouteOctets_Type = Counter32
_FsPimCmnIpMRouteOctets_Object = MibTableColumn
fsPimCmnIpMRouteOctets = _FsPimCmnIpMRouteOctets_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 23),
    _FsPimCmnIpMRouteOctets_Type()
)
fsPimCmnIpMRouteOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteOctets.setStatus("current")
_FsPimCmnIpMRouteProtocol_Type = IANAipMRouteProtocol
_FsPimCmnIpMRouteProtocol_Object = MibTableColumn
fsPimCmnIpMRouteProtocol = _FsPimCmnIpMRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 24),
    _FsPimCmnIpMRouteProtocol_Type()
)
fsPimCmnIpMRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteProtocol.setStatus("current")
_FsPimCmnIpMRouteRtProto_Type = IANAipRouteProtocol
_FsPimCmnIpMRouteRtProto_Object = MibTableColumn
fsPimCmnIpMRouteRtProto = _FsPimCmnIpMRouteRtProto_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 25),
    _FsPimCmnIpMRouteRtProto_Type()
)
fsPimCmnIpMRouteRtProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteRtProto.setStatus("current")
_FsPimCmnIpMRouteRtAddress_Type = InetAddress
_FsPimCmnIpMRouteRtAddress_Object = MibTableColumn
fsPimCmnIpMRouteRtAddress = _FsPimCmnIpMRouteRtAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 26),
    _FsPimCmnIpMRouteRtAddress_Type()
)
fsPimCmnIpMRouteRtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteRtAddress.setStatus("current")
_FsPimCmnIpMRouteRtMasklen_Type = Integer32
_FsPimCmnIpMRouteRtMasklen_Object = MibTableColumn
fsPimCmnIpMRouteRtMasklen = _FsPimCmnIpMRouteRtMasklen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 27),
    _FsPimCmnIpMRouteRtMasklen_Type()
)
fsPimCmnIpMRouteRtMasklen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteRtMasklen.setStatus("current")


class _FsPimCmnIpMRouteRtType_Type(Integer32):
    """Custom type fsPimCmnIpMRouteRtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2))
    )


_FsPimCmnIpMRouteRtType_Type.__name__ = "Integer32"
_FsPimCmnIpMRouteRtType_Object = MibTableColumn
fsPimCmnIpMRouteRtType = _FsPimCmnIpMRouteRtType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 28),
    _FsPimCmnIpMRouteRtType_Type()
)
fsPimCmnIpMRouteRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteRtType.setStatus("current")
_FsPimCmnIpMRouteHCOctets_Type = Counter64
_FsPimCmnIpMRouteHCOctets_Object = MibTableColumn
fsPimCmnIpMRouteHCOctets = _FsPimCmnIpMRouteHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 29),
    _FsPimCmnIpMRouteHCOctets_Type()
)
fsPimCmnIpMRouteHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteHCOctets.setStatus("current")
_FsPimCmnIpMRouteOIfList_Type = PortList
_FsPimCmnIpMRouteOIfList_Object = MibTableColumn
fsPimCmnIpMRouteOIfList = _FsPimCmnIpMRouteOIfList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 30),
    _FsPimCmnIpMRouteOIfList_Type()
)
fsPimCmnIpMRouteOIfList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteOIfList.setStatus("current")
_FsPimCmnIpMRouteRPFVectorAddr_Type = InetAddress
_FsPimCmnIpMRouteRPFVectorAddr_Object = MibTableColumn
fsPimCmnIpMRouteRPFVectorAddr = _FsPimCmnIpMRouteRPFVectorAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 31),
    _FsPimCmnIpMRouteRPFVectorAddr_Type()
)
fsPimCmnIpMRouteRPFVectorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteRPFVectorAddr.setStatus("current")


class _FsPimCmnIpMRoutePimMode_Type(Integer32):
    """Custom type fsPimCmnIpMRoutePimMode based on Integer32"""
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
        *(("dm", 1),
          ("sm", 2),
          ("ssm", 3),
          ("bidir", 4))
    )


_FsPimCmnIpMRoutePimMode_Type.__name__ = "Integer32"
_FsPimCmnIpMRoutePimMode_Object = MibTableColumn
fsPimCmnIpMRoutePimMode = _FsPimCmnIpMRoutePimMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 3, 1, 32),
    _FsPimCmnIpMRoutePimMode_Type()
)
fsPimCmnIpMRoutePimMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRoutePimMode.setStatus("current")
_FsPimCmnIpMRouteNextHopTable_Object = MibTable
fsPimCmnIpMRouteNextHopTable = _FsPimCmnIpMRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 4)
)
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteNextHopTable.setStatus("current")
_FsPimCmnIpMRouteNextHopEntry_Object = MibTableRow
fsPimCmnIpMRouteNextHopEntry = _FsPimCmnIpMRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 4, 1)
)
fsPimCmnIpMRouteNextHopEntry.setIndexNames(
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpMRouteNextHopCompId"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpMRouteNextHopAddrType"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpMRouteNextHopGroup"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpMRouteNextHopSource"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpMRouteNextHopSourceMasklen"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpMRouteNextHopIfIndex"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpMRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteNextHopEntry.setStatus("current")


class _FsPimCmnIpMRouteNextHopCompId_Type(Integer32):
    """Custom type fsPimCmnIpMRouteNextHopCompId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimCmnIpMRouteNextHopCompId_Type.__name__ = "Integer32"
_FsPimCmnIpMRouteNextHopCompId_Object = MibTableColumn
fsPimCmnIpMRouteNextHopCompId = _FsPimCmnIpMRouteNextHopCompId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 4, 1, 1),
    _FsPimCmnIpMRouteNextHopCompId_Type()
)
fsPimCmnIpMRouteNextHopCompId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteNextHopCompId.setStatus("current")
_FsPimCmnIpMRouteNextHopAddrType_Type = InetAddressType
_FsPimCmnIpMRouteNextHopAddrType_Object = MibTableColumn
fsPimCmnIpMRouteNextHopAddrType = _FsPimCmnIpMRouteNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 4, 1, 2),
    _FsPimCmnIpMRouteNextHopAddrType_Type()
)
fsPimCmnIpMRouteNextHopAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteNextHopAddrType.setStatus("current")
_FsPimCmnIpMRouteNextHopGroup_Type = InetAddress
_FsPimCmnIpMRouteNextHopGroup_Object = MibTableColumn
fsPimCmnIpMRouteNextHopGroup = _FsPimCmnIpMRouteNextHopGroup_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 4, 1, 3),
    _FsPimCmnIpMRouteNextHopGroup_Type()
)
fsPimCmnIpMRouteNextHopGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteNextHopGroup.setStatus("current")
_FsPimCmnIpMRouteNextHopSource_Type = InetAddress
_FsPimCmnIpMRouteNextHopSource_Object = MibTableColumn
fsPimCmnIpMRouteNextHopSource = _FsPimCmnIpMRouteNextHopSource_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 4, 1, 4),
    _FsPimCmnIpMRouteNextHopSource_Type()
)
fsPimCmnIpMRouteNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteNextHopSource.setStatus("current")


class _FsPimCmnIpMRouteNextHopSourceMasklen_Type(Integer32):
    """Custom type fsPimCmnIpMRouteNextHopSourceMasklen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsPimCmnIpMRouteNextHopSourceMasklen_Type.__name__ = "Integer32"
_FsPimCmnIpMRouteNextHopSourceMasklen_Object = MibTableColumn
fsPimCmnIpMRouteNextHopSourceMasklen = _FsPimCmnIpMRouteNextHopSourceMasklen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 4, 1, 5),
    _FsPimCmnIpMRouteNextHopSourceMasklen_Type()
)
fsPimCmnIpMRouteNextHopSourceMasklen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteNextHopSourceMasklen.setStatus("current")


class _FsPimCmnIpMRouteNextHopIfIndex_Type(Integer32):
    """Custom type fsPimCmnIpMRouteNextHopIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPimCmnIpMRouteNextHopIfIndex_Type.__name__ = "Integer32"
_FsPimCmnIpMRouteNextHopIfIndex_Object = MibTableColumn
fsPimCmnIpMRouteNextHopIfIndex = _FsPimCmnIpMRouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 4, 1, 6),
    _FsPimCmnIpMRouteNextHopIfIndex_Type()
)
fsPimCmnIpMRouteNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteNextHopIfIndex.setStatus("current")
_FsPimCmnIpMRouteNextHopAddress_Type = InetAddress
_FsPimCmnIpMRouteNextHopAddress_Object = MibTableColumn
fsPimCmnIpMRouteNextHopAddress = _FsPimCmnIpMRouteNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 4, 1, 7),
    _FsPimCmnIpMRouteNextHopAddress_Type()
)
fsPimCmnIpMRouteNextHopAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteNextHopAddress.setStatus("current")


class _FsPimCmnIpMRouteNextHopPruneReason_Type(Integer32):
    """Custom type fsPimCmnIpMRouteNextHopPruneReason based on Integer32"""
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
        *(("forwarding", 0),
          ("other", 1),
          ("prune", 2),
          ("assert", 3))
    )


_FsPimCmnIpMRouteNextHopPruneReason_Type.__name__ = "Integer32"
_FsPimCmnIpMRouteNextHopPruneReason_Object = MibTableColumn
fsPimCmnIpMRouteNextHopPruneReason = _FsPimCmnIpMRouteNextHopPruneReason_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 4, 1, 8),
    _FsPimCmnIpMRouteNextHopPruneReason_Type()
)
fsPimCmnIpMRouteNextHopPruneReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteNextHopPruneReason.setStatus("current")


class _FsPimCmnIpMRouteNextHopState_Type(Integer32):
    """Custom type fsPimCmnIpMRouteNextHopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pruned", 1),
          ("forwarding", 2))
    )


_FsPimCmnIpMRouteNextHopState_Type.__name__ = "Integer32"
_FsPimCmnIpMRouteNextHopState_Object = MibTableColumn
fsPimCmnIpMRouteNextHopState = _FsPimCmnIpMRouteNextHopState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 4, 1, 9),
    _FsPimCmnIpMRouteNextHopState_Type()
)
fsPimCmnIpMRouteNextHopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteNextHopState.setStatus("current")
_FsPimCmnIpMRouteNextHopUpTime_Type = TimeTicks
_FsPimCmnIpMRouteNextHopUpTime_Object = MibTableColumn
fsPimCmnIpMRouteNextHopUpTime = _FsPimCmnIpMRouteNextHopUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 4, 1, 10),
    _FsPimCmnIpMRouteNextHopUpTime_Type()
)
fsPimCmnIpMRouteNextHopUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteNextHopUpTime.setStatus("current")
_FsPimCmnIpMRouteNextHopExpiryTime_Type = TimeTicks
_FsPimCmnIpMRouteNextHopExpiryTime_Object = MibTableColumn
fsPimCmnIpMRouteNextHopExpiryTime = _FsPimCmnIpMRouteNextHopExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 4, 1, 11),
    _FsPimCmnIpMRouteNextHopExpiryTime_Type()
)
fsPimCmnIpMRouteNextHopExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteNextHopExpiryTime.setStatus("current")
_FsPimCmnIpMRouteNextHopProtocol_Type = IANAipMRouteProtocol
_FsPimCmnIpMRouteNextHopProtocol_Object = MibTableColumn
fsPimCmnIpMRouteNextHopProtocol = _FsPimCmnIpMRouteNextHopProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 4, 1, 12),
    _FsPimCmnIpMRouteNextHopProtocol_Type()
)
fsPimCmnIpMRouteNextHopProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteNextHopProtocol.setStatus("current")
_FsPimCmnIpMRouteNextHopPkts_Type = Counter32
_FsPimCmnIpMRouteNextHopPkts_Object = MibTableColumn
fsPimCmnIpMRouteNextHopPkts = _FsPimCmnIpMRouteNextHopPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 4, 1, 13),
    _FsPimCmnIpMRouteNextHopPkts_Type()
)
fsPimCmnIpMRouteNextHopPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpMRouteNextHopPkts.setStatus("current")
_FsPimCmnCandidateRPTable_Object = MibTable
fsPimCmnCandidateRPTable = _FsPimCmnCandidateRPTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 6)
)
if mibBuilder.loadTexts:
    fsPimCmnCandidateRPTable.setStatus("current")
_FsPimCmnCandidateRPEntry_Object = MibTableRow
fsPimCmnCandidateRPEntry = _FsPimCmnCandidateRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 6, 1)
)
fsPimCmnCandidateRPEntry.setIndexNames(
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnCandidateRPCompId"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnCandidateRPAddrType"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnCandidateRPGroupAddress"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnCandidateRPGroupMasklen"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnCandidateRPAddress"),
)
if mibBuilder.loadTexts:
    fsPimCmnCandidateRPEntry.setStatus("current")


class _FsPimCmnCandidateRPCompId_Type(Integer32):
    """Custom type fsPimCmnCandidateRPCompId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimCmnCandidateRPCompId_Type.__name__ = "Integer32"
_FsPimCmnCandidateRPCompId_Object = MibTableColumn
fsPimCmnCandidateRPCompId = _FsPimCmnCandidateRPCompId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 6, 1, 1),
    _FsPimCmnCandidateRPCompId_Type()
)
fsPimCmnCandidateRPCompId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnCandidateRPCompId.setStatus("current")
_FsPimCmnCandidateRPAddrType_Type = InetAddressType
_FsPimCmnCandidateRPAddrType_Object = MibTableColumn
fsPimCmnCandidateRPAddrType = _FsPimCmnCandidateRPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 6, 1, 2),
    _FsPimCmnCandidateRPAddrType_Type()
)
fsPimCmnCandidateRPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnCandidateRPAddrType.setStatus("current")
_FsPimCmnCandidateRPGroupAddress_Type = InetAddress
_FsPimCmnCandidateRPGroupAddress_Object = MibTableColumn
fsPimCmnCandidateRPGroupAddress = _FsPimCmnCandidateRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 6, 1, 3),
    _FsPimCmnCandidateRPGroupAddress_Type()
)
fsPimCmnCandidateRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnCandidateRPGroupAddress.setStatus("current")


class _FsPimCmnCandidateRPGroupMasklen_Type(Integer32):
    """Custom type fsPimCmnCandidateRPGroupMasklen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsPimCmnCandidateRPGroupMasklen_Type.__name__ = "Integer32"
_FsPimCmnCandidateRPGroupMasklen_Object = MibTableColumn
fsPimCmnCandidateRPGroupMasklen = _FsPimCmnCandidateRPGroupMasklen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 6, 1, 4),
    _FsPimCmnCandidateRPGroupMasklen_Type()
)
fsPimCmnCandidateRPGroupMasklen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnCandidateRPGroupMasklen.setStatus("current")
_FsPimCmnCandidateRPAddress_Type = InetAddress
_FsPimCmnCandidateRPAddress_Object = MibTableColumn
fsPimCmnCandidateRPAddress = _FsPimCmnCandidateRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 6, 1, 5),
    _FsPimCmnCandidateRPAddress_Type()
)
fsPimCmnCandidateRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnCandidateRPAddress.setStatus("current")


class _FsPimCmnCandidateRPPriority_Type(Integer32):
    """Custom type fsPimCmnCandidateRPPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPimCmnCandidateRPPriority_Type.__name__ = "Integer32"
_FsPimCmnCandidateRPPriority_Object = MibTableColumn
fsPimCmnCandidateRPPriority = _FsPimCmnCandidateRPPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 6, 1, 6),
    _FsPimCmnCandidateRPPriority_Type()
)
fsPimCmnCandidateRPPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnCandidateRPPriority.setStatus("current")
_FsPimCmnCandidateRPRowStatus_Type = RowStatus
_FsPimCmnCandidateRPRowStatus_Object = MibTableColumn
fsPimCmnCandidateRPRowStatus = _FsPimCmnCandidateRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 6, 1, 7),
    _FsPimCmnCandidateRPRowStatus_Type()
)
fsPimCmnCandidateRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimCmnCandidateRPRowStatus.setStatus("current")


class _FsPimCmnCandidateRPPimMode_Type(Integer32):
    """Custom type fsPimCmnCandidateRPPimMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sm", 2),
          ("bidir", 4))
    )


_FsPimCmnCandidateRPPimMode_Type.__name__ = "Integer32"
_FsPimCmnCandidateRPPimMode_Object = MibTableColumn
fsPimCmnCandidateRPPimMode = _FsPimCmnCandidateRPPimMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 6, 1, 8),
    _FsPimCmnCandidateRPPimMode_Type()
)
fsPimCmnCandidateRPPimMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnCandidateRPPimMode.setStatus("current")
_FsPimCmnStaticRPSetTable_Object = MibTable
fsPimCmnStaticRPSetTable = _FsPimCmnStaticRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 7)
)
if mibBuilder.loadTexts:
    fsPimCmnStaticRPSetTable.setStatus("current")
_FsPimCmnStaticRPSetEntry_Object = MibTableRow
fsPimCmnStaticRPSetEntry = _FsPimCmnStaticRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 7, 1)
)
fsPimCmnStaticRPSetEntry.setIndexNames(
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnStaticRPSetCompId"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnStaticRPAddrType"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnStaticRPSetGroupAddress"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnStaticRPSetGroupMasklen"),
)
if mibBuilder.loadTexts:
    fsPimCmnStaticRPSetEntry.setStatus("current")


class _FsPimCmnStaticRPSetCompId_Type(Integer32):
    """Custom type fsPimCmnStaticRPSetCompId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimCmnStaticRPSetCompId_Type.__name__ = "Integer32"
_FsPimCmnStaticRPSetCompId_Object = MibTableColumn
fsPimCmnStaticRPSetCompId = _FsPimCmnStaticRPSetCompId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 7, 1, 1),
    _FsPimCmnStaticRPSetCompId_Type()
)
fsPimCmnStaticRPSetCompId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnStaticRPSetCompId.setStatus("current")
_FsPimCmnStaticRPAddrType_Type = InetAddressType
_FsPimCmnStaticRPAddrType_Object = MibTableColumn
fsPimCmnStaticRPAddrType = _FsPimCmnStaticRPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 7, 1, 2),
    _FsPimCmnStaticRPAddrType_Type()
)
fsPimCmnStaticRPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnStaticRPAddrType.setStatus("current")
_FsPimCmnStaticRPSetGroupAddress_Type = InetAddress
_FsPimCmnStaticRPSetGroupAddress_Object = MibTableColumn
fsPimCmnStaticRPSetGroupAddress = _FsPimCmnStaticRPSetGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 7, 1, 3),
    _FsPimCmnStaticRPSetGroupAddress_Type()
)
fsPimCmnStaticRPSetGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnStaticRPSetGroupAddress.setStatus("current")


class _FsPimCmnStaticRPSetGroupMasklen_Type(Integer32):
    """Custom type fsPimCmnStaticRPSetGroupMasklen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsPimCmnStaticRPSetGroupMasklen_Type.__name__ = "Integer32"
_FsPimCmnStaticRPSetGroupMasklen_Object = MibTableColumn
fsPimCmnStaticRPSetGroupMasklen = _FsPimCmnStaticRPSetGroupMasklen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 7, 1, 4),
    _FsPimCmnStaticRPSetGroupMasklen_Type()
)
fsPimCmnStaticRPSetGroupMasklen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnStaticRPSetGroupMasklen.setStatus("current")
_FsPimCmnStaticRPAddress_Type = InetAddress
_FsPimCmnStaticRPAddress_Object = MibTableColumn
fsPimCmnStaticRPAddress = _FsPimCmnStaticRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 7, 1, 5),
    _FsPimCmnStaticRPAddress_Type()
)
fsPimCmnStaticRPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimCmnStaticRPAddress.setStatus("current")
_FsPimCmnStaticRPRowStatus_Type = RowStatus
_FsPimCmnStaticRPRowStatus_Object = MibTableColumn
fsPimCmnStaticRPRowStatus = _FsPimCmnStaticRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 7, 1, 6),
    _FsPimCmnStaticRPRowStatus_Type()
)
fsPimCmnStaticRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimCmnStaticRPRowStatus.setStatus("current")


class _FsPimCmnStaticRPEmbdFlag_Type(Integer32):
    """Custom type fsPimCmnStaticRPEmbdFlag based on Integer32"""
    defaultValue = 0

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


_FsPimCmnStaticRPEmbdFlag_Type.__name__ = "Integer32"
_FsPimCmnStaticRPEmbdFlag_Object = MibTableColumn
fsPimCmnStaticRPEmbdFlag = _FsPimCmnStaticRPEmbdFlag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 7, 1, 7),
    _FsPimCmnStaticRPEmbdFlag_Type()
)
fsPimCmnStaticRPEmbdFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnStaticRPEmbdFlag.setStatus("current")


class _FsPimCmnStaticRPPimMode_Type(Integer32):
    """Custom type fsPimCmnStaticRPPimMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sm", 2),
          ("bidir", 4))
    )


_FsPimCmnStaticRPPimMode_Type.__name__ = "Integer32"
_FsPimCmnStaticRPPimMode_Object = MibTableColumn
fsPimCmnStaticRPPimMode = _FsPimCmnStaticRPPimMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 7, 1, 8),
    _FsPimCmnStaticRPPimMode_Type()
)
fsPimCmnStaticRPPimMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnStaticRPPimMode.setStatus("current")
_FsPimCmnComponentModeTable_Object = MibTable
fsPimCmnComponentModeTable = _FsPimCmnComponentModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 8)
)
if mibBuilder.loadTexts:
    fsPimCmnComponentModeTable.setStatus("current")
_FsPimCmnComponentModeEntry_Object = MibTableRow
fsPimCmnComponentModeEntry = _FsPimCmnComponentModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 8, 1)
)
fsPimCmnComponentModeEntry.setIndexNames(
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnComponentId"),
)
if mibBuilder.loadTexts:
    fsPimCmnComponentModeEntry.setStatus("current")


class _FsPimCmnComponentId_Type(Integer32):
    """Custom type fsPimCmnComponentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimCmnComponentId_Type.__name__ = "Integer32"
_FsPimCmnComponentId_Object = MibTableColumn
fsPimCmnComponentId = _FsPimCmnComponentId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 8, 1, 1),
    _FsPimCmnComponentId_Type()
)
fsPimCmnComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnComponentId.setStatus("current")


class _FsPimCmnComponentMode_Type(Integer32):
    """Custom type fsPimCmnComponentMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dense", 1),
          ("sparse", 2))
    )


_FsPimCmnComponentMode_Type.__name__ = "Integer32"
_FsPimCmnComponentMode_Object = MibTableColumn
fsPimCmnComponentMode = _FsPimCmnComponentMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 8, 1, 2),
    _FsPimCmnComponentMode_Type()
)
fsPimCmnComponentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnComponentMode.setStatus("current")


class _FsPimCmnCompGraftRetryCount_Type(Integer32):
    """Custom type fsPimCmnCompGraftRetryCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPimCmnCompGraftRetryCount_Type.__name__ = "Integer32"
_FsPimCmnCompGraftRetryCount_Object = MibTableColumn
fsPimCmnCompGraftRetryCount = _FsPimCmnCompGraftRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 8, 1, 3),
    _FsPimCmnCompGraftRetryCount_Type()
)
fsPimCmnCompGraftRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnCompGraftRetryCount.setStatus("current")
_FsPimCmnRegChkSumCfgTable_Object = MibTable
fsPimCmnRegChkSumCfgTable = _FsPimCmnRegChkSumCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 9)
)
if mibBuilder.loadTexts:
    fsPimCmnRegChkSumCfgTable.setStatus("current")
_FsPimCmnRegChkSumCfgEntry_Object = MibTableRow
fsPimCmnRegChkSumCfgEntry = _FsPimCmnRegChkSumCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 9, 1)
)
fsPimCmnRegChkSumCfgEntry.setIndexNames(
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnRegChkSumTblCompId"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnRegChkSumTblRPAddrType"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnRegChkSumTblRPAddress"),
)
if mibBuilder.loadTexts:
    fsPimCmnRegChkSumCfgEntry.setStatus("current")


class _FsPimCmnRegChkSumTblCompId_Type(Integer32):
    """Custom type fsPimCmnRegChkSumTblCompId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimCmnRegChkSumTblCompId_Type.__name__ = "Integer32"
_FsPimCmnRegChkSumTblCompId_Object = MibTableColumn
fsPimCmnRegChkSumTblCompId = _FsPimCmnRegChkSumTblCompId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 9, 1, 1),
    _FsPimCmnRegChkSumTblCompId_Type()
)
fsPimCmnRegChkSumTblCompId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnRegChkSumTblCompId.setStatus("current")
_FsPimCmnRegChkSumTblRPAddrType_Type = InetAddressType
_FsPimCmnRegChkSumTblRPAddrType_Object = MibTableColumn
fsPimCmnRegChkSumTblRPAddrType = _FsPimCmnRegChkSumTblRPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 9, 1, 2),
    _FsPimCmnRegChkSumTblRPAddrType_Type()
)
fsPimCmnRegChkSumTblRPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnRegChkSumTblRPAddrType.setStatus("current")
_FsPimCmnRegChkSumTblRPAddress_Type = InetAddress
_FsPimCmnRegChkSumTblRPAddress_Object = MibTableColumn
fsPimCmnRegChkSumTblRPAddress = _FsPimCmnRegChkSumTblRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 9, 1, 3),
    _FsPimCmnRegChkSumTblRPAddress_Type()
)
fsPimCmnRegChkSumTblRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnRegChkSumTblRPAddress.setStatus("current")


class _FsPimCmnRPChkSumStatus_Type(Integer32):
    """Custom type fsPimCmnRPChkSumStatus based on Integer32"""
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


_FsPimCmnRPChkSumStatus_Type.__name__ = "Integer32"
_FsPimCmnRPChkSumStatus_Object = MibTableColumn
fsPimCmnRPChkSumStatus = _FsPimCmnRPChkSumStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 9, 1, 4),
    _FsPimCmnRPChkSumStatus_Type()
)
fsPimCmnRPChkSumStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCmnRPChkSumStatus.setStatus("current")
_FsPimCmnDFTable_Object = MibTable
fsPimCmnDFTable = _FsPimCmnDFTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 10)
)
if mibBuilder.loadTexts:
    fsPimCmnDFTable.setStatus("current")
_FsPimCmnDFEntry_Object = MibTableRow
fsPimCmnDFEntry = _FsPimCmnDFEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 10, 1)
)
fsPimCmnDFEntry.setIndexNames(
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnDFIfAddrType"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnDFElectedRP"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnDFIfIndex"),
)
if mibBuilder.loadTexts:
    fsPimCmnDFEntry.setStatus("current")
_FsPimCmnDFIfAddrType_Type = InetAddressType
_FsPimCmnDFIfAddrType_Object = MibTableColumn
fsPimCmnDFIfAddrType = _FsPimCmnDFIfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 10, 1, 1),
    _FsPimCmnDFIfAddrType_Type()
)
fsPimCmnDFIfAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnDFIfAddrType.setStatus("current")
_FsPimCmnDFElectedRP_Type = InetAddress
_FsPimCmnDFElectedRP_Object = MibTableColumn
fsPimCmnDFElectedRP = _FsPimCmnDFElectedRP_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 10, 1, 2),
    _FsPimCmnDFElectedRP_Type()
)
fsPimCmnDFElectedRP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnDFElectedRP.setStatus("current")


class _FsPimCmnDFIfIndex_Type(Integer32):
    """Custom type fsPimCmnDFIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPimCmnDFIfIndex_Type.__name__ = "Integer32"
_FsPimCmnDFIfIndex_Object = MibTableColumn
fsPimCmnDFIfIndex = _FsPimCmnDFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 10, 1, 3),
    _FsPimCmnDFIfIndex_Type()
)
fsPimCmnDFIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnDFIfIndex.setStatus("current")


class _FsPimCmnDFState_Type(Integer32):
    """Custom type fsPimCmnDFState based on Integer32"""
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
        *(("offer", 1),
          ("winner", 2),
          ("backoff", 3),
          ("lose", 4))
    )


_FsPimCmnDFState_Type.__name__ = "Integer32"
_FsPimCmnDFState_Object = MibTableColumn
fsPimCmnDFState = _FsPimCmnDFState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 10, 1, 4),
    _FsPimCmnDFState_Type()
)
fsPimCmnDFState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnDFState.setStatus("current")
_FsPimCmnDFWinnerAddr_Type = InetAddress
_FsPimCmnDFWinnerAddr_Object = MibTableColumn
fsPimCmnDFWinnerAddr = _FsPimCmnDFWinnerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 10, 1, 5),
    _FsPimCmnDFWinnerAddr_Type()
)
fsPimCmnDFWinnerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnDFWinnerAddr.setStatus("current")
_FsPimCmnDFWinnerUptime_Type = TimeTicks
_FsPimCmnDFWinnerUptime_Object = MibTableColumn
fsPimCmnDFWinnerUptime = _FsPimCmnDFWinnerUptime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 10, 1, 6),
    _FsPimCmnDFWinnerUptime_Type()
)
fsPimCmnDFWinnerUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnDFWinnerUptime.setStatus("current")
_FsPimCmnDFElectionStateTimer_Type = TimeTicks
_FsPimCmnDFElectionStateTimer_Object = MibTableColumn
fsPimCmnDFElectionStateTimer = _FsPimCmnDFElectionStateTimer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 10, 1, 7),
    _FsPimCmnDFElectionStateTimer_Type()
)
fsPimCmnDFElectionStateTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnDFElectionStateTimer.setStatus("current")
_FsPimCmnDFWinnerMetric_Type = Unsigned32
_FsPimCmnDFWinnerMetric_Object = MibTableColumn
fsPimCmnDFWinnerMetric = _FsPimCmnDFWinnerMetric_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 10, 1, 8),
    _FsPimCmnDFWinnerMetric_Type()
)
fsPimCmnDFWinnerMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnDFWinnerMetric.setStatus("current")
_FsPimCmnDFWinnerMetricPref_Type = Unsigned32
_FsPimCmnDFWinnerMetricPref_Object = MibTableColumn
fsPimCmnDFWinnerMetricPref = _FsPimCmnDFWinnerMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 10, 1, 9),
    _FsPimCmnDFWinnerMetricPref_Type()
)
fsPimCmnDFWinnerMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnDFWinnerMetricPref.setStatus("current")


class _FsPimCmnDFMessageCount_Type(Integer32):
    """Custom type fsPimCmnDFMessageCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPimCmnDFMessageCount_Type.__name__ = "Integer32"
_FsPimCmnDFMessageCount_Object = MibTableColumn
fsPimCmnDFMessageCount = _FsPimCmnDFMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 10, 1, 10),
    _FsPimCmnDFMessageCount_Type()
)
fsPimCmnDFMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnDFMessageCount.setStatus("current")
_FsPimCmnElectedRPTable_Object = MibTable
fsPimCmnElectedRPTable = _FsPimCmnElectedRPTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 11)
)
if mibBuilder.loadTexts:
    fsPimCmnElectedRPTable.setStatus("current")
_FsPimCmnElectedRPEntry_Object = MibTableRow
fsPimCmnElectedRPEntry = _FsPimCmnElectedRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 11, 1)
)
fsPimCmnElectedRPEntry.setIndexNames(
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnElectedRPCompId"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnElectedRPAddrType"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnElectedRPGroupAddress"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnElectedRPGroupMasklen"),
)
if mibBuilder.loadTexts:
    fsPimCmnElectedRPEntry.setStatus("current")


class _FsPimCmnElectedRPCompId_Type(Integer32):
    """Custom type fsPimCmnElectedRPCompId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimCmnElectedRPCompId_Type.__name__ = "Integer32"
_FsPimCmnElectedRPCompId_Object = MibTableColumn
fsPimCmnElectedRPCompId = _FsPimCmnElectedRPCompId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 11, 1, 1),
    _FsPimCmnElectedRPCompId_Type()
)
fsPimCmnElectedRPCompId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnElectedRPCompId.setStatus("current")
_FsPimCmnElectedRPAddrType_Type = InetAddressType
_FsPimCmnElectedRPAddrType_Object = MibTableColumn
fsPimCmnElectedRPAddrType = _FsPimCmnElectedRPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 11, 1, 2),
    _FsPimCmnElectedRPAddrType_Type()
)
fsPimCmnElectedRPAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnElectedRPAddrType.setStatus("current")
_FsPimCmnElectedRPGroupAddress_Type = InetAddress
_FsPimCmnElectedRPGroupAddress_Object = MibTableColumn
fsPimCmnElectedRPGroupAddress = _FsPimCmnElectedRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 11, 1, 3),
    _FsPimCmnElectedRPGroupAddress_Type()
)
fsPimCmnElectedRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnElectedRPGroupAddress.setStatus("current")


class _FsPimCmnElectedRPGroupMasklen_Type(Integer32):
    """Custom type fsPimCmnElectedRPGroupMasklen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsPimCmnElectedRPGroupMasklen_Type.__name__ = "Integer32"
_FsPimCmnElectedRPGroupMasklen_Object = MibTableColumn
fsPimCmnElectedRPGroupMasklen = _FsPimCmnElectedRPGroupMasklen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 11, 1, 4),
    _FsPimCmnElectedRPGroupMasklen_Type()
)
fsPimCmnElectedRPGroupMasklen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnElectedRPGroupMasklen.setStatus("current")
_FsPimCmnElectedRPAddress_Type = InetAddress
_FsPimCmnElectedRPAddress_Object = MibTableColumn
fsPimCmnElectedRPAddress = _FsPimCmnElectedRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 11, 1, 5),
    _FsPimCmnElectedRPAddress_Type()
)
fsPimCmnElectedRPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnElectedRPAddress.setStatus("current")


class _FsPimCmnElectedRPPriority_Type(Integer32):
    """Custom type fsPimCmnElectedRPPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPimCmnElectedRPPriority_Type.__name__ = "Integer32"
_FsPimCmnElectedRPPriority_Object = MibTableColumn
fsPimCmnElectedRPPriority = _FsPimCmnElectedRPPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 11, 1, 6),
    _FsPimCmnElectedRPPriority_Type()
)
fsPimCmnElectedRPPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnElectedRPPriority.setStatus("current")


class _FsPimCmnElectedRPHoldTime_Type(Integer32):
    """Custom type fsPimCmnElectedRPHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPimCmnElectedRPHoldTime_Type.__name__ = "Integer32"
_FsPimCmnElectedRPHoldTime_Object = MibTableColumn
fsPimCmnElectedRPHoldTime = _FsPimCmnElectedRPHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 11, 1, 7),
    _FsPimCmnElectedRPHoldTime_Type()
)
fsPimCmnElectedRPHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnElectedRPHoldTime.setStatus("current")


class _FsPimCmnElectedRPUpTime_Type(Integer32):
    """Custom type fsPimCmnElectedRPUpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPimCmnElectedRPUpTime_Type.__name__ = "Integer32"
_FsPimCmnElectedRPUpTime_Object = MibTableColumn
fsPimCmnElectedRPUpTime = _FsPimCmnElectedRPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 11, 1, 8),
    _FsPimCmnElectedRPUpTime_Type()
)
fsPimCmnElectedRPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnElectedRPUpTime.setStatus("current")
_FsPimCmnNeighborExtTable_Object = MibTable
fsPimCmnNeighborExtTable = _FsPimCmnNeighborExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 12)
)
if mibBuilder.loadTexts:
    fsPimCmnNeighborExtTable.setStatus("current")
_FsPimCmnNeighborExtEntry_Object = MibTableRow
fsPimCmnNeighborExtEntry = _FsPimCmnNeighborExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 12, 1)
)
fsPimCmnNeighborExtEntry.setIndexNames(
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnNeighborExtIfIndex"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnNeighborExtAddrType"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnNeighborExtAddress"),
)
if mibBuilder.loadTexts:
    fsPimCmnNeighborExtEntry.setStatus("current")
_FsPimCmnNeighborExtIfIndex_Type = Integer32
_FsPimCmnNeighborExtIfIndex_Object = MibTableColumn
fsPimCmnNeighborExtIfIndex = _FsPimCmnNeighborExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 12, 1, 1),
    _FsPimCmnNeighborExtIfIndex_Type()
)
fsPimCmnNeighborExtIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnNeighborExtIfIndex.setStatus("current")
_FsPimCmnNeighborExtAddrType_Type = InetAddressType
_FsPimCmnNeighborExtAddrType_Object = MibTableColumn
fsPimCmnNeighborExtAddrType = _FsPimCmnNeighborExtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 12, 1, 2),
    _FsPimCmnNeighborExtAddrType_Type()
)
fsPimCmnNeighborExtAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnNeighborExtAddrType.setStatus("current")
_FsPimCmnNeighborExtAddress_Type = InetAddress
_FsPimCmnNeighborExtAddress_Object = MibTableColumn
fsPimCmnNeighborExtAddress = _FsPimCmnNeighborExtAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 12, 1, 3),
    _FsPimCmnNeighborExtAddress_Type()
)
fsPimCmnNeighborExtAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnNeighborExtAddress.setStatus("current")
_FsPimCmnNeighborExtCompIdList_Type = CompList
_FsPimCmnNeighborExtCompIdList_Object = MibTableColumn
fsPimCmnNeighborExtCompIdList = _FsPimCmnNeighborExtCompIdList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 12, 1, 4),
    _FsPimCmnNeighborExtCompIdList_Type()
)
fsPimCmnNeighborExtCompIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborExtCompIdList.setStatus("current")
_FsPimCmnNeighborExtUpTime_Type = TimeTicks
_FsPimCmnNeighborExtUpTime_Object = MibTableColumn
fsPimCmnNeighborExtUpTime = _FsPimCmnNeighborExtUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 12, 1, 5),
    _FsPimCmnNeighborExtUpTime_Type()
)
fsPimCmnNeighborExtUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborExtUpTime.setStatus("current")
_FsPimCmnNeighborExtExpiryTime_Type = TimeTicks
_FsPimCmnNeighborExtExpiryTime_Object = MibTableColumn
fsPimCmnNeighborExtExpiryTime = _FsPimCmnNeighborExtExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 12, 1, 6),
    _FsPimCmnNeighborExtExpiryTime_Type()
)
fsPimCmnNeighborExtExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborExtExpiryTime.setStatus("current")
_FsPimCmnNeighborExtGenerationId_Type = Integer32
_FsPimCmnNeighborExtGenerationId_Object = MibTableColumn
fsPimCmnNeighborExtGenerationId = _FsPimCmnNeighborExtGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 12, 1, 7),
    _FsPimCmnNeighborExtGenerationId_Type()
)
fsPimCmnNeighborExtGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborExtGenerationId.setStatus("current")
_FsPimCmnNeighborExtLanDelay_Type = Integer32
_FsPimCmnNeighborExtLanDelay_Object = MibTableColumn
fsPimCmnNeighborExtLanDelay = _FsPimCmnNeighborExtLanDelay_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 12, 1, 8),
    _FsPimCmnNeighborExtLanDelay_Type()
)
fsPimCmnNeighborExtLanDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborExtLanDelay.setStatus("current")
_FsPimCmnNeighborExtDRPriority_Type = Unsigned32
_FsPimCmnNeighborExtDRPriority_Object = MibTableColumn
fsPimCmnNeighborExtDRPriority = _FsPimCmnNeighborExtDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 12, 1, 9),
    _FsPimCmnNeighborExtDRPriority_Type()
)
fsPimCmnNeighborExtDRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborExtDRPriority.setStatus("current")
_FsPimCmnNeighborExtOverrideInterval_Type = Integer32
_FsPimCmnNeighborExtOverrideInterval_Object = MibTableColumn
fsPimCmnNeighborExtOverrideInterval = _FsPimCmnNeighborExtOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 12, 1, 10),
    _FsPimCmnNeighborExtOverrideInterval_Type()
)
fsPimCmnNeighborExtOverrideInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborExtOverrideInterval.setStatus("current")
_FsPimCmnNeighborExtSRCapable_Type = TruthValue
_FsPimCmnNeighborExtSRCapable_Object = MibTableColumn
fsPimCmnNeighborExtSRCapable = _FsPimCmnNeighborExtSRCapable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 12, 1, 11),
    _FsPimCmnNeighborExtSRCapable_Type()
)
fsPimCmnNeighborExtSRCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborExtSRCapable.setStatus("current")
_FsPimCmnNeighborExtRPFCapable_Type = TruthValue
_FsPimCmnNeighborExtRPFCapable_Object = MibTableColumn
fsPimCmnNeighborExtRPFCapable = _FsPimCmnNeighborExtRPFCapable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 12, 1, 12),
    _FsPimCmnNeighborExtRPFCapable_Type()
)
fsPimCmnNeighborExtRPFCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborExtRPFCapable.setStatus("current")
_FsPimCmnNeighborExtBidirCapable_Type = TruthValue
_FsPimCmnNeighborExtBidirCapable_Object = MibTableColumn
fsPimCmnNeighborExtBidirCapable = _FsPimCmnNeighborExtBidirCapable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 12, 1, 13),
    _FsPimCmnNeighborExtBidirCapable_Type()
)
fsPimCmnNeighborExtBidirCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnNeighborExtBidirCapable.setStatus("current")
_FsPimCmnIpGenMRouteTable_Object = MibTable
fsPimCmnIpGenMRouteTable = _FsPimCmnIpGenMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13)
)
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteTable.setStatus("current")
_FsPimCmnIpGenMRouteEntry_Object = MibTableRow
fsPimCmnIpGenMRouteEntry = _FsPimCmnIpGenMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1)
)
fsPimCmnIpGenMRouteEntry.setIndexNames(
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpGenMRouteCompId"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpGenMRouteAddrType"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpGenMRouteGroup"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpGenMRouteGroupMasklen"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpGenMRouteSource"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpGenMRouteSourceMasklen"),
)
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteEntry.setStatus("current")


class _FsPimCmnIpGenMRouteCompId_Type(Integer32):
    """Custom type fsPimCmnIpGenMRouteCompId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimCmnIpGenMRouteCompId_Type.__name__ = "Integer32"
_FsPimCmnIpGenMRouteCompId_Object = MibTableColumn
fsPimCmnIpGenMRouteCompId = _FsPimCmnIpGenMRouteCompId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 1),
    _FsPimCmnIpGenMRouteCompId_Type()
)
fsPimCmnIpGenMRouteCompId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteCompId.setStatus("current")
_FsPimCmnIpGenMRouteAddrType_Type = InetAddressType
_FsPimCmnIpGenMRouteAddrType_Object = MibTableColumn
fsPimCmnIpGenMRouteAddrType = _FsPimCmnIpGenMRouteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 2),
    _FsPimCmnIpGenMRouteAddrType_Type()
)
fsPimCmnIpGenMRouteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteAddrType.setStatus("current")
_FsPimCmnIpGenMRouteGroup_Type = InetAddress
_FsPimCmnIpGenMRouteGroup_Object = MibTableColumn
fsPimCmnIpGenMRouteGroup = _FsPimCmnIpGenMRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 3),
    _FsPimCmnIpGenMRouteGroup_Type()
)
fsPimCmnIpGenMRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteGroup.setStatus("current")


class _FsPimCmnIpGenMRouteGroupMasklen_Type(Integer32):
    """Custom type fsPimCmnIpGenMRouteGroupMasklen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsPimCmnIpGenMRouteGroupMasklen_Type.__name__ = "Integer32"
_FsPimCmnIpGenMRouteGroupMasklen_Object = MibTableColumn
fsPimCmnIpGenMRouteGroupMasklen = _FsPimCmnIpGenMRouteGroupMasklen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 4),
    _FsPimCmnIpGenMRouteGroupMasklen_Type()
)
fsPimCmnIpGenMRouteGroupMasklen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteGroupMasklen.setStatus("current")
_FsPimCmnIpGenMRouteSource_Type = InetAddress
_FsPimCmnIpGenMRouteSource_Object = MibTableColumn
fsPimCmnIpGenMRouteSource = _FsPimCmnIpGenMRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 5),
    _FsPimCmnIpGenMRouteSource_Type()
)
fsPimCmnIpGenMRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteSource.setStatus("current")


class _FsPimCmnIpGenMRouteSourceMasklen_Type(Integer32):
    """Custom type fsPimCmnIpGenMRouteSourceMasklen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsPimCmnIpGenMRouteSourceMasklen_Type.__name__ = "Integer32"
_FsPimCmnIpGenMRouteSourceMasklen_Object = MibTableColumn
fsPimCmnIpGenMRouteSourceMasklen = _FsPimCmnIpGenMRouteSourceMasklen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 6),
    _FsPimCmnIpGenMRouteSourceMasklen_Type()
)
fsPimCmnIpGenMRouteSourceMasklen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteSourceMasklen.setStatus("current")
_FsPimCmnIpGenMRouteUpstreamNeighbor_Type = InetAddress
_FsPimCmnIpGenMRouteUpstreamNeighbor_Object = MibTableColumn
fsPimCmnIpGenMRouteUpstreamNeighbor = _FsPimCmnIpGenMRouteUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 7),
    _FsPimCmnIpGenMRouteUpstreamNeighbor_Type()
)
fsPimCmnIpGenMRouteUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteUpstreamNeighbor.setStatus("current")
_FsPimCmnIpGenMRouteInIfIndex_Type = Integer32
_FsPimCmnIpGenMRouteInIfIndex_Object = MibTableColumn
fsPimCmnIpGenMRouteInIfIndex = _FsPimCmnIpGenMRouteInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 8),
    _FsPimCmnIpGenMRouteInIfIndex_Type()
)
fsPimCmnIpGenMRouteInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteInIfIndex.setStatus("current")
_FsPimCmnIpGenMRouteUpTime_Type = TimeTicks
_FsPimCmnIpGenMRouteUpTime_Object = MibTableColumn
fsPimCmnIpGenMRouteUpTime = _FsPimCmnIpGenMRouteUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 9),
    _FsPimCmnIpGenMRouteUpTime_Type()
)
fsPimCmnIpGenMRouteUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteUpTime.setStatus("current")
_FsPimCmnIpGenMRoutePkts_Type = Counter32
_FsPimCmnIpGenMRoutePkts_Object = MibTableColumn
fsPimCmnIpGenMRoutePkts = _FsPimCmnIpGenMRoutePkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 10),
    _FsPimCmnIpGenMRoutePkts_Type()
)
fsPimCmnIpGenMRoutePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRoutePkts.setStatus("current")
_FsPimCmnIpGenMRouteUpstreamAssertTimer_Type = TimeTicks
_FsPimCmnIpGenMRouteUpstreamAssertTimer_Object = MibTableColumn
fsPimCmnIpGenMRouteUpstreamAssertTimer = _FsPimCmnIpGenMRouteUpstreamAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 11),
    _FsPimCmnIpGenMRouteUpstreamAssertTimer_Type()
)
fsPimCmnIpGenMRouteUpstreamAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteUpstreamAssertTimer.setStatus("current")
_FsPimCmnIpGenMRouteAssertMetric_Type = Integer32
_FsPimCmnIpGenMRouteAssertMetric_Object = MibTableColumn
fsPimCmnIpGenMRouteAssertMetric = _FsPimCmnIpGenMRouteAssertMetric_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 12),
    _FsPimCmnIpGenMRouteAssertMetric_Type()
)
fsPimCmnIpGenMRouteAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteAssertMetric.setStatus("current")
_FsPimCmnIpGenMRouteAssertMetricPref_Type = Integer32
_FsPimCmnIpGenMRouteAssertMetricPref_Object = MibTableColumn
fsPimCmnIpGenMRouteAssertMetricPref = _FsPimCmnIpGenMRouteAssertMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 13),
    _FsPimCmnIpGenMRouteAssertMetricPref_Type()
)
fsPimCmnIpGenMRouteAssertMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteAssertMetricPref.setStatus("current")
_FsPimCmnIpGenMRouteAssertRPTBit_Type = TruthValue
_FsPimCmnIpGenMRouteAssertRPTBit_Object = MibTableColumn
fsPimCmnIpGenMRouteAssertRPTBit = _FsPimCmnIpGenMRouteAssertRPTBit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 14),
    _FsPimCmnIpGenMRouteAssertRPTBit_Type()
)
fsPimCmnIpGenMRouteAssertRPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteAssertRPTBit.setStatus("current")
_FsPimCmnIpGenMRouteTimerFlags_Type = Integer32
_FsPimCmnIpGenMRouteTimerFlags_Object = MibTableColumn
fsPimCmnIpGenMRouteTimerFlags = _FsPimCmnIpGenMRouteTimerFlags_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 15),
    _FsPimCmnIpGenMRouteTimerFlags_Type()
)
fsPimCmnIpGenMRouteTimerFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteTimerFlags.setStatus("current")
_FsPimCmnIpGenMRouteFlags_Type = Integer32
_FsPimCmnIpGenMRouteFlags_Object = MibTableColumn
fsPimCmnIpGenMRouteFlags = _FsPimCmnIpGenMRouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 16),
    _FsPimCmnIpGenMRouteFlags_Type()
)
fsPimCmnIpGenMRouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteFlags.setStatus("current")


class _FsPimCmnIpGenMRouteUpstreamPruneState_Type(Integer32):
    """Custom type fsPimCmnIpGenMRouteUpstreamPruneState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("ackpending", 2),
          ("pruned", 3))
    )


_FsPimCmnIpGenMRouteUpstreamPruneState_Type.__name__ = "Integer32"
_FsPimCmnIpGenMRouteUpstreamPruneState_Object = MibTableColumn
fsPimCmnIpGenMRouteUpstreamPruneState = _FsPimCmnIpGenMRouteUpstreamPruneState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 17),
    _FsPimCmnIpGenMRouteUpstreamPruneState_Type()
)
fsPimCmnIpGenMRouteUpstreamPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteUpstreamPruneState.setStatus("current")
_FsPimCmnIpGenMRouteUpstreamPruneLimitTimer_Type = TimeTicks
_FsPimCmnIpGenMRouteUpstreamPruneLimitTimer_Object = MibTableColumn
fsPimCmnIpGenMRouteUpstreamPruneLimitTimer = _FsPimCmnIpGenMRouteUpstreamPruneLimitTimer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 18),
    _FsPimCmnIpGenMRouteUpstreamPruneLimitTimer_Type()
)
fsPimCmnIpGenMRouteUpstreamPruneLimitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteUpstreamPruneLimitTimer.setStatus("current")


class _FsPimCmnIpGenMRouteOriginatorState_Type(Integer32):
    """Custom type fsPimCmnIpGenMRouteOriginatorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOriginator", 1),
          ("originator", 2))
    )


_FsPimCmnIpGenMRouteOriginatorState_Type.__name__ = "Integer32"
_FsPimCmnIpGenMRouteOriginatorState_Object = MibTableColumn
fsPimCmnIpGenMRouteOriginatorState = _FsPimCmnIpGenMRouteOriginatorState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 19),
    _FsPimCmnIpGenMRouteOriginatorState_Type()
)
fsPimCmnIpGenMRouteOriginatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteOriginatorState.setStatus("current")
_FsPimCmnIpGenMRouteSourceActiveTimer_Type = TimeTicks
_FsPimCmnIpGenMRouteSourceActiveTimer_Object = MibTableColumn
fsPimCmnIpGenMRouteSourceActiveTimer = _FsPimCmnIpGenMRouteSourceActiveTimer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 20),
    _FsPimCmnIpGenMRouteSourceActiveTimer_Type()
)
fsPimCmnIpGenMRouteSourceActiveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteSourceActiveTimer.setStatus("current")
_FsPimCmnIpGenMRouteStateRefreshTimer_Type = TimeTicks
_FsPimCmnIpGenMRouteStateRefreshTimer_Object = MibTableColumn
fsPimCmnIpGenMRouteStateRefreshTimer = _FsPimCmnIpGenMRouteStateRefreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 21),
    _FsPimCmnIpGenMRouteStateRefreshTimer_Type()
)
fsPimCmnIpGenMRouteStateRefreshTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteStateRefreshTimer.setStatus("current")
_FsPimCmnIpGenMRouteExpiryTime_Type = TimeTicks
_FsPimCmnIpGenMRouteExpiryTime_Object = MibTableColumn
fsPimCmnIpGenMRouteExpiryTime = _FsPimCmnIpGenMRouteExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 22),
    _FsPimCmnIpGenMRouteExpiryTime_Type()
)
fsPimCmnIpGenMRouteExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteExpiryTime.setStatus("current")
_FsPimCmnIpGenMRouteDifferentInIfPackets_Type = Counter32
_FsPimCmnIpGenMRouteDifferentInIfPackets_Object = MibTableColumn
fsPimCmnIpGenMRouteDifferentInIfPackets = _FsPimCmnIpGenMRouteDifferentInIfPackets_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 23),
    _FsPimCmnIpGenMRouteDifferentInIfPackets_Type()
)
fsPimCmnIpGenMRouteDifferentInIfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteDifferentInIfPackets.setStatus("current")
_FsPimCmnIpGenMRouteOctets_Type = Counter32
_FsPimCmnIpGenMRouteOctets_Object = MibTableColumn
fsPimCmnIpGenMRouteOctets = _FsPimCmnIpGenMRouteOctets_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 24),
    _FsPimCmnIpGenMRouteOctets_Type()
)
fsPimCmnIpGenMRouteOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteOctets.setStatus("current")
_FsPimCmnIpGenMRouteProtocol_Type = IANAipMRouteProtocol
_FsPimCmnIpGenMRouteProtocol_Object = MibTableColumn
fsPimCmnIpGenMRouteProtocol = _FsPimCmnIpGenMRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 25),
    _FsPimCmnIpGenMRouteProtocol_Type()
)
fsPimCmnIpGenMRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteProtocol.setStatus("current")
_FsPimCmnIpGenMRouteRtProto_Type = IANAipRouteProtocol
_FsPimCmnIpGenMRouteRtProto_Object = MibTableColumn
fsPimCmnIpGenMRouteRtProto = _FsPimCmnIpGenMRouteRtProto_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 26),
    _FsPimCmnIpGenMRouteRtProto_Type()
)
fsPimCmnIpGenMRouteRtProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteRtProto.setStatus("current")
_FsPimCmnIpGenMRouteRtAddress_Type = InetAddress
_FsPimCmnIpGenMRouteRtAddress_Object = MibTableColumn
fsPimCmnIpGenMRouteRtAddress = _FsPimCmnIpGenMRouteRtAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 27),
    _FsPimCmnIpGenMRouteRtAddress_Type()
)
fsPimCmnIpGenMRouteRtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteRtAddress.setStatus("current")
_FsPimCmnIpGenMRouteRtMasklen_Type = Integer32
_FsPimCmnIpGenMRouteRtMasklen_Object = MibTableColumn
fsPimCmnIpGenMRouteRtMasklen = _FsPimCmnIpGenMRouteRtMasklen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 28),
    _FsPimCmnIpGenMRouteRtMasklen_Type()
)
fsPimCmnIpGenMRouteRtMasklen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteRtMasklen.setStatus("current")


class _FsPimCmnIpGenMRouteRtType_Type(Integer32):
    """Custom type fsPimCmnIpGenMRouteRtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2))
    )


_FsPimCmnIpGenMRouteRtType_Type.__name__ = "Integer32"
_FsPimCmnIpGenMRouteRtType_Object = MibTableColumn
fsPimCmnIpGenMRouteRtType = _FsPimCmnIpGenMRouteRtType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 29),
    _FsPimCmnIpGenMRouteRtType_Type()
)
fsPimCmnIpGenMRouteRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteRtType.setStatus("current")
_FsPimCmnIpGenMRouteHCOctets_Type = Counter64
_FsPimCmnIpGenMRouteHCOctets_Object = MibTableColumn
fsPimCmnIpGenMRouteHCOctets = _FsPimCmnIpGenMRouteHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 30),
    _FsPimCmnIpGenMRouteHCOctets_Type()
)
fsPimCmnIpGenMRouteHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteHCOctets.setStatus("current")
_FsPimCmnIpGenMRouteOIfList_Type = PortList
_FsPimCmnIpGenMRouteOIfList_Object = MibTableColumn
fsPimCmnIpGenMRouteOIfList = _FsPimCmnIpGenMRouteOIfList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 31),
    _FsPimCmnIpGenMRouteOIfList_Type()
)
fsPimCmnIpGenMRouteOIfList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteOIfList.setStatus("current")
_FsPimCmnIpGenMRouteRPFVectorAddr_Type = InetAddress
_FsPimCmnIpGenMRouteRPFVectorAddr_Object = MibTableColumn
fsPimCmnIpGenMRouteRPFVectorAddr = _FsPimCmnIpGenMRouteRPFVectorAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 32),
    _FsPimCmnIpGenMRouteRPFVectorAddr_Type()
)
fsPimCmnIpGenMRouteRPFVectorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteRPFVectorAddr.setStatus("current")


class _FsPimCmnIpGenMRoutePimMode_Type(Integer32):
    """Custom type fsPimCmnIpGenMRoutePimMode based on Integer32"""
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
        *(("dm", 1),
          ("sm", 2),
          ("ssm", 3),
          ("bidir", 4))
    )


_FsPimCmnIpGenMRoutePimMode_Type.__name__ = "Integer32"
_FsPimCmnIpGenMRoutePimMode_Object = MibTableColumn
fsPimCmnIpGenMRoutePimMode = _FsPimCmnIpGenMRoutePimMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 33),
    _FsPimCmnIpGenMRoutePimMode_Type()
)
fsPimCmnIpGenMRoutePimMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRoutePimMode.setStatus("current")


class _FsPimCmnIpGenMRouteType_Type(Integer32):
    """Custom type fsPimCmnIpGenMRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("sg", 1),
          ("sgrpt", 2),
          ("starg", 4),
          ("ssrp", 8))
    )


_FsPimCmnIpGenMRouteType_Type.__name__ = "Integer32"
_FsPimCmnIpGenMRouteType_Object = MibTableColumn
fsPimCmnIpGenMRouteType = _FsPimCmnIpGenMRouteType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 34),
    _FsPimCmnIpGenMRouteType_Type()
)
fsPimCmnIpGenMRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteType.setStatus("current")
_FsPimCmnIpGenMRouteNPStatus_Type = Integer32
_FsPimCmnIpGenMRouteNPStatus_Object = MibTableColumn
fsPimCmnIpGenMRouteNPStatus = _FsPimCmnIpGenMRouteNPStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 13, 1, 35),
    _FsPimCmnIpGenMRouteNPStatus_Type()
)
fsPimCmnIpGenMRouteNPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteNPStatus.setStatus("current")
_FsPimCmnIpGenMRouteNextHopTable_Object = MibTable
fsPimCmnIpGenMRouteNextHopTable = _FsPimCmnIpGenMRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 14)
)
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteNextHopTable.setStatus("current")
_FsPimCmnIpGenMRouteNextHopEntry_Object = MibTableRow
fsPimCmnIpGenMRouteNextHopEntry = _FsPimCmnIpGenMRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 14, 1)
)
fsPimCmnIpGenMRouteNextHopEntry.setIndexNames(
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpGenMRouteNextHopCompId"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpGenMRouteNextHopAddrType"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpGenMRouteNextHopGroup"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpGenMRouteNextHopGroupMasklen"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpGenMRouteNextHopSource"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpGenMRouteNextHopSourceMasklen"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpGenMRouteNextHopIfIndex"),
    (0, "ARICENT-PIMCMN-MIB", "fsPimCmnIpGenMRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteNextHopEntry.setStatus("current")


class _FsPimCmnIpGenMRouteNextHopCompId_Type(Integer32):
    """Custom type fsPimCmnIpGenMRouteNextHopCompId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimCmnIpGenMRouteNextHopCompId_Type.__name__ = "Integer32"
_FsPimCmnIpGenMRouteNextHopCompId_Object = MibTableColumn
fsPimCmnIpGenMRouteNextHopCompId = _FsPimCmnIpGenMRouteNextHopCompId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 14, 1, 1),
    _FsPimCmnIpGenMRouteNextHopCompId_Type()
)
fsPimCmnIpGenMRouteNextHopCompId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteNextHopCompId.setStatus("current")
_FsPimCmnIpGenMRouteNextHopAddrType_Type = InetAddressType
_FsPimCmnIpGenMRouteNextHopAddrType_Object = MibTableColumn
fsPimCmnIpGenMRouteNextHopAddrType = _FsPimCmnIpGenMRouteNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 14, 1, 2),
    _FsPimCmnIpGenMRouteNextHopAddrType_Type()
)
fsPimCmnIpGenMRouteNextHopAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteNextHopAddrType.setStatus("current")
_FsPimCmnIpGenMRouteNextHopGroup_Type = InetAddress
_FsPimCmnIpGenMRouteNextHopGroup_Object = MibTableColumn
fsPimCmnIpGenMRouteNextHopGroup = _FsPimCmnIpGenMRouteNextHopGroup_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 14, 1, 3),
    _FsPimCmnIpGenMRouteNextHopGroup_Type()
)
fsPimCmnIpGenMRouteNextHopGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteNextHopGroup.setStatus("current")


class _FsPimCmnIpGenMRouteNextHopGroupMasklen_Type(Integer32):
    """Custom type fsPimCmnIpGenMRouteNextHopGroupMasklen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsPimCmnIpGenMRouteNextHopGroupMasklen_Type.__name__ = "Integer32"
_FsPimCmnIpGenMRouteNextHopGroupMasklen_Object = MibTableColumn
fsPimCmnIpGenMRouteNextHopGroupMasklen = _FsPimCmnIpGenMRouteNextHopGroupMasklen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 14, 1, 4),
    _FsPimCmnIpGenMRouteNextHopGroupMasklen_Type()
)
fsPimCmnIpGenMRouteNextHopGroupMasklen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteNextHopGroupMasklen.setStatus("current")
_FsPimCmnIpGenMRouteNextHopSource_Type = InetAddress
_FsPimCmnIpGenMRouteNextHopSource_Object = MibTableColumn
fsPimCmnIpGenMRouteNextHopSource = _FsPimCmnIpGenMRouteNextHopSource_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 14, 1, 5),
    _FsPimCmnIpGenMRouteNextHopSource_Type()
)
fsPimCmnIpGenMRouteNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteNextHopSource.setStatus("current")


class _FsPimCmnIpGenMRouteNextHopSourceMasklen_Type(Integer32):
    """Custom type fsPimCmnIpGenMRouteNextHopSourceMasklen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_FsPimCmnIpGenMRouteNextHopSourceMasklen_Type.__name__ = "Integer32"
_FsPimCmnIpGenMRouteNextHopSourceMasklen_Object = MibTableColumn
fsPimCmnIpGenMRouteNextHopSourceMasklen = _FsPimCmnIpGenMRouteNextHopSourceMasklen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 14, 1, 6),
    _FsPimCmnIpGenMRouteNextHopSourceMasklen_Type()
)
fsPimCmnIpGenMRouteNextHopSourceMasklen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteNextHopSourceMasklen.setStatus("current")


class _FsPimCmnIpGenMRouteNextHopIfIndex_Type(Integer32):
    """Custom type fsPimCmnIpGenMRouteNextHopIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPimCmnIpGenMRouteNextHopIfIndex_Type.__name__ = "Integer32"
_FsPimCmnIpGenMRouteNextHopIfIndex_Object = MibTableColumn
fsPimCmnIpGenMRouteNextHopIfIndex = _FsPimCmnIpGenMRouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 14, 1, 7),
    _FsPimCmnIpGenMRouteNextHopIfIndex_Type()
)
fsPimCmnIpGenMRouteNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteNextHopIfIndex.setStatus("current")
_FsPimCmnIpGenMRouteNextHopAddress_Type = InetAddress
_FsPimCmnIpGenMRouteNextHopAddress_Object = MibTableColumn
fsPimCmnIpGenMRouteNextHopAddress = _FsPimCmnIpGenMRouteNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 14, 1, 8),
    _FsPimCmnIpGenMRouteNextHopAddress_Type()
)
fsPimCmnIpGenMRouteNextHopAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteNextHopAddress.setStatus("current")


class _FsPimCmnIpGenMRouteNextHopPruneReason_Type(Integer32):
    """Custom type fsPimCmnIpGenMRouteNextHopPruneReason based on Integer32"""
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
        *(("forwarding", 0),
          ("other", 1),
          ("prune", 2),
          ("assert", 3))
    )


_FsPimCmnIpGenMRouteNextHopPruneReason_Type.__name__ = "Integer32"
_FsPimCmnIpGenMRouteNextHopPruneReason_Object = MibTableColumn
fsPimCmnIpGenMRouteNextHopPruneReason = _FsPimCmnIpGenMRouteNextHopPruneReason_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 14, 1, 9),
    _FsPimCmnIpGenMRouteNextHopPruneReason_Type()
)
fsPimCmnIpGenMRouteNextHopPruneReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteNextHopPruneReason.setStatus("current")


class _FsPimCmnIpGenMRouteNextHopState_Type(Integer32):
    """Custom type fsPimCmnIpGenMRouteNextHopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pruned", 1),
          ("forwarding", 2))
    )


_FsPimCmnIpGenMRouteNextHopState_Type.__name__ = "Integer32"
_FsPimCmnIpGenMRouteNextHopState_Object = MibTableColumn
fsPimCmnIpGenMRouteNextHopState = _FsPimCmnIpGenMRouteNextHopState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 14, 1, 10),
    _FsPimCmnIpGenMRouteNextHopState_Type()
)
fsPimCmnIpGenMRouteNextHopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteNextHopState.setStatus("current")
_FsPimCmnIpGenMRouteNextHopUpTime_Type = TimeTicks
_FsPimCmnIpGenMRouteNextHopUpTime_Object = MibTableColumn
fsPimCmnIpGenMRouteNextHopUpTime = _FsPimCmnIpGenMRouteNextHopUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 14, 1, 11),
    _FsPimCmnIpGenMRouteNextHopUpTime_Type()
)
fsPimCmnIpGenMRouteNextHopUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteNextHopUpTime.setStatus("current")
_FsPimCmnIpGenMRouteNextHopExpiryTime_Type = TimeTicks
_FsPimCmnIpGenMRouteNextHopExpiryTime_Object = MibTableColumn
fsPimCmnIpGenMRouteNextHopExpiryTime = _FsPimCmnIpGenMRouteNextHopExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 14, 1, 12),
    _FsPimCmnIpGenMRouteNextHopExpiryTime_Type()
)
fsPimCmnIpGenMRouteNextHopExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteNextHopExpiryTime.setStatus("current")
_FsPimCmnIpGenMRouteNextHopProtocol_Type = IANAipMRouteProtocol
_FsPimCmnIpGenMRouteNextHopProtocol_Object = MibTableColumn
fsPimCmnIpGenMRouteNextHopProtocol = _FsPimCmnIpGenMRouteNextHopProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 14, 1, 13),
    _FsPimCmnIpGenMRouteNextHopProtocol_Type()
)
fsPimCmnIpGenMRouteNextHopProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteNextHopProtocol.setStatus("current")
_FsPimCmnIpGenMRouteNextHopPkts_Type = Counter32
_FsPimCmnIpGenMRouteNextHopPkts_Object = MibTableColumn
fsPimCmnIpGenMRouteNextHopPkts = _FsPimCmnIpGenMRouteNextHopPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 14, 1, 14),
    _FsPimCmnIpGenMRouteNextHopPkts_Type()
)
fsPimCmnIpGenMRouteNextHopPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteNextHopPkts.setStatus("current")
_FsPimCmnIpGenMRouteNextHopNPStatus_Type = Integer32
_FsPimCmnIpGenMRouteNextHopNPStatus_Object = MibTableColumn
fsPimCmnIpGenMRouteNextHopNPStatus = _FsPimCmnIpGenMRouteNextHopNPStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 2, 14, 1, 15),
    _FsPimCmnIpGenMRouteNextHopNPStatus_Type()
)
fsPimCmnIpGenMRouteNextHopNPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimCmnIpGenMRouteNextHopNPStatus.setStatus("current")
_FuturePimCmnTrapsControl_ObjectIdentity = ObjectIdentity
futurePimCmnTrapsControl = _FuturePimCmnTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 3)
)
_FsPimcmnHARtrId_Type = IpAddress
_FsPimcmnHARtrId_Object = MibScalar
fsPimcmnHARtrId = _FsPimcmnHARtrId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 3, 1),
    _FsPimcmnHARtrId_Type()
)
fsPimcmnHARtrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsPimcmnHARtrId.setStatus("current")


class _FsPimCmnHAEvent_Type(Integer32):
    """Custom type fsPimCmnHAEvent based on Integer32"""
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
        *(("standbyInstanceUP", 1),
          ("standbyInstanceDown", 2),
          ("instancesSwitchover", 3),
          ("dynamicBulkupdateStart", 4),
          ("dynamicBulkupdateComplete", 5),
          ("dynamicBulkupdateAborted", 6))
    )


_FsPimCmnHAEvent_Type.__name__ = "Integer32"
_FsPimCmnHAEvent_Object = MibScalar
fsPimCmnHAEvent = _FsPimCmnHAEvent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 3, 3),
    _FsPimCmnHAEvent_Type()
)
fsPimCmnHAEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsPimCmnHAEvent.setStatus("current")
_FuturePimCmnTraps_ObjectIdentity = ObjectIdentity
futurePimCmnTraps = _FuturePimCmnTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 4)
)
_FsPimCmnTraps_ObjectIdentity = ObjectIdentity
fsPimCmnTraps = _FsPimCmnTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 4, 0)
)

# Managed Objects groups


# Notification objects

fsPimCmnHAEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 4, 0, 1)
)
fsPimCmnHAEventTrap.setObjects(
      *(("ARICENT-PIMCMN-MIB", "fsPimcmnHARtrId"),
        ("ARICENT-PIMCMN-MIB", "fsPimCmnHAEvent"))
)
if mibBuilder.loadTexts:
    fsPimCmnHAEventTrap.setStatus(
        "current"
    )

fsPimCmnBidirEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 111, 1, 4, 0, 2)
)
fsPimCmnBidirEventTrap.setObjects(
      *(("ARICENT-PIMCMN-MIB", "fsPimcmnHARtrId"),
        ("ARICENT-PIMCMN-MIB", "fsPimCmnNeighborAddress"),
        ("ARICENT-PIMCMN-MIB", "fsPimCmnNeighborIfIndex"))
)
if mibBuilder.loadTexts:
    fsPimCmnBidirEventTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-PIMCMN-MIB",
    **{"Status": Status,
       "CompList": CompList,
       "fsPimCmnMIB": fsPimCmnMIB,
       "fsPimCmnMIBObjects": fsPimCmnMIBObjects,
       "futurePimCmnScalars": futurePimCmnScalars,
       "fsPimCmnVersionString": fsPimCmnVersionString,
       "fsPimCmnSPTGroupThreshold": fsPimCmnSPTGroupThreshold,
       "fsPimCmnSPTSourceThreshold": fsPimCmnSPTSourceThreshold,
       "fsPimCmnSPTSwitchingPeriod": fsPimCmnSPTSwitchingPeriod,
       "fsPimCmnSPTRpThreshold": fsPimCmnSPTRpThreshold,
       "fsPimCmnSPTRpSwitchingPeriod": fsPimCmnSPTRpSwitchingPeriod,
       "fsPimCmnRegStopRateLimitingPeriod": fsPimCmnRegStopRateLimitingPeriod,
       "fsPimCmnMemoryAllocFailCount": fsPimCmnMemoryAllocFailCount,
       "fsPimCmnGlobalTrace": fsPimCmnGlobalTrace,
       "fsPimCmnGlobalDebug": fsPimCmnGlobalDebug,
       "fsPimCmnPmbrStatus": fsPimCmnPmbrStatus,
       "fsPimCmnRouterMode": fsPimCmnRouterMode,
       "fsPimCmnStaticRpEnabled": fsPimCmnStaticRpEnabled,
       "fsPimCmnIpStatus": fsPimCmnIpStatus,
       "fsPimCmnIpv6Status": fsPimCmnIpv6Status,
       "fsPimCmnSRProcessingStatus": fsPimCmnSRProcessingStatus,
       "fsPimCmnRefreshInterval": fsPimCmnRefreshInterval,
       "fsPimCmnSourceActiveInterval": fsPimCmnSourceActiveInterval,
       "fsPimCmnHAAdminStatus": fsPimCmnHAAdminStatus,
       "fsPimCmnHAState": fsPimCmnHAState,
       "fsPimCmnHADynamicBulkUpdStatus": fsPimCmnHADynamicBulkUpdStatus,
       "fsPimCmnHAForwardingTblEntryCnt": fsPimCmnHAForwardingTblEntryCnt,
       "fsPimCmnIpRpfVector": fsPimCmnIpRpfVector,
       "fsPimCmnIpBidirPIMStatus": fsPimCmnIpBidirPIMStatus,
       "fsPimCmnIpBidirOfferInterval": fsPimCmnIpBidirOfferInterval,
       "fsPimCmnIpBidirOfferLimit": fsPimCmnIpBidirOfferLimit,
       "futurePimCmnTables": futurePimCmnTables,
       "fsPimCmnInterfaceTable": fsPimCmnInterfaceTable,
       "fsPimCmnInterfaceEntry": fsPimCmnInterfaceEntry,
       "fsPimCmnInterfaceIfIndex": fsPimCmnInterfaceIfIndex,
       "fsPimCmnInterfaceAddrType": fsPimCmnInterfaceAddrType,
       "fsPimCmnInterfaceCompId": fsPimCmnInterfaceCompId,
       "fsPimCmnInterfaceDRPriority": fsPimCmnInterfaceDRPriority,
       "fsPimCmnInterfaceHelloHoldTime": fsPimCmnInterfaceHelloHoldTime,
       "fsPimCmnInterfaceLanPruneDelayPresent": fsPimCmnInterfaceLanPruneDelayPresent,
       "fsPimCmnInterfaceLanDelay": fsPimCmnInterfaceLanDelay,
       "fsPimCmnInterfaceOverrideInterval": fsPimCmnInterfaceOverrideInterval,
       "fsPimCmnInterfaceGenerationId": fsPimCmnInterfaceGenerationId,
       "fsPimCmnInterfaceSuppressionInterval": fsPimCmnInterfaceSuppressionInterval,
       "fsPimCmnInterfaceAdminStatus": fsPimCmnInterfaceAdminStatus,
       "fsPimCmnInterfaceBorderBit": fsPimCmnInterfaceBorderBit,
       "fsPimCmnInterfaceGraftRetryInterval": fsPimCmnInterfaceGraftRetryInterval,
       "fsPimCmnInterfaceSRPriorityEnabled": fsPimCmnInterfaceSRPriorityEnabled,
       "fsPimCmnInterfaceTtl": fsPimCmnInterfaceTtl,
       "fsPimCmnInterfaceProtocol": fsPimCmnInterfaceProtocol,
       "fsPimCmnInterfaceRateLimit": fsPimCmnInterfaceRateLimit,
       "fsPimCmnInterfaceInMcastOctets": fsPimCmnInterfaceInMcastOctets,
       "fsPimCmnInterfaceOutMcastOctets": fsPimCmnInterfaceOutMcastOctets,
       "fsPimCmnInterfaceHCInMcastOctets": fsPimCmnInterfaceHCInMcastOctets,
       "fsPimCmnInterfaceHCOutMcastOctets": fsPimCmnInterfaceHCOutMcastOctets,
       "fsPimCmnInterfaceCompIdList": fsPimCmnInterfaceCompIdList,
       "fsPimCmnInterfaceDFOfferSentPkts": fsPimCmnInterfaceDFOfferSentPkts,
       "fsPimCmnInterfaceDFOfferRcvdPkts": fsPimCmnInterfaceDFOfferRcvdPkts,
       "fsPimCmnInterfaceDFWinnerSentPkts": fsPimCmnInterfaceDFWinnerSentPkts,
       "fsPimCmnInterfaceDFWinnerRcvdPkts": fsPimCmnInterfaceDFWinnerRcvdPkts,
       "fsPimCmnInterfaceDFBackoffSentPkts": fsPimCmnInterfaceDFBackoffSentPkts,
       "fsPimCmnInterfaceDFBackoffRcvdPkts": fsPimCmnInterfaceDFBackoffRcvdPkts,
       "fsPimCmnInterfaceDFPassSentPkts": fsPimCmnInterfaceDFPassSentPkts,
       "fsPimCmnInterfaceDFPassRcvdPkts": fsPimCmnInterfaceDFPassRcvdPkts,
       "fsPimCmnInterfaceCKSumErrorPkts": fsPimCmnInterfaceCKSumErrorPkts,
       "fsPimCmnInterfaceInvalidTypePkts": fsPimCmnInterfaceInvalidTypePkts,
       "fsPimCmnInterfaceInvalidDFSubTypePkts": fsPimCmnInterfaceInvalidDFSubTypePkts,
       "fsPimCmnInterfaceAuthFailPkts": fsPimCmnInterfaceAuthFailPkts,
       "fsPimCmnInterfaceFromNonNbrsPkts": fsPimCmnInterfaceFromNonNbrsPkts,
       "fsPimCmnInterfaceJPRcvdOnRPFPkts": fsPimCmnInterfaceJPRcvdOnRPFPkts,
       "fsPimCmnInterfaceJPRcvdNoRPPkts": fsPimCmnInterfaceJPRcvdNoRPPkts,
       "fsPimCmnInterfaceJPRcvdWrongRPPkts": fsPimCmnInterfaceJPRcvdWrongRPPkts,
       "fsPimCmnInterfaceJoinSSMGrpPkts": fsPimCmnInterfaceJoinSSMGrpPkts,
       "fsPimCmnInterfaceJoinBidirGrpPkts": fsPimCmnInterfaceJoinBidirGrpPkts,
       "fsPimCmnInterfaceHelloRcvdPkts": fsPimCmnInterfaceHelloRcvdPkts,
       "fsPimCmnInterfaceHelloSentPkts": fsPimCmnInterfaceHelloSentPkts,
       "fsPimCmnInterfaceJPRcvdPkts": fsPimCmnInterfaceJPRcvdPkts,
       "fsPimCmnInterfaceJPSentPkts": fsPimCmnInterfaceJPSentPkts,
       "fsPimCmnInterfaceAssertRcvdPkts": fsPimCmnInterfaceAssertRcvdPkts,
       "fsPimCmnInterfaceAssertSentPkts": fsPimCmnInterfaceAssertSentPkts,
       "fsPimCmnInterfaceGraftRcvdPkts": fsPimCmnInterfaceGraftRcvdPkts,
       "fsPimCmnInterfaceGraftSentPkts": fsPimCmnInterfaceGraftSentPkts,
       "fsPimCmnInterfaceGraftAckRcvdPkts": fsPimCmnInterfaceGraftAckRcvdPkts,
       "fsPimCmnInterfaceGraftAckSentPkts": fsPimCmnInterfaceGraftAckSentPkts,
       "fsPimCmnInterfacePackLenErrorPkts": fsPimCmnInterfacePackLenErrorPkts,
       "fsPimCmnInterfaceBadVersionPkts": fsPimCmnInterfaceBadVersionPkts,
       "fsPimCmnInterfacePktsfromSelf": fsPimCmnInterfacePktsfromSelf,
       "fsPimCmnInterfaceExtBorderBit": fsPimCmnInterfaceExtBorderBit,
       "fsPimCmnInterfaceJoinSSMBadPkts": fsPimCmnInterfaceJoinSSMBadPkts,
       "fsPimCmnNeighborTable": fsPimCmnNeighborTable,
       "fsPimCmnNeighborEntry": fsPimCmnNeighborEntry,
       "fsPimCmnNeighborCompId": fsPimCmnNeighborCompId,
       "fsPimCmnNeighborAddrType": fsPimCmnNeighborAddrType,
       "fsPimCmnNeighborAddress": fsPimCmnNeighborAddress,
       "fsPimCmnNeighborIfIndex": fsPimCmnNeighborIfIndex,
       "fsPimCmnNeighborUpTime": fsPimCmnNeighborUpTime,
       "fsPimCmnNeighborExpiryTime": fsPimCmnNeighborExpiryTime,
       "fsPimCmnNeighborGenerationId": fsPimCmnNeighborGenerationId,
       "fsPimCmnNeighborLanDelay": fsPimCmnNeighborLanDelay,
       "fsPimCmnNeighborDRPriority": fsPimCmnNeighborDRPriority,
       "fsPimCmnNeighborOverrideInterval": fsPimCmnNeighborOverrideInterval,
       "fsPimCmnNeighborSRCapable": fsPimCmnNeighborSRCapable,
       "fsPimCmnNeighborRPFCapable": fsPimCmnNeighborRPFCapable,
       "fsPimCmnNeighborBidirCapable": fsPimCmnNeighborBidirCapable,
       "fsPimCmnIpMRouteTable": fsPimCmnIpMRouteTable,
       "fsPimCmnIpMRouteEntry": fsPimCmnIpMRouteEntry,
       "fsPimCmnIpMRouteCompId": fsPimCmnIpMRouteCompId,
       "fsPimCmnIpMRouteAddrType": fsPimCmnIpMRouteAddrType,
       "fsPimCmnIpMRouteGroup": fsPimCmnIpMRouteGroup,
       "fsPimCmnIpMRouteSource": fsPimCmnIpMRouteSource,
       "fsPimCmnIpMRouteSourceMasklen": fsPimCmnIpMRouteSourceMasklen,
       "fsPimCmnIpMRouteUpstreamNeighbor": fsPimCmnIpMRouteUpstreamNeighbor,
       "fsPimCmnIpMRouteInIfIndex": fsPimCmnIpMRouteInIfIndex,
       "fsPimCmnIpMRouteUpTime": fsPimCmnIpMRouteUpTime,
       "fsPimCmnIpMRoutePkts": fsPimCmnIpMRoutePkts,
       "fsPimCmnIpMRouteUpstreamAssertTimer": fsPimCmnIpMRouteUpstreamAssertTimer,
       "fsPimCmnIpMRouteAssertMetric": fsPimCmnIpMRouteAssertMetric,
       "fsPimCmnIpMRouteAssertMetricPref": fsPimCmnIpMRouteAssertMetricPref,
       "fsPimCmnIpMRouteAssertRPTBit": fsPimCmnIpMRouteAssertRPTBit,
       "fsPimCmnIpMRouteTimerFlags": fsPimCmnIpMRouteTimerFlags,
       "fsPimCmnIpMRouteFlags": fsPimCmnIpMRouteFlags,
       "fsPimCmnIpMRouteUpstreamPruneState": fsPimCmnIpMRouteUpstreamPruneState,
       "fsPimCmnIpMRouteUpstreamPruneLimitTimer": fsPimCmnIpMRouteUpstreamPruneLimitTimer,
       "fsPimCmnIpMRouteOriginatorState": fsPimCmnIpMRouteOriginatorState,
       "fsPimCmnIpMRouteSourceActiveTimer": fsPimCmnIpMRouteSourceActiveTimer,
       "fsPimCmnIpMRouteStateRefreshTimer": fsPimCmnIpMRouteStateRefreshTimer,
       "fsPimCmnIpMRouteExpiryTime": fsPimCmnIpMRouteExpiryTime,
       "fsPimCmnIpMRouteDifferentInIfPackets": fsPimCmnIpMRouteDifferentInIfPackets,
       "fsPimCmnIpMRouteOctets": fsPimCmnIpMRouteOctets,
       "fsPimCmnIpMRouteProtocol": fsPimCmnIpMRouteProtocol,
       "fsPimCmnIpMRouteRtProto": fsPimCmnIpMRouteRtProto,
       "fsPimCmnIpMRouteRtAddress": fsPimCmnIpMRouteRtAddress,
       "fsPimCmnIpMRouteRtMasklen": fsPimCmnIpMRouteRtMasklen,
       "fsPimCmnIpMRouteRtType": fsPimCmnIpMRouteRtType,
       "fsPimCmnIpMRouteHCOctets": fsPimCmnIpMRouteHCOctets,
       "fsPimCmnIpMRouteOIfList": fsPimCmnIpMRouteOIfList,
       "fsPimCmnIpMRouteRPFVectorAddr": fsPimCmnIpMRouteRPFVectorAddr,
       "fsPimCmnIpMRoutePimMode": fsPimCmnIpMRoutePimMode,
       "fsPimCmnIpMRouteNextHopTable": fsPimCmnIpMRouteNextHopTable,
       "fsPimCmnIpMRouteNextHopEntry": fsPimCmnIpMRouteNextHopEntry,
       "fsPimCmnIpMRouteNextHopCompId": fsPimCmnIpMRouteNextHopCompId,
       "fsPimCmnIpMRouteNextHopAddrType": fsPimCmnIpMRouteNextHopAddrType,
       "fsPimCmnIpMRouteNextHopGroup": fsPimCmnIpMRouteNextHopGroup,
       "fsPimCmnIpMRouteNextHopSource": fsPimCmnIpMRouteNextHopSource,
       "fsPimCmnIpMRouteNextHopSourceMasklen": fsPimCmnIpMRouteNextHopSourceMasklen,
       "fsPimCmnIpMRouteNextHopIfIndex": fsPimCmnIpMRouteNextHopIfIndex,
       "fsPimCmnIpMRouteNextHopAddress": fsPimCmnIpMRouteNextHopAddress,
       "fsPimCmnIpMRouteNextHopPruneReason": fsPimCmnIpMRouteNextHopPruneReason,
       "fsPimCmnIpMRouteNextHopState": fsPimCmnIpMRouteNextHopState,
       "fsPimCmnIpMRouteNextHopUpTime": fsPimCmnIpMRouteNextHopUpTime,
       "fsPimCmnIpMRouteNextHopExpiryTime": fsPimCmnIpMRouteNextHopExpiryTime,
       "fsPimCmnIpMRouteNextHopProtocol": fsPimCmnIpMRouteNextHopProtocol,
       "fsPimCmnIpMRouteNextHopPkts": fsPimCmnIpMRouteNextHopPkts,
       "fsPimCmnCandidateRPTable": fsPimCmnCandidateRPTable,
       "fsPimCmnCandidateRPEntry": fsPimCmnCandidateRPEntry,
       "fsPimCmnCandidateRPCompId": fsPimCmnCandidateRPCompId,
       "fsPimCmnCandidateRPAddrType": fsPimCmnCandidateRPAddrType,
       "fsPimCmnCandidateRPGroupAddress": fsPimCmnCandidateRPGroupAddress,
       "fsPimCmnCandidateRPGroupMasklen": fsPimCmnCandidateRPGroupMasklen,
       "fsPimCmnCandidateRPAddress": fsPimCmnCandidateRPAddress,
       "fsPimCmnCandidateRPPriority": fsPimCmnCandidateRPPriority,
       "fsPimCmnCandidateRPRowStatus": fsPimCmnCandidateRPRowStatus,
       "fsPimCmnCandidateRPPimMode": fsPimCmnCandidateRPPimMode,
       "fsPimCmnStaticRPSetTable": fsPimCmnStaticRPSetTable,
       "fsPimCmnStaticRPSetEntry": fsPimCmnStaticRPSetEntry,
       "fsPimCmnStaticRPSetCompId": fsPimCmnStaticRPSetCompId,
       "fsPimCmnStaticRPAddrType": fsPimCmnStaticRPAddrType,
       "fsPimCmnStaticRPSetGroupAddress": fsPimCmnStaticRPSetGroupAddress,
       "fsPimCmnStaticRPSetGroupMasklen": fsPimCmnStaticRPSetGroupMasklen,
       "fsPimCmnStaticRPAddress": fsPimCmnStaticRPAddress,
       "fsPimCmnStaticRPRowStatus": fsPimCmnStaticRPRowStatus,
       "fsPimCmnStaticRPEmbdFlag": fsPimCmnStaticRPEmbdFlag,
       "fsPimCmnStaticRPPimMode": fsPimCmnStaticRPPimMode,
       "fsPimCmnComponentModeTable": fsPimCmnComponentModeTable,
       "fsPimCmnComponentModeEntry": fsPimCmnComponentModeEntry,
       "fsPimCmnComponentId": fsPimCmnComponentId,
       "fsPimCmnComponentMode": fsPimCmnComponentMode,
       "fsPimCmnCompGraftRetryCount": fsPimCmnCompGraftRetryCount,
       "fsPimCmnRegChkSumCfgTable": fsPimCmnRegChkSumCfgTable,
       "fsPimCmnRegChkSumCfgEntry": fsPimCmnRegChkSumCfgEntry,
       "fsPimCmnRegChkSumTblCompId": fsPimCmnRegChkSumTblCompId,
       "fsPimCmnRegChkSumTblRPAddrType": fsPimCmnRegChkSumTblRPAddrType,
       "fsPimCmnRegChkSumTblRPAddress": fsPimCmnRegChkSumTblRPAddress,
       "fsPimCmnRPChkSumStatus": fsPimCmnRPChkSumStatus,
       "fsPimCmnDFTable": fsPimCmnDFTable,
       "fsPimCmnDFEntry": fsPimCmnDFEntry,
       "fsPimCmnDFIfAddrType": fsPimCmnDFIfAddrType,
       "fsPimCmnDFElectedRP": fsPimCmnDFElectedRP,
       "fsPimCmnDFIfIndex": fsPimCmnDFIfIndex,
       "fsPimCmnDFState": fsPimCmnDFState,
       "fsPimCmnDFWinnerAddr": fsPimCmnDFWinnerAddr,
       "fsPimCmnDFWinnerUptime": fsPimCmnDFWinnerUptime,
       "fsPimCmnDFElectionStateTimer": fsPimCmnDFElectionStateTimer,
       "fsPimCmnDFWinnerMetric": fsPimCmnDFWinnerMetric,
       "fsPimCmnDFWinnerMetricPref": fsPimCmnDFWinnerMetricPref,
       "fsPimCmnDFMessageCount": fsPimCmnDFMessageCount,
       "fsPimCmnElectedRPTable": fsPimCmnElectedRPTable,
       "fsPimCmnElectedRPEntry": fsPimCmnElectedRPEntry,
       "fsPimCmnElectedRPCompId": fsPimCmnElectedRPCompId,
       "fsPimCmnElectedRPAddrType": fsPimCmnElectedRPAddrType,
       "fsPimCmnElectedRPGroupAddress": fsPimCmnElectedRPGroupAddress,
       "fsPimCmnElectedRPGroupMasklen": fsPimCmnElectedRPGroupMasklen,
       "fsPimCmnElectedRPAddress": fsPimCmnElectedRPAddress,
       "fsPimCmnElectedRPPriority": fsPimCmnElectedRPPriority,
       "fsPimCmnElectedRPHoldTime": fsPimCmnElectedRPHoldTime,
       "fsPimCmnElectedRPUpTime": fsPimCmnElectedRPUpTime,
       "fsPimCmnNeighborExtTable": fsPimCmnNeighborExtTable,
       "fsPimCmnNeighborExtEntry": fsPimCmnNeighborExtEntry,
       "fsPimCmnNeighborExtIfIndex": fsPimCmnNeighborExtIfIndex,
       "fsPimCmnNeighborExtAddrType": fsPimCmnNeighborExtAddrType,
       "fsPimCmnNeighborExtAddress": fsPimCmnNeighborExtAddress,
       "fsPimCmnNeighborExtCompIdList": fsPimCmnNeighborExtCompIdList,
       "fsPimCmnNeighborExtUpTime": fsPimCmnNeighborExtUpTime,
       "fsPimCmnNeighborExtExpiryTime": fsPimCmnNeighborExtExpiryTime,
       "fsPimCmnNeighborExtGenerationId": fsPimCmnNeighborExtGenerationId,
       "fsPimCmnNeighborExtLanDelay": fsPimCmnNeighborExtLanDelay,
       "fsPimCmnNeighborExtDRPriority": fsPimCmnNeighborExtDRPriority,
       "fsPimCmnNeighborExtOverrideInterval": fsPimCmnNeighborExtOverrideInterval,
       "fsPimCmnNeighborExtSRCapable": fsPimCmnNeighborExtSRCapable,
       "fsPimCmnNeighborExtRPFCapable": fsPimCmnNeighborExtRPFCapable,
       "fsPimCmnNeighborExtBidirCapable": fsPimCmnNeighborExtBidirCapable,
       "fsPimCmnIpGenMRouteTable": fsPimCmnIpGenMRouteTable,
       "fsPimCmnIpGenMRouteEntry": fsPimCmnIpGenMRouteEntry,
       "fsPimCmnIpGenMRouteCompId": fsPimCmnIpGenMRouteCompId,
       "fsPimCmnIpGenMRouteAddrType": fsPimCmnIpGenMRouteAddrType,
       "fsPimCmnIpGenMRouteGroup": fsPimCmnIpGenMRouteGroup,
       "fsPimCmnIpGenMRouteGroupMasklen": fsPimCmnIpGenMRouteGroupMasklen,
       "fsPimCmnIpGenMRouteSource": fsPimCmnIpGenMRouteSource,
       "fsPimCmnIpGenMRouteSourceMasklen": fsPimCmnIpGenMRouteSourceMasklen,
       "fsPimCmnIpGenMRouteUpstreamNeighbor": fsPimCmnIpGenMRouteUpstreamNeighbor,
       "fsPimCmnIpGenMRouteInIfIndex": fsPimCmnIpGenMRouteInIfIndex,
       "fsPimCmnIpGenMRouteUpTime": fsPimCmnIpGenMRouteUpTime,
       "fsPimCmnIpGenMRoutePkts": fsPimCmnIpGenMRoutePkts,
       "fsPimCmnIpGenMRouteUpstreamAssertTimer": fsPimCmnIpGenMRouteUpstreamAssertTimer,
       "fsPimCmnIpGenMRouteAssertMetric": fsPimCmnIpGenMRouteAssertMetric,
       "fsPimCmnIpGenMRouteAssertMetricPref": fsPimCmnIpGenMRouteAssertMetricPref,
       "fsPimCmnIpGenMRouteAssertRPTBit": fsPimCmnIpGenMRouteAssertRPTBit,
       "fsPimCmnIpGenMRouteTimerFlags": fsPimCmnIpGenMRouteTimerFlags,
       "fsPimCmnIpGenMRouteFlags": fsPimCmnIpGenMRouteFlags,
       "fsPimCmnIpGenMRouteUpstreamPruneState": fsPimCmnIpGenMRouteUpstreamPruneState,
       "fsPimCmnIpGenMRouteUpstreamPruneLimitTimer": fsPimCmnIpGenMRouteUpstreamPruneLimitTimer,
       "fsPimCmnIpGenMRouteOriginatorState": fsPimCmnIpGenMRouteOriginatorState,
       "fsPimCmnIpGenMRouteSourceActiveTimer": fsPimCmnIpGenMRouteSourceActiveTimer,
       "fsPimCmnIpGenMRouteStateRefreshTimer": fsPimCmnIpGenMRouteStateRefreshTimer,
       "fsPimCmnIpGenMRouteExpiryTime": fsPimCmnIpGenMRouteExpiryTime,
       "fsPimCmnIpGenMRouteDifferentInIfPackets": fsPimCmnIpGenMRouteDifferentInIfPackets,
       "fsPimCmnIpGenMRouteOctets": fsPimCmnIpGenMRouteOctets,
       "fsPimCmnIpGenMRouteProtocol": fsPimCmnIpGenMRouteProtocol,
       "fsPimCmnIpGenMRouteRtProto": fsPimCmnIpGenMRouteRtProto,
       "fsPimCmnIpGenMRouteRtAddress": fsPimCmnIpGenMRouteRtAddress,
       "fsPimCmnIpGenMRouteRtMasklen": fsPimCmnIpGenMRouteRtMasklen,
       "fsPimCmnIpGenMRouteRtType": fsPimCmnIpGenMRouteRtType,
       "fsPimCmnIpGenMRouteHCOctets": fsPimCmnIpGenMRouteHCOctets,
       "fsPimCmnIpGenMRouteOIfList": fsPimCmnIpGenMRouteOIfList,
       "fsPimCmnIpGenMRouteRPFVectorAddr": fsPimCmnIpGenMRouteRPFVectorAddr,
       "fsPimCmnIpGenMRoutePimMode": fsPimCmnIpGenMRoutePimMode,
       "fsPimCmnIpGenMRouteType": fsPimCmnIpGenMRouteType,
       "fsPimCmnIpGenMRouteNPStatus": fsPimCmnIpGenMRouteNPStatus,
       "fsPimCmnIpGenMRouteNextHopTable": fsPimCmnIpGenMRouteNextHopTable,
       "fsPimCmnIpGenMRouteNextHopEntry": fsPimCmnIpGenMRouteNextHopEntry,
       "fsPimCmnIpGenMRouteNextHopCompId": fsPimCmnIpGenMRouteNextHopCompId,
       "fsPimCmnIpGenMRouteNextHopAddrType": fsPimCmnIpGenMRouteNextHopAddrType,
       "fsPimCmnIpGenMRouteNextHopGroup": fsPimCmnIpGenMRouteNextHopGroup,
       "fsPimCmnIpGenMRouteNextHopGroupMasklen": fsPimCmnIpGenMRouteNextHopGroupMasklen,
       "fsPimCmnIpGenMRouteNextHopSource": fsPimCmnIpGenMRouteNextHopSource,
       "fsPimCmnIpGenMRouteNextHopSourceMasklen": fsPimCmnIpGenMRouteNextHopSourceMasklen,
       "fsPimCmnIpGenMRouteNextHopIfIndex": fsPimCmnIpGenMRouteNextHopIfIndex,
       "fsPimCmnIpGenMRouteNextHopAddress": fsPimCmnIpGenMRouteNextHopAddress,
       "fsPimCmnIpGenMRouteNextHopPruneReason": fsPimCmnIpGenMRouteNextHopPruneReason,
       "fsPimCmnIpGenMRouteNextHopState": fsPimCmnIpGenMRouteNextHopState,
       "fsPimCmnIpGenMRouteNextHopUpTime": fsPimCmnIpGenMRouteNextHopUpTime,
       "fsPimCmnIpGenMRouteNextHopExpiryTime": fsPimCmnIpGenMRouteNextHopExpiryTime,
       "fsPimCmnIpGenMRouteNextHopProtocol": fsPimCmnIpGenMRouteNextHopProtocol,
       "fsPimCmnIpGenMRouteNextHopPkts": fsPimCmnIpGenMRouteNextHopPkts,
       "fsPimCmnIpGenMRouteNextHopNPStatus": fsPimCmnIpGenMRouteNextHopNPStatus,
       "futurePimCmnTrapsControl": futurePimCmnTrapsControl,
       "fsPimcmnHARtrId": fsPimcmnHARtrId,
       "fsPimCmnHAEvent": fsPimCmnHAEvent,
       "futurePimCmnTraps": futurePimCmnTraps,
       "fsPimCmnTraps": fsPimCmnTraps,
       "fsPimCmnHAEventTrap": fsPimCmnHAEventTrap,
       "fsPimCmnBidirEventTrap": fsPimCmnBidirEventTrap}
)
