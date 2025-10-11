# SNMP MIB module (Aricent-MIRSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/Aricent-MIRSTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:47 2025
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

(BridgeId,
 Timeout,
 fsDot1dBaseBridgeAddress,
 fsDot1dStpDesignatedRoot,
 fsDot1dStpPortState) = mibBuilder.importSymbols(
    "ARICENT-MIStdBRIDGE-MIB",
    "BridgeId",
    "Timeout",
    "fsDot1dBaseBridgeAddress",
    "fsDot1dStpDesignatedRoot",
    "fsDot1dStpPortState")

(fsDot1dStpVersion,) = mibBuilder.importSymbols(
    "ARICENT-MIStdRSTP-MIB",
    "fsDot1dStpVersion")

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

futureMIRstMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 119)
)
if mibBuilder.loadTexts:
    futureMIRstMIB.setRevisions(
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



class Timeout(TextualConvention, Integer32):
    status = "current"
    displayHint = "d4"


# MIB Managed Objects in the order of their OIDs

_FsMIDot1wFutureRst_ObjectIdentity = ObjectIdentity
fsMIDot1wFutureRst = _FsMIDot1wFutureRst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1)
)
_FsMIRstGlobalTrace_Type = TruthValue
_FsMIRstGlobalTrace_Object = MibScalar
fsMIRstGlobalTrace = _FsMIRstGlobalTrace_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 1),
    _FsMIRstGlobalTrace_Type()
)
fsMIRstGlobalTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstGlobalTrace.setStatus("current")
_FsMIRstGlobalDebug_Type = TruthValue
_FsMIRstGlobalDebug_Object = MibScalar
fsMIRstGlobalDebug = _FsMIRstGlobalDebug_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 2),
    _FsMIRstGlobalDebug_Type()
)
fsMIRstGlobalDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstGlobalDebug.setStatus("current")
_FsMIDot1wFutureRstTable_Object = MibTable
fsMIDot1wFutureRstTable = _FsMIDot1wFutureRstTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3)
)
if mibBuilder.loadTexts:
    fsMIDot1wFutureRstTable.setStatus("current")
_FsMIDot1wFutureRstEntry_Object = MibTableRow
fsMIDot1wFutureRstEntry = _FsMIDot1wFutureRstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1)
)
fsMIDot1wFutureRstEntry.setIndexNames(
    (0, "Aricent-MIRSTP-MIB", "fsMIDot1wFutureRstContextId"),
)
if mibBuilder.loadTexts:
    fsMIDot1wFutureRstEntry.setStatus("current")


class _FsMIDot1wFutureRstContextId_Type(Integer32):
    """Custom type fsMIDot1wFutureRstContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIDot1wFutureRstContextId_Type.__name__ = "Integer32"
_FsMIDot1wFutureRstContextId_Object = MibTableColumn
fsMIDot1wFutureRstContextId = _FsMIDot1wFutureRstContextId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 1),
    _FsMIDot1wFutureRstContextId_Type()
)
fsMIDot1wFutureRstContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDot1wFutureRstContextId.setStatus("current")


class _FsMIRstSystemControl_Type(Integer32):
    """Custom type fsMIRstSystemControl based on Integer32"""
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


_FsMIRstSystemControl_Type.__name__ = "Integer32"
_FsMIRstSystemControl_Object = MibTableColumn
fsMIRstSystemControl = _FsMIRstSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 2),
    _FsMIRstSystemControl_Type()
)
fsMIRstSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstSystemControl.setStatus("current")
_FsMIRstModuleStatus_Type = EnabledStatus
_FsMIRstModuleStatus_Object = MibTableColumn
fsMIRstModuleStatus = _FsMIRstModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 3),
    _FsMIRstModuleStatus_Type()
)
fsMIRstModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstModuleStatus.setStatus("current")


class _FsMIRstTraceOption_Type(Integer32):
    """Custom type fsMIRstTraceOption based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIRstTraceOption_Type.__name__ = "Integer32"
_FsMIRstTraceOption_Object = MibTableColumn
fsMIRstTraceOption = _FsMIRstTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 4),
    _FsMIRstTraceOption_Type()
)
fsMIRstTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstTraceOption.setStatus("current")


class _FsMIRstDebugOption_Type(Integer32):
    """Custom type fsMIRstDebugOption based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 524287),
    )


_FsMIRstDebugOption_Type.__name__ = "Integer32"
_FsMIRstDebugOption_Object = MibTableColumn
fsMIRstDebugOption = _FsMIRstDebugOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 5),
    _FsMIRstDebugOption_Type()
)
fsMIRstDebugOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstDebugOption.setStatus("current")
_FsMIRstRstpUpCount_Type = Counter32
_FsMIRstRstpUpCount_Object = MibTableColumn
fsMIRstRstpUpCount = _FsMIRstRstpUpCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 6),
    _FsMIRstRstpUpCount_Type()
)
fsMIRstRstpUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstRstpUpCount.setStatus("current")
_FsMIRstRstpDownCount_Type = Counter32
_FsMIRstRstpDownCount_Object = MibTableColumn
fsMIRstRstpDownCount = _FsMIRstRstpDownCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 7),
    _FsMIRstRstpDownCount_Type()
)
fsMIRstRstpDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstRstpDownCount.setStatus("current")
_FsMIRstBufferFailureCount_Type = Counter32
_FsMIRstBufferFailureCount_Object = MibTableColumn
fsMIRstBufferFailureCount = _FsMIRstBufferFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 8),
    _FsMIRstBufferFailureCount_Type()
)
fsMIRstBufferFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstBufferFailureCount.setStatus("current")
_FsMIRstMemAllocFailureCount_Type = Counter32
_FsMIRstMemAllocFailureCount_Object = MibTableColumn
fsMIRstMemAllocFailureCount = _FsMIRstMemAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 9),
    _FsMIRstMemAllocFailureCount_Type()
)
fsMIRstMemAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstMemAllocFailureCount.setStatus("current")
_FsMIRstNewRootIdCount_Type = Counter32
_FsMIRstNewRootIdCount_Object = MibTableColumn
fsMIRstNewRootIdCount = _FsMIRstNewRootIdCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 10),
    _FsMIRstNewRootIdCount_Type()
)
fsMIRstNewRootIdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstNewRootIdCount.setStatus("current")


class _FsMIRstPortRoleSelSmState_Type(Integer32):
    """Custom type fsMIRstPortRoleSelSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("initbridge", 0),
          ("roleselection", 1))
    )


_FsMIRstPortRoleSelSmState_Type.__name__ = "Integer32"
_FsMIRstPortRoleSelSmState_Object = MibTableColumn
fsMIRstPortRoleSelSmState = _FsMIRstPortRoleSelSmState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 11),
    _FsMIRstPortRoleSelSmState_Type()
)
fsMIRstPortRoleSelSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortRoleSelSmState.setStatus("current")
_FsMIRstOldDesignatedRoot_Type = BridgeId
_FsMIRstOldDesignatedRoot_Object = MibTableColumn
fsMIRstOldDesignatedRoot = _FsMIRstOldDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 12),
    _FsMIRstOldDesignatedRoot_Type()
)
fsMIRstOldDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstOldDesignatedRoot.setStatus("current")


