# SNMP MIB module (ELTEX-PROCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-PROCESS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:48:17 2025
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

(EltexPercent,
 EltexThresholdRelation) = mibBuilder.importSymbols(
    "ELTEX-TC",
    "EltexPercent",
    "EltexThresholdRelation")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

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

(SyslogSeverity,) = mibBuilder.importSymbols(
    "SYSLOG-TC-MIB",
    "SyslogSeverity")


# MODULE-IDENTITY

eltexProcessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 41)
)
if mibBuilder.loadTexts:
    eltexProcessMIB.setRevisions(
        ("2017-05-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltexProcessMIBObjects_ObjectIdentity = ObjectIdentity
eltexProcessMIBObjects = _EltexProcessMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1)
)
_EltexProcessCPU_ObjectIdentity = ObjectIdentity
eltexProcessCPU = _EltexProcessCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1)
)
_EltexProcessCPUMonitorTable_Object = MibTable
eltexProcessCPUMonitorTable = _EltexProcessCPUMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltexProcessCPUMonitorTable.setStatus("current")
_EltexProcessCPUMonitorEntry_Object = MibTableRow
eltexProcessCPUMonitorEntry = _EltexProcessCPUMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 1, 1)
)
eltexProcessCPUMonitorEntry.setIndexNames(
    (0, "ELTEX-PROCESS-MIB", "eltexProcessCPUMonitorIndex"),
    (0, "ELTEX-PROCESS-MIB", "eltexProcessCPUMonitorInterval"),
)
if mibBuilder.loadTexts:
    eltexProcessCPUMonitorEntry.setStatus("current")
_EltexProcessCPUMonitorIndex_Type = Unsigned32
_EltexProcessCPUMonitorIndex_Object = MibTableColumn
eltexProcessCPUMonitorIndex = _EltexProcessCPUMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 1, 1, 1),
    _EltexProcessCPUMonitorIndex_Type()
)
eltexProcessCPUMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexProcessCPUMonitorIndex.setStatus("current")
_EltexProcessCPUMonitorInterval_Type = Unsigned32
_EltexProcessCPUMonitorInterval_Object = MibTableColumn
eltexProcessCPUMonitorInterval = _EltexProcessCPUMonitorInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 1, 1, 2),
    _EltexProcessCPUMonitorInterval_Type()
)
eltexProcessCPUMonitorInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexProcessCPUMonitorInterval.setStatus("current")
if mibBuilder.loadTexts:
    eltexProcessCPUMonitorInterval.setUnits("seconds")
_EltexProcessCPUMonitorPhysicalIndex_Type = PhysicalIndex
_EltexProcessCPUMonitorPhysicalIndex_Object = MibTableColumn
eltexProcessCPUMonitorPhysicalIndex = _EltexProcessCPUMonitorPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 1, 1, 3),
    _EltexProcessCPUMonitorPhysicalIndex_Type()
)
eltexProcessCPUMonitorPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexProcessCPUMonitorPhysicalIndex.setStatus("current")
_EltexProcessCPUMonitorValue_Type = EltexPercent
_EltexProcessCPUMonitorValue_Object = MibTableColumn
eltexProcessCPUMonitorValue = _EltexProcessCPUMonitorValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 1, 1, 4),
    _EltexProcessCPUMonitorValue_Type()
)
eltexProcessCPUMonitorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexProcessCPUMonitorValue.setStatus("current")
if mibBuilder.loadTexts:
    eltexProcessCPUMonitorValue.setUnits("percent")
_EltexProcessCPUMonitorValidValue_Type = TruthValue
_EltexProcessCPUMonitorValidValue_Object = MibTableColumn
eltexProcessCPUMonitorValidValue = _EltexProcessCPUMonitorValidValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 1, 1, 5),
    _EltexProcessCPUMonitorValidValue_Type()
)
eltexProcessCPUMonitorValidValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexProcessCPUMonitorValidValue.setStatus("current")
_EltexProcessCPUMonitorThresholdFreeIndex_Type = Unsigned32
_EltexProcessCPUMonitorThresholdFreeIndex_Object = MibTableColumn
eltexProcessCPUMonitorThresholdFreeIndex = _EltexProcessCPUMonitorThresholdFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 1, 1, 6),
    _EltexProcessCPUMonitorThresholdFreeIndex_Type()
)
eltexProcessCPUMonitorThresholdFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexProcessCPUMonitorThresholdFreeIndex.setStatus("current")
_EltexProcessCPUThreshold_ObjectIdentity = ObjectIdentity
eltexProcessCPUThreshold = _EltexProcessCPUThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 2)
)


