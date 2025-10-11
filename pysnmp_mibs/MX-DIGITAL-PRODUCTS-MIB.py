# SNMP MIB module (MX-DIGITAL-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-DIGITAL-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:18 2025
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

mediatrixDigitalProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 3)
)
if mibBuilder.loadTexts:
    mediatrixDigitalProducts.setRevisions(
        ("1902-08-07 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sysinfo_ObjectIdentity = ObjectIdentity
sysinfo = _Sysinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 3, 1)
)


class _SerialNumber_Type(DisplayString):
    """Custom type serialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SerialNumber_Type.__name__ = "DisplayString"
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 1, 1),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")


class _HwRelease_Type(DisplayString):
    """Custom type hwRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HwRelease_Type.__name__ = "DisplayString"
_HwRelease_Object = MibScalar
hwRelease = _HwRelease_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 1, 3),
    _HwRelease_Type()
)
hwRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRelease.setStatus("current")


class _HwVersion_Type(DisplayString):
    """Custom type hwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_HwVersion_Type.__name__ = "DisplayString"
_HwVersion_Object = MibScalar
hwVersion = _HwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 1, 4),
    _HwVersion_Type()
)
hwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVersion.setStatus("current")


class _SwVersion_Type(DisplayString):
    """Custom type swVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwVersion_Type.__name__ = "DisplayString"
_SwVersion_Object = MibScalar
swVersion = _SwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 4935, 3, 1, 6),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("current")
_Admin_ObjectIdentity = ObjectIdentity
admin = _Admin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 3, 2)
)


class _DeviceReload_Type(Integer32):
    """Custom type deviceReload based on Integer32"""
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


_DeviceReload_Type.__name__ = "Integer32"
_DeviceReload_Object = MibScalar
deviceReload = _DeviceReload_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 2, 1),
    _DeviceReload_Type()
)
deviceReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceReload.setStatus("mandatory")


class _SaveRunningConfig_Type(Integer32):
    """Custom type saveRunningConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("saveConfiguration", 1))
    )


_SaveRunningConfig_Type.__name__ = "Integer32"
_SaveRunningConfig_Object = MibScalar
saveRunningConfig = _SaveRunningConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 2, 2),
    _SaveRunningConfig_Type()
)
saveRunningConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveRunningConfig.setStatus("mandatory")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 3, 3)
)
_StartupConfigUpload_ObjectIdentity = ObjectIdentity
startupConfigUpload = _StartupConfigUpload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 3, 3, 1)
)


class _UploadExecute_Type(Integer32):
    """Custom type uploadExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("uploadConfiguration", 1))
    )


_UploadExecute_Type.__name__ = "Integer32"
_UploadExecute_Object = MibScalar
uploadExecute = _UploadExecute_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 3, 1, 1),
    _UploadExecute_Type()
)
uploadExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uploadExecute.setStatus("mandatory")


class _UploadTftpServerAddress_Type(OctetString):
    """Custom type uploadTftpServerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_UploadTftpServerAddress_Type.__name__ = "OctetString"
_UploadTftpServerAddress_Object = MibScalar
uploadTftpServerAddress = _UploadTftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 3, 1, 2),
    _UploadTftpServerAddress_Type()
)
uploadTftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uploadTftpServerAddress.setStatus("mandatory")


class _UploadTftpServerPort_Type(Integer32):
    """Custom type uploadTftpServerPort based on Integer32"""
    defaultValue = 69

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UploadTftpServerPort_Type.__name__ = "Integer32"
_UploadTftpServerPort_Object = MibScalar
uploadTftpServerPort = _UploadTftpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 3, 1, 3),
    _UploadTftpServerPort_Type()
)
uploadTftpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uploadTftpServerPort.setStatus("mandatory")


class _UploadTftpServerPath_Type(OctetString):
    """Custom type uploadTftpServerPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_UploadTftpServerPath_Type.__name__ = "OctetString"
