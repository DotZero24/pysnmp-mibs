# SNMP MIB module (RAISECOM-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:50 2025
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

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

raisecomSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1)
)

raisecomCpu = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1)
)

raisecomEndPool = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 2)
)

raisecomMemory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 3)
)

raisecomInformation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ProcessStatus(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("delay", 2),
          ("delay-s", 3),
          ("pend", 4),
          ("pend-t", 5),
          ("pend-s", 6),
          ("pend-t-s", 7),
          ("suspend", 8),
          ("dead", 9))
    )



class CPUTimeStamp(TextualConvention, OctetString):
    status = "current"
    displayHint = "4d.4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class PortAlarmEventList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1



# MIB Managed Objects in the order of their OIDs



class _RaisecomCpuBusy1Per_Type(Integer32):
    """Custom type raisecomCpuBusy1Per based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaisecomCpuBusy1Per_Type.__name__ = "Integer32"
_RaisecomCpuBusy1Per_Object = MibScalar
raisecomCpuBusy1Per = _RaisecomCpuBusy1Per_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 1),
    _RaisecomCpuBusy1Per_Type()
)
raisecomCpuBusy1Per.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomCpuBusy1Per.setStatus("mandatory")
if mibBuilder.loadTexts:
    raisecomCpuBusy1Per.setUnits("percent")


class _RaisecomCpuBusy60Per_Type(Integer32):
    """Custom type raisecomCpuBusy60Per based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaisecomCpuBusy60Per_Type.__name__ = "Integer32"
_RaisecomCpuBusy60Per_Object = MibScalar
raisecomCpuBusy60Per = _RaisecomCpuBusy60Per_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 2),
    _RaisecomCpuBusy60Per_Type()
)
raisecomCpuBusy60Per.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomCpuBusy60Per.setStatus("mandatory")
if mibBuilder.loadTexts:
    raisecomCpuBusy60Per.setUnits("percent")
_RaisecomCPUTrapGroup_ObjectIdentity = ObjectIdentity
raisecomCPUTrapGroup = _RaisecomCPUTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 3)
)
_RaisecomCPUScalarGroup_ObjectIdentity = ObjectIdentity
raisecomCPUScalarGroup = _RaisecomCPUScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 4)
)


class _RaisecomCPUUtilizationTotal_Type(Integer32):
    """Custom type raisecomCPUUtilizationTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaisecomCPUUtilizationTotal_Type.__name__ = "Integer32"
_RaisecomCPUUtilizationTotal_Object = MibScalar
raisecomCPUUtilizationTotal = _RaisecomCPUUtilizationTotal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 4, 1),
    _RaisecomCPUUtilizationTotal_Type()
)
raisecomCPUUtilizationTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomCPUUtilizationTotal.setStatus("current")
if mibBuilder.loadTexts:
    raisecomCPUUtilizationTotal.setUnits("percent")


class _RaisecomCPUHistoryTableSize_Type(Integer32):
    """Custom type raisecomCPUHistoryTableSize based on Integer32"""
    defaultValue = 60


_RaisecomCPUHistoryTableSize_Type.__name__ = "Integer32"
_RaisecomCPUHistoryTableSize_Object = MibScalar
raisecomCPUHistoryTableSize = _RaisecomCPUHistoryTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 4, 2),
    _RaisecomCPUHistoryTableSize_Type()
)
raisecomCPUHistoryTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomCPUHistoryTableSize.setStatus("current")
_RaisecomCPUThresholdTrapEnable_Type = EnableVar
_RaisecomCPUThresholdTrapEnable_Object = MibScalar
raisecomCPUThresholdTrapEnable = _RaisecomCPUThresholdTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 4, 3),
    _RaisecomCPUThresholdTrapEnable_Type()
)
raisecomCPUThresholdTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomCPUThresholdTrapEnable.setStatus("current")


class _RaisecomCPURisingThresholdValue_Type(Integer32):
    """Custom type raisecomCPURisingThresholdValue based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RaisecomCPURisingThresholdValue_Type.__name__ = "Integer32"
_RaisecomCPURisingThresholdValue_Object = MibScalar
raisecomCPURisingThresholdValue = _RaisecomCPURisingThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 4, 4),
    _RaisecomCPURisingThresholdValue_Type()
)
raisecomCPURisingThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomCPURisingThresholdValue.setStatus("current")


class _RaisecomCPUFallingThresholdValue_Type(Integer32):
    """Custom type raisecomCPUFallingThresholdValue based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RaisecomCPUFallingThresholdValue_Type.__name__ = "Integer32"
_RaisecomCPUFallingThresholdValue_Object = MibScalar
raisecomCPUFallingThresholdValue = _RaisecomCPUFallingThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 4, 5),
    _RaisecomCPUFallingThresholdValue_Type()
)
raisecomCPUFallingThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomCPUFallingThresholdValue.setStatus("current")


class _RaisecomCPUThresholdInterval_Type(Integer32):
    """Custom type raisecomCPUThresholdInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 36000),
    )


_RaisecomCPUThresholdInterval_Type.__name__ = "Integer32"
_RaisecomCPUThresholdInterval_Object = MibScalar
raisecomCPUThresholdInterval = _RaisecomCPUThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 4, 6),
    _RaisecomCPUThresholdInterval_Type()
)
raisecomCPUThresholdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomCPUThresholdInterval.setStatus("current")


class _RaisecomCpuTotalProcNum_Type(Integer32):
    """Custom type raisecomCpuTotalProcNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_RaisecomCpuTotalProcNum_Type.__name__ = "Integer32"
_RaisecomCpuTotalProcNum_Object = MibScalar
raisecomCpuTotalProcNum = _RaisecomCpuTotalProcNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 4, 7),
    _RaisecomCpuTotalProcNum_Type()
)
raisecomCpuTotalProcNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomCpuTotalProcNum.setStatus("current")


class _RaisecomCPUTrapUtilization_Type(Integer32):
    """Custom type raisecomCPUTrapUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaisecomCPUTrapUtilization_Type.__name__ = "Integer32"
_RaisecomCPUTrapUtilization_Object = MibScalar
raisecomCPUTrapUtilization = _RaisecomCPUTrapUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 4, 8),
    _RaisecomCPUTrapUtilization_Type()
)
raisecomCPUTrapUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomCPUTrapUtilization.setStatus("current")
if mibBuilder.loadTexts:
    raisecomCPUTrapUtilization.setUnits("percent")
_RaisecomCPUTableGroup_ObjectIdentity = ObjectIdentity
raisecomCPUTableGroup = _RaisecomCPUTableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5)
)
_RaisecomCPUUtilizationGroup_ObjectIdentity = ObjectIdentity
raisecomCPUUtilizationGroup = _RaisecomCPUUtilizationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 1)
)
_RaisecomCPUUtilizationTable_Object = MibTable
raisecomCPUUtilizationTable = _RaisecomCPUUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    raisecomCPUUtilizationTable.setStatus("current")
_RaisecomCPUUtilizationEntry_Object = MibTableRow
raisecomCPUUtilizationEntry = _RaisecomCPUUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 1, 1, 1)
)
raisecomCPUUtilizationEntry.setIndexNames(
    (0, "RAISECOM-SYSTEM-MIB", "raisecomCPUUtilizationIndex"),
)
if mibBuilder.loadTexts:
    raisecomCPUUtilizationEntry.setStatus("current")
_RaisecomCPUUtilizationIndex_Type = Integer32
_RaisecomCPUUtilizationIndex_Object = MibTableColumn
raisecomCPUUtilizationIndex = _RaisecomCPUUtilizationIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 1, 1, 1, 1),
    _RaisecomCPUUtilizationIndex_Type()
)
raisecomCPUUtilizationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomCPUUtilizationIndex.setStatus("current")


class _RaisecomCPUUtilizationPeriod_Type(Integer32):
    """Custom type raisecomCPUUtilizationPeriod based on Integer32"""
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
        *(("oneSec", 1),
          ("fiveSec", 2),
          ("oneMin", 3),
          ("tenMin", 4),
          ("twoHour", 5))
    )


_RaisecomCPUUtilizationPeriod_Type.__name__ = "Integer32"
_RaisecomCPUUtilizationPeriod_Object = MibTableColumn
raisecomCPUUtilizationPeriod = _RaisecomCPUUtilizationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 1, 1, 1, 2),
    _RaisecomCPUUtilizationPeriod_Type()
)
raisecomCPUUtilizationPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomCPUUtilizationPeriod.setStatus("current")


