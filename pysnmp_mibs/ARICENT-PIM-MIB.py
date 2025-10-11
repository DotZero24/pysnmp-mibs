# SNMP MIB module (ARICENT-PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-PIM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:28 2025
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

fsPimMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 20)
)
if mibBuilder.loadTexts:
    fsPimMIB.setRevisions(
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



# MIB Managed Objects in the order of their OIDs

_FsPimMIBObjects_ObjectIdentity = ObjectIdentity
fsPimMIBObjects = _FsPimMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1)
)
_FuturePimScalars_ObjectIdentity = ObjectIdentity
futurePimScalars = _FuturePimScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 1)
)
_FsPimVersionString_Type = DisplayString
_FsPimVersionString_Object = MibScalar
fsPimVersionString = _FsPimVersionString_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 1, 1),
    _FsPimVersionString_Type()
)
fsPimVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimVersionString.setStatus("current")


class _FsPimSPTGroupThreshold_Type(Integer32):
    """Custom type fsPimSPTGroupThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsPimSPTGroupThreshold_Type.__name__ = "Integer32"
_FsPimSPTGroupThreshold_Object = MibScalar
fsPimSPTGroupThreshold = _FsPimSPTGroupThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 1, 2),
    _FsPimSPTGroupThreshold_Type()
)
fsPimSPTGroupThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimSPTGroupThreshold.setStatus("current")


class _FsPimSPTSourceThreshold_Type(Integer32):
    """Custom type fsPimSPTSourceThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsPimSPTSourceThreshold_Type.__name__ = "Integer32"
_FsPimSPTSourceThreshold_Object = MibScalar
fsPimSPTSourceThreshold = _FsPimSPTSourceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 1, 3),
    _FsPimSPTSourceThreshold_Type()
)
fsPimSPTSourceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimSPTSourceThreshold.setStatus("current")


class _FsPimSPTSwitchingPeriod_Type(Integer32):
    """Custom type fsPimSPTSwitchingPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsPimSPTSwitchingPeriod_Type.__name__ = "Integer32"
_FsPimSPTSwitchingPeriod_Object = MibScalar
fsPimSPTSwitchingPeriod = _FsPimSPTSwitchingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 1, 4),
    _FsPimSPTSwitchingPeriod_Type()
)
fsPimSPTSwitchingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimSPTSwitchingPeriod.setStatus("current")


class _FsPimSPTRpThreshold_Type(Integer32):
    """Custom type fsPimSPTRpThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsPimSPTRpThreshold_Type.__name__ = "Integer32"
_FsPimSPTRpThreshold_Object = MibScalar
fsPimSPTRpThreshold = _FsPimSPTRpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 1, 5),
    _FsPimSPTRpThreshold_Type()
)
fsPimSPTRpThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimSPTRpThreshold.setStatus("current")


class _FsPimSPTRpSwitchingPeriod_Type(Integer32):
    """Custom type fsPimSPTRpSwitchingPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsPimSPTRpSwitchingPeriod_Type.__name__ = "Integer32"
_FsPimSPTRpSwitchingPeriod_Object = MibScalar
fsPimSPTRpSwitchingPeriod = _FsPimSPTRpSwitchingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 1, 6),
    _FsPimSPTRpSwitchingPeriod_Type()
)
fsPimSPTRpSwitchingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimSPTRpSwitchingPeriod.setStatus("current")


class _FsPimRegStopRateLimitingPeriod_Type(Integer32):
    """Custom type fsPimRegStopRateLimitingPeriod based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsPimRegStopRateLimitingPeriod_Type.__name__ = "Integer32"
_FsPimRegStopRateLimitingPeriod_Object = MibScalar
fsPimRegStopRateLimitingPeriod = _FsPimRegStopRateLimitingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 1, 7),
    _FsPimRegStopRateLimitingPeriod_Type()
)
fsPimRegStopRateLimitingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimRegStopRateLimitingPeriod.setStatus("current")
_FsPimMemoryAllocFailCount_Type = Integer32
_FsPimMemoryAllocFailCount_Object = MibScalar
fsPimMemoryAllocFailCount = _FsPimMemoryAllocFailCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 1, 8),
    _FsPimMemoryAllocFailCount_Type()
)
fsPimMemoryAllocFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimMemoryAllocFailCount.setStatus("current")


class _FsPimGlobalTrace_Type(Integer32):
    """Custom type fsPimGlobalTrace based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPimGlobalTrace_Type.__name__ = "Integer32"
_FsPimGlobalTrace_Object = MibScalar
fsPimGlobalTrace = _FsPimGlobalTrace_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 1, 9),
    _FsPimGlobalTrace_Type()
)
fsPimGlobalTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimGlobalTrace.setStatus("current")


class _FsPimGlobalDebug_Type(Integer32):
    """Custom type fsPimGlobalDebug based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPimGlobalDebug_Type.__name__ = "Integer32"
_FsPimGlobalDebug_Object = MibScalar
fsPimGlobalDebug = _FsPimGlobalDebug_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 1, 10),
    _FsPimGlobalDebug_Type()
)
fsPimGlobalDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimGlobalDebug.setStatus("current")


class _FsPimPmbrStatus_Type(Integer32):
    """Custom type fsPimPmbrStatus based on Integer32"""
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


_FsPimPmbrStatus_Type.__name__ = "Integer32"
_FsPimPmbrStatus_Object = MibScalar
fsPimPmbrStatus = _FsPimPmbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 1, 11),
    _FsPimPmbrStatus_Type()
)
fsPimPmbrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimPmbrStatus.setStatus("current")


class _FsPimRouterMode_Type(Integer32):
    """Custom type fsPimRouterMode based on Integer32"""
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