class _FsMIRstDynamicPathcostCalculation_Type(TruthValue):
    """Custom type fsMIRstDynamicPathcostCalculation based on TruthValue"""
    defaultValue = 2


_FsMIRstDynamicPathcostCalculation_Type.__name__ = "TruthValue"
_FsMIRstDynamicPathcostCalculation_Object = MibTableColumn
fsMIRstDynamicPathcostCalculation = _FsMIRstDynamicPathcostCalculation_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 13),
    _FsMIRstDynamicPathcostCalculation_Type()
)
fsMIRstDynamicPathcostCalculation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstDynamicPathcostCalculation.setStatus("current")


class _FsMIRstContextName_Type(DisplayString):
    """Custom type fsMIRstContextName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsMIRstContextName_Type.__name__ = "DisplayString"
_FsMIRstContextName_Object = MibTableColumn
fsMIRstContextName = _FsMIRstContextName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 14),
    _FsMIRstContextName_Type()
)
fsMIRstContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstContextName.setStatus("current")


class _FsMIRstCalcPortPathCostOnSpeedChg_Type(TruthValue):
    """Custom type fsMIRstCalcPortPathCostOnSpeedChg based on TruthValue"""
    defaultValue = 2


_FsMIRstCalcPortPathCostOnSpeedChg_Type.__name__ = "TruthValue"
_FsMIRstCalcPortPathCostOnSpeedChg_Object = MibTableColumn
fsMIRstCalcPortPathCostOnSpeedChg = _FsMIRstCalcPortPathCostOnSpeedChg_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 15),
    _FsMIRstCalcPortPathCostOnSpeedChg_Type()
)
fsMIRstCalcPortPathCostOnSpeedChg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstCalcPortPathCostOnSpeedChg.setStatus("current")
_FsMIRstClearBridgeStats_Type = TruthValue
_FsMIRstClearBridgeStats_Object = MibTableColumn
fsMIRstClearBridgeStats = _FsMIRstClearBridgeStats_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 16),
    _FsMIRstClearBridgeStats_Type()
)
fsMIRstClearBridgeStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstClearBridgeStats.setStatus("current")


class _FsMIRstRcvdEvent_Type(Integer32):
    """Custom type fsMIRstRcvdEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configurationEvent", 1),
          ("bpduEvent", 2),
          ("timerExpiryEvent", 3))
    )


_FsMIRstRcvdEvent_Type.__name__ = "Integer32"
_FsMIRstRcvdEvent_Object = MibTableColumn
fsMIRstRcvdEvent = _FsMIRstRcvdEvent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 17),
    _FsMIRstRcvdEvent_Type()
)
fsMIRstRcvdEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstRcvdEvent.setStatus("current")
_FsMIRstRcvdEventSubType_Type = Integer32
_FsMIRstRcvdEventSubType_Object = MibTableColumn
fsMIRstRcvdEventSubType = _FsMIRstRcvdEventSubType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 18),
    _FsMIRstRcvdEventSubType_Type()
)
fsMIRstRcvdEventSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstRcvdEventSubType.setStatus("current")
_FsMIRstRcvdEventTimeStamp_Type = Unsigned32
_FsMIRstRcvdEventTimeStamp_Object = MibTableColumn
fsMIRstRcvdEventTimeStamp = _FsMIRstRcvdEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 19),
    _FsMIRstRcvdEventTimeStamp_Type()
)
fsMIRstRcvdEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstRcvdEventTimeStamp.setStatus("current")
_FsMIRstRcvdPortStateChangeTimeStamp_Type = Unsigned32
_FsMIRstRcvdPortStateChangeTimeStamp_Object = MibTableColumn
fsMIRstRcvdPortStateChangeTimeStamp = _FsMIRstRcvdPortStateChangeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 20),
    _FsMIRstRcvdPortStateChangeTimeStamp_Type()
)
fsMIRstRcvdPortStateChangeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstRcvdPortStateChangeTimeStamp.setStatus("current")


class _FsMIRstFlushInterval_Type(Timeout):
    """Custom type fsMIRstFlushInterval based on Timeout"""
    defaultValue = 0

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_FsMIRstFlushInterval_Type.__name__ = "Timeout"
_FsMIRstFlushInterval_Object = MibTableColumn
fsMIRstFlushInterval = _FsMIRstFlushInterval_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 21),
    _FsMIRstFlushInterval_Type()
)
fsMIRstFlushInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstFlushInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsMIRstFlushInterval.setUnits("centi-seconds")


class _FsMIRstFlushIndicationThreshold_Type(Integer32):
    """Custom type fsMIRstFlushIndicationThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIRstFlushIndicationThreshold_Type.__name__ = "Integer32"
_FsMIRstFlushIndicationThreshold_Object = MibTableColumn
fsMIRstFlushIndicationThreshold = _FsMIRstFlushIndicationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 22),
    _FsMIRstFlushIndicationThreshold_Type()
)
fsMIRstFlushIndicationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstFlushIndicationThreshold.setStatus("current")
_FsMIRstTotalFlushCount_Type = Counter32
_FsMIRstTotalFlushCount_Object = MibTableColumn
fsMIRstTotalFlushCount = _FsMIRstTotalFlushCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 23),
    _FsMIRstTotalFlushCount_Type()
)
fsMIRstTotalFlushCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstTotalFlushCount.setStatus("current")


class _FsMIRstFwdDelayAltPortRoleTrOptimization_Type(EnabledStatus):
    """Custom type fsMIRstFwdDelayAltPortRoleTrOptimization based on EnabledStatus"""
    defaultValue = 1


_FsMIRstFwdDelayAltPortRoleTrOptimization_Type.__name__ = "EnabledStatus"
_FsMIRstFwdDelayAltPortRoleTrOptimization_Object = MibTableColumn
fsMIRstFwdDelayAltPortRoleTrOptimization = _FsMIRstFwdDelayAltPortRoleTrOptimization_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 24),
    _FsMIRstFwdDelayAltPortRoleTrOptimization_Type()
)
fsMIRstFwdDelayAltPortRoleTrOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstFwdDelayAltPortRoleTrOptimization.setStatus("current")


class _FsMIRstBpduGuard_Type(Integer32):
    """Custom type fsMIRstBpduGuard based on Integer32"""
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


_FsMIRstBpduGuard_Type.__name__ = "Integer32"
_FsMIRstBpduGuard_Object = MibTableColumn
fsMIRstBpduGuard = _FsMIRstBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 25),
    _FsMIRstBpduGuard_Type()
)
fsMIRstBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstBpduGuard.setStatus("current")


class _FsMIRstStpPerfStatus_Type(Integer32):
    """Custom type fsMIRstStpPerfStatus based on Integer32"""
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


_FsMIRstStpPerfStatus_Type.__name__ = "Integer32"
_FsMIRstStpPerfStatus_Object = MibTableColumn
fsMIRstStpPerfStatus = _FsMIRstStpPerfStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 3, 1, 26),
    _FsMIRstStpPerfStatus_Type()
)
fsMIRstStpPerfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstStpPerfStatus.setStatus("current")
_FsMIRstPortExtTable_Object = MibTable
fsMIRstPortExtTable = _FsMIRstPortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4)
)
if mibBuilder.loadTexts:
    fsMIRstPortExtTable.setStatus("current")
_FsMIRstPortExtEntry_Object = MibTableRow
fsMIRstPortExtEntry = _FsMIRstPortExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1)
)
fsMIRstPortExtEntry.setIndexNames(
    (0, "Aricent-MIRSTP-MIB", "fsMIRstPort"),
)
if mibBuilder.loadTexts:
    fsMIRstPortExtEntry.setStatus("current")


class _FsMIRstPort_Type(Integer32):
    """Custom type fsMIRstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FsMIRstPort_Type.__name__ = "Integer32"