class _RaisecomCPUUtilization_Type(Integer32):
    """Custom type raisecomCPUUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaisecomCPUUtilization_Type.__name__ = "Integer32"
_RaisecomCPUUtilization_Object = MibTableColumn
raisecomCPUUtilization = _RaisecomCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 1, 1, 1, 3),
    _RaisecomCPUUtilization_Type()
)
raisecomCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomCPUUtilization.setStatus("current")
if mibBuilder.loadTexts:
    raisecomCPUUtilization.setUnits("percent")
_RaisecomCPUHistoryTable_Object = MibTable
raisecomCPUHistoryTable = _RaisecomCPUHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    raisecomCPUHistoryTable.setStatus("current")
_RaisecomCPUHistoryEntry_Object = MibTableRow
raisecomCPUHistoryEntry = _RaisecomCPUHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 1, 2, 1)
)
raisecomCPUHistoryEntry.setIndexNames(
    (0, "RAISECOM-SYSTEM-MIB", "raisecomCPUHistoryPeriod"),
    (0, "RAISECOM-SYSTEM-MIB", "raisecomCPUHistoryIndex"),
)
if mibBuilder.loadTexts:
    raisecomCPUHistoryEntry.setStatus("current")


class _RaisecomCPUHistoryPeriod_Type(Integer32):
    """Custom type raisecomCPUHistoryPeriod based on Integer32"""
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
        *(("fiveSec", 1),
          ("oneMin", 2),
          ("tenMin", 3),
          ("twoHour", 4))
    )


_RaisecomCPUHistoryPeriod_Type.__name__ = "Integer32"
_RaisecomCPUHistoryPeriod_Object = MibTableColumn
raisecomCPUHistoryPeriod = _RaisecomCPUHistoryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 1, 2, 1, 1),
    _RaisecomCPUHistoryPeriod_Type()
)
raisecomCPUHistoryPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomCPUHistoryPeriod.setStatus("current")
_RaisecomCPUHistoryIndex_Type = Integer32
_RaisecomCPUHistoryIndex_Object = MibTableColumn
raisecomCPUHistoryIndex = _RaisecomCPUHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 1, 2, 1, 2),
    _RaisecomCPUHistoryIndex_Type()
)
raisecomCPUHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomCPUHistoryIndex.setStatus("current")


class _RaisecomCPUHistoryTotalUtil_Type(Integer32):
    """Custom type raisecomCPUHistoryTotalUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaisecomCPUHistoryTotalUtil_Type.__name__ = "Integer32"
_RaisecomCPUHistoryTotalUtil_Object = MibTableColumn
raisecomCPUHistoryTotalUtil = _RaisecomCPUHistoryTotalUtil_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 1, 2, 1, 3),
    _RaisecomCPUHistoryTotalUtil_Type()
)
raisecomCPUHistoryTotalUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomCPUHistoryTotalUtil.setStatus("current")
if mibBuilder.loadTexts:
    raisecomCPUHistoryTotalUtil.setUnits("percent")
_RaisecomCPUProcessesGroup_ObjectIdentity = ObjectIdentity
raisecomCPUProcessesGroup = _RaisecomCPUProcessesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2)
)
_RaisecomProcessesTable_Object = MibTable
raisecomProcessesTable = _RaisecomProcessesTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    raisecomProcessesTable.setStatus("current")
_RaisecomProcessesEntry_Object = MibTableRow
raisecomProcessesEntry = _RaisecomProcessesEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1)
)
raisecomProcessesEntry.setIndexNames(
    (0, "RAISECOM-SYSTEM-MIB", "raisecomProcessIndex"),
)
if mibBuilder.loadTexts:
    raisecomProcessesEntry.setStatus("current")
_RaisecomProcessIndex_Type = Integer32
_RaisecomProcessIndex_Object = MibTableColumn
raisecomProcessIndex = _RaisecomProcessIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 1),
    _RaisecomProcessIndex_Type()
)
raisecomProcessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessIndex.setStatus("current")
_RaisecomProcessPID_Type = Integer32
_RaisecomProcessPID_Object = MibTableColumn
raisecomProcessPID = _RaisecomProcessPID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 2),
    _RaisecomProcessPID_Type()
)
raisecomProcessPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessPID.setStatus("current")


class _RaisecomProcessName_Type(OctetString):
    """Custom type raisecomProcessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RaisecomProcessName_Type.__name__ = "OctetString"
_RaisecomProcessName_Object = MibTableColumn
raisecomProcessName = _RaisecomProcessName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 3),
    _RaisecomProcessName_Type()
)
raisecomProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessName.setStatus("current")
_RaisecomProcessRunTimeTotal_Type = CPUTimeStamp
_RaisecomProcessRunTimeTotal_Object = MibTableColumn
raisecomProcessRunTimeTotal = _RaisecomProcessRunTimeTotal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 4),
    _RaisecomProcessRunTimeTotal_Type()
)
raisecomProcessRunTimeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessRunTimeTotal.setStatus("current")
_RaisecomProcessInvokedTotal_Type = Integer32
_RaisecomProcessInvokedTotal_Object = MibTableColumn
raisecomProcessInvokedTotal = _RaisecomProcessInvokedTotal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 5),
    _RaisecomProcessInvokedTotal_Type()
)
raisecomProcessInvokedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessInvokedTotal.setStatus("current")
_RaisecomProcessTimeCreated_Type = TimeStamp
_RaisecomProcessTimeCreated_Object = MibTableColumn
raisecomProcessTimeCreated = _RaisecomProcessTimeCreated_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 6),
    _RaisecomProcessTimeCreated_Type()
)
raisecomProcessTimeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessTimeCreated.setStatus("current")
_RaisecomProcessNormalPriority_Type = Integer32
_RaisecomProcessNormalPriority_Object = MibTableColumn
raisecomProcessNormalPriority = _RaisecomProcessNormalPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 7),
    _RaisecomProcessNormalPriority_Type()
)
raisecomProcessNormalPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessNormalPriority.setStatus("current")
_RaisecomProcessCurrentPriority_Type = Integer32
_RaisecomProcessCurrentPriority_Object = MibTableColumn
raisecomProcessCurrentPriority = _RaisecomProcessCurrentPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 8),
    _RaisecomProcessCurrentPriority_Type()
)
raisecomProcessCurrentPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessCurrentPriority.setStatus("current")
_RaisecomProcessStatus_Type = ProcessStatus
_RaisecomProcessStatus_Object = MibTableColumn
raisecomProcessStatus = _RaisecomProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 9),
    _RaisecomProcessStatus_Type()
)
raisecomProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessStatus.setStatus("current")
_RaisecomProcessErrorNo_Type = Integer32
_RaisecomProcessErrorNo_Object = MibTableColumn
raisecomProcessErrorNo = _RaisecomProcessErrorNo_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 10),
    _RaisecomProcessErrorNo_Type()
)
raisecomProcessErrorNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessErrorNo.setStatus("current")
_RaisecomProcessStackSize_Type = Integer32
_RaisecomProcessStackSize_Object = MibTableColumn
raisecomProcessStackSize = _RaisecomProcessStackSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 11),
    _RaisecomProcessStackSize_Type()
)
raisecomProcessStackSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessStackSize.setStatus("current")
_RaisecomProcessStackCurrentSize_Type = Integer32
_RaisecomProcessStackCurrentSize_Object = MibTableColumn
raisecomProcessStackCurrentSize = _RaisecomProcessStackCurrentSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 12),
    _RaisecomProcessStackCurrentSize_Type()
)
raisecomProcessStackCurrentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessStackCurrentSize.setStatus("current")
_RaisecomProcessStackMaxSize_Type = Integer32
_RaisecomProcessStackMaxSize_Object = MibTableColumn
raisecomProcessStackMaxSize = _RaisecomProcessStackMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 13),
    _RaisecomProcessStackMaxSize_Type()
)
raisecomProcessStackMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessStackMaxSize.setStatus("current")
_RaisecomProcessStackBegin_Type = Integer32
_RaisecomProcessStackBegin_Object = MibTableColumn
raisecomProcessStackBegin = _RaisecomProcessStackBegin_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 14),
    _RaisecomProcessStackBegin_Type()
)
raisecomProcessStackBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessStackBegin.setStatus("current")
_RaisecomProcessStackPointer_Type = Integer32
_RaisecomProcessStackPointer_Object = MibTableColumn
raisecomProcessStackPointer = _RaisecomProcessStackPointer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 15),
    _RaisecomProcessStackPointer_Type()
)
raisecomProcessStackPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessStackPointer.setStatus("current")
_RaisecomProcessStackEnd_Type = Integer32
_RaisecomProcessStackEnd_Object = MibTableColumn
raisecomProcessStackEnd = _RaisecomProcessStackEnd_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 16),
    _RaisecomProcessStackEnd_Type()
)
raisecomProcessStackEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessStackEnd.setStatus("current")
_RaisecomProcessProgramCounter_Type = Integer32
_RaisecomProcessProgramCounter_Object = MibTableColumn
raisecomProcessProgramCounter = _RaisecomProcessProgramCounter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 17),
    _RaisecomProcessProgramCounter_Type()
)
raisecomProcessProgramCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessProgramCounter.setStatus("current")
_RaisecomProcessEntry_Type = Integer32
_RaisecomProcessEntry_Object = MibTableColumn
raisecomProcessEntry = _RaisecomProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 18),
    _RaisecomProcessEntry_Type()
)
raisecomProcessEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessEntry.setStatus("current")
_RaisecomProcessSemWait_Type = Integer32
_RaisecomProcessSemWait_Object = MibTableColumn
raisecomProcessSemWait = _RaisecomProcessSemWait_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 19),
    _RaisecomProcessSemWait_Type()
)
raisecomProcessSemWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessSemWait.setStatus("current")
_RaisecomProcessDelay_Type = Integer32
_RaisecomProcessDelay_Object = MibTableColumn
raisecomProcessDelay = _RaisecomProcessDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 1, 1, 20),
    _RaisecomProcessDelay_Type()
)
raisecomProcessDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessDelay.setStatus("current")
_RaisecomProcessStatisticsTable_Object = MibTable
raisecomProcessStatisticsTable = _RaisecomProcessStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    raisecomProcessStatisticsTable.setStatus("current")
_RaisecomProcessStatisticsEntry_Object = MibTableRow
raisecomProcessStatisticsEntry = _RaisecomProcessStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 2, 1)
)
raisecomProcessStatisticsEntry.setIndexNames(
    (0, "RAISECOM-SYSTEM-MIB", "raisecomProcessIndex"),
    (0, "RAISECOM-SYSTEM-MIB", "raisecomProcessStatisticsPeriod"),
)
if mibBuilder.loadTexts:
    raisecomProcessStatisticsEntry.setStatus("current")


class _RaisecomProcessStatisticsPeriod_Type(Integer32):
    """Custom type raisecomProcessStatisticsPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fiveSec", 1),
          ("oneMin", 2),
          ("tenMin", 3))
    )