_FsPimRouterMode_Type.__name__ = "Integer32"
_FsPimRouterMode_Object = MibScalar
fsPimRouterMode = _FsPimRouterMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 1, 12),
    _FsPimRouterMode_Type()
)
fsPimRouterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimRouterMode.setStatus("current")


class _FsPimStaticRpEnabled_Type(Integer32):
    """Custom type fsPimStaticRpEnabled based on Integer32"""
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
          ("enabled", 1))
    )


_FsPimStaticRpEnabled_Type.__name__ = "Integer32"
_FsPimStaticRpEnabled_Object = MibScalar
fsPimStaticRpEnabled = _FsPimStaticRpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 1, 13),
    _FsPimStaticRpEnabled_Type()
)
fsPimStaticRpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimStaticRpEnabled.setStatus("current")


class _FsPimStatus_Type(Integer32):
    """Custom type fsPimStatus based on Integer32"""
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


_FsPimStatus_Type.__name__ = "Integer32"
_FsPimStatus_Object = MibScalar
fsPimStatus = _FsPimStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 1, 14),
    _FsPimStatus_Type()
)
fsPimStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimStatus.setStatus("current")
_FuturePimTables_ObjectIdentity = ObjectIdentity
futurePimTables = _FuturePimTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2)
)
_FsPimInterfaceTable_Object = MibTable
fsPimInterfaceTable = _FsPimInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsPimInterfaceTable.setStatus("current")
_FsPimInterfaceEntry_Object = MibTableRow
fsPimInterfaceEntry = _FsPimInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 1, 1)
)
fsPimInterfaceEntry.setIndexNames(
    (0, "ARICENT-PIM-MIB", "fsPimInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    fsPimInterfaceEntry.setStatus("current")


class _FsPimInterfaceIfIndex_Type(Integer32):
    """Custom type fsPimInterfaceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPimInterfaceIfIndex_Type.__name__ = "Integer32"
_FsPimInterfaceIfIndex_Object = MibTableColumn
fsPimInterfaceIfIndex = _FsPimInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 1, 1, 1),
    _FsPimInterfaceIfIndex_Type()
)
fsPimInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimInterfaceIfIndex.setStatus("current")


class _FsPimInterfaceCompId_Type(Integer32):
    """Custom type fsPimInterfaceCompId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimInterfaceCompId_Type.__name__ = "Integer32"
_FsPimInterfaceCompId_Object = MibTableColumn
fsPimInterfaceCompId = _FsPimInterfaceCompId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 1, 1, 2),
    _FsPimInterfaceCompId_Type()
)
fsPimInterfaceCompId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceCompId.setStatus("current")


class _FsPimInterfaceDRPriority_Type(Unsigned32):
    """Custom type fsPimInterfaceDRPriority based on Unsigned32"""
    defaultValue = 1


_FsPimInterfaceDRPriority_Type.__name__ = "Unsigned32"
_FsPimInterfaceDRPriority_Object = MibTableColumn
fsPimInterfaceDRPriority = _FsPimInterfaceDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 1, 1, 3),
    _FsPimInterfaceDRPriority_Type()
)
fsPimInterfaceDRPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceDRPriority.setStatus("current")


class _FsPimInterfaceHelloHoldTime_Type(Integer32):
    """Custom type fsPimInterfaceHelloHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPimInterfaceHelloHoldTime_Type.__name__ = "Integer32"
_FsPimInterfaceHelloHoldTime_Object = MibTableColumn
fsPimInterfaceHelloHoldTime = _FsPimInterfaceHelloHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 1, 1, 4),
    _FsPimInterfaceHelloHoldTime_Type()
)
fsPimInterfaceHelloHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimInterfaceHelloHoldTime.setStatus("current")


class _FsPimInterfaceLanPruneDelayPresent_Type(Integer32):
    """Custom type fsPimInterfaceLanPruneDelayPresent based on Integer32"""
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


_FsPimInterfaceLanPruneDelayPresent_Type.__name__ = "Integer32"
_FsPimInterfaceLanPruneDelayPresent_Object = MibTableColumn
fsPimInterfaceLanPruneDelayPresent = _FsPimInterfaceLanPruneDelayPresent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 1, 1, 5),
    _FsPimInterfaceLanPruneDelayPresent_Type()
)
fsPimInterfaceLanPruneDelayPresent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceLanPruneDelayPresent.setStatus("current")


class _FsPimInterfaceLanDelay_Type(Integer32):
    """Custom type fsPimInterfaceLanDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPimInterfaceLanDelay_Type.__name__ = "Integer32"
_FsPimInterfaceLanDelay_Object = MibTableColumn
fsPimInterfaceLanDelay = _FsPimInterfaceLanDelay_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 1, 1, 6),
    _FsPimInterfaceLanDelay_Type()
)
fsPimInterfaceLanDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceLanDelay.setStatus("current")


