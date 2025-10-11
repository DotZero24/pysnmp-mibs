# SNMP MIB module (DMOS-SYSMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/datacom/DMOS-SYSMON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:04:49 2025
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

(datacomDevicesMIBs,) = mibBuilder.importSymbols(
    "DATACOM-SMI",
    "datacomDevicesMIBs")

(Unsigned8,
 UnsignedPercent) = mibBuilder.importSymbols(
    "DMOS-TC-MIB",
    "Unsigned8",
    "UnsignedPercent")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

dmosSysmonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4)
)
if mibBuilder.loadTexts:
    dmosSysmonMIB.setRevisions(
        ("2016-02-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cpu_ObjectIdentity = ObjectIdentity
cpu = _Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1)
)
_CpuChassisTable_Object = MibTable
cpuChassisTable = _CpuChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 1)
)
if mibBuilder.loadTexts:
    cpuChassisTable.setStatus("current")
_CpuChassisEntry_Object = MibTableRow
cpuChassisEntry = _CpuChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 1, 1)
)
cpuChassisEntry.setIndexNames(
    (0, "DMOS-SYSMON-MIB", "cpuChassisId"),
)
if mibBuilder.loadTexts:
    cpuChassisEntry.setStatus("current")
_CpuChassisId_Type = Unsigned32
_CpuChassisId_Object = MibTableColumn
cpuChassisId = _CpuChassisId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 1, 1, 1),
    _CpuChassisId_Type()
)
cpuChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuChassisId.setStatus("current")
_CpuSlotTable_Object = MibTable
cpuSlotTable = _CpuSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 2)
)
if mibBuilder.loadTexts:
    cpuSlotTable.setStatus("current")
_CpuSlotEntry_Object = MibTableRow
cpuSlotEntry = _CpuSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 2, 1)
)
cpuSlotEntry.setIndexNames(
    (0, "DMOS-SYSMON-MIB", "cpuChassisId"),
    (0, "DMOS-SYSMON-MIB", "cpuSlotId"),
)
if mibBuilder.loadTexts:
    cpuSlotEntry.setStatus("current")
_CpuSlotId_Type = DisplayString
_CpuSlotId_Object = MibTableColumn
cpuSlotId = _CpuSlotId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 2, 1, 1),
    _CpuSlotId_Type()
)
cpuSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpuSlotId.setStatus("current")
_CpuLoadFiveSecondsActive_Type = UnsignedPercent
_CpuLoadFiveSecondsActive_Object = MibTableColumn
cpuLoadFiveSecondsActive = _CpuLoadFiveSecondsActive_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 2, 1, 2),
    _CpuLoadFiveSecondsActive_Type()
)
cpuLoadFiveSecondsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoadFiveSecondsActive.setStatus("current")
if mibBuilder.loadTexts:
    cpuLoadFiveSecondsActive.setUnits("%")
_CpuLoadFiveSecondsIdle_Type = UnsignedPercent
_CpuLoadFiveSecondsIdle_Object = MibTableColumn
cpuLoadFiveSecondsIdle = _CpuLoadFiveSecondsIdle_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 2, 1, 3),
    _CpuLoadFiveSecondsIdle_Type()
)
cpuLoadFiveSecondsIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoadFiveSecondsIdle.setStatus("current")
if mibBuilder.loadTexts:
    cpuLoadFiveSecondsIdle.setUnits("%")
_CpuLoadOneMinuteActive_Type = UnsignedPercent
_CpuLoadOneMinuteActive_Object = MibTableColumn
cpuLoadOneMinuteActive = _CpuLoadOneMinuteActive_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 2, 1, 4),
    _CpuLoadOneMinuteActive_Type()
)
cpuLoadOneMinuteActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoadOneMinuteActive.setStatus("current")
if mibBuilder.loadTexts:
    cpuLoadOneMinuteActive.setUnits("%")
_CpuLoadOneMinuteIdle_Type = UnsignedPercent
_CpuLoadOneMinuteIdle_Object = MibTableColumn
cpuLoadOneMinuteIdle = _CpuLoadOneMinuteIdle_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 2, 1, 5),
    _CpuLoadOneMinuteIdle_Type()
)
cpuLoadOneMinuteIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoadOneMinuteIdle.setStatus("current")
if mibBuilder.loadTexts:
    cpuLoadOneMinuteIdle.setUnits("%")
