# SNMP MIB module (LEFTHAND-NETWORKS-NSM-STORAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/LEFTHAND-NETWORKS-NSM-STORAGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:41:20 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(lhnModules,
 lhnNsm) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-GLOBAL-REG-MIB",
    "lhnModules",
    "lhnNsm")

(lhnNsmStorage,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-NSM-MIB",
    "lhnNsmStorage")

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


# MODULE-IDENTITY

lhnNsmStorageModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 5)
)
if mibBuilder.loadTexts:
    lhnNsmStorageModule.setRevisions(
        ("2013-11-21 00:00",
         "2013-06-25 00:00",
         "2012-09-04 00:00",
         "2011-06-21 00:00",
         "2010-09-07 00:00",
         "2010-07-19 00:00",
         "2009-11-20 00:00",
         "2009-03-10 00:00",
         "2008-01-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LhnNsmStorageModuleConformance_ObjectIdentity = ObjectIdentity
lhnNsmStorageModuleConformance = _LhnNsmStorageModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 5, 1)
)
_LhnNsmStorageModuleCompliances_ObjectIdentity = ObjectIdentity
lhnNsmStorageModuleCompliances = _LhnNsmStorageModuleCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 5, 1, 1)
)
_LhnNsmStorageModuleGroups_ObjectIdentity = ObjectIdentity
lhnNsmStorageModuleGroups = _LhnNsmStorageModuleGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 5, 1, 2)
)
_StorageDeviceCount_Type = Integer32
_StorageDeviceCount_Object = MibScalar
storageDeviceCount = _StorageDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 1),
    _StorageDeviceCount_Type()
)
storageDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceCount.setStatus("current")
_StorageDeviceTable_Object = MibTable
storageDeviceTable = _StorageDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    storageDeviceTable.setStatus("current")
_StorageDeviceEntry_Object = MibTableRow
storageDeviceEntry = _StorageDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1)
)
storageDeviceEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceIndex"),
)
if mibBuilder.loadTexts:
    storageDeviceEntry.setStatus("current")
_StorageDeviceIndex_Type = Unsigned32
_StorageDeviceIndex_Object = MibTableColumn
storageDeviceIndex = _StorageDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 1),
    _StorageDeviceIndex_Type()
)
storageDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    storageDeviceIndex.setStatus("current")
_StorageDeviceModel_Type = DisplayString
_StorageDeviceModel_Object = MibTableColumn
storageDeviceModel = _StorageDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 2),
    _StorageDeviceModel_Type()
)
storageDeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceModel.setStatus("current")
_StorageDeviceClass_Type = DisplayString
_StorageDeviceClass_Object = MibTableColumn
storageDeviceClass = _StorageDeviceClass_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 3),
    _StorageDeviceClass_Type()
)
storageDeviceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceClass.setStatus("current")
_StorageDeviceCapacityInBytes_Type = CounterBasedGauge64
_StorageDeviceCapacityInBytes_Object = MibTableColumn
storageDeviceCapacityInBytes = _StorageDeviceCapacityInBytes_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 4),
    _StorageDeviceCapacityInBytes_Type()
)
storageDeviceCapacityInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceCapacityInBytes.setStatus("obsolete")
if mibBuilder.loadTexts:
    storageDeviceCapacityInBytes.setUnits("Blocks (512 bytes)")
_StorageDeviceMode_Type = DisplayString
_StorageDeviceMode_Object = MibTableColumn
storageDeviceMode = _StorageDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 5),
    _StorageDeviceMode_Type()
)
storageDeviceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceMode.setStatus("current")
_StorageDeviceChain_Type = DisplayString
_StorageDeviceChain_Object = MibTableColumn
storageDeviceChain = _StorageDeviceChain_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 6),
    _StorageDeviceChain_Type()
)
storageDeviceChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceChain.setStatus("obsolete")
_StorageDeviceSerialNumber_Type = DisplayString
_StorageDeviceSerialNumber_Object = MibTableColumn
storageDeviceSerialNumber = _StorageDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 7),
    _StorageDeviceSerialNumber_Type()
)
storageDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceSerialNumber.setStatus("current")
_StorageDeviceTemperature_Type = Gauge32
_StorageDeviceTemperature_Object = MibTableColumn
storageDeviceTemperature = _StorageDeviceTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 9),
    _StorageDeviceTemperature_Type()
)
storageDeviceTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceTemperature.setStatus("current")
if mibBuilder.loadTexts:
    storageDeviceTemperature.setUnits("Celsius")