class _FsPimInterfaceOverrideInterval_Type(Integer32):
    """Custom type fsPimInterfaceOverrideInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsPimInterfaceOverrideInterval_Type.__name__ = "Integer32"
_FsPimInterfaceOverrideInterval_Object = MibTableColumn
fsPimInterfaceOverrideInterval = _FsPimInterfaceOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 1, 1, 7),
    _FsPimInterfaceOverrideInterval_Type()
)
fsPimInterfaceOverrideInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceOverrideInterval.setStatus("current")
_FsPimInterfaceGenerationId_Type = Integer32
_FsPimInterfaceGenerationId_Object = MibTableColumn
fsPimInterfaceGenerationId = _FsPimInterfaceGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 1, 1, 8),
    _FsPimInterfaceGenerationId_Type()
)
fsPimInterfaceGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimInterfaceGenerationId.setStatus("current")
_FsPimInterfaceSuppressionInterval_Type = Integer32
_FsPimInterfaceSuppressionInterval_Object = MibTableColumn
fsPimInterfaceSuppressionInterval = _FsPimInterfaceSuppressionInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 1, 1, 9),
    _FsPimInterfaceSuppressionInterval_Type()
)
fsPimInterfaceSuppressionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimInterfaceSuppressionInterval.setStatus("current")
_FsPimInterfaceAdminStatus_Type = Integer32
_FsPimInterfaceAdminStatus_Object = MibTableColumn
fsPimInterfaceAdminStatus = _FsPimInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 1, 1, 10),
    _FsPimInterfaceAdminStatus_Type()
)
fsPimInterfaceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceAdminStatus.setStatus("current")
_FsPimInterfaceBorderBit_Type = Integer32
_FsPimInterfaceBorderBit_Object = MibTableColumn
fsPimInterfaceBorderBit = _FsPimInterfaceBorderBit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 1, 1, 11),
    _FsPimInterfaceBorderBit_Type()
)
fsPimInterfaceBorderBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimInterfaceBorderBit.setStatus("current")
_FsPimNeighborTable_Object = MibTable
fsPimNeighborTable = _FsPimNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fsPimNeighborTable.setStatus("current")
_FsPimNeighborEntry_Object = MibTableRow
fsPimNeighborEntry = _FsPimNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 2, 1)
)
fsPimNeighborEntry.setIndexNames(
    (0, "ARICENT-PIM-MIB", "fsPimNeighborAddress"),
    (0, "ARICENT-PIM-MIB", "fsPimNeighborCompId"),
)
if mibBuilder.loadTexts:
    fsPimNeighborEntry.setStatus("current")
_FsPimNeighborAddress_Type = IpAddress
_FsPimNeighborAddress_Object = MibTableColumn
fsPimNeighborAddress = _FsPimNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 2, 1, 1),
    _FsPimNeighborAddress_Type()
)
fsPimNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimNeighborAddress.setStatus("current")


class _FsPimNeighborCompId_Type(Integer32):
    """Custom type fsPimNeighborCompId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimNeighborCompId_Type.__name__ = "Integer32"
_FsPimNeighborCompId_Object = MibTableColumn
fsPimNeighborCompId = _FsPimNeighborCompId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 2, 1, 2),
    _FsPimNeighborCompId_Type()
)
fsPimNeighborCompId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimNeighborCompId.setStatus("current")
_FsPimNeighborIfIndex_Type = Integer32
_FsPimNeighborIfIndex_Object = MibTableColumn
fsPimNeighborIfIndex = _FsPimNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 2, 1, 3),
    _FsPimNeighborIfIndex_Type()
)
fsPimNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimNeighborIfIndex.setStatus("current")
_FsPimNeighborUpTime_Type = TimeTicks
_FsPimNeighborUpTime_Object = MibTableColumn
fsPimNeighborUpTime = _FsPimNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 2, 1, 4),
    _FsPimNeighborUpTime_Type()
)
fsPimNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimNeighborUpTime.setStatus("current")
_FsPimNeighborExpiryTime_Type = TimeTicks
_FsPimNeighborExpiryTime_Object = MibTableColumn
fsPimNeighborExpiryTime = _FsPimNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 2, 1, 5),
    _FsPimNeighborExpiryTime_Type()
)
fsPimNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimNeighborExpiryTime.setStatus("current")
_FsPimNeighborGenerationId_Type = Integer32
_FsPimNeighborGenerationId_Object = MibTableColumn
fsPimNeighborGenerationId = _FsPimNeighborGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 2, 1, 6),
    _FsPimNeighborGenerationId_Type()
)
fsPimNeighborGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimNeighborGenerationId.setStatus("current")
_FsPimNeighborLanDelay_Type = Integer32
_FsPimNeighborLanDelay_Object = MibTableColumn
fsPimNeighborLanDelay = _FsPimNeighborLanDelay_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 2, 1, 7),
    _FsPimNeighborLanDelay_Type()
)
fsPimNeighborLanDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimNeighborLanDelay.setStatus("current")
_FsPimNeighborDRPriority_Type = Unsigned32
_FsPimNeighborDRPriority_Object = MibTableColumn
fsPimNeighborDRPriority = _FsPimNeighborDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 2, 1, 8),
    _FsPimNeighborDRPriority_Type()
)
fsPimNeighborDRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimNeighborDRPriority.setStatus("current")
_FsPimNeighborOverrideInterval_Type = Integer32
_FsPimNeighborOverrideInterval_Object = MibTableColumn
fsPimNeighborOverrideInterval = _FsPimNeighborOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 2, 1, 9),
    _FsPimNeighborOverrideInterval_Type()
)
fsPimNeighborOverrideInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimNeighborOverrideInterval.setStatus("current")
_FsPimIpMRouteTable_Object = MibTable
fsPimIpMRouteTable = _FsPimIpMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fsPimIpMRouteTable.setStatus("current")
_FsPimIpMRouteEntry_Object = MibTableRow
fsPimIpMRouteEntry = _FsPimIpMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 3, 1)
)
fsPimIpMRouteEntry.setIndexNames(
    (0, "ARICENT-PIM-MIB", "fsPimIpMRouteCompId"),
    (0, "ARICENT-PIM-MIB", "fsPimIpMRouteGroup"),
    (0, "ARICENT-PIM-MIB", "fsPimIpMRouteSource"),
    (0, "ARICENT-PIM-MIB", "fsPimIpMRouteSourceMask"),
)
if mibBuilder.loadTexts:
    fsPimIpMRouteEntry.setStatus("current")