class _EltexProcessCPUThresholdNotificationGlobalEnable_Type(TruthValue):
    """Custom type eltexProcessCPUThresholdNotificationGlobalEnable based on TruthValue"""
    defaultValue = 2


_EltexProcessCPUThresholdNotificationGlobalEnable_Type.__name__ = "TruthValue"
_EltexProcessCPUThresholdNotificationGlobalEnable_Object = MibScalar
eltexProcessCPUThresholdNotificationGlobalEnable = _EltexProcessCPUThresholdNotificationGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 2, 1),
    _EltexProcessCPUThresholdNotificationGlobalEnable_Type()
)
eltexProcessCPUThresholdNotificationGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexProcessCPUThresholdNotificationGlobalEnable.setStatus("current")


class _EltexProcessCPUThresholdRecoveryNotificationGlobalEnable_Type(TruthValue):
    """Custom type eltexProcessCPUThresholdRecoveryNotificationGlobalEnable based on TruthValue"""
    defaultValue = 2


_EltexProcessCPUThresholdRecoveryNotificationGlobalEnable_Type.__name__ = "TruthValue"
_EltexProcessCPUThresholdRecoveryNotificationGlobalEnable_Object = MibScalar
eltexProcessCPUThresholdRecoveryNotificationGlobalEnable = _EltexProcessCPUThresholdRecoveryNotificationGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 2, 2),
    _EltexProcessCPUThresholdRecoveryNotificationGlobalEnable_Type()
)
eltexProcessCPUThresholdRecoveryNotificationGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexProcessCPUThresholdRecoveryNotificationGlobalEnable.setStatus("current")
_EltexProcessCPUThresholdTable_Object = MibTable
eltexProcessCPUThresholdTable = _EltexProcessCPUThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    eltexProcessCPUThresholdTable.setStatus("current")
_EltexProcessCPUThresholdEntry_Object = MibTableRow
eltexProcessCPUThresholdEntry = _EltexProcessCPUThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 2, 3, 1)
)
eltexProcessCPUThresholdEntry.setIndexNames(
    (0, "ELTEX-PROCESS-MIB", "eltexProcessCPUMonitorIndex"),
    (0, "ELTEX-PROCESS-MIB", "eltexProcessCPUThresholdIndex"),
    (0, "ELTEX-PROCESS-MIB", "eltexProcessCPUMonitorInterval"),
)
if mibBuilder.loadTexts:
    eltexProcessCPUThresholdEntry.setStatus("current")
_EltexProcessCPUThresholdIndex_Type = Unsigned32
_EltexProcessCPUThresholdIndex_Object = MibTableColumn
eltexProcessCPUThresholdIndex = _EltexProcessCPUThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 2, 3, 1, 1),
    _EltexProcessCPUThresholdIndex_Type()
)
eltexProcessCPUThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexProcessCPUThresholdIndex.setStatus("current")
_EltexProcessCPUThresholdRowStatus_Type = RowStatus
_EltexProcessCPUThresholdRowStatus_Object = MibTableColumn
eltexProcessCPUThresholdRowStatus = _EltexProcessCPUThresholdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 2, 3, 1, 2),
    _EltexProcessCPUThresholdRowStatus_Type()
)
eltexProcessCPUThresholdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexProcessCPUThresholdRowStatus.setStatus("current")
_EltexProcessCPUThresholdValue_Type = EltexPercent
_EltexProcessCPUThresholdValue_Object = MibTableColumn
eltexProcessCPUThresholdValue = _EltexProcessCPUThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 2, 3, 1, 3),
    _EltexProcessCPUThresholdValue_Type()
)
eltexProcessCPUThresholdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexProcessCPUThresholdValue.setStatus("current")


class _EltexProcessCPUThresholdFlappingInterval_Type(EltexPercent):
    """Custom type eltexProcessCPUThresholdFlappingInterval based on EltexPercent"""
    defaultValue = 0