_StorageDeviceTemperatureCritical_Type = Integer32
_StorageDeviceTemperatureCritical_Object = MibTableColumn
storageDeviceTemperatureCritical = _StorageDeviceTemperatureCritical_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 10),
    _StorageDeviceTemperatureCritical_Type()
)
storageDeviceTemperatureCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceTemperatureCritical.setStatus("current")
if mibBuilder.loadTexts:
    storageDeviceTemperatureCritical.setUnits("Celsius")
_StorageDeviceTemperatureLimit_Type = Integer32
_StorageDeviceTemperatureLimit_Object = MibTableColumn
storageDeviceTemperatureLimit = _StorageDeviceTemperatureLimit_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 11),
    _StorageDeviceTemperatureLimit_Type()
)
storageDeviceTemperatureLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceTemperatureLimit.setStatus("current")
if mibBuilder.loadTexts:
    storageDeviceTemperatureLimit.setUnits("Celsius")


class _StorageDeviceTemperatureStatus_Type(Integer32):
    """Custom type storageDeviceTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_StorageDeviceTemperatureStatus_Type.__name__ = "Integer32"
_StorageDeviceTemperatureStatus_Object = MibTableColumn
storageDeviceTemperatureStatus = _StorageDeviceTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 12),
    _StorageDeviceTemperatureStatus_Type()
)
storageDeviceTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceTemperatureStatus.setStatus("current")
_StorageDeviceLabel_Type = DisplayString
_StorageDeviceLabel_Object = MibTableColumn
storageDeviceLabel = _StorageDeviceLabel_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 13),
    _StorageDeviceLabel_Type()
)
storageDeviceLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceLabel.setStatus("current")
_StorageDeviceName_Type = DisplayString
_StorageDeviceName_Object = MibTableColumn
storageDeviceName = _StorageDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 14),
    _StorageDeviceName_Type()
)
storageDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceName.setStatus("current")
_StorageDeviceRaidDevice_Type = DisplayString
_StorageDeviceRaidDevice_Object = MibTableColumn
storageDeviceRaidDevice = _StorageDeviceRaidDevice_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 15),
    _StorageDeviceRaidDevice_Type()
)
storageDeviceRaidDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceRaidDevice.setStatus("current")
_StorageDeviceFirmwareVersion_Type = DisplayString
_StorageDeviceFirmwareVersion_Object = MibTableColumn
storageDeviceFirmwareVersion = _StorageDeviceFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 16),
    _StorageDeviceFirmwareVersion_Type()
)
storageDeviceFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceFirmwareVersion.setStatus("current")
_StorageDeviceSmartHealth_Type = DisplayString
_StorageDeviceSmartHealth_Object = MibTableColumn
storageDeviceSmartHealth = _StorageDeviceSmartHealth_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 17),
    _StorageDeviceSmartHealth_Type()
)
storageDeviceSmartHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceSmartHealth.setStatus("current")


class _StorageDeviceSmartHealthStatus_Type(Integer32):
    """Custom type storageDeviceSmartHealthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_StorageDeviceSmartHealthStatus_Type.__name__ = "Integer32"
_StorageDeviceSmartHealthStatus_Object = MibTableColumn
storageDeviceSmartHealthStatus = _StorageDeviceSmartHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 18),
    _StorageDeviceSmartHealthStatus_Type()
)
storageDeviceSmartHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceSmartHealthStatus.setStatus("current")
_StorageDeviceCapacity_Type = Integer32
_StorageDeviceCapacity_Object = MibTableColumn
storageDeviceCapacity = _StorageDeviceCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 19),
    _StorageDeviceCapacity_Type()
)
storageDeviceCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceCapacity.setStatus("current")
if mibBuilder.loadTexts:
    storageDeviceCapacity.setUnits("MB")
