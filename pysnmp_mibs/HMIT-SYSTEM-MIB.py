# SNMP MIB module (HMIT-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HMIT-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:53:29 2025
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

(hmITMgmt,) = mibBuilder.importSymbols(
    "HMIT-SMI",
    "hmITMgmt")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hmITSystemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600)
)
if mibBuilder.loadTexts:
    hmITSystemMib.setRevisions(
        ("2010-01-08 17:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmITSystemTrap_ObjectIdentity = ObjectIdentity
hmITSystemTrap = _HmITSystemTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 0)
)
_HmITSysInfoMib_ObjectIdentity = ObjectIdentity
hmITSysInfoMib = _HmITSysInfoMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 1)
)


class _SysVoltage_Type(Integer32):
    """Custom type sysVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SysVoltage_Type.__name__ = "Integer32"
_SysVoltage_Object = MibScalar
sysVoltage = _SysVoltage_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 1, 1),
    _SysVoltage_Type()
)
sysVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysVoltage.setStatus("current")
if mibBuilder.loadTexts:
    sysVoltage.setUnits("mV")


class _SysCurrent_Type(Integer32):
    """Custom type sysCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SysCurrent_Type.__name__ = "Integer32"
_SysCurrent_Object = MibScalar
sysCurrent = _SysCurrent_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 1, 2),
    _SysCurrent_Type()
)
sysCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCurrent.setStatus("current")
if mibBuilder.loadTexts:
    sysCurrent.setUnits("mA")
_HmITSysMpuMib_ObjectIdentity = ObjectIdentity
hmITSysMpuMib = _HmITSysMpuMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2)
)
_MpuInfoTable_Object = MibTable
mpuInfoTable = _MpuInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1)
)
if mibBuilder.loadTexts:
    mpuInfoTable.setStatus("current")
_MpuInfoEntry_Object = MibTableRow
mpuInfoEntry = _MpuInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1)
)
mpuInfoEntry.setIndexNames(
    (0, "HMIT-SYSTEM-MIB", "mpuIndex"),
)
if mibBuilder.loadTexts:
    mpuInfoEntry.setStatus("current")


class _MpuIndex_Type(Integer32):
    """Custom type mpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MpuIndex_Type.__name__ = "Integer32"
_MpuIndex_Object = MibTableColumn
mpuIndex = _MpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 1),
    _MpuIndex_Type()
)
mpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuIndex.setStatus("current")


class _MpuType_Type(Gauge32):
    """Custom type mpuType based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MpuType_Type.__name__ = "Gauge32"
_MpuType_Object = MibTableColumn
mpuType = _MpuType_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 2),
    _MpuType_Type()
)
mpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuType.setStatus("current")


class _MpuDescription_Type(DisplayString):
    """Custom type mpuDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MpuDescription_Type.__name__ = "DisplayString"
_MpuDescription_Object = MibTableColumn
mpuDescription = _MpuDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 3),
    _MpuDescription_Type()
)
mpuDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpuDescription.setStatus("current")


class _MpuSerialNumber_Type(DisplayString):
    """Custom type mpuSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MpuSerialNumber_Type.__name__ = "DisplayString"
_MpuSerialNumber_Object = MibTableColumn
mpuSerialNumber = _MpuSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 4),
    _MpuSerialNumber_Type()
)
mpuSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuSerialNumber.setStatus("current")


class _MpuSoftwareVersion_Type(DisplayString):
    """Custom type mpuSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MpuSoftwareVersion_Type.__name__ = "DisplayString"
_MpuSoftwareVersion_Object = MibTableColumn
mpuSoftwareVersion = _MpuSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 5),
    _MpuSoftwareVersion_Type()
)
mpuSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuSoftwareVersion.setStatus("current")
_MpuHardwareVersion_Type = DisplayString
_MpuHardwareVersion_Object = MibTableColumn
mpuHardwareVersion = _MpuHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 6),
    _MpuHardwareVersion_Type()
)
mpuHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuHardwareVersion.setStatus("current")
_MpuFPGAVersion_Type = DisplayString
_MpuFPGAVersion_Object = MibTableColumn
mpuFPGAVersion = _MpuFPGAVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 7),
    _MpuFPGAVersion_Type()
)
mpuFPGAVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuFPGAVersion.setStatus("current")


class _MpuMonitorVersion_Type(DisplayString):
    """Custom type mpuMonitorVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MpuMonitorVersion_Type.__name__ = "DisplayString"
_MpuMonitorVersion_Object = MibTableColumn
mpuMonitorVersion = _MpuMonitorVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 8),
    _MpuMonitorVersion_Type()
)
mpuMonitorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuMonitorVersion.setStatus("current")


class _MpuCMMSoftwareVersion_Type(DisplayString):
    """Custom type mpuCMMSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MpuCMMSoftwareVersion_Type.__name__ = "DisplayString"
_MpuCMMSoftwareVersion_Object = MibTableColumn
mpuCMMSoftwareVersion = _MpuCMMSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 9),
    _MpuCMMSoftwareVersion_Type()
)
mpuCMMSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuCMMSoftwareVersion.setStatus("current")


class _MpuCMMHardwareVersion_Type(DisplayString):
    """Custom type mpuCMMHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MpuCMMHardwareVersion_Type.__name__ = "DisplayString"
_MpuCMMHardwareVersion_Object = MibTableColumn
mpuCMMHardwareVersion = _MpuCMMHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 10),
    _MpuCMMHardwareVersion_Type()
)
mpuCMMHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuCMMHardwareVersion.setStatus("current")


