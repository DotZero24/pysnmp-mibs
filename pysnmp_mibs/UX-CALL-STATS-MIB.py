# SNMP MIB module (UX-CALL-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/sonus/UX-CALL-STATS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:43:51 2025
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

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ux = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 177, 15)
)
if mibBuilder.loadTexts:
    ux.setRevisions(
        ("2009-11-04 17:05",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Net_ObjectIdentity = ObjectIdentity
net = _Net_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 177)
)
_UxObjects_ObjectIdentity = ObjectIdentity
uxObjects = _UxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 177, 15, 1)
)
_IpSystem_ObjectIdentity = ObjectIdentity
ipSystem = _IpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 4)
)
_SysVersion_Type = DisplayString
_SysVersion_Object = MibScalar
sysVersion = _SysVersion_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 4, 1),
    _SysVersion_Type()
)
sysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVersion.setStatus("current")
_SysBuildNumber_Type = DisplayString
_SysBuildNumber_Object = MibScalar
sysBuildNumber = _SysBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 4, 2),
    _SysBuildNumber_Type()
)
sysBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBuildNumber.setStatus("current")
_IpTelephony_ObjectIdentity = ObjectIdentity
ipTelephony = _IpTelephony_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5)
)
_CallStatistics_ObjectIdentity = ObjectIdentity
callStatistics = _CallStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1)
)
_UxPortTable_Object = MibTable
uxPortTable = _UxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    uxPortTable.setStatus("current")
_UxPortEntry_Object = MibTableRow
uxPortEntry = _UxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1)
)
uxPortEntry.setIndexNames(
    (0, "UX-CALL-STATS-MIB", "uxPTIndex"),
)
if mibBuilder.loadTexts:
    uxPortEntry.setStatus("current")
_UxPTIndex_Type = Unsigned32
_UxPTIndex_Object = MibTableColumn
uxPTIndex = _UxPTIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 1),
    _UxPTIndex_Type()
)
uxPTIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxPTIndex.setStatus("current")
_UxPTShelf_Type = Unsigned32
_UxPTShelf_Object = MibTableColumn
uxPTShelf = _UxPTShelf_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 2),
    _UxPTShelf_Type()
)
uxPTShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTShelf.setStatus("current")
_UxPTSlot_Type = Unsigned32
_UxPTSlot_Object = MibTableColumn
uxPTSlot = _UxPTSlot_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 3),
    _UxPTSlot_Type()
)
uxPTSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTSlot.setStatus("current")
_UxPTPort_Type = Unsigned32
_UxPTPort_Object = MibTableColumn
uxPTPort = _UxPTPort_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 4),
    _UxPTPort_Type()
)
uxPTPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTPort.setStatus("current")
_UxPTCurrentCalls_Type = Gauge32
_UxPTCurrentCalls_Object = MibTableColumn
uxPTCurrentCalls = _UxPTCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 5),
    _UxPTCurrentCalls_Type()
)
uxPTCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTCurrentCalls.setStatus("current")
_UxPTTotalCalls_Type = Counter32
_UxPTTotalCalls_Object = MibTableColumn
uxPTTotalCalls = _UxPTTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 6),
    _UxPTTotalCalls_Type()
)
uxPTTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTTotalCalls.setStatus("current")
_UxPTConnectedCalls_Type = Counter32
_UxPTConnectedCalls_Object = MibTableColumn
uxPTConnectedCalls = _UxPTConnectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 7),
    _UxPTConnectedCalls_Type()
)
uxPTConnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTConnectedCalls.setStatus("current")
_UxPTRefusedCalls_Type = Counter32
_UxPTRefusedCalls_Object = MibTableColumn
uxPTRefusedCalls = _UxPTRefusedCalls_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 8),
    _UxPTRefusedCalls_Type()
)
uxPTRefusedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTRefusedCalls.setStatus("current")
_UxPTErroredCalls_Type = Counter32
_UxPTErroredCalls_Object = MibTableColumn
uxPTErroredCalls = _UxPTErroredCalls_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 9),
    _UxPTErroredCalls_Type()
)
uxPTErroredCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTErroredCalls.setStatus("current")
_UxPTEgressCallAttempts_Type = Counter32
_UxPTEgressCallAttempts_Object = MibTableColumn
uxPTEgressCallAttempts = _UxPTEgressCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 10),
    _UxPTEgressCallAttempts_Type()
)
uxPTEgressCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTEgressCallAttempts.setStatus("current")
_UxPTEgressCallsAccepted_Type = Counter32
_UxPTEgressCallsAccepted_Object = MibTableColumn
uxPTEgressCallsAccepted = _UxPTEgressCallsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 11),
    _UxPTEgressCallsAccepted_Type()
)
uxPTEgressCallsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTEgressCallsAccepted.setStatus("current")
_UxPTEgressCallsCompleted_Type = Counter32
_UxPTEgressCallsCompleted_Object = MibTableColumn
uxPTEgressCallsCompleted = _UxPTEgressCallsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 12),
    _UxPTEgressCallsCompleted_Type()
)
uxPTEgressCallsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTEgressCallsCompleted.setStatus("current")
_UxPTEgressCallsRejected_Type = Counter32
_UxPTEgressCallsRejected_Object = MibTableColumn
uxPTEgressCallsRejected = _UxPTEgressCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 13),
    _UxPTEgressCallsRejected_Type()
)
uxPTEgressCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTEgressCallsRejected.setStatus("current")
_UxPTIngressCallAttempts_Type = Counter32
_UxPTIngressCallAttempts_Object = MibTableColumn
uxPTIngressCallAttempts = _UxPTIngressCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 14),
    _UxPTIngressCallAttempts_Type()
)
uxPTIngressCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTIngressCallAttempts.setStatus("current")
_UxPTIngressCallsAccepted_Type = Counter32
_UxPTIngressCallsAccepted_Object = MibTableColumn
uxPTIngressCallsAccepted = _UxPTIngressCallsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 15),
    _UxPTIngressCallsAccepted_Type()
)
uxPTIngressCallsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTIngressCallsAccepted.setStatus("current")
_UxPTIngressCallsCompleted_Type = Counter32
_UxPTIngressCallsCompleted_Object = MibTableColumn
uxPTIngressCallsCompleted = _UxPTIngressCallsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 16),
    _UxPTIngressCallsCompleted_Type()
)
uxPTIngressCallsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTIngressCallsCompleted.setStatus("current")
_UxPTIngressCallsRejected_Type = Counter32
_UxPTIngressCallsRejected_Object = MibTableColumn
uxPTIngressCallsRejected = _UxPTIngressCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 17),
    _UxPTIngressCallsRejected_Type()
)
uxPTIngressCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTIngressCallsRejected.setStatus("current")
_UxPTBlockedCalls_Type = Counter32
_UxPTBlockedCalls_Object = MibTableColumn
uxPTBlockedCalls = _UxPTBlockedCalls_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 18),
    _UxPTBlockedCalls_Type()
)
uxPTBlockedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTBlockedCalls.setStatus("current")
_UxPTEgressBlockedCalls_Type = Counter32
_UxPTEgressBlockedCalls_Object = MibTableColumn
uxPTEgressBlockedCalls = _UxPTEgressBlockedCalls_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 19),
    _UxPTEgressBlockedCalls_Type()
)
uxPTEgressBlockedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTEgressBlockedCalls.setStatus("current")
_UxPTIngressBlockedCalls_Type = Counter32
_UxPTIngressBlockedCalls_Object = MibTableColumn
uxPTIngressBlockedCalls = _UxPTIngressBlockedCalls_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 20),
    _UxPTIngressBlockedCalls_Type()
)
uxPTIngressBlockedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTIngressBlockedCalls.setStatus("current")
_UxPTEgressCurrentCalls_Type = Counter32
_UxPTEgressCurrentCalls_Object = MibTableColumn
uxPTEgressCurrentCalls = _UxPTEgressCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 21),
    _UxPTEgressCurrentCalls_Type()
)
uxPTEgressCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTEgressCurrentCalls.setStatus("current")
_UxPTIngressCurrentCalls_Type = Counter32
_UxPTIngressCurrentCalls_Object = MibTableColumn
uxPTIngressCurrentCalls = _UxPTIngressCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 22),
    _UxPTIngressCurrentCalls_Type()
)
uxPTIngressCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTIngressCurrentCalls.setStatus("current")
_UxPTBHCARate_Type = Counter32
_UxPTBHCARate_Object = MibTableColumn
uxPTBHCARate = _UxPTBHCARate_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 23),
    _UxPTBHCARate_Type()
)
uxPTBHCARate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTBHCARate.setStatus("current")
_UxPTBHCCRate_Type = Counter32
_UxPTBHCCRate_Object = MibTableColumn
uxPTBHCCRate = _UxPTBHCCRate_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 1, 2, 1, 24),
    _UxPTBHCCRate_Type()
)
uxPTBHCCRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPTBHCCRate.setStatus("current")
_UxCallRtTablesTable_Object = MibTable
uxCallRtTablesTable = _UxCallRtTablesTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 2)
)
if mibBuilder.loadTexts:
    uxCallRtTablesTable.setStatus("current")
_UxCallRtTablesEntry_Object = MibTableRow
uxCallRtTablesEntry = _UxCallRtTablesEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 2, 1)
)
uxCallRtTablesEntry.setIndexNames(
    (0, "UX-CALL-STATS-MIB", "uxCallRtTablesTableIndex"),
)
if mibBuilder.loadTexts:
    uxCallRtTablesEntry.setStatus("current")