_RaisecomProcessStatisticsPeriod_Type.__name__ = "Integer32"
_RaisecomProcessStatisticsPeriod_Object = MibTableColumn
raisecomProcessStatisticsPeriod = _RaisecomProcessStatisticsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 2, 1, 1),
    _RaisecomProcessStatisticsPeriod_Type()
)
raisecomProcessStatisticsPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomProcessStatisticsPeriod.setStatus("current")
_RaisecomProcessRunTime_Type = CPUTimeStamp
_RaisecomProcessRunTime_Object = MibTableColumn
raisecomProcessRunTime = _RaisecomProcessRunTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 2, 1, 2),
    _RaisecomProcessRunTime_Type()
)
raisecomProcessRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessRunTime.setStatus("current")
_RaisecomProcessInvoked_Type = Integer32
_RaisecomProcessInvoked_Object = MibTableColumn
raisecomProcessInvoked = _RaisecomProcessInvoked_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 2, 1, 3),
    _RaisecomProcessInvoked_Type()
)
raisecomProcessInvoked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessInvoked.setStatus("current")


class _RaisecomProcessUtilization_Type(Integer32):
    """Custom type raisecomProcessUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RaisecomProcessUtilization_Type.__name__ = "Integer32"
_RaisecomProcessUtilization_Object = MibTableColumn
raisecomProcessUtilization = _RaisecomProcessUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 2, 1, 4),
    _RaisecomProcessUtilization_Type()
)
raisecomProcessUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomProcessUtilization.setStatus("current")
if mibBuilder.loadTexts:
    raisecomProcessUtilization.setUnits("percent")
_RaisecomDeadProcessesTable_Object = MibTable
raisecomDeadProcessesTable = _RaisecomDeadProcessesTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    raisecomDeadProcessesTable.setStatus("current")
_RaisecomDeadProcessesEntry_Object = MibTableRow
raisecomDeadProcessesEntry = _RaisecomDeadProcessesEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 3, 1)
)
raisecomDeadProcessesEntry.setIndexNames(
    (0, "RAISECOM-SYSTEM-MIB", "raisecomDeadProcessIndex"),
)
if mibBuilder.loadTexts:
    raisecomDeadProcessesEntry.setStatus("current")
_RaisecomDeadProcessIndex_Type = Integer32
_RaisecomDeadProcessIndex_Object = MibTableColumn
raisecomDeadProcessIndex = _RaisecomDeadProcessIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 3, 1, 1),
    _RaisecomDeadProcessIndex_Type()
)
raisecomDeadProcessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomDeadProcessIndex.setStatus("current")


class _RaisecomDeadProcessName_Type(OctetString):
    """Custom type raisecomDeadProcessName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RaisecomDeadProcessName_Type.__name__ = "OctetString"
_RaisecomDeadProcessName_Object = MibTableColumn
raisecomDeadProcessName = _RaisecomDeadProcessName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 3, 1, 2),
    _RaisecomDeadProcessName_Type()
)
raisecomDeadProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDeadProcessName.setStatus("current")
_RaisecomDeadProcessEntry_Type = Integer32
_RaisecomDeadProcessEntry_Object = MibTableColumn
raisecomDeadProcessEntry = _RaisecomDeadProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 3, 1, 3),
    _RaisecomDeadProcessEntry_Type()
)
raisecomDeadProcessEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDeadProcessEntry.setStatus("current")
_RaisecomDeadProcessErrorNo_Type = Integer32
_RaisecomDeadProcessErrorNo_Object = MibTableColumn
raisecomDeadProcessErrorNo = _RaisecomDeadProcessErrorNo_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 3, 1, 4),
    _RaisecomDeadProcessErrorNo_Type()
)
raisecomDeadProcessErrorNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDeadProcessErrorNo.setStatus("current")
_RaisecomDeadProcessPriority_Type = Integer32
_RaisecomDeadProcessPriority_Object = MibTableColumn
raisecomDeadProcessPriority = _RaisecomDeadProcessPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 3, 1, 5),
    _RaisecomDeadProcessPriority_Type()
)
raisecomDeadProcessPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDeadProcessPriority.setStatus("current")
_RaisecomDeadProcessMaxStackSize_Type = Integer32
_RaisecomDeadProcessMaxStackSize_Object = MibTableColumn
raisecomDeadProcessMaxStackSize = _RaisecomDeadProcessMaxStackSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 3, 1, 6),
    _RaisecomDeadProcessMaxStackSize_Type()
)
raisecomDeadProcessMaxStackSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDeadProcessMaxStackSize.setStatus("current")
_RaisecomDeadProcessTimeDelete_Type = TimeStamp
_RaisecomDeadProcessTimeDelete_Object = MibTableColumn
raisecomDeadProcessTimeDelete = _RaisecomDeadProcessTimeDelete_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 3, 1, 7),
    _RaisecomDeadProcessTimeDelete_Type()
)
raisecomDeadProcessTimeDelete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDeadProcessTimeDelete.setStatus("current")
_RaisecomDeadProcessDeadTimes_Type = Integer32
_RaisecomDeadProcessDeadTimes_Object = MibTableColumn
raisecomDeadProcessDeadTimes = _RaisecomDeadProcessDeadTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 3, 1, 8),
    _RaisecomDeadProcessDeadTimes_Type()
)
raisecomDeadProcessDeadTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDeadProcessDeadTimes.setStatus("current")
_RaisecomDeadProcessStatus_Type = ProcessStatus
_RaisecomDeadProcessStatus_Object = MibTableColumn
raisecomDeadProcessStatus = _RaisecomDeadProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 5, 2, 3, 1, 9),
    _RaisecomDeadProcessStatus_Type()
)
raisecomDeadProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDeadProcessStatus.setStatus("current")
_RaisecomEndPoolTable_Object = MibTable
raisecomEndPoolTable = _RaisecomEndPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    raisecomEndPoolTable.setStatus("current")
_RaisecomEndPoolEntry_Object = MibTableRow
raisecomEndPoolEntry = _RaisecomEndPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 2, 1, 1)
)
raisecomEndPoolEntry.setIndexNames(
    (0, "RAISECOM-SYSTEM-MIB", "raisecomBasePort"),
)
if mibBuilder.loadTexts:
    raisecomEndPoolEntry.setStatus("current")
_RaisecomBasePort_Type = Integer32
_RaisecomBasePort_Object = MibTableColumn
raisecomBasePort = _RaisecomBasePort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 2, 1, 1, 1),
    _RaisecomBasePort_Type()
)
raisecomBasePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomBasePort.setStatus("current")
_RaisecomTotalEndPool_Type = Integer32
_RaisecomTotalEndPool_Object = MibTableColumn
raisecomTotalEndPool = _RaisecomTotalEndPool_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 2, 1, 1, 2),
    _RaisecomTotalEndPool_Type()
)
raisecomTotalEndPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomTotalEndPool.setStatus("current")
_RaisecomFreeEndPool_Type = Integer32
_RaisecomFreeEndPool_Object = MibTableColumn
raisecomFreeEndPool = _RaisecomFreeEndPool_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 2, 1, 1, 3),
    _RaisecomFreeEndPool_Type()
)
raisecomFreeEndPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomFreeEndPool.setStatus("current")
_RaisecomTotalMemory_Type = Integer32
_RaisecomTotalMemory_Object = MibScalar
raisecomTotalMemory = _RaisecomTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 3, 1),
    _RaisecomTotalMemory_Type()
)
raisecomTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomTotalMemory.setStatus("current")
if mibBuilder.loadTexts:
    raisecomTotalMemory.setUnits("Byte")