_CpuLoadFiveMinutesActive_Type = UnsignedPercent
_CpuLoadFiveMinutesActive_Object = MibTableColumn
cpuLoadFiveMinutesActive = _CpuLoadFiveMinutesActive_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 2, 1, 6),
    _CpuLoadFiveMinutesActive_Type()
)
cpuLoadFiveMinutesActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoadFiveMinutesActive.setStatus("current")
if mibBuilder.loadTexts:
    cpuLoadFiveMinutesActive.setUnits("%")
_CpuLoadFiveMinutesIdle_Type = UnsignedPercent
_CpuLoadFiveMinutesIdle_Object = MibTableColumn
cpuLoadFiveMinutesIdle = _CpuLoadFiveMinutesIdle_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 2, 1, 7),
    _CpuLoadFiveMinutesIdle_Type()
)
cpuLoadFiveMinutesIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoadFiveMinutesIdle.setStatus("current")
if mibBuilder.loadTexts:
    cpuLoadFiveMinutesIdle.setUnits("%")
_CpuCoreTable_Object = MibTable
cpuCoreTable = _CpuCoreTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3)
)
if mibBuilder.loadTexts:
    cpuCoreTable.setStatus("current")
_CpuCoreEntry_Object = MibTableRow
cpuCoreEntry = _CpuCoreEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1)
)
cpuCoreEntry.setIndexNames(
    (0, "DMOS-SYSMON-MIB", "cpuChassisId"),
    (0, "DMOS-SYSMON-MIB", "cpuSlotId"),
    (0, "DMOS-SYSMON-MIB", "cpuCoreCoreId"),
)
if mibBuilder.loadTexts:
    cpuCoreEntry.setStatus("current")