_EltexProcessCPUThresholdFlappingInterval_Type.__name__ = "EltexPercent"
_EltexProcessCPUThresholdFlappingInterval_Object = MibTableColumn
eltexProcessCPUThresholdFlappingInterval = _EltexProcessCPUThresholdFlappingInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 2, 3, 1, 4),
    _EltexProcessCPUThresholdFlappingInterval_Type()
)
eltexProcessCPUThresholdFlappingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexProcessCPUThresholdFlappingInterval.setStatus("current")


class _EltexProcessCPUThresholdSeverity_Type(SyslogSeverity):
    """Custom type eltexProcessCPUThresholdSeverity based on SyslogSeverity"""
    defaultValue = 1


_EltexProcessCPUThresholdSeverity_Type.__name__ = "SyslogSeverity"
_EltexProcessCPUThresholdSeverity_Object = MibTableColumn
eltexProcessCPUThresholdSeverity = _EltexProcessCPUThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 2, 3, 1, 5),
    _EltexProcessCPUThresholdSeverity_Type()
)
eltexProcessCPUThresholdSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexProcessCPUThresholdSeverity.setStatus("current")
_EltexProcessCPUThresholdRelation_Type = EltexThresholdRelation
_EltexProcessCPUThresholdRelation_Object = MibTableColumn
eltexProcessCPUThresholdRelation = _EltexProcessCPUThresholdRelation_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 2, 3, 1, 6),
    _EltexProcessCPUThresholdRelation_Type()
)
eltexProcessCPUThresholdRelation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexProcessCPUThresholdRelation.setStatus("current")


class _EltexProcessCPUThresholdNotificationEnable_Type(TruthValue):
    """Custom type eltexProcessCPUThresholdNotificationEnable based on TruthValue"""
    defaultValue = 1


_EltexProcessCPUThresholdNotificationEnable_Type.__name__ = "TruthValue"
_EltexProcessCPUThresholdNotificationEnable_Object = MibTableColumn
eltexProcessCPUThresholdNotificationEnable = _EltexProcessCPUThresholdNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 2, 3, 1, 7),
    _EltexProcessCPUThresholdNotificationEnable_Type()
)
eltexProcessCPUThresholdNotificationEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexProcessCPUThresholdNotificationEnable.setStatus("current")


class _EltexProcessCPUThresholdRecoveryNotificationEnable_Type(TruthValue):
    """Custom type eltexProcessCPUThresholdRecoveryNotificationEnable based on TruthValue"""
    defaultValue = 1


_EltexProcessCPUThresholdRecoveryNotificationEnable_Type.__name__ = "TruthValue"
_EltexProcessCPUThresholdRecoveryNotificationEnable_Object = MibTableColumn
eltexProcessCPUThresholdRecoveryNotificationEnable = _EltexProcessCPUThresholdRecoveryNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 2, 3, 1, 8),
    _EltexProcessCPUThresholdRecoveryNotificationEnable_Type()
)
eltexProcessCPUThresholdRecoveryNotificationEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexProcessCPUThresholdRecoveryNotificationEnable.setStatus("current")
_EltexProcessCPUThresholdEvaluation_Type = TruthValue
_EltexProcessCPUThresholdEvaluation_Object = MibTableColumn
eltexProcessCPUThresholdEvaluation = _EltexProcessCPUThresholdEvaluation_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 1, 2, 3, 1, 9),
    _EltexProcessCPUThresholdEvaluation_Type()
)
eltexProcessCPUThresholdEvaluation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexProcessCPUThresholdEvaluation.setStatus("current")
_EltexProcessMemory_ObjectIdentity = ObjectIdentity
eltexProcessMemory = _EltexProcessMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2)
)
_EltexProcessMemoryTable_Object = MibTable
eltexProcessMemoryTable = _EltexProcessMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltexProcessMemoryTable.setStatus("current")
_EltexProcessMemoryEntry_Object = MibTableRow
eltexProcessMemoryEntry = _EltexProcessMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 1, 1)
)
eltexProcessMemoryEntry.setIndexNames(
    (0, "ELTEX-PROCESS-MIB", "eltexProcessMemoryIndex"),
)
if mibBuilder.loadTexts:
    eltexProcessMemoryEntry.setStatus("current")