class _MpuCMMMonitorVersion_Type(DisplayString):
    """Custom type mpuCMMMonitorVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MpuCMMMonitorVersion_Type.__name__ = "DisplayString"
_MpuCMMMonitorVersion_Object = MibTableColumn
mpuCMMMonitorVersion = _MpuCMMMonitorVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 11),
    _MpuCMMMonitorVersion_Type()
)
mpuCMMMonitorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuCMMMonitorVersion.setStatus("current")
_MpuFlashTotalBytes_Type = Counter64
_MpuFlashTotalBytes_Object = MibTableColumn
mpuFlashTotalBytes = _MpuFlashTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 12),
    _MpuFlashTotalBytes_Type()
)
mpuFlashTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuFlashTotalBytes.setStatus("current")
_MpuFlashLeftBytes_Type = Counter64
_MpuFlashLeftBytes_Object = MibTableColumn
mpuFlashLeftBytes = _MpuFlashLeftBytes_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 13),
    _MpuFlashLeftBytes_Type()
)
mpuFlashLeftBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuFlashLeftBytes.setStatus("current")


class _MpuWorkingMode_Type(Integer32):
    """Custom type mpuWorkingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("doubleRouter", 3))
    )


_MpuWorkingMode_Type.__name__ = "Integer32"
_MpuWorkingMode_Object = MibTableColumn
mpuWorkingMode = _MpuWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 14),
    _MpuWorkingMode_Type()
)
mpuWorkingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuWorkingMode.setStatus("current")


class _MpuOnlineStatus_Type(Integer32):
    """Custom type mpuOnlineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2))
    )


_MpuOnlineStatus_Type.__name__ = "Integer32"
_MpuOnlineStatus_Object = MibTableColumn
mpuOnlineStatus = _MpuOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 15),
    _MpuOnlineStatus_Type()
)
mpuOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuOnlineStatus.setStatus("current")


class _MpuWorkingStatus_Type(Integer32):
    """Custom type mpuWorkingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_MpuWorkingStatus_Type.__name__ = "Integer32"
_MpuWorkingStatus_Object = MibTableColumn
mpuWorkingStatus = _MpuWorkingStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 16),
    _MpuWorkingStatus_Type()
)
mpuWorkingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuWorkingStatus.setStatus("current")


class _MpuPowerStatus_Type(Integer32):
    """Custom type mpuPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_MpuPowerStatus_Type.__name__ = "Integer32"
_MpuPowerStatus_Object = MibTableColumn
mpuPowerStatus = _MpuPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 17),
    _MpuPowerStatus_Type()
)
mpuPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuPowerStatus.setStatus("current")


class _MpuSynchronizationStatus_Type(Integer32):
    """Custom type mpuSynchronizationStatus based on Integer32"""
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
        *(("batchSync", 1),
          ("realtimeSync", 2),
          ("noSlave", 3),
          ("abnormal", 4))
    )


_MpuSynchronizationStatus_Type.__name__ = "Integer32"
_MpuSynchronizationStatus_Object = MibTableColumn
mpuSynchronizationStatus = _MpuSynchronizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 18),
    _MpuSynchronizationStatus_Type()
)
mpuSynchronizationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuSynchronizationStatus.setStatus("current")


class _MpuCFStatus_Type(Integer32):
    """Custom type mpuCFStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2))
    )


_MpuCFStatus_Type.__name__ = "Integer32"
_MpuCFStatus_Object = MibTableColumn
mpuCFStatus = _MpuCFStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 19),
    _MpuCFStatus_Type()
)
mpuCFStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuCFStatus.setStatus("current")


class _MpuTemperature_Type(Integer32):
    """Custom type mpuTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 1000),
    )


_MpuTemperature_Type.__name__ = "Integer32"
_MpuTemperature_Object = MibTableColumn
mpuTemperature = _MpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 20),
    _MpuTemperature_Type()
)
mpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuTemperature.setStatus("current")


class _MpuSubSlotNumber_Type(Integer32):
    """Custom type mpuSubSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MpuSubSlotNumber_Type.__name__ = "Integer32"
_MpuSubSlotNumber_Object = MibTableColumn
mpuSubSlotNumber = _MpuSubSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 21),
    _MpuSubSlotNumber_Type()
)
mpuSubSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuSubSlotNumber.setStatus("current")


class _HmITSysMpuUserSerialNumber_Type(DisplayString):
    """Custom type hmITSysMpuUserSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HmITSysMpuUserSerialNumber_Type.__name__ = "DisplayString"
_HmITSysMpuUserSerialNumber_Object = MibTableColumn
hmITSysMpuUserSerialNumber = _HmITSysMpuUserSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 22),
    _HmITSysMpuUserSerialNumber_Type()
)
hmITSysMpuUserSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmITSysMpuUserSerialNumber.setStatus("current")


class _MpuModel_Type(DisplayString):
    """Custom type mpuModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MpuModel_Type.__name__ = "DisplayString"
_MpuModel_Object = MibTableColumn
mpuModel = _MpuModel_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 2, 1, 1, 23),
    _MpuModel_Type()
)
mpuModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpuModel.setStatus("current")
_HmITSysSubSlotMib_ObjectIdentity = ObjectIdentity
hmITSysSubSlotMib = _HmITSysSubSlotMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 5)
)
_SubSlotTable_Object = MibTable
subSlotTable = _SubSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 5, 1)
)
if mibBuilder.loadTexts:
    subSlotTable.setStatus("current")
_SubSlotEntry_Object = MibTableRow
subSlotEntry = _SubSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 5, 1, 1)
)
subSlotEntry.setIndexNames(
    (0, "HMIT-SYSTEM-MIB", "subSlotParentIndex"),
    (0, "HMIT-SYSTEM-MIB", "subSlotIndex"),
)
if mibBuilder.loadTexts:
    subSlotEntry.setStatus("current")


class _SubSlotParentIndex_Type(Integer32):
    """Custom type subSlotParentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubSlotParentIndex_Type.__name__ = "Integer32"
_SubSlotParentIndex_Object = MibTableColumn
subSlotParentIndex = _SubSlotParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 5, 1, 1, 1),
    _SubSlotParentIndex_Type()
)
subSlotParentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subSlotParentIndex.setStatus("current")


class _SubSlotIndex_Type(Integer32):
    """Custom type subSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubSlotIndex_Type.__name__ = "Integer32"
_SubSlotIndex_Object = MibTableColumn
subSlotIndex = _SubSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 5, 1, 1, 2),
    _SubSlotIndex_Type()
)
subSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subSlotIndex.setStatus("current")