_FsMIRstPort_Object = MibTableColumn
fsMIRstPort = _FsMIRstPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 1),
    _FsMIRstPort_Type()
)
fsMIRstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRstPort.setStatus("current")


class _FsMIRstPortRole_Type(Integer32):
    """Custom type fsMIRstPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabledPort", 0),
          ("alternatePort", 1),
          ("backupPort", 2),
          ("rootPort", 3),
          ("designatedPort", 4))
    )


_FsMIRstPortRole_Type.__name__ = "Integer32"
_FsMIRstPortRole_Object = MibTableColumn
fsMIRstPortRole = _FsMIRstPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 2),
    _FsMIRstPortRole_Type()
)
fsMIRstPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortRole.setStatus("current")


class _FsMIRstPortOperVersion_Type(Integer32):
    """Custom type fsMIRstPortOperVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stpCompatible", 0),
          ("rstp", 2))
    )


_FsMIRstPortOperVersion_Type.__name__ = "Integer32"
_FsMIRstPortOperVersion_Object = MibTableColumn
fsMIRstPortOperVersion = _FsMIRstPortOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 3),
    _FsMIRstPortOperVersion_Type()
)
fsMIRstPortOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortOperVersion.setStatus("current")


class _FsMIRstPortInfoSmState_Type(Integer32):
    """Custom type fsMIRstPortInfoSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("aged", 1),
          ("update", 2),
          ("superior", 3),
          ("repeat", 4),
          ("notdesignated", 5),
          ("present", 6),
          ("receive", 7),
          ("inferiordesignated", 8))
    )


_FsMIRstPortInfoSmState_Type.__name__ = "Integer32"
_FsMIRstPortInfoSmState_Object = MibTableColumn
fsMIRstPortInfoSmState = _FsMIRstPortInfoSmState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 4),
    _FsMIRstPortInfoSmState_Type()
)
fsMIRstPortInfoSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortInfoSmState.setStatus("current")


class _FsMIRstPortMigSmState_Type(Integer32):
    """Custom type fsMIRstPortMigSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("checkingrstp", 0),
          ("selectingstp", 1),
          ("sensing", 2))
    )


_FsMIRstPortMigSmState_Type.__name__ = "Integer32"
_FsMIRstPortMigSmState_Object = MibTableColumn
fsMIRstPortMigSmState = _FsMIRstPortMigSmState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 5),
    _FsMIRstPortMigSmState_Type()
)
fsMIRstPortMigSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortMigSmState.setStatus("current")


class _FsMIRstPortRoleTransSmState_Type(Integer32):
    """Custom type fsMIRstPortRoleTransSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("disableport", 1),
          ("disabledport", 2),
          ("rootport", 3),
          ("designatedport", 4),
          ("backupport", 5),
          ("rootproposed", 6),
          ("rootagreed", 7),
          ("reroot", 8),
          ("rootforward", 9),
          ("rootlearn", 10),
          ("rerooted", 11),
          ("designatedpropose", 12),
          ("designatedsynced", 13),
          ("designatedretired", 14),
          ("designatedforward", 15),
          ("designatedlearn", 16),
          ("designatedlisten", 17))
    )


_FsMIRstPortRoleTransSmState_Type.__name__ = "Integer32"
_FsMIRstPortRoleTransSmState_Object = MibTableColumn
fsMIRstPortRoleTransSmState = _FsMIRstPortRoleTransSmState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 6),
    _FsMIRstPortRoleTransSmState_Type()
)
fsMIRstPortRoleTransSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortRoleTransSmState.setStatus("current")


class _FsMIRstPortStateTransSmState_Type(Integer32):
    """Custom type fsMIRstPortStateTransSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 0),
          ("learning", 1),
          ("forwarding", 2))
    )


_FsMIRstPortStateTransSmState_Type.__name__ = "Integer32"
_FsMIRstPortStateTransSmState_Object = MibTableColumn
fsMIRstPortStateTransSmState = _FsMIRstPortStateTransSmState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 7),
    _FsMIRstPortStateTransSmState_Type()
)
fsMIRstPortStateTransSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortStateTransSmState.setStatus("current")


class _FsMIRstPortTopoChSmState_Type(Integer32):
    """Custom type fsMIRstPortTopoChSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("learning", 1),
          ("detected", 2),
          ("active", 3),
          ("notifiedtcn", 4),
          ("notifiedtc", 5),
          ("propagating", 6),
          ("acknowledged", 7))
    )


_FsMIRstPortTopoChSmState_Type.__name__ = "Integer32"
_FsMIRstPortTopoChSmState_Object = MibTableColumn
fsMIRstPortTopoChSmState = _FsMIRstPortTopoChSmState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 8),
    _FsMIRstPortTopoChSmState_Type()
)
fsMIRstPortTopoChSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortTopoChSmState.setStatus("current")


class _FsMIRstPortTxSmState_Type(Integer32):
    """Custom type fsMIRstPortTxSmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("transmitinit", 0),
          ("transmitperiodic", 1),
          ("transmitconfig", 2),
          ("transmittcn", 3),
          ("transmitrstp", 4),
          ("idle", 5))
    )