_StorageDeviceHotRemovable_Type = TruthValue
_StorageDeviceHotRemovable_Object = MibTableColumn
storageDeviceHotRemovable = _StorageDeviceHotRemovable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 20),
    _StorageDeviceHotRemovable_Type()
)
storageDeviceHotRemovable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceHotRemovable.setStatus("current")
_StorageDeviceState_Type = DisplayString
_StorageDeviceState_Object = MibTableColumn
storageDeviceState = _StorageDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 90),
    _StorageDeviceState_Type()
)
storageDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceState.setStatus("current")


class _StorageDeviceStatus_Type(Integer32):
    """Custom type storageDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_StorageDeviceStatus_Type.__name__ = "Integer32"
_StorageDeviceStatus_Object = MibTableColumn
storageDeviceStatus = _StorageDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 91),
    _StorageDeviceStatus_Type()
)
storageDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceStatus.setStatus("current")
_StorageDeviceRowStatus_Type = RowStatus
_StorageDeviceRowStatus_Object = MibTableColumn
storageDeviceRowStatus = _StorageDeviceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 2, 1, 99),
    _StorageDeviceRowStatus_Type()
)
storageDeviceRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDeviceRowStatus.setStatus("obsolete")
_StorageRaidCount_Type = Integer32
_StorageRaidCount_Object = MibScalar
storageRaidCount = _StorageRaidCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 3),
    _StorageRaidCount_Type()
)
storageRaidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidCount.setStatus("current")
_StorageRaidTable_Object = MibTable
storageRaidTable = _StorageRaidTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4)
)
if mibBuilder.loadTexts:
    storageRaidTable.setStatus("current")
_StorageRaidEntry_Object = MibTableRow
storageRaidEntry = _StorageRaidEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1)
)
storageRaidEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidIndex"),
)
if mibBuilder.loadTexts:
    storageRaidEntry.setStatus("current")
_StorageRaidIndex_Type = Unsigned32
_StorageRaidIndex_Object = MibTableColumn
storageRaidIndex = _StorageRaidIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 1),
    _StorageRaidIndex_Type()
)
storageRaidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    storageRaidIndex.setStatus("current")
_StorageRaidDeviceName_Type = DisplayString
_StorageRaidDeviceName_Object = MibTableColumn
storageRaidDeviceName = _StorageRaidDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 2),
    _StorageRaidDeviceName_Type()
)
storageRaidDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidDeviceName.setStatus("current")
_StorageRaidLevel_Type = DisplayString
_StorageRaidLevel_Object = MibTableColumn
storageRaidLevel = _StorageRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 3),
    _StorageRaidLevel_Type()
)
storageRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidLevel.setStatus("current")
_StorageRaidDiskCount_Type = Integer32
_StorageRaidDiskCount_Object = MibTableColumn
storageRaidDiskCount = _StorageRaidDiskCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 4),
    _StorageRaidDiskCount_Type()
)
storageRaidDiskCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidDiskCount.setStatus("current")
_StorageRaidSpareDiskCount_Type = Integer32
_StorageRaidSpareDiskCount_Object = MibTableColumn
storageRaidSpareDiskCount = _StorageRaidSpareDiskCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 5),
    _StorageRaidSpareDiskCount_Type()
)
storageRaidSpareDiskCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidSpareDiskCount.setStatus("obsolete")
_StorageRaidSuperBlock_Type = TruthValue
_StorageRaidSuperBlock_Object = MibTableColumn
storageRaidSuperBlock = _StorageRaidSuperBlock_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 6),
    _StorageRaidSuperBlock_Type()
)
storageRaidSuperBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidSuperBlock.setStatus("obsolete")
_StorageRaidChunkSize_Type = Integer32
_StorageRaidChunkSize_Object = MibTableColumn
storageRaidChunkSize = _StorageRaidChunkSize_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 7),
    _StorageRaidChunkSize_Type()
)
storageRaidChunkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidChunkSize.setStatus("obsolete")
if mibBuilder.loadTexts:
    storageRaidChunkSize.setUnits("Kbytes")
_StorageRaidDisks_Type = DisplayString
_StorageRaidDisks_Object = MibTableColumn
storageRaidDisks = _StorageRaidDisks_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 8),
    _StorageRaidDisks_Type()
)
storageRaidDisks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidDisks.setStatus("current")
_StorageRaidDevice_Type = DisplayString
_StorageRaidDevice_Object = MibTableColumn
storageRaidDevice = _StorageRaidDevice_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 9),
    _StorageRaidDevice_Type()
)
storageRaidDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidDevice.setStatus("current")
_StorageRaidDeviceCapacity_Type = Integer32
_StorageRaidDeviceCapacity_Object = MibTableColumn
storageRaidDeviceCapacity = _StorageRaidDeviceCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 10),
    _StorageRaidDeviceCapacity_Type()
)
storageRaidDeviceCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidDeviceCapacity.setStatus("current")
if mibBuilder.loadTexts:
    storageRaidDeviceCapacity.setUnits("MB")
_StorageRaidDeviceParityInitState_Type = DisplayString
_StorageRaidDeviceParityInitState_Object = MibTableColumn
storageRaidDeviceParityInitState = _StorageRaidDeviceParityInitState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 11),
    _StorageRaidDeviceParityInitState_Type()
)
storageRaidDeviceParityInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidDeviceParityInitState.setStatus("current")
_StorageRaidRebuildPercent_Type = Gauge32
_StorageRaidRebuildPercent_Object = MibTableColumn
storageRaidRebuildPercent = _StorageRaidRebuildPercent_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 12),
    _StorageRaidRebuildPercent_Type()
)
storageRaidRebuildPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidRebuildPercent.setStatus("current")
if mibBuilder.loadTexts:
    storageRaidRebuildPercent.setUnits("%")
_StorageRaidRebuildTime_Type = Gauge32
_StorageRaidRebuildTime_Object = MibTableColumn
storageRaidRebuildTime = _StorageRaidRebuildTime_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 13),
    _StorageRaidRebuildTime_Type()
)
storageRaidRebuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidRebuildTime.setStatus("current")
if mibBuilder.loadTexts:
    storageRaidRebuildTime.setUnits("minutes")
_StorageRaidDeviceState_Type = DisplayString
_StorageRaidDeviceState_Object = MibTableColumn
storageRaidDeviceState = _StorageRaidDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 90),
    _StorageRaidDeviceState_Type()
)
storageRaidDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidDeviceState.setStatus("current")


class _StorageRaidDeviceStatus_Type(Integer32):
    """Custom type storageRaidDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_StorageRaidDeviceStatus_Type.__name__ = "Integer32"
