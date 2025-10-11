# SNMP MIB module (MX-COMDASYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-COMDASYS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:45 2025
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

(mediatrix,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrix")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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

(AutonomousType,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

comdasysGW = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 4)
)
if mibBuilder.loadTexts:
    comdasysGW.setRevisions(
        ("1921-04-08 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sysinfo_ObjectIdentity = ObjectIdentity
sysinfo = _Sysinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 4, 1)
)


class _SwVersion_Type(DisplayString):
    """Custom type swVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwVersion_Type.__name__ = "DisplayString"
_SwVersion_Object = MibScalar
swVersion = _SwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 1, 1),
    _SwVersion_Type()
)
swVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swVersion.setStatus("current")


class _ProductName_Type(DisplayString):
    """Custom type productName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ProductName_Type.__name__ = "DisplayString"
_ProductName_Object = MibScalar
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 1, 2),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("current")
_Admin_ObjectIdentity = ObjectIdentity
admin = _Admin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 4, 2)
)


class _DeviceRestart_Type(Integer32):
    """Custom type deviceRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("reload", 1))
    )


_DeviceRestart_Type.__name__ = "Integer32"
_DeviceRestart_Object = MibScalar
deviceRestart = _DeviceRestart_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 2, 1),
    _DeviceRestart_Type()
)
deviceRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceRestart.setStatus("mandatory")
_DaemonNumber_Type = Integer32
_DaemonNumber_Object = MibScalar
daemonNumber = _DaemonNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 2, 2),
    _DaemonNumber_Type()
)
daemonNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daemonNumber.setStatus("mandatory")
_DaemonTable_Object = MibTable
daemonTable = _DaemonTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 2, 3)
)
if mibBuilder.loadTexts:
    daemonTable.setStatus("mandatory")
_DaemonEntry_Object = MibTableRow
daemonEntry = _DaemonEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 2, 3, 1)
)
daemonEntry.setIndexNames(
    (0, "MX-COMDASYS-MIB", "daemonDescr"),
)
if mibBuilder.loadTexts:
    daemonEntry.setStatus("mandatory")
_DaemonDescr_Type = DisplayString
_DaemonDescr_Object = MibTableColumn
daemonDescr = _DaemonDescr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 2, 3, 1, 1),
    _DaemonDescr_Type()
)
daemonDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daemonDescr.setStatus("mandatory")
_DaemonStatus_Type = Gauge32
_DaemonStatus_Object = MibTableColumn
daemonStatus = _DaemonStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 2, 3, 1, 2),
    _DaemonStatus_Type()
)
daemonStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daemonStatus.setStatus("mandatory")


class _DaemonRestart_Type(Integer32):
    """Custom type daemonRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("reload", 1))
    )


_DaemonRestart_Type.__name__ = "Integer32"
_DaemonRestart_Object = MibTableColumn
daemonRestart = _DaemonRestart_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 2, 3, 1, 3),
    _DaemonRestart_Type()
)
daemonRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daemonRestart.setStatus("mandatory")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 4, 3)
)


class _DownloadExecute_Type(Integer32):
    """Custom type downloadExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("downloadConfiguration", 1))
    )


_DownloadExecute_Type.__name__ = "Integer32"
_DownloadExecute_Object = MibScalar
downloadExecute = _DownloadExecute_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 3, 1),
    _DownloadExecute_Type()
)
downloadExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadExecute.setStatus("mandatory")


class _DownloadFtpServerAddress_Type(OctetString):
    """Custom type downloadFtpServerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DownloadFtpServerAddress_Type.__name__ = "OctetString"
_DownloadFtpServerAddress_Object = MibScalar
downloadFtpServerAddress = _DownloadFtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 3, 2),
    _DownloadFtpServerAddress_Type()
)
downloadFtpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadFtpServerAddress.setStatus("mandatory")


class _DownloadFtpServerPort_Type(Integer32):
    """Custom type downloadFtpServerPort based on Integer32"""
    defaultValue = 21

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DownloadFtpServerPort_Type.__name__ = "Integer32"
_DownloadFtpServerPort_Object = MibScalar
downloadFtpServerPort = _DownloadFtpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 3, 3),
    _DownloadFtpServerPort_Type()
)
downloadFtpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadFtpServerPort.setStatus("current")


