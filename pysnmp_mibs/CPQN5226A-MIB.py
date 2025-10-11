# SNMP MIB module (CPQN5226A-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/CPQN5226A-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:33:26 2025
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

(CpqnRowStatus,) = mibBuilder.importSymbols(
    "CPQNUNIF-MIB",
    "CpqnRowStatus")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Compaq_ObjectIdentity = ObjectIdentity
compaq = _Compaq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232)
)
_Compaq_dallas_npd_ObjectIdentity = ObjectIdentity
compaq_dallas_npd = _Compaq_dallas_npd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101)
)
_SwitchedMedia_ObjectIdentity = ObjectIdentity
switchedMedia = _SwitchedMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2)
)
_Cpqn52nn_ObjectIdentity = ObjectIdentity
cpqn52nn = _Cpqn52nn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2)
)
_Cpqn52nnOIDInfo_ObjectIdentity = ObjectIdentity
cpqn52nnOIDInfo = _Cpqn52nnOIDInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 1)
)
_Cpqn5226_ObjectIdentity = ObjectIdentity
cpqn5226 = _Cpqn5226_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 1, 1)
)
_Cpqn5226A_ObjectIdentity = ObjectIdentity
cpqn5226A = _Cpqn5226A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 1, 3)
)
_Cpqn52nnModuleInfo_ObjectIdentity = ObjectIdentity
cpqn52nnModuleInfo = _Cpqn52nnModuleInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 2)
)


class _Cpqn52nnVT100ScreenRefresh_Type(Integer32):
    """Custom type cpqn52nnVT100ScreenRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cpqn52nnVT100ScreenRefresh_Type.__name__ = "Integer32"
_Cpqn52nnVT100ScreenRefresh_Object = MibScalar
cpqn52nnVT100ScreenRefresh = _Cpqn52nnVT100ScreenRefresh_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 2, 1),
    _Cpqn52nnVT100ScreenRefresh_Type()
)
cpqn52nnVT100ScreenRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnVT100ScreenRefresh.setStatus("mandatory")
_Cpqn52nnBooterWriteCycles_Type = Integer32
_Cpqn52nnBooterWriteCycles_Object = MibScalar
cpqn52nnBooterWriteCycles = _Cpqn52nnBooterWriteCycles_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 2, 2),
    _Cpqn52nnBooterWriteCycles_Type()
)
cpqn52nnBooterWriteCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnBooterWriteCycles.setStatus("mandatory")
_Cpqn52nnRuntimeWriteCycles_Type = Integer32
_Cpqn52nnRuntimeWriteCycles_Object = MibScalar
cpqn52nnRuntimeWriteCycles = _Cpqn52nnRuntimeWriteCycles_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 2, 3),
    _Cpqn52nnRuntimeWriteCycles_Type()
)
cpqn52nnRuntimeWriteCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnRuntimeWriteCycles.setStatus("mandatory")


class _Cpqn52nnSwitchModeType_Type(Integer32):
    """Custom type cpqn52nnSwitchModeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("store-and-forward", 1),
          ("cut-through", 2),
          ("fragment-free", 3))
    )


_Cpqn52nnSwitchModeType_Type.__name__ = "Integer32"
_Cpqn52nnSwitchModeType_Object = MibScalar
cpqn52nnSwitchModeType = _Cpqn52nnSwitchModeType_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 2, 4),
    _Cpqn52nnSwitchModeType_Type()
)
cpqn52nnSwitchModeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnSwitchModeType.setStatus("mandatory")
_Cpqn52nnCreateTimeout_Type = Integer32
_Cpqn52nnCreateTimeout_Object = MibScalar
cpqn52nnCreateTimeout = _Cpqn52nnCreateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 2, 5),
    _Cpqn52nnCreateTimeout_Type()
)
cpqn52nnCreateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnCreateTimeout.setStatus("mandatory")
_Cpqn52nnPowerSupplyTable_Object = MibTable
cpqn52nnPowerSupplyTable = _Cpqn52nnPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 2, 6)
)
if mibBuilder.loadTexts:
    cpqn52nnPowerSupplyTable.setStatus("mandatory")
_Cpqn52nnPowerSupplyEntry_Object = MibTableRow
cpqn52nnPowerSupplyEntry = _Cpqn52nnPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 2, 6, 1)
)
cpqn52nnPowerSupplyEntry.setIndexNames(
    (0, "CPQN5226A-MIB", "cpqn52nnPsIndex"),
)
if mibBuilder.loadTexts:
    cpqn52nnPowerSupplyEntry.setStatus("mandatory")


class _Cpqn52nnPsIndex_Type(Integer32):
    """Custom type cpqn52nnPsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("power-supply-a", 1),
          ("power-supply-b", 2))
    )


_Cpqn52nnPsIndex_Type.__name__ = "Integer32"
_Cpqn52nnPsIndex_Object = MibTableColumn
cpqn52nnPsIndex = _Cpqn52nnPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 2, 6, 1, 1),
    _Cpqn52nnPsIndex_Type()
)
cpqn52nnPsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnPsIndex.setStatus("mandatory")


class _Cpqn52nnPsStatus_Type(Integer32):
    """Custom type cpqn52nnPsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("bad", 2),
          ("not-present", 3))
    )


_Cpqn52nnPsStatus_Type.__name__ = "Integer32"
_Cpqn52nnPsStatus_Object = MibTableColumn
cpqn52nnPsStatus = _Cpqn52nnPsStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 2, 6, 1, 2),
    _Cpqn52nnPsStatus_Type()
)
cpqn52nnPsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnPsStatus.setStatus("mandatory")
_Cpqn52nnMemoryInfo_ObjectIdentity = ObjectIdentity
cpqn52nnMemoryInfo = _Cpqn52nnMemoryInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3)
)
_Cpqn52nnHashInfo_ObjectIdentity = ObjectIdentity
cpqn52nnHashInfo = _Cpqn52nnHashInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 1)
)


class _Cpqn52nnHashTableSize_Type(Integer32):
    """Custom type cpqn52nnHashTableSize based on Integer32"""
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
        *(("eight-K", 1),
          ("sixteen-K", 2),
          ("thirty-two-K", 3),
          ("sixty-four-K", 4))
    )


_Cpqn52nnHashTableSize_Type.__name__ = "Integer32"
_Cpqn52nnHashTableSize_Object = MibScalar
cpqn52nnHashTableSize = _Cpqn52nnHashTableSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 1, 1),
    _Cpqn52nnHashTableSize_Type()
)
cpqn52nnHashTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnHashTableSize.setStatus("mandatory")
_Cpqn52nnRmonMemory_ObjectIdentity = ObjectIdentity
cpqn52nnRmonMemory = _Cpqn52nnRmonMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 2)
)
_Cpqn52nnMaxMemory_Type = Integer32
_Cpqn52nnMaxMemory_Object = MibScalar
cpqn52nnMaxMemory = _Cpqn52nnMaxMemory_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 2, 1),
    _Cpqn52nnMaxMemory_Type()
)
cpqn52nnMaxMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnMaxMemory.setStatus("mandatory")
_Cpqn52nnMemAllocFailure_Type = Integer32
_Cpqn52nnMemAllocFailure_Object = MibScalar
cpqn52nnMemAllocFailure = _Cpqn52nnMemAllocFailure_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 2, 2),
    _Cpqn52nnMemAllocFailure_Type()
)
cpqn52nnMemAllocFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnMemAllocFailure.setStatus("mandatory")
_Cpqn52nnRmonMemoryCeiling_Type = Integer32
_Cpqn52nnRmonMemoryCeiling_Object = MibScalar
cpqn52nnRmonMemoryCeiling = _Cpqn52nnRmonMemoryCeiling_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 2, 3),
    _Cpqn52nnRmonMemoryCeiling_Type()
)
cpqn52nnRmonMemoryCeiling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnRmonMemoryCeiling.setStatus("mandatory")
_Cpqn52nnStatisticsMemoryCeiling_Type = Integer32
_Cpqn52nnStatisticsMemoryCeiling_Object = MibScalar
cpqn52nnStatisticsMemoryCeiling = _Cpqn52nnStatisticsMemoryCeiling_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 2, 4),
    _Cpqn52nnStatisticsMemoryCeiling_Type()
)
cpqn52nnStatisticsMemoryCeiling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnStatisticsMemoryCeiling.setStatus("mandatory")
_Cpqn52nnHistoryMemoryCeiling_Type = Integer32
_Cpqn52nnHistoryMemoryCeiling_Object = MibScalar
cpqn52nnHistoryMemoryCeiling = _Cpqn52nnHistoryMemoryCeiling_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 2, 5),
    _Cpqn52nnHistoryMemoryCeiling_Type()
)
cpqn52nnHistoryMemoryCeiling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnHistoryMemoryCeiling.setStatus("mandatory")
_Cpqn52nnAlarmMemoryCeiling_Type = Integer32
_Cpqn52nnAlarmMemoryCeiling_Object = MibScalar
cpqn52nnAlarmMemoryCeiling = _Cpqn52nnAlarmMemoryCeiling_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 2, 6),
    _Cpqn52nnAlarmMemoryCeiling_Type()
)
cpqn52nnAlarmMemoryCeiling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnAlarmMemoryCeiling.setStatus("mandatory")
_Cpqn52nnEventMemoryCeiling_Type = Integer32
_Cpqn52nnEventMemoryCeiling_Object = MibScalar
cpqn52nnEventMemoryCeiling = _Cpqn52nnEventMemoryCeiling_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 2, 7),
    _Cpqn52nnEventMemoryCeiling_Type()
)
cpqn52nnEventMemoryCeiling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnEventMemoryCeiling.setStatus("mandatory")
_Cpqn52nnRmonMemoryUsed_Type = Integer32
_Cpqn52nnRmonMemoryUsed_Object = MibScalar
cpqn52nnRmonMemoryUsed = _Cpqn52nnRmonMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 2, 8),
    _Cpqn52nnRmonMemoryUsed_Type()
)
cpqn52nnRmonMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnRmonMemoryUsed.setStatus("mandatory")
_Cpqn52nnStatisticsMemoryUsed_Type = Integer32
_Cpqn52nnStatisticsMemoryUsed_Object = MibScalar
cpqn52nnStatisticsMemoryUsed = _Cpqn52nnStatisticsMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 2, 9),
    _Cpqn52nnStatisticsMemoryUsed_Type()
)
cpqn52nnStatisticsMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnStatisticsMemoryUsed.setStatus("mandatory")
_Cpqn52nnHistoryMemoryUsed_Type = Integer32
_Cpqn52nnHistoryMemoryUsed_Object = MibScalar
cpqn52nnHistoryMemoryUsed = _Cpqn52nnHistoryMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 2, 10),
    _Cpqn52nnHistoryMemoryUsed_Type()
)
cpqn52nnHistoryMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnHistoryMemoryUsed.setStatus("mandatory")
_Cpqn52nnAlarmMemoryUsed_Type = Integer32
_Cpqn52nnAlarmMemoryUsed_Object = MibScalar
cpqn52nnAlarmMemoryUsed = _Cpqn52nnAlarmMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 2, 11),
    _Cpqn52nnAlarmMemoryUsed_Type()
)
cpqn52nnAlarmMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnAlarmMemoryUsed.setStatus("mandatory")
_Cpqn52nnEventMemoryUsed_Type = Integer32
_Cpqn52nnEventMemoryUsed_Object = MibScalar
cpqn52nnEventMemoryUsed = _Cpqn52nnEventMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 2, 12),
    _Cpqn52nnEventMemoryUsed_Type()
)
cpqn52nnEventMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnEventMemoryUsed.setStatus("mandatory")
_Cpqn52nnMemoryThreshold_ObjectIdentity = ObjectIdentity
cpqn52nnMemoryThreshold = _Cpqn52nnMemoryThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3)
)
_Cpqn52nnMaxPktMemory_Type = Integer32
_Cpqn52nnMaxPktMemory_Object = MibScalar
cpqn52nnMaxPktMemory = _Cpqn52nnMaxPktMemory_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 1),
    _Cpqn52nnMaxPktMemory_Type()
)
cpqn52nnMaxPktMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnMaxPktMemory.setStatus("mandatory")