_StorageRaidDeviceStatus_Object = MibTableColumn
storageRaidDeviceStatus = _StorageRaidDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 91),
    _StorageRaidDeviceStatus_Type()
)
storageRaidDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidDeviceStatus.setStatus("current")
_StorageRaidDeviceRowStatus_Type = RowStatus
_StorageRaidDeviceRowStatus_Object = MibTableColumn
storageRaidDeviceRowStatus = _StorageRaidDeviceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 4, 1, 99),
    _StorageRaidDeviceRowStatus_Type()
)
storageRaidDeviceRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidDeviceRowStatus.setStatus("obsolete")
_StorageRaidDescription_Type = DisplayString
_StorageRaidDescription_Object = MibScalar
storageRaidDescription = _StorageRaidDescription_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 5),
    _StorageRaidDescription_Type()
)
storageRaidDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidDescription.setStatus("current")
_StorageRaidMode_Type = DisplayString
_StorageRaidMode_Object = MibScalar
storageRaidMode = _StorageRaidMode_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 7),
    _StorageRaidMode_Type()
)
storageRaidMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidMode.setStatus("current")
_StorageRaidCapacity_Type = Integer32
_StorageRaidCapacity_Object = MibScalar
storageRaidCapacity = _StorageRaidCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 8),
    _StorageRaidCapacity_Type()
)
storageRaidCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidCapacity.setStatus("current")
if mibBuilder.loadTexts:
    storageRaidCapacity.setUnits("MB")