_UploadTftpServerPath_Object = MibScalar
uploadTftpServerPath = _UploadTftpServerPath_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 3, 1, 4),
    _UploadTftpServerPath_Type()
)
uploadTftpServerPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uploadTftpServerPath.setStatus("mandatory")


class _UploadStatus_Type(Integer32):
    """Custom type uploadStatus based on Integer32"""
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


_UploadStatus_Type.__name__ = "Integer32"
_UploadStatus_Object = MibScalar
uploadStatus = _UploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 3, 1, 5),
    _UploadStatus_Type()
)
uploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uploadStatus.setStatus("mandatory")
_StartupConfigDownload_ObjectIdentity = ObjectIdentity
startupConfigDownload = _StartupConfigDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 3, 3, 2)
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
    (1, 3, 6, 1, 4, 1, 4935, 3, 3, 2, 1),
    _DownloadExecute_Type()
)
downloadExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadExecute.setStatus("mandatory")


class _DownloadTftpServerAddress_Type(OctetString):
    """Custom type downloadTftpServerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DownloadTftpServerAddress_Type.__name__ = "OctetString"
_DownloadTftpServerAddress_Object = MibScalar
downloadTftpServerAddress = _DownloadTftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 3, 2, 2),
    _DownloadTftpServerAddress_Type()
)
downloadTftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadTftpServerAddress.setStatus("mandatory")


class _DownloadTftpServerPort_Type(Integer32):
    """Custom type downloadTftpServerPort based on Integer32"""
    defaultValue = 69

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DownloadTftpServerPort_Type.__name__ = "Integer32"
_DownloadTftpServerPort_Object = MibScalar
downloadTftpServerPort = _DownloadTftpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 3, 2, 3),
    _DownloadTftpServerPort_Type()
)
downloadTftpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadTftpServerPort.setStatus("current")


class _DownloadTftpServerPath_Type(OctetString):
    """Custom type downloadTftpServerPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DownloadTftpServerPath_Type.__name__ = "OctetString"
_DownloadTftpServerPath_Object = MibScalar
downloadTftpServerPath = _DownloadTftpServerPath_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 3, 2, 4),
    _DownloadTftpServerPath_Type()
)
downloadTftpServerPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downloadTftpServerPath.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 4935, 3, 3, 2, 5),
    _DownloadStatus_Type()
)
downloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downloadStatus.setStatus("mandatory")
_Firmware_ObjectIdentity = ObjectIdentity
firmware = _Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 3, 4)
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
    (1, 3, 6, 1, 4, 1, 4935, 3, 4, 1),
    _FirmwareLoadExecute_Type()
)
firmwareLoadExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareLoadExecute.setStatus("mandatory")


class _FirmwareTftpServerAddress_Type(OctetString):
    """Custom type firmwareTftpServerAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FirmwareTftpServerAddress_Type.__name__ = "OctetString"
_FirmwareTftpServerAddress_Object = MibScalar
firmwareTftpServerAddress = _FirmwareTftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 4, 2),
    _FirmwareTftpServerAddress_Type()
)
firmwareTftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareTftpServerAddress.setStatus("mandatory")


class _FirmwareTftpServerPort_Type(Integer32):
    """Custom type firmwareTftpServerPort based on Integer32"""
    defaultValue = 69

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FirmwareTftpServerPort_Type.__name__ = "Integer32"
_FirmwareTftpServerPort_Object = MibScalar
firmwareTftpServerPort = _FirmwareTftpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 4, 3),
    _FirmwareTftpServerPort_Type()
)
firmwareTftpServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareTftpServerPort.setStatus("current")


class _FirmwareTftpServerPath_Type(OctetString):
    """Custom type firmwareTftpServerPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FirmwareTftpServerPath_Type.__name__ = "OctetString"