class _SubSlotCardType_Type(Gauge32):
    """Custom type subSlotCardType based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SubSlotCardType_Type.__name__ = "Gauge32"
_SubSlotCardType_Object = MibTableColumn
subSlotCardType = _SubSlotCardType_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 5, 1, 1, 3),
    _SubSlotCardType_Type()
)
subSlotCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subSlotCardType.setStatus("current")


class _SubSlotPortNumber_Type(Integer32):
    """Custom type subSlotPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SubSlotPortNumber_Type.__name__ = "Integer32"
_SubSlotPortNumber_Object = MibTableColumn
subSlotPortNumber = _SubSlotPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 5, 1, 1, 4),
    _SubSlotPortNumber_Type()
)
subSlotPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subSlotPortNumber.setStatus("current")


class _SubSlotOnlineStatus_Type(Integer32):
    """Custom type subSlotOnlineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2))
    )


_SubSlotOnlineStatus_Type.__name__ = "Integer32"
_SubSlotOnlineStatus_Object = MibTableColumn
subSlotOnlineStatus = _SubSlotOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 5, 1, 1, 5),
    _SubSlotOnlineStatus_Type()
)
subSlotOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subSlotOnlineStatus.setStatus("current")
_HmITSysPortMib_ObjectIdentity = ObjectIdentity
hmITSysPortMib = _HmITSysPortMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 6)
)
_PortInfoTable_Object = MibTable
portInfoTable = _PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 6, 1)
)
if mibBuilder.loadTexts:
    portInfoTable.setStatus("current")
_PortInfoEntry_Object = MibTableRow
portInfoEntry = _PortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 6, 1, 1)
)
portInfoEntry.setIndexNames(
    (0, "HMIT-SYSTEM-MIB", "portSlotIndex"),
    (0, "HMIT-SYSTEM-MIB", "portSubSlotIndex"),
    (0, "HMIT-SYSTEM-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portInfoEntry.setStatus("current")


class _PortSlotIndex_Type(Integer32):
    """Custom type portSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortSlotIndex_Type.__name__ = "Integer32"
_PortSlotIndex_Object = MibTableColumn
portSlotIndex = _PortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 6, 1, 1, 1),
    _PortSlotIndex_Type()
)
portSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSlotIndex.setStatus("current")


class _PortSubSlotIndex_Type(Integer32):
    """Custom type portSubSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortSubSlotIndex_Type.__name__ = "Integer32"
_PortSubSlotIndex_Object = MibTableColumn
portSubSlotIndex = _PortSubSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 6, 1, 1, 2),
    _PortSubSlotIndex_Type()
)
portSubSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSubSlotIndex.setStatus("current")


class _PortIndex_Type(Integer32):
    """Custom type portIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortIndex_Type.__name__ = "Integer32"
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 6, 1, 1, 3),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 6, 1, 1, 4),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("current")


class _PortLinkStatus_Type(Integer32):
    """Custom type portLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("loop", 3))
    )


_PortLinkStatus_Type.__name__ = "Integer32"
_PortLinkStatus_Object = MibTableColumn
portLinkStatus = _PortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 6, 1, 1, 5),
    _PortLinkStatus_Type()
)
portLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLinkStatus.setStatus("current")


class _PortOnlineStatus_Type(Integer32):
    """Custom type portOnlineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2))
    )


_PortOnlineStatus_Type.__name__ = "Integer32"
_PortOnlineStatus_Object = MibTableColumn
portOnlineStatus = _PortOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 6, 1, 1, 6),
    _PortOnlineStatus_Type()
)
portOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOnlineStatus.setStatus("current")
_HmITSysPowerMib_ObjectIdentity = ObjectIdentity
hmITSysPowerMib = _HmITSysPowerMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7)
)
_PowerInfoTable_Object = MibTable
powerInfoTable = _PowerInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7, 1)
)
if mibBuilder.loadTexts:
    powerInfoTable.setStatus("current")
_PowerInfoEntry_Object = MibTableRow
powerInfoEntry = _PowerInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7, 1, 1)
)
powerInfoEntry.setIndexNames(
    (0, "HMIT-SYSTEM-MIB", "powerIndex"),
)
if mibBuilder.loadTexts:
    powerInfoEntry.setStatus("current")


class _PowerIndex_Type(Integer32):
    """Custom type powerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PowerIndex_Type.__name__ = "Integer32"
_PowerIndex_Object = MibTableColumn
powerIndex = _PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7, 1, 1, 1),
    _PowerIndex_Type()
)
powerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerIndex.setStatus("current")


class _PowerType_Type(Integer32):
    """Custom type powerType based on Integer32"""
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
        *(("alternatingNonIntelligent", 1),
          ("directNonIntelligent", 2),
          ("alternatingIntelligent", 3),
          ("directIntelligent", 4))
    )


_PowerType_Type.__name__ = "Integer32"
_PowerType_Object = MibTableColumn
powerType = _PowerType_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7, 1, 1, 2),
    _PowerType_Type()
)
powerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerType.setStatus("current")


class _PowerDescription_Type(DisplayString):
    """Custom type powerDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PowerDescription_Type.__name__ = "DisplayString"
_PowerDescription_Object = MibTableColumn
powerDescription = _PowerDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7, 1, 1, 3),
    _PowerDescription_Type()
)
powerDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerDescription.setStatus("current")


class _PowerSerialNumber_Type(DisplayString):
    """Custom type powerSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PowerSerialNumber_Type.__name__ = "DisplayString"
_PowerSerialNumber_Object = MibTableColumn
powerSerialNumber = _PowerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7, 1, 1, 4),
    _PowerSerialNumber_Type()
)
powerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSerialNumber.setStatus("current")


class _PowerCMMSoftwareVersion_Type(DisplayString):
    """Custom type powerCMMSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PowerCMMSoftwareVersion_Type.__name__ = "DisplayString"
_PowerCMMSoftwareVersion_Object = MibTableColumn
powerCMMSoftwareVersion = _PowerCMMSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7, 1, 1, 5),
    _PowerCMMSoftwareVersion_Type()
)
powerCMMSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerCMMSoftwareVersion.setStatus("current")