class _FsPimIpMRouteCompId_Type(Integer32):
    """Custom type fsPimIpMRouteCompId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimIpMRouteCompId_Type.__name__ = "Integer32"
_FsPimIpMRouteCompId_Object = MibTableColumn
fsPimIpMRouteCompId = _FsPimIpMRouteCompId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 3, 1, 1),
    _FsPimIpMRouteCompId_Type()
)
fsPimIpMRouteCompId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimIpMRouteCompId.setStatus("current")
_FsPimIpMRouteGroup_Type = IpAddress
_FsPimIpMRouteGroup_Object = MibTableColumn
fsPimIpMRouteGroup = _FsPimIpMRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 3, 1, 2),
    _FsPimIpMRouteGroup_Type()
)
fsPimIpMRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimIpMRouteGroup.setStatus("current")
_FsPimIpMRouteSource_Type = IpAddress
_FsPimIpMRouteSource_Object = MibTableColumn
fsPimIpMRouteSource = _FsPimIpMRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 3, 1, 3),
    _FsPimIpMRouteSource_Type()
)
fsPimIpMRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimIpMRouteSource.setStatus("current")
_FsPimIpMRouteSourceMask_Type = IpAddress
_FsPimIpMRouteSourceMask_Object = MibTableColumn
fsPimIpMRouteSourceMask = _FsPimIpMRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 3, 1, 4),
    _FsPimIpMRouteSourceMask_Type()
)
fsPimIpMRouteSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimIpMRouteSourceMask.setStatus("current")
_FsPimIpMRouteUpstreamNeighbor_Type = IpAddress
_FsPimIpMRouteUpstreamNeighbor_Object = MibTableColumn
fsPimIpMRouteUpstreamNeighbor = _FsPimIpMRouteUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 3, 1, 5),
    _FsPimIpMRouteUpstreamNeighbor_Type()
)
fsPimIpMRouteUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteUpstreamNeighbor.setStatus("current")
_FsPimIpMRouteInIfIndex_Type = Integer32
_FsPimIpMRouteInIfIndex_Object = MibTableColumn
fsPimIpMRouteInIfIndex = _FsPimIpMRouteInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 3, 1, 6),
    _FsPimIpMRouteInIfIndex_Type()
)
fsPimIpMRouteInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteInIfIndex.setStatus("current")
_FsPimIpMRouteUpTime_Type = TimeTicks
_FsPimIpMRouteUpTime_Object = MibTableColumn
fsPimIpMRouteUpTime = _FsPimIpMRouteUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 3, 1, 7),
    _FsPimIpMRouteUpTime_Type()
)
fsPimIpMRouteUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteUpTime.setStatus("current")
_FsPimIpMRoutePkts_Type = Counter32
_FsPimIpMRoutePkts_Object = MibTableColumn
fsPimIpMRoutePkts = _FsPimIpMRoutePkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 3, 1, 8),
    _FsPimIpMRoutePkts_Type()
)
fsPimIpMRoutePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRoutePkts.setStatus("current")
_FsPimIpMRouteUpstreamAssertTimer_Type = TimeTicks
_FsPimIpMRouteUpstreamAssertTimer_Object = MibTableColumn
fsPimIpMRouteUpstreamAssertTimer = _FsPimIpMRouteUpstreamAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 3, 1, 9),
    _FsPimIpMRouteUpstreamAssertTimer_Type()
)
fsPimIpMRouteUpstreamAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteUpstreamAssertTimer.setStatus("current")
_FsPimIpMRouteAssertMetric_Type = Integer32
_FsPimIpMRouteAssertMetric_Object = MibTableColumn
fsPimIpMRouteAssertMetric = _FsPimIpMRouteAssertMetric_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 3, 1, 10),
    _FsPimIpMRouteAssertMetric_Type()
)
fsPimIpMRouteAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteAssertMetric.setStatus("current")
_FsPimIpMRouteAssertMetricPref_Type = Integer32
_FsPimIpMRouteAssertMetricPref_Object = MibTableColumn
fsPimIpMRouteAssertMetricPref = _FsPimIpMRouteAssertMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 3, 1, 11),
    _FsPimIpMRouteAssertMetricPref_Type()
)
fsPimIpMRouteAssertMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteAssertMetricPref.setStatus("current")
_FsPimIpMRouteAssertRPTBit_Type = TruthValue
_FsPimIpMRouteAssertRPTBit_Object = MibTableColumn
fsPimIpMRouteAssertRPTBit = _FsPimIpMRouteAssertRPTBit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 3, 1, 12),
    _FsPimIpMRouteAssertRPTBit_Type()
)
fsPimIpMRouteAssertRPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteAssertRPTBit.setStatus("current")
_FsPimIpMRouteTimerFlags_Type = Integer32
_FsPimIpMRouteTimerFlags_Object = MibTableColumn
fsPimIpMRouteTimerFlags = _FsPimIpMRouteTimerFlags_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 3, 1, 13),
    _FsPimIpMRouteTimerFlags_Type()
)
fsPimIpMRouteTimerFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteTimerFlags.setStatus("current")
_FsPimIpMRouteFlags_Type = Integer32
_FsPimIpMRouteFlags_Object = MibTableColumn
fsPimIpMRouteFlags = _FsPimIpMRouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 3, 1, 14),
    _FsPimIpMRouteFlags_Type()
)
fsPimIpMRouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteFlags.setStatus("current")
_FsPimIpMRouteNextHopTable_Object = MibTable
fsPimIpMRouteNextHopTable = _FsPimIpMRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 4)
)
if mibBuilder.loadTexts:
    fsPimIpMRouteNextHopTable.setStatus("current")
_FsPimIpMRouteNextHopEntry_Object = MibTableRow
fsPimIpMRouteNextHopEntry = _FsPimIpMRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 4, 1)
)
fsPimIpMRouteNextHopEntry.setIndexNames(
    (0, "ARICENT-PIM-MIB", "fsPimIpMRouteNextHopCompId"),
    (0, "ARICENT-PIM-MIB", "fsPimIpMRouteNextHopGroup"),
    (0, "ARICENT-PIM-MIB", "fsPimIpMRouteNextHopSource"),
    (0, "ARICENT-PIM-MIB", "fsPimIpMRouteNextHopSourceMask"),
    (0, "ARICENT-PIM-MIB", "fsPimIpMRouteNextHopIfIndex"),
    (0, "ARICENT-PIM-MIB", "fsPimIpMRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    fsPimIpMRouteNextHopEntry.setStatus("current")


class _FsPimIpMRouteNextHopCompId_Type(Integer32):
    """Custom type fsPimIpMRouteNextHopCompId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimIpMRouteNextHopCompId_Type.__name__ = "Integer32"