_EltexProcessMemoryIndex_Type = Unsigned32
_EltexProcessMemoryIndex_Object = MibTableColumn
eltexProcessMemoryIndex = _EltexProcessMemoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 1, 1, 1),
    _EltexProcessMemoryIndex_Type()
)
eltexProcessMemoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexProcessMemoryIndex.setStatus("current")
_EltexProcessMemoryPhysicalIndex_Type = PhysicalIndex
_EltexProcessMemoryPhysicalIndex_Object = MibTableColumn
eltexProcessMemoryPhysicalIndex = _EltexProcessMemoryPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 1, 1, 2),
    _EltexProcessMemoryPhysicalIndex_Type()
)
eltexProcessMemoryPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexProcessMemoryPhysicalIndex.setStatus("current")
_EltexProcessMemoryTotal_Type = Gauge32
_EltexProcessMemoryTotal_Object = MibTableColumn
eltexProcessMemoryTotal = _EltexProcessMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 1, 1, 3),
    _EltexProcessMemoryTotal_Type()
)
eltexProcessMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexProcessMemoryTotal.setStatus("current")
if mibBuilder.loadTexts:
    eltexProcessMemoryTotal.setUnits("bytes")
_EltexProcessMemoryTotalOverflow_Type = Gauge32
_EltexProcessMemoryTotalOverflow_Object = MibTableColumn
eltexProcessMemoryTotalOverflow = _EltexProcessMemoryTotalOverflow_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 1, 1, 4),
    _EltexProcessMemoryTotalOverflow_Type()
)
eltexProcessMemoryTotalOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexProcessMemoryTotalOverflow.setStatus("current")
if mibBuilder.loadTexts:
    eltexProcessMemoryTotalOverflow.setUnits("bytes")
_EltexProcessMemoryHCTotal_Type = Counter64
_EltexProcessMemoryHCTotal_Object = MibTableColumn
eltexProcessMemoryHCTotal = _EltexProcessMemoryHCTotal_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 1, 1, 5),
    _EltexProcessMemoryHCTotal_Type()
)
eltexProcessMemoryHCTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexProcessMemoryHCTotal.setStatus("current")
if mibBuilder.loadTexts:
    eltexProcessMemoryHCTotal.setUnits("bytes")
_EltexProcessMemoryFreePercent_Type = EltexPercent
_EltexProcessMemoryFreePercent_Object = MibTableColumn
eltexProcessMemoryFreePercent = _EltexProcessMemoryFreePercent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 1, 1, 6),
    _EltexProcessMemoryFreePercent_Type()
)
eltexProcessMemoryFreePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexProcessMemoryFreePercent.setStatus("current")
_EltexProcessMemoryFree_Type = Gauge32
_EltexProcessMemoryFree_Object = MibTableColumn
eltexProcessMemoryFree = _EltexProcessMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 1, 1, 7),
    _EltexProcessMemoryFree_Type()
)
eltexProcessMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexProcessMemoryFree.setStatus("current")
if mibBuilder.loadTexts:
    eltexProcessMemoryFree.setUnits("bytes")
_EltexProcessMemoryFreeOverflow_Type = Gauge32
_EltexProcessMemoryFreeOverflow_Object = MibTableColumn
eltexProcessMemoryFreeOverflow = _EltexProcessMemoryFreeOverflow_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 1, 1, 8),
    _EltexProcessMemoryFreeOverflow_Type()
)
eltexProcessMemoryFreeOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexProcessMemoryFreeOverflow.setStatus("current")
if mibBuilder.loadTexts:
    eltexProcessMemoryFreeOverflow.setUnits("bytes")
_EltexProcessMemoryHCFree_Type = Counter64
_EltexProcessMemoryHCFree_Object = MibTableColumn
eltexProcessMemoryHCFree = _EltexProcessMemoryHCFree_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 1, 1, 9),
    _EltexProcessMemoryHCFree_Type()
)
eltexProcessMemoryHCFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexProcessMemoryHCFree.setStatus("current")
if mibBuilder.loadTexts:
    eltexProcessMemoryHCFree.setUnits("bytes")