_CpuCoreCoreId_Type = Unsigned8
_CpuCoreCoreId_Object = MibTableColumn
cpuCoreCoreId = _CpuCoreCoreId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 1),
    _CpuCoreCoreId_Type()
)
cpuCoreCoreId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpuCoreCoreId.setStatus("current")
_CpuCoreFiveSecondsActive_Type = UnsignedPercent
_CpuCoreFiveSecondsActive_Object = MibTableColumn
cpuCoreFiveSecondsActive = _CpuCoreFiveSecondsActive_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 2),
    _CpuCoreFiveSecondsActive_Type()
)
cpuCoreFiveSecondsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreFiveSecondsActive.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreFiveSecondsActive.setUnits("%")
_CpuCoreFiveSecondsUser_Type = UnsignedPercent
_CpuCoreFiveSecondsUser_Object = MibTableColumn
cpuCoreFiveSecondsUser = _CpuCoreFiveSecondsUser_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 3),
    _CpuCoreFiveSecondsUser_Type()
)
cpuCoreFiveSecondsUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreFiveSecondsUser.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreFiveSecondsUser.setUnits("%")
_CpuCoreFiveSecondsSystem_Type = UnsignedPercent
_CpuCoreFiveSecondsSystem_Object = MibTableColumn
cpuCoreFiveSecondsSystem = _CpuCoreFiveSecondsSystem_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 4),
    _CpuCoreFiveSecondsSystem_Type()
)
cpuCoreFiveSecondsSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreFiveSecondsSystem.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreFiveSecondsSystem.setUnits("%")
_CpuCoreFiveSecondsNice_Type = UnsignedPercent
_CpuCoreFiveSecondsNice_Object = MibTableColumn
cpuCoreFiveSecondsNice = _CpuCoreFiveSecondsNice_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 5),
    _CpuCoreFiveSecondsNice_Type()
)
cpuCoreFiveSecondsNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreFiveSecondsNice.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreFiveSecondsNice.setUnits("%")
_CpuCoreFiveSecondsIdle_Type = UnsignedPercent
_CpuCoreFiveSecondsIdle_Object = MibTableColumn
cpuCoreFiveSecondsIdle = _CpuCoreFiveSecondsIdle_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 6),
    _CpuCoreFiveSecondsIdle_Type()
)
cpuCoreFiveSecondsIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreFiveSecondsIdle.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreFiveSecondsIdle.setUnits("%")
_CpuCoreFiveSecondsWait_Type = UnsignedPercent
_CpuCoreFiveSecondsWait_Object = MibTableColumn
cpuCoreFiveSecondsWait = _CpuCoreFiveSecondsWait_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 7),
    _CpuCoreFiveSecondsWait_Type()
)
cpuCoreFiveSecondsWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreFiveSecondsWait.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreFiveSecondsWait.setUnits("%")
_CpuCoreFiveSecondsInterrupt_Type = UnsignedPercent
_CpuCoreFiveSecondsInterrupt_Object = MibTableColumn
cpuCoreFiveSecondsInterrupt = _CpuCoreFiveSecondsInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 8),
    _CpuCoreFiveSecondsInterrupt_Type()
)
cpuCoreFiveSecondsInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreFiveSecondsInterrupt.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreFiveSecondsInterrupt.setUnits("%")
_CpuCoreFiveSecondsSoftirq_Type = UnsignedPercent
_CpuCoreFiveSecondsSoftirq_Object = MibTableColumn
cpuCoreFiveSecondsSoftirq = _CpuCoreFiveSecondsSoftirq_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 9),
    _CpuCoreFiveSecondsSoftirq_Type()
)
cpuCoreFiveSecondsSoftirq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreFiveSecondsSoftirq.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreFiveSecondsSoftirq.setUnits("%")
_CpuCoreOneMinuteActive_Type = UnsignedPercent
_CpuCoreOneMinuteActive_Object = MibTableColumn
cpuCoreOneMinuteActive = _CpuCoreOneMinuteActive_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 10),
    _CpuCoreOneMinuteActive_Type()
)
cpuCoreOneMinuteActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreOneMinuteActive.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreOneMinuteActive.setUnits("%")
_CpuCoreOneMinuteUser_Type = UnsignedPercent
_CpuCoreOneMinuteUser_Object = MibTableColumn
cpuCoreOneMinuteUser = _CpuCoreOneMinuteUser_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 11),
    _CpuCoreOneMinuteUser_Type()
)
cpuCoreOneMinuteUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreOneMinuteUser.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreOneMinuteUser.setUnits("%")
_CpuCoreOneMinuteSystem_Type = UnsignedPercent
_CpuCoreOneMinuteSystem_Object = MibTableColumn
cpuCoreOneMinuteSystem = _CpuCoreOneMinuteSystem_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 12),
    _CpuCoreOneMinuteSystem_Type()
)
cpuCoreOneMinuteSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreOneMinuteSystem.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreOneMinuteSystem.setUnits("%")
_CpuCoreOneMinuteNice_Type = UnsignedPercent
_CpuCoreOneMinuteNice_Object = MibTableColumn
cpuCoreOneMinuteNice = _CpuCoreOneMinuteNice_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 13),
    _CpuCoreOneMinuteNice_Type()
)
cpuCoreOneMinuteNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreOneMinuteNice.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreOneMinuteNice.setUnits("%")
_CpuCoreOneMinuteIdle_Type = UnsignedPercent
_CpuCoreOneMinuteIdle_Object = MibTableColumn
cpuCoreOneMinuteIdle = _CpuCoreOneMinuteIdle_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 14),
    _CpuCoreOneMinuteIdle_Type()
)
cpuCoreOneMinuteIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreOneMinuteIdle.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreOneMinuteIdle.setUnits("%")
_CpuCoreOneMinuteWait_Type = UnsignedPercent
_CpuCoreOneMinuteWait_Object = MibTableColumn
cpuCoreOneMinuteWait = _CpuCoreOneMinuteWait_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 15),
    _CpuCoreOneMinuteWait_Type()
)
cpuCoreOneMinuteWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreOneMinuteWait.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreOneMinuteWait.setUnits("%")
_CpuCoreOneMinuteInterrupt_Type = UnsignedPercent
_CpuCoreOneMinuteInterrupt_Object = MibTableColumn
cpuCoreOneMinuteInterrupt = _CpuCoreOneMinuteInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 16),
    _CpuCoreOneMinuteInterrupt_Type()
)
cpuCoreOneMinuteInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreOneMinuteInterrupt.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreOneMinuteInterrupt.setUnits("%")
_CpuCoreOneMinuteSoftirq_Type = UnsignedPercent
_CpuCoreOneMinuteSoftirq_Object = MibTableColumn
cpuCoreOneMinuteSoftirq = _CpuCoreOneMinuteSoftirq_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 17),
    _CpuCoreOneMinuteSoftirq_Type()
)
cpuCoreOneMinuteSoftirq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreOneMinuteSoftirq.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreOneMinuteSoftirq.setUnits("%")
_CpuCoreFiveMinutesActive_Type = UnsignedPercent
_CpuCoreFiveMinutesActive_Object = MibTableColumn
cpuCoreFiveMinutesActive = _CpuCoreFiveMinutesActive_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 18),
    _CpuCoreFiveMinutesActive_Type()
)
cpuCoreFiveMinutesActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreFiveMinutesActive.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreFiveMinutesActive.setUnits("%")
_CpuCoreFiveMinutesUser_Type = UnsignedPercent
_CpuCoreFiveMinutesUser_Object = MibTableColumn
cpuCoreFiveMinutesUser = _CpuCoreFiveMinutesUser_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 19),
    _CpuCoreFiveMinutesUser_Type()
)
cpuCoreFiveMinutesUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreFiveMinutesUser.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreFiveMinutesUser.setUnits("%")
_CpuCoreFiveMinutesSystem_Type = UnsignedPercent
_CpuCoreFiveMinutesSystem_Object = MibTableColumn
cpuCoreFiveMinutesSystem = _CpuCoreFiveMinutesSystem_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 20),
    _CpuCoreFiveMinutesSystem_Type()
)
cpuCoreFiveMinutesSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreFiveMinutesSystem.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreFiveMinutesSystem.setUnits("%")
_CpuCoreFiveMinutesNice_Type = UnsignedPercent
_CpuCoreFiveMinutesNice_Object = MibTableColumn
cpuCoreFiveMinutesNice = _CpuCoreFiveMinutesNice_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 21),
    _CpuCoreFiveMinutesNice_Type()
)
cpuCoreFiveMinutesNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreFiveMinutesNice.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreFiveMinutesNice.setUnits("%")
_CpuCoreFiveMinutesIdle_Type = UnsignedPercent
_CpuCoreFiveMinutesIdle_Object = MibTableColumn
cpuCoreFiveMinutesIdle = _CpuCoreFiveMinutesIdle_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 22),
    _CpuCoreFiveMinutesIdle_Type()
)
cpuCoreFiveMinutesIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreFiveMinutesIdle.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreFiveMinutesIdle.setUnits("%")
_CpuCoreFiveMinutesWait_Type = UnsignedPercent
_CpuCoreFiveMinutesWait_Object = MibTableColumn
cpuCoreFiveMinutesWait = _CpuCoreFiveMinutesWait_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 23),
    _CpuCoreFiveMinutesWait_Type()
)
cpuCoreFiveMinutesWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreFiveMinutesWait.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreFiveMinutesWait.setUnits("%")
_CpuCoreFiveMinutesInterrupt_Type = UnsignedPercent
_CpuCoreFiveMinutesInterrupt_Object = MibTableColumn
cpuCoreFiveMinutesInterrupt = _CpuCoreFiveMinutesInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 24),
    _CpuCoreFiveMinutesInterrupt_Type()
)
cpuCoreFiveMinutesInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreFiveMinutesInterrupt.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreFiveMinutesInterrupt.setUnits("%")
_CpuCoreFiveMinutesSoftirq_Type = UnsignedPercent
_CpuCoreFiveMinutesSoftirq_Object = MibTableColumn
cpuCoreFiveMinutesSoftirq = _CpuCoreFiveMinutesSoftirq_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 1, 3, 1, 25),
    _CpuCoreFiveMinutesSoftirq_Type()
)
cpuCoreFiveMinutesSoftirq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreFiveMinutesSoftirq.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreFiveMinutesSoftirq.setUnits("%")
_Memory_ObjectIdentity = ObjectIdentity
memory = _Memory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2)
)
_MemoryChassisTable_Object = MibTable
memoryChassisTable = _MemoryChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 1)
)
if mibBuilder.loadTexts:
    memoryChassisTable.setStatus("current")