class _StorageRaidStatus_Type(Integer32):
    """Custom type storageRaidStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_StorageRaidStatus_Type.__name__ = "Integer32"
_StorageRaidStatus_Object = MibScalar
storageRaidStatus = _StorageRaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 11),
    _StorageRaidStatus_Type()
)
storageRaidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidStatus.setStatus("current")
_StorageRaidState_Type = DisplayString
_StorageRaidState_Object = MibScalar
storageRaidState = _StorageRaidState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 12),
    _StorageRaidState_Type()
)
storageRaidState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidState.setStatus("current")
_StorageRaidMinimumSpeed_Type = DisplayString
_StorageRaidMinimumSpeed_Object = MibScalar
storageRaidMinimumSpeed = _StorageRaidMinimumSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 13),
    _StorageRaidMinimumSpeed_Type()
)
storageRaidMinimumSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidMinimumSpeed.setStatus("current")
_StorageRaidMaximumSpeed_Type = DisplayString
_StorageRaidMaximumSpeed_Object = MibScalar
storageRaidMaximumSpeed = _StorageRaidMaximumSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 14),
    _StorageRaidMaximumSpeed_Type()
)
storageRaidMaximumSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidMaximumSpeed.setStatus("current")


class _StorageRaidParityInitState_Type(Integer32):
    """Custom type storageRaidParityInitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("complete", 1),
          ("inProgress", 2),
          ("notApplicable", 3))
    )


_StorageRaidParityInitState_Type.__name__ = "Integer32"
_StorageRaidParityInitState_Object = MibScalar
storageRaidParityInitState = _StorageRaidParityInitState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 15),
    _StorageRaidParityInitState_Type()
)
storageRaidParityInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidParityInitState.setStatus("obsolete")
_StorageRaidStatsIOsRead_Type = Counter64
_StorageRaidStatsIOsRead_Object = MibScalar
storageRaidStatsIOsRead = _StorageRaidStatsIOsRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 16),
    _StorageRaidStatsIOsRead_Type()
)
storageRaidStatsIOsRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidStatsIOsRead.setStatus("current")
if mibBuilder.loadTexts:
    storageRaidStatsIOsRead.setUnits("operations")
_StorageRaidStatsIOsWrite_Type = Counter64
_StorageRaidStatsIOsWrite_Object = MibScalar
storageRaidStatsIOsWrite = _StorageRaidStatsIOsWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 17),
    _StorageRaidStatsIOsWrite_Type()
)
storageRaidStatsIOsWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidStatsIOsWrite.setStatus("current")
if mibBuilder.loadTexts:
    storageRaidStatsIOsWrite.setUnits("operations")
_StorageRaidStatsKbytesRead_Type = Counter64
_StorageRaidStatsKbytesRead_Object = MibScalar
storageRaidStatsKbytesRead = _StorageRaidStatsKbytesRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 19),
    _StorageRaidStatsKbytesRead_Type()
)
storageRaidStatsKbytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidStatsKbytesRead.setStatus("current")
if mibBuilder.loadTexts:
    storageRaidStatsKbytesRead.setUnits("kB")
_StorageRaidStatsKbytesWrite_Type = Counter64
_StorageRaidStatsKbytesWrite_Object = MibScalar
storageRaidStatsKbytesWrite = _StorageRaidStatsKbytesWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 20),
    _StorageRaidStatsKbytesWrite_Type()
)
storageRaidStatsKbytesWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidStatsKbytesWrite.setStatus("current")
if mibBuilder.loadTexts:
    storageRaidStatsKbytesWrite.setUnits("kB")