class _DownloadStatus_Type(Integer32):
    """Custom type downloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("success", 1),
          ("inProgress", 2))
    )


_DownloadStatus_Type.__name__ = "Integer32"
_DownloadStatus_Object = MibScalar
downloadStatus = _DownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 3, 4),
    _DownloadStatus_Type()
)
downloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downloadStatus.setStatus("mandatory")
_Firmware_ObjectIdentity = ObjectIdentity
firmware = _Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 4, 4)
)


class _FirmwareLoadExecute_Type(Integer32):
    """Custom type firmwareLoadExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("loadFirmware", 1))
    )


_FirmwareLoadExecute_Type.__name__ = "Integer32"
_FirmwareLoadExecute_Object = MibScalar
firmwareLoadExecute = _FirmwareLoadExecute_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 4, 1),
    _FirmwareLoadExecute_Type()
)
firmwareLoadExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareLoadExecute.setStatus("mandatory")


class _FirmwareFtpServerAddress_Type(OctetString):
    """Custom type firmwareFtpServerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FirmwareFtpServerAddress_Type.__name__ = "OctetString"
_FirmwareFtpServerAddress_Object = MibScalar
firmwareFtpServerAddress = _FirmwareFtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 4, 2),
    _FirmwareFtpServerAddress_Type()
)
firmwareFtpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareFtpServerAddress.setStatus("mandatory")


class _FirmwareFtpServerPort_Type(Integer32):
    """Custom type firmwareFtpServerPort based on Integer32"""
    defaultValue = 21

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FirmwareFtpServerPort_Type.__name__ = "Integer32"
_FirmwareFtpServerPort_Object = MibScalar
firmwareFtpServerPort = _FirmwareFtpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 4, 3),
    _FirmwareFtpServerPort_Type()
)
firmwareFtpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareFtpServerPort.setStatus("current")


class _FirmwareLoadStatus_Type(Integer32):
    """Custom type firmwareLoadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("success", 1),
          ("inProgress", 2))
    )


_FirmwareLoadStatus_Type.__name__ = "Integer32"
_FirmwareLoadStatus_Object = MibScalar
firmwareLoadStatus = _FirmwareLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 4, 4),
    _FirmwareLoadStatus_Type()
)
firmwareLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareLoadStatus.setStatus("mandatory")
_Performance_ObjectIdentity = ObjectIdentity
performance = _Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70)
)
_Cpu_ObjectIdentity = ObjectIdentity
cpu = _Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 10)
)
_CpuNumber_Type = Integer32
_CpuNumber_Object = MibScalar
cpuNumber = _CpuNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 10, 1),
    _CpuNumber_Type()
)
cpuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuNumber.setStatus("mandatory")
_CpuTable_Object = MibTable
cpuTable = _CpuTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 10, 2)
)
if mibBuilder.loadTexts:
    cpuTable.setStatus("mandatory")
_CpuEntry_Object = MibTableRow
cpuEntry = _CpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 10, 2, 1)
)
cpuEntry.setIndexNames(
    (0, "MX-COMDASYS-MIB", "cpuDescr"),
)
if mibBuilder.loadTexts:
    cpuEntry.setStatus("mandatory")
_CpuDescr_Type = DisplayString
_CpuDescr_Object = MibTableColumn
cpuDescr = _CpuDescr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 10, 2, 1, 1),
    _CpuDescr_Type()
)
cpuDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuDescr.setStatus("mandatory")
_CpuWorkloadCurrent_Type = Gauge32
_CpuWorkloadCurrent_Object = MibTableColumn
cpuWorkloadCurrent = _CpuWorkloadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 10, 2, 1, 2),
    _CpuWorkloadCurrent_Type()
)
cpuWorkloadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuWorkloadCurrent.setStatus("mandatory")
_CpuWorkload1MinuteAverage_Type = Gauge32
_CpuWorkload1MinuteAverage_Object = MibTableColumn
cpuWorkload1MinuteAverage = _CpuWorkload1MinuteAverage_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 10, 2, 1, 3),
    _CpuWorkload1MinuteAverage_Type()
)
cpuWorkload1MinuteAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuWorkload1MinuteAverage.setStatus("mandatory")
_CpuWorkload5MinuteAverage_Type = Gauge32
_CpuWorkload5MinuteAverage_Object = MibTableColumn
cpuWorkload5MinuteAverage = _CpuWorkload5MinuteAverage_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 10, 2, 1, 4),
    _CpuWorkload5MinuteAverage_Type()
)
cpuWorkload5MinuteAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuWorkload5MinuteAverage.setStatus("mandatory")
_Memory_ObjectIdentity = ObjectIdentity
memory = _Memory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 20)
)
_MemoryPoolNumber_Type = Integer32
_MemoryPoolNumber_Object = MibScalar
memoryPoolNumber = _MemoryPoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 20, 1),
    _MemoryPoolNumber_Type()
)
memoryPoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolNumber.setStatus("mandatory")
_MemoryPoolTable_Object = MibTable
memoryPoolTable = _MemoryPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 20, 2)
)
if mibBuilder.loadTexts:
    memoryPoolTable.setStatus("mandatory")