_MemoryChassisEntry_Object = MibTableRow
memoryChassisEntry = _MemoryChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 1, 1)
)
memoryChassisEntry.setIndexNames(
    (0, "DMOS-SYSMON-MIB", "memoryChassisId"),
)
if mibBuilder.loadTexts:
    memoryChassisEntry.setStatus("current")
_MemoryChassisId_Type = Unsigned32
_MemoryChassisId_Object = MibTableColumn
memoryChassisId = _MemoryChassisId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 1, 1, 1),
    _MemoryChassisId_Type()
)
memoryChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryChassisId.setStatus("current")
_MemorySlotTable_Object = MibTable
memorySlotTable = _MemorySlotTable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2)
)
if mibBuilder.loadTexts:
    memorySlotTable.setStatus("current")
_MemorySlotEntry_Object = MibTableRow
memorySlotEntry = _MemorySlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1)
)
memorySlotEntry.setIndexNames(
    (0, "DMOS-SYSMON-MIB", "memoryChassisId"),
    (0, "DMOS-SYSMON-MIB", "memorySlotId"),
)
if mibBuilder.loadTexts:
    memorySlotEntry.setStatus("current")
_MemorySlotId_Type = DisplayString
_MemorySlotId_Object = MibTableColumn
memorySlotId = _MemorySlotId_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 1),
    _MemorySlotId_Type()
)
memorySlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    memorySlotId.setStatus("current")
_MemoryFiveSecondsTotal_Type = Unsigned32
_MemoryFiveSecondsTotal_Object = MibTableColumn
memoryFiveSecondsTotal = _MemoryFiveSecondsTotal_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 2),
    _MemoryFiveSecondsTotal_Type()
)
memoryFiveSecondsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFiveSecondsTotal.setStatus("current")
if mibBuilder.loadTexts:
    memoryFiveSecondsTotal.setUnits("Bytes")