class _Cpqn52nnGlobalMemThreshTrapEnable_Type(Integer32):
    """Custom type cpqn52nnGlobalMemThreshTrapEnable based on Integer32"""
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


_Cpqn52nnGlobalMemThreshTrapEnable_Type.__name__ = "Integer32"
_Cpqn52nnGlobalMemThreshTrapEnable_Object = MibScalar
cpqn52nnGlobalMemThreshTrapEnable = _Cpqn52nnGlobalMemThreshTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 2),
    _Cpqn52nnGlobalMemThreshTrapEnable_Type()
)
cpqn52nnGlobalMemThreshTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnGlobalMemThreshTrapEnable.setStatus("mandatory")


class _Cpqn52nnBcastMemThreshEnable_Type(Integer32):
    """Custom type cpqn52nnBcastMemThreshEnable based on Integer32"""
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


_Cpqn52nnBcastMemThreshEnable_Type.__name__ = "Integer32"
_Cpqn52nnBcastMemThreshEnable_Object = MibScalar
cpqn52nnBcastMemThreshEnable = _Cpqn52nnBcastMemThreshEnable_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 3),
    _Cpqn52nnBcastMemThreshEnable_Type()
)
cpqn52nnBcastMemThreshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnBcastMemThreshEnable.setStatus("mandatory")


class _Cpqn52nnBcastPktCeiling_Type(Integer32):
    """Custom type cpqn52nnBcastPktCeiling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Cpqn52nnBcastPktCeiling_Type.__name__ = "Integer32"
_Cpqn52nnBcastPktCeiling_Object = MibScalar
cpqn52nnBcastPktCeiling = _Cpqn52nnBcastPktCeiling_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 4),
    _Cpqn52nnBcastPktCeiling_Type()
)
cpqn52nnBcastPktCeiling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnBcastPktCeiling.setStatus("mandatory")


class _Cpqn52nnBcastHysteresisCtl_Type(Integer32):
    """Custom type cpqn52nnBcastHysteresisCtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cpqn52nnBcastHysteresisCtl_Type.__name__ = "Integer32"
_Cpqn52nnBcastHysteresisCtl_Object = MibScalar
cpqn52nnBcastHysteresisCtl = _Cpqn52nnBcastHysteresisCtl_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 5),
    _Cpqn52nnBcastHysteresisCtl_Type()
)
cpqn52nnBcastHysteresisCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnBcastHysteresisCtl.setStatus("mandatory")
_Cpqn52nnBcastPktCnt_Type = Integer32
_Cpqn52nnBcastPktCnt_Object = MibScalar
cpqn52nnBcastPktCnt = _Cpqn52nnBcastPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 6),
    _Cpqn52nnBcastPktCnt_Type()
)
cpqn52nnBcastPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnBcastPktCnt.setStatus("mandatory")


class _Cpqn52nnBcastCongestionStatus_Type(Integer32):
    """Custom type cpqn52nnBcastCongestionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("congested", 1),
          ("not-congested", 2))
    )


_Cpqn52nnBcastCongestionStatus_Type.__name__ = "Integer32"
_Cpqn52nnBcastCongestionStatus_Object = MibScalar
cpqn52nnBcastCongestionStatus = _Cpqn52nnBcastCongestionStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 7),
    _Cpqn52nnBcastCongestionStatus_Type()
)
cpqn52nnBcastCongestionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnBcastCongestionStatus.setStatus("mandatory")
_Cpqn52nnPortMemThreshTable_Object = MibTable
cpqn52nnPortMemThreshTable = _Cpqn52nnPortMemThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 8)
)
if mibBuilder.loadTexts:
    cpqn52nnPortMemThreshTable.setStatus("mandatory")
_Cpqn52nnPortMemThreshEntry_Object = MibTableRow
cpqn52nnPortMemThreshEntry = _Cpqn52nnPortMemThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 8, 1)
)
cpqn52nnPortMemThreshEntry.setIndexNames(
    (0, "CPQN5226A-MIB", "cpqn52nnPortThreshIfIndex"),
)
if mibBuilder.loadTexts:
    cpqn52nnPortMemThreshEntry.setStatus("mandatory")
_Cpqn52nnPortThreshIfIndex_Type = Integer32
_Cpqn52nnPortThreshIfIndex_Object = MibTableColumn
cpqn52nnPortThreshIfIndex = _Cpqn52nnPortThreshIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 8, 1, 1),
    _Cpqn52nnPortThreshIfIndex_Type()
)
cpqn52nnPortThreshIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnPortThreshIfIndex.setStatus("mandatory")


class _Cpqn52nnPortTxPktThreshEnable_Type(Integer32):
    """Custom type cpqn52nnPortTxPktThreshEnable based on Integer32"""
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


_Cpqn52nnPortTxPktThreshEnable_Type.__name__ = "Integer32"
_Cpqn52nnPortTxPktThreshEnable_Object = MibTableColumn
cpqn52nnPortTxPktThreshEnable = _Cpqn52nnPortTxPktThreshEnable_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 8, 1, 2),
    _Cpqn52nnPortTxPktThreshEnable_Type()
)
cpqn52nnPortTxPktThreshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnPortTxPktThreshEnable.setStatus("mandatory")
_Cpqn52nnPortTxPktCongestionStatus_Type = Integer32
_Cpqn52nnPortTxPktCongestionStatus_Object = MibTableColumn
cpqn52nnPortTxPktCongestionStatus = _Cpqn52nnPortTxPktCongestionStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 8, 1, 3),
    _Cpqn52nnPortTxPktCongestionStatus_Type()
)
cpqn52nnPortTxPktCongestionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnPortTxPktCongestionStatus.setStatus("mandatory")
_Cpqn52nnPortTxPktCnt_Type = Integer32
_Cpqn52nnPortTxPktCnt_Object = MibTableColumn
cpqn52nnPortTxPktCnt = _Cpqn52nnPortTxPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 8, 1, 4),
    _Cpqn52nnPortTxPktCnt_Type()
)
cpqn52nnPortTxPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnPortTxPktCnt.setStatus("mandatory")


class _Cpqn52nnPortTxPktCeiling_Type(Integer32):
    """Custom type cpqn52nnPortTxPktCeiling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_Cpqn52nnPortTxPktCeiling_Type.__name__ = "Integer32"
_Cpqn52nnPortTxPktCeiling_Object = MibTableColumn
cpqn52nnPortTxPktCeiling = _Cpqn52nnPortTxPktCeiling_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 8, 1, 5),
    _Cpqn52nnPortTxPktCeiling_Type()
)
cpqn52nnPortTxPktCeiling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnPortTxPktCeiling.setStatus("mandatory")