_FsPimIpMRouteNextHopCompId_Object = MibTableColumn
fsPimIpMRouteNextHopCompId = _FsPimIpMRouteNextHopCompId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 4, 1, 1),
    _FsPimIpMRouteNextHopCompId_Type()
)
fsPimIpMRouteNextHopCompId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimIpMRouteNextHopCompId.setStatus("current")
_FsPimIpMRouteNextHopGroup_Type = IpAddress
_FsPimIpMRouteNextHopGroup_Object = MibTableColumn
fsPimIpMRouteNextHopGroup = _FsPimIpMRouteNextHopGroup_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 4, 1, 2),
    _FsPimIpMRouteNextHopGroup_Type()
)
fsPimIpMRouteNextHopGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimIpMRouteNextHopGroup.setStatus("current")
_FsPimIpMRouteNextHopSource_Type = IpAddress
_FsPimIpMRouteNextHopSource_Object = MibTableColumn
fsPimIpMRouteNextHopSource = _FsPimIpMRouteNextHopSource_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 4, 1, 3),
    _FsPimIpMRouteNextHopSource_Type()
)
fsPimIpMRouteNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimIpMRouteNextHopSource.setStatus("current")
_FsPimIpMRouteNextHopSourceMask_Type = IpAddress
_FsPimIpMRouteNextHopSourceMask_Object = MibTableColumn
fsPimIpMRouteNextHopSourceMask = _FsPimIpMRouteNextHopSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 4, 1, 4),
    _FsPimIpMRouteNextHopSourceMask_Type()
)
fsPimIpMRouteNextHopSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimIpMRouteNextHopSourceMask.setStatus("current")


class _FsPimIpMRouteNextHopIfIndex_Type(Integer32):
    """Custom type fsPimIpMRouteNextHopIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsPimIpMRouteNextHopIfIndex_Type.__name__ = "Integer32"
_FsPimIpMRouteNextHopIfIndex_Object = MibTableColumn
fsPimIpMRouteNextHopIfIndex = _FsPimIpMRouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 4, 1, 5),
    _FsPimIpMRouteNextHopIfIndex_Type()
)
fsPimIpMRouteNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimIpMRouteNextHopIfIndex.setStatus("current")
_FsPimIpMRouteNextHopAddress_Type = IpAddress
_FsPimIpMRouteNextHopAddress_Object = MibTableColumn
fsPimIpMRouteNextHopAddress = _FsPimIpMRouteNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 4, 1, 6),
    _FsPimIpMRouteNextHopAddress_Type()
)
fsPimIpMRouteNextHopAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimIpMRouteNextHopAddress.setStatus("current")


class _FsPimIpMRouteNextHopPruneReason_Type(Integer32):
    """Custom type fsPimIpMRouteNextHopPruneReason based on Integer32"""
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


_FsPimIpMRouteNextHopPruneReason_Type.__name__ = "Integer32"
_FsPimIpMRouteNextHopPruneReason_Object = MibTableColumn
fsPimIpMRouteNextHopPruneReason = _FsPimIpMRouteNextHopPruneReason_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 4, 1, 7),
    _FsPimIpMRouteNextHopPruneReason_Type()
)
fsPimIpMRouteNextHopPruneReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteNextHopPruneReason.setStatus("current")


class _FsPimIpMRouteNextHopState_Type(Integer32):
    """Custom type fsPimIpMRouteNextHopState based on Integer32"""
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


_FsPimIpMRouteNextHopState_Type.__name__ = "Integer32"
_FsPimIpMRouteNextHopState_Object = MibTableColumn
fsPimIpMRouteNextHopState = _FsPimIpMRouteNextHopState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 4, 1, 8),
    _FsPimIpMRouteNextHopState_Type()
)
fsPimIpMRouteNextHopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPimIpMRouteNextHopState.setStatus("current")
_FsPimCandidateRPTable_Object = MibTable
fsPimCandidateRPTable = _FsPimCandidateRPTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 6)
)
if mibBuilder.loadTexts:
    fsPimCandidateRPTable.setStatus("current")
_FsPimCandidateRPEntry_Object = MibTableRow
fsPimCandidateRPEntry = _FsPimCandidateRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 6, 1)
)
fsPimCandidateRPEntry.setIndexNames(
    (0, "ARICENT-PIM-MIB", "fsPimCandidateRPCompId"),
    (0, "ARICENT-PIM-MIB", "fsPimCandidateRPGroupAddress"),
    (0, "ARICENT-PIM-MIB", "fsPimCandidateRPGroupMask"),
    (0, "ARICENT-PIM-MIB", "fsPimCandidateRPAddress"),
)
if mibBuilder.loadTexts:
    fsPimCandidateRPEntry.setStatus("current")


class _FsPimCandidateRPCompId_Type(Integer32):
    """Custom type fsPimCandidateRPCompId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimCandidateRPCompId_Type.__name__ = "Integer32"