class _PowerCMMHardwareVersion_Type(DisplayString):
    """Custom type powerCMMHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PowerCMMHardwareVersion_Type.__name__ = "DisplayString"
_PowerCMMHardwareVersion_Object = MibTableColumn
powerCMMHardwareVersion = _PowerCMMHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7, 1, 1, 6),
    _PowerCMMHardwareVersion_Type()
)
powerCMMHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerCMMHardwareVersion.setStatus("current")


class _PowerCMMMonitorVersion_Type(DisplayString):
    """Custom type powerCMMMonitorVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PowerCMMMonitorVersion_Type.__name__ = "DisplayString"
_PowerCMMMonitorVersion_Object = MibTableColumn
powerCMMMonitorVersion = _PowerCMMMonitorVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7, 1, 1, 7),
    _PowerCMMMonitorVersion_Type()
)
powerCMMMonitorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerCMMMonitorVersion.setStatus("current")


class _PowerOnlineStatus_Type(Integer32):
    """Custom type powerOnlineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2))
    )


_PowerOnlineStatus_Type.__name__ = "Integer32"
_PowerOnlineStatus_Object = MibTableColumn
powerOnlineStatus = _PowerOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7, 1, 1, 8),
    _PowerOnlineStatus_Type()
)
powerOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerOnlineStatus.setStatus("current")


class _PowerWorkingStatus_Type(Integer32):
    """Custom type powerWorkingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_PowerWorkingStatus_Type.__name__ = "Integer32"
_PowerWorkingStatus_Object = MibTableColumn
powerWorkingStatus = _PowerWorkingStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7, 1, 1, 9),
    _PowerWorkingStatus_Type()
)
powerWorkingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerWorkingStatus.setStatus("current")


class _PowerAlarmStatus_Type(Integer32):
    """Custom type powerAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_PowerAlarmStatus_Type.__name__ = "Integer32"
_PowerAlarmStatus_Object = MibTableColumn
powerAlarmStatus = _PowerAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7, 1, 1, 10),
    _PowerAlarmStatus_Type()
)
powerAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerAlarmStatus.setStatus("current")


class _PowerVoltageInput_Type(Integer32):
    """Custom type powerVoltageInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PowerVoltageInput_Type.__name__ = "Integer32"
_PowerVoltageInput_Object = MibTableColumn
powerVoltageInput = _PowerVoltageInput_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7, 1, 1, 11),
    _PowerVoltageInput_Type()
)
powerVoltageInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerVoltageInput.setStatus("current")
if mibBuilder.loadTexts:
    powerVoltageInput.setUnits("mV")


class _PowerVoltageOutput_Type(Integer32):
    """Custom type powerVoltageOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PowerVoltageOutput_Type.__name__ = "Integer32"
_PowerVoltageOutput_Object = MibTableColumn
powerVoltageOutput = _PowerVoltageOutput_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7, 1, 1, 12),
    _PowerVoltageOutput_Type()
)
powerVoltageOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerVoltageOutput.setStatus("current")
if mibBuilder.loadTexts:
    powerVoltageOutput.setUnits("mV")


class _PowerCurrentInput_Type(Integer32):
    """Custom type powerCurrentInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PowerCurrentInput_Type.__name__ = "Integer32"
_PowerCurrentInput_Object = MibTableColumn
powerCurrentInput = _PowerCurrentInput_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7, 1, 1, 13),
    _PowerCurrentInput_Type()
)
powerCurrentInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerCurrentInput.setStatus("current")
if mibBuilder.loadTexts:
    powerCurrentInput.setUnits("mA")


class _PowerCurrentOutput_Type(Integer32):
    """Custom type powerCurrentOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PowerCurrentOutput_Type.__name__ = "Integer32"
_PowerCurrentOutput_Object = MibTableColumn
powerCurrentOutput = _PowerCurrentOutput_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7, 1, 1, 14),
    _PowerCurrentOutput_Type()
)
powerCurrentOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerCurrentOutput.setStatus("current")
if mibBuilder.loadTexts:
    powerCurrentOutput.setUnits("mA")


class _PowerUserSerialNumber_Type(DisplayString):
    """Custom type powerUserSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_PowerUserSerialNumber_Type.__name__ = "DisplayString"
_PowerUserSerialNumber_Object = MibTableColumn
powerUserSerialNumber = _PowerUserSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7, 1, 1, 15),
    _PowerUserSerialNumber_Type()
)
powerUserSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUserSerialNumber.setStatus("current")


class _PowerName_Type(DisplayString):
    """Custom type powerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_PowerName_Type.__name__ = "DisplayString"
_PowerName_Object = MibTableColumn
powerName = _PowerName_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 7, 1, 1, 16),
    _PowerName_Type()
)
powerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerName.setStatus("current")
_HmITSysFanCardMib_ObjectIdentity = ObjectIdentity
hmITSysFanCardMib = _HmITSysFanCardMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8)
)
_FanCardInfoTable_Object = MibTable
fanCardInfoTable = _FanCardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 1)
)
if mibBuilder.loadTexts:
    fanCardInfoTable.setStatus("current")
_FanCardInfoEntry_Object = MibTableRow
fanCardInfoEntry = _FanCardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 1, 1)
)
fanCardInfoEntry.setIndexNames(
    (0, "HMIT-SYSTEM-MIB", "fanCardIndex"),
)
if mibBuilder.loadTexts:
    fanCardInfoEntry.setStatus("current")


class _FanCardIndex_Type(Integer32):
    """Custom type fanCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FanCardIndex_Type.__name__ = "Integer32"
_FanCardIndex_Object = MibTableColumn
fanCardIndex = _FanCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 1, 1, 1),
    _FanCardIndex_Type()
)
fanCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCardIndex.setStatus("current")


class _FanCardDescription_Type(DisplayString):
    """Custom type fanCardDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_FanCardDescription_Type.__name__ = "DisplayString"
_FanCardDescription_Object = MibTableColumn
fanCardDescription = _FanCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 1, 1, 2),
    _FanCardDescription_Type()
)
fanCardDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanCardDescription.setStatus("current")


class _FanCardSerialNumber_Type(DisplayString):
    """Custom type fanCardSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FanCardSerialNumber_Type.__name__ = "DisplayString"