class _Cpqn52nnPortTxPktHysteresisCtl_Type(Integer32):
    """Custom type cpqn52nnPortTxPktHysteresisCtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cpqn52nnPortTxPktHysteresisCtl_Type.__name__ = "Integer32"
_Cpqn52nnPortTxPktHysteresisCtl_Object = MibTableColumn
cpqn52nnPortTxPktHysteresisCtl = _Cpqn52nnPortTxPktHysteresisCtl_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 8, 1, 6),
    _Cpqn52nnPortTxPktHysteresisCtl_Type()
)
cpqn52nnPortTxPktHysteresisCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnPortTxPktHysteresisCtl.setStatus("mandatory")


class _Cpqn52nnPortRxMemThreshEnable_Type(Integer32):
    """Custom type cpqn52nnPortRxMemThreshEnable based on Integer32"""
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


_Cpqn52nnPortRxMemThreshEnable_Type.__name__ = "Integer32"
_Cpqn52nnPortRxMemThreshEnable_Object = MibTableColumn
cpqn52nnPortRxMemThreshEnable = _Cpqn52nnPortRxMemThreshEnable_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 8, 1, 7),
    _Cpqn52nnPortRxMemThreshEnable_Type()
)
cpqn52nnPortRxMemThreshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnPortRxMemThreshEnable.setStatus("mandatory")
_Cpqn52nnPortRxMemCongestionStatus_Type = Integer32
_Cpqn52nnPortRxMemCongestionStatus_Object = MibTableColumn
cpqn52nnPortRxMemCongestionStatus = _Cpqn52nnPortRxMemCongestionStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 8, 1, 8),
    _Cpqn52nnPortRxMemCongestionStatus_Type()
)
cpqn52nnPortRxMemCongestionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnPortRxMemCongestionStatus.setStatus("mandatory")
_Cpqn52nnPortRxMemSectorCnt_Type = Integer32
_Cpqn52nnPortRxMemSectorCnt_Object = MibTableColumn
cpqn52nnPortRxMemSectorCnt = _Cpqn52nnPortRxMemSectorCnt_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 8, 1, 9),
    _Cpqn52nnPortRxMemSectorCnt_Type()
)
cpqn52nnPortRxMemSectorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnPortRxMemSectorCnt.setStatus("mandatory")
_Cpqn52nnPortRxMemCeiling_Type = Integer32
_Cpqn52nnPortRxMemCeiling_Object = MibTableColumn
cpqn52nnPortRxMemCeiling = _Cpqn52nnPortRxMemCeiling_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 8, 1, 10),
    _Cpqn52nnPortRxMemCeiling_Type()
)
cpqn52nnPortRxMemCeiling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnPortRxMemCeiling.setStatus("mandatory")


class _Cpqn52nnPortRxMemHysteresisCtl_Type(Integer32):
    """Custom type cpqn52nnPortRxMemHysteresisCtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Cpqn52nnPortRxMemHysteresisCtl_Type.__name__ = "Integer32"
_Cpqn52nnPortRxMemHysteresisCtl_Object = MibTableColumn
cpqn52nnPortRxMemHysteresisCtl = _Cpqn52nnPortRxMemHysteresisCtl_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 8, 1, 11),
    _Cpqn52nnPortRxMemHysteresisCtl_Type()
)
cpqn52nnPortRxMemHysteresisCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnPortRxMemHysteresisCtl.setStatus("mandatory")


class _Cpqn52nnPortCongestionTrapEnable_Type(Integer32):
    """Custom type cpqn52nnPortCongestionTrapEnable based on Integer32"""
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


_Cpqn52nnPortCongestionTrapEnable_Type.__name__ = "Integer32"
_Cpqn52nnPortCongestionTrapEnable_Object = MibTableColumn
cpqn52nnPortCongestionTrapEnable = _Cpqn52nnPortCongestionTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 3, 8, 1, 12),
    _Cpqn52nnPortCongestionTrapEnable_Type()
)
cpqn52nnPortCongestionTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnPortCongestionTrapEnable.setStatus("mandatory")
_Cpqn52nnDramInfo_ObjectIdentity = ObjectIdentity
cpqn52nnDramInfo = _Cpqn52nnDramInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 4)
)
_Cpqn52nnDramTable_Object = MibTable
cpqn52nnDramTable = _Cpqn52nnDramTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 4, 1)
)
if mibBuilder.loadTexts:
    cpqn52nnDramTable.setStatus("mandatory")
_Cpqn52nnDramEntry_Object = MibTableRow
cpqn52nnDramEntry = _Cpqn52nnDramEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 4, 1, 1)
)
cpqn52nnDramEntry.setIndexNames(
    (0, "CPQN5226A-MIB", "cpqn52nnDramIndex"),
)
if mibBuilder.loadTexts:
    cpqn52nnDramEntry.setStatus("mandatory")


class _Cpqn52nnDramIndex_Type(Integer32):
    """Custom type cpqn52nnDramIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet-buffers", 1),
          ("cpu-dram", 2))
    )


_Cpqn52nnDramIndex_Type.__name__ = "Integer32"
_Cpqn52nnDramIndex_Object = MibTableColumn
cpqn52nnDramIndex = _Cpqn52nnDramIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 4, 1, 1, 1),
    _Cpqn52nnDramIndex_Type()
)
cpqn52nnDramIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnDramIndex.setStatus("mandatory")
_Cpqn52nnDramSize_Type = Integer32
_Cpqn52nnDramSize_Object = MibTableColumn
cpqn52nnDramSize = _Cpqn52nnDramSize_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 4, 1, 1, 2),
    _Cpqn52nnDramSize_Type()
)
cpqn52nnDramSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnDramSize.setStatus("mandatory")


class _Cpqn52nnDramType_Type(Integer32):
    """Custom type cpqn52nnDramType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fastpage-mode", 1),
          ("edo", 2),
          ("synchronous", 3))
    )


_Cpqn52nnDramType_Type.__name__ = "Integer32"
_Cpqn52nnDramType_Object = MibTableColumn
cpqn52nnDramType = _Cpqn52nnDramType_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 4, 1, 1, 3),
    _Cpqn52nnDramType_Type()
)
cpqn52nnDramType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnDramType.setStatus("mandatory")


class _Cpqn52nnDramSpeed_Type(Integer32):
    """Custom type cpqn52nnDramSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dram-70ns", 1),
          ("dram-60ns", 2))
    )


_Cpqn52nnDramSpeed_Type.__name__ = "Integer32"
_Cpqn52nnDramSpeed_Object = MibTableColumn
cpqn52nnDramSpeed = _Cpqn52nnDramSpeed_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 3, 4, 1, 1, 4),
    _Cpqn52nnDramSpeed_Type()
)
cpqn52nnDramSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnDramSpeed.setStatus("mandatory")
_Cpqn52nnPortInfo_ObjectIdentity = ObjectIdentity
cpqn52nnPortInfo = _Cpqn52nnPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4)
)
_Cpqn52nnPortStatusTable_Object = MibTable
cpqn52nnPortStatusTable = _Cpqn52nnPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cpqn52nnPortStatusTable.setStatus("mandatory")
_Cpqn52nnPortStatusEntry_Object = MibTableRow
cpqn52nnPortStatusEntry = _Cpqn52nnPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 1, 1)
)
cpqn52nnPortStatusEntry.setIndexNames(
    (0, "CPQN5226A-MIB", "cpqn52nnPortIfIndex"),
    (0, "CPQN5226A-MIB", "cpqn52nnPortIfMauIndex"),
)
if mibBuilder.loadTexts:
    cpqn52nnPortStatusEntry.setStatus("mandatory")
_Cpqn52nnPortIfIndex_Type = Integer32
_Cpqn52nnPortIfIndex_Object = MibTableColumn
cpqn52nnPortIfIndex = _Cpqn52nnPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 1, 1, 1),
    _Cpqn52nnPortIfIndex_Type()
)
cpqn52nnPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnPortIfIndex.setStatus("mandatory")
_Cpqn52nnPortIfMauIndex_Type = Integer32
_Cpqn52nnPortIfMauIndex_Object = MibTableColumn
cpqn52nnPortIfMauIndex = _Cpqn52nnPortIfMauIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 1, 1, 2),
    _Cpqn52nnPortIfMauIndex_Type()
)
cpqn52nnPortIfMauIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnPortIfMauIndex.setStatus("mandatory")


class _Cpqn52nnPortName_Type(DisplayString):
    """Custom type cpqn52nnPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Cpqn52nnPortName_Type.__name__ = "DisplayString"
_Cpqn52nnPortName_Object = MibTableColumn
cpqn52nnPortName = _Cpqn52nnPortName_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 1, 1, 3),
    _Cpqn52nnPortName_Type()
)
cpqn52nnPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnPortName.setStatus("mandatory")


class _Cpqn52nnPortType_Type(Integer32):
    """Custom type cpqn52nnPortType based on Integer32"""
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
              9,
              10,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("eth-10-baseT", 2),
          ("tx", 3),
          ("fxsc", 4),
          ("fxst", 5),
          ("eth-10-100", 6),
          ("fddi-das", 7),
          ("fddi-sas", 8),
          ("fddi-sas-tp-pmd", 9),
          ("atm", 10),
          ("unknown", 1000))
    )


_Cpqn52nnPortType_Type.__name__ = "Integer32"
_Cpqn52nnPortType_Object = MibTableColumn
cpqn52nnPortType = _Cpqn52nnPortType_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 1, 1, 4),
    _Cpqn52nnPortType_Type()
)
cpqn52nnPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnPortType.setStatus("mandatory")


class _Cpqn52nnMdiMdixStatus_Type(Integer32):
    """Custom type cpqn52nnMdiMdixStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 1),
          ("mdi-x", 2))
    )


_Cpqn52nnMdiMdixStatus_Type.__name__ = "Integer32"
_Cpqn52nnMdiMdixStatus_Object = MibTableColumn
cpqn52nnMdiMdixStatus = _Cpqn52nnMdiMdixStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 1, 1, 5),
    _Cpqn52nnMdiMdixStatus_Type()
)
cpqn52nnMdiMdixStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnMdiMdixStatus.setStatus("mandatory")


class _Cpqn52nnMdiMdixEnable_Type(Integer32):
    """Custom type cpqn52nnMdiMdixEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 1),
          ("mdi-x", 2),
          ("auto-sensing", 3))
    )


_Cpqn52nnMdiMdixEnable_Type.__name__ = "Integer32"
_Cpqn52nnMdiMdixEnable_Object = MibTableColumn
cpqn52nnMdiMdixEnable = _Cpqn52nnMdiMdixEnable_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 1, 1, 6),
    _Cpqn52nnMdiMdixEnable_Type()
)
cpqn52nnMdiMdixEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnMdiMdixEnable.setStatus("mandatory")
_Cpqn52nnPortMonitorTable_Object = MibTable
cpqn52nnPortMonitorTable = _Cpqn52nnPortMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    cpqn52nnPortMonitorTable.setStatus("mandatory")
_Cpqn52nnPortMonitorEntry_Object = MibTableRow
cpqn52nnPortMonitorEntry = _Cpqn52nnPortMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 2, 1)
)
cpqn52nnPortMonitorEntry.setIndexNames(
    (0, "CPQN5226A-MIB", "cpqn52nnPortMonitorIndex"),
)
if mibBuilder.loadTexts:
    cpqn52nnPortMonitorEntry.setStatus("mandatory")