_RaisecomAvailableMemory_Type = Integer32
_RaisecomAvailableMemory_Object = MibScalar
raisecomAvailableMemory = _RaisecomAvailableMemory_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 3, 2),
    _RaisecomAvailableMemory_Type()
)
raisecomAvailableMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomAvailableMemory.setStatus("current")
if mibBuilder.loadTexts:
    raisecomAvailableMemory.setUnits("Byte")
_RaisecomMaxUtilmemory_Type = Integer32
_RaisecomMaxUtilmemory_Object = MibScalar
raisecomMaxUtilmemory = _RaisecomMaxUtilmemory_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 3, 3),
    _RaisecomMaxUtilmemory_Type()
)
raisecomMaxUtilmemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomMaxUtilmemory.setStatus("current")
if mibBuilder.loadTexts:
    raisecomMaxUtilmemory.setUnits("percent")
_RaisecomDeviceType_Type = OctetString
_RaisecomDeviceType_Object = MibScalar
raisecomDeviceType = _RaisecomDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 1),
    _RaisecomDeviceType_Type()
)
raisecomDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomDeviceType.setStatus("current")
_RaisecomTemperature_ObjectIdentity = ObjectIdentity
raisecomTemperature = _RaisecomTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 2)
)
_RaisecomTemperatureValue_Type = Integer32
_RaisecomTemperatureValue_Object = MibScalar
raisecomTemperatureValue = _RaisecomTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 2, 1),
    _RaisecomTemperatureValue_Type()
)
raisecomTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomTemperatureValue.setStatus("current")
if mibBuilder.loadTexts:
    raisecomTemperatureValue.setUnits("Celsius ")
_RaisecomTemperatureMin_Type = Integer32
_RaisecomTemperatureMin_Object = MibScalar
raisecomTemperatureMin = _RaisecomTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 2, 2),
    _RaisecomTemperatureMin_Type()
)
raisecomTemperatureMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomTemperatureMin.setStatus("current")
if mibBuilder.loadTexts:
    raisecomTemperatureMin.setUnits("Celsius ")
_RaisecomTemperatureMax_Type = Integer32
_RaisecomTemperatureMax_Object = MibScalar
raisecomTemperatureMax = _RaisecomTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 2, 3),
    _RaisecomTemperatureMax_Type()
)
raisecomTemperatureMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomTemperatureMax.setStatus("current")
if mibBuilder.loadTexts:
    raisecomTemperatureMax.setUnits("Celsius ")
_RaisecomTemperatureTrapEnable_Type = EnableVar
_RaisecomTemperatureTrapEnable_Object = MibScalar
raisecomTemperatureTrapEnable = _RaisecomTemperatureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 2, 4),
    _RaisecomTemperatureTrapEnable_Type()
)
raisecomTemperatureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomTemperatureTrapEnable.setStatus("deprecated")
_RaisecomTemperatureThresholdLow_Type = Integer32
_RaisecomTemperatureThresholdLow_Object = MibScalar
raisecomTemperatureThresholdLow = _RaisecomTemperatureThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 2, 5),
    _RaisecomTemperatureThresholdLow_Type()
)
raisecomTemperatureThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomTemperatureThresholdLow.setStatus("current")
if mibBuilder.loadTexts:
    raisecomTemperatureThresholdLow.setUnits("Celsius ")
_RaisecomTemperatureThresholdHigh_Type = Integer32
_RaisecomTemperatureThresholdHigh_Object = MibScalar
raisecomTemperatureThresholdHigh = _RaisecomTemperatureThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 2, 6),
    _RaisecomTemperatureThresholdHigh_Type()
)
raisecomTemperatureThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomTemperatureThresholdHigh.setStatus("current")
if mibBuilder.loadTexts:
    raisecomTemperatureThresholdHigh.setUnits("Celsius ")
_RaisecomTemperatureTrapTimes_Type = Integer32
_RaisecomTemperatureTrapTimes_Object = MibScalar
raisecomTemperatureTrapTimes = _RaisecomTemperatureTrapTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 2, 7),
    _RaisecomTemperatureTrapTimes_Type()
)
raisecomTemperatureTrapTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomTemperatureTrapTimes.setStatus("current")
_RaisecomTemperatureHighTimes_Type = Integer32
_RaisecomTemperatureHighTimes_Object = MibScalar
raisecomTemperatureHighTimes = _RaisecomTemperatureHighTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 2, 8),
    _RaisecomTemperatureHighTimes_Type()
)
raisecomTemperatureHighTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomTemperatureHighTimes.setStatus("current")
_RaisecomTemperatureLowTimes_Type = Integer32
_RaisecomTemperatureLowTimes_Object = MibScalar
raisecomTemperatureLowTimes = _RaisecomTemperatureLowTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 2, 9),
    _RaisecomTemperatureLowTimes_Type()
)
raisecomTemperatureLowTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomTemperatureLowTimes.setStatus("current")
_RaisecomVolt_ObjectIdentity = ObjectIdentity
raisecomVolt = _RaisecomVolt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 3)
)
_RaisecomVoltTable_Object = MibTable
raisecomVoltTable = _RaisecomVoltTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    raisecomVoltTable.setStatus("current")
_RaisecomVoltEntry_Object = MibTableRow
raisecomVoltEntry = _RaisecomVoltEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 3, 1, 1)
)
raisecomVoltEntry.setIndexNames(
    (0, "RAISECOM-SYSTEM-MIB", "raisecomVoltIndex"),
)
if mibBuilder.loadTexts:
    raisecomVoltEntry.setStatus("current")
_RaisecomVoltIndex_Type = Integer32
_RaisecomVoltIndex_Object = MibTableColumn
raisecomVoltIndex = _RaisecomVoltIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 3, 1, 1, 1),
    _RaisecomVoltIndex_Type()
)
raisecomVoltIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomVoltIndex.setStatus("current")
_RaisecomVoltReference_Type = Integer32
_RaisecomVoltReference_Object = MibTableColumn
raisecomVoltReference = _RaisecomVoltReference_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 3, 1, 1, 2),
    _RaisecomVoltReference_Type()
)
raisecomVoltReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomVoltReference.setStatus("current")
if mibBuilder.loadTexts:
    raisecomVoltReference.setUnits("mV")
_RaisecomVoltValue_Type = Integer32
_RaisecomVoltValue_Object = MibTableColumn
raisecomVoltValue = _RaisecomVoltValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 3, 1, 1, 3),
    _RaisecomVoltValue_Type()
)
raisecomVoltValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomVoltValue.setStatus("current")
if mibBuilder.loadTexts:
    raisecomVoltValue.setUnits("mV")
_RaisecomVoltMin_Type = Integer32
_RaisecomVoltMin_Object = MibTableColumn
raisecomVoltMin = _RaisecomVoltMin_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 3, 1, 1, 4),
    _RaisecomVoltMin_Type()
)
raisecomVoltMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomVoltMin.setStatus("current")
if mibBuilder.loadTexts:
    raisecomVoltMin.setUnits("mV")
_RaisecomVoltMax_Type = Integer32
_RaisecomVoltMax_Object = MibTableColumn
raisecomVoltMax = _RaisecomVoltMax_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 3, 1, 1, 5),
    _RaisecomVoltMax_Type()
)
raisecomVoltMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomVoltMax.setStatus("current")
if mibBuilder.loadTexts:
    raisecomVoltMax.setUnits("mV")
_RaisecomVoltTrapEnable_Type = EnableVar
_RaisecomVoltTrapEnable_Object = MibTableColumn
raisecomVoltTrapEnable = _RaisecomVoltTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 3, 1, 1, 6),
    _RaisecomVoltTrapEnable_Type()
)
raisecomVoltTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomVoltTrapEnable.setStatus("deprecated")
_RaisecomVoltThresholdLow_Type = Integer32
_RaisecomVoltThresholdLow_Object = MibTableColumn
raisecomVoltThresholdLow = _RaisecomVoltThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 3, 1, 1, 7),
    _RaisecomVoltThresholdLow_Type()
)
raisecomVoltThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomVoltThresholdLow.setStatus("current")
if mibBuilder.loadTexts:
    raisecomVoltThresholdLow.setUnits("mV")
_RaisecomVoltThresholdHigh_Type = Integer32
_RaisecomVoltThresholdHigh_Object = MibTableColumn
raisecomVoltThresholdHigh = _RaisecomVoltThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 3, 1, 1, 8),
    _RaisecomVoltThresholdHigh_Type()
)
raisecomVoltThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomVoltThresholdHigh.setStatus("current")
if mibBuilder.loadTexts:
    raisecomVoltThresholdHigh.setUnits("mV")