_FanCardSerialNumber_Object = MibTableColumn
fanCardSerialNumber = _FanCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 1, 1, 3),
    _FanCardSerialNumber_Type()
)
fanCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCardSerialNumber.setStatus("current")


class _FanCardCMMSoftwareVersion_Type(DisplayString):
    """Custom type fanCardCMMSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FanCardCMMSoftwareVersion_Type.__name__ = "DisplayString"
_FanCardCMMSoftwareVersion_Object = MibTableColumn
fanCardCMMSoftwareVersion = _FanCardCMMSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 1, 1, 4),
    _FanCardCMMSoftwareVersion_Type()
)
fanCardCMMSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCardCMMSoftwareVersion.setStatus("current")


class _FanCardCMMHardwareVersion_Type(DisplayString):
    """Custom type fanCardCMMHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FanCardCMMHardwareVersion_Type.__name__ = "DisplayString"
_FanCardCMMHardwareVersion_Object = MibTableColumn
fanCardCMMHardwareVersion = _FanCardCMMHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 1, 1, 5),
    _FanCardCMMHardwareVersion_Type()
)
fanCardCMMHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCardCMMHardwareVersion.setStatus("current")


class _FanCardCMMMonitorVersion_Type(DisplayString):
    """Custom type fanCardCMMMonitorVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FanCardCMMMonitorVersion_Type.__name__ = "DisplayString"
_FanCardCMMMonitorVersion_Object = MibTableColumn
fanCardCMMMonitorVersion = _FanCardCMMMonitorVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 1, 1, 6),
    _FanCardCMMMonitorVersion_Type()
)
fanCardCMMMonitorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCardCMMMonitorVersion.setStatus("current")


class _FanCardOnlineStatus_Type(Integer32):
    """Custom type fanCardOnlineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2))
    )


_FanCardOnlineStatus_Type.__name__ = "Integer32"
_FanCardOnlineStatus_Object = MibTableColumn
fanCardOnlineStatus = _FanCardOnlineStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 1, 1, 7),
    _FanCardOnlineStatus_Type()
)
fanCardOnlineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCardOnlineStatus.setStatus("current")


class _FanCardWorkingStatus_Type(Integer32):
    """Custom type fanCardWorkingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_FanCardWorkingStatus_Type.__name__ = "Integer32"
_FanCardWorkingStatus_Object = MibTableColumn
fanCardWorkingStatus = _FanCardWorkingStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 1, 1, 8),
    _FanCardWorkingStatus_Type()
)
fanCardWorkingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCardWorkingStatus.setStatus("current")


class _FanCardAlarmStatus_Type(Integer32):
    """Custom type fanCardAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_FanCardAlarmStatus_Type.__name__ = "Integer32"
_FanCardAlarmStatus_Object = MibTableColumn
fanCardAlarmStatus = _FanCardAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 1, 1, 9),
    _FanCardAlarmStatus_Type()
)
fanCardAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCardAlarmStatus.setStatus("current")


class _FanCardGrps_Type(Integer32):
    """Custom type fanCardGrps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FanCardGrps_Type.__name__ = "Integer32"
_FanCardGrps_Object = MibTableColumn
fanCardGrps = _FanCardGrps_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 1, 1, 10),
    _FanCardGrps_Type()
)
fanCardGrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCardGrps.setStatus("current")


class _FanCardNumPerGrp_Type(Integer32):
    """Custom type fanCardNumPerGrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FanCardNumPerGrp_Type.__name__ = "Integer32"
_FanCardNumPerGrp_Object = MibTableColumn
fanCardNumPerGrp = _FanCardNumPerGrp_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 1, 1, 11),
    _FanCardNumPerGrp_Type()
)
fanCardNumPerGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCardNumPerGrp.setStatus("current")


class _FanCardUserSerialNumber_Type(DisplayString):
    """Custom type fanCardUserSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FanCardUserSerialNumber_Type.__name__ = "DisplayString"
_FanCardUserSerialNumber_Object = MibTableColumn
fanCardUserSerialNumber = _FanCardUserSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 1, 1, 12),
    _FanCardUserSerialNumber_Type()
)
fanCardUserSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCardUserSerialNumber.setStatus("current")


class _FanCardName_Type(DisplayString):
    """Custom type fanCardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FanCardName_Type.__name__ = "DisplayString"
_FanCardName_Object = MibTableColumn
fanCardName = _FanCardName_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 1, 1, 13),
    _FanCardName_Type()
)
fanCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCardName.setStatus("current")
_FanInfoTable_Object = MibTable
fanInfoTable = _FanInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 2)
)
if mibBuilder.loadTexts:
    fanInfoTable.setStatus("current")
_FanInfoEntry_Object = MibTableRow
fanInfoEntry = _FanInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 2, 1)
)
fanInfoEntry.setIndexNames(
    (0, "HMIT-SYSTEM-MIB", "fanInfoIndex"),
    (0, "HMIT-SYSTEM-MIB", "fanIndex"),
)
if mibBuilder.loadTexts:
    fanInfoEntry.setStatus("current")


class _FanInfoIndex_Type(Integer32):
    """Custom type fanInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FanInfoIndex_Type.__name__ = "Integer32"
_FanInfoIndex_Object = MibTableColumn
fanInfoIndex = _FanInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 2, 1, 1),
    _FanInfoIndex_Type()
)
fanInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanInfoIndex.setStatus("current")


class _FanIndex_Type(Integer32):
    """Custom type fanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FanIndex_Type.__name__ = "Integer32"
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 2, 1, 2),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanIndex.setStatus("current")


class _FanStatus_Type(Integer32):
    """Custom type fanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FanStatus_Type.__name__ = "Integer32"
_FanStatus_Object = MibTableColumn
fanStatus = _FanStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 2, 1, 3),
    _FanStatus_Type()
)
fanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanStatus.setStatus("current")


class _FanSpeed_Type(Integer32):
    """Custom type fanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FanSpeed_Type.__name__ = "Integer32"