_FsPimCandidateRPCompId_Object = MibTableColumn
fsPimCandidateRPCompId = _FsPimCandidateRPCompId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 6, 1, 1),
    _FsPimCandidateRPCompId_Type()
)
fsPimCandidateRPCompId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCandidateRPCompId.setStatus("current")
_FsPimCandidateRPGroupAddress_Type = IpAddress
_FsPimCandidateRPGroupAddress_Object = MibTableColumn
fsPimCandidateRPGroupAddress = _FsPimCandidateRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 6, 1, 2),
    _FsPimCandidateRPGroupAddress_Type()
)
fsPimCandidateRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCandidateRPGroupAddress.setStatus("current")
_FsPimCandidateRPGroupMask_Type = IpAddress
_FsPimCandidateRPGroupMask_Object = MibTableColumn
fsPimCandidateRPGroupMask = _FsPimCandidateRPGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 6, 1, 3),
    _FsPimCandidateRPGroupMask_Type()
)
fsPimCandidateRPGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCandidateRPGroupMask.setStatus("current")
_FsPimCandidateRPAddress_Type = IpAddress
_FsPimCandidateRPAddress_Object = MibTableColumn
fsPimCandidateRPAddress = _FsPimCandidateRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 6, 1, 4),
    _FsPimCandidateRPAddress_Type()
)
fsPimCandidateRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimCandidateRPAddress.setStatus("current")


class _FsPimCandidateRPPriority_Type(Integer32):
    """Custom type fsPimCandidateRPPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPimCandidateRPPriority_Type.__name__ = "Integer32"
_FsPimCandidateRPPriority_Object = MibTableColumn
fsPimCandidateRPPriority = _FsPimCandidateRPPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 6, 1, 5),
    _FsPimCandidateRPPriority_Type()
)
fsPimCandidateRPPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCandidateRPPriority.setStatus("current")
_FsPimCandidateRPRowStatus_Type = RowStatus
_FsPimCandidateRPRowStatus_Object = MibTableColumn
fsPimCandidateRPRowStatus = _FsPimCandidateRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 6, 1, 6),
    _FsPimCandidateRPRowStatus_Type()
)
fsPimCandidateRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimCandidateRPRowStatus.setStatus("current")
_FsPimStaticRPSetTable_Object = MibTable
fsPimStaticRPSetTable = _FsPimStaticRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 7)
)
if mibBuilder.loadTexts:
    fsPimStaticRPSetTable.setStatus("current")
_FsPimStaticRPSetEntry_Object = MibTableRow
fsPimStaticRPSetEntry = _FsPimStaticRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 7, 1)
)
fsPimStaticRPSetEntry.setIndexNames(
    (0, "ARICENT-PIM-MIB", "fsPimStaticRPSetCompId"),
    (0, "ARICENT-PIM-MIB", "fsPimStaticRPSetGroupAddress"),
    (0, "ARICENT-PIM-MIB", "fsPimStaticRPSetGroupMask"),
)
if mibBuilder.loadTexts:
    fsPimStaticRPSetEntry.setStatus("current")


class _FsPimStaticRPSetCompId_Type(Integer32):
    """Custom type fsPimStaticRPSetCompId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimStaticRPSetCompId_Type.__name__ = "Integer32"
_FsPimStaticRPSetCompId_Object = MibTableColumn
fsPimStaticRPSetCompId = _FsPimStaticRPSetCompId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 7, 1, 1),
    _FsPimStaticRPSetCompId_Type()
)
fsPimStaticRPSetCompId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStaticRPSetCompId.setStatus("current")
_FsPimStaticRPSetGroupAddress_Type = IpAddress
_FsPimStaticRPSetGroupAddress_Object = MibTableColumn
fsPimStaticRPSetGroupAddress = _FsPimStaticRPSetGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 7, 1, 2),
    _FsPimStaticRPSetGroupAddress_Type()
)
fsPimStaticRPSetGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStaticRPSetGroupAddress.setStatus("current")
_FsPimStaticRPSetGroupMask_Type = IpAddress
_FsPimStaticRPSetGroupMask_Object = MibTableColumn
fsPimStaticRPSetGroupMask = _FsPimStaticRPSetGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 7, 1, 3),
    _FsPimStaticRPSetGroupMask_Type()
)
fsPimStaticRPSetGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimStaticRPSetGroupMask.setStatus("current")
_FsPimStaticRPAddress_Type = IpAddress
_FsPimStaticRPAddress_Object = MibTableColumn
fsPimStaticRPAddress = _FsPimStaticRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 7, 1, 4),
    _FsPimStaticRPAddress_Type()
)
fsPimStaticRPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimStaticRPAddress.setStatus("current")
_FsPimStaticRPRowStatus_Type = RowStatus
_FsPimStaticRPRowStatus_Object = MibTableColumn
fsPimStaticRPRowStatus = _FsPimStaticRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 7, 1, 5),
    _FsPimStaticRPRowStatus_Type()
)
fsPimStaticRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPimStaticRPRowStatus.setStatus("current")
_FsPimComponentModeTable_Object = MibTable
fsPimComponentModeTable = _FsPimComponentModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 8)
)
if mibBuilder.loadTexts:
    fsPimComponentModeTable.setStatus("current")
_FsPimComponentModeEntry_Object = MibTableRow
fsPimComponentModeEntry = _FsPimComponentModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 8, 1)
)
fsPimComponentModeEntry.setIndexNames(
    (0, "ARICENT-PIM-MIB", "fsPimComponentId"),
)
if mibBuilder.loadTexts:
    fsPimComponentModeEntry.setStatus("current")