_StorageRaidStatsQDepthTotal_Type = Gauge32
_StorageRaidStatsQDepthTotal_Object = MibScalar
storageRaidStatsQDepthTotal = _StorageRaidStatsQDepthTotal_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 22),
    _StorageRaidStatsQDepthTotal_Type()
)
storageRaidStatsQDepthTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidStatsQDepthTotal.setStatus("current")
if mibBuilder.loadTexts:
    storageRaidStatsQDepthTotal.setUnits("operations")
_StorageRaidStatsIoLatencyRead_Type = Counter64
_StorageRaidStatsIoLatencyRead_Object = MibScalar
storageRaidStatsIoLatencyRead = _StorageRaidStatsIoLatencyRead_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 23),
    _StorageRaidStatsIoLatencyRead_Type()
)
storageRaidStatsIoLatencyRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidStatsIoLatencyRead.setStatus("current")
if mibBuilder.loadTexts:
    storageRaidStatsIoLatencyRead.setUnits("ms")
_StorageRaidStatsIoLatencyWrite_Type = Counter64
_StorageRaidStatsIoLatencyWrite_Object = MibScalar
storageRaidStatsIoLatencyWrite = _StorageRaidStatsIoLatencyWrite_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 24),
    _StorageRaidStatsIoLatencyWrite_Type()
)
storageRaidStatsIoLatencyWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageRaidStatsIoLatencyWrite.setStatus("current")
if mibBuilder.loadTexts:
    storageRaidStatsIoLatencyWrite.setUnits("ms")
_StorageOsRaidCount_Type = Integer32
_StorageOsRaidCount_Object = MibScalar
storageOsRaidCount = _StorageOsRaidCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 50),
    _StorageOsRaidCount_Type()
)
storageOsRaidCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageOsRaidCount.setStatus("current")
_StorageOsRaidTable_Object = MibTable
storageOsRaidTable = _StorageOsRaidTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 51)
)
if mibBuilder.loadTexts:
    storageOsRaidTable.setStatus("current")
_StorageOsRaidEntry_Object = MibTableRow
storageOsRaidEntry = _StorageOsRaidEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 51, 1)
)
storageOsRaidEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageOsRaidIndex"),
)
if mibBuilder.loadTexts:
    storageOsRaidEntry.setStatus("current")
_StorageOsRaidIndex_Type = Unsigned32
_StorageOsRaidIndex_Object = MibTableColumn
storageOsRaidIndex = _StorageOsRaidIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 51, 1, 1),
    _StorageOsRaidIndex_Type()
)
storageOsRaidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    storageOsRaidIndex.setStatus("current")
_StorageOsRaidName_Type = DisplayString
_StorageOsRaidName_Object = MibTableColumn
storageOsRaidName = _StorageOsRaidName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 51, 1, 2),
    _StorageOsRaidName_Type()
)
storageOsRaidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageOsRaidName.setStatus("current")
_StorageOsRaidDevice_Type = DisplayString
_StorageOsRaidDevice_Object = MibTableColumn
storageOsRaidDevice = _StorageOsRaidDevice_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 51, 1, 3),
    _StorageOsRaidDevice_Type()
)
storageOsRaidDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageOsRaidDevice.setStatus("current")
_StorageOsRaidMode_Type = DisplayString
_StorageOsRaidMode_Object = MibTableColumn
storageOsRaidMode = _StorageOsRaidMode_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 51, 1, 4),
    _StorageOsRaidMode_Type()
)
storageOsRaidMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageOsRaidMode.setStatus("obsolete")
_StorageOsRaidSize_Type = Integer32
_StorageOsRaidSize_Object = MibTableColumn
storageOsRaidSize = _StorageOsRaidSize_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 51, 1, 5),
    _StorageOsRaidSize_Type()
)
storageOsRaidSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageOsRaidSize.setStatus("current")
if mibBuilder.loadTexts:
    storageOsRaidSize.setUnits("MB")