_FsMIRstPortTxSmState_Type.__name__ = "Integer32"
_FsMIRstPortTxSmState_Object = MibTableColumn
fsMIRstPortTxSmState = _FsMIRstPortTxSmState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 9),
    _FsMIRstPortTxSmState_Type()
)
fsMIRstPortTxSmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortTxSmState.setStatus("current")
_FsMIRstPortRxRstBpduCount_Type = Counter32
_FsMIRstPortRxRstBpduCount_Object = MibTableColumn
fsMIRstPortRxRstBpduCount = _FsMIRstPortRxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 10),
    _FsMIRstPortRxRstBpduCount_Type()
)
fsMIRstPortRxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortRxRstBpduCount.setStatus("current")
_FsMIRstPortRxConfigBpduCount_Type = Counter32
_FsMIRstPortRxConfigBpduCount_Object = MibTableColumn
fsMIRstPortRxConfigBpduCount = _FsMIRstPortRxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 11),
    _FsMIRstPortRxConfigBpduCount_Type()
)
fsMIRstPortRxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortRxConfigBpduCount.setStatus("current")
_FsMIRstPortRxTcnBpduCount_Type = Counter32
_FsMIRstPortRxTcnBpduCount_Object = MibTableColumn
fsMIRstPortRxTcnBpduCount = _FsMIRstPortRxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 12),
    _FsMIRstPortRxTcnBpduCount_Type()
)
fsMIRstPortRxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortRxTcnBpduCount.setStatus("current")
_FsMIRstPortTxRstBpduCount_Type = Counter32
_FsMIRstPortTxRstBpduCount_Object = MibTableColumn
fsMIRstPortTxRstBpduCount = _FsMIRstPortTxRstBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 13),
    _FsMIRstPortTxRstBpduCount_Type()
)
fsMIRstPortTxRstBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortTxRstBpduCount.setStatus("current")
_FsMIRstPortTxConfigBpduCount_Type = Counter32
_FsMIRstPortTxConfigBpduCount_Object = MibTableColumn
fsMIRstPortTxConfigBpduCount = _FsMIRstPortTxConfigBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 14),
    _FsMIRstPortTxConfigBpduCount_Type()
)
fsMIRstPortTxConfigBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortTxConfigBpduCount.setStatus("current")
_FsMIRstPortTxTcnBpduCount_Type = Counter32
_FsMIRstPortTxTcnBpduCount_Object = MibTableColumn
fsMIRstPortTxTcnBpduCount = _FsMIRstPortTxTcnBpduCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 15),
    _FsMIRstPortTxTcnBpduCount_Type()
)
fsMIRstPortTxTcnBpduCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortTxTcnBpduCount.setStatus("current")
_FsMIRstPortInvalidRstBpduRxCount_Type = Counter32
_FsMIRstPortInvalidRstBpduRxCount_Object = MibTableColumn
fsMIRstPortInvalidRstBpduRxCount = _FsMIRstPortInvalidRstBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 16),
    _FsMIRstPortInvalidRstBpduRxCount_Type()
)
fsMIRstPortInvalidRstBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortInvalidRstBpduRxCount.setStatus("current")
_FsMIRstPortInvalidConfigBpduRxCount_Type = Counter32
_FsMIRstPortInvalidConfigBpduRxCount_Object = MibTableColumn
fsMIRstPortInvalidConfigBpduRxCount = _FsMIRstPortInvalidConfigBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 17),
    _FsMIRstPortInvalidConfigBpduRxCount_Type()
)
fsMIRstPortInvalidConfigBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortInvalidConfigBpduRxCount.setStatus("current")
_FsMIRstPortInvalidTcnBpduRxCount_Type = Counter32
_FsMIRstPortInvalidTcnBpduRxCount_Object = MibTableColumn
fsMIRstPortInvalidTcnBpduRxCount = _FsMIRstPortInvalidTcnBpduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 18),
    _FsMIRstPortInvalidTcnBpduRxCount_Type()
)
fsMIRstPortInvalidTcnBpduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortInvalidTcnBpduRxCount.setStatus("current")
_FsMIRstPortProtocolMigrationCount_Type = Counter32
_FsMIRstPortProtocolMigrationCount_Object = MibTableColumn
fsMIRstPortProtocolMigrationCount = _FsMIRstPortProtocolMigrationCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 19),
    _FsMIRstPortProtocolMigrationCount_Type()
)
fsMIRstPortProtocolMigrationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortProtocolMigrationCount.setStatus("current")
_FsMIRstPortEffectivePortState_Type = TruthValue
_FsMIRstPortEffectivePortState_Object = MibTableColumn
fsMIRstPortEffectivePortState = _FsMIRstPortEffectivePortState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 20),
    _FsMIRstPortEffectivePortState_Type()
)
fsMIRstPortEffectivePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortEffectivePortState.setStatus("current")
_FsMIRstPortAutoEdge_Type = TruthValue
_FsMIRstPortAutoEdge_Object = MibTableColumn
fsMIRstPortAutoEdge = _FsMIRstPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 21),
    _FsMIRstPortAutoEdge_Type()
)
fsMIRstPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstPortAutoEdge.setStatus("current")
_FsMIRstPortRestrictedRole_Type = TruthValue
_FsMIRstPortRestrictedRole_Object = MibTableColumn
fsMIRstPortRestrictedRole = _FsMIRstPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 22),
    _FsMIRstPortRestrictedRole_Type()
)
fsMIRstPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstPortRestrictedRole.setStatus("current")
_FsMIRstPortRestrictedTCN_Type = TruthValue
_FsMIRstPortRestrictedTCN_Object = MibTableColumn
fsMIRstPortRestrictedTCN = _FsMIRstPortRestrictedTCN_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 23),
    _FsMIRstPortRestrictedTCN_Type()
)
fsMIRstPortRestrictedTCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstPortRestrictedTCN.setStatus("current")


class _FsMIRstPortEnableBPDURx_Type(TruthValue):
    """Custom type fsMIRstPortEnableBPDURx based on TruthValue"""
    defaultValue = 1


_FsMIRstPortEnableBPDURx_Type.__name__ = "TruthValue"
_FsMIRstPortEnableBPDURx_Object = MibTableColumn
fsMIRstPortEnableBPDURx = _FsMIRstPortEnableBPDURx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 24),
    _FsMIRstPortEnableBPDURx_Type()
)
fsMIRstPortEnableBPDURx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstPortEnableBPDURx.setStatus("current")


class _FsMIRstPortEnableBPDUTx_Type(TruthValue):
    """Custom type fsMIRstPortEnableBPDUTx based on TruthValue"""
    defaultValue = 1


_FsMIRstPortEnableBPDUTx_Type.__name__ = "TruthValue"
_FsMIRstPortEnableBPDUTx_Object = MibTableColumn
fsMIRstPortEnableBPDUTx = _FsMIRstPortEnableBPDUTx_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 25),
    _FsMIRstPortEnableBPDUTx_Type()
)
fsMIRstPortEnableBPDUTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstPortEnableBPDUTx.setStatus("current")
_FsMIRstPortPseudoRootId_Type = BridgeId
_FsMIRstPortPseudoRootId_Object = MibTableColumn
fsMIRstPortPseudoRootId = _FsMIRstPortPseudoRootId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 26),
    _FsMIRstPortPseudoRootId_Type()
)
fsMIRstPortPseudoRootId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstPortPseudoRootId.setStatus("current")


class _FsMIRstPortIsL2Gp_Type(TruthValue):
    """Custom type fsMIRstPortIsL2Gp based on TruthValue"""
    defaultValue = 2


_FsMIRstPortIsL2Gp_Type.__name__ = "TruthValue"
_FsMIRstPortIsL2Gp_Object = MibTableColumn
fsMIRstPortIsL2Gp = _FsMIRstPortIsL2Gp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 27),
    _FsMIRstPortIsL2Gp_Type()
)
fsMIRstPortIsL2Gp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstPortIsL2Gp.setStatus("current")


class _FsMIRstPortLoopGuard_Type(TruthValue):
    """Custom type fsMIRstPortLoopGuard based on TruthValue"""
    defaultValue = 2