_Cpqn52nnPortMonitorIndex_Type = Integer32
_Cpqn52nnPortMonitorIndex_Object = MibTableColumn
cpqn52nnPortMonitorIndex = _Cpqn52nnPortMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 2, 1, 1),
    _Cpqn52nnPortMonitorIndex_Type()
)
cpqn52nnPortMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnPortMonitorIndex.setStatus("mandatory")
_Cpqn52nnPortMonitorRowStatus_Type = CpqnRowStatus
_Cpqn52nnPortMonitorRowStatus_Object = MibTableColumn
cpqn52nnPortMonitorRowStatus = _Cpqn52nnPortMonitorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 2, 1, 2),
    _Cpqn52nnPortMonitorRowStatus_Type()
)
cpqn52nnPortMonitorRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnPortMonitorRowStatus.setStatus("mandatory")
_Cpqn52nnPortMonitorIfIndex_Type = Integer32
_Cpqn52nnPortMonitorIfIndex_Object = MibTableColumn
cpqn52nnPortMonitorIfIndex = _Cpqn52nnPortMonitorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 2, 1, 3),
    _Cpqn52nnPortMonitorIfIndex_Type()
)
cpqn52nnPortMonitorIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnPortMonitorIfIndex.setStatus("mandatory")
_Cpqn52nnPortMonitoredIfMap_Type = Integer32
_Cpqn52nnPortMonitoredIfMap_Object = MibTableColumn
cpqn52nnPortMonitoredIfMap = _Cpqn52nnPortMonitoredIfMap_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 2, 1, 4),
    _Cpqn52nnPortMonitoredIfMap_Type()
)
cpqn52nnPortMonitoredIfMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnPortMonitoredIfMap.setStatus("mandatory")


class _Cpqn52nnPortMonitoredDataType_Type(Integer32):
    """Custom type cpqn52nnPortMonitoredDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tx-only", 1),
          ("rx-only", 2),
          ("both-tx-and-rx", 3))
    )


_Cpqn52nnPortMonitoredDataType_Type.__name__ = "Integer32"
_Cpqn52nnPortMonitoredDataType_Object = MibTableColumn
cpqn52nnPortMonitoredDataType = _Cpqn52nnPortMonitoredDataType_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 2, 1, 5),
    _Cpqn52nnPortMonitoredDataType_Type()
)
cpqn52nnPortMonitoredDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnPortMonitoredDataType.setStatus("mandatory")
_Cpqn52nnPortBondingTable_Object = MibTable
cpqn52nnPortBondingTable = _Cpqn52nnPortBondingTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 3)
)
if mibBuilder.loadTexts:
    cpqn52nnPortBondingTable.setStatus("mandatory")
_Cpqn52nnPortBondingEntry_Object = MibTableRow
cpqn52nnPortBondingEntry = _Cpqn52nnPortBondingEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 3, 1)
)
cpqn52nnPortBondingEntry.setIndexNames(
    (0, "CPQN5226A-MIB", "cpqn52nnBondIndex"),
)
if mibBuilder.loadTexts:
    cpqn52nnPortBondingEntry.setStatus("mandatory")
_Cpqn52nnBondIndex_Type = Integer32
_Cpqn52nnBondIndex_Object = MibTableColumn
cpqn52nnBondIndex = _Cpqn52nnBondIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 3, 1, 1),
    _Cpqn52nnBondIndex_Type()
)
cpqn52nnBondIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnBondIndex.setStatus("mandatory")
_Cpqn52nnBondRowStatus_Type = CpqnRowStatus
_Cpqn52nnBondRowStatus_Object = MibTableColumn
cpqn52nnBondRowStatus = _Cpqn52nnBondRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 3, 1, 2),
    _Cpqn52nnBondRowStatus_Type()
)
cpqn52nnBondRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnBondRowStatus.setStatus("mandatory")
_Cpqn52nnBondMap_Type = Integer32
_Cpqn52nnBondMap_Object = MibTableColumn
cpqn52nnBondMap = _Cpqn52nnBondMap_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 4, 3, 1, 3),
    _Cpqn52nnBondMap_Type()
)
cpqn52nnBondMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnBondMap.setStatus("mandatory")
_Cpqn52nnIfStatusInfo_ObjectIdentity = ObjectIdentity
cpqn52nnIfStatusInfo = _Cpqn52nnIfStatusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 5)
)
_Cpqn52nnIfStatusTable_Object = MibTable
cpqn52nnIfStatusTable = _Cpqn52nnIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cpqn52nnIfStatusTable.setStatus("mandatory")
_Cpqn52nnIfStatusEntry_Object = MibTableRow
cpqn52nnIfStatusEntry = _Cpqn52nnIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 5, 1, 1)
)
cpqn52nnIfStatusEntry.setIndexNames(
    (0, "CPQN5226A-MIB", "cpqn52nnIfStatusIfIndex"),
)
if mibBuilder.loadTexts:
    cpqn52nnIfStatusEntry.setStatus("mandatory")
_Cpqn52nnIfStatusIfIndex_Type = Integer32
_Cpqn52nnIfStatusIfIndex_Object = MibTableColumn
cpqn52nnIfStatusIfIndex = _Cpqn52nnIfStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 5, 1, 1, 1),
    _Cpqn52nnIfStatusIfIndex_Type()
)
cpqn52nnIfStatusIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnIfStatusIfIndex.setStatus("mandatory")


class _Cpqn52nnIfStatusIfType_Type(Integer32):
    """Custom type cpqn52nnIfStatusIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("quad-cascade-lsi-l64381", 1),
          ("tlan-ti-tnete110", 2),
          ("qe110-lsi", 3))
    )


_Cpqn52nnIfStatusIfType_Type.__name__ = "Integer32"
_Cpqn52nnIfStatusIfType_Object = MibTableColumn
cpqn52nnIfStatusIfType = _Cpqn52nnIfStatusIfType_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 5, 1, 1, 2),
    _Cpqn52nnIfStatusIfType_Type()
)
cpqn52nnIfStatusIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnIfStatusIfType.setStatus("mandatory")


class _Cpqn52nnIfStpStatus_Type(Integer32):
    """Custom type cpqn52nnIfStpStatus based on Integer32"""
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


_Cpqn52nnIfStpStatus_Type.__name__ = "Integer32"
_Cpqn52nnIfStpStatus_Object = MibTableColumn
cpqn52nnIfStpStatus = _Cpqn52nnIfStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 5, 1, 1, 3),
    _Cpqn52nnIfStpStatus_Type()
)
cpqn52nnIfStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnIfStpStatus.setStatus("mandatory")


class _Cpqn52nnIfResetStatus_Type(Integer32):
    """Custom type cpqn52nnIfResetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interface-not-resetting", 1),
          ("reset-interface", 2))
    )


_Cpqn52nnIfResetStatus_Type.__name__ = "Integer32"
_Cpqn52nnIfResetStatus_Object = MibTableColumn
cpqn52nnIfResetStatus = _Cpqn52nnIfResetStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 5, 1, 1, 4),
    _Cpqn52nnIfResetStatus_Type()
)
cpqn52nnIfResetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnIfResetStatus.setStatus("mandatory")


class _Cpqn52nnIfLearningStatus_Type(Integer32):
    """Custom type cpqn52nnIfLearningStatus based on Integer32"""
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


_Cpqn52nnIfLearningStatus_Type.__name__ = "Integer32"
_Cpqn52nnIfLearningStatus_Object = MibTableColumn
cpqn52nnIfLearningStatus = _Cpqn52nnIfLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 5, 1, 1, 5),
    _Cpqn52nnIfLearningStatus_Type()
)
cpqn52nnIfLearningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnIfLearningStatus.setStatus("mandatory")


class _Cpqn52nnIfAgingStatus_Type(Integer32):
    """Custom type cpqn52nnIfAgingStatus based on Integer32"""
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


_Cpqn52nnIfAgingStatus_Type.__name__ = "Integer32"
_Cpqn52nnIfAgingStatus_Object = MibTableColumn
cpqn52nnIfAgingStatus = _Cpqn52nnIfAgingStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 5, 1, 1, 6),
    _Cpqn52nnIfAgingStatus_Type()
)
cpqn52nnIfAgingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnIfAgingStatus.setStatus("mandatory")


class _Cpqn52nnIfAgingTime_Type(Integer32):
    """Custom type cpqn52nnIfAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_Cpqn52nnIfAgingTime_Type.__name__ = "Integer32"
_Cpqn52nnIfAgingTime_Object = MibTableColumn
cpqn52nnIfAgingTime = _Cpqn52nnIfAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 5, 1, 1, 7),
    _Cpqn52nnIfAgingTime_Type()
)
cpqn52nnIfAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnIfAgingTime.setStatus("mandatory")


class _Cpqn52nnIfSwitchModeSrcStatus_Type(Integer32):
    """Custom type cpqn52nnIfSwitchModeSrcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("store-and-forward", 1),
          ("cut-through", 2),
          ("fragment-free", 3))
    )


_Cpqn52nnIfSwitchModeSrcStatus_Type.__name__ = "Integer32"
_Cpqn52nnIfSwitchModeSrcStatus_Object = MibTableColumn
cpqn52nnIfSwitchModeSrcStatus = _Cpqn52nnIfSwitchModeSrcStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 5, 1, 1, 8),
    _Cpqn52nnIfSwitchModeSrcStatus_Type()
)
cpqn52nnIfSwitchModeSrcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnIfSwitchModeSrcStatus.setStatus("mandatory")


class _Cpqn52nnIfSwitchModeDestStatus_Type(Integer32):
    """Custom type cpqn52nnIfSwitchModeDestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("store-and-forward", 1),
          ("cut-through", 2),
          ("fragment-free", 3))
    )