_MemoryFiveSecondsUsed_Type = Unsigned32
_MemoryFiveSecondsUsed_Object = MibTableColumn
memoryFiveSecondsUsed = _MemoryFiveSecondsUsed_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 3),
    _MemoryFiveSecondsUsed_Type()
)
memoryFiveSecondsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFiveSecondsUsed.setStatus("current")
if mibBuilder.loadTexts:
    memoryFiveSecondsUsed.setUnits("Bytes")
_MemoryFiveSecondsFree_Type = Unsigned32
_MemoryFiveSecondsFree_Object = MibTableColumn
memoryFiveSecondsFree = _MemoryFiveSecondsFree_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 4),
    _MemoryFiveSecondsFree_Type()
)
memoryFiveSecondsFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFiveSecondsFree.setStatus("current")
if mibBuilder.loadTexts:
    memoryFiveSecondsFree.setUnits("Bytes")
_MemoryFiveSecondsBuffered_Type = Unsigned32
_MemoryFiveSecondsBuffered_Object = MibTableColumn
memoryFiveSecondsBuffered = _MemoryFiveSecondsBuffered_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 5),
    _MemoryFiveSecondsBuffered_Type()
)
memoryFiveSecondsBuffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFiveSecondsBuffered.setStatus("current")
if mibBuilder.loadTexts:
    memoryFiveSecondsBuffered.setUnits("Bytes")
_MemoryFiveSecondsCached_Type = Unsigned32
_MemoryFiveSecondsCached_Object = MibTableColumn
memoryFiveSecondsCached = _MemoryFiveSecondsCached_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 6),
    _MemoryFiveSecondsCached_Type()
)
memoryFiveSecondsCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFiveSecondsCached.setStatus("current")
if mibBuilder.loadTexts:
    memoryFiveSecondsCached.setUnits("Bytes")
_MemoryFiveSecondsAvailable_Type = Unsigned32
_MemoryFiveSecondsAvailable_Object = MibTableColumn
memoryFiveSecondsAvailable = _MemoryFiveSecondsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 7),
    _MemoryFiveSecondsAvailable_Type()
)
memoryFiveSecondsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFiveSecondsAvailable.setStatus("current")
if mibBuilder.loadTexts:
    memoryFiveSecondsAvailable.setUnits("Bytes")
_MemoryFiveSecondsSlabRecl_Type = Unsigned32
_MemoryFiveSecondsSlabRecl_Object = MibTableColumn
memoryFiveSecondsSlabRecl = _MemoryFiveSecondsSlabRecl_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 8),
    _MemoryFiveSecondsSlabRecl_Type()
)
memoryFiveSecondsSlabRecl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFiveSecondsSlabRecl.setStatus("current")
if mibBuilder.loadTexts:
    memoryFiveSecondsSlabRecl.setUnits("Bytes")
_MemoryFiveSecondsSlabUnrecl_Type = Unsigned32
_MemoryFiveSecondsSlabUnrecl_Object = MibTableColumn
memoryFiveSecondsSlabUnrecl = _MemoryFiveSecondsSlabUnrecl_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 9),
    _MemoryFiveSecondsSlabUnrecl_Type()
)
memoryFiveSecondsSlabUnrecl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFiveSecondsSlabUnrecl.setStatus("current")
if mibBuilder.loadTexts:
    memoryFiveSecondsSlabUnrecl.setUnits("Bytes")
_MemoryFiveMinutesTotal_Type = Unsigned32
_MemoryFiveMinutesTotal_Object = MibTableColumn
memoryFiveMinutesTotal = _MemoryFiveMinutesTotal_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 10),
    _MemoryFiveMinutesTotal_Type()
)
memoryFiveMinutesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFiveMinutesTotal.setStatus("current")
if mibBuilder.loadTexts:
    memoryFiveMinutesTotal.setUnits("Bytes")