_EltexProcessMemoryThresholdFreeIndex_Type = Unsigned32
_EltexProcessMemoryThresholdFreeIndex_Object = MibTableColumn
eltexProcessMemoryThresholdFreeIndex = _EltexProcessMemoryThresholdFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 1, 1, 10),
    _EltexProcessMemoryThresholdFreeIndex_Type()
)
eltexProcessMemoryThresholdFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexProcessMemoryThresholdFreeIndex.setStatus("current")
_EltexProcessMemoryThreshold_ObjectIdentity = ObjectIdentity
eltexProcessMemoryThreshold = _EltexProcessMemoryThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 2)
)


class _EltexProcessMemoryThresholdNotificationGlobalEnable_Type(TruthValue):
    """Custom type eltexProcessMemoryThresholdNotificationGlobalEnable based on TruthValue"""
    defaultValue = 2


_EltexProcessMemoryThresholdNotificationGlobalEnable_Type.__name__ = "TruthValue"
_EltexProcessMemoryThresholdNotificationGlobalEnable_Object = MibScalar
eltexProcessMemoryThresholdNotificationGlobalEnable = _EltexProcessMemoryThresholdNotificationGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 2, 1),
    _EltexProcessMemoryThresholdNotificationGlobalEnable_Type()
)
eltexProcessMemoryThresholdNotificationGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexProcessMemoryThresholdNotificationGlobalEnable.setStatus("current")


class _EltexProcessMemoryThresholdRecoveryNotificationGlobalEnable_Type(TruthValue):
    """Custom type eltexProcessMemoryThresholdRecoveryNotificationGlobalEnable based on TruthValue"""
    defaultValue = 2


_EltexProcessMemoryThresholdRecoveryNotificationGlobalEnable_Type.__name__ = "TruthValue"
_EltexProcessMemoryThresholdRecoveryNotificationGlobalEnable_Object = MibScalar
eltexProcessMemoryThresholdRecoveryNotificationGlobalEnable = _EltexProcessMemoryThresholdRecoveryNotificationGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 2, 2),
    _EltexProcessMemoryThresholdRecoveryNotificationGlobalEnable_Type()
)
eltexProcessMemoryThresholdRecoveryNotificationGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexProcessMemoryThresholdRecoveryNotificationGlobalEnable.setStatus("current")
_EltexProcessMemoryThresholdTable_Object = MibTable
eltexProcessMemoryThresholdTable = _EltexProcessMemoryThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    eltexProcessMemoryThresholdTable.setStatus("current")
_EltexProcessMemoryThresholdEntry_Object = MibTableRow
eltexProcessMemoryThresholdEntry = _EltexProcessMemoryThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 2, 3, 1)
)
eltexProcessMemoryThresholdEntry.setIndexNames(
    (0, "ELTEX-PROCESS-MIB", "eltexProcessMemoryIndex"),
    (0, "ELTEX-PROCESS-MIB", "eltexProcessMemoryThresholdIndex"),
)
if mibBuilder.loadTexts:
    eltexProcessMemoryThresholdEntry.setStatus("current")
_EltexProcessMemoryThresholdIndex_Type = Unsigned32
_EltexProcessMemoryThresholdIndex_Object = MibTableColumn
eltexProcessMemoryThresholdIndex = _EltexProcessMemoryThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 2, 3, 1, 1),
    _EltexProcessMemoryThresholdIndex_Type()
)
eltexProcessMemoryThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltexProcessMemoryThresholdIndex.setStatus("current")
_EltexProcessMemoryThresholdRowStatus_Type = RowStatus
_EltexProcessMemoryThresholdRowStatus_Object = MibTableColumn
eltexProcessMemoryThresholdRowStatus = _EltexProcessMemoryThresholdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 2, 3, 1, 2),
    _EltexProcessMemoryThresholdRowStatus_Type()
)
eltexProcessMemoryThresholdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexProcessMemoryThresholdRowStatus.setStatus("current")
_EltexProcessMemoryThresholdValue_Type = EltexPercent
_EltexProcessMemoryThresholdValue_Object = MibTableColumn
eltexProcessMemoryThresholdValue = _EltexProcessMemoryThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 2, 3, 1, 3),
    _EltexProcessMemoryThresholdValue_Type()
)
eltexProcessMemoryThresholdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexProcessMemoryThresholdValue.setStatus("current")