_Cpqn52nnIfSwitchModeDestStatus_Type.__name__ = "Integer32"
_Cpqn52nnIfSwitchModeDestStatus_Object = MibTableColumn
cpqn52nnIfSwitchModeDestStatus = _Cpqn52nnIfSwitchModeDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 5, 1, 1, 9),
    _Cpqn52nnIfSwitchModeDestStatus_Type()
)
cpqn52nnIfSwitchModeDestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnIfSwitchModeDestStatus.setStatus("mandatory")


class _Cpqn52nnIfSwitchModeSrc_Type(Integer32):
    """Custom type cpqn52nnIfSwitchModeSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("store-and-forward", 1),
          ("cut-through", 2),
          ("fragment-free", 3))
    )


_Cpqn52nnIfSwitchModeSrc_Type.__name__ = "Integer32"
_Cpqn52nnIfSwitchModeSrc_Object = MibTableColumn
cpqn52nnIfSwitchModeSrc = _Cpqn52nnIfSwitchModeSrc_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 5, 1, 1, 10),
    _Cpqn52nnIfSwitchModeSrc_Type()
)
cpqn52nnIfSwitchModeSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnIfSwitchModeSrc.setStatus("mandatory")


class _Cpqn52nnIfSwitchModeDest_Type(Integer32):
    """Custom type cpqn52nnIfSwitchModeDest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("store-and-forward", 1),
          ("cut-through", 2),
          ("fragment-free", 3))
    )


_Cpqn52nnIfSwitchModeDest_Type.__name__ = "Integer32"
_Cpqn52nnIfSwitchModeDest_Object = MibTableColumn
cpqn52nnIfSwitchModeDest = _Cpqn52nnIfSwitchModeDest_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 5, 1, 1, 11),
    _Cpqn52nnIfSwitchModeDest_Type()
)
cpqn52nnIfSwitchModeDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnIfSwitchModeDest.setStatus("mandatory")


class _Cpqn52nnIfArbPriority_Type(Integer32):
    """Custom type cpqn52nnIfArbPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Cpqn52nnIfArbPriority_Type.__name__ = "Integer32"
_Cpqn52nnIfArbPriority_Object = MibTableColumn
cpqn52nnIfArbPriority = _Cpqn52nnIfArbPriority_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 5, 1, 1, 12),
    _Cpqn52nnIfArbPriority_Type()
)
cpqn52nnIfArbPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnIfArbPriority.setStatus("mandatory")
_Cpqn52nnIfStatsInfo_ObjectIdentity = ObjectIdentity
cpqn52nnIfStatsInfo = _Cpqn52nnIfStatsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6)
)
_Cpqn52nnQuadCascade_ObjectIdentity = ObjectIdentity
cpqn52nnQuadCascade = _Cpqn52nnQuadCascade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 1)
)
_Cpqn52nnQuadIfTable_Object = MibTable
cpqn52nnQuadIfTable = _Cpqn52nnQuadIfTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    cpqn52nnQuadIfTable.setStatus("mandatory")
_Cpqn52nnQuadIfEntry_Object = MibTableRow
cpqn52nnQuadIfEntry = _Cpqn52nnQuadIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 1, 1, 1)
)
cpqn52nnQuadIfEntry.setIndexNames(
    (0, "CPQN5226A-MIB", "cpqn52nnQuadIfIndex"),
)
if mibBuilder.loadTexts:
    cpqn52nnQuadIfEntry.setStatus("mandatory")
_Cpqn52nnQuadIfIndex_Type = Integer32
_Cpqn52nnQuadIfIndex_Object = MibTableColumn
cpqn52nnQuadIfIndex = _Cpqn52nnQuadIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 1, 1, 1, 1),
    _Cpqn52nnQuadIfIndex_Type()
)
cpqn52nnQuadIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnQuadIfIndex.setStatus("mandatory")
_Cpqn52nnQuadIfAlignFcsErrors_Type = Counter32
_Cpqn52nnQuadIfAlignFcsErrors_Object = MibTableColumn
cpqn52nnQuadIfAlignFcsErrors = _Cpqn52nnQuadIfAlignFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 1, 1, 1, 2),
    _Cpqn52nnQuadIfAlignFcsErrors_Type()
)
cpqn52nnQuadIfAlignFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnQuadIfAlignFcsErrors.setStatus("mandatory")
_Cpqn52nnQuadIfTxRunts_Type = Counter32
_Cpqn52nnQuadIfTxRunts_Object = MibTableColumn
cpqn52nnQuadIfTxRunts = _Cpqn52nnQuadIfTxRunts_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 1, 1, 1, 3),
    _Cpqn52nnQuadIfTxRunts_Type()
)
cpqn52nnQuadIfTxRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnQuadIfTxRunts.setStatus("mandatory")
_Cpqn52nnQuadIfRxRunts_Type = Counter32
_Cpqn52nnQuadIfRxRunts_Object = MibTableColumn
cpqn52nnQuadIfRxRunts = _Cpqn52nnQuadIfRxRunts_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 1, 1, 1, 4),
    _Cpqn52nnQuadIfRxRunts_Type()
)
cpqn52nnQuadIfRxRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnQuadIfRxRunts.setStatus("mandatory")
_Cpqn52nnQuadIfTotalCollisions_Type = Counter32
_Cpqn52nnQuadIfTotalCollisions_Object = MibTableColumn
cpqn52nnQuadIfTotalCollisions = _Cpqn52nnQuadIfTotalCollisions_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 1, 1, 1, 5),
    _Cpqn52nnQuadIfTotalCollisions_Type()
)
cpqn52nnQuadIfTotalCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnQuadIfTotalCollisions.setStatus("mandatory")
_Cpqn52nnQuadIfCfgTable_Object = MibTable
cpqn52nnQuadIfCfgTable = _Cpqn52nnQuadIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 1, 2)
)
if mibBuilder.loadTexts:
    cpqn52nnQuadIfCfgTable.setStatus("mandatory")
_Cpqn52nnQuadIfCfgEntry_Object = MibTableRow
cpqn52nnQuadIfCfgEntry = _Cpqn52nnQuadIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 1, 2, 1)
)
cpqn52nnQuadIfCfgEntry.setIndexNames(
    (0, "CPQN5226A-MIB", "cpqn52nnQuadIfCfgIndex"),
    (0, "CPQN5226A-MIB", "cpqn52nnQuadIfCfgMauIndex"),
)
if mibBuilder.loadTexts:
    cpqn52nnQuadIfCfgEntry.setStatus("mandatory")
_Cpqn52nnQuadIfCfgIndex_Type = Integer32
_Cpqn52nnQuadIfCfgIndex_Object = MibTableColumn
cpqn52nnQuadIfCfgIndex = _Cpqn52nnQuadIfCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 1, 2, 1, 1),
    _Cpqn52nnQuadIfCfgIndex_Type()
)
cpqn52nnQuadIfCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnQuadIfCfgIndex.setStatus("mandatory")
_Cpqn52nnQuadIfCfgMauIndex_Type = Integer32
_Cpqn52nnQuadIfCfgMauIndex_Object = MibTableColumn
cpqn52nnQuadIfCfgMauIndex = _Cpqn52nnQuadIfCfgMauIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 1, 2, 1, 2),
    _Cpqn52nnQuadIfCfgMauIndex_Type()
)
cpqn52nnQuadIfCfgMauIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnQuadIfCfgMauIndex.setStatus("mandatory")


class _Cpqn52nnQuadIfCfgLinkForce_Type(Integer32):
    """Custom type cpqn52nnQuadIfCfgLinkForce based on Integer32"""
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


_Cpqn52nnQuadIfCfgLinkForce_Type.__name__ = "Integer32"
_Cpqn52nnQuadIfCfgLinkForce_Object = MibTableColumn
cpqn52nnQuadIfCfgLinkForce = _Cpqn52nnQuadIfCfgLinkForce_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 1, 2, 1, 3),
    _Cpqn52nnQuadIfCfgLinkForce_Type()
)
cpqn52nnQuadIfCfgLinkForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnQuadIfCfgLinkForce.setStatus("mandatory")


class _Cpqn52nnQuadIfCfgLinkPolarityCorrect_Type(Integer32):
    """Custom type cpqn52nnQuadIfCfgLinkPolarityCorrect based on Integer32"""
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


_Cpqn52nnQuadIfCfgLinkPolarityCorrect_Type.__name__ = "Integer32"
_Cpqn52nnQuadIfCfgLinkPolarityCorrect_Object = MibTableColumn
cpqn52nnQuadIfCfgLinkPolarityCorrect = _Cpqn52nnQuadIfCfgLinkPolarityCorrect_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 1, 2, 1, 4),
    _Cpqn52nnQuadIfCfgLinkPolarityCorrect_Type()
)
cpqn52nnQuadIfCfgLinkPolarityCorrect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnQuadIfCfgLinkPolarityCorrect.setStatus("mandatory")
_Cpqn52nnTlan_ObjectIdentity = ObjectIdentity
cpqn52nnTlan = _Cpqn52nnTlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 2)
)
_Cpqn52nnTlanIfTable_Object = MibTable
cpqn52nnTlanIfTable = _Cpqn52nnTlanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    cpqn52nnTlanIfTable.setStatus("mandatory")
_Cpqn52nnTlanIfEntry_Object = MibTableRow
cpqn52nnTlanIfEntry = _Cpqn52nnTlanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 2, 1, 1)
)
cpqn52nnTlanIfEntry.setIndexNames(
    (0, "CPQN5226A-MIB", "cpqn52nnTlanIfIndex"),
)
if mibBuilder.loadTexts:
    cpqn52nnTlanIfEntry.setStatus("mandatory")
_Cpqn52nnTlanIfIndex_Type = Integer32
_Cpqn52nnTlanIfIndex_Object = MibTableColumn
cpqn52nnTlanIfIndex = _Cpqn52nnTlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 2, 1, 1, 1),
    _Cpqn52nnTlanIfIndex_Type()
)
cpqn52nnTlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnTlanIfIndex.setStatus("mandatory")
_Cpqn52nnTlanIfTxGoodFrms_Type = Counter32
_Cpqn52nnTlanIfTxGoodFrms_Object = MibTableColumn
cpqn52nnTlanIfTxGoodFrms = _Cpqn52nnTlanIfTxGoodFrms_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 2, 1, 1, 2),
    _Cpqn52nnTlanIfTxGoodFrms_Type()
)
cpqn52nnTlanIfTxGoodFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnTlanIfTxGoodFrms.setStatus("mandatory")
_Cpqn52nnTlanIfRxUndersizeFrms_Type = Counter32
_Cpqn52nnTlanIfRxUndersizeFrms_Object = MibTableColumn
cpqn52nnTlanIfRxUndersizeFrms = _Cpqn52nnTlanIfRxUndersizeFrms_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 2, 1, 1, 3),
    _Cpqn52nnTlanIfRxUndersizeFrms_Type()
)
cpqn52nnTlanIfRxUndersizeFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnTlanIfRxUndersizeFrms.setStatus("mandatory")
_Cpqn52nnTlanIfRxOverruns_Type = Counter32
_Cpqn52nnTlanIfRxOverruns_Object = MibTableColumn
cpqn52nnTlanIfRxOverruns = _Cpqn52nnTlanIfRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 2, 1, 1, 4),
    _Cpqn52nnTlanIfRxOverruns_Type()
)
cpqn52nnTlanIfRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnTlanIfRxOverruns.setStatus("mandatory")
_Cpqn52nnTlanIfRxAlignSymbolErrs_Type = Counter32
_Cpqn52nnTlanIfRxAlignSymbolErrs_Object = MibTableColumn
cpqn52nnTlanIfRxAlignSymbolErrs = _Cpqn52nnTlanIfRxAlignSymbolErrs_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 6, 2, 1, 1, 5),
    _Cpqn52nnTlanIfRxAlignSymbolErrs_Type()
)
cpqn52nnTlanIfRxAlignSymbolErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnTlanIfRxAlignSymbolErrs.setStatus("mandatory")
_Cpqn52nnSwitchStatsInfo_ObjectIdentity = ObjectIdentity
cpqn52nnSwitchStatsInfo = _Cpqn52nnSwitchStatsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 7)
)
_Cpqn52nnHashMemory_ObjectIdentity = ObjectIdentity
cpqn52nnHashMemory = _Cpqn52nnHashMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 7, 1)
)
_Cpqn52nnHashStaticNum_Type = Integer32
_Cpqn52nnHashStaticNum_Object = MibScalar
cpqn52nnHashStaticNum = _Cpqn52nnHashStaticNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 7, 1, 1),
    _Cpqn52nnHashStaticNum_Type()
)
cpqn52nnHashStaticNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnHashStaticNum.setStatus("mandatory")
_Cpqn52nnHashDynamicNum_Type = Integer32
_Cpqn52nnHashDynamicNum_Object = MibScalar
cpqn52nnHashDynamicNum = _Cpqn52nnHashDynamicNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 7, 1, 2),
    _Cpqn52nnHashDynamicNum_Type()
)
cpqn52nnHashDynamicNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnHashDynamicNum.setStatus("mandatory")
_Cpqn52nnHashChainNum_Type = Integer32
_Cpqn52nnHashChainNum_Object = MibScalar
cpqn52nnHashChainNum = _Cpqn52nnHashChainNum_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 7, 1, 3),
    _Cpqn52nnHashChainNum_Type()
)
cpqn52nnHashChainNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnHashChainNum.setStatus("mandatory")
_Cpqn52nnHashChainLength_Type = Integer32
_Cpqn52nnHashChainLength_Object = MibScalar
cpqn52nnHashChainLength = _Cpqn52nnHashChainLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 7, 1, 4),
    _Cpqn52nnHashChainLength_Type()
)
cpqn52nnHashChainLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnHashChainLength.setStatus("mandatory")
_Cpqn52nnDropPkts_ObjectIdentity = ObjectIdentity
cpqn52nnDropPkts = _Cpqn52nnDropPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 7, 2)
)
_Cpqn52nnDropsWholeMemoryCtr_Type = Counter32
_Cpqn52nnDropsWholeMemoryCtr_Object = MibScalar
cpqn52nnDropsWholeMemoryCtr = _Cpqn52nnDropsWholeMemoryCtr_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 7, 2, 1),
    _Cpqn52nnDropsWholeMemoryCtr_Type()
)
cpqn52nnDropsWholeMemoryCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnDropsWholeMemoryCtr.setStatus("mandatory")
_Cpqn52nnDropsBcastMemoryCtr_Type = Counter32
_Cpqn52nnDropsBcastMemoryCtr_Object = MibScalar
cpqn52nnDropsBcastMemoryCtr = _Cpqn52nnDropsBcastMemoryCtr_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 7, 2, 2),
    _Cpqn52nnDropsBcastMemoryCtr_Type()
)
cpqn52nnDropsBcastMemoryCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnDropsBcastMemoryCtr.setStatus("mandatory")
_Cpqn52nnDropsIfMemoryCtr_Type = Counter32
_Cpqn52nnDropsIfMemoryCtr_Object = MibScalar
cpqn52nnDropsIfMemoryCtr = _Cpqn52nnDropsIfMemoryCtr_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 7, 2, 3),
    _Cpqn52nnDropsIfMemoryCtr_Type()
)
cpqn52nnDropsIfMemoryCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnDropsIfMemoryCtr.setStatus("mandatory")
_Cpqn52nnBusMonitorInfo_ObjectIdentity = ObjectIdentity
cpqn52nnBusMonitorInfo = _Cpqn52nnBusMonitorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 8)
)
_Cpqn52nnBusMonTable_Object = MibTable
cpqn52nnBusMonTable = _Cpqn52nnBusMonTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 8, 1)
)
if mibBuilder.loadTexts:
    cpqn52nnBusMonTable.setStatus("mandatory")
_Cpqn52nnBusMonEntry_Object = MibTableRow
cpqn52nnBusMonEntry = _Cpqn52nnBusMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 8, 1, 1)
)
cpqn52nnBusMonEntry.setIndexNames(
    (0, "CPQN5226A-MIB", "cpqn52nnBusMonIndex"),
)
if mibBuilder.loadTexts:
    cpqn52nnBusMonEntry.setStatus("mandatory")
_Cpqn52nnBusMonIndex_Type = Integer32
_Cpqn52nnBusMonIndex_Object = MibTableColumn
cpqn52nnBusMonIndex = _Cpqn52nnBusMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 8, 1, 1, 1),
    _Cpqn52nnBusMonIndex_Type()
)
cpqn52nnBusMonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnBusMonIndex.setStatus("mandatory")
_Cpqn52nnBusMonRowStatus_Type = CpqnRowStatus
_Cpqn52nnBusMonRowStatus_Object = MibTableColumn
cpqn52nnBusMonRowStatus = _Cpqn52nnBusMonRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 8, 1, 1, 2),
    _Cpqn52nnBusMonRowStatus_Type()
)
cpqn52nnBusMonRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnBusMonRowStatus.setStatus("mandatory")


class _Cpqn52nnBusMonBusType_Type(Integer32):
    """Custom type cpqn52nnBusMonBusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac-bus", 1),
          ("mem-bus", 2))
    )