_MemoryPoolEntry_Object = MibTableRow
memoryPoolEntry = _MemoryPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 20, 2, 1)
)
memoryPoolEntry.setIndexNames(
    (0, "MX-COMDASYS-MIB", "memDescr"),
)
if mibBuilder.loadTexts:
    memoryPoolEntry.setStatus("mandatory")
_MemDescr_Type = DisplayString
_MemDescr_Object = MibTableColumn
memDescr = _MemDescr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 20, 2, 1, 1),
    _MemDescr_Type()
)
memDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memDescr.setStatus("mandatory")
_MemTotalBytes_Type = Integer32
_MemTotalBytes_Object = MibTableColumn
memTotalBytes = _MemTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 20, 2, 1, 2),
    _MemTotalBytes_Type()
)
memTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalBytes.setStatus("optional")
_MemAllocatedBytes_Type = Integer32
_MemAllocatedBytes_Object = MibTableColumn
memAllocatedBytes = _MemAllocatedBytes_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 20, 2, 1, 3),
    _MemAllocatedBytes_Type()
)
memAllocatedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAllocatedBytes.setStatus("mandatory")
_MemFreeBytes_Type = Integer32
_MemFreeBytes_Object = MibTableColumn
memFreeBytes = _MemFreeBytes_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 20, 2, 1, 4),
    _MemFreeBytes_Type()
)
memFreeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memFreeBytes.setStatus("mandatory")
_MemLargestFreeBlock_Type = Integer32
_MemLargestFreeBlock_Object = MibTableColumn
memLargestFreeBlock = _MemLargestFreeBlock_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 20, 2, 1, 5),
    _MemLargestFreeBlock_Type()
)
memLargestFreeBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memLargestFreeBlock.setStatus("mandatory")
_MemAllocatedBlocks_Type = Integer32
_MemAllocatedBlocks_Object = MibTableColumn
memAllocatedBlocks = _MemAllocatedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 20, 2, 1, 6),
    _MemAllocatedBlocks_Type()
)
memAllocatedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAllocatedBlocks.setStatus("mandatory")
_MemFreeBlocks_Type = Integer32
_MemFreeBlocks_Object = MibTableColumn
memFreeBlocks = _MemFreeBlocks_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 20, 2, 1, 7),
    _MemFreeBlocks_Type()
)
memFreeBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memFreeBlocks.setStatus("mandatory")
_Temperature_ObjectIdentity = ObjectIdentity
temperature = _Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 30)
)
_TempProbeNumber_Type = Integer32
_TempProbeNumber_Object = MibScalar
tempProbeNumber = _TempProbeNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 30, 1),
    _TempProbeNumber_Type()
)
tempProbeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempProbeNumber.setStatus("mandatory")
_TempProbeTable_Object = MibTable
tempProbeTable = _TempProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 30, 2)
)
if mibBuilder.loadTexts:
    tempProbeTable.setStatus("mandatory")
_TempProbeEntry_Object = MibTableRow
tempProbeEntry = _TempProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 30, 2, 1)
)
tempProbeEntry.setIndexNames(
    (0, "MX-COMDASYS-MIB", "tempProbeDescr"),
)
if mibBuilder.loadTexts:
    tempProbeEntry.setStatus("mandatory")