_FsMIRstPortLoopGuard_Type.__name__ = "TruthValue"
_FsMIRstPortLoopGuard_Object = MibTableColumn
fsMIRstPortLoopGuard = _FsMIRstPortLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 28),
    _FsMIRstPortLoopGuard_Type()
)
fsMIRstPortLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstPortLoopGuard.setStatus("current")
_FsMIRstPortClearStats_Type = TruthValue
_FsMIRstPortClearStats_Object = MibTableColumn
fsMIRstPortClearStats = _FsMIRstPortClearStats_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 29),
    _FsMIRstPortClearStats_Type()
)
fsMIRstPortClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstPortClearStats.setStatus("current")


class _FsMIRstPortRcvdEvent_Type(Integer32):
    """Custom type fsMIRstPortRcvdEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configurationEvent", 1),
          ("bpduEvent", 2),
          ("timerExpiryEvent", 3))
    )


_FsMIRstPortRcvdEvent_Type.__name__ = "Integer32"
_FsMIRstPortRcvdEvent_Object = MibTableColumn
fsMIRstPortRcvdEvent = _FsMIRstPortRcvdEvent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 30),
    _FsMIRstPortRcvdEvent_Type()
)
fsMIRstPortRcvdEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortRcvdEvent.setStatus("current")
_FsMIRstPortRcvdEventSubType_Type = Integer32
_FsMIRstPortRcvdEventSubType_Object = MibTableColumn
fsMIRstPortRcvdEventSubType = _FsMIRstPortRcvdEventSubType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 31),
    _FsMIRstPortRcvdEventSubType_Type()
)
fsMIRstPortRcvdEventSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortRcvdEventSubType.setStatus("current")
_FsMIRstPortRcvdEventTimeStamp_Type = Unsigned32
_FsMIRstPortRcvdEventTimeStamp_Object = MibTableColumn
fsMIRstPortRcvdEventTimeStamp = _FsMIRstPortRcvdEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 32),
    _FsMIRstPortRcvdEventTimeStamp_Type()
)
fsMIRstPortRcvdEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortRcvdEventTimeStamp.setStatus("current")
_FsMIRstPortStateChangeTimeStamp_Type = Unsigned32
_FsMIRstPortStateChangeTimeStamp_Object = MibTableColumn
fsMIRstPortStateChangeTimeStamp = _FsMIRstPortStateChangeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 33),
    _FsMIRstPortStateChangeTimeStamp_Type()
)
fsMIRstPortStateChangeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortStateChangeTimeStamp.setStatus("current")
_FsMIRstPortRowStatus_Type = RowStatus
_FsMIRstPortRowStatus_Object = MibTableColumn
fsMIRstPortRowStatus = _FsMIRstPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 34),
    _FsMIRstPortRowStatus_Type()
)
fsMIRstPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIRstPortRowStatus.setStatus("current")


class _FsMIRstLoopInconsistentState_Type(TruthValue):
    """Custom type fsMIRstLoopInconsistentState based on TruthValue"""
    defaultValue = 2


_FsMIRstLoopInconsistentState_Type.__name__ = "TruthValue"
_FsMIRstLoopInconsistentState_Object = MibTableColumn
fsMIRstLoopInconsistentState = _FsMIRstLoopInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 35),
    _FsMIRstLoopInconsistentState_Type()
)
fsMIRstLoopInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstLoopInconsistentState.setStatus("current")


class _FsMIRstPortBpduGuard_Type(Integer32):
    """Custom type fsMIRstPortBpduGuard based on Integer32"""
    defaultValue = 0

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
          ("enable", 1),
          ("disable", 2))
    )


_FsMIRstPortBpduGuard_Type.__name__ = "Integer32"
_FsMIRstPortBpduGuard_Object = MibTableColumn
fsMIRstPortBpduGuard = _FsMIRstPortBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 36),
    _FsMIRstPortBpduGuard_Type()
)
fsMIRstPortBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstPortBpduGuard.setStatus("current")


class _FsMIRstPortRootGuard_Type(TruthValue):
    """Custom type fsMIRstPortRootGuard based on TruthValue"""
    defaultValue = 2


_FsMIRstPortRootGuard_Type.__name__ = "TruthValue"
_FsMIRstPortRootGuard_Object = MibTableColumn
fsMIRstPortRootGuard = _FsMIRstPortRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 37),
    _FsMIRstPortRootGuard_Type()
)
fsMIRstPortRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstPortRootGuard.setStatus("current")


class _FsMIRstRootInconsistentState_Type(TruthValue):
    """Custom type fsMIRstRootInconsistentState based on TruthValue"""
    defaultValue = 2


_FsMIRstRootInconsistentState_Type.__name__ = "TruthValue"
_FsMIRstRootInconsistentState_Object = MibTableColumn
fsMIRstRootInconsistentState = _FsMIRstRootInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 38),
    _FsMIRstRootInconsistentState_Type()
)
fsMIRstRootInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstRootInconsistentState.setStatus("current")


class _FsMIRstPortErrorRecovery_Type(Timeout):
    """Custom type fsMIRstPortErrorRecovery based on Timeout"""
    defaultValue = 30000

    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3000, 6553500),
    )


_FsMIRstPortErrorRecovery_Type.__name__ = "Timeout"
_FsMIRstPortErrorRecovery_Object = MibTableColumn
fsMIRstPortErrorRecovery = _FsMIRstPortErrorRecovery_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 39),
    _FsMIRstPortErrorRecovery_Type()
)
fsMIRstPortErrorRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstPortErrorRecovery.setStatus("current")
if mibBuilder.loadTexts:
    fsMIRstPortErrorRecovery.setUnits("centi-seconds")


class _FsMIRstPortStpModeDot1wEnabled_Type(EnabledStatus):
    """Custom type fsMIRstPortStpModeDot1wEnabled based on EnabledStatus"""
    defaultValue = 2


_FsMIRstPortStpModeDot1wEnabled_Type.__name__ = "EnabledStatus"
_FsMIRstPortStpModeDot1wEnabled_Object = MibTableColumn
fsMIRstPortStpModeDot1wEnabled = _FsMIRstPortStpModeDot1wEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 40),
    _FsMIRstPortStpModeDot1wEnabled_Type()
)
fsMIRstPortStpModeDot1wEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstPortStpModeDot1wEnabled.setStatus("current")


class _FsMIRstPortBpduInconsistentState_Type(TruthValue):
    """Custom type fsMIRstPortBpduInconsistentState based on TruthValue"""
    defaultValue = 2


_FsMIRstPortBpduInconsistentState_Type.__name__ = "TruthValue"
_FsMIRstPortBpduInconsistentState_Object = MibTableColumn
fsMIRstPortBpduInconsistentState = _FsMIRstPortBpduInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 41),
    _FsMIRstPortBpduInconsistentState_Type()
)
fsMIRstPortBpduInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortBpduInconsistentState.setStatus("current")


class _FsMIRstPortBpduGuardAction_Type(Integer32):
    """Custom type fsMIRstPortBpduGuardAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-discarding", 1),
          ("admin-down", 2))
    )