_RaisecomVoltTrapTimes_Type = Integer32
_RaisecomVoltTrapTimes_Object = MibTableColumn
raisecomVoltTrapTimes = _RaisecomVoltTrapTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 3, 1, 1, 9),
    _RaisecomVoltTrapTimes_Type()
)
raisecomVoltTrapTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomVoltTrapTimes.setStatus("current")
_RaisecomVoltHighTimes_Type = Integer32
_RaisecomVoltHighTimes_Object = MibTableColumn
raisecomVoltHighTimes = _RaisecomVoltHighTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 3, 1, 1, 10),
    _RaisecomVoltHighTimes_Type()
)
raisecomVoltHighTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomVoltHighTimes.setStatus("current")
_RaisecomVoltLowTimes_Type = Integer32
_RaisecomVoltLowTimes_Object = MibTableColumn
raisecomVoltLowTimes = _RaisecomVoltLowTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 3, 1, 1, 11),
    _RaisecomVoltLowTimes_Type()
)
raisecomVoltLowTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomVoltLowTimes.setStatus("current")
_RaisecomInformationTrap_ObjectIdentity = ObjectIdentity
raisecomInformationTrap = _RaisecomInformationTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 4)
)
_RaisecomAlarm_ObjectIdentity = ObjectIdentity
raisecomAlarm = _RaisecomAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5)
)
_RaisecomAlarmTrap_ObjectIdentity = ObjectIdentity
raisecomAlarmTrap = _RaisecomAlarmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 1)
)
_RaisecomAlarmGlobal_ObjectIdentity = ObjectIdentity
raisecomAlarmGlobal = _RaisecomAlarmGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 2)
)


class _RaisecomAlarmTrapEnable_Type(EnableVar):
    """Custom type raisecomAlarmTrapEnable based on EnableVar"""
    defaultValue = 2


_RaisecomAlarmTrapEnable_Type.__name__ = "EnableVar"
_RaisecomAlarmTrapEnable_Object = MibScalar
raisecomAlarmTrapEnable = _RaisecomAlarmTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 2, 1),
    _RaisecomAlarmTrapEnable_Type()
)
raisecomAlarmTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmTrapEnable.setStatus("current")


class _RaisecomAlarmSyslogEnable_Type(EnableVar):
    """Custom type raisecomAlarmSyslogEnable based on EnableVar"""
    defaultValue = 2


_RaisecomAlarmSyslogEnable_Type.__name__ = "EnableVar"
_RaisecomAlarmSyslogEnable_Object = MibScalar
raisecomAlarmSyslogEnable = _RaisecomAlarmSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 2, 2),
    _RaisecomAlarmSyslogEnable_Type()
)
raisecomAlarmSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmSyslogEnable.setStatus("current")
_RaisecomAlarmClear_Type = TruthValue
_RaisecomAlarmClear_Object = MibScalar
raisecomAlarmClear = _RaisecomAlarmClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 2, 3),
    _RaisecomAlarmClear_Type()
)
raisecomAlarmClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmClear.setStatus("current")
_RaisecomAlarmHwmonitorPeriod_Type = Integer32
_RaisecomAlarmHwmonitorPeriod_Object = MibScalar
raisecomAlarmHwmonitorPeriod = _RaisecomAlarmHwmonitorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 2, 4),
    _RaisecomAlarmHwmonitorPeriod_Type()
)
raisecomAlarmHwmonitorPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmHwmonitorPeriod.setStatus("current")
_RaisecomAlarmPower_ObjectIdentity = ObjectIdentity
raisecomAlarmPower = _RaisecomAlarmPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 3)
)


class _RaisecomAlarmPowerTrapEnable_Type(EnableVar):
    """Custom type raisecomAlarmPowerTrapEnable based on EnableVar"""
    defaultValue = 1


_RaisecomAlarmPowerTrapEnable_Type.__name__ = "EnableVar"
_RaisecomAlarmPowerTrapEnable_Object = MibScalar
raisecomAlarmPowerTrapEnable = _RaisecomAlarmPowerTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 3, 1),
    _RaisecomAlarmPowerTrapEnable_Type()
)
raisecomAlarmPowerTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmPowerTrapEnable.setStatus("current")


class _RaisecomAlarmPowerRelayEnable_Type(EnableVar):
    """Custom type raisecomAlarmPowerRelayEnable based on EnableVar"""
    defaultValue = 1


_RaisecomAlarmPowerRelayEnable_Type.__name__ = "EnableVar"
_RaisecomAlarmPowerRelayEnable_Object = MibScalar
raisecomAlarmPowerRelayEnable = _RaisecomAlarmPowerRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 3, 2),
    _RaisecomAlarmPowerRelayEnable_Type()
)
raisecomAlarmPowerRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmPowerRelayEnable.setStatus("current")


class _RaisecomAlarmPowerSyslogEnable_Type(EnableVar):
    """Custom type raisecomAlarmPowerSyslogEnable based on EnableVar"""
    defaultValue = 1


_RaisecomAlarmPowerSyslogEnable_Type.__name__ = "EnableVar"
_RaisecomAlarmPowerSyslogEnable_Object = MibScalar
raisecomAlarmPowerSyslogEnable = _RaisecomAlarmPowerSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 3, 3),
    _RaisecomAlarmPowerSyslogEnable_Type()
)
raisecomAlarmPowerSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmPowerSyslogEnable.setStatus("current")
_RaisecomAlarmPowerOneTimes_Type = Integer32
_RaisecomAlarmPowerOneTimes_Object = MibScalar
raisecomAlarmPowerOneTimes = _RaisecomAlarmPowerOneTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 3, 4),
    _RaisecomAlarmPowerOneTimes_Type()
)
raisecomAlarmPowerOneTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomAlarmPowerOneTimes.setStatus("current")
_RaisecomAlarmPowerTwoTimes_Type = Integer32
_RaisecomAlarmPowerTwoTimes_Object = MibScalar
raisecomAlarmPowerTwoTimes = _RaisecomAlarmPowerTwoTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 3, 5),
    _RaisecomAlarmPowerTwoTimes_Type()
)
raisecomAlarmPowerTwoTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomAlarmPowerTwoTimes.setStatus("current")


class _RaisecomAlarmPowerStatus_Type(Integer32):
    """Custom type raisecomAlarmPowerStatus based on Integer32"""
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
        *(("dual-power-on", 1),
          ("dual-power-off", 2),
          ("power1-off", 3),
          ("power2-off", 4))
    )


_RaisecomAlarmPowerStatus_Type.__name__ = "Integer32"
_RaisecomAlarmPowerStatus_Object = MibScalar
raisecomAlarmPowerStatus = _RaisecomAlarmPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 3, 6),
    _RaisecomAlarmPowerStatus_Type()
)
raisecomAlarmPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomAlarmPowerStatus.setStatus("current")
_RaisecomAlarmTemperature_ObjectIdentity = ObjectIdentity
raisecomAlarmTemperature = _RaisecomAlarmTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 4)
)


class _RaisecomAlarmTemperatureTrapEnable_Type(EnableVar):
    """Custom type raisecomAlarmTemperatureTrapEnable based on EnableVar"""
    defaultValue = 1


_RaisecomAlarmTemperatureTrapEnable_Type.__name__ = "EnableVar"
_RaisecomAlarmTemperatureTrapEnable_Object = MibScalar
raisecomAlarmTemperatureTrapEnable = _RaisecomAlarmTemperatureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 4, 1),
    _RaisecomAlarmTemperatureTrapEnable_Type()
)
raisecomAlarmTemperatureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmTemperatureTrapEnable.setStatus("current")


class _RaisecomAlarmTemperatureRelayEnable_Type(EnableVar):
    """Custom type raisecomAlarmTemperatureRelayEnable based on EnableVar"""
    defaultValue = 1


_RaisecomAlarmTemperatureRelayEnable_Type.__name__ = "EnableVar"
_RaisecomAlarmTemperatureRelayEnable_Object = MibScalar
raisecomAlarmTemperatureRelayEnable = _RaisecomAlarmTemperatureRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 4, 2),
    _RaisecomAlarmTemperatureRelayEnable_Type()
)
raisecomAlarmTemperatureRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmTemperatureRelayEnable.setStatus("current")


class _RaisecomAlarmTemperatureSyslogEnable_Type(EnableVar):
    """Custom type raisecomAlarmTemperatureSyslogEnable based on EnableVar"""
    defaultValue = 1


_RaisecomAlarmTemperatureSyslogEnable_Type.__name__ = "EnableVar"
_RaisecomAlarmTemperatureSyslogEnable_Object = MibScalar
raisecomAlarmTemperatureSyslogEnable = _RaisecomAlarmTemperatureSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 4, 3),
    _RaisecomAlarmTemperatureSyslogEnable_Type()
)
raisecomAlarmTemperatureSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmTemperatureSyslogEnable.setStatus("current")
_RaisecomAlarmVoltage_ObjectIdentity = ObjectIdentity
raisecomAlarmVoltage = _RaisecomAlarmVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 5)
)


class _RaisecomAlarmVoltTrapEnable_Type(EnableVar):
    """Custom type raisecomAlarmVoltTrapEnable based on EnableVar"""
    defaultValue = 1