_FanSpeed_Object = MibTableColumn
fanSpeed = _FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 8, 2, 1, 4),
    _FanSpeed_Type()
)
fanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeed.setStatus("current")
_HmITSysCpuMib_ObjectIdentity = ObjectIdentity
hmITSysCpuMib = _HmITSysCpuMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 9)
)
_CpuUtilizationTable_Object = MibTable
cpuUtilizationTable = _CpuUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 9, 1)
)
if mibBuilder.loadTexts:
    cpuUtilizationTable.setStatus("current")
_CpuUtilizationEntry_Object = MibTableRow
cpuUtilizationEntry = _CpuUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 9, 1, 1)
)
cpuUtilizationEntry.setIndexNames(
    (0, "HMIT-SYSTEM-MIB", "cpuIndex"),
    (0, "HMIT-SYSTEM-MIB", "cpuCoreId"),
)
if mibBuilder.loadTexts:
    cpuUtilizationEntry.setStatus("current")


class _CpuIndex_Type(Integer32):
    """Custom type cpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CpuIndex_Type.__name__ = "Integer32"
_CpuIndex_Object = MibTableColumn
cpuIndex = _CpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 9, 1, 1, 1),
    _CpuIndex_Type()
)
cpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuIndex.setStatus("current")


class _CpuCoreId_Type(Integer32):
    """Custom type cpuCoreId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CpuCoreId_Type.__name__ = "Integer32"
_CpuCoreId_Object = MibTableColumn
cpuCoreId = _CpuCoreId_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 9, 1, 1, 2),
    _CpuCoreId_Type()
)
cpuCoreId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreId.setStatus("current")


class _CpuCoreUtilization_Type(Integer32):
    """Custom type cpuCoreUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuCoreUtilization_Type.__name__ = "Integer32"
_CpuCoreUtilization_Object = MibTableColumn
cpuCoreUtilization = _CpuCoreUtilization_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 9, 1, 1, 3),
    _CpuCoreUtilization_Type()
)
cpuCoreUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCoreUtilization.setStatus("current")
if mibBuilder.loadTexts:
    cpuCoreUtilization.setUnits("%")


class _CpuPeakUtilizationPerMinute_Type(Integer32):
    """Custom type cpuPeakUtilizationPerMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpuPeakUtilizationPerMinute_Type.__name__ = "Integer32"
_CpuPeakUtilizationPerMinute_Object = MibTableColumn
cpuPeakUtilizationPerMinute = _CpuPeakUtilizationPerMinute_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 9, 1, 1, 4),
    _CpuPeakUtilizationPerMinute_Type()
)
cpuPeakUtilizationPerMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPeakUtilizationPerMinute.setStatus("current")
if mibBuilder.loadTexts:
    cpuPeakUtilizationPerMinute.setUnits("%")
_CpuTemperatureTable_Object = MibTable
cpuTemperatureTable = _CpuTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 9, 2)
)
if mibBuilder.loadTexts:
    cpuTemperatureTable.setStatus("current")
_CpuTemperatureEntry_Object = MibTableRow
cpuTemperatureEntry = _CpuTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 9, 2, 1)
)
cpuTemperatureEntry.setIndexNames(
    (0, "HMIT-SYSTEM-MIB", "cpuTemperatureIndex"),
)
if mibBuilder.loadTexts:
    cpuTemperatureEntry.setStatus("current")


class _CpuTemperatureIndex_Type(Integer32):
    """Custom type cpuTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CpuTemperatureIndex_Type.__name__ = "Integer32"
_CpuTemperatureIndex_Object = MibTableColumn
cpuTemperatureIndex = _CpuTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 9, 2, 1, 1),
    _CpuTemperatureIndex_Type()
)
cpuTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTemperatureIndex.setStatus("current")


class _CpuTemperature_Type(Integer32):
    """Custom type cpuTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 1000),
    )


_CpuTemperature_Type.__name__ = "Integer32"
_CpuTemperature_Object = MibTableColumn
cpuTemperature = _CpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 9, 2, 1, 2),
    _CpuTemperature_Type()
)
cpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTemperature.setStatus("current")
if mibBuilder.loadTexts:
    cpuTemperature.setUnits("'C")
_HmITSysMemoryMib_ObjectIdentity = ObjectIdentity
hmITSysMemoryMib = _HmITSysMemoryMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 10)
)
_MemoryTable_Object = MibTable
memoryTable = _MemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 10, 1)
)
if mibBuilder.loadTexts:
    memoryTable.setStatus("current")
_MemoryEntry_Object = MibTableRow
memoryEntry = _MemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 10, 1, 1)
)
memoryEntry.setIndexNames(
    (0, "HMIT-SYSTEM-MIB", "memIndex"),
)
if mibBuilder.loadTexts:
    memoryEntry.setStatus("current")


class _MemIndex_Type(Integer32):
    """Custom type memIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MemIndex_Type.__name__ = "Integer32"
_MemIndex_Object = MibTableColumn
memIndex = _MemIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 10, 1, 1, 1),
    _MemIndex_Type()
)
memIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memIndex.setStatus("current")


class _MemBytesFree_Type(Gauge32):
    """Custom type memBytesFree based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MemBytesFree_Type.__name__ = "Gauge32"
_MemBytesFree_Object = MibTableColumn
memBytesFree = _MemBytesFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 10, 1, 1, 2),
    _MemBytesFree_Type()
)
memBytesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memBytesFree.setStatus("current")


class _MemBlocksFree_Type(Gauge32):
    """Custom type memBlocksFree based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MemBlocksFree_Type.__name__ = "Gauge32"
_MemBlocksFree_Object = MibTableColumn
memBlocksFree = _MemBlocksFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 10, 1, 1, 3),
    _MemBlocksFree_Type()
)
memBlocksFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memBlocksFree.setStatus("current")


class _MemAvgBlockSizeFree_Type(Gauge32):
    """Custom type memAvgBlockSizeFree based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MemAvgBlockSizeFree_Type.__name__ = "Gauge32"
_MemAvgBlockSizeFree_Object = MibTableColumn
memAvgBlockSizeFree = _MemAvgBlockSizeFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 10, 1, 1, 4),
    _MemAvgBlockSizeFree_Type()
)
memAvgBlockSizeFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvgBlockSizeFree.setStatus("current")