_FsMIRstPortBpduGuardAction_Type.__name__ = "Integer32"
_FsMIRstPortBpduGuardAction_Object = MibTableColumn
fsMIRstPortBpduGuardAction = _FsMIRstPortBpduGuardAction_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 1, 4, 1, 42),
    _FsMIRstPortBpduGuardAction_Type()
)
fsMIRstPortBpduGuardAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstPortBpduGuardAction.setStatus("current")
_FsMIDot1wFsRstTrapsControl_ObjectIdentity = ObjectIdentity
fsMIDot1wFsRstTrapsControl = _FsMIDot1wFsRstTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 119, 2)
)


class _FsMIRstSetGlobalTraps_Type(Integer32):
    """Custom type fsMIRstSetGlobalTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsMIRstSetGlobalTraps_Type.__name__ = "Integer32"
_FsMIRstSetGlobalTraps_Object = MibScalar
fsMIRstSetGlobalTraps = _FsMIRstSetGlobalTraps_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 2, 1),
    _FsMIRstSetGlobalTraps_Type()
)
fsMIRstSetGlobalTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstSetGlobalTraps.setStatus("current")


class _FsMIRstGlobalErrTrapType_Type(Integer32):
    """Custom type fsMIRstGlobalErrTrapType based on Integer32"""
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


_FsMIRstGlobalErrTrapType_Type.__name__ = "Integer32"
_FsMIRstGlobalErrTrapType_Object = MibScalar
fsMIRstGlobalErrTrapType = _FsMIRstGlobalErrTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 2, 2),
    _FsMIRstGlobalErrTrapType_Type()
)
fsMIRstGlobalErrTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstGlobalErrTrapType.setStatus("current")
_FsMIDot1wFsRstTrapsControlTable_Object = MibTable
fsMIDot1wFsRstTrapsControlTable = _FsMIDot1wFsRstTrapsControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 2, 3)
)
if mibBuilder.loadTexts:
    fsMIDot1wFsRstTrapsControlTable.setStatus("current")
_FsMIDot1wFsRstTrapsControlEntry_Object = MibTableRow
fsMIDot1wFsRstTrapsControlEntry = _FsMIDot1wFsRstTrapsControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 2, 3, 1)
)
fsMIDot1wFsRstTrapsControlEntry.setIndexNames(
    (0, "Aricent-MIRSTP-MIB", "fsMIDot1wFutureRstContextId"),
)
if mibBuilder.loadTexts:
    fsMIDot1wFsRstTrapsControlEntry.setStatus("current")


class _FsMIRstSetTraps_Type(Integer32):
    """Custom type fsMIRstSetTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FsMIRstSetTraps_Type.__name__ = "Integer32"
_FsMIRstSetTraps_Object = MibTableColumn
fsMIRstSetTraps = _FsMIRstSetTraps_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 2, 3, 1, 1),
    _FsMIRstSetTraps_Type()
)
fsMIRstSetTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRstSetTraps.setStatus("current")


class _FsMIRstGenTrapType_Type(Integer32):
    """Custom type fsMIRstGenTrapType based on Integer32"""
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
          ("up", 1),
          ("down", 2))
    )


_FsMIRstGenTrapType_Type.__name__ = "Integer32"
_FsMIRstGenTrapType_Object = MibTableColumn
fsMIRstGenTrapType = _FsMIRstGenTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 2, 3, 1, 2),
    _FsMIRstGenTrapType_Type()
)
fsMIRstGenTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstGenTrapType.setStatus("current")
_FsMIRstPortTrapNotificationTable_Object = MibTable
fsMIRstPortTrapNotificationTable = _FsMIRstPortTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 2, 4)
)
if mibBuilder.loadTexts:
    fsMIRstPortTrapNotificationTable.setStatus("current")
_FsMIRstPortTrapNotificationEntry_Object = MibTableRow
fsMIRstPortTrapNotificationEntry = _FsMIRstPortTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 2, 4, 1)
)
fsMIRstPortTrapNotificationEntry.setIndexNames(
    (0, "Aricent-MIRSTP-MIB", "fsMIRstPortTrapIndex"),
)
if mibBuilder.loadTexts:
    fsMIRstPortTrapNotificationEntry.setStatus("current")


class _FsMIRstPortTrapIndex_Type(Integer32):
    """Custom type fsMIRstPortTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_FsMIRstPortTrapIndex_Type.__name__ = "Integer32"
_FsMIRstPortTrapIndex_Object = MibTableColumn
fsMIRstPortTrapIndex = _FsMIRstPortTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 2, 4, 1, 1),
    _FsMIRstPortTrapIndex_Type()
)
fsMIRstPortTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRstPortTrapIndex.setStatus("current")


class _FsMIRstPortMigrationType_Type(Integer32):
    """Custom type fsMIRstPortMigrationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sendstp", 0),
          ("sendrstp", 1))
    )


_FsMIRstPortMigrationType_Type.__name__ = "Integer32"
_FsMIRstPortMigrationType_Object = MibTableColumn
fsMIRstPortMigrationType = _FsMIRstPortMigrationType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 2, 4, 1, 2),
    _FsMIRstPortMigrationType_Type()
)
fsMIRstPortMigrationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortMigrationType.setStatus("current")


class _FsMIRstPktErrType_Type(Integer32):
    """Custom type fsMIRstPktErrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("protocolIdErr", 0),
          ("invalidBpdu", 1),
          ("configLengthErr", 2),
          ("tcnLengthErr", 3),
          ("rstpLengthErr", 4),
          ("maxAgeErr", 5),
          ("fwdDelayErr", 6),
          ("helloTimeErr", 7))
    )


_FsMIRstPktErrType_Type.__name__ = "Integer32"
_FsMIRstPktErrType_Object = MibTableColumn
fsMIRstPktErrType = _FsMIRstPktErrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 2, 4, 1, 3),
    _FsMIRstPktErrType_Type()
)
fsMIRstPktErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPktErrType.setStatus("current")
_FsMIRstPktErrVal_Type = Integer32
_FsMIRstPktErrVal_Object = MibTableColumn
fsMIRstPktErrVal = _FsMIRstPktErrVal_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 2, 4, 1, 4),
    _FsMIRstPktErrVal_Type()
)
fsMIRstPktErrVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPktErrVal.setStatus("current")


class _FsMIRstPortRoleType_Type(Integer32):
    """Custom type fsMIRstPortRoleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabledPort", 0),
          ("alternatePort", 1),
          ("backupPort", 2),
          ("rootPort", 3),
          ("designatedPort", 4))
    )


_FsMIRstPortRoleType_Type.__name__ = "Integer32"
_FsMIRstPortRoleType_Object = MibTableColumn
fsMIRstPortRoleType = _FsMIRstPortRoleType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 2, 4, 1, 5),
    _FsMIRstPortRoleType_Type()
)
fsMIRstPortRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstPortRoleType.setStatus("current")