_TempProbeDescr_Type = DisplayString
_TempProbeDescr_Object = MibTableColumn
tempProbeDescr = _TempProbeDescr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 30, 2, 1, 1),
    _TempProbeDescr_Type()
)
tempProbeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempProbeDescr.setStatus("mandatory")
_CurrentDegreesCelsius_Type = Gauge32
_CurrentDegreesCelsius_Object = MibTableColumn
currentDegreesCelsius = _CurrentDegreesCelsius_Object(
    (1, 3, 6, 1, 4, 1, 4935, 4, 70, 30, 2, 1, 2),
    _CurrentDegreesCelsius_Type()
)
currentDegreesCelsius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDegreesCelsius.setStatus("mandatory")
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 4, 90)
)
_Convergence_33xx_Biab_ObjectIdentity = ObjectIdentity
convergence_33xx_Biab = _Convergence_33xx_Biab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 4, 90, 100)
)
_Convergence_1600_ObjectIdentity = ObjectIdentity
convergence_1600 = _Convergence_1600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 4, 90, 200)
)
_Convergence_2600_ObjectIdentity = ObjectIdentity
convergence_2600 = _Convergence_2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 4, 90, 300)
)
_Convergence_3600_ObjectIdentity = ObjectIdentity
convergence_3600 = _Convergence_3600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 4, 90, 400)
)
_Convergence_4600_ObjectIdentity = ObjectIdentity
convergence_4600 = _Convergence_4600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 4, 90, 500)
)
_Fmc_2800_ObjectIdentity = ObjectIdentity
fmc_2800 = _Fmc_2800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 4, 90, 600)
)
_Fmc_3800_ObjectIdentity = ObjectIdentity
fmc_3800 = _Fmc_3800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 4, 90, 700)
)
_Fmc_4800_ObjectIdentity = ObjectIdentity
fmc_4800 = _Fmc_4800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 4, 90, 800)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-COMDASYS-MIB",
    **{"comdasysGW": comdasysGW,
       "sysinfo": sysinfo,
       "swVersion": swVersion,
       "productName": productName,
       "admin": admin,
       "deviceRestart": deviceRestart,
       "daemonNumber": daemonNumber,
       "daemonTable": daemonTable,
       "daemonEntry": daemonEntry,
       "daemonDescr": daemonDescr,
       "daemonStatus": daemonStatus,
       "daemonRestart": daemonRestart,
       "config": config,
       "downloadExecute": downloadExecute,
       "downloadFtpServerAddress": downloadFtpServerAddress,
       "downloadFtpServerPort": downloadFtpServerPort,
       "downloadStatus": downloadStatus,
       "firmware": firmware,
       "firmwareLoadExecute": firmwareLoadExecute,
       "firmwareFtpServerAddress": firmwareFtpServerAddress,
       "firmwareFtpServerPort": firmwareFtpServerPort,
       "firmwareLoadStatus": firmwareLoadStatus,
       "performance": performance,
       "cpu": cpu,
       "cpuNumber": cpuNumber,
       "cpuTable": cpuTable,
       "cpuEntry": cpuEntry,
       "cpuDescr": cpuDescr,
       "cpuWorkloadCurrent": cpuWorkloadCurrent,
       "cpuWorkload1MinuteAverage": cpuWorkload1MinuteAverage,
       "cpuWorkload5MinuteAverage": cpuWorkload5MinuteAverage,
       "memory": memory,
       "memoryPoolNumber": memoryPoolNumber,
       "memoryPoolTable": memoryPoolTable,
       "memoryPoolEntry": memoryPoolEntry,
       "memDescr": memDescr,
       "memTotalBytes": memTotalBytes,
       "memAllocatedBytes": memAllocatedBytes,
       "memFreeBytes": memFreeBytes,
       "memLargestFreeBlock": memLargestFreeBlock,
       "memAllocatedBlocks": memAllocatedBlocks,
       "memFreeBlocks": memFreeBlocks,
       "temperature": temperature,
       "tempProbeNumber": tempProbeNumber,
       "tempProbeTable": tempProbeTable,
       "tempProbeEntry": tempProbeEntry,
       "tempProbeDescr": tempProbeDescr,
       "currentDegreesCelsius": currentDegreesCelsius,
       "products": products,
       "convergence-33xx-Biab": convergence_33xx_Biab,
       "convergence-1600": convergence_1600,
       "convergence-2600": convergence_2600,
       "convergence-3600": convergence_3600,
       "convergence-4600": convergence_4600,
       "fmc-2800": fmc_2800,
       "fmc-3800": fmc_3800,
       "fmc-4800": fmc_4800}
)