_RaisecomAlarmVoltTrapEnable_Type.__name__ = "EnableVar"
_RaisecomAlarmVoltTrapEnable_Object = MibScalar
raisecomAlarmVoltTrapEnable = _RaisecomAlarmVoltTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 5, 1),
    _RaisecomAlarmVoltTrapEnable_Type()
)
raisecomAlarmVoltTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmVoltTrapEnable.setStatus("current")


class _RaisecomAlarmVoltRelayEnable_Type(EnableVar):
    """Custom type raisecomAlarmVoltRelayEnable based on EnableVar"""
    defaultValue = 1


_RaisecomAlarmVoltRelayEnable_Type.__name__ = "EnableVar"
_RaisecomAlarmVoltRelayEnable_Object = MibScalar
raisecomAlarmVoltRelayEnable = _RaisecomAlarmVoltRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 5, 2),
    _RaisecomAlarmVoltRelayEnable_Type()
)
raisecomAlarmVoltRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmVoltRelayEnable.setStatus("current")


class _RaisecomAlarmVoltSyslogEnable_Type(EnableVar):
    """Custom type raisecomAlarmVoltSyslogEnable based on EnableVar"""
    defaultValue = 1


_RaisecomAlarmVoltSyslogEnable_Type.__name__ = "EnableVar"
_RaisecomAlarmVoltSyslogEnable_Object = MibScalar
raisecomAlarmVoltSyslogEnable = _RaisecomAlarmVoltSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 5, 3),
    _RaisecomAlarmVoltSyslogEnable_Type()
)
raisecomAlarmVoltSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmVoltSyslogEnable.setStatus("current")
_RaisecomAlarmPort_ObjectIdentity = ObjectIdentity
raisecomAlarmPort = _RaisecomAlarmPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 6)
)
_RaisecomAlarmPortTable_Object = MibTable
raisecomAlarmPortTable = _RaisecomAlarmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 6, 1)
)
if mibBuilder.loadTexts:
    raisecomAlarmPortTable.setStatus("current")
_RaisecomAlarmPortEntry_Object = MibTableRow
raisecomAlarmPortEntry = _RaisecomAlarmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 6, 1, 1)
)
raisecomAlarmPortEntry.setIndexNames(
    (0, "RAISECOM-SYSTEM-MIB", "raisecomAlarmPortIndex"),
)
if mibBuilder.loadTexts:
    raisecomAlarmPortEntry.setStatus("current")
_RaisecomAlarmPortIndex_Type = Integer32
_RaisecomAlarmPortIndex_Object = MibTableColumn
raisecomAlarmPortIndex = _RaisecomAlarmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 6, 1, 1, 1),
    _RaisecomAlarmPortIndex_Type()
)
raisecomAlarmPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomAlarmPortIndex.setStatus("current")
_RaisecomAlarmPortSyslogEvList_Type = PortAlarmEventList
_RaisecomAlarmPortSyslogEvList_Object = MibTableColumn
raisecomAlarmPortSyslogEvList = _RaisecomAlarmPortSyslogEvList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 6, 1, 1, 2),
    _RaisecomAlarmPortSyslogEvList_Type()
)
raisecomAlarmPortSyslogEvList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmPortSyslogEvList.setStatus("current")
_RaisecomAlarmPortNotifiesEvList_Type = PortAlarmEventList
_RaisecomAlarmPortNotifiesEvList_Object = MibTableColumn
raisecomAlarmPortNotifiesEvList = _RaisecomAlarmPortNotifiesEvList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 6, 1, 1, 3),
    _RaisecomAlarmPortNotifiesEvList_Type()
)
raisecomAlarmPortNotifiesEvList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmPortNotifiesEvList.setStatus("current")
_RaisecomAlarmPortRelayEvList_Type = PortAlarmEventList
_RaisecomAlarmPortRelayEvList_Object = MibTableColumn
raisecomAlarmPortRelayEvList = _RaisecomAlarmPortRelayEvList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 6, 1, 1, 4),
    _RaisecomAlarmPortRelayEvList_Type()
)
raisecomAlarmPortRelayEvList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmPortRelayEvList.setStatus("current")
_RaisecomAlarmPortEvList_Type = PortAlarmEventList
_RaisecomAlarmPortEvList_Object = MibTableColumn
raisecomAlarmPortEvList = _RaisecomAlarmPortEvList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 6, 1, 1, 5),
    _RaisecomAlarmPortEvList_Type()
)
raisecomAlarmPortEvList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomAlarmPortEvList.setStatus("current")
_RaisecomAlarmHistory_ObjectIdentity = ObjectIdentity
raisecomAlarmHistory = _RaisecomAlarmHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 7)
)
_RaisecomAlarmHistTable_Object = MibTable
raisecomAlarmHistTable = _RaisecomAlarmHistTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 7, 1)
)
if mibBuilder.loadTexts:
    raisecomAlarmHistTable.setStatus("current")
_RaisecomAlarmHistEntry_Object = MibTableRow
raisecomAlarmHistEntry = _RaisecomAlarmHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 7, 1, 1)
)
raisecomAlarmHistEntry.setIndexNames(
    (0, "RAISECOM-SYSTEM-MIB", "raisecomAlarmHistIndex"),
)
if mibBuilder.loadTexts:
    raisecomAlarmHistEntry.setStatus("current")
_RaisecomAlarmHistIndex_Type = Integer32
_RaisecomAlarmHistIndex_Object = MibTableColumn
raisecomAlarmHistIndex = _RaisecomAlarmHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 7, 1, 1, 1),
    _RaisecomAlarmHistIndex_Type()
)
raisecomAlarmHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomAlarmHistIndex.setStatus("current")


class _RaisecomAlarmHistStatus_Type(Integer32):
    """Custom type raisecomAlarmHistStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asserted", 1),
          ("cleared", 2),
          ("clearall", 3))
    )


_RaisecomAlarmHistStatus_Type.__name__ = "Integer32"
_RaisecomAlarmHistStatus_Object = MibTableColumn
raisecomAlarmHistStatus = _RaisecomAlarmHistStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 7, 1, 1, 2),
    _RaisecomAlarmHistStatus_Type()
)
raisecomAlarmHistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomAlarmHistStatus.setStatus("deprecated")
_RaisecomAlarmHistSource_Type = Integer32
_RaisecomAlarmHistSource_Object = MibTableColumn
raisecomAlarmHistSource = _RaisecomAlarmHistSource_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 7, 1, 1, 3),
    _RaisecomAlarmHistSource_Type()
)
raisecomAlarmHistSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomAlarmHistSource.setStatus("current")


class _RaisecomAlarmHistDescr_Type(OctetString):
    """Custom type raisecomAlarmHistDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RaisecomAlarmHistDescr_Type.__name__ = "OctetString"
_RaisecomAlarmHistDescr_Object = MibTableColumn
raisecomAlarmHistDescr = _RaisecomAlarmHistDescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 7, 1, 1, 4),
    _RaisecomAlarmHistDescr_Type()
)
raisecomAlarmHistDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomAlarmHistDescr.setStatus("current")
_RaisecomAlarmHistTimestamp_Type = Integer32
_RaisecomAlarmHistTimestamp_Object = MibTableColumn
raisecomAlarmHistTimestamp = _RaisecomAlarmHistTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 7, 1, 1, 5),
    _RaisecomAlarmHistTimestamp_Type()
)
raisecomAlarmHistTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomAlarmHistTimestamp.setStatus("current")


class _RaisecomAlarmHistType_Type(Integer32):
    """Custom type raisecomAlarmHistType based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("dev-power-down", 0),
          ("power-abnormal", 1),
          ("high-temperature", 2),
          ("low-temperature", 3),
          ("high-volt", 4),
          ("low-volt", 5),
          ("link-down", 6),
          ("link-falut", 7),
          ("not-forward", 8),
          ("power-normal", 9),
          ("normal-temperature", 10),
          ("normal-volt", 11),
          ("link-up", 12),
          ("link-ok", 13),
          ("forward", 14),
          ("all-alarm", 15))
    )


_RaisecomAlarmHistType_Type.__name__ = "Integer32"
_RaisecomAlarmHistType_Object = MibTableColumn
raisecomAlarmHistType = _RaisecomAlarmHistType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 7, 1, 1, 6),
    _RaisecomAlarmHistType_Type()
)
raisecomAlarmHistType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomAlarmHistType.setStatus("current")
_RaisecomAlarmCurrent_ObjectIdentity = ObjectIdentity
raisecomAlarmCurrent = _RaisecomAlarmCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 8)
)
_RaisecomAlarmCurtTable_Object = MibTable
raisecomAlarmCurtTable = _RaisecomAlarmCurtTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 8, 1)
)
if mibBuilder.loadTexts:
    raisecomAlarmCurtTable.setStatus("current")
_RaisecomAlarmCurtEntry_Object = MibTableRow
raisecomAlarmCurtEntry = _RaisecomAlarmCurtEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 8, 1, 1)
)
raisecomAlarmCurtEntry.setIndexNames(
    (0, "RAISECOM-SYSTEM-MIB", "raisecomAlarmCurtIndex"),
)
if mibBuilder.loadTexts:
    raisecomAlarmCurtEntry.setStatus("current")
_RaisecomAlarmCurtIndex_Type = Integer32
_RaisecomAlarmCurtIndex_Object = MibTableColumn
raisecomAlarmCurtIndex = _RaisecomAlarmCurtIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 8, 1, 1, 1),
    _RaisecomAlarmCurtIndex_Type()
)
raisecomAlarmCurtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomAlarmCurtIndex.setStatus("current")
_RaisecomAlarmCurtSource_Type = Integer32
_RaisecomAlarmCurtSource_Object = MibTableColumn
raisecomAlarmCurtSource = _RaisecomAlarmCurtSource_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 8, 1, 1, 2),
    _RaisecomAlarmCurtSource_Type()
)
raisecomAlarmCurtSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomAlarmCurtSource.setStatus("current")


class _RaisecomAlarmCurtDescr_Type(OctetString):
    """Custom type raisecomAlarmCurtDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RaisecomAlarmCurtDescr_Type.__name__ = "OctetString"