_MemoryFiveMinutesUsed_Type = Unsigned32
_MemoryFiveMinutesUsed_Object = MibTableColumn
memoryFiveMinutesUsed = _MemoryFiveMinutesUsed_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 11),
    _MemoryFiveMinutesUsed_Type()
)
memoryFiveMinutesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFiveMinutesUsed.setStatus("current")
if mibBuilder.loadTexts:
    memoryFiveMinutesUsed.setUnits("Bytes")
_MemoryFiveMinutesFree_Type = Unsigned32
_MemoryFiveMinutesFree_Object = MibTableColumn
memoryFiveMinutesFree = _MemoryFiveMinutesFree_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 12),
    _MemoryFiveMinutesFree_Type()
)
memoryFiveMinutesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFiveMinutesFree.setStatus("current")
if mibBuilder.loadTexts:
    memoryFiveMinutesFree.setUnits("Bytes")
_MemoryFiveMinutesBuffered_Type = Unsigned32
_MemoryFiveMinutesBuffered_Object = MibTableColumn
memoryFiveMinutesBuffered = _MemoryFiveMinutesBuffered_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 13),
    _MemoryFiveMinutesBuffered_Type()
)
memoryFiveMinutesBuffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFiveMinutesBuffered.setStatus("current")
if mibBuilder.loadTexts:
    memoryFiveMinutesBuffered.setUnits("Bytes")
_MemoryFiveMinutesCached_Type = Unsigned32
_MemoryFiveMinutesCached_Object = MibTableColumn
memoryFiveMinutesCached = _MemoryFiveMinutesCached_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 14),
    _MemoryFiveMinutesCached_Type()
)
memoryFiveMinutesCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFiveMinutesCached.setStatus("current")
if mibBuilder.loadTexts:
    memoryFiveMinutesCached.setUnits("Bytes")
_MemoryFiveMinutesAvailable_Type = Unsigned32
_MemoryFiveMinutesAvailable_Object = MibTableColumn
memoryFiveMinutesAvailable = _MemoryFiveMinutesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 15),
    _MemoryFiveMinutesAvailable_Type()
)
memoryFiveMinutesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFiveMinutesAvailable.setStatus("current")
if mibBuilder.loadTexts:
    memoryFiveMinutesAvailable.setUnits("Bytes")
_MemoryFiveMinutesSlabRecl_Type = Unsigned32
_MemoryFiveMinutesSlabRecl_Object = MibTableColumn
memoryFiveMinutesSlabRecl = _MemoryFiveMinutesSlabRecl_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 16),
    _MemoryFiveMinutesSlabRecl_Type()
)
memoryFiveMinutesSlabRecl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFiveMinutesSlabRecl.setStatus("current")
if mibBuilder.loadTexts:
    memoryFiveMinutesSlabRecl.setUnits("Bytes")
_MemoryFiveMinutesSlabUnrecl_Type = Unsigned32
_MemoryFiveMinutesSlabUnrecl_Object = MibTableColumn
memoryFiveMinutesSlabUnrecl = _MemoryFiveMinutesSlabUnrecl_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 17),
    _MemoryFiveMinutesSlabUnrecl_Type()
)
memoryFiveMinutesSlabUnrecl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFiveMinutesSlabUnrecl.setStatus("current")
if mibBuilder.loadTexts:
    memoryFiveMinutesSlabUnrecl.setUnits("Bytes")
_MemoryThirtyMinutesTotal_Type = Unsigned32
_MemoryThirtyMinutesTotal_Object = MibTableColumn
memoryThirtyMinutesTotal = _MemoryThirtyMinutesTotal_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 18),
    _MemoryThirtyMinutesTotal_Type()
)
memoryThirtyMinutesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryThirtyMinutesTotal.setStatus("current")
if mibBuilder.loadTexts:
    memoryThirtyMinutesTotal.setUnits("Bytes")
_MemoryThirtyMinutesUsed_Type = Unsigned32
_MemoryThirtyMinutesUsed_Object = MibTableColumn
memoryThirtyMinutesUsed = _MemoryThirtyMinutesUsed_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 19),
    _MemoryThirtyMinutesUsed_Type()
)
memoryThirtyMinutesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryThirtyMinutesUsed.setStatus("current")
if mibBuilder.loadTexts:
    memoryThirtyMinutesUsed.setUnits("Bytes")