class _MemMaxBlockSizeFree_Type(Gauge32):
    """Custom type memMaxBlockSizeFree based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MemMaxBlockSizeFree_Type.__name__ = "Gauge32"
_MemMaxBlockSizeFree_Object = MibTableColumn
memMaxBlockSizeFree = _MemMaxBlockSizeFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 10, 1, 1, 5),
    _MemMaxBlockSizeFree_Type()
)
memMaxBlockSizeFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memMaxBlockSizeFree.setStatus("current")


class _MemBytesAlloc_Type(Gauge32):
    """Custom type memBytesAlloc based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MemBytesAlloc_Type.__name__ = "Gauge32"
_MemBytesAlloc_Object = MibTableColumn
memBytesAlloc = _MemBytesAlloc_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 10, 1, 1, 6),
    _MemBytesAlloc_Type()
)
memBytesAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memBytesAlloc.setStatus("current")


class _MemBlocksAlloc_Type(Gauge32):
    """Custom type memBlocksAlloc based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MemBlocksAlloc_Type.__name__ = "Gauge32"
_MemBlocksAlloc_Object = MibTableColumn
memBlocksAlloc = _MemBlocksAlloc_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 10, 1, 1, 7),
    _MemBlocksAlloc_Type()
)
memBlocksAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memBlocksAlloc.setStatus("current")


class _MemAvgBlockSizeAlloc_Type(Gauge32):
    """Custom type memAvgBlockSizeAlloc based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MemAvgBlockSizeAlloc_Type.__name__ = "Gauge32"
_MemAvgBlockSizeAlloc_Object = MibTableColumn
memAvgBlockSizeAlloc = _MemAvgBlockSizeAlloc_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 10, 1, 1, 8),
    _MemAvgBlockSizeAlloc_Type()
)
memAvgBlockSizeAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvgBlockSizeAlloc.setStatus("current")


class _MemTotalBytes_Type(Gauge32):
    """Custom type memTotalBytes based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MemTotalBytes_Type.__name__ = "Gauge32"
_MemTotalBytes_Object = MibTableColumn
memTotalBytes = _MemTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 10, 1, 1, 9),
    _MemTotalBytes_Type()
)
memTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalBytes.setStatus("current")


class _MemUtilization_Type(Gauge32):
    """Custom type memUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MemUtilization_Type.__name__ = "Gauge32"
_MemUtilization_Object = MibTableColumn
memUtilization = _MemUtilization_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 10, 1, 1, 10),
    _MemUtilization_Type()
)
memUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUtilization.setStatus("current")
if mibBuilder.loadTexts:
    memUtilization.setUnits("%")