_RaisecomAlarmCurtDescr_Object = MibTableColumn
raisecomAlarmCurtDescr = _RaisecomAlarmCurtDescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 8, 1, 1, 3),
    _RaisecomAlarmCurtDescr_Type()
)
raisecomAlarmCurtDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomAlarmCurtDescr.setStatus("current")
_RaisecomAlarmCurtTimestamp_Type = Integer32
_RaisecomAlarmCurtTimestamp_Object = MibTableColumn
raisecomAlarmCurtTimestamp = _RaisecomAlarmCurtTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 8, 1, 1, 4),
    _RaisecomAlarmCurtTimestamp_Type()
)
raisecomAlarmCurtTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomAlarmCurtTimestamp.setStatus("current")


class _RaisecomAlarmCurtType_Type(Integer32):
    """Custom type raisecomAlarmCurtType based on Integer32"""
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
        *(("dev-power-down", 0),
          ("power-abnormal", 1),
          ("high-temperature", 2),
          ("low-temperature", 3),
          ("high-volt", 4),
          ("low-volt", 5),
          ("link-down", 6),
          ("link-falut", 7),
          ("not-forward", 8))
    )


_RaisecomAlarmCurtType_Type.__name__ = "Integer32"
_RaisecomAlarmCurtType_Object = MibTableColumn
raisecomAlarmCurtType = _RaisecomAlarmCurtType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 8, 1, 1, 5),
    _RaisecomAlarmCurtType_Type()
)
raisecomAlarmCurtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomAlarmCurtType.setStatus("current")

# Managed Objects groups


# Notification objects

raisecomCPURisingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 3, 1)
)
raisecomCPURisingThreshold.setObjects(
      *(("RAISECOM-SYSTEM-MIB", "raisecomProcessIndex"),
        ("RAISECOM-SYSTEM-MIB", "raisecomProcessUtilization"),
        ("RAISECOM-SYSTEM-MIB", "raisecomCPUUtilization"))
)
if mibBuilder.loadTexts:
    raisecomCPURisingThreshold.setStatus(
        "current"
    )

raisecomCPUFallingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 1, 3, 2)
)
raisecomCPUFallingThreshold.setObjects(
    ("RAISECOM-SYSTEM-MIB", "raisecomCPUUtilization")
)
if mibBuilder.loadTexts:
    raisecomCPUFallingThreshold.setStatus(
        "current"
    )

temperatureAbnormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 4, 1)
)
temperatureAbnormalTrap.setObjects(
    ("RAISECOM-SYSTEM-MIB", "raisecomTemperatureValue")
)
if mibBuilder.loadTexts:
    temperatureAbnormalTrap.setStatus(
        "deprecated"
    )

temperatureNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 4, 2)
)
temperatureNormalTrap.setObjects(
    ("RAISECOM-SYSTEM-MIB", "raisecomTemperatureValue")
)
if mibBuilder.loadTexts:
    temperatureNormalTrap.setStatus(
        "deprecated"
    )

raisecomVoltAbnormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 4, 3)
)
raisecomVoltAbnormalTrap.setObjects(
      *(("RAISECOM-SYSTEM-MIB", "raisecomVoltIndex"),
        ("RAISECOM-SYSTEM-MIB", "raisecomVoltReference"),
        ("RAISECOM-SYSTEM-MIB", "raisecomVoltValue"))
)
if mibBuilder.loadTexts:
    raisecomVoltAbnormalTrap.setStatus(
        "deprecated"
    )

raisecomVoltNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 4, 4)
)
raisecomVoltNormalTrap.setObjects(
      *(("RAISECOM-SYSTEM-MIB", "raisecomVoltIndex"),
        ("RAISECOM-SYSTEM-MIB", "raisecomVoltReference"),
        ("RAISECOM-SYSTEM-MIB", "raisecomVoltValue"))
)
if mibBuilder.loadTexts:
    raisecomVoltNormalTrap.setStatus(
        "deprecated"
    )

raisecomAlarmInformationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 1, 4, 5, 1, 1)
)
raisecomAlarmInformationTrap.setObjects(
      *(("RAISECOM-SYSTEM-MIB", "raisecomAlarmHistSource"),
        ("RAISECOM-SYSTEM-MIB", "raisecomAlarmHistDescr"),
        ("RAISECOM-SYSTEM-MIB", "raisecomAlarmHistTimestamp"),
        ("RAISECOM-SYSTEM-MIB", "raisecomAlarmHistType"))
)
if mibBuilder.loadTexts:
    raisecomAlarmInformationTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-SYSTEM-MIB",
    **{"ProcessStatus": ProcessStatus,
       "CPUTimeStamp": CPUTimeStamp,
       "PortAlarmEventList": PortAlarmEventList,
       "raisecomSystem": raisecomSystem,
       "raisecomCpu": raisecomCpu,
       "raisecomCpuBusy1Per": raisecomCpuBusy1Per,
       "raisecomCpuBusy60Per": raisecomCpuBusy60Per,
       "raisecomCPUTrapGroup": raisecomCPUTrapGroup,
       "raisecomCPURisingThreshold": raisecomCPURisingThreshold,
       "raisecomCPUFallingThreshold": raisecomCPUFallingThreshold,
       "raisecomCPUScalarGroup": raisecomCPUScalarGroup,
       "raisecomCPUUtilizationTotal": raisecomCPUUtilizationTotal,
       "raisecomCPUHistoryTableSize": raisecomCPUHistoryTableSize,
       "raisecomCPUThresholdTrapEnable": raisecomCPUThresholdTrapEnable,
       "raisecomCPURisingThresholdValue": raisecomCPURisingThresholdValue,
       "raisecomCPUFallingThresholdValue": raisecomCPUFallingThresholdValue,
       "raisecomCPUThresholdInterval": raisecomCPUThresholdInterval,
       "raisecomCpuTotalProcNum": raisecomCpuTotalProcNum,
       "raisecomCPUTrapUtilization": raisecomCPUTrapUtilization,
       "raisecomCPUTableGroup": raisecomCPUTableGroup,
       "raisecomCPUUtilizationGroup": raisecomCPUUtilizationGroup,
       "raisecomCPUUtilizationTable": raisecomCPUUtilizationTable,
       "raisecomCPUUtilizationEntry": raisecomCPUUtilizationEntry,
       "raisecomCPUUtilizationIndex": raisecomCPUUtilizationIndex,
       "raisecomCPUUtilizationPeriod": raisecomCPUUtilizationPeriod,
       "raisecomCPUUtilization": raisecomCPUUtilization,
       "raisecomCPUHistoryTable": raisecomCPUHistoryTable,
       "raisecomCPUHistoryEntry": raisecomCPUHistoryEntry,
       "raisecomCPUHistoryPeriod": raisecomCPUHistoryPeriod,
       "raisecomCPUHistoryIndex": raisecomCPUHistoryIndex,
       "raisecomCPUHistoryTotalUtil": raisecomCPUHistoryTotalUtil,
       "raisecomCPUProcessesGroup": raisecomCPUProcessesGroup,
       "raisecomProcessesTable": raisecomProcessesTable,
       "raisecomProcessesEntry": raisecomProcessesEntry,
       "raisecomProcessIndex": raisecomProcessIndex,
       "raisecomProcessPID": raisecomProcessPID,
       "raisecomProcessName": raisecomProcessName,
       "raisecomProcessRunTimeTotal": raisecomProcessRunTimeTotal,
       "raisecomProcessInvokedTotal": raisecomProcessInvokedTotal,
       "raisecomProcessTimeCreated": raisecomProcessTimeCreated,
       "raisecomProcessNormalPriority": raisecomProcessNormalPriority,
       "raisecomProcessCurrentPriority": raisecomProcessCurrentPriority,
       "raisecomProcessStatus": raisecomProcessStatus,
       "raisecomProcessErrorNo": raisecomProcessErrorNo,
       "raisecomProcessStackSize": raisecomProcessStackSize,
       "raisecomProcessStackCurrentSize": raisecomProcessStackCurrentSize,
       "raisecomProcessStackMaxSize": raisecomProcessStackMaxSize,
       "raisecomProcessStackBegin": raisecomProcessStackBegin,
       "raisecomProcessStackPointer": raisecomProcessStackPointer,
       "raisecomProcessStackEnd": raisecomProcessStackEnd,
       "raisecomProcessProgramCounter": raisecomProcessProgramCounter,
       "raisecomProcessEntry": raisecomProcessEntry,
       "raisecomProcessSemWait": raisecomProcessSemWait,
       "raisecomProcessDelay": raisecomProcessDelay,
       "raisecomProcessStatisticsTable": raisecomProcessStatisticsTable,
       "raisecomProcessStatisticsEntry": raisecomProcessStatisticsEntry,
       "raisecomProcessStatisticsPeriod": raisecomProcessStatisticsPeriod,
       "raisecomProcessRunTime": raisecomProcessRunTime,
       "raisecomProcessInvoked": raisecomProcessInvoked,
       "raisecomProcessUtilization": raisecomProcessUtilization,
       "raisecomDeadProcessesTable": raisecomDeadProcessesTable,
       "raisecomDeadProcessesEntry": raisecomDeadProcessesEntry,
       "raisecomDeadProcessIndex": raisecomDeadProcessIndex,
       "raisecomDeadProcessName": raisecomDeadProcessName,
       "raisecomDeadProcessEntry": raisecomDeadProcessEntry,
       "raisecomDeadProcessErrorNo": raisecomDeadProcessErrorNo,
       "raisecomDeadProcessPriority": raisecomDeadProcessPriority,
       "raisecomDeadProcessMaxStackSize": raisecomDeadProcessMaxStackSize,
       "raisecomDeadProcessTimeDelete": raisecomDeadProcessTimeDelete,
       "raisecomDeadProcessDeadTimes": raisecomDeadProcessDeadTimes,
       "raisecomDeadProcessStatus": raisecomDeadProcessStatus,
       "raisecomEndPool": raisecomEndPool,
       "raisecomEndPoolTable": raisecomEndPoolTable,
       "raisecomEndPoolEntry": raisecomEndPoolEntry,
       "raisecomBasePort": raisecomBasePort,
       "raisecomTotalEndPool": raisecomTotalEndPool,
       "raisecomFreeEndPool": raisecomFreeEndPool,
       "raisecomMemory": raisecomMemory,
       "raisecomTotalMemory": raisecomTotalMemory,
       "raisecomAvailableMemory": raisecomAvailableMemory,
       "raisecomMaxUtilmemory": raisecomMaxUtilmemory,
       "raisecomInformation": raisecomInformation,
       "raisecomDeviceType": raisecomDeviceType,
       "raisecomTemperature": raisecomTemperature,
       "raisecomTemperatureValue": raisecomTemperatureValue,
       "raisecomTemperatureMin": raisecomTemperatureMin,
       "raisecomTemperatureMax": raisecomTemperatureMax,
       "raisecomTemperatureTrapEnable": raisecomTemperatureTrapEnable,
       "raisecomTemperatureThresholdLow": raisecomTemperatureThresholdLow,
       "raisecomTemperatureThresholdHigh": raisecomTemperatureThresholdHigh,
       "raisecomTemperatureTrapTimes": raisecomTemperatureTrapTimes,
       "raisecomTemperatureHighTimes": raisecomTemperatureHighTimes,
       "raisecomTemperatureLowTimes": raisecomTemperatureLowTimes,
       "raisecomVolt": raisecomVolt,
       "raisecomVoltTable": raisecomVoltTable,
       "raisecomVoltEntry": raisecomVoltEntry,
       "raisecomVoltIndex": raisecomVoltIndex,
       "raisecomVoltReference": raisecomVoltReference,
       "raisecomVoltValue": raisecomVoltValue,
       "raisecomVoltMin": raisecomVoltMin,
       "raisecomVoltMax": raisecomVoltMax,
       "raisecomVoltTrapEnable": raisecomVoltTrapEnable,
       "raisecomVoltThresholdLow": raisecomVoltThresholdLow,
       "raisecomVoltThresholdHigh": raisecomVoltThresholdHigh,
       "raisecomVoltTrapTimes": raisecomVoltTrapTimes,
       "raisecomVoltHighTimes": raisecomVoltHighTimes,
       "raisecomVoltLowTimes": raisecomVoltLowTimes,
       "raisecomInformationTrap": raisecomInformationTrap,
       "temperatureAbnormalTrap": temperatureAbnormalTrap,
       "temperatureNormalTrap": temperatureNormalTrap,
       "raisecomVoltAbnormalTrap": raisecomVoltAbnormalTrap,
       "raisecomVoltNormalTrap": raisecomVoltNormalTrap,
       "raisecomAlarm": raisecomAlarm,
       "raisecomAlarmTrap": raisecomAlarmTrap,
       "raisecomAlarmInformationTrap": raisecomAlarmInformationTrap,
       "raisecomAlarmGlobal": raisecomAlarmGlobal,
       "raisecomAlarmTrapEnable": raisecomAlarmTrapEnable,
       "raisecomAlarmSyslogEnable": raisecomAlarmSyslogEnable,
       "raisecomAlarmClear": raisecomAlarmClear,
       "raisecomAlarmHwmonitorPeriod": raisecomAlarmHwmonitorPeriod,
       "raisecomAlarmPower": raisecomAlarmPower,
       "raisecomAlarmPowerTrapEnable": raisecomAlarmPowerTrapEnable,
       "raisecomAlarmPowerRelayEnable": raisecomAlarmPowerRelayEnable,
       "raisecomAlarmPowerSyslogEnable": raisecomAlarmPowerSyslogEnable,
       "raisecomAlarmPowerOneTimes": raisecomAlarmPowerOneTimes,
       "raisecomAlarmPowerTwoTimes": raisecomAlarmPowerTwoTimes,
       "raisecomAlarmPowerStatus": raisecomAlarmPowerStatus,
       "raisecomAlarmTemperature": raisecomAlarmTemperature,
       "raisecomAlarmTemperatureTrapEnable": raisecomAlarmTemperatureTrapEnable,
       "raisecomAlarmTemperatureRelayEnable": raisecomAlarmTemperatureRelayEnable,
       "raisecomAlarmTemperatureSyslogEnable": raisecomAlarmTemperatureSyslogEnable,
       "raisecomAlarmVoltage": raisecomAlarmVoltage,
       "raisecomAlarmVoltTrapEnable": raisecomAlarmVoltTrapEnable,
       "raisecomAlarmVoltRelayEnable": raisecomAlarmVoltRelayEnable,
       "raisecomAlarmVoltSyslogEnable": raisecomAlarmVoltSyslogEnable,
       "raisecomAlarmPort": raisecomAlarmPort,
       "raisecomAlarmPortTable": raisecomAlarmPortTable,
       "raisecomAlarmPortEntry": raisecomAlarmPortEntry,
       "raisecomAlarmPortIndex": raisecomAlarmPortIndex,
       "raisecomAlarmPortSyslogEvList": raisecomAlarmPortSyslogEvList,
       "raisecomAlarmPortNotifiesEvList": raisecomAlarmPortNotifiesEvList,
       "raisecomAlarmPortRelayEvList": raisecomAlarmPortRelayEvList,
       "raisecomAlarmPortEvList": raisecomAlarmPortEvList,
       "raisecomAlarmHistory": raisecomAlarmHistory,
       "raisecomAlarmHistTable": raisecomAlarmHistTable,
       "raisecomAlarmHistEntry": raisecomAlarmHistEntry,
       "raisecomAlarmHistIndex": raisecomAlarmHistIndex,
       "raisecomAlarmHistStatus": raisecomAlarmHistStatus,
       "raisecomAlarmHistSource": raisecomAlarmHistSource,
       "raisecomAlarmHistDescr": raisecomAlarmHistDescr,
       "raisecomAlarmHistTimestamp": raisecomAlarmHistTimestamp,
       "raisecomAlarmHistType": raisecomAlarmHistType,
       "raisecomAlarmCurrent": raisecomAlarmCurrent,
       "raisecomAlarmCurtTable": raisecomAlarmCurtTable,
       "raisecomAlarmCurtEntry": raisecomAlarmCurtEntry,
       "raisecomAlarmCurtIndex": raisecomAlarmCurtIndex,
       "raisecomAlarmCurtSource": raisecomAlarmCurtSource,
       "raisecomAlarmCurtDescr": raisecomAlarmCurtDescr,
       "raisecomAlarmCurtTimestamp": raisecomAlarmCurtTimestamp,
       "raisecomAlarmCurtType": raisecomAlarmCurtType}
)