class _EltexProcessMemoryThresholdFlappingInterval_Type(EltexPercent):
    """Custom type eltexProcessMemoryThresholdFlappingInterval based on EltexPercent"""
    defaultValue = 0


_EltexProcessMemoryThresholdFlappingInterval_Type.__name__ = "EltexPercent"
_EltexProcessMemoryThresholdFlappingInterval_Object = MibTableColumn
eltexProcessMemoryThresholdFlappingInterval = _EltexProcessMemoryThresholdFlappingInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 2, 3, 1, 4),
    _EltexProcessMemoryThresholdFlappingInterval_Type()
)
eltexProcessMemoryThresholdFlappingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexProcessMemoryThresholdFlappingInterval.setStatus("current")


class _EltexProcessMemoryThresholdSeverity_Type(SyslogSeverity):
    """Custom type eltexProcessMemoryThresholdSeverity based on SyslogSeverity"""
    defaultValue = 1


_EltexProcessMemoryThresholdSeverity_Type.__name__ = "SyslogSeverity"
_EltexProcessMemoryThresholdSeverity_Object = MibTableColumn
eltexProcessMemoryThresholdSeverity = _EltexProcessMemoryThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 2, 3, 1, 5),
    _EltexProcessMemoryThresholdSeverity_Type()
)
eltexProcessMemoryThresholdSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexProcessMemoryThresholdSeverity.setStatus("current")
_EltexProcessMemoryThresholdRelation_Type = EltexThresholdRelation
_EltexProcessMemoryThresholdRelation_Object = MibTableColumn
eltexProcessMemoryThresholdRelation = _EltexProcessMemoryThresholdRelation_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 2, 3, 1, 6),
    _EltexProcessMemoryThresholdRelation_Type()
)
eltexProcessMemoryThresholdRelation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexProcessMemoryThresholdRelation.setStatus("current")


class _EltexProcessMemoryThresholdNotificationEnable_Type(TruthValue):
    """Custom type eltexProcessMemoryThresholdNotificationEnable based on TruthValue"""
    defaultValue = 1


_EltexProcessMemoryThresholdNotificationEnable_Type.__name__ = "TruthValue"
_EltexProcessMemoryThresholdNotificationEnable_Object = MibTableColumn
eltexProcessMemoryThresholdNotificationEnable = _EltexProcessMemoryThresholdNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 2, 3, 1, 7),
    _EltexProcessMemoryThresholdNotificationEnable_Type()
)
eltexProcessMemoryThresholdNotificationEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexProcessMemoryThresholdNotificationEnable.setStatus("current")


class _EltexProcessMemoryThresholdRecoveryNotificationEnable_Type(TruthValue):
    """Custom type eltexProcessMemoryThresholdRecoveryNotificationEnable based on TruthValue"""
    defaultValue = 1


_EltexProcessMemoryThresholdRecoveryNotificationEnable_Type.__name__ = "TruthValue"
_EltexProcessMemoryThresholdRecoveryNotificationEnable_Object = MibTableColumn
eltexProcessMemoryThresholdRecoveryNotificationEnable = _EltexProcessMemoryThresholdRecoveryNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 2, 3, 1, 8),
    _EltexProcessMemoryThresholdRecoveryNotificationEnable_Type()
)
eltexProcessMemoryThresholdRecoveryNotificationEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexProcessMemoryThresholdRecoveryNotificationEnable.setStatus("current")
_EltexProcessMemoryThresholdEvaluation_Type = TruthValue
_EltexProcessMemoryThresholdEvaluation_Object = MibTableColumn
eltexProcessMemoryThresholdEvaluation = _EltexProcessMemoryThresholdEvaluation_Object(
    (1, 3, 6, 1, 4, 1, 35265, 41, 1, 2, 2, 3, 1, 9),
    _EltexProcessMemoryThresholdEvaluation_Type()
)
eltexProcessMemoryThresholdEvaluation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexProcessMemoryThresholdEvaluation.setStatus("current")
_EltexProcessMIBNotification_ObjectIdentity = ObjectIdentity
eltexProcessMIBNotification = _EltexProcessMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 41, 2)
)
_EltexProcessMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
eltexProcessMIBNotificationPrefix = _EltexProcessMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 41, 2, 0)
)