_FirmwareTftpServerPath_Object = MibScalar
firmwareTftpServerPath = _FirmwareTftpServerPath_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 4, 4),
    _FirmwareTftpServerPath_Type()
)
firmwareTftpServerPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareTftpServerPath.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 4935, 3, 4, 5),
    _FirmwareLoadStatus_Type()
)
firmwareLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareLoadStatus.setStatus("mandatory")
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 3, 5)
)
_Mediatrix1400_2400_ObjectIdentity = ObjectIdentity
mediatrix1400_2400 = _Mediatrix1400_2400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 3, 5, 2)
)
_Mediatrix1500_1600_2500_2600_ObjectIdentity = ObjectIdentity
mediatrix1500_1600_2500_2600 = _Mediatrix1500_1600_2500_2600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 3, 5, 3)
)
_Performance_ObjectIdentity = ObjectIdentity
performance = _Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70)
)
_Cpu_ObjectIdentity = ObjectIdentity
cpu = _Cpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 10)
)
_CpuNumber_Type = Integer32
_CpuNumber_Object = MibScalar
cpuNumber = _CpuNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 10, 1),
    _CpuNumber_Type()
)
cpuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuNumber.setStatus("mandatory")
_CpuTable_Object = MibTable
cpuTable = _CpuTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 10, 2)
)
if mibBuilder.loadTexts:
    cpuTable.setStatus("mandatory")
_CpuEntry_Object = MibTableRow
cpuEntry = _CpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 10, 2, 1)
)
cpuEntry.setIndexNames(
    (0, "MX-DIGITAL-PRODUCTS-MIB", "cpuDescr"),
)
if mibBuilder.loadTexts:
    cpuEntry.setStatus("mandatory")
_CpuDescr_Type = DisplayString
_CpuDescr_Object = MibTableColumn
cpuDescr = _CpuDescr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 10, 2, 1, 1),
    _CpuDescr_Type()
)
cpuDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuDescr.setStatus("mandatory")
_CpuWorkloadCurrent_Type = Gauge32
_CpuWorkloadCurrent_Object = MibTableColumn
cpuWorkloadCurrent = _CpuWorkloadCurrent_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 10, 2, 1, 2),
    _CpuWorkloadCurrent_Type()
)
cpuWorkloadCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuWorkloadCurrent.setStatus("mandatory")
_CpuWorkload1MinuteAverage_Type = Gauge32
_CpuWorkload1MinuteAverage_Object = MibTableColumn
cpuWorkload1MinuteAverage = _CpuWorkload1MinuteAverage_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 10, 2, 1, 3),
    _CpuWorkload1MinuteAverage_Type()
)
cpuWorkload1MinuteAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuWorkload1MinuteAverage.setStatus("mandatory")
_CpuWorkload5MinuteAverage_Type = Gauge32
_CpuWorkload5MinuteAverage_Object = MibTableColumn
cpuWorkload5MinuteAverage = _CpuWorkload5MinuteAverage_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 10, 2, 1, 4),
    _CpuWorkload5MinuteAverage_Type()
)
cpuWorkload5MinuteAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuWorkload5MinuteAverage.setStatus("mandatory")
_Memory_ObjectIdentity = ObjectIdentity
memory = _Memory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 20)
)
_MemoryPoolNumber_Type = Integer32
_MemoryPoolNumber_Object = MibScalar
memoryPoolNumber = _MemoryPoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 20, 1),
    _MemoryPoolNumber_Type()
)
memoryPoolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryPoolNumber.setStatus("mandatory")
_MemoryPoolTable_Object = MibTable
memoryPoolTable = _MemoryPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 20, 2)
)
if mibBuilder.loadTexts:
    memoryPoolTable.setStatus("mandatory")
_MemoryPoolEntry_Object = MibTableRow
memoryPoolEntry = _MemoryPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 20, 2, 1)
)
memoryPoolEntry.setIndexNames(
    (0, "MX-DIGITAL-PRODUCTS-MIB", "memDescr"),
)
if mibBuilder.loadTexts:
    memoryPoolEntry.setStatus("mandatory")