class _FsPimComponentId_Type(Integer32):
    """Custom type fsPimComponentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimComponentId_Type.__name__ = "Integer32"
_FsPimComponentId_Object = MibTableColumn
fsPimComponentId = _FsPimComponentId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 8, 1, 1),
    _FsPimComponentId_Type()
)
fsPimComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimComponentId.setStatus("current")


class _FsPimComponentMode_Type(Integer32):
    """Custom type fsPimComponentMode based on Integer32"""
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


_FsPimComponentMode_Type.__name__ = "Integer32"
_FsPimComponentMode_Object = MibTableColumn
fsPimComponentMode = _FsPimComponentMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 8, 1, 2),
    _FsPimComponentMode_Type()
)
fsPimComponentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimComponentMode.setStatus("current")


class _FsPimCompGraftRetryCount_Type(Integer32):
    """Custom type fsPimCompGraftRetryCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPimCompGraftRetryCount_Type.__name__ = "Integer32"
_FsPimCompGraftRetryCount_Object = MibTableColumn
fsPimCompGraftRetryCount = _FsPimCompGraftRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 8, 1, 3),
    _FsPimCompGraftRetryCount_Type()
)
fsPimCompGraftRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimCompGraftRetryCount.setStatus("current")
_FsPimRegChkSumCfgTable_Object = MibTable
fsPimRegChkSumCfgTable = _FsPimRegChkSumCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 9)
)
if mibBuilder.loadTexts:
    fsPimRegChkSumCfgTable.setStatus("current")
_FsPimRegChkSumCfgEntry_Object = MibTableRow
fsPimRegChkSumCfgEntry = _FsPimRegChkSumCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 9, 1)
)
fsPimRegChkSumCfgEntry.setIndexNames(
    (0, "ARICENT-PIM-MIB", "fsPimRegChkSumTblCompId"),
    (0, "ARICENT-PIM-MIB", "fsPimRegChkSumTblRPAddress"),
)
if mibBuilder.loadTexts:
    fsPimRegChkSumCfgEntry.setStatus("current")