class _CacheUtilization_Type(Gauge32):
    """Custom type cacheUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CacheUtilization_Type.__name__ = "Gauge32"
_CacheUtilization_Object = MibTableColumn
cacheUtilization = _CacheUtilization_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 10, 1, 1, 11),
    _CacheUtilization_Type()
)
cacheUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cacheUtilization.setStatus("current")
if mibBuilder.loadTexts:
    cacheUtilization.setUnits("%")
_MemKBytesFree_Type = Counter64
_MemKBytesFree_Object = MibTableColumn
memKBytesFree = _MemKBytesFree_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 10, 1, 1, 12),
    _MemKBytesFree_Type()
)
memKBytesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memKBytesFree.setStatus("current")
_MemKBytesAlloc_Type = Counter64
_MemKBytesAlloc_Object = MibTableColumn
memKBytesAlloc = _MemKBytesAlloc_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 10, 1, 1, 13),
    _MemKBytesAlloc_Type()
)
memKBytesAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memKBytesAlloc.setStatus("current")
_MemTotalKBytes_Type = Counter64
_MemTotalKBytes_Object = MibTableColumn
memTotalKBytes = _MemTotalKBytes_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 10, 1, 1, 14),
    _MemTotalKBytes_Type()
)
memTotalKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalKBytes.setStatus("current")

# Managed Objects groups


# Notification objects

hmITSysMemUtilizationAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 0, 5)
)
if mibBuilder.loadTexts:
    hmITSysMemUtilizationAlarm.setStatus(
        "current"
    )

hmITSysCpuUtilizationAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 0, 6)
)
if mibBuilder.loadTexts:
    hmITSysCpuUtilizationAlarm.setStatus(
        "current"
    )

hmITSysCacheUtilizationAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 0, 7)
)
if mibBuilder.loadTexts:
    hmITSysCacheUtilizationAlarm.setStatus(
        "current"
    )

hmITSysMpuCoreNormalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 0, 18)
)
if mibBuilder.loadTexts:
    hmITSysMpuCoreNormalAlarm.setStatus(
        "current"
    )

hmITSysMpuBoardWarnAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 0, 19)
)
if mibBuilder.loadTexts:
    hmITSysMpuBoardWarnAlarm.setStatus(
        "current"
    )

hmITSysMpuBoardNormalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3, 600, 0, 20)
)
if mibBuilder.loadTexts:
    hmITSysMpuBoardNormalAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HMIT-SYSTEM-MIB",
    **{"hmITSystemMib": hmITSystemMib,
       "hmITSystemTrap": hmITSystemTrap,
       "hmITSysMemUtilizationAlarm": hmITSysMemUtilizationAlarm,
       "hmITSysCpuUtilizationAlarm": hmITSysCpuUtilizationAlarm,
       "hmITSysCacheUtilizationAlarm": hmITSysCacheUtilizationAlarm,
       "hmITSysMpuCoreNormalAlarm": hmITSysMpuCoreNormalAlarm,
       "hmITSysMpuBoardWarnAlarm": hmITSysMpuBoardWarnAlarm,
       "hmITSysMpuBoardNormalAlarm": hmITSysMpuBoardNormalAlarm,
       "hmITSysInfoMib": hmITSysInfoMib,
       "sysVoltage": sysVoltage,
       "sysCurrent": sysCurrent,
       "hmITSysMpuMib": hmITSysMpuMib,
       "mpuInfoTable": mpuInfoTable,
       "mpuInfoEntry": mpuInfoEntry,
       "mpuIndex": mpuIndex,
       "mpuType": mpuType,
       "mpuDescription": mpuDescription,
       "mpuSerialNumber": mpuSerialNumber,
       "mpuSoftwareVersion": mpuSoftwareVersion,
       "mpuHardwareVersion": mpuHardwareVersion,
       "mpuFPGAVersion": mpuFPGAVersion,
       "mpuMonitorVersion": mpuMonitorVersion,
       "mpuCMMSoftwareVersion": mpuCMMSoftwareVersion,
       "mpuCMMHardwareVersion": mpuCMMHardwareVersion,
       "mpuCMMMonitorVersion": mpuCMMMonitorVersion,
       "mpuFlashTotalBytes": mpuFlashTotalBytes,
       "mpuFlashLeftBytes": mpuFlashLeftBytes,
       "mpuWorkingMode": mpuWorkingMode,
       "mpuOnlineStatus": mpuOnlineStatus,
       "mpuWorkingStatus": mpuWorkingStatus,
       "mpuPowerStatus": mpuPowerStatus,
       "mpuSynchronizationStatus": mpuSynchronizationStatus,
       "mpuCFStatus": mpuCFStatus,
       "mpuTemperature": mpuTemperature,
       "mpuSubSlotNumber": mpuSubSlotNumber,
       "hmITSysMpuUserSerialNumber": hmITSysMpuUserSerialNumber,
       "mpuModel": mpuModel,
       "hmITSysSubSlotMib": hmITSysSubSlotMib,
       "subSlotTable": subSlotTable,
       "subSlotEntry": subSlotEntry,
       "subSlotParentIndex": subSlotParentIndex,
       "subSlotIndex": subSlotIndex,
       "subSlotCardType": subSlotCardType,
       "subSlotPortNumber": subSlotPortNumber,
       "subSlotOnlineStatus": subSlotOnlineStatus,
       "hmITSysPortMib": hmITSysPortMib,
       "portInfoTable": portInfoTable,
       "portInfoEntry": portInfoEntry,
       "portSlotIndex": portSlotIndex,
       "portSubSlotIndex": portSubSlotIndex,
       "portIndex": portIndex,
       "portType": portType,
       "portLinkStatus": portLinkStatus,
       "portOnlineStatus": portOnlineStatus,
       "hmITSysPowerMib": hmITSysPowerMib,
       "powerInfoTable": powerInfoTable,
       "powerInfoEntry": powerInfoEntry,
       "powerIndex": powerIndex,
       "powerType": powerType,
       "powerDescription": powerDescription,
       "powerSerialNumber": powerSerialNumber,
       "powerCMMSoftwareVersion": powerCMMSoftwareVersion,
       "powerCMMHardwareVersion": powerCMMHardwareVersion,
       "powerCMMMonitorVersion": powerCMMMonitorVersion,
       "powerOnlineStatus": powerOnlineStatus,
       "powerWorkingStatus": powerWorkingStatus,
       "powerAlarmStatus": powerAlarmStatus,
       "powerVoltageInput": powerVoltageInput,
       "powerVoltageOutput": powerVoltageOutput,
       "powerCurrentInput": powerCurrentInput,
       "powerCurrentOutput": powerCurrentOutput,
       "powerUserSerialNumber": powerUserSerialNumber,
       "powerName": powerName,
       "hmITSysFanCardMib": hmITSysFanCardMib,
       "fanCardInfoTable": fanCardInfoTable,
       "fanCardInfoEntry": fanCardInfoEntry,
       "fanCardIndex": fanCardIndex,
       "fanCardDescription": fanCardDescription,
       "fanCardSerialNumber": fanCardSerialNumber,
       "fanCardCMMSoftwareVersion": fanCardCMMSoftwareVersion,
       "fanCardCMMHardwareVersion": fanCardCMMHardwareVersion,
       "fanCardCMMMonitorVersion": fanCardCMMMonitorVersion,
       "fanCardOnlineStatus": fanCardOnlineStatus,
       "fanCardWorkingStatus": fanCardWorkingStatus,
       "fanCardAlarmStatus": fanCardAlarmStatus,
       "fanCardGrps": fanCardGrps,
       "fanCardNumPerGrp": fanCardNumPerGrp,
       "fanCardUserSerialNumber": fanCardUserSerialNumber,
       "fanCardName": fanCardName,
       "fanInfoTable": fanInfoTable,
       "fanInfoEntry": fanInfoEntry,
       "fanInfoIndex": fanInfoIndex,
       "fanIndex": fanIndex,
       "fanStatus": fanStatus,
       "fanSpeed": fanSpeed,
       "hmITSysCpuMib": hmITSysCpuMib,
       "cpuUtilizationTable": cpuUtilizationTable,
       "cpuUtilizationEntry": cpuUtilizationEntry,
       "cpuIndex": cpuIndex,
       "cpuCoreId": cpuCoreId,
       "cpuCoreUtilization": cpuCoreUtilization,
       "cpuPeakUtilizationPerMinute": cpuPeakUtilizationPerMinute,
       "cpuTemperatureTable": cpuTemperatureTable,
       "cpuTemperatureEntry": cpuTemperatureEntry,
       "cpuTemperatureIndex": cpuTemperatureIndex,
       "cpuTemperature": cpuTemperature,
       "hmITSysMemoryMib": hmITSysMemoryMib,
       "memoryTable": memoryTable,
       "memoryEntry": memoryEntry,
       "memIndex": memIndex,
       "memBytesFree": memBytesFree,
       "memBlocksFree": memBlocksFree,
       "memAvgBlockSizeFree": memAvgBlockSizeFree,
       "memMaxBlockSizeFree": memMaxBlockSizeFree,
       "memBytesAlloc": memBytesAlloc,
       "memBlocksAlloc": memBlocksAlloc,
       "memAvgBlockSizeAlloc": memAvgBlockSizeAlloc,
       "memTotalBytes": memTotalBytes,
       "memUtilization": memUtilization,
       "cacheUtilization": cacheUtilization,
       "memKBytesFree": memKBytesFree,
       "memKBytesAlloc": memKBytesAlloc,
       "memTotalKBytes": memTotalKBytes}
)