_MemoryThirtyMinutesFree_Type = Unsigned32
_MemoryThirtyMinutesFree_Object = MibTableColumn
memoryThirtyMinutesFree = _MemoryThirtyMinutesFree_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 20),
    _MemoryThirtyMinutesFree_Type()
)
memoryThirtyMinutesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryThirtyMinutesFree.setStatus("current")
if mibBuilder.loadTexts:
    memoryThirtyMinutesFree.setUnits("Bytes")
_MemoryThirtyMinutesBuffered_Type = Unsigned32
_MemoryThirtyMinutesBuffered_Object = MibTableColumn
memoryThirtyMinutesBuffered = _MemoryThirtyMinutesBuffered_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 21),
    _MemoryThirtyMinutesBuffered_Type()
)
memoryThirtyMinutesBuffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryThirtyMinutesBuffered.setStatus("current")
if mibBuilder.loadTexts:
    memoryThirtyMinutesBuffered.setUnits("Bytes")
_MemoryThirtyMinutesCached_Type = Unsigned32
_MemoryThirtyMinutesCached_Object = MibTableColumn
memoryThirtyMinutesCached = _MemoryThirtyMinutesCached_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 22),
    _MemoryThirtyMinutesCached_Type()
)
memoryThirtyMinutesCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryThirtyMinutesCached.setStatus("current")
if mibBuilder.loadTexts:
    memoryThirtyMinutesCached.setUnits("Bytes")
_MemoryThirtyMinutesAvailable_Type = Unsigned32
_MemoryThirtyMinutesAvailable_Object = MibTableColumn
memoryThirtyMinutesAvailable = _MemoryThirtyMinutesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 23),
    _MemoryThirtyMinutesAvailable_Type()
)
memoryThirtyMinutesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryThirtyMinutesAvailable.setStatus("current")
if mibBuilder.loadTexts:
    memoryThirtyMinutesAvailable.setUnits("Bytes")
_MemoryThirtyMinutesSlabRecl_Type = Unsigned32
_MemoryThirtyMinutesSlabRecl_Object = MibTableColumn
memoryThirtyMinutesSlabRecl = _MemoryThirtyMinutesSlabRecl_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 24),
    _MemoryThirtyMinutesSlabRecl_Type()
)
memoryThirtyMinutesSlabRecl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryThirtyMinutesSlabRecl.setStatus("current")
if mibBuilder.loadTexts:
    memoryThirtyMinutesSlabRecl.setUnits("Bytes")