class _UxCallRtTablesTableIndex_Type(Integer32):
    """Custom type uxCallRtTablesTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxCallRtTablesTableIndex_Type.__name__ = "Integer32"
_UxCallRtTablesTableIndex_Object = MibTableColumn
uxCallRtTablesTableIndex = _UxCallRtTablesTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 2, 1, 1),
    _UxCallRtTablesTableIndex_Type()
)
uxCallRtTablesTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCallRtTablesTableIndex.setStatus("current")
_UxDesc_Type = DisplayString
_UxDesc_Object = MibTableColumn
uxDesc = _UxDesc_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 2, 1, 2),
    _UxDesc_Type()
)
uxDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxDesc.setStatus("current")


class _UxCallRtSequence_Type(DisplayString):
    """Custom type uxCallRtSequence based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30000),
    )


_UxCallRtSequence_Type.__name__ = "DisplayString"
_UxCallRtSequence_Object = MibTableColumn
uxCallRtSequence = _UxCallRtSequence_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 2, 1, 3),
    _UxCallRtSequence_Type()
)
uxCallRtSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCallRtSequence.setStatus("current")
_UxCallRtTable_Object = MibTable
uxCallRtTable = _UxCallRtTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 3)
)
if mibBuilder.loadTexts:
    uxCallRtTable.setStatus("current")
_UxCallRtEntry_Object = MibTableRow
uxCallRtEntry = _UxCallRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 3, 1)
)
uxCallRtEntry.setIndexNames(
    (0, "UX-CALL-STATS-MIB", "uxCallRtTablesIndex"),
    (0, "UX-CALL-STATS-MIB", "uxCallRtIndex"),
)
if mibBuilder.loadTexts:
    uxCallRtEntry.setStatus("current")


class _UxCallRtTablesIndex_Type(Integer32):
    """Custom type uxCallRtTablesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxCallRtTablesIndex_Type.__name__ = "Integer32"
_UxCallRtTablesIndex_Object = MibTableColumn
uxCallRtTablesIndex = _UxCallRtTablesIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 3, 1, 1),
    _UxCallRtTablesIndex_Type()
)
uxCallRtTablesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCallRtTablesIndex.setStatus("current")


class _UxCallRtIndex_Type(Integer32):
    """Custom type uxCallRtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxCallRtIndex_Type.__name__ = "Integer32"
_UxCallRtIndex_Object = MibTableColumn
uxCallRtIndex = _UxCallRtIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 3, 1, 2),
    _UxCallRtIndex_Type()
)
uxCallRtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCallRtIndex.setStatus("current")
_UxDescription_Type = DisplayString
_UxDescription_Object = MibTableColumn
uxDescription = _UxDescription_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 3, 1, 3),
    _UxDescription_Type()
)
uxDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxDescription.setStatus("current")


class _UxAdminState_Type(Integer32):
    """Custom type uxAdminState based on Integer32"""
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


_UxAdminState_Type.__name__ = "Integer32"
_UxAdminState_Object = MibTableColumn
uxAdminState = _UxAdminState_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 3, 1, 4),
    _UxAdminState_Type()
)
uxAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAdminState.setStatus("current")
_UxRoutePriority_Type = Integer32
_UxRoutePriority_Object = MibTableColumn
uxRoutePriority = _UxRoutePriority_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 3, 1, 5),
    _UxRoutePriority_Type()
)
uxRoutePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxRoutePriority.setStatus("current")
_UxSignalingGroupList_Type = DisplayString
_UxSignalingGroupList_Object = MibTableColumn
uxSignalingGroupList = _UxSignalingGroupList_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 3, 1, 6),
    _UxSignalingGroupList_Type()
)
uxSignalingGroupList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSignalingGroupList.setStatus("current")
_UxQualityMetricCalls_Type = Integer32
_UxQualityMetricCalls_Object = MibTableColumn
uxQualityMetricCalls = _UxQualityMetricCalls_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 3, 1, 7),
    _UxQualityMetricCalls_Type()
)
uxQualityMetricCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxQualityMetricCalls.setStatus("current")
_UxQualityMetricTime_Type = Integer32
_UxQualityMetricTime_Object = MibTableColumn
uxQualityMetricTime = _UxQualityMetricTime_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 3, 1, 8),
    _UxQualityMetricTime_Type()
)
uxQualityMetricTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxQualityMetricTime.setStatus("current")
_UxQualityMinASRThreshold_Type = Integer32
_UxQualityMinASRThreshold_Object = MibTableColumn
uxQualityMinASRThreshold = _UxQualityMinASRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 3, 1, 9),
    _UxQualityMinASRThreshold_Type()
)
uxQualityMinASRThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxQualityMinASRThreshold.setStatus("current")
_UxQualityMaxRoundTripDelayThreshold_Type = Integer32
_UxQualityMaxRoundTripDelayThreshold_Object = MibTableColumn
uxQualityMaxRoundTripDelayThreshold = _UxQualityMaxRoundTripDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 3, 1, 10),
    _UxQualityMaxRoundTripDelayThreshold_Type()
)
uxQualityMaxRoundTripDelayThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxQualityMaxRoundTripDelayThreshold.setStatus("current")
_UxQualityMaxJitterThreshold_Type = Integer32
_UxQualityMaxJitterThreshold_Object = MibTableColumn
uxQualityMaxJitterThreshold = _UxQualityMaxJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 3, 1, 11),
    _UxQualityMaxJitterThreshold_Type()
)
uxQualityMaxJitterThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxQualityMaxJitterThreshold.setStatus("current")
_UxQualityMinMOSThreshold_Type = Integer32
_UxQualityMinMOSThreshold_Object = MibTableColumn
uxQualityMinMOSThreshold = _UxQualityMinMOSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 3, 1, 12),
    _UxQualityMinMOSThreshold_Type()
)
uxQualityMinMOSThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxQualityMinMOSThreshold.setStatus("current")
_UxSGTable_Object = MibTable
uxSGTable = _UxSGTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 4)
)
if mibBuilder.loadTexts:
    uxSGTable.setStatus("current")
_UxSGEntry_Object = MibTableRow
uxSGEntry = _UxSGEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 4, 1)
)
uxSGEntry.setIndexNames(
    (0, "UX-CALL-STATS-MIB", "uxSGEntryIndex"),
)
if mibBuilder.loadTexts:
    uxSGEntry.setStatus("current")


class _UxSGEntryIndex_Type(Integer32):
    """Custom type uxSGEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxSGEntryIndex_Type.__name__ = "Integer32"
_UxSGEntryIndex_Object = MibTableColumn
uxSGEntryIndex = _UxSGEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 4, 1, 1),
    _UxSGEntryIndex_Type()
)
uxSGEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSGEntryIndex.setStatus("current")
_UxSGDescription_Type = DisplayString
_UxSGDescription_Object = MibTableColumn
uxSGDescription = _UxSGDescription_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 4, 1, 2),
    _UxSGDescription_Type()
)
uxSGDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSGDescription.setStatus("current")


class _UxSGType_Type(Integer32):
    """Custom type uxSGType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sip", 1),
          ("isdn", 2),
          ("cas", 3))
    )


_UxSGType_Type.__name__ = "Integer32"
_UxSGType_Object = MibTableColumn
uxSGType = _UxSGType_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 4, 1, 3),
    _UxSGType_Type()
)
uxSGType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSGType.setStatus("current")


class _UxSGAdminState_Type(Integer32):
    """Custom type uxSGAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("drain", 2))
    )


_UxSGAdminState_Type.__name__ = "Integer32"
_UxSGAdminState_Object = MibTableColumn
uxSGAdminState = _UxSGAdminState_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 4, 1, 4),
    _UxSGAdminState_Type()
)
uxSGAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSGAdminState.setStatus("current")


class _UxSGServiceState_Type(Integer32):
    """Custom type uxSGServiceState based on Integer32"""
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


_UxSGServiceState_Type.__name__ = "Integer32"
_UxSGServiceState_Object = MibTableColumn
uxSGServiceState = _UxSGServiceState_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 4, 1, 5),
    _UxSGServiceState_Type()
)
uxSGServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSGServiceState.setStatus("current")
_UxSipServerTable_Object = MibTable
uxSipServerTable = _UxSipServerTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 5)
)
if mibBuilder.loadTexts:
    uxSipServerTable.setStatus("current")
_UxSipServerEntry_Object = MibTableRow
uxSipServerEntry = _UxSipServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 5, 1)
)
uxSipServerEntry.setIndexNames(
    (0, "UX-CALL-STATS-MIB", "uxSGIndex"),
    (0, "UX-CALL-STATS-MIB", "uxSipServerIndex"),
)
if mibBuilder.loadTexts:
    uxSipServerEntry.setStatus("current")


class _UxSGIndex_Type(Integer32):
    """Custom type uxSGIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxSGIndex_Type.__name__ = "Integer32"
_UxSGIndex_Object = MibTableColumn
uxSGIndex = _UxSGIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 5, 1, 1),
    _UxSGIndex_Type()
)
uxSGIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSGIndex.setStatus("current")