class _FsPimRegChkSumTblCompId_Type(Integer32):
    """Custom type fsPimRegChkSumTblCompId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsPimRegChkSumTblCompId_Type.__name__ = "Integer32"
_FsPimRegChkSumTblCompId_Object = MibTableColumn
fsPimRegChkSumTblCompId = _FsPimRegChkSumTblCompId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 9, 1, 1),
    _FsPimRegChkSumTblCompId_Type()
)
fsPimRegChkSumTblCompId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimRegChkSumTblCompId.setStatus("current")
_FsPimRegChkSumTblRPAddress_Type = IpAddress
_FsPimRegChkSumTblRPAddress_Object = MibTableColumn
fsPimRegChkSumTblRPAddress = _FsPimRegChkSumTblRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 9, 1, 2),
    _FsPimRegChkSumTblRPAddress_Type()
)
fsPimRegChkSumTblRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPimRegChkSumTblRPAddress.setStatus("current")


class _FsPimRPChkSumStatus_Type(Integer32):
    """Custom type fsPimRPChkSumStatus based on Integer32"""
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


_FsPimRPChkSumStatus_Type.__name__ = "Integer32"
_FsPimRPChkSumStatus_Object = MibTableColumn
fsPimRPChkSumStatus = _FsPimRPChkSumStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 2, 9, 1, 3),
    _FsPimRPChkSumStatus_Type()
)
fsPimRPChkSumStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPimRPChkSumStatus.setStatus("current")
_FuturePimTraps_ObjectIdentity = ObjectIdentity
futurePimTraps = _FuturePimTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 20, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-PIM-MIB",
    **{"Status": Status,
       "fsPimMIB": fsPimMIB,
       "fsPimMIBObjects": fsPimMIBObjects,
       "futurePimScalars": futurePimScalars,
       "fsPimVersionString": fsPimVersionString,
       "fsPimSPTGroupThreshold": fsPimSPTGroupThreshold,
       "fsPimSPTSourceThreshold": fsPimSPTSourceThreshold,
       "fsPimSPTSwitchingPeriod": fsPimSPTSwitchingPeriod,
       "fsPimSPTRpThreshold": fsPimSPTRpThreshold,
       "fsPimSPTRpSwitchingPeriod": fsPimSPTRpSwitchingPeriod,
       "fsPimRegStopRateLimitingPeriod": fsPimRegStopRateLimitingPeriod,
       "fsPimMemoryAllocFailCount": fsPimMemoryAllocFailCount,
       "fsPimGlobalTrace": fsPimGlobalTrace,
       "fsPimGlobalDebug": fsPimGlobalDebug,
       "fsPimPmbrStatus": fsPimPmbrStatus,
       "fsPimRouterMode": fsPimRouterMode,
       "fsPimStaticRpEnabled": fsPimStaticRpEnabled,
       "fsPimStatus": fsPimStatus,
       "futurePimTables": futurePimTables,
       "fsPimInterfaceTable": fsPimInterfaceTable,
       "fsPimInterfaceEntry": fsPimInterfaceEntry,
       "fsPimInterfaceIfIndex": fsPimInterfaceIfIndex,
       "fsPimInterfaceCompId": fsPimInterfaceCompId,
       "fsPimInterfaceDRPriority": fsPimInterfaceDRPriority,
       "fsPimInterfaceHelloHoldTime": fsPimInterfaceHelloHoldTime,
       "fsPimInterfaceLanPruneDelayPresent": fsPimInterfaceLanPruneDelayPresent,
       "fsPimInterfaceLanDelay": fsPimInterfaceLanDelay,
       "fsPimInterfaceOverrideInterval": fsPimInterfaceOverrideInterval,
       "fsPimInterfaceGenerationId": fsPimInterfaceGenerationId,
       "fsPimInterfaceSuppressionInterval": fsPimInterfaceSuppressionInterval,
       "fsPimInterfaceAdminStatus": fsPimInterfaceAdminStatus,
       "fsPimInterfaceBorderBit": fsPimInterfaceBorderBit,
       "fsPimNeighborTable": fsPimNeighborTable,
       "fsPimNeighborEntry": fsPimNeighborEntry,
       "fsPimNeighborAddress": fsPimNeighborAddress,
       "fsPimNeighborCompId": fsPimNeighborCompId,
       "fsPimNeighborIfIndex": fsPimNeighborIfIndex,
       "fsPimNeighborUpTime": fsPimNeighborUpTime,
       "fsPimNeighborExpiryTime": fsPimNeighborExpiryTime,
       "fsPimNeighborGenerationId": fsPimNeighborGenerationId,
       "fsPimNeighborLanDelay": fsPimNeighborLanDelay,
       "fsPimNeighborDRPriority": fsPimNeighborDRPriority,
       "fsPimNeighborOverrideInterval": fsPimNeighborOverrideInterval,
       "fsPimIpMRouteTable": fsPimIpMRouteTable,
       "fsPimIpMRouteEntry": fsPimIpMRouteEntry,
       "fsPimIpMRouteCompId": fsPimIpMRouteCompId,
       "fsPimIpMRouteGroup": fsPimIpMRouteGroup,
       "fsPimIpMRouteSource": fsPimIpMRouteSource,
       "fsPimIpMRouteSourceMask": fsPimIpMRouteSourceMask,
       "fsPimIpMRouteUpstreamNeighbor": fsPimIpMRouteUpstreamNeighbor,
       "fsPimIpMRouteInIfIndex": fsPimIpMRouteInIfIndex,
       "fsPimIpMRouteUpTime": fsPimIpMRouteUpTime,
       "fsPimIpMRoutePkts": fsPimIpMRoutePkts,
       "fsPimIpMRouteUpstreamAssertTimer": fsPimIpMRouteUpstreamAssertTimer,
       "fsPimIpMRouteAssertMetric": fsPimIpMRouteAssertMetric,
       "fsPimIpMRouteAssertMetricPref": fsPimIpMRouteAssertMetricPref,
       "fsPimIpMRouteAssertRPTBit": fsPimIpMRouteAssertRPTBit,
       "fsPimIpMRouteTimerFlags": fsPimIpMRouteTimerFlags,
       "fsPimIpMRouteFlags": fsPimIpMRouteFlags,
       "fsPimIpMRouteNextHopTable": fsPimIpMRouteNextHopTable,
       "fsPimIpMRouteNextHopEntry": fsPimIpMRouteNextHopEntry,
       "fsPimIpMRouteNextHopCompId": fsPimIpMRouteNextHopCompId,
       "fsPimIpMRouteNextHopGroup": fsPimIpMRouteNextHopGroup,
       "fsPimIpMRouteNextHopSource": fsPimIpMRouteNextHopSource,
       "fsPimIpMRouteNextHopSourceMask": fsPimIpMRouteNextHopSourceMask,
       "fsPimIpMRouteNextHopIfIndex": fsPimIpMRouteNextHopIfIndex,
       "fsPimIpMRouteNextHopAddress": fsPimIpMRouteNextHopAddress,
       "fsPimIpMRouteNextHopPruneReason": fsPimIpMRouteNextHopPruneReason,
       "fsPimIpMRouteNextHopState": fsPimIpMRouteNextHopState,
       "fsPimCandidateRPTable": fsPimCandidateRPTable,
       "fsPimCandidateRPEntry": fsPimCandidateRPEntry,
       "fsPimCandidateRPCompId": fsPimCandidateRPCompId,
       "fsPimCandidateRPGroupAddress": fsPimCandidateRPGroupAddress,
       "fsPimCandidateRPGroupMask": fsPimCandidateRPGroupMask,
       "fsPimCandidateRPAddress": fsPimCandidateRPAddress,
       "fsPimCandidateRPPriority": fsPimCandidateRPPriority,
       "fsPimCandidateRPRowStatus": fsPimCandidateRPRowStatus,
       "fsPimStaticRPSetTable": fsPimStaticRPSetTable,
       "fsPimStaticRPSetEntry": fsPimStaticRPSetEntry,
       "fsPimStaticRPSetCompId": fsPimStaticRPSetCompId,
       "fsPimStaticRPSetGroupAddress": fsPimStaticRPSetGroupAddress,
       "fsPimStaticRPSetGroupMask": fsPimStaticRPSetGroupMask,
       "fsPimStaticRPAddress": fsPimStaticRPAddress,
       "fsPimStaticRPRowStatus": fsPimStaticRPRowStatus,
       "fsPimComponentModeTable": fsPimComponentModeTable,
       "fsPimComponentModeEntry": fsPimComponentModeEntry,
       "fsPimComponentId": fsPimComponentId,
       "fsPimComponentMode": fsPimComponentMode,
       "fsPimCompGraftRetryCount": fsPimCompGraftRetryCount,
       "fsPimRegChkSumCfgTable": fsPimRegChkSumCfgTable,
       "fsPimRegChkSumCfgEntry": fsPimRegChkSumCfgEntry,
       "fsPimRegChkSumTblCompId": fsPimRegChkSumTblCompId,
       "fsPimRegChkSumTblRPAddress": fsPimRegChkSumTblRPAddress,
       "fsPimRPChkSumStatus": fsPimRPChkSumStatus,
       "futurePimTraps": futurePimTraps}
)