class _FsMIRstOldRoleType_Type(Integer32):
    """Custom type fsMIRstOldRoleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabledPort", 0),
          ("alternatePort", 1),
          ("backupPort", 2),
          ("rootPort", 3),
          ("designatedPort", 4))
    )


_FsMIRstOldRoleType_Type.__name__ = "Integer32"
_FsMIRstOldRoleType_Object = MibTableColumn
fsMIRstOldRoleType = _FsMIRstOldRoleType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 119, 2, 4, 1, 6),
    _FsMIRstOldRoleType_Type()
)
fsMIRstOldRoleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRstOldRoleType.setStatus("current")
_FsMIDot1wFutureRstTraps_ObjectIdentity = ObjectIdentity
fsMIDot1wFutureRstTraps = _FsMIDot1wFutureRstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 119, 3)
)
_FsMIRstTraps_ObjectIdentity = ObjectIdentity
fsMIRstTraps = _FsMIRstTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 119, 3, 0)
)

# Managed Objects groups


# Notification objects

fsMIRstGlobalErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 119, 3, 0, 1)
)
fsMIRstGlobalErrTrap.setObjects(
      *(("ARICENT-MIStdBRIDGE-MIB", "fsDot1dBaseBridgeAddress"),
        ("Aricent-MIRSTP-MIB", "fsMIRstGlobalErrTrapType"))
)
if mibBuilder.loadTexts:
    fsMIRstGlobalErrTrap.setStatus(
        "current"
    )

fsMIRstGenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 119, 3, 0, 2)
)
fsMIRstGenTrap.setObjects(
      *(("ARICENT-MIStdBRIDGE-MIB", "fsDot1dBaseBridgeAddress"),
        ("Aricent-MIRSTP-MIB", "fsMIRstContextName"),
        ("Aricent-MIRSTP-MIB", "fsMIRstGenTrapType"))
)
if mibBuilder.loadTexts:
    fsMIRstGenTrap.setStatus(
        "current"
    )

fsMIRstNewRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 119, 3, 0, 3)
)
fsMIRstNewRootTrap.setObjects(
      *(("ARICENT-MIStdBRIDGE-MIB", "fsDot1dBaseBridgeAddress"),
        ("Aricent-MIRSTP-MIB", "fsMIRstContextName"),
        ("Aricent-MIRSTP-MIB", "fsMIRstOldDesignatedRoot"),
        ("ARICENT-MIStdBRIDGE-MIB", "fsDot1dStpDesignatedRoot"))
)
if mibBuilder.loadTexts:
    fsMIRstNewRootTrap.setStatus(
        "current"
    )

fsMIRstTopologyChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 119, 3, 0, 4)
)
fsMIRstTopologyChgTrap.setObjects(
      *(("ARICENT-MIStdBRIDGE-MIB", "fsDot1dBaseBridgeAddress"),
        ("Aricent-MIRSTP-MIB", "fsMIRstContextName"))
)
if mibBuilder.loadTexts:
    fsMIRstTopologyChgTrap.setStatus(
        "current"
    )

fsMIRstProtocolMigrationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 119, 3, 0, 5)
)
fsMIRstProtocolMigrationTrap.setObjects(
      *(("ARICENT-MIStdBRIDGE-MIB", "fsDot1dBaseBridgeAddress"),
        ("Aricent-MIRSTP-MIB", "fsMIRstContextName"),
        ("ARICENT-MIStdRSTP-MIB", "fsDot1dStpVersion"),
        ("Aricent-MIRSTP-MIB", "fsMIRstPortMigrationType"))
)
if mibBuilder.loadTexts:
    fsMIRstProtocolMigrationTrap.setStatus(
        "current"
    )

fsMIRstInvalidBpduRxdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 119, 3, 0, 6)
)
fsMIRstInvalidBpduRxdTrap.setObjects(
      *(("ARICENT-MIStdBRIDGE-MIB", "fsDot1dBaseBridgeAddress"),
        ("Aricent-MIRSTP-MIB", "fsMIRstContextName"),
        ("Aricent-MIRSTP-MIB", "fsMIRstPktErrType"),
        ("Aricent-MIRSTP-MIB", "fsMIRstPktErrVal"))
)
if mibBuilder.loadTexts:
    fsMIRstInvalidBpduRxdTrap.setStatus(
        "current"
    )

fsMIRstNewPortRoleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 119, 3, 0, 7)
)
fsMIRstNewPortRoleTrap.setObjects(
      *(("ARICENT-MIStdBRIDGE-MIB", "fsDot1dBaseBridgeAddress"),
        ("Aricent-MIRSTP-MIB", "fsMIRstPortRoleType"),
        ("Aricent-MIRSTP-MIB", "fsMIRstOldRoleType"))
)
if mibBuilder.loadTexts:
    fsMIRstNewPortRoleTrap.setStatus(
        "current"
    )

fsMIRstHwFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 119, 3, 0, 8)
)
fsMIRstHwFailureTrap.setObjects(
      *(("ARICENT-MIStdBRIDGE-MIB", "fsDot1dBaseBridgeAddress"),
        ("Aricent-MIRSTP-MIB", "fsMIRstContextName"),
        ("ARICENT-MIStdBRIDGE-MIB", "fsDot1dStpPortState"))
)
if mibBuilder.loadTexts:
    fsMIRstHwFailureTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Aricent-MIRSTP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "Timeout": Timeout,
       "futureMIRstMIB": futureMIRstMIB,
       "fsMIDot1wFutureRst": fsMIDot1wFutureRst,
       "fsMIRstGlobalTrace": fsMIRstGlobalTrace,
       "fsMIRstGlobalDebug": fsMIRstGlobalDebug,
       "fsMIDot1wFutureRstTable": fsMIDot1wFutureRstTable,
       "fsMIDot1wFutureRstEntry": fsMIDot1wFutureRstEntry,
       "fsMIDot1wFutureRstContextId": fsMIDot1wFutureRstContextId,
       "fsMIRstSystemControl": fsMIRstSystemControl,
       "fsMIRstModuleStatus": fsMIRstModuleStatus,
       "fsMIRstTraceOption": fsMIRstTraceOption,
       "fsMIRstDebugOption": fsMIRstDebugOption,
       "fsMIRstRstpUpCount": fsMIRstRstpUpCount,
       "fsMIRstRstpDownCount": fsMIRstRstpDownCount,
       "fsMIRstBufferFailureCount": fsMIRstBufferFailureCount,
       "fsMIRstMemAllocFailureCount": fsMIRstMemAllocFailureCount,
       "fsMIRstNewRootIdCount": fsMIRstNewRootIdCount,
       "fsMIRstPortRoleSelSmState": fsMIRstPortRoleSelSmState,
       "fsMIRstOldDesignatedRoot": fsMIRstOldDesignatedRoot,
       "fsMIRstDynamicPathcostCalculation": fsMIRstDynamicPathcostCalculation,
       "fsMIRstContextName": fsMIRstContextName,
       "fsMIRstCalcPortPathCostOnSpeedChg": fsMIRstCalcPortPathCostOnSpeedChg,
       "fsMIRstClearBridgeStats": fsMIRstClearBridgeStats,
       "fsMIRstRcvdEvent": fsMIRstRcvdEvent,
       "fsMIRstRcvdEventSubType": fsMIRstRcvdEventSubType,
       "fsMIRstRcvdEventTimeStamp": fsMIRstRcvdEventTimeStamp,
       "fsMIRstRcvdPortStateChangeTimeStamp": fsMIRstRcvdPortStateChangeTimeStamp,
       "fsMIRstFlushInterval": fsMIRstFlushInterval,
       "fsMIRstFlushIndicationThreshold": fsMIRstFlushIndicationThreshold,
       "fsMIRstTotalFlushCount": fsMIRstTotalFlushCount,
       "fsMIRstFwdDelayAltPortRoleTrOptimization": fsMIRstFwdDelayAltPortRoleTrOptimization,
       "fsMIRstBpduGuard": fsMIRstBpduGuard,
       "fsMIRstStpPerfStatus": fsMIRstStpPerfStatus,
       "fsMIRstPortExtTable": fsMIRstPortExtTable,
       "fsMIRstPortExtEntry": fsMIRstPortExtEntry,
       "fsMIRstPort": fsMIRstPort,
       "fsMIRstPortRole": fsMIRstPortRole,
       "fsMIRstPortOperVersion": fsMIRstPortOperVersion,
       "fsMIRstPortInfoSmState": fsMIRstPortInfoSmState,
       "fsMIRstPortMigSmState": fsMIRstPortMigSmState,
       "fsMIRstPortRoleTransSmState": fsMIRstPortRoleTransSmState,
       "fsMIRstPortStateTransSmState": fsMIRstPortStateTransSmState,
       "fsMIRstPortTopoChSmState": fsMIRstPortTopoChSmState,
       "fsMIRstPortTxSmState": fsMIRstPortTxSmState,
       "fsMIRstPortRxRstBpduCount": fsMIRstPortRxRstBpduCount,
       "fsMIRstPortRxConfigBpduCount": fsMIRstPortRxConfigBpduCount,
       "fsMIRstPortRxTcnBpduCount": fsMIRstPortRxTcnBpduCount,
       "fsMIRstPortTxRstBpduCount": fsMIRstPortTxRstBpduCount,
       "fsMIRstPortTxConfigBpduCount": fsMIRstPortTxConfigBpduCount,
       "fsMIRstPortTxTcnBpduCount": fsMIRstPortTxTcnBpduCount,
       "fsMIRstPortInvalidRstBpduRxCount": fsMIRstPortInvalidRstBpduRxCount,
       "fsMIRstPortInvalidConfigBpduRxCount": fsMIRstPortInvalidConfigBpduRxCount,
       "fsMIRstPortInvalidTcnBpduRxCount": fsMIRstPortInvalidTcnBpduRxCount,
       "fsMIRstPortProtocolMigrationCount": fsMIRstPortProtocolMigrationCount,
       "fsMIRstPortEffectivePortState": fsMIRstPortEffectivePortState,
       "fsMIRstPortAutoEdge": fsMIRstPortAutoEdge,
       "fsMIRstPortRestrictedRole": fsMIRstPortRestrictedRole,
       "fsMIRstPortRestrictedTCN": fsMIRstPortRestrictedTCN,
       "fsMIRstPortEnableBPDURx": fsMIRstPortEnableBPDURx,
       "fsMIRstPortEnableBPDUTx": fsMIRstPortEnableBPDUTx,
       "fsMIRstPortPseudoRootId": fsMIRstPortPseudoRootId,
       "fsMIRstPortIsL2Gp": fsMIRstPortIsL2Gp,
       "fsMIRstPortLoopGuard": fsMIRstPortLoopGuard,
       "fsMIRstPortClearStats": fsMIRstPortClearStats,
       "fsMIRstPortRcvdEvent": fsMIRstPortRcvdEvent,
       "fsMIRstPortRcvdEventSubType": fsMIRstPortRcvdEventSubType,
       "fsMIRstPortRcvdEventTimeStamp": fsMIRstPortRcvdEventTimeStamp,
       "fsMIRstPortStateChangeTimeStamp": fsMIRstPortStateChangeTimeStamp,
       "fsMIRstPortRowStatus": fsMIRstPortRowStatus,
       "fsMIRstLoopInconsistentState": fsMIRstLoopInconsistentState,
       "fsMIRstPortBpduGuard": fsMIRstPortBpduGuard,
       "fsMIRstPortRootGuard": fsMIRstPortRootGuard,
       "fsMIRstRootInconsistentState": fsMIRstRootInconsistentState,
       "fsMIRstPortErrorRecovery": fsMIRstPortErrorRecovery,
       "fsMIRstPortStpModeDot1wEnabled": fsMIRstPortStpModeDot1wEnabled,
       "fsMIRstPortBpduInconsistentState": fsMIRstPortBpduInconsistentState,
       "fsMIRstPortBpduGuardAction": fsMIRstPortBpduGuardAction,
       "fsMIDot1wFsRstTrapsControl": fsMIDot1wFsRstTrapsControl,
       "fsMIRstSetGlobalTraps": fsMIRstSetGlobalTraps,
       "fsMIRstGlobalErrTrapType": fsMIRstGlobalErrTrapType,
       "fsMIDot1wFsRstTrapsControlTable": fsMIDot1wFsRstTrapsControlTable,
       "fsMIDot1wFsRstTrapsControlEntry": fsMIDot1wFsRstTrapsControlEntry,
       "fsMIRstSetTraps": fsMIRstSetTraps,
       "fsMIRstGenTrapType": fsMIRstGenTrapType,
       "fsMIRstPortTrapNotificationTable": fsMIRstPortTrapNotificationTable,
       "fsMIRstPortTrapNotificationEntry": fsMIRstPortTrapNotificationEntry,
       "fsMIRstPortTrapIndex": fsMIRstPortTrapIndex,
       "fsMIRstPortMigrationType": fsMIRstPortMigrationType,
       "fsMIRstPktErrType": fsMIRstPktErrType,
       "fsMIRstPktErrVal": fsMIRstPktErrVal,
       "fsMIRstPortRoleType": fsMIRstPortRoleType,
       "fsMIRstOldRoleType": fsMIRstOldRoleType,
       "fsMIDot1wFutureRstTraps": fsMIDot1wFutureRstTraps,
       "fsMIRstTraps": fsMIRstTraps,
       "fsMIRstGlobalErrTrap": fsMIRstGlobalErrTrap,
       "fsMIRstGenTrap": fsMIRstGenTrap,
       "fsMIRstNewRootTrap": fsMIRstNewRootTrap,
       "fsMIRstTopologyChgTrap": fsMIRstTopologyChgTrap,
       "fsMIRstProtocolMigrationTrap": fsMIRstProtocolMigrationTrap,
       "fsMIRstInvalidBpduRxdTrap": fsMIRstInvalidBpduRxdTrap,
       "fsMIRstNewPortRoleTrap": fsMIRstNewPortRoleTrap,
       "fsMIRstHwFailureTrap": fsMIRstHwFailureTrap}
)