class _UxSipServerIndex_Type(Integer32):
    """Custom type uxSipServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxSipServerIndex_Type.__name__ = "Integer32"
_UxSipServerIndex_Object = MibTableColumn
uxSipServerIndex = _UxSipServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 5, 1, 2),
    _UxSipServerIndex_Type()
)
uxSipServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSipServerIndex.setStatus("current")
_UxSipSvrPriority_Type = Integer32
_UxSipSvrPriority_Object = MibTableColumn
uxSipSvrPriority = _UxSipSvrPriority_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 5, 1, 3),
    _UxSipSvrPriority_Type()
)
uxSipSvrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSipSvrPriority.setStatus("current")
_UxSipSvrHost_Type = DisplayString
_UxSipSvrHost_Object = MibTableColumn
uxSipSvrHost = _UxSipSvrHost_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 5, 1, 4),
    _UxSipSvrHost_Type()
)
uxSipSvrHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSipSvrHost.setStatus("current")
_UxSipSvrPort_Type = Integer32
_UxSipSvrPort_Object = MibTableColumn
uxSipSvrPort = _UxSipSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 5, 1, 5),
    _UxSipSvrPort_Type()
)
uxSipSvrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSipSvrPort.setStatus("current")


class _UxSipSvrTransProtocol_Type(Integer32):
    """Custom type uxSipSvrTransProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("udp", 1),
          ("tcp", 2),
          ("tls", 4))
    )


_UxSipSvrTransProtocol_Type.__name__ = "Integer32"
_UxSipSvrTransProtocol_Object = MibTableColumn
uxSipSvrTransProtocol = _UxSipSvrTransProtocol_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 5, 1, 6),
    _UxSipSvrTransProtocol_Type()
)
uxSipSvrTransProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSipSvrTransProtocol.setStatus("current")
_UxChannelStatusTable_Object = MibTable
uxChannelStatusTable = _UxChannelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 6)
)
if mibBuilder.loadTexts:
    uxChannelStatusTable.setStatus("current")
_UxChannelStatusEntry_Object = MibTableRow
uxChannelStatusEntry = _UxChannelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 6, 1)
)
uxChannelStatusEntry.setIndexNames(
    (0, "UX-CALL-STATS-MIB", "uxChShelfNumber"),
    (0, "UX-CALL-STATS-MIB", "uxChSlotNumber"),
    (0, "UX-CALL-STATS-MIB", "uxChPortNumber"),
    (0, "UX-CALL-STATS-MIB", "uxChChannelNumber"),
)
if mibBuilder.loadTexts:
    uxChannelStatusEntry.setStatus("current")
_UxChShelfNumber_Type = Unsigned32
_UxChShelfNumber_Object = MibTableColumn
uxChShelfNumber = _UxChShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 6, 1, 1),
    _UxChShelfNumber_Type()
)
uxChShelfNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxChShelfNumber.setStatus("current")
_UxChSlotNumber_Type = Unsigned32
_UxChSlotNumber_Object = MibTableColumn
uxChSlotNumber = _UxChSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 6, 1, 2),
    _UxChSlotNumber_Type()
)
uxChSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxChSlotNumber.setStatus("current")
_UxChPortNumber_Type = Unsigned32
_UxChPortNumber_Object = MibTableColumn
uxChPortNumber = _UxChPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 6, 1, 3),
    _UxChPortNumber_Type()
)
uxChPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxChPortNumber.setStatus("current")
_UxChChannelNumber_Type = Unsigned32
_UxChChannelNumber_Object = MibTableColumn
uxChChannelNumber = _UxChChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 6, 1, 4),
    _UxChChannelNumber_Type()
)
uxChChannelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uxChChannelNumber.setStatus("current")


class _UxChAdminState_Type(Integer32):
    """Custom type uxChAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_UxChAdminState_Type.__name__ = "Integer32"
_UxChAdminState_Object = MibTableColumn
uxChAdminState = _UxChAdminState_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 6, 1, 5),
    _UxChAdminState_Type()
)
uxChAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxChAdminState.setStatus("current")


class _UxChOperState_Type(Integer32):
    """Custom type uxChOperState based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("outOfService", 0),
          ("idle", 1),
          ("pending", 2),
          ("waitingForRoute", 3),
          ("actionList", 4),
          ("waitingForDigits", 5),
          ("remoteSetUp", 6),
          ("peerSetUp", 7),
          ("alerting", 8),
          ("inBandInfo", 9),
          ("connected", 10),
          ("toneGeneration", 11),
          ("releasing", 12),
          ("aborting", 13),
          ("resetting", 14),
          ("up", 15),
          ("down", 16))
    )


_UxChOperState_Type.__name__ = "Integer32"
_UxChOperState_Object = MibTableColumn
uxChOperState = _UxChOperState_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 6, 1, 6),
    _UxChOperState_Type()
)
uxChOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxChOperState.setStatus("current")
_UxChInUseSeconds_Type = Counter32
_UxChInUseSeconds_Object = MibTableColumn
uxChInUseSeconds = _UxChInUseSeconds_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 6, 1, 7),
    _UxChInUseSeconds_Type()
)
uxChInUseSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxChInUseSeconds.setStatus("current")
_UxSGStatsCurrentTable_Object = MibTable
uxSGStatsCurrentTable = _UxSGStatsCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 7)
)
if mibBuilder.loadTexts:
    uxSGStatsCurrentTable.setStatus("current")
_UxSGStatsCurrentEntry_Object = MibTableRow
uxSGStatsCurrentEntry = _UxSGStatsCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 7, 1)
)
uxSGStatsCurrentEntry.setIndexNames(
    (0, "UX-CALL-STATS-MIB", "uxSGCurrentIndex"),
)
if mibBuilder.loadTexts:
    uxSGStatsCurrentEntry.setStatus("current")


class _UxSGCurrentIndex_Type(Integer32):
    """Custom type uxSGCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxSGCurrentIndex_Type.__name__ = "Integer32"
_UxSGCurrentIndex_Object = MibTableColumn
uxSGCurrentIndex = _UxSGCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 7, 1, 1),
    _UxSGCurrentIndex_Type()
)
uxSGCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSGCurrentIndex.setStatus("current")
_UxSGCurrentPeakChannelUsage_Type = PerfCurrentCount
_UxSGCurrentPeakChannelUsage_Object = MibTableColumn
uxSGCurrentPeakChannelUsage = _UxSGCurrentPeakChannelUsage_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 7, 1, 2),
    _UxSGCurrentPeakChannelUsage_Type()
)
uxSGCurrentPeakChannelUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSGCurrentPeakChannelUsage.setStatus("current")
_UxSGCurrentCompletedCalls_Type = PerfCurrentCount
_UxSGCurrentCompletedCalls_Object = MibTableColumn
uxSGCurrentCompletedCalls = _UxSGCurrentCompletedCalls_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 7, 1, 3),
    _UxSGCurrentCompletedCalls_Type()
)
uxSGCurrentCompletedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSGCurrentCompletedCalls.setStatus("current")
_UxSGCurrentIncompleteCalls_Type = PerfCurrentCount
_UxSGCurrentIncompleteCalls_Object = MibTableColumn
uxSGCurrentIncompleteCalls = _UxSGCurrentIncompleteCalls_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 7, 1, 4),
    _UxSGCurrentIncompleteCalls_Type()
)
uxSGCurrentIncompleteCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSGCurrentIncompleteCalls.setStatus("current")
_UxSGStatsIntervalTable_Object = MibTable
uxSGStatsIntervalTable = _UxSGStatsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 8)
)
if mibBuilder.loadTexts:
    uxSGStatsIntervalTable.setStatus("current")
_UxSGStatsIntervalEntry_Object = MibTableRow
uxSGStatsIntervalEntry = _UxSGStatsIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 8, 1)
)
uxSGStatsIntervalEntry.setIndexNames(
    (0, "UX-CALL-STATS-MIB", "uxSGIntervalIndex"),
    (0, "UX-CALL-STATS-MIB", "uxSGIntervalNumber"),
)
if mibBuilder.loadTexts:
    uxSGStatsIntervalEntry.setStatus("current")


class _UxSGIntervalIndex_Type(Integer32):
    """Custom type uxSGIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxSGIntervalIndex_Type.__name__ = "Integer32"
_UxSGIntervalIndex_Object = MibTableColumn
uxSGIntervalIndex = _UxSGIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 8, 1, 1),
    _UxSGIntervalIndex_Type()
)
uxSGIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSGIntervalIndex.setStatus("current")


class _UxSGIntervalNumber_Type(Integer32):
    """Custom type uxSGIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_UxSGIntervalNumber_Type.__name__ = "Integer32"
_UxSGIntervalNumber_Object = MibTableColumn
uxSGIntervalNumber = _UxSGIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 8, 1, 2),
    _UxSGIntervalNumber_Type()
)
uxSGIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSGIntervalNumber.setStatus("current")
_UxSGIntervalPeakChannelUsage_Type = PerfIntervalCount
_UxSGIntervalPeakChannelUsage_Object = MibTableColumn
uxSGIntervalPeakChannelUsage = _UxSGIntervalPeakChannelUsage_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 8, 1, 3),
    _UxSGIntervalPeakChannelUsage_Type()
)
uxSGIntervalPeakChannelUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSGIntervalPeakChannelUsage.setStatus("current")
_UxSGIntervalCompletedCalls_Type = PerfIntervalCount
_UxSGIntervalCompletedCalls_Object = MibTableColumn
uxSGIntervalCompletedCalls = _UxSGIntervalCompletedCalls_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 8, 1, 4),
    _UxSGIntervalCompletedCalls_Type()
)
uxSGIntervalCompletedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSGIntervalCompletedCalls.setStatus("current")
_UxSGIntervalIncompleteCalls_Type = PerfIntervalCount
_UxSGIntervalIncompleteCalls_Object = MibTableColumn
uxSGIntervalIncompleteCalls = _UxSGIntervalIncompleteCalls_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 8, 1, 5),
    _UxSGIntervalIncompleteCalls_Type()
)
uxSGIntervalIncompleteCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSGIntervalIncompleteCalls.setStatus("current")
_UxCallRtStatsCurrentTable_Object = MibTable
uxCallRtStatsCurrentTable = _UxCallRtStatsCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 10)
)
if mibBuilder.loadTexts:
    uxCallRtStatsCurrentTable.setStatus("current")
_UxCallRtStatsCurrentEntry_Object = MibTableRow
uxCallRtStatsCurrentEntry = _UxCallRtStatsCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 10, 1)
)
uxCallRtStatsCurrentEntry.setIndexNames(
    (0, "UX-CALL-STATS-MIB", "uxCallRtCurrentTablesIndex"),
    (0, "UX-CALL-STATS-MIB", "uxCallRtCurrentEntryIndex"),
)
if mibBuilder.loadTexts:
    uxCallRtStatsCurrentEntry.setStatus("current")


class _UxCallRtCurrentTablesIndex_Type(Integer32):
    """Custom type uxCallRtCurrentTablesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxCallRtCurrentTablesIndex_Type.__name__ = "Integer32"