_Cpqn52nnBusMonBusType_Type.__name__ = "Integer32"
_Cpqn52nnBusMonBusType_Object = MibTableColumn
cpqn52nnBusMonBusType = _Cpqn52nnBusMonBusType_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 8, 1, 1, 3),
    _Cpqn52nnBusMonBusType_Type()
)
cpqn52nnBusMonBusType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnBusMonBusType.setStatus("mandatory")


class _Cpqn52nnBusMonDataType_Type(Integer32):
    """Custom type cpqn52nnBusMonDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tx-only", 1),
          ("rx-only", 2),
          ("both-tx-and-rx", 3))
    )


_Cpqn52nnBusMonDataType_Type.__name__ = "Integer32"
_Cpqn52nnBusMonDataType_Object = MibTableColumn
cpqn52nnBusMonDataType = _Cpqn52nnBusMonDataType_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 8, 1, 1, 4),
    _Cpqn52nnBusMonDataType_Type()
)
cpqn52nnBusMonDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnBusMonDataType.setStatus("mandatory")


class _Cpqn52nnBusMonPktType_Type(Integer32):
    """Custom type cpqn52nnBusMonPktType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pkt-data-only", 1),
          ("pkt-overhead-only", 2),
          ("both-data-and-overhead", 3))
    )


_Cpqn52nnBusMonPktType_Type.__name__ = "Integer32"
_Cpqn52nnBusMonPktType_Object = MibTableColumn
cpqn52nnBusMonPktType = _Cpqn52nnBusMonPktType_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 8, 1, 1, 5),
    _Cpqn52nnBusMonPktType_Type()
)
cpqn52nnBusMonPktType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnBusMonPktType.setStatus("mandatory")