# Managed Objects groups


# Notification objects

eltexProcessCPUThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 41, 2, 0, 1)
)
eltexProcessCPUThresholdNotification.setObjects(
      *(("ELTEX-PROCESS-MIB", "eltexProcessCPUThresholdSeverity"),
        ("ELTEX-PROCESS-MIB", "eltexProcessCPUThresholdRelation"),
        ("ELTEX-PROCESS-MIB", "eltexProcessCPUThresholdValue"),
        ("ELTEX-PROCESS-MIB", "eltexProcessCPUMonitorValue"))
)
if mibBuilder.loadTexts:
    eltexProcessCPUThresholdNotification.setStatus(
        "current"
    )

eltexProcessCPUThresholdRecoveryNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 41, 2, 0, 2)
)
eltexProcessCPUThresholdRecoveryNotification.setObjects(
      *(("ELTEX-PROCESS-MIB", "eltexProcessCPUThresholdSeverity"),
        ("ELTEX-PROCESS-MIB", "eltexProcessCPUThresholdRelation"),
        ("ELTEX-PROCESS-MIB", "eltexProcessCPUThresholdValue"),
        ("ELTEX-PROCESS-MIB", "eltexProcessCPUMonitorValue"))
)
if mibBuilder.loadTexts:
    eltexProcessCPUThresholdRecoveryNotification.setStatus(
        "current"
    )

eltexProcessMemoryThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 41, 2, 0, 3)
)
eltexProcessMemoryThresholdNotification.setObjects(
      *(("ELTEX-PROCESS-MIB", "eltexProcessMemoryThresholdSeverity"),
        ("ELTEX-PROCESS-MIB", "eltexProcessMemoryThresholdRelation"),
        ("ELTEX-PROCESS-MIB", "eltexProcessMemoryThresholdValue"),
        ("ELTEX-PROCESS-MIB", "eltexProcessMemoryFreePercent"))
)
if mibBuilder.loadTexts:
    eltexProcessMemoryThresholdNotification.setStatus(
        "current"
    )

eltexProcessMemoryThresholdRecoveryNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 41, 2, 0, 4)
)
eltexProcessMemoryThresholdRecoveryNotification.setObjects(
      *(("ELTEX-PROCESS-MIB", "eltexProcessMemoryThresholdSeverity"),
        ("ELTEX-PROCESS-MIB", "eltexProcessMemoryThresholdRelation"),
        ("ELTEX-PROCESS-MIB", "eltexProcessMemoryThresholdValue"),
        ("ELTEX-PROCESS-MIB", "eltexProcessMemoryFreePercent"))
)
if mibBuilder.loadTexts:
    eltexProcessMemoryThresholdRecoveryNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-PROCESS-MIB",
    **{"eltexProcessMIB": eltexProcessMIB,
       "eltexProcessMIBObjects": eltexProcessMIBObjects,
       "eltexProcessCPU": eltexProcessCPU,
       "eltexProcessCPUMonitorTable": eltexProcessCPUMonitorTable,
       "eltexProcessCPUMonitorEntry": eltexProcessCPUMonitorEntry,
       "eltexProcessCPUMonitorIndex": eltexProcessCPUMonitorIndex,
       "eltexProcessCPUMonitorInterval": eltexProcessCPUMonitorInterval,
       "eltexProcessCPUMonitorPhysicalIndex": eltexProcessCPUMonitorPhysicalIndex,
       "eltexProcessCPUMonitorValue": eltexProcessCPUMonitorValue,
       "eltexProcessCPUMonitorValidValue": eltexProcessCPUMonitorValidValue,
       "eltexProcessCPUMonitorThresholdFreeIndex": eltexProcessCPUMonitorThresholdFreeIndex,
       "eltexProcessCPUThreshold": eltexProcessCPUThreshold,
       "eltexProcessCPUThresholdNotificationGlobalEnable": eltexProcessCPUThresholdNotificationGlobalEnable,
       "eltexProcessCPUThresholdRecoveryNotificationGlobalEnable": eltexProcessCPUThresholdRecoveryNotificationGlobalEnable,
       "eltexProcessCPUThresholdTable": eltexProcessCPUThresholdTable,
       "eltexProcessCPUThresholdEntry": eltexProcessCPUThresholdEntry,
       "eltexProcessCPUThresholdIndex": eltexProcessCPUThresholdIndex,
       "eltexProcessCPUThresholdRowStatus": eltexProcessCPUThresholdRowStatus,
       "eltexProcessCPUThresholdValue": eltexProcessCPUThresholdValue,
       "eltexProcessCPUThresholdFlappingInterval": eltexProcessCPUThresholdFlappingInterval,
       "eltexProcessCPUThresholdSeverity": eltexProcessCPUThresholdSeverity,
       "eltexProcessCPUThresholdRelation": eltexProcessCPUThresholdRelation,
       "eltexProcessCPUThresholdNotificationEnable": eltexProcessCPUThresholdNotificationEnable,
       "eltexProcessCPUThresholdRecoveryNotificationEnable": eltexProcessCPUThresholdRecoveryNotificationEnable,
       "eltexProcessCPUThresholdEvaluation": eltexProcessCPUThresholdEvaluation,
       "eltexProcessMemory": eltexProcessMemory,
       "eltexProcessMemoryTable": eltexProcessMemoryTable,
       "eltexProcessMemoryEntry": eltexProcessMemoryEntry,
       "eltexProcessMemoryIndex": eltexProcessMemoryIndex,
       "eltexProcessMemoryPhysicalIndex": eltexProcessMemoryPhysicalIndex,
       "eltexProcessMemoryTotal": eltexProcessMemoryTotal,
       "eltexProcessMemoryTotalOverflow": eltexProcessMemoryTotalOverflow,
       "eltexProcessMemoryHCTotal": eltexProcessMemoryHCTotal,
       "eltexProcessMemoryFreePercent": eltexProcessMemoryFreePercent,
       "eltexProcessMemoryFree": eltexProcessMemoryFree,
       "eltexProcessMemoryFreeOverflow": eltexProcessMemoryFreeOverflow,
       "eltexProcessMemoryHCFree": eltexProcessMemoryHCFree,
       "eltexProcessMemoryThresholdFreeIndex": eltexProcessMemoryThresholdFreeIndex,
       "eltexProcessMemoryThreshold": eltexProcessMemoryThreshold,
       "eltexProcessMemoryThresholdNotificationGlobalEnable": eltexProcessMemoryThresholdNotificationGlobalEnable,
       "eltexProcessMemoryThresholdRecoveryNotificationGlobalEnable": eltexProcessMemoryThresholdRecoveryNotificationGlobalEnable,
       "eltexProcessMemoryThresholdTable": eltexProcessMemoryThresholdTable,
       "eltexProcessMemoryThresholdEntry": eltexProcessMemoryThresholdEntry,
       "eltexProcessMemoryThresholdIndex": eltexProcessMemoryThresholdIndex,
       "eltexProcessMemoryThresholdRowStatus": eltexProcessMemoryThresholdRowStatus,
       "eltexProcessMemoryThresholdValue": eltexProcessMemoryThresholdValue,
       "eltexProcessMemoryThresholdFlappingInterval": eltexProcessMemoryThresholdFlappingInterval,
       "eltexProcessMemoryThresholdSeverity": eltexProcessMemoryThresholdSeverity,
       "eltexProcessMemoryThresholdRelation": eltexProcessMemoryThresholdRelation,
       "eltexProcessMemoryThresholdNotificationEnable": eltexProcessMemoryThresholdNotificationEnable,
       "eltexProcessMemoryThresholdRecoveryNotificationEnable": eltexProcessMemoryThresholdRecoveryNotificationEnable,
       "eltexProcessMemoryThresholdEvaluation": eltexProcessMemoryThresholdEvaluation,
       "eltexProcessMIBNotification": eltexProcessMIBNotification,
       "eltexProcessMIBNotificationPrefix": eltexProcessMIBNotificationPrefix,
       "eltexProcessCPUThresholdNotification": eltexProcessCPUThresholdNotification,
       "eltexProcessCPUThresholdRecoveryNotification": eltexProcessCPUThresholdRecoveryNotification,
       "eltexProcessMemoryThresholdNotification": eltexProcessMemoryThresholdNotification,
       "eltexProcessMemoryThresholdRecoveryNotification": eltexProcessMemoryThresholdRecoveryNotification}
)