_UxCallRtCurrentTablesIndex_Object = MibTableColumn
uxCallRtCurrentTablesIndex = _UxCallRtCurrentTablesIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 10, 1, 1),
    _UxCallRtCurrentTablesIndex_Type()
)
uxCallRtCurrentTablesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCallRtCurrentTablesIndex.setStatus("current")


class _UxCallRtCurrentEntryIndex_Type(Integer32):
    """Custom type uxCallRtCurrentEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxCallRtCurrentEntryIndex_Type.__name__ = "Integer32"
_UxCallRtCurrentEntryIndex_Object = MibTableColumn
uxCallRtCurrentEntryIndex = _UxCallRtCurrentEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 10, 1, 2),
    _UxCallRtCurrentEntryIndex_Type()
)
uxCallRtCurrentEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCallRtCurrentEntryIndex.setStatus("current")
_UxCallRtCurrentRuleUsage_Type = PerfCurrentCount
_UxCallRtCurrentRuleUsage_Object = MibTableColumn
uxCallRtCurrentRuleUsage = _UxCallRtCurrentRuleUsage_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 10, 1, 3),
    _UxCallRtCurrentRuleUsage_Type()
)
uxCallRtCurrentRuleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCallRtCurrentRuleUsage.setStatus("current")
_UxCallRtStatsIntervalTable_Object = MibTable
uxCallRtStatsIntervalTable = _UxCallRtStatsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 11)
)
if mibBuilder.loadTexts:
    uxCallRtStatsIntervalTable.setStatus("current")
_UxCallRtStatsIntervalEntry_Object = MibTableRow
uxCallRtStatsIntervalEntry = _UxCallRtStatsIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 11, 1)
)
uxCallRtStatsIntervalEntry.setIndexNames(
    (0, "UX-CALL-STATS-MIB", "uxCallRtIntervalTablesIndex"),
    (0, "UX-CALL-STATS-MIB", "uxCallRtIntervalEntryIndex"),
    (0, "UX-CALL-STATS-MIB", "uxCallRtIntervalNumber"),
)
if mibBuilder.loadTexts:
    uxCallRtStatsIntervalEntry.setStatus("current")


class _UxCallRtIntervalTablesIndex_Type(Integer32):
    """Custom type uxCallRtIntervalTablesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxCallRtIntervalTablesIndex_Type.__name__ = "Integer32"
_UxCallRtIntervalTablesIndex_Object = MibTableColumn
uxCallRtIntervalTablesIndex = _UxCallRtIntervalTablesIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 11, 1, 1),
    _UxCallRtIntervalTablesIndex_Type()
)
uxCallRtIntervalTablesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCallRtIntervalTablesIndex.setStatus("current")


class _UxCallRtIntervalEntryIndex_Type(Integer32):
    """Custom type uxCallRtIntervalEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxCallRtIntervalEntryIndex_Type.__name__ = "Integer32"
_UxCallRtIntervalEntryIndex_Object = MibTableColumn
uxCallRtIntervalEntryIndex = _UxCallRtIntervalEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 11, 1, 2),
    _UxCallRtIntervalEntryIndex_Type()
)
uxCallRtIntervalEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCallRtIntervalEntryIndex.setStatus("current")


class _UxCallRtIntervalNumber_Type(Integer32):
    """Custom type uxCallRtIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_UxCallRtIntervalNumber_Type.__name__ = "Integer32"
_UxCallRtIntervalNumber_Object = MibTableColumn
uxCallRtIntervalNumber = _UxCallRtIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 11, 1, 3),
    _UxCallRtIntervalNumber_Type()
)
uxCallRtIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCallRtIntervalNumber.setStatus("current")
_UxCallRtIntervalRuleUsage_Type = PerfIntervalCount
_UxCallRtIntervalRuleUsage_Object = MibTableColumn
uxCallRtIntervalRuleUsage = _UxCallRtIntervalRuleUsage_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 11, 1, 4),
    _UxCallRtIntervalRuleUsage_Type()
)
uxCallRtIntervalRuleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCallRtIntervalRuleUsage.setStatus("current")
_UxCallRtStatsTotalTable_Object = MibTable
uxCallRtStatsTotalTable = _UxCallRtStatsTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 12)
)
if mibBuilder.loadTexts:
    uxCallRtStatsTotalTable.setStatus("current")
_UxCallRtStatsTotalEntry_Object = MibTableRow
uxCallRtStatsTotalEntry = _UxCallRtStatsTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 12, 1)
)
uxCallRtStatsTotalEntry.setIndexNames(
    (0, "UX-CALL-STATS-MIB", "uxCallRtTotalTablesIndex"),
    (0, "UX-CALL-STATS-MIB", "uxCallRtTotalEntryIndex"),
)
if mibBuilder.loadTexts:
    uxCallRtStatsTotalEntry.setStatus("current")


class _UxCallRtTotalTablesIndex_Type(Integer32):
    """Custom type uxCallRtTotalTablesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxCallRtTotalTablesIndex_Type.__name__ = "Integer32"
_UxCallRtTotalTablesIndex_Object = MibTableColumn
uxCallRtTotalTablesIndex = _UxCallRtTotalTablesIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 12, 1, 1),
    _UxCallRtTotalTablesIndex_Type()
)
uxCallRtTotalTablesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCallRtTotalTablesIndex.setStatus("current")


class _UxCallRtTotalEntryIndex_Type(Integer32):
    """Custom type uxCallRtTotalEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxCallRtTotalEntryIndex_Type.__name__ = "Integer32"
_UxCallRtTotalEntryIndex_Object = MibTableColumn
uxCallRtTotalEntryIndex = _UxCallRtTotalEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 12, 1, 2),
    _UxCallRtTotalEntryIndex_Type()
)
uxCallRtTotalEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCallRtTotalEntryIndex.setStatus("current")
_UxCallRtTotalRuleUsage_Type = PerfTotalCount
_UxCallRtTotalRuleUsage_Object = MibTableColumn
uxCallRtTotalRuleUsage = _UxCallRtTotalRuleUsage_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 12, 1, 3),
    _UxCallRtTotalRuleUsage_Type()
)
uxCallRtTotalRuleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCallRtTotalRuleUsage.setStatus("current")
_UxLicenseStatsIntervalTable_Object = MibTable
uxLicenseStatsIntervalTable = _UxLicenseStatsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 13)
)
if mibBuilder.loadTexts:
    uxLicenseStatsIntervalTable.setStatus("current")
_UxLicenseStatsIntervalEntry_Object = MibTableRow
uxLicenseStatsIntervalEntry = _UxLicenseStatsIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 13, 1)
)
uxLicenseStatsIntervalEntry.setIndexNames(
    (0, "UX-CALL-STATS-MIB", "uxLicenseIntervalNumber"),
)
if mibBuilder.loadTexts:
    uxLicenseStatsIntervalEntry.setStatus("current")


class _UxLicenseIntervalNumber_Type(Integer32):
    """Custom type uxLicenseIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_UxLicenseIntervalNumber_Type.__name__ = "Integer32"
_UxLicenseIntervalNumber_Object = MibTableColumn
uxLicenseIntervalNumber = _UxLicenseIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 13, 1, 1),
    _UxLicenseIntervalNumber_Type()
)
uxLicenseIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxLicenseIntervalNumber.setStatus("current")
_UxLicenseIntervalPeakSIPCall_Type = PerfTotalCount
_UxLicenseIntervalPeakSIPCall_Object = MibTableColumn
uxLicenseIntervalPeakSIPCall = _UxLicenseIntervalPeakSIPCall_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 13, 1, 2),
    _UxLicenseIntervalPeakSIPCall_Type()
)
uxLicenseIntervalPeakSIPCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxLicenseIntervalPeakSIPCall.setStatus("current")
_UxLicenseIntervalPeakSIPRegistration_Type = PerfTotalCount
_UxLicenseIntervalPeakSIPRegistration_Object = MibTableColumn
uxLicenseIntervalPeakSIPRegistration = _UxLicenseIntervalPeakSIPRegistration_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 13, 1, 3),
    _UxLicenseIntervalPeakSIPRegistration_Type()
)
uxLicenseIntervalPeakSIPRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxLicenseIntervalPeakSIPRegistration.setStatus("current")
_UxLicenseIntervalPeakTDMChannel_Type = PerfTotalCount
_UxLicenseIntervalPeakTDMChannel_Object = MibTableColumn
uxLicenseIntervalPeakTDMChannel = _UxLicenseIntervalPeakTDMChannel_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 13, 1, 4),
    _UxLicenseIntervalPeakTDMChannel_Type()
)
uxLicenseIntervalPeakTDMChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxLicenseIntervalPeakTDMChannel.setStatus("deprecated")
_UxLicenseIntervalPeakDSP_Type = PerfTotalCount
_UxLicenseIntervalPeakDSP_Object = MibTableColumn
uxLicenseIntervalPeakDSP = _UxLicenseIntervalPeakDSP_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 13, 1, 5),
    _UxLicenseIntervalPeakDSP_Type()
)
uxLicenseIntervalPeakDSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxLicenseIntervalPeakDSP.setStatus("current")
_UxSIPRegistrationsStatsCurrentTable_Object = MibTable
uxSIPRegistrationsStatsCurrentTable = _UxSIPRegistrationsStatsCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 15)
)
if mibBuilder.loadTexts:
    uxSIPRegistrationsStatsCurrentTable.setStatus("current")
_UxSIPRegistrationsStatsCurrentEntry_Object = MibTableRow
uxSIPRegistrationsStatsCurrentEntry = _UxSIPRegistrationsStatsCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 15, 1)
)
uxSIPRegistrationsStatsCurrentEntry.setIndexNames(
    (0, "UX-CALL-STATS-MIB", "uxSIPRegistrationsCurrentIndex"),
)
if mibBuilder.loadTexts:
    uxSIPRegistrationsStatsCurrentEntry.setStatus("current")


class _UxSIPRegistrationsCurrentIndex_Type(Integer32):
    """Custom type uxSIPRegistrationsCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxSIPRegistrationsCurrentIndex_Type.__name__ = "Integer32"