_StorageOsRaidState_Type = DisplayString
_StorageOsRaidState_Object = MibTableColumn
storageOsRaidState = _StorageOsRaidState_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 51, 1, 90),
    _StorageOsRaidState_Type()
)
storageOsRaidState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageOsRaidState.setStatus("current")
_StorageOsRaidRowStatus_Type = RowStatus
_StorageOsRaidRowStatus_Object = MibTableColumn
storageOsRaidRowStatus = _StorageOsRaidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 4, 51, 1, 99),
    _StorageOsRaidRowStatus_Type()
)
storageOsRaidRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageOsRaidRowStatus.setStatus("obsolete")

# Managed Objects groups

lefthandNetworksNsmStorageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 5, 1, 2, 1)
)
lefthandNetworksNsmStorageGroup.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceCount"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceModel"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceClass"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceMode"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceSerialNumber"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceTemperature"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceTemperatureCritical"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceTemperatureLimit"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceTemperatureStatus"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceLabel"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceName"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceRaidDevice"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceFirmwareVersion"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceSmartHealth"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceSmartHealthStatus"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceCapacity"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceHotRemovable"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceState"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceStatus"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidCount"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidDeviceName"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidLevel"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidDiskCount"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidDisks"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidDevice"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidDeviceCapacity"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidDeviceParityInitState"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidRebuildPercent"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidRebuildTime"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidDeviceState"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidDeviceStatus"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidDescription"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidMode"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidCapacity"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidStatus"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidState"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidMinimumSpeed"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidMaximumSpeed"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidStatsIOsRead"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidStatsIOsWrite"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidStatsKbytesRead"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidStatsKbytesWrite"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidStatsQDepthTotal"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidStatsIoLatencyRead"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidStatsIoLatencyWrite"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageOsRaidCount"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageOsRaidName"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageOsRaidDevice"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageOsRaidSize"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageOsRaidState"))
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmStorageGroup.setStatus("current")