class _Cpqn52nnBusMonSwitchModeType_Type(Integer32):
    """Custom type cpqn52nnBusMonSwitchModeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("store-and-forward-only", 1),
          ("cut-through-only", 2),
          ("both-switch-modes", 3))
    )


_Cpqn52nnBusMonSwitchModeType_Type.__name__ = "Integer32"
_Cpqn52nnBusMonSwitchModeType_Object = MibTableColumn
cpqn52nnBusMonSwitchModeType = _Cpqn52nnBusMonSwitchModeType_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 8, 1, 1, 6),
    _Cpqn52nnBusMonSwitchModeType_Type()
)
cpqn52nnBusMonSwitchModeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnBusMonSwitchModeType.setStatus("mandatory")
_Cpqn52nnBusMonCurrentUtilization_Type = Integer32
_Cpqn52nnBusMonCurrentUtilization_Object = MibTableColumn
cpqn52nnBusMonCurrentUtilization = _Cpqn52nnBusMonCurrentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 8, 1, 1, 7),
    _Cpqn52nnBusMonCurrentUtilization_Type()
)
cpqn52nnBusMonCurrentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnBusMonCurrentUtilization.setStatus("mandatory")
_Cpqn52nnBusMonPeakUtilization_Type = Integer32
_Cpqn52nnBusMonPeakUtilization_Object = MibTableColumn
cpqn52nnBusMonPeakUtilization = _Cpqn52nnBusMonPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 8, 1, 1, 8),
    _Cpqn52nnBusMonPeakUtilization_Type()
)
cpqn52nnBusMonPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqn52nnBusMonPeakUtilization.setStatus("mandatory")
_Cpqn52nnBusMonRisingThreshold_Type = Integer32
_Cpqn52nnBusMonRisingThreshold_Object = MibTableColumn
cpqn52nnBusMonRisingThreshold = _Cpqn52nnBusMonRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 8, 1, 1, 9),
    _Cpqn52nnBusMonRisingThreshold_Type()
)
cpqn52nnBusMonRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnBusMonRisingThreshold.setStatus("mandatory")
_Cpqn52nnBusMonFallingThreshold_Type = Integer32
_Cpqn52nnBusMonFallingThreshold_Object = MibTableColumn
cpqn52nnBusMonFallingThreshold = _Cpqn52nnBusMonFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 8, 1, 1, 10),
    _Cpqn52nnBusMonFallingThreshold_Type()
)
cpqn52nnBusMonFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnBusMonFallingThreshold.setStatus("mandatory")


class _Cpqn52nnBusMonAction_Type(Integer32):
    """Custom type cpqn52nnBusMonAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("backpressure", 2),
          ("filter-broadcast", 3))
    )


_Cpqn52nnBusMonAction_Type.__name__ = "Integer32"
_Cpqn52nnBusMonAction_Object = MibTableColumn
cpqn52nnBusMonAction = _Cpqn52nnBusMonAction_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 8, 1, 1, 11),
    _Cpqn52nnBusMonAction_Type()
)
cpqn52nnBusMonAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnBusMonAction.setStatus("mandatory")


class _Cpqn52nnBusMonTrapEnable_Type(Integer32):
    """Custom type cpqn52nnBusMonTrapEnable based on Integer32"""
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


_Cpqn52nnBusMonTrapEnable_Type.__name__ = "Integer32"
_Cpqn52nnBusMonTrapEnable_Object = MibTableColumn
cpqn52nnBusMonTrapEnable = _Cpqn52nnBusMonTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 8, 1, 1, 12),
    _Cpqn52nnBusMonTrapEnable_Type()
)
cpqn52nnBusMonTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqn52nnBusMonTrapEnable.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqn52nnPowerSupplyStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 0, 1)
)
cpqn52nnPowerSupplyStatusTrap.setObjects(
      *(("CPQN5226A-MIB", "cpqn52nnPsIndex"),
        ("CPQN5226A-MIB", "cpqn52nnPsStatus"))
)
if mibBuilder.loadTexts:
    cpqn52nnPowerSupplyStatusTrap.setStatus(
        ""
    )

cpqn52nnUplinkInsertedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 0, 2)
)
cpqn52nnUplinkInsertedTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CPQN5226A-MIB", "cpqn52nnPortType"))
)
if mibBuilder.loadTexts:
    cpqn52nnUplinkInsertedTrap.setStatus(
        ""
    )

cpqn52nnUplinkRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 0, 3)
)
cpqn52nnUplinkRemovedTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CPQN5226A-MIB", "cpqn52nnPortType"))
)
if mibBuilder.loadTexts:
    cpqn52nnUplinkRemovedTrap.setStatus(
        ""
    )

cpqn52nnBusMonRisingThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 0, 4)
)
cpqn52nnBusMonRisingThresholdTrap.setObjects(
      *(("CPQN5226A-MIB", "cpqn52nnBusMonIndex"),
        ("CPQN5226A-MIB", "cpqn52nnBusMonBusType"),
        ("CPQN5226A-MIB", "cpqn52nnBusMonCurrentUtilization"))
)
if mibBuilder.loadTexts:
    cpqn52nnBusMonRisingThresholdTrap.setStatus(
        ""
    )

cpqn52nnBusMonFallingThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 0, 5)
)
cpqn52nnBusMonFallingThresholdTrap.setObjects(
      *(("CPQN5226A-MIB", "cpqn52nnBusMonIndex"),
        ("CPQN5226A-MIB", "cpqn52nnBusMonBusType"),
        ("CPQN5226A-MIB", "cpqn52nnBusMonCurrentUtilization"))
)
if mibBuilder.loadTexts:
    cpqn52nnBusMonFallingThresholdTrap.setStatus(
        ""
    )

cpqb52nnGlobalBcastMemCongestionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 0, 7)
)
cpqb52nnGlobalBcastMemCongestionTrap.setObjects(
    ("CPQN5226A-MIB", "cpqn52nnBcastCongestionStatus")
)
if mibBuilder.loadTexts:
    cpqb52nnGlobalBcastMemCongestionTrap.setStatus(
        ""
    )

cpqb52nnPortTxPktCongestionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 0, 8)
)
cpqb52nnPortTxPktCongestionTrap.setObjects(
      *(("CPQN5226A-MIB", "cpqn52nnPortThreshIfIndex"),
        ("CPQN5226A-MIB", "cpqn52nnPortTxPktCongestionStatus"))
)
if mibBuilder.loadTexts:
    cpqb52nnPortTxPktCongestionTrap.setStatus(
        ""
    )