_UxSIPRegistrationsCurrentIndex_Object = MibTableColumn
uxSIPRegistrationsCurrentIndex = _UxSIPRegistrationsCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 15, 1, 1),
    _UxSIPRegistrationsCurrentIndex_Type()
)
uxSIPRegistrationsCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSIPRegistrationsCurrentIndex.setStatus("current")
_UxSIPRegistrationsCurrentPeakUsers_Type = PerfCurrentCount
_UxSIPRegistrationsCurrentPeakUsers_Object = MibTableColumn
uxSIPRegistrationsCurrentPeakUsers = _UxSIPRegistrationsCurrentPeakUsers_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 15, 1, 2),
    _UxSIPRegistrationsCurrentPeakUsers_Type()
)
uxSIPRegistrationsCurrentPeakUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSIPRegistrationsCurrentPeakUsers.setStatus("current")
_UxSIPRegistrationsStatsIntervalTable_Object = MibTable
uxSIPRegistrationsStatsIntervalTable = _UxSIPRegistrationsStatsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 16)
)
if mibBuilder.loadTexts:
    uxSIPRegistrationsStatsIntervalTable.setStatus("current")
_UxSIPRegistrationsStatsIntervalEntry_Object = MibTableRow
uxSIPRegistrationsStatsIntervalEntry = _UxSIPRegistrationsStatsIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 16, 1)
)
uxSIPRegistrationsStatsIntervalEntry.setIndexNames(
    (0, "UX-CALL-STATS-MIB", "uxSIPRegistrationsIntervalIndex"),
    (0, "UX-CALL-STATS-MIB", "uxSIPRegistrationsIntervalNumber"),
)
if mibBuilder.loadTexts:
    uxSIPRegistrationsStatsIntervalEntry.setStatus("current")


class _UxSIPRegistrationsIntervalIndex_Type(Integer32):
    """Custom type uxSIPRegistrationsIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxSIPRegistrationsIntervalIndex_Type.__name__ = "Integer32"
_UxSIPRegistrationsIntervalIndex_Object = MibTableColumn
uxSIPRegistrationsIntervalIndex = _UxSIPRegistrationsIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 16, 1, 1),
    _UxSIPRegistrationsIntervalIndex_Type()
)
uxSIPRegistrationsIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSIPRegistrationsIntervalIndex.setStatus("current")


class _UxSIPRegistrationsIntervalNumber_Type(Integer32):
    """Custom type uxSIPRegistrationsIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_UxSIPRegistrationsIntervalNumber_Type.__name__ = "Integer32"
_UxSIPRegistrationsIntervalNumber_Object = MibTableColumn
uxSIPRegistrationsIntervalNumber = _UxSIPRegistrationsIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 16, 1, 2),
    _UxSIPRegistrationsIntervalNumber_Type()
)
uxSIPRegistrationsIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSIPRegistrationsIntervalNumber.setStatus("current")
_UxSIPRegistrationsIntervalPeakUsers_Type = PerfIntervalCount
_UxSIPRegistrationsIntervalPeakUsers_Object = MibTableColumn
uxSIPRegistrationsIntervalPeakUsers = _UxSIPRegistrationsIntervalPeakUsers_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 16, 1, 3),
    _UxSIPRegistrationsIntervalPeakUsers_Type()
)
uxSIPRegistrationsIntervalPeakUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSIPRegistrationsIntervalPeakUsers.setStatus("current")
_UxEthernetPortStatsIntervalTable_Object = MibTable
uxEthernetPortStatsIntervalTable = _UxEthernetPortStatsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17)
)
if mibBuilder.loadTexts:
    uxEthernetPortStatsIntervalTable.setStatus("current")
_UxEthernetPortStatsIntervalEntry_Object = MibTableRow
uxEthernetPortStatsIntervalEntry = _UxEthernetPortStatsIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1)
)
uxEthernetPortStatsIntervalEntry.setIndexNames(
    (0, "UX-CALL-STATS-MIB", "uxEthernetPortIntervalIndex"),
    (0, "UX-CALL-STATS-MIB", "uxEthernetPortInterval"),
)
if mibBuilder.loadTexts:
    uxEthernetPortStatsIntervalEntry.setStatus("current")


class _UxEthernetPortIntervalIndex_Type(Integer32):
    """Custom type uxEthernetPortIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxEthernetPortIntervalIndex_Type.__name__ = "Integer32"
_UxEthernetPortIntervalIndex_Object = MibTableColumn
uxEthernetPortIntervalIndex = _UxEthernetPortIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 1),
    _UxEthernetPortIntervalIndex_Type()
)
uxEthernetPortIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxEthernetPortIntervalIndex.setStatus("current")


class _UxEthernetPortInterval_Type(Integer32):
    """Custom type uxEthernetPortInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_UxEthernetPortInterval_Type.__name__ = "Integer32"