_MemDescr_Type = DisplayString
_MemDescr_Object = MibTableColumn
memDescr = _MemDescr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 20, 2, 1, 1),
    _MemDescr_Type()
)
memDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memDescr.setStatus("mandatory")
_MemTotalBytes_Type = Integer32
_MemTotalBytes_Object = MibTableColumn
memTotalBytes = _MemTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 20, 2, 1, 2),
    _MemTotalBytes_Type()
)
memTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalBytes.setStatus("optional")
_MemAllocatedBytes_Type = Integer32
_MemAllocatedBytes_Object = MibTableColumn
memAllocatedBytes = _MemAllocatedBytes_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 20, 2, 1, 3),
    _MemAllocatedBytes_Type()
)
memAllocatedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAllocatedBytes.setStatus("mandatory")
_MemFreeBytes_Type = Integer32
_MemFreeBytes_Object = MibTableColumn
memFreeBytes = _MemFreeBytes_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 20, 2, 1, 4),
    _MemFreeBytes_Type()
)
memFreeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memFreeBytes.setStatus("mandatory")
_MemLargestFreeBlock_Type = Integer32
_MemLargestFreeBlock_Object = MibTableColumn
memLargestFreeBlock = _MemLargestFreeBlock_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 20, 2, 1, 5),
    _MemLargestFreeBlock_Type()
)
memLargestFreeBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memLargestFreeBlock.setStatus("mandatory")
_MemAllocatedBlocks_Type = Integer32
_MemAllocatedBlocks_Object = MibTableColumn
memAllocatedBlocks = _MemAllocatedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 20, 2, 1, 6),
    _MemAllocatedBlocks_Type()
)
memAllocatedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAllocatedBlocks.setStatus("mandatory")
_MemFreeBlocks_Type = Integer32
_MemFreeBlocks_Object = MibTableColumn
memFreeBlocks = _MemFreeBlocks_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 20, 2, 1, 7),
    _MemFreeBlocks_Type()
)
memFreeBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memFreeBlocks.setStatus("mandatory")
_Temperature_ObjectIdentity = ObjectIdentity
temperature = _Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 30)
)
_TempProbeNumber_Type = Integer32
_TempProbeNumber_Object = MibScalar
tempProbeNumber = _TempProbeNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 30, 1),
    _TempProbeNumber_Type()
)
tempProbeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempProbeNumber.setStatus("mandatory")
_TempProbeTable_Object = MibTable
tempProbeTable = _TempProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 30, 2)
)
if mibBuilder.loadTexts:
    tempProbeTable.setStatus("mandatory")
_TempProbeEntry_Object = MibTableRow
tempProbeEntry = _TempProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 30, 2, 1)
)
tempProbeEntry.setIndexNames(
    (0, "MX-DIGITAL-PRODUCTS-MIB", "tempProbeDescr"),
)
if mibBuilder.loadTexts:
    tempProbeEntry.setStatus("mandatory")
_TempProbeDescr_Type = DisplayString
_TempProbeDescr_Object = MibTableColumn
tempProbeDescr = _TempProbeDescr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 30, 2, 1, 1),
    _TempProbeDescr_Type()
)
tempProbeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempProbeDescr.setStatus("mandatory")
_CurrentDegreesCelsius_Type = Gauge32
_CurrentDegreesCelsius_Object = MibTableColumn
currentDegreesCelsius = _CurrentDegreesCelsius_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 30, 2, 1, 2),
    _CurrentDegreesCelsius_Type()
)
currentDegreesCelsius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentDegreesCelsius.setStatus("mandatory")
_Gateway_ObjectIdentity = ObjectIdentity
gateway = _Gateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 40)
)
_GwNumber_Type = Integer32
_GwNumber_Object = MibScalar
gwNumber = _GwNumber_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 40, 1),
    _GwNumber_Type()
)
gwNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwNumber.setStatus("mandatory")
_GwTable_Object = MibTable
gwTable = _GwTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 40, 2)
)
if mibBuilder.loadTexts:
    gwTable.setStatus("mandatory")