cpqb52nnPortRxMemCongestionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 101, 2, 2, 0, 9)
)
cpqb52nnPortRxMemCongestionTrap.setObjects(
      *(("CPQN5226A-MIB", "cpqn52nnPortThreshIfIndex"),
        ("CPQN5226A-MIB", "cpqn52nnPortRxMemCongestionStatus"))
)
if mibBuilder.loadTexts:
    cpqb52nnPortRxMemCongestionTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQN5226A-MIB",
    **{"compaq": compaq,
       "compaq-dallas-npd": compaq_dallas_npd,
       "switchedMedia": switchedMedia,
       "cpqn52nn": cpqn52nn,
       "cpqn52nnPowerSupplyStatusTrap": cpqn52nnPowerSupplyStatusTrap,
       "cpqn52nnUplinkInsertedTrap": cpqn52nnUplinkInsertedTrap,
       "cpqn52nnUplinkRemovedTrap": cpqn52nnUplinkRemovedTrap,
       "cpqn52nnBusMonRisingThresholdTrap": cpqn52nnBusMonRisingThresholdTrap,
       "cpqn52nnBusMonFallingThresholdTrap": cpqn52nnBusMonFallingThresholdTrap,
       "cpqb52nnGlobalBcastMemCongestionTrap": cpqb52nnGlobalBcastMemCongestionTrap,
       "cpqb52nnPortTxPktCongestionTrap": cpqb52nnPortTxPktCongestionTrap,
       "cpqb52nnPortRxMemCongestionTrap": cpqb52nnPortRxMemCongestionTrap,
       "cpqn52nnOIDInfo": cpqn52nnOIDInfo,
       "cpqn5226": cpqn5226,
       "cpqn5226A": cpqn5226A,
       "cpqn52nnModuleInfo": cpqn52nnModuleInfo,
       "cpqn52nnVT100ScreenRefresh": cpqn52nnVT100ScreenRefresh,
       "cpqn52nnBooterWriteCycles": cpqn52nnBooterWriteCycles,
       "cpqn52nnRuntimeWriteCycles": cpqn52nnRuntimeWriteCycles,
       "cpqn52nnSwitchModeType": cpqn52nnSwitchModeType,
       "cpqn52nnCreateTimeout": cpqn52nnCreateTimeout,
       "cpqn52nnPowerSupplyTable": cpqn52nnPowerSupplyTable,
       "cpqn52nnPowerSupplyEntry": cpqn52nnPowerSupplyEntry,
       "cpqn52nnPsIndex": cpqn52nnPsIndex,
       "cpqn52nnPsStatus": cpqn52nnPsStatus,
       "cpqn52nnMemoryInfo": cpqn52nnMemoryInfo,
       "cpqn52nnHashInfo": cpqn52nnHashInfo,
       "cpqn52nnHashTableSize": cpqn52nnHashTableSize,
       "cpqn52nnRmonMemory": cpqn52nnRmonMemory,
       "cpqn52nnMaxMemory": cpqn52nnMaxMemory,
       "cpqn52nnMemAllocFailure": cpqn52nnMemAllocFailure,
       "cpqn52nnRmonMemoryCeiling": cpqn52nnRmonMemoryCeiling,
       "cpqn52nnStatisticsMemoryCeiling": cpqn52nnStatisticsMemoryCeiling,
       "cpqn52nnHistoryMemoryCeiling": cpqn52nnHistoryMemoryCeiling,
       "cpqn52nnAlarmMemoryCeiling": cpqn52nnAlarmMemoryCeiling,
       "cpqn52nnEventMemoryCeiling": cpqn52nnEventMemoryCeiling,
       "cpqn52nnRmonMemoryUsed": cpqn52nnRmonMemoryUsed,
       "cpqn52nnStatisticsMemoryUsed": cpqn52nnStatisticsMemoryUsed,
       "cpqn52nnHistoryMemoryUsed": cpqn52nnHistoryMemoryUsed,
       "cpqn52nnAlarmMemoryUsed": cpqn52nnAlarmMemoryUsed,
       "cpqn52nnEventMemoryUsed": cpqn52nnEventMemoryUsed,
       "cpqn52nnMemoryThreshold": cpqn52nnMemoryThreshold,
       "cpqn52nnMaxPktMemory": cpqn52nnMaxPktMemory,
       "cpqn52nnGlobalMemThreshTrapEnable": cpqn52nnGlobalMemThreshTrapEnable,
       "cpqn52nnBcastMemThreshEnable": cpqn52nnBcastMemThreshEnable,
       "cpqn52nnBcastPktCeiling": cpqn52nnBcastPktCeiling,
       "cpqn52nnBcastHysteresisCtl": cpqn52nnBcastHysteresisCtl,
       "cpqn52nnBcastPktCnt": cpqn52nnBcastPktCnt,
       "cpqn52nnBcastCongestionStatus": cpqn52nnBcastCongestionStatus,
       "cpqn52nnPortMemThreshTable": cpqn52nnPortMemThreshTable,
       "cpqn52nnPortMemThreshEntry": cpqn52nnPortMemThreshEntry,
       "cpqn52nnPortThreshIfIndex": cpqn52nnPortThreshIfIndex,
       "cpqn52nnPortTxPktThreshEnable": cpqn52nnPortTxPktThreshEnable,
       "cpqn52nnPortTxPktCongestionStatus": cpqn52nnPortTxPktCongestionStatus,
       "cpqn52nnPortTxPktCnt": cpqn52nnPortTxPktCnt,
       "cpqn52nnPortTxPktCeiling": cpqn52nnPortTxPktCeiling,
       "cpqn52nnPortTxPktHysteresisCtl": cpqn52nnPortTxPktHysteresisCtl,
       "cpqn52nnPortRxMemThreshEnable": cpqn52nnPortRxMemThreshEnable,
       "cpqn52nnPortRxMemCongestionStatus": cpqn52nnPortRxMemCongestionStatus,
       "cpqn52nnPortRxMemSectorCnt": cpqn52nnPortRxMemSectorCnt,
       "cpqn52nnPortRxMemCeiling": cpqn52nnPortRxMemCeiling,
       "cpqn52nnPortRxMemHysteresisCtl": cpqn52nnPortRxMemHysteresisCtl,
       "cpqn52nnPortCongestionTrapEnable": cpqn52nnPortCongestionTrapEnable,
       "cpqn52nnDramInfo": cpqn52nnDramInfo,
       "cpqn52nnDramTable": cpqn52nnDramTable,
       "cpqn52nnDramEntry": cpqn52nnDramEntry,
       "cpqn52nnDramIndex": cpqn52nnDramIndex,
       "cpqn52nnDramSize": cpqn52nnDramSize,
       "cpqn52nnDramType": cpqn52nnDramType,
       "cpqn52nnDramSpeed": cpqn52nnDramSpeed,
       "cpqn52nnPortInfo": cpqn52nnPortInfo,
       "cpqn52nnPortStatusTable": cpqn52nnPortStatusTable,
       "cpqn52nnPortStatusEntry": cpqn52nnPortStatusEntry,
       "cpqn52nnPortIfIndex": cpqn52nnPortIfIndex,
       "cpqn52nnPortIfMauIndex": cpqn52nnPortIfMauIndex,
       "cpqn52nnPortName": cpqn52nnPortName,
       "cpqn52nnPortType": cpqn52nnPortType,
       "cpqn52nnMdiMdixStatus": cpqn52nnMdiMdixStatus,
       "cpqn52nnMdiMdixEnable": cpqn52nnMdiMdixEnable,
       "cpqn52nnPortMonitorTable": cpqn52nnPortMonitorTable,
       "cpqn52nnPortMonitorEntry": cpqn52nnPortMonitorEntry,
       "cpqn52nnPortMonitorIndex": cpqn52nnPortMonitorIndex,
       "cpqn52nnPortMonitorRowStatus": cpqn52nnPortMonitorRowStatus,
       "cpqn52nnPortMonitorIfIndex": cpqn52nnPortMonitorIfIndex,
       "cpqn52nnPortMonitoredIfMap": cpqn52nnPortMonitoredIfMap,
       "cpqn52nnPortMonitoredDataType": cpqn52nnPortMonitoredDataType,
       "cpqn52nnPortBondingTable": cpqn52nnPortBondingTable,
       "cpqn52nnPortBondingEntry": cpqn52nnPortBondingEntry,
       "cpqn52nnBondIndex": cpqn52nnBondIndex,
       "cpqn52nnBondRowStatus": cpqn52nnBondRowStatus,
       "cpqn52nnBondMap": cpqn52nnBondMap,
       "cpqn52nnIfStatusInfo": cpqn52nnIfStatusInfo,
       "cpqn52nnIfStatusTable": cpqn52nnIfStatusTable,
       "cpqn52nnIfStatusEntry": cpqn52nnIfStatusEntry,
       "cpqn52nnIfStatusIfIndex": cpqn52nnIfStatusIfIndex,
       "cpqn52nnIfStatusIfType": cpqn52nnIfStatusIfType,
       "cpqn52nnIfStpStatus": cpqn52nnIfStpStatus,
       "cpqn52nnIfResetStatus": cpqn52nnIfResetStatus,
       "cpqn52nnIfLearningStatus": cpqn52nnIfLearningStatus,
       "cpqn52nnIfAgingStatus": cpqn52nnIfAgingStatus,
       "cpqn52nnIfAgingTime": cpqn52nnIfAgingTime,
       "cpqn52nnIfSwitchModeSrcStatus": cpqn52nnIfSwitchModeSrcStatus,
       "cpqn52nnIfSwitchModeDestStatus": cpqn52nnIfSwitchModeDestStatus,
       "cpqn52nnIfSwitchModeSrc": cpqn52nnIfSwitchModeSrc,
       "cpqn52nnIfSwitchModeDest": cpqn52nnIfSwitchModeDest,
       "cpqn52nnIfArbPriority": cpqn52nnIfArbPriority,
       "cpqn52nnIfStatsInfo": cpqn52nnIfStatsInfo,
       "cpqn52nnQuadCascade": cpqn52nnQuadCascade,
       "cpqn52nnQuadIfTable": cpqn52nnQuadIfTable,
       "cpqn52nnQuadIfEntry": cpqn52nnQuadIfEntry,
       "cpqn52nnQuadIfIndex": cpqn52nnQuadIfIndex,
       "cpqn52nnQuadIfAlignFcsErrors": cpqn52nnQuadIfAlignFcsErrors,
       "cpqn52nnQuadIfTxRunts": cpqn52nnQuadIfTxRunts,
       "cpqn52nnQuadIfRxRunts": cpqn52nnQuadIfRxRunts,
       "cpqn52nnQuadIfTotalCollisions": cpqn52nnQuadIfTotalCollisions,
       "cpqn52nnQuadIfCfgTable": cpqn52nnQuadIfCfgTable,
       "cpqn52nnQuadIfCfgEntry": cpqn52nnQuadIfCfgEntry,
       "cpqn52nnQuadIfCfgIndex": cpqn52nnQuadIfCfgIndex,
       "cpqn52nnQuadIfCfgMauIndex": cpqn52nnQuadIfCfgMauIndex,
       "cpqn52nnQuadIfCfgLinkForce": cpqn52nnQuadIfCfgLinkForce,
       "cpqn52nnQuadIfCfgLinkPolarityCorrect": cpqn52nnQuadIfCfgLinkPolarityCorrect,
       "cpqn52nnTlan": cpqn52nnTlan,
       "cpqn52nnTlanIfTable": cpqn52nnTlanIfTable,
       "cpqn52nnTlanIfEntry": cpqn52nnTlanIfEntry,
       "cpqn52nnTlanIfIndex": cpqn52nnTlanIfIndex,
       "cpqn52nnTlanIfTxGoodFrms": cpqn52nnTlanIfTxGoodFrms,
       "cpqn52nnTlanIfRxUndersizeFrms": cpqn52nnTlanIfRxUndersizeFrms,
       "cpqn52nnTlanIfRxOverruns": cpqn52nnTlanIfRxOverruns,
       "cpqn52nnTlanIfRxAlignSymbolErrs": cpqn52nnTlanIfRxAlignSymbolErrs,
       "cpqn52nnSwitchStatsInfo": cpqn52nnSwitchStatsInfo,
       "cpqn52nnHashMemory": cpqn52nnHashMemory,
       "cpqn52nnHashStaticNum": cpqn52nnHashStaticNum,
       "cpqn52nnHashDynamicNum": cpqn52nnHashDynamicNum,
       "cpqn52nnHashChainNum": cpqn52nnHashChainNum,
       "cpqn52nnHashChainLength": cpqn52nnHashChainLength,
       "cpqn52nnDropPkts": cpqn52nnDropPkts,
       "cpqn52nnDropsWholeMemoryCtr": cpqn52nnDropsWholeMemoryCtr,
       "cpqn52nnDropsBcastMemoryCtr": cpqn52nnDropsBcastMemoryCtr,
       "cpqn52nnDropsIfMemoryCtr": cpqn52nnDropsIfMemoryCtr,
       "cpqn52nnBusMonitorInfo": cpqn52nnBusMonitorInfo,
       "cpqn52nnBusMonTable": cpqn52nnBusMonTable,
       "cpqn52nnBusMonEntry": cpqn52nnBusMonEntry,
       "cpqn52nnBusMonIndex": cpqn52nnBusMonIndex,
       "cpqn52nnBusMonRowStatus": cpqn52nnBusMonRowStatus,
       "cpqn52nnBusMonBusType": cpqn52nnBusMonBusType,
       "cpqn52nnBusMonDataType": cpqn52nnBusMonDataType,
       "cpqn52nnBusMonPktType": cpqn52nnBusMonPktType,
       "cpqn52nnBusMonSwitchModeType": cpqn52nnBusMonSwitchModeType,
       "cpqn52nnBusMonCurrentUtilization": cpqn52nnBusMonCurrentUtilization,
       "cpqn52nnBusMonPeakUtilization": cpqn52nnBusMonPeakUtilization,
       "cpqn52nnBusMonRisingThreshold": cpqn52nnBusMonRisingThreshold,
       "cpqn52nnBusMonFallingThreshold": cpqn52nnBusMonFallingThreshold,
       "cpqn52nnBusMonAction": cpqn52nnBusMonAction,
       "cpqn52nnBusMonTrapEnable": cpqn52nnBusMonTrapEnable}
)