_UxEthernetPortInterval_Object = MibTableColumn
uxEthernetPortInterval = _UxEthernetPortInterval_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 2),
    _UxEthernetPortInterval_Type()
)
uxEthernetPortInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxEthernetPortInterval.setStatus("current")
_UxIntervalifInUcastPkts_Type = PerfIntervalCount
_UxIntervalifInUcastPkts_Object = MibTableColumn
uxIntervalifInUcastPkts = _UxIntervalifInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 3),
    _UxIntervalifInUcastPkts_Type()
)
uxIntervalifInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifInUcastPkts.setStatus("current")
_UxIntervalifInBroadcastPkts_Type = PerfIntervalCount
_UxIntervalifInBroadcastPkts_Object = MibTableColumn
uxIntervalifInBroadcastPkts = _UxIntervalifInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 4),
    _UxIntervalifInBroadcastPkts_Type()
)
uxIntervalifInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifInBroadcastPkts.setStatus("current")
_UxIntervalifInMulticastPkts_Type = PerfIntervalCount
_UxIntervalifInMulticastPkts_Object = MibTableColumn
uxIntervalifInMulticastPkts = _UxIntervalifInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 5),
    _UxIntervalifInMulticastPkts_Type()
)
uxIntervalifInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifInMulticastPkts.setStatus("current")
_UxIntervalifInOctets_Type = PerfIntervalCount
_UxIntervalifInOctets_Object = MibTableColumn
uxIntervalifInOctets = _UxIntervalifInOctets_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 6),
    _UxIntervalifInOctets_Type()
)
uxIntervalifInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifInOctets.setStatus("current")
_UxIntervalifInErrors_Type = PerfIntervalCount
_UxIntervalifInErrors_Object = MibTableColumn
uxIntervalifInErrors = _UxIntervalifInErrors_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 7),
    _UxIntervalifInErrors_Type()
)
uxIntervalifInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifInErrors.setStatus("current")
_UxIntervalifInDiscards_Type = PerfIntervalCount
_UxIntervalifInDiscards_Object = MibTableColumn
uxIntervalifInDiscards = _UxIntervalifInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 8),
    _UxIntervalifInDiscards_Type()
)
uxIntervalifInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifInDiscards.setStatus("current")
_UxIntervalifInUnknwnProto_Type = PerfIntervalCount
_UxIntervalifInUnknwnProto_Object = MibTableColumn
uxIntervalifInUnknwnProto = _UxIntervalifInUnknwnProto_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 9),
    _UxIntervalifInUnknwnProto_Type()
)
uxIntervalifInUnknwnProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifInUnknwnProto.setStatus("current")
_UxIntervalifInUndersizedPkts_Type = PerfIntervalCount
_UxIntervalifInUndersizedPkts_Object = MibTableColumn
uxIntervalifInUndersizedPkts = _UxIntervalifInUndersizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 10),
    _UxIntervalifInUndersizedPkts_Type()
)
uxIntervalifInUndersizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifInUndersizedPkts.setStatus("current")
_UxIntervalifInOverSizedPkts_Type = PerfIntervalCount
_UxIntervalifInOverSizedPkts_Object = MibTableColumn
uxIntervalifInOverSizedPkts = _UxIntervalifInOverSizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 11),
    _UxIntervalifInOverSizedPkts_Type()
)
uxIntervalifInOverSizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifInOverSizedPkts.setStatus("current")
_UxIntervalifInFCSErrors_Type = PerfIntervalCount
_UxIntervalifInFCSErrors_Object = MibTableColumn
uxIntervalifInFCSErrors = _UxIntervalifInFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 12),
    _UxIntervalifInFCSErrors_Type()
)
uxIntervalifInFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifInFCSErrors.setStatus("current")
_UxIntervalifInAlignErrors_Type = PerfIntervalCount
_UxIntervalifInAlignErrors_Object = MibTableColumn
uxIntervalifInAlignErrors = _UxIntervalifInAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 13),
    _UxIntervalifInAlignErrors_Type()
)
uxIntervalifInAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifInAlignErrors.setStatus("current")
_UxIntervalifInFragmentedPkts_Type = PerfIntervalCount
_UxIntervalifInFragmentedPkts_Object = MibTableColumn
uxIntervalifInFragmentedPkts = _UxIntervalifInFragmentedPkts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 14),
    _UxIntervalifInFragmentedPkts_Type()
)
uxIntervalifInFragmentedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifInFragmentedPkts.setStatus("current")
_UxIntervalifOutUcastPkts_Type = PerfIntervalCount
_UxIntervalifOutUcastPkts_Object = MibTableColumn
uxIntervalifOutUcastPkts = _UxIntervalifOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 15),
    _UxIntervalifOutUcastPkts_Type()
)
uxIntervalifOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifOutUcastPkts.setStatus("current")
_UxIntervalifOutOctets_Type = PerfIntervalCount
_UxIntervalifOutOctets_Object = MibTableColumn
uxIntervalifOutOctets = _UxIntervalifOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 16),
    _UxIntervalifOutOctets_Type()
)
uxIntervalifOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifOutOctets.setStatus("current")
_UxIntervalifOutBroadcastPkts_Type = PerfIntervalCount
_UxIntervalifOutBroadcastPkts_Object = MibTableColumn
uxIntervalifOutBroadcastPkts = _UxIntervalifOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 17),
    _UxIntervalifOutBroadcastPkts_Type()
)
uxIntervalifOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifOutBroadcastPkts.setStatus("current")
_UxIntervalifOutMulticastPkts_Type = PerfIntervalCount
_UxIntervalifOutMulticastPkts_Object = MibTableColumn
uxIntervalifOutMulticastPkts = _UxIntervalifOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 18),
    _UxIntervalifOutMulticastPkts_Type()
)
uxIntervalifOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifOutMulticastPkts.setStatus("current")
_UxIntervalifOutErrors_Type = PerfIntervalCount
_UxIntervalifOutErrors_Object = MibTableColumn
uxIntervalifOutErrors = _UxIntervalifOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 19),
    _UxIntervalifOutErrors_Type()
)
uxIntervalifOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifOutErrors.setStatus("current")
_UxIntervalifOutDiscards_Type = PerfIntervalCount
_UxIntervalifOutDiscards_Object = MibTableColumn
uxIntervalifOutDiscards = _UxIntervalifOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 20),
    _UxIntervalifOutDiscards_Type()
)
uxIntervalifOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifOutDiscards.setStatus("current")
_UxIntervalifOutLateCollissions_Type = PerfIntervalCount
_UxIntervalifOutLateCollissions_Object = MibTableColumn
uxIntervalifOutLateCollissions = _UxIntervalifOutLateCollissions_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 21),
    _UxIntervalifOutLateCollissions_Type()
)
uxIntervalifOutLateCollissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifOutLateCollissions.setStatus("current")
_UxIntervalifOutDeferredTransmissions_Type = PerfIntervalCount
_UxIntervalifOutDeferredTransmissions_Object = MibTableColumn
uxIntervalifOutDeferredTransmissions = _UxIntervalifOutDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 17, 1, 22),
    _UxIntervalifOutDeferredTransmissions_Type()
)
uxIntervalifOutDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxIntervalifOutDeferredTransmissions.setStatus("current")
_UxEthernetPortStatsCurrentTable_Object = MibTable
uxEthernetPortStatsCurrentTable = _UxEthernetPortStatsCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18)
)
if mibBuilder.loadTexts:
    uxEthernetPortStatsCurrentTable.setStatus("current")
_UxEthernetPortStatsCurrentEntry_Object = MibTableRow
uxEthernetPortStatsCurrentEntry = _UxEthernetPortStatsCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1)
)
uxEthernetPortStatsCurrentEntry.setIndexNames(
    (0, "UX-CALL-STATS-MIB", "uxEthernetPortCurrentIndex"),
)
if mibBuilder.loadTexts:
    uxEthernetPortStatsCurrentEntry.setStatus("current")