_GwEntry_Object = MibTableRow
gwEntry = _GwEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 40, 2, 1)
)
gwEntry.setIndexNames(
    (0, "MX-DIGITAL-PRODUCTS-MIB", "gwDescr"),
)
if mibBuilder.loadTexts:
    gwEntry.setStatus("mandatory")
_GwDescr_Type = DisplayString
_GwDescr_Object = MibTableColumn
gwDescr = _GwDescr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 40, 2, 1, 1),
    _GwDescr_Type()
)
gwDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwDescr.setStatus("mandatory")
_GwCurrentConnectedCalls_Type = Gauge32
_GwCurrentConnectedCalls_Object = MibTableColumn
gwCurrentConnectedCalls = _GwCurrentConnectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 40, 2, 1, 2),
    _GwCurrentConnectedCalls_Type()
)
gwCurrentConnectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwCurrentConnectedCalls.setStatus("mandatory")
_GwCurrentOngoingCalls_Type = Gauge32
_GwCurrentOngoingCalls_Object = MibTableColumn
gwCurrentOngoingCalls = _GwCurrentOngoingCalls_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 40, 2, 1, 3),
    _GwCurrentOngoingCalls_Type()
)
gwCurrentOngoingCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwCurrentOngoingCalls.setStatus("mandatory")
_GwTotalAccumulatedCalls_Type = Counter32
_GwTotalAccumulatedCalls_Object = MibTableColumn
gwTotalAccumulatedCalls = _GwTotalAccumulatedCalls_Object(
    (1, 3, 6, 1, 4, 1, 4935, 3, 70, 40, 2, 1, 4),
    _GwTotalAccumulatedCalls_Type()
)
gwTotalAccumulatedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwTotalAccumulatedCalls.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-DIGITAL-PRODUCTS-MIB",
    **{"mediatrixDigitalProducts": mediatrixDigitalProducts,
       "sysinfo": sysinfo,
       "serialNumber": serialNumber,
       "hwRelease": hwRelease,
       "hwVersion": hwVersion,
       "swVersion": swVersion,
       "productName": productName,
       "admin": admin,
       "deviceReload": deviceReload,
       "saveRunningConfig": saveRunningConfig,
       "config": config,
       "startupConfigUpload": startupConfigUpload,
       "uploadExecute": uploadExecute,
       "uploadTftpServerAddress": uploadTftpServerAddress,
       "uploadTftpServerPort": uploadTftpServerPort,
       "uploadTftpServerPath": uploadTftpServerPath,
       "uploadStatus": uploadStatus,
       "startupConfigDownload": startupConfigDownload,
       "downloadExecute": downloadExecute,
       "downloadTftpServerAddress": downloadTftpServerAddress,
       "downloadTftpServerPort": downloadTftpServerPort,
       "downloadTftpServerPath": downloadTftpServerPath,
       "downloadStatus": downloadStatus,
       "firmware": firmware,
       "firmwareLoadExecute": firmwareLoadExecute,
       "firmwareTftpServerAddress": firmwareTftpServerAddress,
       "firmwareTftpServerPort": firmwareTftpServerPort,
       "firmwareTftpServerPath": firmwareTftpServerPath,
       "firmwareLoadStatus": firmwareLoadStatus,
       "products": products,
       "mediatrix1400-2400": mediatrix1400_2400,
       "mediatrix1500-1600-2500-2600": mediatrix1500_1600_2500_2600,
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
       "gateway": gateway,
       "gwNumber": gwNumber,
       "gwTable": gwTable,
       "gwEntry": gwEntry,
       "gwDescr": gwDescr,
       "gwCurrentConnectedCalls": gwCurrentConnectedCalls,
       "gwCurrentOngoingCalls": gwCurrentOngoingCalls,
       "gwTotalAccumulatedCalls": gwTotalAccumulatedCalls}
)