lefthandNetworksNsmStorageGroupObsolete = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 5, 1, 2, 2)
)
lefthandNetworksNsmStorageGroupObsolete.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceCapacityInBytes"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceChain"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageDeviceRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidSpareDiskCount"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidSuperBlock"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidChunkSize"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidParityInitState"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageRaidDeviceRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageOsRaidMode"),
        ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "storageOsRaidRowStatus"))
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmStorageGroupObsolete.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lefthandNetworksNsmStorageMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 5, 1, 1, 1)
)
lefthandNetworksNsmStorageMibCompliance.setObjects(
    ("LEFTHAND-NETWORKS-NSM-STORAGE-MIB", "lefthandNetworksNsmStorageGroup")
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmStorageMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NSM-STORAGE-MIB",
    **{"lhnNsmStorageModule": lhnNsmStorageModule,
       "lhnNsmStorageModuleConformance": lhnNsmStorageModuleConformance,
       "lhnNsmStorageModuleCompliances": lhnNsmStorageModuleCompliances,
       "lefthandNetworksNsmStorageMibCompliance": lefthandNetworksNsmStorageMibCompliance,
       "lhnNsmStorageModuleGroups": lhnNsmStorageModuleGroups,
       "lefthandNetworksNsmStorageGroup": lefthandNetworksNsmStorageGroup,
       "lefthandNetworksNsmStorageGroupObsolete": lefthandNetworksNsmStorageGroupObsolete,
       "storageDeviceCount": storageDeviceCount,
       "storageDeviceTable": storageDeviceTable,
       "storageDeviceEntry": storageDeviceEntry,
       "storageDeviceIndex": storageDeviceIndex,
       "storageDeviceModel": storageDeviceModel,
       "storageDeviceClass": storageDeviceClass,
       "storageDeviceCapacityInBytes": storageDeviceCapacityInBytes,
       "storageDeviceMode": storageDeviceMode,
       "storageDeviceChain": storageDeviceChain,
       "storageDeviceSerialNumber": storageDeviceSerialNumber,
       "storageDeviceTemperature": storageDeviceTemperature,
       "storageDeviceTemperatureCritical": storageDeviceTemperatureCritical,
       "storageDeviceTemperatureLimit": storageDeviceTemperatureLimit,
       "storageDeviceTemperatureStatus": storageDeviceTemperatureStatus,
       "storageDeviceLabel": storageDeviceLabel,
       "storageDeviceName": storageDeviceName,
       "storageDeviceRaidDevice": storageDeviceRaidDevice,
       "storageDeviceFirmwareVersion": storageDeviceFirmwareVersion,
       "storageDeviceSmartHealth": storageDeviceSmartHealth,
       "storageDeviceSmartHealthStatus": storageDeviceSmartHealthStatus,
       "storageDeviceCapacity": storageDeviceCapacity,
       "storageDeviceHotRemovable": storageDeviceHotRemovable,
       "storageDeviceState": storageDeviceState,
       "storageDeviceStatus": storageDeviceStatus,
       "storageDeviceRowStatus": storageDeviceRowStatus,
       "storageRaidCount": storageRaidCount,
       "storageRaidTable": storageRaidTable,
       "storageRaidEntry": storageRaidEntry,
       "storageRaidIndex": storageRaidIndex,
       "storageRaidDeviceName": storageRaidDeviceName,
       "storageRaidLevel": storageRaidLevel,
       "storageRaidDiskCount": storageRaidDiskCount,
       "storageRaidSpareDiskCount": storageRaidSpareDiskCount,
       "storageRaidSuperBlock": storageRaidSuperBlock,
       "storageRaidChunkSize": storageRaidChunkSize,
       "storageRaidDisks": storageRaidDisks,
       "storageRaidDevice": storageRaidDevice,
       "storageRaidDeviceCapacity": storageRaidDeviceCapacity,
       "storageRaidDeviceParityInitState": storageRaidDeviceParityInitState,
       "storageRaidRebuildPercent": storageRaidRebuildPercent,
       "storageRaidRebuildTime": storageRaidRebuildTime,
       "storageRaidDeviceState": storageRaidDeviceState,
       "storageRaidDeviceStatus": storageRaidDeviceStatus,
       "storageRaidDeviceRowStatus": storageRaidDeviceRowStatus,
       "storageRaidDescription": storageRaidDescription,
       "storageRaidMode": storageRaidMode,
       "storageRaidCapacity": storageRaidCapacity,
       "storageRaidStatus": storageRaidStatus,
       "storageRaidState": storageRaidState,
       "storageRaidMinimumSpeed": storageRaidMinimumSpeed,
       "storageRaidMaximumSpeed": storageRaidMaximumSpeed,
       "storageRaidParityInitState": storageRaidParityInitState,
       "storageRaidStatsIOsRead": storageRaidStatsIOsRead,
       "storageRaidStatsIOsWrite": storageRaidStatsIOsWrite,
       "storageRaidStatsKbytesRead": storageRaidStatsKbytesRead,
       "storageRaidStatsKbytesWrite": storageRaidStatsKbytesWrite,
       "storageRaidStatsQDepthTotal": storageRaidStatsQDepthTotal,
       "storageRaidStatsIoLatencyRead": storageRaidStatsIoLatencyRead,
       "storageRaidStatsIoLatencyWrite": storageRaidStatsIoLatencyWrite,
       "storageOsRaidCount": storageOsRaidCount,
       "storageOsRaidTable": storageOsRaidTable,
       "storageOsRaidEntry": storageOsRaidEntry,
       "storageOsRaidIndex": storageOsRaidIndex,
       "storageOsRaidName": storageOsRaidName,
       "storageOsRaidDevice": storageOsRaidDevice,
       "storageOsRaidMode": storageOsRaidMode,
       "storageOsRaidSize": storageOsRaidSize,
       "storageOsRaidState": storageOsRaidState,
       "storageOsRaidRowStatus": storageOsRaidRowStatus}
)