class _UxEthernetPortCurrentIndex_Type(Integer32):
    """Custom type uxEthernetPortCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxEthernetPortCurrentIndex_Type.__name__ = "Integer32"
_UxEthernetPortCurrentIndex_Object = MibTableColumn
uxEthernetPortCurrentIndex = _UxEthernetPortCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 1),
    _UxEthernetPortCurrentIndex_Type()
)
uxEthernetPortCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxEthernetPortCurrentIndex.setStatus("current")
_UxCurrentifInUcastPkts_Type = PerfCurrentCount
_UxCurrentifInUcastPkts_Object = MibTableColumn
uxCurrentifInUcastPkts = _UxCurrentifInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 2),
    _UxCurrentifInUcastPkts_Type()
)
uxCurrentifInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifInUcastPkts.setStatus("current")
_UxCurrentifInBroadcastPkts_Type = PerfCurrentCount
_UxCurrentifInBroadcastPkts_Object = MibTableColumn
uxCurrentifInBroadcastPkts = _UxCurrentifInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 3),
    _UxCurrentifInBroadcastPkts_Type()
)
uxCurrentifInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifInBroadcastPkts.setStatus("current")
_UxCurrentifInMulticastPkts_Type = PerfCurrentCount
_UxCurrentifInMulticastPkts_Object = MibTableColumn
uxCurrentifInMulticastPkts = _UxCurrentifInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 4),
    _UxCurrentifInMulticastPkts_Type()
)
uxCurrentifInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifInMulticastPkts.setStatus("current")
_UxCurrentifInOctets_Type = PerfCurrentCount
_UxCurrentifInOctets_Object = MibTableColumn
uxCurrentifInOctets = _UxCurrentifInOctets_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 5),
    _UxCurrentifInOctets_Type()
)
uxCurrentifInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifInOctets.setStatus("current")
_UxCurrentifInErrors_Type = PerfCurrentCount
_UxCurrentifInErrors_Object = MibTableColumn
uxCurrentifInErrors = _UxCurrentifInErrors_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 6),
    _UxCurrentifInErrors_Type()
)
uxCurrentifInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifInErrors.setStatus("current")
_UxCurrentifInDiscards_Type = PerfCurrentCount
_UxCurrentifInDiscards_Object = MibTableColumn
uxCurrentifInDiscards = _UxCurrentifInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 7),
    _UxCurrentifInDiscards_Type()
)
uxCurrentifInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifInDiscards.setStatus("current")
_UxCurrentifInUnknwnProto_Type = PerfCurrentCount
_UxCurrentifInUnknwnProto_Object = MibTableColumn
uxCurrentifInUnknwnProto = _UxCurrentifInUnknwnProto_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 8),
    _UxCurrentifInUnknwnProto_Type()
)
uxCurrentifInUnknwnProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifInUnknwnProto.setStatus("current")
_UxCurrentifInUndersizedPkts_Type = PerfCurrentCount
_UxCurrentifInUndersizedPkts_Object = MibTableColumn
uxCurrentifInUndersizedPkts = _UxCurrentifInUndersizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 9),
    _UxCurrentifInUndersizedPkts_Type()
)
uxCurrentifInUndersizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifInUndersizedPkts.setStatus("current")
_UxCurrentifInOverSizedPkts_Type = PerfCurrentCount
_UxCurrentifInOverSizedPkts_Object = MibTableColumn
uxCurrentifInOverSizedPkts = _UxCurrentifInOverSizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 10),
    _UxCurrentifInOverSizedPkts_Type()
)
uxCurrentifInOverSizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifInOverSizedPkts.setStatus("current")
_UxCurrentifInFCSErrors_Type = PerfCurrentCount
_UxCurrentifInFCSErrors_Object = MibTableColumn
uxCurrentifInFCSErrors = _UxCurrentifInFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 11),
    _UxCurrentifInFCSErrors_Type()
)
uxCurrentifInFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifInFCSErrors.setStatus("current")
_UxCurrentifInAlignErrors_Type = PerfCurrentCount
_UxCurrentifInAlignErrors_Object = MibTableColumn
uxCurrentifInAlignErrors = _UxCurrentifInAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 12),
    _UxCurrentifInAlignErrors_Type()
)
uxCurrentifInAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifInAlignErrors.setStatus("current")
_UxCurrentifInFragmentedPkts_Type = PerfCurrentCount
_UxCurrentifInFragmentedPkts_Object = MibTableColumn
uxCurrentifInFragmentedPkts = _UxCurrentifInFragmentedPkts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 13),
    _UxCurrentifInFragmentedPkts_Type()
)
uxCurrentifInFragmentedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifInFragmentedPkts.setStatus("current")
_UxCurrentifOutUcastPkts_Type = PerfCurrentCount
_UxCurrentifOutUcastPkts_Object = MibTableColumn
uxCurrentifOutUcastPkts = _UxCurrentifOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 14),
    _UxCurrentifOutUcastPkts_Type()
)
uxCurrentifOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifOutUcastPkts.setStatus("current")
_UxCurrentifOutOctets_Type = PerfCurrentCount
_UxCurrentifOutOctets_Object = MibTableColumn
uxCurrentifOutOctets = _UxCurrentifOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 15),
    _UxCurrentifOutOctets_Type()
)
uxCurrentifOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifOutOctets.setStatus("current")
_UxCurrentifOutBroadcastPkts_Type = PerfCurrentCount
_UxCurrentifOutBroadcastPkts_Object = MibTableColumn
uxCurrentifOutBroadcastPkts = _UxCurrentifOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 16),
    _UxCurrentifOutBroadcastPkts_Type()
)
uxCurrentifOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifOutBroadcastPkts.setStatus("current")
_UxCurrentifOutMulticastPkts_Type = PerfCurrentCount
_UxCurrentifOutMulticastPkts_Object = MibTableColumn
uxCurrentifOutMulticastPkts = _UxCurrentifOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 17),
    _UxCurrentifOutMulticastPkts_Type()
)
uxCurrentifOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifOutMulticastPkts.setStatus("current")
_UxCurrentifOutErrors_Type = PerfCurrentCount
_UxCurrentifOutErrors_Object = MibTableColumn
uxCurrentifOutErrors = _UxCurrentifOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 18),
    _UxCurrentifOutErrors_Type()
)
uxCurrentifOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifOutErrors.setStatus("current")
_UxCurrentifOutDiscards_Type = PerfCurrentCount
_UxCurrentifOutDiscards_Object = MibTableColumn
uxCurrentifOutDiscards = _UxCurrentifOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 19),
    _UxCurrentifOutDiscards_Type()
)
uxCurrentifOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifOutDiscards.setStatus("current")
_UxCurrentifOutLateCollissions_Type = PerfCurrentCount
_UxCurrentifOutLateCollissions_Object = MibTableColumn
uxCurrentifOutLateCollissions = _UxCurrentifOutLateCollissions_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 20),
    _UxCurrentifOutLateCollissions_Type()
)
uxCurrentifOutLateCollissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifOutLateCollissions.setStatus("current")
_UxCurrentifOutDeferredTransmissions_Type = PerfCurrentCount
_UxCurrentifOutDeferredTransmissions_Object = MibTableColumn
uxCurrentifOutDeferredTransmissions = _UxCurrentifOutDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 18, 1, 21),
    _UxCurrentifOutDeferredTransmissions_Type()
)
uxCurrentifOutDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCurrentifOutDeferredTransmissions.setStatus("current")
_UxGlobalCallCounters_ObjectIdentity = ObjectIdentity
uxGlobalCallCounters = _UxGlobalCallCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 19)
)
_UxNumCallAttempts_Type = Integer32
_UxNumCallAttempts_Object = MibScalar
uxNumCallAttempts = _UxNumCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 19, 1),
    _UxNumCallAttempts_Type()
)
uxNumCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxNumCallAttempts.setStatus("current")
_UxNumCallSucceeded_Type = Integer32
_UxNumCallSucceeded_Object = MibScalar
uxNumCallSucceeded = _UxNumCallSucceeded_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 19, 2),
    _UxNumCallSucceeded_Type()
)
uxNumCallSucceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxNumCallSucceeded.setStatus("current")
_UxNumCallFailed_Type = Integer32
_UxNumCallFailed_Object = MibScalar
uxNumCallFailed = _UxNumCallFailed_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 19, 3),
    _UxNumCallFailed_Type()
)
uxNumCallFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxNumCallFailed.setStatus("current")
_UxNumCallCurrentlyUp_Type = Integer32
_UxNumCallCurrentlyUp_Object = MibScalar
uxNumCallCurrentlyUp = _UxNumCallCurrentlyUp_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 19, 4),
    _UxNumCallCurrentlyUp_Type()
)
uxNumCallCurrentlyUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxNumCallCurrentlyUp.setStatus("current")
_UxNumCallCurrentlyTransient_Type = Integer32
_UxNumCallCurrentlyTransient_Object = MibScalar
uxNumCallCurrentlyTransient = _UxNumCallCurrentlyTransient_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 19, 5),
    _UxNumCallCurrentlyTransient_Type()
)
uxNumCallCurrentlyTransient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxNumCallCurrentlyTransient.setStatus("current")
_UxNumInternalGlares_Type = Integer32
_UxNumInternalGlares_Object = MibScalar
uxNumInternalGlares = _UxNumInternalGlares_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 19, 6),
    _UxNumInternalGlares_Type()
)
uxNumInternalGlares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxNumInternalGlares.setStatus("current")
_UxNumExternalGlares_Type = Integer32
_UxNumExternalGlares_Object = MibScalar
uxNumExternalGlares = _UxNumExternalGlares_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 19, 7),
    _UxNumExternalGlares_Type()
)
uxNumExternalGlares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxNumExternalGlares.setStatus("current")
_UxNumCallAbandonedNoTrunk_Type = Integer32
_UxNumCallAbandonedNoTrunk_Object = MibScalar
uxNumCallAbandonedNoTrunk = _UxNumCallAbandonedNoTrunk_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 19, 8),
    _UxNumCallAbandonedNoTrunk_Type()
)
uxNumCallAbandonedNoTrunk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxNumCallAbandonedNoTrunk.setStatus("current")
_UxNumCallUnAnswered_Type = Integer32
_UxNumCallUnAnswered_Object = MibScalar
uxNumCallUnAnswered = _UxNumCallUnAnswered_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 19, 9),
    _UxNumCallUnAnswered_Type()
)
uxNumCallUnAnswered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxNumCallUnAnswered.setStatus("current")
_UxTraps_ObjectIdentity = ObjectIdentity
uxTraps = _UxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 177, 15, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UX-CALL-STATS-MIB",
    **{"net": net,
       "ux": ux,
       "uxObjects": uxObjects,
       "ipSystem": ipSystem,
       "sysVersion": sysVersion,
       "sysBuildNumber": sysBuildNumber,
       "ipTelephony": ipTelephony,
       "callStatistics": callStatistics,
       "uxPortTable": uxPortTable,
       "uxPortEntry": uxPortEntry,
       "uxPTIndex": uxPTIndex,
       "uxPTShelf": uxPTShelf,
       "uxPTSlot": uxPTSlot,
       "uxPTPort": uxPTPort,
       "uxPTCurrentCalls": uxPTCurrentCalls,
       "uxPTTotalCalls": uxPTTotalCalls,
       "uxPTConnectedCalls": uxPTConnectedCalls,
       "uxPTRefusedCalls": uxPTRefusedCalls,
       "uxPTErroredCalls": uxPTErroredCalls,
       "uxPTEgressCallAttempts": uxPTEgressCallAttempts,
       "uxPTEgressCallsAccepted": uxPTEgressCallsAccepted,
       "uxPTEgressCallsCompleted": uxPTEgressCallsCompleted,
       "uxPTEgressCallsRejected": uxPTEgressCallsRejected,
       "uxPTIngressCallAttempts": uxPTIngressCallAttempts,
       "uxPTIngressCallsAccepted": uxPTIngressCallsAccepted,
       "uxPTIngressCallsCompleted": uxPTIngressCallsCompleted,
       "uxPTIngressCallsRejected": uxPTIngressCallsRejected,
       "uxPTBlockedCalls": uxPTBlockedCalls,
       "uxPTEgressBlockedCalls": uxPTEgressBlockedCalls,
       "uxPTIngressBlockedCalls": uxPTIngressBlockedCalls,
       "uxPTEgressCurrentCalls": uxPTEgressCurrentCalls,
       "uxPTIngressCurrentCalls": uxPTIngressCurrentCalls,
       "uxPTBHCARate": uxPTBHCARate,
       "uxPTBHCCRate": uxPTBHCCRate,
       "uxCallRtTablesTable": uxCallRtTablesTable,
       "uxCallRtTablesEntry": uxCallRtTablesEntry,
       "uxCallRtTablesTableIndex": uxCallRtTablesTableIndex,
       "uxDesc": uxDesc,
       "uxCallRtSequence": uxCallRtSequence,
       "uxCallRtTable": uxCallRtTable,
       "uxCallRtEntry": uxCallRtEntry,
       "uxCallRtTablesIndex": uxCallRtTablesIndex,
       "uxCallRtIndex": uxCallRtIndex,
       "uxDescription": uxDescription,
       "uxAdminState": uxAdminState,
       "uxRoutePriority": uxRoutePriority,
       "uxSignalingGroupList": uxSignalingGroupList,
       "uxQualityMetricCalls": uxQualityMetricCalls,
       "uxQualityMetricTime": uxQualityMetricTime,
       "uxQualityMinASRThreshold": uxQualityMinASRThreshold,
       "uxQualityMaxRoundTripDelayThreshold": uxQualityMaxRoundTripDelayThreshold,
       "uxQualityMaxJitterThreshold": uxQualityMaxJitterThreshold,
       "uxQualityMinMOSThreshold": uxQualityMinMOSThreshold,
       "uxSGTable": uxSGTable,
       "uxSGEntry": uxSGEntry,
       "uxSGEntryIndex": uxSGEntryIndex,
       "uxSGDescription": uxSGDescription,
       "uxSGType": uxSGType,
       "uxSGAdminState": uxSGAdminState,
       "uxSGServiceState": uxSGServiceState,
       "uxSipServerTable": uxSipServerTable,
       "uxSipServerEntry": uxSipServerEntry,
       "uxSGIndex": uxSGIndex,
       "uxSipServerIndex": uxSipServerIndex,
       "uxSipSvrPriority": uxSipSvrPriority,
       "uxSipSvrHost": uxSipSvrHost,
       "uxSipSvrPort": uxSipSvrPort,
       "uxSipSvrTransProtocol": uxSipSvrTransProtocol,
       "uxChannelStatusTable": uxChannelStatusTable,
       "uxChannelStatusEntry": uxChannelStatusEntry,
       "uxChShelfNumber": uxChShelfNumber,
       "uxChSlotNumber": uxChSlotNumber,
       "uxChPortNumber": uxChPortNumber,
       "uxChChannelNumber": uxChChannelNumber,
       "uxChAdminState": uxChAdminState,
       "uxChOperState": uxChOperState,
       "uxChInUseSeconds": uxChInUseSeconds,
       "uxSGStatsCurrentTable": uxSGStatsCurrentTable,
       "uxSGStatsCurrentEntry": uxSGStatsCurrentEntry,
       "uxSGCurrentIndex": uxSGCurrentIndex,
       "uxSGCurrentPeakChannelUsage": uxSGCurrentPeakChannelUsage,
       "uxSGCurrentCompletedCalls": uxSGCurrentCompletedCalls,
       "uxSGCurrentIncompleteCalls": uxSGCurrentIncompleteCalls,
       "uxSGStatsIntervalTable": uxSGStatsIntervalTable,
       "uxSGStatsIntervalEntry": uxSGStatsIntervalEntry,
       "uxSGIntervalIndex": uxSGIntervalIndex,
       "uxSGIntervalNumber": uxSGIntervalNumber,
       "uxSGIntervalPeakChannelUsage": uxSGIntervalPeakChannelUsage,
       "uxSGIntervalCompletedCalls": uxSGIntervalCompletedCalls,
       "uxSGIntervalIncompleteCalls": uxSGIntervalIncompleteCalls,
       "uxCallRtStatsCurrentTable": uxCallRtStatsCurrentTable,
       "uxCallRtStatsCurrentEntry": uxCallRtStatsCurrentEntry,
       "uxCallRtCurrentTablesIndex": uxCallRtCurrentTablesIndex,
       "uxCallRtCurrentEntryIndex": uxCallRtCurrentEntryIndex,
       "uxCallRtCurrentRuleUsage": uxCallRtCurrentRuleUsage,
       "uxCallRtStatsIntervalTable": uxCallRtStatsIntervalTable,
       "uxCallRtStatsIntervalEntry": uxCallRtStatsIntervalEntry,
       "uxCallRtIntervalTablesIndex": uxCallRtIntervalTablesIndex,
       "uxCallRtIntervalEntryIndex": uxCallRtIntervalEntryIndex,
       "uxCallRtIntervalNumber": uxCallRtIntervalNumber,
       "uxCallRtIntervalRuleUsage": uxCallRtIntervalRuleUsage,
       "uxCallRtStatsTotalTable": uxCallRtStatsTotalTable,
       "uxCallRtStatsTotalEntry": uxCallRtStatsTotalEntry,
       "uxCallRtTotalTablesIndex": uxCallRtTotalTablesIndex,
       "uxCallRtTotalEntryIndex": uxCallRtTotalEntryIndex,
       "uxCallRtTotalRuleUsage": uxCallRtTotalRuleUsage,
       "uxLicenseStatsIntervalTable": uxLicenseStatsIntervalTable,
       "uxLicenseStatsIntervalEntry": uxLicenseStatsIntervalEntry,
       "uxLicenseIntervalNumber": uxLicenseIntervalNumber,
       "uxLicenseIntervalPeakSIPCall": uxLicenseIntervalPeakSIPCall,
       "uxLicenseIntervalPeakSIPRegistration": uxLicenseIntervalPeakSIPRegistration,
       "uxLicenseIntervalPeakTDMChannel": uxLicenseIntervalPeakTDMChannel,
       "uxLicenseIntervalPeakDSP": uxLicenseIntervalPeakDSP,
       "uxSIPRegistrationsStatsCurrentTable": uxSIPRegistrationsStatsCurrentTable,
       "uxSIPRegistrationsStatsCurrentEntry": uxSIPRegistrationsStatsCurrentEntry,
       "uxSIPRegistrationsCurrentIndex": uxSIPRegistrationsCurrentIndex,
       "uxSIPRegistrationsCurrentPeakUsers": uxSIPRegistrationsCurrentPeakUsers,
       "uxSIPRegistrationsStatsIntervalTable": uxSIPRegistrationsStatsIntervalTable,
       "uxSIPRegistrationsStatsIntervalEntry": uxSIPRegistrationsStatsIntervalEntry,
       "uxSIPRegistrationsIntervalIndex": uxSIPRegistrationsIntervalIndex,
       "uxSIPRegistrationsIntervalNumber": uxSIPRegistrationsIntervalNumber,
       "uxSIPRegistrationsIntervalPeakUsers": uxSIPRegistrationsIntervalPeakUsers,
       "uxEthernetPortStatsIntervalTable": uxEthernetPortStatsIntervalTable,
       "uxEthernetPortStatsIntervalEntry": uxEthernetPortStatsIntervalEntry,
       "uxEthernetPortIntervalIndex": uxEthernetPortIntervalIndex,
       "uxEthernetPortInterval": uxEthernetPortInterval,
       "uxIntervalifInUcastPkts": uxIntervalifInUcastPkts,
       "uxIntervalifInBroadcastPkts": uxIntervalifInBroadcastPkts,
       "uxIntervalifInMulticastPkts": uxIntervalifInMulticastPkts,
       "uxIntervalifInOctets": uxIntervalifInOctets,
       "uxIntervalifInErrors": uxIntervalifInErrors,
       "uxIntervalifInDiscards": uxIntervalifInDiscards,
       "uxIntervalifInUnknwnProto": uxIntervalifInUnknwnProto,
       "uxIntervalifInUndersizedPkts": uxIntervalifInUndersizedPkts,
       "uxIntervalifInOverSizedPkts": uxIntervalifInOverSizedPkts,
       "uxIntervalifInFCSErrors": uxIntervalifInFCSErrors,
       "uxIntervalifInAlignErrors": uxIntervalifInAlignErrors,
       "uxIntervalifInFragmentedPkts": uxIntervalifInFragmentedPkts,
       "uxIntervalifOutUcastPkts": uxIntervalifOutUcastPkts,
       "uxIntervalifOutOctets": uxIntervalifOutOctets,
       "uxIntervalifOutBroadcastPkts": uxIntervalifOutBroadcastPkts,
       "uxIntervalifOutMulticastPkts": uxIntervalifOutMulticastPkts,
       "uxIntervalifOutErrors": uxIntervalifOutErrors,
       "uxIntervalifOutDiscards": uxIntervalifOutDiscards,
       "uxIntervalifOutLateCollissions": uxIntervalifOutLateCollissions,
       "uxIntervalifOutDeferredTransmissions": uxIntervalifOutDeferredTransmissions,
       "uxEthernetPortStatsCurrentTable": uxEthernetPortStatsCurrentTable,
       "uxEthernetPortStatsCurrentEntry": uxEthernetPortStatsCurrentEntry,
       "uxEthernetPortCurrentIndex": uxEthernetPortCurrentIndex,
       "uxCurrentifInUcastPkts": uxCurrentifInUcastPkts,
       "uxCurrentifInBroadcastPkts": uxCurrentifInBroadcastPkts,
       "uxCurrentifInMulticastPkts": uxCurrentifInMulticastPkts,
       "uxCurrentifInOctets": uxCurrentifInOctets,
       "uxCurrentifInErrors": uxCurrentifInErrors,
       "uxCurrentifInDiscards": uxCurrentifInDiscards,
       "uxCurrentifInUnknwnProto": uxCurrentifInUnknwnProto,
       "uxCurrentifInUndersizedPkts": uxCurrentifInUndersizedPkts,
       "uxCurrentifInOverSizedPkts": uxCurrentifInOverSizedPkts,
       "uxCurrentifInFCSErrors": uxCurrentifInFCSErrors,
       "uxCurrentifInAlignErrors": uxCurrentifInAlignErrors,
       "uxCurrentifInFragmentedPkts": uxCurrentifInFragmentedPkts,
       "uxCurrentifOutUcastPkts": uxCurrentifOutUcastPkts,
       "uxCurrentifOutOctets": uxCurrentifOutOctets,
       "uxCurrentifOutBroadcastPkts": uxCurrentifOutBroadcastPkts,
       "uxCurrentifOutMulticastPkts": uxCurrentifOutMulticastPkts,
       "uxCurrentifOutErrors": uxCurrentifOutErrors,
       "uxCurrentifOutDiscards": uxCurrentifOutDiscards,
       "uxCurrentifOutLateCollissions": uxCurrentifOutLateCollissions,
       "uxCurrentifOutDeferredTransmissions": uxCurrentifOutDeferredTransmissions,
       "uxGlobalCallCounters": uxGlobalCallCounters,
       "uxNumCallAttempts": uxNumCallAttempts,
       "uxNumCallSucceeded": uxNumCallSucceeded,
       "uxNumCallFailed": uxNumCallFailed,
       "uxNumCallCurrentlyUp": uxNumCallCurrentlyUp,
       "uxNumCallCurrentlyTransient": uxNumCallCurrentlyTransient,
       "uxNumInternalGlares": uxNumInternalGlares,
       "uxNumExternalGlares": uxNumExternalGlares,
       "uxNumCallAbandonedNoTrunk": uxNumCallAbandonedNoTrunk,
       "uxNumCallUnAnswered": uxNumCallUnAnswered,
       "uxTraps": uxTraps}
)