_MemoryThirtyMinutesSlabUnrecl_Type = Unsigned32
_MemoryThirtyMinutesSlabUnrecl_Object = MibTableColumn
memoryThirtyMinutesSlabUnrecl = _MemoryThirtyMinutesSlabUnrecl_Object(
    (1, 3, 6, 1, 4, 1, 3709, 3, 6, 4, 2, 2, 1, 25),
    _MemoryThirtyMinutesSlabUnrecl_Type()
)
memoryThirtyMinutesSlabUnrecl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryThirtyMinutesSlabUnrecl.setStatus("current")
if mibBuilder.loadTexts:
    memoryThirtyMinutesSlabUnrecl.setUnits("Bytes")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DMOS-SYSMON-MIB",
    **{"dmosSysmonMIB": dmosSysmonMIB,
       "cpu": cpu,
       "cpuChassisTable": cpuChassisTable,
       "cpuChassisEntry": cpuChassisEntry,
       "cpuChassisId": cpuChassisId,
       "cpuSlotTable": cpuSlotTable,
       "cpuSlotEntry": cpuSlotEntry,
       "cpuSlotId": cpuSlotId,
       "cpuLoadFiveSecondsActive": cpuLoadFiveSecondsActive,
       "cpuLoadFiveSecondsIdle": cpuLoadFiveSecondsIdle,
       "cpuLoadOneMinuteActive": cpuLoadOneMinuteActive,
       "cpuLoadOneMinuteIdle": cpuLoadOneMinuteIdle,
       "cpuLoadFiveMinutesActive": cpuLoadFiveMinutesActive,
       "cpuLoadFiveMinutesIdle": cpuLoadFiveMinutesIdle,
       "cpuCoreTable": cpuCoreTable,
       "cpuCoreEntry": cpuCoreEntry,
       "cpuCoreCoreId": cpuCoreCoreId,
       "cpuCoreFiveSecondsActive": cpuCoreFiveSecondsActive,
       "cpuCoreFiveSecondsUser": cpuCoreFiveSecondsUser,
       "cpuCoreFiveSecondsSystem": cpuCoreFiveSecondsSystem,
       "cpuCoreFiveSecondsNice": cpuCoreFiveSecondsNice,
       "cpuCoreFiveSecondsIdle": cpuCoreFiveSecondsIdle,
       "cpuCoreFiveSecondsWait": cpuCoreFiveSecondsWait,
       "cpuCoreFiveSecondsInterrupt": cpuCoreFiveSecondsInterrupt,
       "cpuCoreFiveSecondsSoftirq": cpuCoreFiveSecondsSoftirq,
       "cpuCoreOneMinuteActive": cpuCoreOneMinuteActive,
       "cpuCoreOneMinuteUser": cpuCoreOneMinuteUser,
       "cpuCoreOneMinuteSystem": cpuCoreOneMinuteSystem,
       "cpuCoreOneMinuteNice": cpuCoreOneMinuteNice,
       "cpuCoreOneMinuteIdle": cpuCoreOneMinuteIdle,
       "cpuCoreOneMinuteWait": cpuCoreOneMinuteWait,
       "cpuCoreOneMinuteInterrupt": cpuCoreOneMinuteInterrupt,
       "cpuCoreOneMinuteSoftirq": cpuCoreOneMinuteSoftirq,
       "cpuCoreFiveMinutesActive": cpuCoreFiveMinutesActive,
       "cpuCoreFiveMinutesUser": cpuCoreFiveMinutesUser,
       "cpuCoreFiveMinutesSystem": cpuCoreFiveMinutesSystem,
       "cpuCoreFiveMinutesNice": cpuCoreFiveMinutesNice,
       "cpuCoreFiveMinutesIdle": cpuCoreFiveMinutesIdle,
       "cpuCoreFiveMinutesWait": cpuCoreFiveMinutesWait,
       "cpuCoreFiveMinutesInterrupt": cpuCoreFiveMinutesInterrupt,
       "cpuCoreFiveMinutesSoftirq": cpuCoreFiveMinutesSoftirq,
       "memory": memory,
       "memoryChassisTable": memoryChassisTable,
       "memoryChassisEntry": memoryChassisEntry,
       "memoryChassisId": memoryChassisId,
       "memorySlotTable": memorySlotTable,
       "memorySlotEntry": memorySlotEntry,
       "memorySlotId": memorySlotId,
       "memoryFiveSecondsTotal": memoryFiveSecondsTotal,
       "memoryFiveSecondsUsed": memoryFiveSecondsUsed,
       "memoryFiveSecondsFree": memoryFiveSecondsFree,
       "memoryFiveSecondsBuffered": memoryFiveSecondsBuffered,
       "memoryFiveSecondsCached": memoryFiveSecondsCached,
       "memoryFiveSecondsAvailable": memoryFiveSecondsAvailable,
       "memoryFiveSecondsSlabRecl": memoryFiveSecondsSlabRecl,
       "memoryFiveSecondsSlabUnrecl": memoryFiveSecondsSlabUnrecl,
       "memoryFiveMinutesTotal": memoryFiveMinutesTotal,
       "memoryFiveMinutesUsed": memoryFiveMinutesUsed,
       "memoryFiveMinutesFree": memoryFiveMinutesFree,
       "memoryFiveMinutesBuffered": memoryFiveMinutesBuffered,
       "memoryFiveMinutesCached": memoryFiveMinutesCached,
       "memoryFiveMinutesAvailable": memoryFiveMinutesAvailable,
       "memoryFiveMinutesSlabRecl": memoryFiveMinutesSlabRecl,
       "memoryFiveMinutesSlabUnrecl": memoryFiveMinutesSlabUnrecl,
       "memoryThirtyMinutesTotal": memoryThirtyMinutesTotal,
       "memoryThirtyMinutesUsed": memoryThirtyMinutesUsed,
       "memoryThirtyMinutesFree": memoryThirtyMinutesFree,
       "memoryThirtyMinutesBuffered": memoryThirtyMinutesBuffered,
       "memoryThirtyMinutesCached": memoryThirtyMinutesCached,
       "memoryThirtyMinutesAvailable": memoryThirtyMinutesAvailable,
       "memoryThirtyMinutesSlabRecl": memoryThirtyMinutesSlabRecl,
       "memoryThirtyMinutesSlabUnrecl": memoryThirtyMinutesSlabUnrecl}
)
